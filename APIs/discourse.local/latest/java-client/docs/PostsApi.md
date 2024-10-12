# PostsApi

All URIs are relative to *http://discourse.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTopicPostPM**](PostsApi.md#createTopicPostPM) | **POST** /posts.json | Creates a new topic, a new post, or a private message |
| [**deletePost**](PostsApi.md#deletePost) | **DELETE** /posts/{id}.json | delete a single post |
| [**getPost**](PostsApi.md#getPost) | **GET** /posts/{id}.json | Retrieve a single post |
| [**listPosts**](PostsApi.md#listPosts) | **GET** /posts.json | List latest posts across topics |
| [**lockPost**](PostsApi.md#lockPost) | **PUT** /posts/{id}/locked.json | Lock a post from being edited |
| [**performPostAction**](PostsApi.md#performPostAction) | **POST** /post_actions.json | Like a post and other actions |
| [**postReplies**](PostsApi.md#postReplies) | **GET** /posts/{id}/replies.json | List replies to a post |
| [**updatePost**](PostsApi.md#updatePost) | **PUT** /posts/{id}.json | Update a single post |


<a id="createTopicPostPM"></a>
# **createTopicPostPM**
> CreateTopicPostPM200Response createTopicPostPM(createTopicPostPMRequest)

Creates a new topic, a new post, or a private message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    PostsApi apiInstance = new PostsApi(defaultClient);
    CreateTopicPostPMRequest createTopicPostPMRequest = new CreateTopicPostPMRequest(); // CreateTopicPostPMRequest | 
    try {
      CreateTopicPostPM200Response result = apiInstance.createTopicPostPM(createTopicPostPMRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#createTopicPostPM");
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
| **createTopicPostPMRequest** | [**CreateTopicPostPMRequest**](CreateTopicPostPMRequest.md)|  | [optional] |

### Return type

[**CreateTopicPostPM200Response**](CreateTopicPostPM200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | post created |  -  |

<a id="deletePost"></a>
# **deletePost**
> deletePost(id, deletePostRequest)

delete a single post

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    PostsApi apiInstance = new PostsApi(defaultClient);
    Integer id = 56; // Integer | 
    DeletePostRequest deletePostRequest = new DeletePostRequest(); // DeletePostRequest | 
    try {
      apiInstance.deletePost(id, deletePostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#deletePost");
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
| **id** | **Integer**|  | |
| **deletePostRequest** | [**DeletePostRequest**](DeletePostRequest.md)|  | [optional] |

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
| **200** | success response |  -  |

<a id="getPost"></a>
# **getPost**
> GetPost200Response getPost(id)

Retrieve a single post

This endpoint can be used to get the number of likes on a post using the &#x60;actions_summary&#x60; property in the response. &#x60;actions_summary&#x60; responses with the id of &#x60;2&#x60; signify a &#x60;like&#x60;. If there are no &#x60;actions_summary&#x60; items with the id of &#x60;2&#x60;, that means there are 0 likes. Other ids likely refer to various different flag types. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    PostsApi apiInstance = new PostsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      GetPost200Response result = apiInstance.getPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#getPost");
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
| **id** | **String**|  | |

### Return type

[**GetPost200Response**](GetPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | single post |  -  |

<a id="listPosts"></a>
# **listPosts**
> ListPosts200Response listPosts(apiKey, apiUsername, before)

List latest posts across topics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    PostsApi apiInstance = new PostsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String before = "before_example"; // String | Load posts with an id lower than this value. Useful for pagination.
    try {
      ListPosts200Response result = apiInstance.listPosts(apiKey, apiUsername, before);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#listPosts");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **before** | **String**| Load posts with an id lower than this value. Useful for pagination. | [optional] |

### Return type

[**ListPosts200Response**](ListPosts200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | latest posts |  -  |

<a id="lockPost"></a>
# **lockPost**
> LockPost200Response lockPost(apiKey, apiUsername, id, lockPostRequest)

Lock a post from being edited

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    PostsApi apiInstance = new PostsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String id = "id_example"; // String | 
    LockPostRequest lockPostRequest = new LockPostRequest(); // LockPostRequest | 
    try {
      LockPost200Response result = apiInstance.lockPost(apiKey, apiUsername, id, lockPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#lockPost");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **id** | **String**|  | |
| **lockPostRequest** | [**LockPostRequest**](LockPostRequest.md)|  | [optional] |

### Return type

[**LockPost200Response**](LockPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | post updated |  -  |

<a id="performPostAction"></a>
# **performPostAction**
> PerformPostAction200Response performPostAction(apiKey, apiUsername, performPostActionRequest)

Like a post and other actions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    PostsApi apiInstance = new PostsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    PerformPostActionRequest performPostActionRequest = new PerformPostActionRequest(); // PerformPostActionRequest | 
    try {
      PerformPostAction200Response result = apiInstance.performPostAction(apiKey, apiUsername, performPostActionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#performPostAction");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **performPostActionRequest** | [**PerformPostActionRequest**](PerformPostActionRequest.md)|  | [optional] |

### Return type

[**PerformPostAction200Response**](PerformPostAction200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | post updated |  -  |

<a id="postReplies"></a>
# **postReplies**
> Set&lt;PostReplies200ResponseInner&gt; postReplies(id)

List replies to a post

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    PostsApi apiInstance = new PostsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      Set<PostReplies200ResponseInner> result = apiInstance.postReplies(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#postReplies");
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
| **id** | **String**|  | |

### Return type

[**Set&lt;PostReplies200ResponseInner&gt;**](PostReplies200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | post replies |  -  |

<a id="updatePost"></a>
# **updatePost**
> UpdatePost200Response updatePost(id, updatePostRequest)

Update a single post

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    PostsApi apiInstance = new PostsApi(defaultClient);
    String id = "id_example"; // String | 
    UpdatePostRequest updatePostRequest = new UpdatePostRequest(); // UpdatePostRequest | 
    try {
      UpdatePost200Response result = apiInstance.updatePost(id, updatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#updatePost");
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
| **id** | **String**|  | |
| **updatePostRequest** | [**UpdatePostRequest**](UpdatePostRequest.md)|  | [optional] |

### Return type

[**UpdatePost200Response**](UpdatePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | post updated |  -  |

