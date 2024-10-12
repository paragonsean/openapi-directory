# DefaultApi

All URIs are relative to *https://airport-web.appspot.com/_ah/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**airportApiGetAirport**](DefaultApi.md#airportApiGetAirport) | **GET** /airportsapi/v1/airports/{icao_code} |  |


<a id="airportApiGetAirport"></a>
# **airportApiGetAirport**
> ApiEndpointsAirportResponse airportApiGetAirport(icaoCode)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://airport-web.appspot.com/_ah/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String icaoCode = "icaoCode_example"; // String | 
    try {
      ApiEndpointsAirportResponse result = apiInstance.airportApiGetAirport(icaoCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#airportApiGetAirport");
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
| **icaoCode** | **String**|  | |

### Return type

[**ApiEndpointsAirportResponse**](ApiEndpointsAirportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response |  -  |

