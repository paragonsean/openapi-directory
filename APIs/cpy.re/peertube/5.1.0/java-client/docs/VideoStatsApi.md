# VideoStatsApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1VideosIdStatsOverallGet**](VideoStatsApi.md#apiV1VideosIdStatsOverallGet) | **GET** /api/v1/videos/{id}/stats/overall | Get overall stats of a video |
| [**apiV1VideosIdStatsRetentionGet**](VideoStatsApi.md#apiV1VideosIdStatsRetentionGet) | **GET** /api/v1/videos/{id}/stats/retention | Get retention stats of a video |
| [**apiV1VideosIdStatsTimeseriesMetricGet**](VideoStatsApi.md#apiV1VideosIdStatsTimeseriesMetricGet) | **GET** /api/v1/videos/{id}/stats/timeseries/{metric} | Get timeserie stats of a video |


<a id="apiV1VideosIdStatsOverallGet"></a>
# **apiV1VideosIdStatsOverallGet**
> VideoStatsOverall apiV1VideosIdStatsOverallGet(id, startDate, endDate)

Get overall stats of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoStatsApi apiInstance = new VideoStatsApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Filter stats by start date
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Filter stats by end date
    try {
      VideoStatsOverall result = apiInstance.apiV1VideosIdStatsOverallGet(id, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoStatsApi#apiV1VideosIdStatsOverallGet");
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
| **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | |
| **startDate** | **OffsetDateTime**| Filter stats by start date | [optional] |
| **endDate** | **OffsetDateTime**| Filter stats by end date | [optional] |

### Return type

[**VideoStatsOverall**](VideoStatsOverall.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1VideosIdStatsRetentionGet"></a>
# **apiV1VideosIdStatsRetentionGet**
> VideoStatsRetention apiV1VideosIdStatsRetentionGet(id)

Get retention stats of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoStatsApi apiInstance = new VideoStatsApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      VideoStatsRetention result = apiInstance.apiV1VideosIdStatsRetentionGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoStatsApi#apiV1VideosIdStatsRetentionGet");
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
| **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | |

### Return type

[**VideoStatsRetention**](VideoStatsRetention.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1VideosIdStatsTimeseriesMetricGet"></a>
# **apiV1VideosIdStatsTimeseriesMetricGet**
> VideoStatsTimeserie apiV1VideosIdStatsTimeseriesMetricGet(id, metric, startDate, endDate)

Get timeserie stats of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoStatsApi apiInstance = new VideoStatsApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    String metric = "viewers"; // String | The metric to get
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Filter stats by start date
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Filter stats by end date
    try {
      VideoStatsTimeserie result = apiInstance.apiV1VideosIdStatsTimeseriesMetricGet(id, metric, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoStatsApi#apiV1VideosIdStatsTimeseriesMetricGet");
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
| **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | |
| **metric** | **String**| The metric to get | [enum: viewers, aggregateWatchTime] |
| **startDate** | **OffsetDateTime**| Filter stats by start date | [optional] |
| **endDate** | **OffsetDateTime**| Filter stats by end date | [optional] |

### Return type

[**VideoStatsTimeserie**](VideoStatsTimeserie.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

