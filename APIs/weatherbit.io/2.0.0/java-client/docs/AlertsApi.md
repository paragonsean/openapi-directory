# AlertsApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**alertslatlatlonlonGet**](AlertsApi.md#alertslatlatlonlonGet) | **GET** /alerts?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns severe weather alerts issued by meteorological agencies - Given a lat/lon. |


<a id="alertslatlatlonlonGet"></a>
# **alertslatlatlonlonGet**
> WeatherAlert alertslatlatlonlonGet(lat, lon, key, paramCallback)

Returns severe weather alerts issued by meteorological agencies - Given a lat/lon.

Returns severe weather alerts issued by meteorological agencies - given a lat, and a lon.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String key = "key_example"; // String | Your registered API key.
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback - Example - callback=func
    try {
      WeatherAlert result = apiInstance.alertslatlatlonlonGet(lat, lon, key, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertslatlatlonlonGet");
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
| **lat** | **Double**| Latitude component of location. | |
| **lon** | **Double**| Longitude component of location. | |
| **key** | **String**| Your registered API key. | |
| **paramCallback** | **String**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional] |

### Return type

[**WeatherAlert**](WeatherAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Weather Alert Object. |  -  |
| **0** | No Data. |  -  |

