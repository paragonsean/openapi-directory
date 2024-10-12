# StatsApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1MetricsPlaybackPost**](StatsApi.md#apiV1MetricsPlaybackPost) | **POST** /api/v1/metrics/playback | Create playback metrics |
| [**getInstanceStats**](StatsApi.md#getInstanceStats) | **GET** /api/v1/server/stats | Get instance stats |


<a id="apiV1MetricsPlaybackPost"></a>
# **apiV1MetricsPlaybackPost**
> apiV1MetricsPlaybackPost(playbackMetricCreate)

Create playback metrics

These metrics are exposed by OpenTelemetry metrics exporter if enabled.

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
    defaultClient.setBasePath("https://peertube2.cpy.re");

    StatsApi apiInstance = new StatsApi(defaultClient);
    PlaybackMetricCreate playbackMetricCreate = new PlaybackMetricCreate(); // PlaybackMetricCreate | 
    try {
      apiInstance.apiV1MetricsPlaybackPost(playbackMetricCreate);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#apiV1MetricsPlaybackPost");
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
| **playbackMetricCreate** | [**PlaybackMetricCreate**](PlaybackMetricCreate.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="getInstanceStats"></a>
# **getInstanceStats**
> ServerStats getInstanceStats()

Get instance stats

Get instance public statistics. This endpoint is cached.

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
    defaultClient.setBasePath("https://peertube2.cpy.re");

    StatsApi apiInstance = new StatsApi(defaultClient);
    try {
      ServerStats result = apiInstance.getInstanceStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#getInstanceStats");
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

[**ServerStats**](ServerStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

