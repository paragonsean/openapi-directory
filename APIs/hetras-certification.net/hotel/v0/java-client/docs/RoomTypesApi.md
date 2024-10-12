# RoomTypesApi

All URIs are relative to *https://api.hetras-certification.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**roomTypesGetRoomType**](RoomTypesApi.md#roomTypesGetRoomType) | **GET** /api/hotel/v0/hotels/{hotelId}/room_types/{code} | Get all the details for a specific room type in the hotel. |
| [**roomTypesGetRoomTypes**](RoomTypesApi.md#roomTypesGetRoomTypes) | **GET** /api/hotel/v0/hotels/{hotelId}/room_types | Get a list with the details of all room types for for the specified hotel id. |


<a id="roomTypesGetRoomType"></a>
# **roomTypesGetRoomType**
> RoomType roomTypesGetRoomType(appId, appKey, hotelId, code)

Get all the details for a specific room type in the hotel.

With this call you can load the details about a specific room type in the hotel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoomTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RoomTypesApi apiInstance = new RoomTypesApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id the room type belongs to.
    String code = "code_example"; // String | The code of the room type you want to see details for.
    try {
      RoomType result = apiInstance.roomTypesGetRoomType(appId, appKey, hotelId, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoomTypesApi#roomTypesGetRoomType");
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
| **hotelId** | **Integer**| The hotel id the room type belongs to. | |
| **code** | **String**| The code of the room type you want to see details for. | |

### Return type

[**RoomType**](RoomType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Room type details for the given room and hotel. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI or the requested room could not be found. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="roomTypesGetRoomTypes"></a>
# **roomTypesGetRoomTypes**
> List&lt;RoomType&gt; roomTypesGetRoomTypes(appId, appKey, hotelId)

Get a list with the details of all room types for for the specified hotel id.

With this call you can load the details about a all available room types for the specified hotel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoomTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RoomTypesApi apiInstance = new RoomTypesApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id the room type belongs to.
    try {
      List<RoomType> result = apiInstance.roomTypesGetRoomTypes(appId, appKey, hotelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoomTypesApi#roomTypesGetRoomTypes");
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
| **hotelId** | **Integer**| The hotel id the room type belongs to. | |

### Return type

[**List&lt;RoomType&gt;**](RoomType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of room types for the given hotel. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI or the requested room could not be found. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

