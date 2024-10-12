# PatternsApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**patternsGetPatternByRun**](PatternsApi.md#patternsGetPatternByRun) | **GET** /v3/pattern/run/{run_ref}/route_type/{route_type} | View the stopping pattern for a specific trip/service run |


<a id="patternsGetPatternByRun"></a>
# **patternsGetPatternByRun**
> V3StoppingPattern patternsGetPatternByRun(runRef, routeType, expand, stopId, dateUtc, includeSkippedStops, includeGeopath, token, devid, signature)

View the stopping pattern for a specific trip/service run

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatternsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    PatternsApi apiInstance = new PatternsApi(defaultClient);
    String runRef = "runRef_example"; // String | The run_ref is the identifier of a run as returned by the departures/_* and runs/_* endpoints. WARNING, run_id is deprecated. Use run_ref instead.
    Integer routeType = 0; // Integer | Number identifying transport mode; values returned via RouteTypes API
    List<String> expand = Arrays.asList(); // List<String> | List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor and None. Default is Disruption. Run must be expanded to receive VehiclePosition and VehicleDescriptor information.
    Integer stopId = 56; // Integer | Filter by stop_id; values returned by Stops API
    OffsetDateTime dateUtc = OffsetDateTime.now(); // OffsetDateTime | Filter by the date and time of the request (ISO 8601 UTC format)
    Boolean includeSkippedStops = true; // Boolean | Include any skipped stops in a stopping pattern. Defaults to false.
    Boolean includeGeopath = true; // Boolean | Indicates if geopath data will be returned (default = false)
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3StoppingPattern result = apiInstance.patternsGetPatternByRun(runRef, routeType, expand, stopId, dateUtc, includeSkippedStops, includeGeopath, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatternsApi#patternsGetPatternByRun");
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
| **runRef** | **String**| The run_ref is the identifier of a run as returned by the departures/_* and runs/_* endpoints. WARNING, run_id is deprecated. Use run_ref instead. | |
| **routeType** | **Integer**| Number identifying transport mode; values returned via RouteTypes API | [enum: 0, 1, 2, 3, 4] |
| **expand** | [**List&lt;String&gt;**](String.md)| List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor and None. Default is Disruption. Run must be expanded to receive VehiclePosition and VehicleDescriptor information. | [enum: All, Stop, Route, Run, Direction, Disruption, VehicleDescriptor, VehiclePosition, None] |
| **stopId** | **Integer**| Filter by stop_id; values returned by Stops API | [optional] |
| **dateUtc** | **OffsetDateTime**| Filter by the date and time of the request (ISO 8601 UTC format) | [optional] |
| **includeSkippedStops** | **Boolean**| Include any skipped stops in a stopping pattern. Defaults to false. | [optional] |
| **includeGeopath** | **Boolean**| Indicates if geopath data will be returned (default &#x3D; false) | [optional] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3StoppingPattern**](V3StoppingPattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stopping pattern of the specified run_ref and route type. (NOTE: the departure sequence field should be used to sort departures in chronological order, however it is not always N+1 or N-1 of the previous or following departure. e.g 100, 200, 250, 300 instead of 1, 2, 3, 4) |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

