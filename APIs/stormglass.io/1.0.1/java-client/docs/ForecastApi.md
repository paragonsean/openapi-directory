# ForecastApi

All URIs are relative to *https://api.stormglass.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getForecast**](ForecastApi.md#getForecast) | **GET** /forecast | Get hourly forecasts by coordinates |


<a id="getForecast"></a>
# **getForecast**
> Forecast getForecast(lat, lng)

Get hourly forecasts by coordinates

Get forecast info for the given coordinates. For every hour and property, you will get a list of weather sources and their values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.stormglass.io");
    
    // Configure API key authorization: authenticationToken
    ApiKeyAuth authenticationToken = (ApiKeyAuth) defaultClient.getAuthentication("authenticationToken");
    authenticationToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //authenticationToken.setApiKeyPrefix("Token");

    ForecastApi apiInstance = new ForecastApi(defaultClient);
    BigDecimal lat = new BigDecimal(78); // BigDecimal | The latitude for a location. Valid input is a number between -90 and 90.
    BigDecimal lng = new BigDecimal(78); // BigDecimal | The longitude for a location. Valid input is a number between -180 and 180.
    try {
      Forecast result = apiInstance.getForecast(lat, lng);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForecastApi#getForecast");
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
| **lat** | **BigDecimal**| The latitude for a location. Valid input is a number between -90 and 90. | |
| **lng** | **BigDecimal**| The longitude for a location. Valid input is a number between -180 and 180. | |

### Return type

[**Forecast**](Forecast.md)

### Authorization

[authenticationToken](../README.md#authenticationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **403** | Unauthorized or API key is invalid |  -  |
| **422** | Invalid or missing coordinates |  -  |

