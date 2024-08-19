# AirQualityApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**airQualityGet**](AirQualityApi.md#airQualityGet) | **GET** /AirQuality | Gets air quality data feed |


<a id="airQualityGet"></a>
# **airQualityGet**
> Object airQualityGet()

Gets air quality data feed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirQualityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    AirQualityApi apiInstance = new AirQualityApi(defaultClient);
    try {
      Object result = apiInstance.airQualityGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirQualityApi#airQualityGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

