# ChannelsVideosApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoToChannel**](ChannelsVideosApi.md#addVideoToChannel) | **PUT** /channels/{channel_id}/videos/{video_id} | Add a specific video to a channel |
| [**addVideosToChannel**](ChannelsVideosApi.md#addVideosToChannel) | **PUT** /channels/{channel_id}/videos | Add a list of videos to a channel |
| [**deleteVideoFromChannel**](ChannelsVideosApi.md#deleteVideoFromChannel) | **DELETE** /channels/{channel_id}/videos/{video_id} | Remove a specific video from a channel |
| [**getAvailableVideoChannels**](ChannelsVideosApi.md#getAvailableVideoChannels) | **GET** /videos/{video_id}/available_channels | Get all the channels to which a user can add or remove a specific video |
| [**getChannelVideo**](ChannelsVideosApi.md#getChannelVideo) | **GET** /channels/{channel_id}/videos/{video_id} | Get a specific video in a channel |
| [**getChannelVideos**](ChannelsVideosApi.md#getChannelVideos) | **GET** /channels/{channel_id}/videos | Get all the videos in a channel |
| [**removeVideosFromChannel**](ChannelsVideosApi.md#removeVideosFromChannel) | **DELETE** /channels/{channel_id}/videos | Remove a list of videos from a channel |


<a id="addVideoToChannel"></a>
# **addVideoToChannel**
> addVideoToChannel(channelId, videoId)

Add a specific video to a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsVideosApi;

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

    ChannelsVideosApi apiInstance = new ChannelsVideosApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.addVideoToChannel(channelId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsVideosApi#addVideoToChannel");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
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
| **204** | The video was added. |  -  |
| **403** | The video can&#39;t be added to channels, or the authenticated user isn&#39;t the moderator of this channel. |  -  |
| **404** | No such channel exists, or no such video exists. |  -  |

<a id="addVideosToChannel"></a>
# **addVideosToChannel**
> addVideosToChannel(channelId, addVideosToChannelRequest)

Add a list of videos to a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsVideosApi;

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

    ChannelsVideosApi apiInstance = new ChannelsVideosApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    AddVideosToChannelRequest addVideosToChannelRequest = new AddVideosToChannelRequest(); // AddVideosToChannelRequest | 
    try {
      apiInstance.addVideosToChannel(channelId, addVideosToChannelRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsVideosApi#addVideosToChannel");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
| **addVideosToChannelRequest** | [**AddVideosToChannelRequest**](AddVideosToChannelRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The videos were added. |  -  |
| **403** | The authenticated user isn&#39;t a moderator of the channel, or the video can&#39;t be added to the channel. |  -  |
| **404** | No such channel exists, or no such user exists. |  -  |

<a id="deleteVideoFromChannel"></a>
# **deleteVideoFromChannel**
> deleteVideoFromChannel(channelId, videoId)

Remove a specific video from a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsVideosApi;

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

    ChannelsVideosApi apiInstance = new ChannelsVideosApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteVideoFromChannel(channelId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsVideosApi#deleteVideoFromChannel");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
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
| **204** | The video was removed. |  -  |
| **403** | The authenticated user isn&#39;t a moderator of this channel. |  -  |
| **404** | No such channel exists, or no such video exists. |  -  |

<a id="getAvailableVideoChannels"></a>
# **getAvailableVideoChannels**
> List&lt;Channel&gt; getAvailableVideoChannels(videoId)

Get all the channels to which a user can add or remove a specific video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsVideosApi;

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

    ChannelsVideosApi apiInstance = new ChannelsVideosApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      List<Channel> result = apiInstance.getAvailableVideoChannels(videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsVideosApi#getAvailableVideoChannels");
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

[**List&lt;Channel&gt;**](Channel.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.channel+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The channels were returned. |  -  |
| **403** | The authenticated user can&#39;t add or remove this video from any channel. |  -  |
| **404** | The authenticated user can&#39;t moderate channels. |  -  |

<a id="getChannelVideo"></a>
# **getChannelVideo**
> Video getChannelVideo(channelId, videoId)

Get a specific video in a channel

This method returns a specific video in a channel. You can use it to determine whether the video is in the channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsVideosApi;

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

    ChannelsVideosApi apiInstance = new ChannelsVideosApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      Video result = apiInstance.getChannelVideo(channelId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsVideosApi#getChannelVideo");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
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
| **404** | No such channel exists. |  -  |

<a id="getChannelVideos"></a>
# **getChannelVideos**
> List&lt;Video&gt; getChannelVideos(channelId, containingUri, direction, filter, filterEmbeddable, page, perPage, query, sort)

Get all the videos in a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsVideosApi;

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

    ChannelsVideosApi apiInstance = new ChannelsVideosApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    String containingUri = "/videos/258684937"; // String | The page that contains the video URI.
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "embeddable"; // String | The attribute by which to filter the results.
    Boolean filterEmbeddable = true; // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "added"; // String | The way to sort the results.
    try {
      List<Video> result = apiInstance.getChannelVideos(channelId, containingUri, direction, filter, filterEmbeddable, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsVideosApi#getChannelVideos");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
| **containingUri** | **String**| The page that contains the video URI. | [optional] |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: embeddable] |
| **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: added, alphabetical, comments, date, default, duration, likes, manual, modified_time, plays] |

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
| **304** | No videos have been added to this channel since the given &#x60;If-Modified-Since&#x60; header. |  -  |
| **400** | The **sort** field is &#x60;default&#x60;, but the **direction** field has a value. |  -  |
| **404** | No such channel exists. |  -  |

<a id="removeVideosFromChannel"></a>
# **removeVideosFromChannel**
> Video removeVideosFromChannel(channelId, removeVideosFromChannelRequest)

Remove a list of videos from a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsVideosApi;

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

    ChannelsVideosApi apiInstance = new ChannelsVideosApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    RemoveVideosFromChannelRequest removeVideosFromChannelRequest = new RemoveVideosFromChannelRequest(); // RemoveVideosFromChannelRequest | 
    try {
      Video result = apiInstance.removeVideosFromChannel(channelId, removeVideosFromChannelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsVideosApi#removeVideosFromChannel");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
| **removeVideosFromChannelRequest** | [**RemoveVideosFromChannelRequest**](RemoveVideosFromChannelRequest.md)|  | |

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The videos were removed. |  -  |
| **403** | The authenticated user isn&#39;t a moderator of this channel, or you can&#39;t remove this video from the channel. |  -  |
| **404** | No such channel exists, or no such user exists. |  -  |

