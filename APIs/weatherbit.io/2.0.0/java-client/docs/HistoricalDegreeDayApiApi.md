# HistoricalDegreeDayApiApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**historyEnergylatlatlonlonGet**](HistoricalDegreeDayApiApi.md#historyEnergylatlatlonlonGet) | **GET** /history/energy?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns Energy API response  - Given a single lat/lon.  |


<a id="historyEnergylatlatlonlonGet"></a>
# **historyEnergylatlatlonlonGet**
> EnergyObsGroup historyEnergylatlatlonlonGet(lat, lon, startDate, endDate, key, tp, threshold, units, paramCallback)

Returns Energy API response  - Given a single lat/lon. 

Returns aggregate energy specific historical weather fields, over a specified time period.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoricalDegreeDayApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    HistoricalDegreeDayApiApi apiInstance = new HistoricalDegreeDayApiApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String key = "key_example"; // String | Your registered API key.
    String tp = "hourly"; // String | Time period to aggregate by (daily, monthly)
    Double threshold = 3.4D; // Double | Temperature threshold to use to calculate degree days (default 18 C) 
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      EnergyObsGroup result = apiInstance.historyEnergylatlatlonlonGet(lat, lon, startDate, endDate, key, tp, threshold, units, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoricalDegreeDayApiApi#historyEnergylatlatlonlonGet");
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
| **startDate** | **String**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH). | |
| **endDate** | **String**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH). | |
| **key** | **String**| Your registered API key. | |
| **tp** | **String**| Time period to aggregate by (daily, monthly) | [optional] [enum: hourly, daily, monthly] |
| **threshold** | **Double**| Temperature threshold to use to calculate degree days (default 18 C)  | [optional] |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**EnergyObsGroup**](EnergyObsGroup.md)

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

