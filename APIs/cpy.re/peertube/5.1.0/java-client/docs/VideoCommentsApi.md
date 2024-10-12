# VideoCommentsApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1VideosIdCommentThreadsGet**](VideoCommentsApi.md#apiV1VideosIdCommentThreadsGet) | **GET** /api/v1/videos/{id}/comment-threads | List threads of a video |
| [**apiV1VideosIdCommentThreadsPost**](VideoCommentsApi.md#apiV1VideosIdCommentThreadsPost) | **POST** /api/v1/videos/{id}/comment-threads | Create a thread |
| [**apiV1VideosIdCommentThreadsThreadIdGet**](VideoCommentsApi.md#apiV1VideosIdCommentThreadsThreadIdGet) | **GET** /api/v1/videos/{id}/comment-threads/{threadId} | Get a thread |
| [**apiV1VideosIdCommentsCommentIdDelete**](VideoCommentsApi.md#apiV1VideosIdCommentsCommentIdDelete) | **DELETE** /api/v1/videos/{id}/comments/{commentId} | Delete a comment or a reply |
| [**apiV1VideosIdCommentsCommentIdPost**](VideoCommentsApi.md#apiV1VideosIdCommentsCommentIdPost) | **POST** /api/v1/videos/{id}/comments/{commentId} | Reply to a thread of a video |


<a id="apiV1VideosIdCommentThreadsGet"></a>
# **apiV1VideosIdCommentThreadsGet**
> CommentThreadResponse apiV1VideosIdCommentThreadsGet(id, start, count, sort)

List threads of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoCommentsApi apiInstance = new VideoCommentsApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort comments by criteria
    try {
      CommentThreadResponse result = apiInstance.apiV1VideosIdCommentThreadsGet(id, start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoCommentsApi#apiV1VideosIdCommentThreadsGet");
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
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort comments by criteria | [optional] [enum: -createdAt, -totalReplies] |

### Return type

[**CommentThreadResponse**](CommentThreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1VideosIdCommentThreadsPost"></a>
# **apiV1VideosIdCommentThreadsPost**
> CommentThreadPostResponse apiV1VideosIdCommentThreadsPost(id, apiV1VideosIdCommentThreadsPostRequest)

Create a thread

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoCommentsApi apiInstance = new VideoCommentsApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    ApiV1VideosIdCommentThreadsPostRequest apiV1VideosIdCommentThreadsPostRequest = new ApiV1VideosIdCommentThreadsPostRequest(); // ApiV1VideosIdCommentThreadsPostRequest | 
    try {
      CommentThreadPostResponse result = apiInstance.apiV1VideosIdCommentThreadsPost(id, apiV1VideosIdCommentThreadsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoCommentsApi#apiV1VideosIdCommentThreadsPost");
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
| **apiV1VideosIdCommentThreadsPostRequest** | [**ApiV1VideosIdCommentThreadsPostRequest**](ApiV1VideosIdCommentThreadsPostRequest.md)|  | [optional] |

### Return type

[**CommentThreadPostResponse**](CommentThreadPostResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **404** | video does not exist |  -  |

<a id="apiV1VideosIdCommentThreadsThreadIdGet"></a>
# **apiV1VideosIdCommentThreadsThreadIdGet**
> VideoCommentThreadTree apiV1VideosIdCommentThreadsThreadIdGet(id, threadId)

Get a thread

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoCommentsApi apiInstance = new VideoCommentsApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    Integer threadId = 56; // Integer | The thread id (root comment id)
    try {
      VideoCommentThreadTree result = apiInstance.apiV1VideosIdCommentThreadsThreadIdGet(id, threadId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoCommentsApi#apiV1VideosIdCommentThreadsThreadIdGet");
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
| **threadId** | **Integer**| The thread id (root comment id) | |

### Return type

[**VideoCommentThreadTree**](VideoCommentThreadTree.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1VideosIdCommentsCommentIdDelete"></a>
# **apiV1VideosIdCommentsCommentIdDelete**
> apiV1VideosIdCommentsCommentIdDelete(id, commentId)

Delete a comment or a reply

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoCommentsApi apiInstance = new VideoCommentsApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    Integer commentId = 56; // Integer | The comment id
    try {
      apiInstance.apiV1VideosIdCommentsCommentIdDelete(id, commentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoCommentsApi#apiV1VideosIdCommentsCommentIdDelete");
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
| **commentId** | **Integer**| The comment id | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **403** | cannot remove comment of another user |  -  |
| **404** | comment or video does not exist |  -  |
| **409** | comment is already deleted |  -  |

<a id="apiV1VideosIdCommentsCommentIdPost"></a>
# **apiV1VideosIdCommentsCommentIdPost**
> CommentThreadPostResponse apiV1VideosIdCommentsCommentIdPost(id, commentId, apiV1VideosIdCommentThreadsPostRequest)

Reply to a thread of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoCommentsApi apiInstance = new VideoCommentsApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    Integer commentId = 56; // Integer | The comment id
    ApiV1VideosIdCommentThreadsPostRequest apiV1VideosIdCommentThreadsPostRequest = new ApiV1VideosIdCommentThreadsPostRequest(); // ApiV1VideosIdCommentThreadsPostRequest | 
    try {
      CommentThreadPostResponse result = apiInstance.apiV1VideosIdCommentsCommentIdPost(id, commentId, apiV1VideosIdCommentThreadsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoCommentsApi#apiV1VideosIdCommentsCommentIdPost");
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
| **commentId** | **Integer**| The comment id | |
| **apiV1VideosIdCommentThreadsPostRequest** | [**ApiV1VideosIdCommentThreadsPostRequest**](ApiV1VideosIdCommentThreadsPostRequest.md)|  | [optional] |

### Return type

[**CommentThreadPostResponse**](CommentThreadPostResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **404** | thread or video does not exist |  -  |

