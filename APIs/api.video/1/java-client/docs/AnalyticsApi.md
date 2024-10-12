# AnalyticsApi

All URIs are relative to *https://ws.api.video*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETAnalyticsLiveStreamsLiveStreamId**](AnalyticsApi.md#gETAnalyticsLiveStreamsLiveStreamId) | **GET** /analytics/live-streams/{liveStreamId} | List live stream player sessions |
| [**gETAnalyticsSessionsSessionIdEvents**](AnalyticsApi.md#gETAnalyticsSessionsSessionIdEvents) | **GET** /analytics/sessions/{sessionId}/events | List player session events |
| [**gETAnalyticsVideosVideoId**](AnalyticsApi.md#gETAnalyticsVideosVideoId) | **GET** /analytics/videos/{videoId} | List video player sessions |


<a id="gETAnalyticsLiveStreamsLiveStreamId"></a>
# **gETAnalyticsLiveStreamsLiveStreamId**
> RawStatisticsListLiveStreamAnalyticsResponse gETAnalyticsLiveStreamsLiveStreamId(liveStreamId).period(period).currentPage(currentPage).pageSize(pageSize).execute();

List live stream player sessions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String liveStreamId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The unique identifier for the live stream you want to retrieve analytics for.
    String period = "2019-01-01"; // String | Period must have one of the following formats:  - For a day : \"2018-01-01\", - For a week: \"2018-W01\",  - For a month: \"2018-01\" - For a year: \"2018\" For a range period:  -  Date range: \"2018-01-01/2018-01-15\" 
    Integer currentPage = 1; // Integer | Choose the number of search results to return per page. Minimum value: 1
    Integer pageSize = 25; // Integer | Results per page. Allowed values 1-100, default is 25.
    try {
      RawStatisticsListLiveStreamAnalyticsResponse result = apiInstance.gETAnalyticsLiveStreamsLiveStreamId(liveStreamId)
            .period(period)
            .currentPage(currentPage)
            .pageSize(pageSize)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#gETAnalyticsLiveStreamsLiveStreamId");
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
| **liveStreamId** | **String**| The unique identifier for the live stream you want to retrieve analytics for. | |
| **period** | **String**| Period must have one of the following formats:  - For a day : \&quot;2018-01-01\&quot;, - For a week: \&quot;2018-W01\&quot;,  - For a month: \&quot;2018-01\&quot; - For a year: \&quot;2018\&quot; For a range period:  -  Date range: \&quot;2018-01-01/2018-01-15\&quot;  | [optional] |
| **currentPage** | **Integer**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1] |
| **pageSize** | **Integer**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25] |

### Return type

[**RawStatisticsListLiveStreamAnalyticsResponse**](RawStatisticsListLiveStreamAnalyticsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="gETAnalyticsSessionsSessionIdEvents"></a>
# **gETAnalyticsSessionsSessionIdEvents**
> RawStatisticsListPlayerSessionEventsResponse gETAnalyticsSessionsSessionIdEvents(sessionId).currentPage(currentPage).pageSize(pageSize).execute();

List player session events

Useful to track and measure video&#39;s engagement.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String sessionId = "psEmFwGQUAXR2lFHj5nDOpy"; // String | A unique identifier you can use to reference and track a session with.
    Integer currentPage = 1; // Integer | Choose the number of search results to return per page. Minimum value: 1
    Integer pageSize = 25; // Integer | Results per page. Allowed values 1-100, default is 25.
    try {
      RawStatisticsListPlayerSessionEventsResponse result = apiInstance.gETAnalyticsSessionsSessionIdEvents(sessionId)
            .currentPage(currentPage)
            .pageSize(pageSize)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#gETAnalyticsSessionsSessionIdEvents");
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
| **sessionId** | **String**| A unique identifier you can use to reference and track a session with. | |
| **currentPage** | **Integer**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1] |
| **pageSize** | **Integer**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25] |

### Return type

[**RawStatisticsListPlayerSessionEventsResponse**](RawStatisticsListPlayerSessionEventsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="gETAnalyticsVideosVideoId"></a>
# **gETAnalyticsVideosVideoId**
> RawStatisticsListSessionsResponse gETAnalyticsVideosVideoId(videoId).period(period).metadata(metadata).currentPage(currentPage).pageSize(pageSize).execute();

List video player sessions

Retrieve all available user sessions for a specific video. Tutorials that use the [analytics endpoint](https://api.video/blog/endpoints/analytics).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Prklg"; // String | The unique identifier for the video you want to retrieve session information for.
    String period = "period_example"; // String | Period must have one of the following formats:  - For a day : 2018-01-01, - For a week: 2018-W01,  - For a month: 2018-01 - For a year: 2018 For a range period:  -  Date range: 2018-01-01/2018-01-15 
    List<String> metadata = Arrays.asList(); // List<String> | Metadata and [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata) filter. Send an array of key value pairs you want to filter sessios with.
    Integer currentPage = 1; // Integer | Choose the number of search results to return per page. Minimum value: 1
    Integer pageSize = 25; // Integer | Results per page. Allowed values 1-100, default is 25.
    try {
      RawStatisticsListSessionsResponse result = apiInstance.gETAnalyticsVideosVideoId(videoId)
            .period(period)
            .metadata(metadata)
            .currentPage(currentPage)
            .pageSize(pageSize)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#gETAnalyticsVideosVideoId");
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
| **videoId** | **String**| The unique identifier for the video you want to retrieve session information for. | |
| **period** | **String**| Period must have one of the following formats:  - For a day : 2018-01-01, - For a week: 2018-W01,  - For a month: 2018-01 - For a year: 2018 For a range period:  -  Date range: 2018-01-01/2018-01-15  | [optional] |
| **metadata** | [**List&lt;String&gt;**](String.md)| Metadata and [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata) filter. Send an array of key value pairs you want to filter sessios with. | [optional] |
| **currentPage** | **Integer**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1] |
| **pageSize** | **Integer**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25] |

### Return type

[**RawStatisticsListSessionsResponse**](RawStatisticsListSessionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

