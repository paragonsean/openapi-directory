# RoomsApi

All URIs are relative to *https://api.hetras-certification.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**roomsGetAvailableRooms**](RoomsApi.md#roomsGetAvailableRooms) | **GET** /api/hotel/v0/hotels/{hotelId}/rooms/available | Request available rooms using a given criteria. |
| [**roomsGetRoom**](RoomsApi.md#roomsGetRoom) | **GET** /api/hotel/v0/hotels/{hotelId}/rooms/{roomNumber} | Get all the details for a specific room in the hotel. |
| [**roomsGetRooms**](RoomsApi.md#roomsGetRooms) | **GET** /api/hotel/v0/hotels/{hotelId}/rooms | Get a list of rooms using the provided filtering and pagination criteria. |
| [**roomsGetRoomsCount**](RoomsApi.md#roomsGetRoomsCount) | **GET** /api/hotel/v0/hotels/{hotelId}/rooms/$count | Get the count of all rooms in the hotel matching the given filter criteria. |
| [**roomsPatchRoom**](RoomsApi.md#roomsPatchRoom) | **PATCH** /api/hotel/v0/hotels/{hotelId}/rooms/{roomNumber} | Partially updates a room. |


<a id="roomsGetAvailableRooms"></a>
# **roomsGetAvailableRooms**
> RoomListResponse roomsGetAvailableRooms(appId, appKey, hotelId, from, to, adults, includeOutOfService, roomTypes, amenities, views, locations, skip, top, inlinecount)

Request available rooms using a given criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoomsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RoomsApi apiInstance = new RoomsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel you are looking for available rooms.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Rooms returned will not be assigned to a reservation or be under maintenance between this date              and the specified to date. Still there could be departing reservations or ending maintenances              for this date.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | Rooms returned will not be assigned to a reservation or be under maintenance between the specified              from date and this date. Still there could be arriving reservations or beginning maintenances              for this date.
    byte[] adults = null; // byte[] | Specifies number of adults the returned rooms will have to be able to house. The default value is 1.
    Boolean includeOutOfService = true; // Boolean | Should rooms that are set OutOfService in the defined time period be returned as available. By default              they are not.
    List<String> roomTypes = Arrays.asList(); // List<String> | Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types.
    List<String> amenities = Arrays.asList(); // List<String> | Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes.
    List<String> views = Arrays.asList(); // List<String> | Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes.
    List<String> locations = Arrays.asList(); // List<String> | Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes.
    Integer skip = 56; // Integer | Amount of items to skip.
    Integer top = 56; // Integer | Amount of items to select.
    String inlinecount = "None"; // String | Return total number of items for a given filter criteria.
    try {
      RoomListResponse result = apiInstance.roomsGetAvailableRooms(appId, appKey, hotelId, from, to, adults, includeOutOfService, roomTypes, amenities, views, locations, skip, top, inlinecount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoomsApi#roomsGetAvailableRooms");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**| Application identifier | |
| **appKey** | **String**| Application key. | |
| **hotelId** | **Integer**| The hotel you are looking for available rooms. | |
| **from** | **OffsetDateTime**| Rooms returned will not be assigned to a reservation or be under maintenance between this date              and the specified to date. Still there could be departing reservations or ending maintenances              for this date. | |
| **to** | **OffsetDateTime**| Rooms returned will not be assigned to a reservation or be under maintenance between the specified              from date and this date. Still there could be arriving reservations or beginning maintenances              for this date. | |
| **adults** | **byte[]**| Specifies number of adults the returned rooms will have to be able to house. The default value is 1. | [optional] |
| **includeOutOfService** | **Boolean**| Should rooms that are set OutOfService in the defined time period be returned as available. By default              they are not. | [optional] |
| **roomTypes** | [**List&lt;String&gt;**](String.md)| Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types. | [optional] |
| **amenities** | [**List&lt;String&gt;**](String.md)| Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes. | [optional] |
| **views** | [**List&lt;String&gt;**](String.md)| Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes. | [optional] |
| **locations** | [**List&lt;String&gt;**](String.md)| Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes. | [optional] |
| **skip** | **Integer**| Amount of items to skip. | [optional] |
| **top** | **Integer**| Amount of items to select. | [optional] |
| **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] [enum: None, AllPages] |

### Return type

[**RoomListResponse**](RoomListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of available rooms in the specified time period. |  -  |
| **204** | There are no available rooms found for the given criteria. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI or the requested room could not be found. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="roomsGetRoom"></a>
# **roomsGetRoom**
> Room roomsGetRoom(appId, appKey, hotelId, roomNumber)

Get all the details for a specific room in the hotel.

With this call you can load the details about a specific room in the hotel. It will show you the current status of the room.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoomsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RoomsApi apiInstance = new RoomsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id the room belongs to.
    String roomNumber = "roomNumber_example"; // String | The room number you want to see details for.
    try {
      Room result = apiInstance.roomsGetRoom(appId, appKey, hotelId, roomNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoomsApi#roomsGetRoom");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**| Application identifier | |
| **appKey** | **String**| Application key. | |
| **hotelId** | **Integer**| The hotel id the room belongs to. | |
| **roomNumber** | **String**| The room number you want to see details for. | |

### Return type

[**Room**](Room.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Room details for the given room and hotel. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI or the requested room could not be found. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="roomsGetRooms"></a>
# **roomsGetRooms**
> RoomListResponse roomsGetRooms(appId, appKey, hotelId, occupancy, conditions, maintenances, roomTypes, amenities, views, locations, skip, top, inlinecount)

Get a list of rooms using the provided filtering and pagination criteria.

Find all rooms for the hotel that match the specified filter criteria. The filtering will be done based on the current state of              the rooms.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoomsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RoomsApi apiInstance = new RoomsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel you are trying to find rooms for.
    String occupancy = "Occupied"; // String | Return results only for rooms that have the given frontdesk ocuppancy status.
    List<String> conditions = Arrays.asList(); // List<String> | Return results only for rooms that have the given room condition status.
    List<String> maintenances = Arrays.asList(); // List<String> | Return results only for rooms that have the given maintenance status.
    List<String> roomTypes = Arrays.asList(); // List<String> | Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types.
    List<String> amenities = Arrays.asList(); // List<String> | Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes.
    List<String> views = Arrays.asList(); // List<String> | Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes.
    List<String> locations = Arrays.asList(); // List<String> | Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes.
    Integer skip = 56; // Integer | Amount of items to skip.
    Integer top = 56; // Integer | Amount of items to select.
    String inlinecount = "None"; // String | Return total number of items for a given filter criteria.
    try {
      RoomListResponse result = apiInstance.roomsGetRooms(appId, appKey, hotelId, occupancy, conditions, maintenances, roomTypes, amenities, views, locations, skip, top, inlinecount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoomsApi#roomsGetRooms");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**| Application identifier | |
| **appKey** | **String**| Application key. | |
| **hotelId** | **Integer**| The hotel you are trying to find rooms for. | |
| **occupancy** | **String**| Return results only for rooms that have the given frontdesk ocuppancy status. | [optional] [enum: Occupied, Vacant] |
| **conditions** | [**List&lt;String&gt;**](String.md)| Return results only for rooms that have the given room condition status. | [optional] [enum: CleanNotInspected, Clean, Dirty] |
| **maintenances** | [**List&lt;String&gt;**](String.md)| Return results only for rooms that have the given maintenance status. | [optional] [enum: NotSet, None, OutOfInventory, OutOfOrder, OutOfService] |
| **roomTypes** | [**List&lt;String&gt;**](String.md)| Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types. | [optional] |
| **amenities** | [**List&lt;String&gt;**](String.md)| Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes. | [optional] |
| **views** | [**List&lt;String&gt;**](String.md)| Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes. | [optional] |
| **locations** | [**List&lt;String&gt;**](String.md)| Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes. | [optional] |
| **skip** | **Integer**| Amount of items to skip. | [optional] |
| **top** | **Integer**| Amount of items to select. | [optional] |
| **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] [enum: None, AllPages] |

### Return type

[**RoomListResponse**](RoomListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of rooms for the hotel based on the set filter criteria. |  -  |
| **204** | There are no rooms found for the given filtering and pagination criteria. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI or the requested room could not be found. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="roomsGetRoomsCount"></a>
# **roomsGetRoomsCount**
> TotalCountResponse roomsGetRoomsCount(appId, appKey, hotelId, occupancy, conditions, maintenances, roomTypes, amenities, views, locations)

Get the count of all rooms in the hotel matching the given filter criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoomsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RoomsApi apiInstance = new RoomsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel you are counting the rooms for.
    String occupancy = "Occupied"; // String | Return results only for rooms that have the given frontdesk ocuppancy status.
    List<String> conditions = Arrays.asList(); // List<String> | Return results only for rooms that have the given room condition status.
    List<String> maintenances = Arrays.asList(); // List<String> | Return results only for rooms that have the given maintenance status.
    List<String> roomTypes = Arrays.asList(); // List<String> | Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types.
    List<String> amenities = Arrays.asList(); // List<String> | Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes.
    List<String> views = Arrays.asList(); // List<String> | Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes.
    List<String> locations = Arrays.asList(); // List<String> | Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes.
    try {
      TotalCountResponse result = apiInstance.roomsGetRoomsCount(appId, appKey, hotelId, occupancy, conditions, maintenances, roomTypes, amenities, views, locations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoomsApi#roomsGetRoomsCount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**| Application identifier | |
| **appKey** | **String**| Application key. | |
| **hotelId** | **Integer**| The hotel you are counting the rooms for. | |
| **occupancy** | **String**| Return results only for rooms that have the given frontdesk ocuppancy status. | [optional] [enum: Occupied, Vacant] |
| **conditions** | [**List&lt;String&gt;**](String.md)| Return results only for rooms that have the given room condition status. | [optional] [enum: CleanNotInspected, Clean, Dirty] |
| **maintenances** | [**List&lt;String&gt;**](String.md)| Return results only for rooms that have the given maintenance status. | [optional] [enum: NotSet, None, OutOfInventory, OutOfOrder, OutOfService] |
| **roomTypes** | [**List&lt;String&gt;**](String.md)| Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types. | [optional] |
| **amenities** | [**List&lt;String&gt;**](String.md)| Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes. | [optional] |
| **views** | [**List&lt;String&gt;**](String.md)| Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes. | [optional] |
| **locations** | [**List&lt;String&gt;**](String.md)| Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes. | [optional] |

### Return type

[**TotalCountResponse**](TotalCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The room count in the hotel matching the given filter criteria. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI or the requested room could not be found. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="roomsPatchRoom"></a>
# **roomsPatchRoom**
> Object roomsPatchRoom(appId, appKey, hotelId, roomNumber, patchRequest)

Partially updates a room.

The hetras API is using this &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/patch\&quot; onfocus&#x3D;\&quot;this.blur()\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Patch Specification&lt;/a&gt;              to partially update an existing resource. Currently this call only allows to modify condition and housekeeping occupancy status of the room.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/status/condition\&quot;, \&quot;value\&quot;: \&quot;CleanNotInspected\&quot;                }, {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/status/housekeeping_occupancy\&quot;, \&quot;value\&quot;: \&quot;Vacant\&quot;                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.&lt;br /&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoomsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RoomsApi apiInstance = new RoomsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id the room belongs to.
    String roomNumber = "roomNumber_example"; // String | The room number of the room you would like to update.
    List<OperationRoomPatchRequest> patchRequest = Arrays.asList(); // List<OperationRoomPatchRequest> | A set of JSON Patch operations.
    try {
      Object result = apiInstance.roomsPatchRoom(appId, appKey, hotelId, roomNumber, patchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoomsApi#roomsPatchRoom");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**| Application identifier | |
| **appKey** | **String**| Application key. | |
| **hotelId** | **Integer**| The hotel id the room belongs to. | |
| **roomNumber** | **String**| The room number of the room you would like to update. | |
| **patchRequest** | [**List&lt;OperationRoomPatchRequest&gt;**](OperationRoomPatchRequest.md)| A set of JSON Patch operations. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The update was successful |  -  |
| **400** | Bad request. Request body erroneous. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

