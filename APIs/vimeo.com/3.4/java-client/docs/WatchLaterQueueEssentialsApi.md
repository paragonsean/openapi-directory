# WatchLaterQueueEssentialsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoToWatchLater**](WatchLaterQueueEssentialsApi.md#addVideoToWatchLater) | **PUT** /users/{user_id}/watchlater/{video_id} | Add a video to a user&#39;s Watch Later queue |
| [**addVideoToWatchLaterAlt1**](WatchLaterQueueEssentialsApi.md#addVideoToWatchLaterAlt1) | **PUT** /me/watchlater/{video_id} | Add a video to a user&#39;s Watch Later queue |
| [**checkWatchLaterQueue**](WatchLaterQueueEssentialsApi.md#checkWatchLaterQueue) | **GET** /users/{user_id}/watchlater/{video_id} | Check if a user has added a specific video to their Watch Later queue |
| [**checkWatchLaterQueueAlt1**](WatchLaterQueueEssentialsApi.md#checkWatchLaterQueueAlt1) | **GET** /me/watchlater/{video_id} | Check if a user has added a specific video to their Watch Later queue |
| [**deleteVideoFromWatchLater**](WatchLaterQueueEssentialsApi.md#deleteVideoFromWatchLater) | **DELETE** /users/{user_id}/watchlater/{video_id} | Remove a video from a user&#39;s Watch Later queue |
| [**deleteVideoFromWatchLaterAlt1**](WatchLaterQueueEssentialsApi.md#deleteVideoFromWatchLaterAlt1) | **DELETE** /me/watchlater/{video_id} | Remove a video from a user&#39;s Watch Later queue |
| [**getWatchLaterQueue**](WatchLaterQueueEssentialsApi.md#getWatchLaterQueue) | **GET** /users/{user_id}/watchlater | Get all the videos in a user&#39;s Watch Later queue |
| [**getWatchLaterQueueAlt1**](WatchLaterQueueEssentialsApi.md#getWatchLaterQueueAlt1) | **GET** /me/watchlater | Get all the videos in a user&#39;s Watch Later queue |


<a id="addVideoToWatchLater"></a>
# **addVideoToWatchLater**
> addVideoToWatchLater(userId, videoId)

Add a video to a user&#39;s Watch Later queue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WatchLaterQueueEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WatchLaterQueueEssentialsApi apiInstance = new WatchLaterQueueEssentialsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.addVideoToWatchLater(userId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WatchLaterQueueEssentialsApi#addVideoToWatchLater");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was added. |  -  |

<a id="addVideoToWatchLaterAlt1"></a>
# **addVideoToWatchLaterAlt1**
> addVideoToWatchLaterAlt1(videoId)

Add a video to a user&#39;s Watch Later queue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WatchLaterQueueEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WatchLaterQueueEssentialsApi apiInstance = new WatchLaterQueueEssentialsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.addVideoToWatchLaterAlt1(videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WatchLaterQueueEssentialsApi#addVideoToWatchLaterAlt1");
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
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was added. |  -  |

<a id="checkWatchLaterQueue"></a>
# **checkWatchLaterQueue**
> Video checkWatchLaterQueue(userId, videoId)

Check if a user has added a specific video to their Watch Later queue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WatchLaterQueueEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WatchLaterQueueEssentialsApi apiInstance = new WatchLaterQueueEssentialsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      Video result = apiInstance.checkWatchLaterQueue(userId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WatchLaterQueueEssentialsApi#checkWatchLaterQueue");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The video appears in the user&#39;s Watch Later queue. |  -  |
| **404** | The video doesn&#39;t appear in the user&#39;s Watch Later queue. |  -  |

<a id="checkWatchLaterQueueAlt1"></a>
# **checkWatchLaterQueueAlt1**
> Video checkWatchLaterQueueAlt1(videoId)

Check if a user has added a specific video to their Watch Later queue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WatchLaterQueueEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WatchLaterQueueEssentialsApi apiInstance = new WatchLaterQueueEssentialsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      Video result = apiInstance.checkWatchLaterQueueAlt1(videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WatchLaterQueueEssentialsApi#checkWatchLaterQueueAlt1");
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
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The video appears in the user&#39;s Watch Later queue. |  -  |
| **404** | The video doesn&#39;t appear in the user&#39;s Watch Later queue. |  -  |

<a id="deleteVideoFromWatchLater"></a>
# **deleteVideoFromWatchLater**
> deleteVideoFromWatchLater(userId, videoId)

Remove a video from a user&#39;s Watch Later queue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WatchLaterQueueEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WatchLaterQueueEssentialsApi apiInstance = new WatchLaterQueueEssentialsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteVideoFromWatchLater(userId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WatchLaterQueueEssentialsApi#deleteVideoFromWatchLater");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was deleted. |  -  |

<a id="deleteVideoFromWatchLaterAlt1"></a>
# **deleteVideoFromWatchLaterAlt1**
> deleteVideoFromWatchLaterAlt1(videoId)

Remove a video from a user&#39;s Watch Later queue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WatchLaterQueueEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WatchLaterQueueEssentialsApi apiInstance = new WatchLaterQueueEssentialsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteVideoFromWatchLaterAlt1(videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WatchLaterQueueEssentialsApi#deleteVideoFromWatchLaterAlt1");
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
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was deleted. |  -  |

<a id="getWatchLaterQueue"></a>
# **getWatchLaterQueue**
> List&lt;Video&gt; getWatchLaterQueue(userId, direction, filter, filterEmbeddable, page, perPage, query, sort)

Get all the videos in a user&#39;s Watch Later queue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WatchLaterQueueEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WatchLaterQueueEssentialsApi apiInstance = new WatchLaterQueueEssentialsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "embeddable"; // String | The attribute by which to filter the results.
    Boolean filterEmbeddable = true; // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<Video> result = apiInstance.getWatchLaterQueue(userId, direction, filter, filterEmbeddable, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WatchLaterQueueEssentialsApi#getWatchLaterQueue");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: embeddable] |
| **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, comments, date, duration, likes, plays] |

### Return type

[**List&lt;Video&gt;**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The videos were returned. |  -  |
| **304** | The user hasn&#39;t added any videos to their Watch Later queue since the given &#x60;If-Modified-Since&#x60; header. |  -  |

<a id="getWatchLaterQueueAlt1"></a>
# **getWatchLaterQueueAlt1**
> List&lt;Video&gt; getWatchLaterQueueAlt1(direction, filter, filterEmbeddable, page, perPage, query, sort)

Get all the videos in a user&#39;s Watch Later queue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WatchLaterQueueEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WatchLaterQueueEssentialsApi apiInstance = new WatchLaterQueueEssentialsApi(defaultClient);
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "embeddable"; // String | The attribute by which to filter the results.
    Boolean filterEmbeddable = true; // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<Video> result = apiInstance.getWatchLaterQueueAlt1(direction, filter, filterEmbeddable, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WatchLaterQueueEssentialsApi#getWatchLaterQueueAlt1");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: embeddable] |
| **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, comments, date, duration, likes, plays] |

### Return type

[**List&lt;Video&gt;**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The videos were returned. |  -  |
| **304** | The user hasn&#39;t added any videos to their Watch Later queue since the given &#x60;If-Modified-Since&#x60; header. |  -  |

