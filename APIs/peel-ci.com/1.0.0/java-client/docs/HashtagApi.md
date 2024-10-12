# HashtagApi

All URIs are relative to *http://hashtag.peel-ci.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRelatedHashtags**](HashtagApi.md#getRelatedHashtags) | **GET** /hashtag/related | Gets related hashtags for a show. |
| [**getTrendingShows**](HashtagApi.md#getTrendingShows) | **GET** /hashtag/trendingShows | Gets trending shows. |
| [**getTuneinLinks**](HashtagApi.md#getTuneinLinks) | **GET** /hashtag/tuneinlinks | Gets tunein URLs (links) from either a tweet, hashtags, @mentions, or show ID. |


<a id="getRelatedHashtags"></a>
# **getRelatedHashtags**
> getRelatedHashtags(showID, timeWindow)

Gets related hashtags for a show.

Returns any official hashtag and any hashtags which were learned within the most recent time window for the show.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HashtagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://hashtag.peel-ci.com");

    HashtagApi apiInstance = new HashtagApi(defaultClient);
    String showID = "showID_example"; // String | Unique ID for a show
    String timeWindow = "timeWindow_example"; // String | Time window in seconds (default is 2 hours)
    try {
      apiInstance.getRelatedHashtags(showID, timeWindow);
    } catch (ApiException e) {
      System.err.println("Exception when calling HashtagApi#getRelatedHashtags");
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
| **showID** | **String**| Unique ID for a show | |
| **timeWindow** | **String**| Time window in seconds (default is 2 hours) | [optional] |

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
| **200** | No response was specified |  -  |

<a id="getTrendingShows"></a>
# **getTrendingShows**
> getTrendingShows(limit, timeWindow)

Gets trending shows.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HashtagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://hashtag.peel-ci.com");

    HashtagApi apiInstance = new HashtagApi(defaultClient);
    String limit = "limit_example"; // String | Number of trending shows (default is 20)
    String timeWindow = "timeWindow_example"; // String | Time window in seconds (default is 2 hours)
    try {
      apiInstance.getTrendingShows(limit, timeWindow);
    } catch (ApiException e) {
      System.err.println("Exception when calling HashtagApi#getTrendingShows");
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
| **limit** | **String**| Number of trending shows (default is 20) | [optional] |
| **timeWindow** | **String**| Time window in seconds (default is 2 hours) | [optional] |

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
| **200** | No response was specified |  -  |

<a id="getTuneinLinks"></a>
# **getTuneinLinks**
> getTuneinLinks(tweet, hashtags, showID)

Gets tunein URLs (links) from either a tweet, hashtags, @mentions, or show ID.

Either use &lt;b&gt;tweet&lt;/b&gt;, &lt;b&gt;hashtags&lt;/b&gt;, or &lt;b&gt;showID&lt;/b&gt; as the parameter. The tunein URLs that match best are returned in order of best match.&lt;br/&gt;&lt;br/&gt;A &lt;b&gt;tweet&lt;/b&gt; in this context is shorthand for text from a social networking conversation, e.g., it could be from Facebook, Twitter, LinkedIn, etc., and be greater than 140 characters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HashtagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://hashtag.peel-ci.com");

    HashtagApi apiInstance = new HashtagApi(defaultClient);
    String tweet = "tweet_example"; // String | Text from a social networking conversation
    String hashtags = "hashtags_example"; // String | Comma separated list of hashtags and @mentions
    String showID = "showID_example"; // String | Unique ID for a show
    try {
      apiInstance.getTuneinLinks(tweet, hashtags, showID);
    } catch (ApiException e) {
      System.err.println("Exception when calling HashtagApi#getTuneinLinks");
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
| **tweet** | **String**| Text from a social networking conversation | [optional] |
| **hashtags** | **String**| Comma separated list of hashtags and @mentions | [optional] |
| **showID** | **String**| Unique ID for a show | [optional] |

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
| **200** | No response was specified |  -  |

