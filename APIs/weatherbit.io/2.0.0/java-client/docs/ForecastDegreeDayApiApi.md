# ForecastDegreeDayApiApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**forecastEnergylatlatlonlonGet**](ForecastDegreeDayApiApi.md#forecastEnergylatlatlonlonGet) | **GET** /forecast/energy?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns Energy Forecast API response  - Given a single lat/lon.  |


<a id="forecastEnergylatlatlonlonGet"></a>
# **forecastEnergylatlatlonlonGet**
> EnergyObsGroupForecast forecastEnergylatlatlonlonGet(lat, lon, key, threshold, units, tp, paramCallback)

Returns Energy Forecast API response  - Given a single lat/lon. 

Retrieve an 8 day forecast relevant to te Energy Sector (degree days, solar radiation, precipitation, wind).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForecastDegreeDayApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    ForecastDegreeDayApiApi apiInstance = new ForecastDegreeDayApiApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String key = "key_example"; // String | Your registered API key.
    Double threshold = 3.4D; // Double | Temperature threshold to use to calculate degree days (default 18 C) 
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String tp = "hourly"; // String | Time period (default: daily)
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      EnergyObsGroupForecast result = apiInstance.forecastEnergylatlatlonlonGet(lat, lon, key, threshold, units, tp, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForecastDegreeDayApiApi#forecastEnergylatlatlonlonGet");
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
| **threshold** | **Double**| Temperature threshold to use to calculate degree days (default 18 C)  | [optional] |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **tp** | **String**| Time period (default: daily) | [optional] [enum: hourly, daily] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**EnergyObsGroupForecast**](EnergyObsGroupForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Energy Data Object. |  -  |
| **0** | No Data. |  -  |

