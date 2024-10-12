# GroupsVideosApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoToGroup**](GroupsVideosApi.md#addVideoToGroup) | **PUT** /groups/{group_id}/videos/{video_id} | Add a video to a group |
| [**deleteVideoFromGroup**](GroupsVideosApi.md#deleteVideoFromGroup) | **DELETE** /groups/{group_id}/videos/{video_id} | Remove a video from a group |
| [**getGroupVideo**](GroupsVideosApi.md#getGroupVideo) | **GET** /groups/{group_id}/videos/{video_id} | Get a specific video in a group |
| [**getGroupVideos**](GroupsVideosApi.md#getGroupVideos) | **GET** /groups/{group_id}/videos | Get all the videos in a group |


<a id="addVideoToGroup"></a>
# **addVideoToGroup**
> Video addVideoToGroup(groupId, videoId)

Add a video to a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsVideosApi;

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

    GroupsVideosApi apiInstance = new GroupsVideosApi(defaultClient);
    BigDecimal groupId = new BigDecimal("1108"); // BigDecimal | The ID of the group.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      Video result = apiInstance.addVideoToGroup(groupId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsVideosApi#addVideoToGroup");
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
| **groupId** | **BigDecimal**| The ID of the group. | |
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
| **200** | The video was added. |  -  |
| **202** | The video is in pending status. |  -  |
| **403** | * The video is already in the group. * The user can&#39;t add videos to the group. |  -  |

<a id="deleteVideoFromGroup"></a>
# **deleteVideoFromGroup**
> deleteVideoFromGroup(groupId, videoId)

Remove a video from a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsVideosApi;

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

    GroupsVideosApi apiInstance = new GroupsVideosApi(defaultClient);
    BigDecimal groupId = new BigDecimal("1108"); // BigDecimal | The ID of the group.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteVideoFromGroup(groupId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsVideosApi#deleteVideoFromGroup");
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
| **groupId** | **BigDecimal**| The ID of the group. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was deleted. |  -  |
| **403** | The authenticated user can&#39;t modify this group&#39;s videos. |  -  |

<a id="getGroupVideo"></a>
# **getGroupVideo**
> Video getGroupVideo(groupId, videoId)

Get a specific video in a group

Check if a group has a video.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsVideosApi;

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

    GroupsVideosApi apiInstance = new GroupsVideosApi(defaultClient);
    BigDecimal groupId = new BigDecimal("1108"); // BigDecimal | The ID of the group.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      Video result = apiInstance.getGroupVideo(groupId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsVideosApi#getGroupVideo");
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
| **groupId** | **BigDecimal**| The ID of the group. | |
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
| **200** | The video was returned. |  -  |
| **404** | No such video or group exists. |  -  |

<a id="getGroupVideos"></a>
# **getGroupVideos**
> List&lt;Video&gt; getGroupVideos(groupId, direction, filter, filterEmbeddable, page, perPage, query, sort)

Get all the videos in a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsVideosApi;

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

    GroupsVideosApi apiInstance = new GroupsVideosApi(defaultClient);
    BigDecimal groupId = new BigDecimal("1108"); // BigDecimal | The ID of the group.
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "embeddable"; // String | The attribute by which to filter the results.
    Boolean filterEmbeddable = true; // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<Video> result = apiInstance.getGroupVideos(groupId, direction, filter, filterEmbeddable, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsVideosApi#getGroupVideos");
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
| **groupId** | **BigDecimal**| The ID of the group. | |
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
| **304** | No videos have been added to this group since the given &#x60;If-Modified-Since&#x60; header. |  -  |
| **404** | No such group exists. |  -  |

