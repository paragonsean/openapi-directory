# StopsApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**stopsStopDetails**](StopsApi.md#stopsStopDetails) | **GET** /v3/stops/{stop_id}/route_type/{route_type} | View facilities at a specific stop (Metro and V/Line stations only) |
| [**stopsStopsByGeolocation**](StopsApi.md#stopsStopsByGeolocation) | **GET** /v3/stops/location/{latitude},{longitude} | View all stops near a specific location |
| [**stopsStopsForRoute**](StopsApi.md#stopsStopsForRoute) | **GET** /v3/stops/route/{route_id}/route_type/{route_type} | View all stops on a specific route |


<a id="stopsStopDetails"></a>
# **stopsStopDetails**
> V3StopResponse stopsStopDetails(stopId, routeType, stopLocation, stopAmenities, stopAccessibility, stopContact, stopTicket, gtfs, stopStaffing, stopDisruptions, token, devid, signature)

View facilities at a specific stop (Metro and V/Line stations only)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    StopsApi apiInstance = new StopsApi(defaultClient);
    Integer stopId = 56; // Integer | Identifier of stop; values returned by Stops API
    Integer routeType = 0; // Integer | Number identifying transport mode; values returned via RouteTypes API
    Boolean stopLocation = true; // Boolean | Indicates if stop location information will be returned (default = false)
    Boolean stopAmenities = true; // Boolean | Indicates if stop amenity information will be returned (default = false)
    Boolean stopAccessibility = true; // Boolean | Indicates if stop accessibility information will be returned (default = false)
    Boolean stopContact = true; // Boolean | Indicates if stop contact information will be returned (default = false)
    Boolean stopTicket = true; // Boolean | Indicates if stop ticket information will be returned (default = false)
    Boolean gtfs = true; // Boolean | Incdicates whether the stop_id is a GTFS ID or not
    Boolean stopStaffing = true; // Boolean | Indicates if stop staffing information will be returned (default = false)
    Boolean stopDisruptions = true; // Boolean | Indicates if stop disruption information will be returned (default = false)
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3StopResponse result = apiInstance.stopsStopDetails(stopId, routeType, stopLocation, stopAmenities, stopAccessibility, stopContact, stopTicket, gtfs, stopStaffing, stopDisruptions, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopsApi#stopsStopDetails");
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
| **stopId** | **Integer**| Identifier of stop; values returned by Stops API | |
| **routeType** | **Integer**| Number identifying transport mode; values returned via RouteTypes API | [enum: 0, 1, 2, 3, 4] |
| **stopLocation** | **Boolean**| Indicates if stop location information will be returned (default &#x3D; false) | [optional] |
| **stopAmenities** | **Boolean**| Indicates if stop amenity information will be returned (default &#x3D; false) | [optional] |
| **stopAccessibility** | **Boolean**| Indicates if stop accessibility information will be returned (default &#x3D; false) | [optional] |
| **stopContact** | **Boolean**| Indicates if stop contact information will be returned (default &#x3D; false) | [optional] |
| **stopTicket** | **Boolean**| Indicates if stop ticket information will be returned (default &#x3D; false) | [optional] |
| **gtfs** | **Boolean**| Incdicates whether the stop_id is a GTFS ID or not | [optional] |
| **stopStaffing** | **Boolean**| Indicates if stop staffing information will be returned (default &#x3D; false) | [optional] |
| **stopDisruptions** | **Boolean**| Indicates if stop disruption information will be returned (default &#x3D; false) | [optional] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3StopResponse**](V3StopResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stop location, amenity and accessibility facility information for the specified stop (metropolitan and V/Line stations only). |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

<a id="stopsStopsByGeolocation"></a>
# **stopsStopsByGeolocation**
> V3StopsByDistanceResponse stopsStopsByGeolocation(latitude, longitude, routeTypes, maxResults, maxDistance, stopDisruptions, token, devid, signature)

View all stops near a specific location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    StopsApi apiInstance = new StopsApi(defaultClient);
    Float latitude = 3.4F; // Float | Geographic coordinate of latitude
    Float longitude = 3.4F; // Float | Geographic coordinate of longitude
    List<Integer> routeTypes = Arrays.asList(); // List<Integer> | Filter by route_type; values returned via RouteTypes API
    Integer maxResults = 56; // Integer | Maximum number of results returned (default = 30)
    Double maxDistance = 3.4D; // Double | Filter by maximum distance (in metres) from location specified via latitude and longitude parameters (default = 300)
    Boolean stopDisruptions = true; // Boolean | Indicates if stop disruption information will be returned (default = false)
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3StopsByDistanceResponse result = apiInstance.stopsStopsByGeolocation(latitude, longitude, routeTypes, maxResults, maxDistance, stopDisruptions, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopsApi#stopsStopsByGeolocation");
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
| **latitude** | **Float**| Geographic coordinate of latitude | |
| **longitude** | **Float**| Geographic coordinate of longitude | |
| **routeTypes** | [**List&lt;Integer&gt;**](Integer.md)| Filter by route_type; values returned via RouteTypes API | [optional] [enum: 0, 1, 2, 3, 4] |
| **maxResults** | **Integer**| Maximum number of results returned (default &#x3D; 30) | [optional] |
| **maxDistance** | **Double**| Filter by maximum distance (in metres) from location specified via latitude and longitude parameters (default &#x3D; 300) | [optional] |
| **stopDisruptions** | **Boolean**| Indicates if stop disruption information will be returned (default &#x3D; false) | [optional] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3StopsByDistanceResponse**](V3StopsByDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All stops near the specified location. |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

<a id="stopsStopsForRoute"></a>
# **stopsStopsForRoute**
> V3StopsOnRouteResponse stopsStopsForRoute(routeId, routeType, directionId, stopDisruptions, includeGeopath, geopathUtc, token, devid, signature)

View all stops on a specific route

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    StopsApi apiInstance = new StopsApi(defaultClient);
    Integer routeId = 56; // Integer | Identifier of route; values returned by Routes API - v3/routes
    Integer routeType = 0; // Integer | Number identifying transport mode; values returned via RouteTypes API
    Integer directionId = 56; // Integer | An optional direction; values returned by Directions API. When this is set, stop sequence information is returned in the response.
    Boolean stopDisruptions = true; // Boolean | Indicates if stop disruption information will be returned (default = false)
    Boolean includeGeopath = true; // Boolean | Indicates if geopath data will be returned (default = false)
    OffsetDateTime geopathUtc = OffsetDateTime.now(); // OffsetDateTime | Filter geopaths by date (ISO 8601 UTC format) (default = current date)
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3StopsOnRouteResponse result = apiInstance.stopsStopsForRoute(routeId, routeType, directionId, stopDisruptions, includeGeopath, geopathUtc, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopsApi#stopsStopsForRoute");
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
| **routeId** | **Integer**| Identifier of route; values returned by Routes API - v3/routes | |
| **routeType** | **Integer**| Number identifying transport mode; values returned via RouteTypes API | [enum: 0, 1, 2, 3, 4] |
| **directionId** | **Integer**| An optional direction; values returned by Directions API. When this is set, stop sequence information is returned in the response. | [optional] |
| **stopDisruptions** | **Boolean**| Indicates if stop disruption information will be returned (default &#x3D; false) | [optional] |
| **includeGeopath** | **Boolean**| Indicates if geopath data will be returned (default &#x3D; false) | [optional] |
| **geopathUtc** | **OffsetDateTime**| Filter geopaths by date (ISO 8601 UTC format) (default &#x3D; current date) | [optional] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3StopsOnRouteResponse**](V3StopsOnRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All stops on the specified route. |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

