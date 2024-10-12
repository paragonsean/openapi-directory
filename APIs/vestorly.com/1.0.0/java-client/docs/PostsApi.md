# PostsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPost**](PostsApi.md#createPost) | **POST** /posts |  |
| [**findPosts**](PostsApi.md#findPosts) | **GET** /posts |  |
| [**getPostByID**](PostsApi.md#getPostByID) | **GET** /posts/{id} |  |
| [**updatePostByID**](PostsApi.md#updatePostByID) | **PUT** /posts/{id} |  |


<a id="createPost"></a>
# **createPost**
> Postresponse createPost(vestorlyAuth, post, accessToken)



Create a new post in the Vestorly Platform

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    PostsApi apiInstance = new PostsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    PostInput post = new PostInput(); // PostInput | Post you want to create
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Postresponse result = apiInstance.createPost(vestorlyAuth, post, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#createPost");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **post** | [**PostInput**](PostInput.md)| Post you want to create | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Postresponse**](Postresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | posts response |  -  |

<a id="findPosts"></a>
# **findPosts**
> Posts findPosts(vestorlyAuth, accessToken, textQuery, externalUrl, isPublished)



Query all posts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    PostsApi apiInstance = new PostsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    String textQuery = "textQuery_example"; // String | Filter post by parameters
    String externalUrl = "externalUrl_example"; // String | Filter by External URL
    String isPublished = "isPublished_example"; // String | Filter by is_published boolean
    try {
      Posts result = apiInstance.findPosts(vestorlyAuth, accessToken, textQuery, externalUrl, isPublished);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#findPosts");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **accessToken** | **String**| OAuth Token | [optional] |
| **textQuery** | **String**| Filter post by parameters | [optional] |
| **externalUrl** | **String**| Filter by External URL | [optional] |
| **isPublished** | **String**| Filter by is_published boolean | [optional] |

### Return type

[**Posts**](Posts.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | posts response |  -  |

<a id="getPostByID"></a>
# **getPostByID**
> Postresponse getPostByID(vestorlyAuth, id, accessToken)



Query all posts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    PostsApi apiInstance = new PostsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | ID of post to fetch
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Postresponse result = apiInstance.getPostByID(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#getPostByID");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **id** | **String**| ID of post to fetch | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Postresponse**](Postresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | post response |  -  |

<a id="updatePostByID"></a>
# **updatePostByID**
> Postresponse updatePostByID(vestorlyAuth, id, post, accessToken)



Update A Post

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    PostsApi apiInstance = new PostsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | id of post to update
    Post post = new Post(); // Post | Post you want to update
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Postresponse result = apiInstance.updatePostByID(vestorlyAuth, id, post, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#updatePostByID");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **id** | **String**| id of post to update | |
| **post** | [**Post**](Post.md)| Post you want to update | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Postresponse**](Postresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | post response |  -  |

