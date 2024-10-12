# DeparturesApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**departuresGetForStop**](DeparturesApi.md#departuresGetForStop) | **GET** /v3/departures/route_type/{route_type}/stop/{stop_id} | View departures for all routes from a stop |
| [**departuresGetForStopAndRoute**](DeparturesApi.md#departuresGetForStopAndRoute) | **GET** /v3/departures/route_type/{route_type}/stop/{stop_id}/route/{route_id} | View departures for a specific route from a stop |


<a id="departuresGetForStop"></a>
# **departuresGetForStop**
> V3DeparturesResponse departuresGetForStop(routeType, stopId, platformNumbers, directionId, gtfs, dateUtc, maxResults, includeCancelled, lookBackwards, expand, includeGeopath, token, devid, signature)

View departures for all routes from a stop

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeparturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    DeparturesApi apiInstance = new DeparturesApi(defaultClient);
    Integer routeType = 0; // Integer | Number identifying transport mode; values returned via RouteTypes API
    Integer stopId = 56; // Integer | Identifier of stop; values returned by Stops API
    List<Integer> platformNumbers = Arrays.asList(); // List<Integer> | Filter by platform number at stop
    Integer directionId = 56; // Integer | Filter by identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id}
    Boolean gtfs = true; // Boolean | Indicates that stop_id parameter will accept \"GTFS stop_id\" data
    OffsetDateTime dateUtc = OffsetDateTime.now(); // OffsetDateTime | Filter by the date and time of the request (ISO 8601 UTC format) (default = current date and time)
    Integer maxResults = 56; // Integer | Maximum number of results returned
    Boolean includeCancelled = true; // Boolean | Indicates if cancelled services (if they exist) are returned (default = false) - metropolitan train only
    Boolean lookBackwards = true; // Boolean | Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default = false). Requires max_results &gt; 0.
    List<String> expand = Arrays.asList(); // List<String> | List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.              Run must be expanded to receive VehiclePosition and VehicleDescriptor information.
    Boolean includeGeopath = true; // Boolean | Indicates if the route geopath should be returned
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3DeparturesResponse result = apiInstance.departuresGetForStop(routeType, stopId, platformNumbers, directionId, gtfs, dateUtc, maxResults, includeCancelled, lookBackwards, expand, includeGeopath, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeparturesApi#departuresGetForStop");
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
| **routeType** | **Integer**| Number identifying transport mode; values returned via RouteTypes API | [enum: 0, 1, 2, 3, 4] |
| **stopId** | **Integer**| Identifier of stop; values returned by Stops API | |
| **platformNumbers** | [**List&lt;Integer&gt;**](Integer.md)| Filter by platform number at stop | [optional] |
| **directionId** | **Integer**| Filter by identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id} | [optional] |
| **gtfs** | **Boolean**| Indicates that stop_id parameter will accept \&quot;GTFS stop_id\&quot; data | [optional] |
| **dateUtc** | **OffsetDateTime**| Filter by the date and time of the request (ISO 8601 UTC format) (default &#x3D; current date and time) | [optional] |
| **maxResults** | **Integer**| Maximum number of results returned | [optional] |
| **includeCancelled** | **Boolean**| Indicates if cancelled services (if they exist) are returned (default &#x3D; false) - metropolitan train only | [optional] |
| **lookBackwards** | **Boolean**| Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default &#x3D; false). Requires max_results &amp;gt; 0. | [optional] |
| **expand** | [**List&lt;String&gt;**](String.md)| List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.              Run must be expanded to receive VehiclePosition and VehicleDescriptor information. | [optional] [enum: All, Stop, Route, Run, Direction, Disruption, VehicleDescriptor, VehiclePosition, None] |
| **includeGeopath** | **Boolean**| Indicates if the route geopath should be returned | [optional] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3DeparturesResponse**](V3DeparturesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service departures from the specified stop for all routes of the specified route type; departures are timetabled and real-time (if applicable). |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

<a id="departuresGetForStopAndRoute"></a>
# **departuresGetForStopAndRoute**
> V3DeparturesResponse departuresGetForStopAndRoute(routeType, stopId, routeId, directionId, gtfs, dateUtc, maxResults, includeCancelled, lookBackwards, expand, includeGeopath, token, devid, signature)

View departures for a specific route from a stop

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeparturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    DeparturesApi apiInstance = new DeparturesApi(defaultClient);
    Integer routeType = 0; // Integer | Number identifying transport mode; values returned via RouteTypes API
    Integer stopId = 56; // Integer | Identifier of stop; values returned by Stops API
    String routeId = "routeId_example"; // String | Identifier of route; values returned by Routes API - v3/routes
    Integer directionId = 56; // Integer | Filter by identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id}
    Boolean gtfs = true; // Boolean | Indicates that stop_id parameter will accept \"GTFS stop_id\" data
    OffsetDateTime dateUtc = OffsetDateTime.now(); // OffsetDateTime | Filter by the date and time of the request (ISO 8601 UTC format) (default = current date and time)
    Integer maxResults = 56; // Integer | Maximum number of results returned
    Boolean includeCancelled = true; // Boolean | Indicates if cancelled services (if they exist) are returned (default = false) - metropolitan train only
    Boolean lookBackwards = true; // Boolean | Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default = false). Requires max_results &gt; 0.
    List<String> expand = Arrays.asList(); // List<String> | List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.              Run must be expanded to receive VehiclePosition and VehicleDescriptor information.
    Boolean includeGeopath = true; // Boolean | Indicates if the route geopath should be returned
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3DeparturesResponse result = apiInstance.departuresGetForStopAndRoute(routeType, stopId, routeId, directionId, gtfs, dateUtc, maxResults, includeCancelled, lookBackwards, expand, includeGeopath, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeparturesApi#departuresGetForStopAndRoute");
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
| **routeType** | **Integer**| Number identifying transport mode; values returned via RouteTypes API | [enum: 0, 1, 2, 3, 4] |
| **stopId** | **Integer**| Identifier of stop; values returned by Stops API | |
| **routeId** | **String**| Identifier of route; values returned by Routes API - v3/routes | |
| **directionId** | **Integer**| Filter by identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id} | [optional] |
| **gtfs** | **Boolean**| Indicates that stop_id parameter will accept \&quot;GTFS stop_id\&quot; data | [optional] |
| **dateUtc** | **OffsetDateTime**| Filter by the date and time of the request (ISO 8601 UTC format) (default &#x3D; current date and time) | [optional] |
| **maxResults** | **Integer**| Maximum number of results returned | [optional] |
| **includeCancelled** | **Boolean**| Indicates if cancelled services (if they exist) are returned (default &#x3D; false) - metropolitan train only | [optional] |
| **lookBackwards** | **Boolean**| Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default &#x3D; false). Requires max_results &amp;gt; 0. | [optional] |
| **expand** | [**List&lt;String&gt;**](String.md)| List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.              Run must be expanded to receive VehiclePosition and VehicleDescriptor information. | [optional] [enum: All, Stop, Route, Run, Direction, Disruption, VehicleDescriptor, VehiclePosition, None] |
| **includeGeopath** | **Boolean**| Indicates if the route geopath should be returned | [optional] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3DeparturesResponse**](V3DeparturesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service departures from the specified stop for the specified route (and route type); departures are timetabled and real-time (if applicable). |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

