# TrafficCountApiApi

All URIs are relative to *https://idealspot-geodata.p.rapidapi.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchNearestRoadSegments**](TrafficCountApiApi.md#fetchNearestRoadSegments) | **GET** /traffic/roads/nearest/{latitude}/{longitude} | Fetch Nearest Road Segments |
| [**vehicleTrafficCountsforRoadSegment**](TrafficCountApiApi.md#vehicleTrafficCountsforRoadSegment) | **GET** /traffic/counts/{segment_id} | Vehicle Traffic Counts for Road Segment |


<a id="fetchNearestRoadSegments"></a>
# **fetchNearestRoadSegments**
> SearchRoadSegments fetchNearestRoadSegments(n, latitude, longitude, xRapidAPIKey, xRapidAPIHost)

Fetch Nearest Road Segments

For given latitude and longitude, find &#x60;n&#x60; nearest road segments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficCountApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://idealspot-geodata.p.rapidapi.com/api/v1");

    TrafficCountApiApi apiInstance = new TrafficCountApiApi(defaultClient);
    Integer n = 56; // Integer | Number of road segments to return (between 1 and 20)
    Double latitude = 3.4D; // Double | (Required) Search coordinate latitude
    Double longitude = 3.4D; // Double | (Required) Search coordinate longitude
    String xRapidAPIKey = "xRapidAPIKey_example"; // String | (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    String xRapidAPIHost = "xRapidAPIHost_example"; // String | 
    try {
      SearchRoadSegments result = apiInstance.fetchNearestRoadSegments(n, latitude, longitude, xRapidAPIKey, xRapidAPIHost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficCountApiApi#fetchNearestRoadSegments");
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
| **n** | **Integer**| Number of road segments to return (between 1 and 20) | |
| **latitude** | **Double**| (Required) Search coordinate latitude | |
| **longitude** | **Double**| (Required) Search coordinate longitude | |
| **xRapidAPIKey** | **String**| (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata | |
| **xRapidAPIHost** | **String**|  | |

### Return type

[**SearchRoadSegments**](SearchRoadSegments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  |

<a id="vehicleTrafficCountsforRoadSegment"></a>
# **vehicleTrafficCountsforRoadSegment**
> VehicleTrafficCountsforRoadSegment vehicleTrafficCountsforRoadSegment(segmentId, xRapidAPIKey, xRapidAPIHost)

Vehicle Traffic Counts for Road Segment

Time of day, day of week, and side of street vehicle traffic counts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficCountApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://idealspot-geodata.p.rapidapi.com/api/v1");

    TrafficCountApiApi apiInstance = new TrafficCountApiApi(defaultClient);
    Integer segmentId = 56; // Integer | (Required) Road segment ID. Fetched from Search Road Segments
    String xRapidAPIKey = "xRapidAPIKey_example"; // String | (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    String xRapidAPIHost = "xRapidAPIHost_example"; // String | 
    try {
      VehicleTrafficCountsforRoadSegment result = apiInstance.vehicleTrafficCountsforRoadSegment(segmentId, xRapidAPIKey, xRapidAPIHost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficCountApiApi#vehicleTrafficCountsforRoadSegment");
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
| **segmentId** | **Integer**| (Required) Road segment ID. Fetched from Search Road Segments | |
| **xRapidAPIKey** | **String**| (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata | |
| **xRapidAPIHost** | **String**|  | |

### Return type

[**VehicleTrafficCountsforRoadSegment**](VehicleTrafficCountsforRoadSegment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  |

