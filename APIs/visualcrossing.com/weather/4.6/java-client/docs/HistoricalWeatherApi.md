# HistoricalWeatherApi

All URIs are relative to *https://weather.visualcrossing.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**visualCrossingWebServicesRestServicesWeatherdataHistoryGet**](HistoricalWeatherApi.md#visualCrossingWebServicesRestServicesWeatherdataHistoryGet) | **GET** /VisualCrossingWebServices/rest/services/weatherdata/history | Retrieves hourly or daily historical weather records. |


<a id="visualCrossingWebServicesRestServicesWeatherdataHistoryGet"></a>
# **visualCrossingWebServicesRestServicesWeatherdataHistoryGet**
> visualCrossingWebServicesRestServicesWeatherdataHistoryGet(maxDistance, shortColumnNames, endDateTime, aggregateHours, collectStationContributions, startDateTime, maxStations, allowAsynch, locations, includeNormals, contentType, unitGroup, key)

Retrieves hourly or daily historical weather records.

The weather history data is suitable for retrieving hourly or daily historical weather records.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoricalWeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://weather.visualcrossing.com");

    HistoricalWeatherApi apiInstance = new HistoricalWeatherApi(defaultClient);
    String maxDistance = "-1"; // String | 
    Boolean shortColumnNames = false; // Boolean | 
    String endDateTime = "2020-02-04T00%3A00%3A00"; // String | 
    String aggregateHours = "24"; // String | 
    Boolean collectStationContributions = false; // Boolean | 
    String startDateTime = "2020-01-28T00%3A00%3A00"; // String | 
    String maxStations = "-1"; // String | 
    Boolean allowAsynch = false; // Boolean | 
    String locations = "Sterling%2C%20VA%2C%20US"; // String | 
    Boolean includeNormals = false; // Boolean | 
    String contentType = "json"; // String | 
    String unitGroup = "us"; // String | 
    String key = "INSERT_YOUR_KEY"; // String | 
    try {
      apiInstance.visualCrossingWebServicesRestServicesWeatherdataHistoryGet(maxDistance, shortColumnNames, endDateTime, aggregateHours, collectStationContributions, startDateTime, maxStations, allowAsynch, locations, includeNormals, contentType, unitGroup, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoricalWeatherApi#visualCrossingWebServicesRestServicesWeatherdataHistoryGet");
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
| **maxDistance** | **String**|  | [optional] |
| **shortColumnNames** | **Boolean**|  | [optional] |
| **endDateTime** | **String**|  | [optional] |
| **aggregateHours** | **String**|  | [optional] |
| **collectStationContributions** | **Boolean**|  | [optional] |
| **startDateTime** | **String**|  | [optional] |
| **maxStations** | **String**|  | [optional] |
| **allowAsynch** | **Boolean**|  | [optional] |
| **locations** | **String**|  | [optional] |
| **includeNormals** | **Boolean**|  | [optional] |
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

