# WeatherForecastApi

All URIs are relative to *https://weather.visualcrossing.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**visualCrossingWebServicesRestServicesWeatherdataForecastGet**](WeatherForecastApi.md#visualCrossingWebServicesRestServicesWeatherdataForecastGet) | **GET** /VisualCrossingWebServices/rest/services/weatherdata/forecast | Weather Forecast API |


<a id="visualCrossingWebServicesRestServicesWeatherdataForecastGet"></a>
# **visualCrossingWebServicesRestServicesWeatherdataForecastGet**
> visualCrossingWebServicesRestServicesWeatherdataForecastGet(sendAsDatasource, allowAsynch, shortColumnNames, locations, aggregateHours, contentType, unitGroup, key)

Weather Forecast API

Provides access to weather forecast information. The forecast is available for up to 15 days at the hourly, 12 hour and daily summary level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WeatherForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://weather.visualcrossing.com");

    WeatherForecastApi apiInstance = new WeatherForecastApi(defaultClient);
    Boolean sendAsDatasource = false; // Boolean | 
    Boolean allowAsynch = false; // Boolean | 
    Boolean shortColumnNames = false; // Boolean | 
    String locations = "Sterling%2C%20VA%2C%20US"; // String | 
    String aggregateHours = "24"; // String | 
    String contentType = "json"; // String | 
    String unitGroup = "us"; // String | 
    String key = "INSERT_YOUR_KEY"; // String | 
    try {
      apiInstance.visualCrossingWebServicesRestServicesWeatherdataForecastGet(sendAsDatasource, allowAsynch, shortColumnNames, locations, aggregateHours, contentType, unitGroup, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling WeatherForecastApi#visualCrossingWebServicesRestServicesWeatherdataForecastGet");
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
| **sendAsDatasource** | **Boolean**|  | [optional] |
| **allowAsynch** | **Boolean**|  | [optional] |
| **shortColumnNames** | **Boolean**|  | [optional] |
| **locations** | **String**|  | [optional] |
| **aggregateHours** | **String**|  | [optional] |
| **contentType** | **String**|  | [optional] |
| **unitGroup** | **String**|  | [optional] |
| **key** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Auto generated using Swagger Inspector |  -  |

