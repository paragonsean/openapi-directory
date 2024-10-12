# NearestAirportsApi

All URIs are relative to *https://api.aviationdata.systems*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**nearestAirportsNearestAirportList**](NearestAirportsApi.md#nearestAirportsNearestAirportList) | **GET** /v1/airport/nearest/{result_count}/{latitude}/{longitude} | Search for airports by location |


<a id="nearestAirportsNearestAirportList"></a>
# **nearestAirportsNearestAirportList**
> AirportsAPIControllersNearestAirportsControllerResponse nearestAirportsNearestAirportList(resultCount, latitude, longitude)

Search for airports by location

Required parameters: result_count, latitude, longitude, airport_service_type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NearestAirportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.aviationdata.systems");

    NearestAirportsApi apiInstance = new NearestAirportsApi(defaultClient);
    Integer resultCount = 56; // Integer | Required: Number of airports to return. Min: 1 Max: 20
    Double latitude = 3.4D; // Double | Required: Latitude
    Double longitude = 3.4D; // Double | Required: Longitude
    try {
      AirportsAPIControllersNearestAirportsControllerResponse result = apiInstance.nearestAirportsNearestAirportList(resultCount, latitude, longitude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NearestAirportsApi#nearestAirportsNearestAirportList");
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
| **resultCount** | **Integer**| Required: Number of airports to return. Min: 1 Max: 20 | |
| **latitude** | **Double**| Required: Latitude | |
| **longitude** | **Double**| Required: Longitude | |

### Return type

[**AirportsAPIControllersNearestAirportsControllerResponse**](AirportsAPIControllersNearestAirportsControllerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

