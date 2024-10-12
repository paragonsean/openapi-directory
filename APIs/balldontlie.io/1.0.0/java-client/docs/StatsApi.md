# StatsApi

All URIs are relative to *https://balldontlie.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**allStatsExampleParameters**](StatsApi.md#allStatsExampleParameters) | **GET** /api/v1/stats | all stats (example parameters) |


<a id="allStatsExampleParameters"></a>
# **allStatsExampleParameters**
> allStatsExampleParameters(season, playerIds)

all stats (example parameters)

all stats (example parameters)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://balldontlie.io");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String season = "2018"; // String | 
    String playerIds = "237"; // String | 
    try {
      apiInstance.allStatsExampleParameters(season, playerIds);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#allStatsExampleParameters");
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
| **season** | **String**|  | [optional] |
| **playerIds** | **String**|  | [optional] |

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
| **200** |  |  -  |

