# VideosCommentsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createComment**](VideosCommentsApi.md#createComment) | **POST** /videos/{video_id}/comments | Add a comment to a video |
| [**createCommentAlt1**](VideosCommentsApi.md#createCommentAlt1) | **POST** /channels/{channel_id}/videos/{video_id}/comments | Add a comment to a video |
| [**createCommentReply**](VideosCommentsApi.md#createCommentReply) | **POST** /videos/{video_id}/comments/{comment_id}/replies | Add a reply to a video comment |
| [**deleteComment**](VideosCommentsApi.md#deleteComment) | **DELETE** /videos/{video_id}/comments/{comment_id} | Delete a video comment |
| [**editComment**](VideosCommentsApi.md#editComment) | **PATCH** /videos/{video_id}/comments/{comment_id} | Edit a video comment |
| [**getComment**](VideosCommentsApi.md#getComment) | **GET** /videos/{video_id}/comments/{comment_id} | Get a specific video comment |
| [**getCommentReplies**](VideosCommentsApi.md#getCommentReplies) | **GET** /videos/{video_id}/comments/{comment_id}/replies | Get all the replies to a video comment |
| [**getComments**](VideosCommentsApi.md#getComments) | **GET** /videos/{video_id}/comments | Get all the comments on a video |
| [**getCommentsAlt1**](VideosCommentsApi.md#getCommentsAlt1) | **GET** /channels/{channel_id}/videos/{video_id}/comments | Get all the comments on a video |


<a id="createComment"></a>
# **createComment**
> Comment createComment(videoId, createCommentAlt1Request)

Add a comment to a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCommentsApi;

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

    VideosCommentsApi apiInstance = new VideosCommentsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    CreateCommentAlt1Request createCommentAlt1Request = new CreateCommentAlt1Request(); // CreateCommentAlt1Request | 
    try {
      Comment result = apiInstance.createComment(videoId, createCommentAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCommentsApi#createComment");
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
| **createCommentAlt1Request** | [**CreateCommentAlt1Request**](CreateCommentAlt1Request.md)|  | |

### Return type

[**Comment**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.comment+json
 - **Accept**: application/vnd.vimeo.comment+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The comment was added. |  -  |
| **400** | Error code 2207: The comment text is missing. |  -  |
| **401** | Error code 8003: The user credentials are invalid. |  -  |
| **403** | * Error code 3413: Comments are disabled for this video. * Error code 3411: The authenticated user is unverified. * Error code 3412: The authenticated user can&#39;t comment. * Error code 3301: The comment was flagged as spam. |  -  |

<a id="createCommentAlt1"></a>
# **createCommentAlt1**
> Comment createCommentAlt1(channelId, videoId, createCommentAlt1Request)

Add a comment to a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCommentsApi;

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

    VideosCommentsApi apiInstance = new VideosCommentsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    CreateCommentAlt1Request createCommentAlt1Request = new CreateCommentAlt1Request(); // CreateCommentAlt1Request | 
    try {
      Comment result = apiInstance.createCommentAlt1(channelId, videoId, createCommentAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCommentsApi#createCommentAlt1");
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
| **createCommentAlt1Request** | [**CreateCommentAlt1Request**](CreateCommentAlt1Request.md)|  | |

### Return type

[**Comment**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.comment+json
 - **Accept**: application/vnd.vimeo.comment+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The comment was added. |  -  |
| **400** | Error code 2207: The comment text is missing. |  -  |
| **401** | Error code 8003: The user credentials are invalid. |  -  |
| **403** | * Error code 3413: Comments are disabled for this video. * Error code 3411: The authenticated user is unverified. * Error code 3412: The authenticated user can&#39;t comment. * Error code 3301: The comment was flagged as spam. |  -  |

<a id="createCommentReply"></a>
# **createCommentReply**
> Comment createCommentReply(commentId, videoId, createCommentReplyRequest)

Add a reply to a video comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCommentsApi;

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

    VideosCommentsApi apiInstance = new VideosCommentsApi(defaultClient);
    BigDecimal commentId = new BigDecimal("12345"); // BigDecimal | The ID of the comment.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    CreateCommentReplyRequest createCommentReplyRequest = new CreateCommentReplyRequest(); // CreateCommentReplyRequest | 
    try {
      Comment result = apiInstance.createCommentReply(commentId, videoId, createCommentReplyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCommentsApi#createCommentReply");
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
| **commentId** | **BigDecimal**| The ID of the comment. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **createCommentReplyRequest** | [**CreateCommentReplyRequest**](CreateCommentReplyRequest.md)|  | |

### Return type

[**Comment**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.comment+json
 - **Accept**: application/vnd.vimeo.comment+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The reply was added. |  -  |
| **400** | Error code 2207: The comment text is missing. |  -  |
| **403** | * Error code 3413: Comments are disabled on this video. * Error code 3411: The authenticated user is unverified. * Error code 3412: The authenticated user can&#39;t comment. * Error code 3301: The comment was flagged as spam. |  -  |

<a id="deleteComment"></a>
# **deleteComment**
> deleteComment(commentId, videoId)

Delete a video comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCommentsApi;

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

    VideosCommentsApi apiInstance = new VideosCommentsApi(defaultClient);
    BigDecimal commentId = new BigDecimal("12345"); // BigDecimal | The ID of the comment.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteComment(commentId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCommentsApi#deleteComment");
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
| **commentId** | **BigDecimal**| The ID of the comment. | |
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
| **204** | The comment was deleted. |  -  |
| **403** | Error code 3415: The authenticated user didn&#39;t write this comment and can&#39;t delete it. |  -  |
| **404** | * No such video or comment exists. * Error code 5000: The deleted comment still exists. |  -  |

<a id="editComment"></a>
# **editComment**
> Comment editComment(commentId, videoId, editCommentRequest)

Edit a video comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCommentsApi;

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

    VideosCommentsApi apiInstance = new VideosCommentsApi(defaultClient);
    BigDecimal commentId = new BigDecimal("12345"); // BigDecimal | The ID of the comment.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    EditCommentRequest editCommentRequest = new EditCommentRequest(); // EditCommentRequest | 
    try {
      Comment result = apiInstance.editComment(commentId, videoId, editCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCommentsApi#editComment");
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
| **commentId** | **BigDecimal**| The ID of the comment. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **editCommentRequest** | [**EditCommentRequest**](EditCommentRequest.md)|  | |

### Return type

[**Comment**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.comment+json
 - **Accept**: application/vnd.vimeo.comment+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The comment was edited. |  -  |
| **400** | Error code 2207: The comment text is missing. |  -  |
| **403** | * Error code 3411: The authenticated user is unverified. * Error code 3412: The authenticated user can&#39;t post comments. * Error code 3414: The authenticated user didn&#39;t write the comment and can&#39;t edit it. * Error code 3301: The supplied comment was flagged as spam. |  -  |

<a id="getComment"></a>
# **getComment**
> Comment getComment(commentId, videoId)

Get a specific video comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCommentsApi;

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

    VideosCommentsApi apiInstance = new VideosCommentsApi(defaultClient);
    BigDecimal commentId = new BigDecimal("12345"); // BigDecimal | The ID of the comment.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      Comment result = apiInstance.getComment(commentId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCommentsApi#getComment");
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
| **commentId** | **BigDecimal**| The ID of the comment. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

[**Comment**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.comment+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The comment was returned. |  -  |
| **404** | No such video or comment exists. |  -  |

<a id="getCommentReplies"></a>
# **getCommentReplies**
> List&lt;Comment&gt; getCommentReplies(commentId, videoId, page, perPage)

Get all the replies to a video comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCommentsApi;

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

    VideosCommentsApi apiInstance = new VideosCommentsApi(defaultClient);
    BigDecimal commentId = new BigDecimal("12345"); // BigDecimal | The ID of the comment.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Comment> result = apiInstance.getCommentReplies(commentId, videoId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCommentsApi#getCommentReplies");
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
| **commentId** | **BigDecimal**| The ID of the comment. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**List&lt;Comment&gt;**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.comment+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The replies were returned. |  -  |
| **404** | No such video or comment exists. |  -  |

<a id="getComments"></a>
# **getComments**
> List&lt;Comment&gt; getComments(videoId, direction, page, perPage)

Get all the comments on a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCommentsApi;

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

    VideosCommentsApi apiInstance = new VideosCommentsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Comment> result = apiInstance.getComments(videoId, direction, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCommentsApi#getComments");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**List&lt;Comment&gt;**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.comment+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The comments were returned. |  -  |

<a id="getCommentsAlt1"></a>
# **getCommentsAlt1**
> List&lt;Comment&gt; getCommentsAlt1(channelId, videoId, direction, page, perPage)

Get all the comments on a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCommentsApi;

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

    VideosCommentsApi apiInstance = new VideosCommentsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Comment> result = apiInstance.getCommentsAlt1(channelId, videoId, direction, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCommentsApi#getCommentsAlt1");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**List&lt;Comment&gt;**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.comment+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The comments were returned. |  -  |

