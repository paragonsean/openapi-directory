# TimelineWeatherApiSingleDateRequestApi

All URIs are relative to *https://weather.visualcrossing.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**visualCrossingWebServicesRestServicesTimelineLocationStartdateGet**](TimelineWeatherApiSingleDateRequestApi.md#visualCrossingWebServicesRestServicesTimelineLocationStartdateGet) | **GET** /VisualCrossingWebServices/rest/services/timeline/{location}/{startdate} | Historical and Forecast Weather API |


<a id="visualCrossingWebServicesRestServicesTimelineLocationStartdateGet"></a>
# **visualCrossingWebServicesRestServicesTimelineLocationStartdateGet**
> visualCrossingWebServicesRestServicesTimelineLocationStartdateGet(location, startdate, key, contentType, unitGroup, include, lang)

Historical and Forecast Weather API

Seamless access to daily and hourly historical and forecast weather data plus weather alerts, events and current conditions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimelineWeatherApiSingleDateRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://weather.visualcrossing.com");

    TimelineWeatherApiSingleDateRequestApi apiInstance = new TimelineWeatherApiSingleDateRequestApi(defaultClient);
    String location = "London,UK"; // String | 
    String startdate = "2022-02-01T00:00:00.000Z"; // String | 
    String key = "INSERT_YOUR_KEY"; // String | 
    String contentType = "json"; // String | data format of the output either json or CSV
    String unitGroup = "us"; // String | 
    String include = "days"; // String | data to include in the output (required for CSV format - days,hours,alerts,current,events )
    String lang = "us"; // String | Language to use for weather descriptions
    try {
      apiInstance.visualCrossingWebServicesRestServicesTimelineLocationStartdateGet(location, startdate, key, contentType, unitGroup, include, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimelineWeatherApiSingleDateRequestApi#visualCrossingWebServicesRestServicesTimelineLocationStartdateGet");
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
| **location** | **String**|  | |
| **startdate** | **String**|  | |
| **key** | **String**|  | |
| **contentType** | **String**| data format of the output either json or CSV | [optional] |
| **unitGroup** | **String**|  | [optional] |
| **include** | **String**| data to include in the output (required for CSV format - days,hours,alerts,current,events ) | [optional] |
| **lang** | **String**| Language to use for weather descriptions | [optional] |

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

