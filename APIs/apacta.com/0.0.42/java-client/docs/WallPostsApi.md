# WallPostsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**wallPostsGet**](WallPostsApi.md#wallPostsGet) | **GET** /wall_posts | View list of wall posts |
| [**wallPostsPost**](WallPostsApi.md#wallPostsPost) | **POST** /wall_posts | Add a wall post |
| [**wallPostsWallPostIdGet**](WallPostsApi.md#wallPostsWallPostIdGet) | **GET** /wall_posts/{wall_post_id} | View wall post |
| [**wallPostsWallPostIdWallCommentsGet**](WallPostsApi.md#wallPostsWallPostIdWallCommentsGet) | **GET** /wall_posts/{wall_post_id}/wall_comments | See wall comments to a wall post |


<a id="wallPostsGet"></a>
# **wallPostsGet**
> WallPostsGet200Response wallPostsGet(projectId, userId)

View list of wall posts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WallPostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    WallPostsApi apiInstance = new WallPostsApi(defaultClient);
    UUID projectId = UUID.randomUUID(); // UUID | 
    UUID userId = UUID.randomUUID(); // UUID | 
    try {
      WallPostsGet200Response result = apiInstance.wallPostsGet(projectId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WallPostsApi#wallPostsGet");
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
| **projectId** | **UUID**|  | [optional] |
| **userId** | **UUID**|  | [optional] |

### Return type

[**WallPostsGet200Response**](WallPostsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Not authorized to access project |  -  |
| **404** | Project not found |  -  |

<a id="wallPostsPost"></a>
# **wallPostsPost**
> ClockingRecordsPost201Response wallPostsPost(wallPostsPostRequest)

Add a wall post

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WallPostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    WallPostsApi apiInstance = new WallPostsApi(defaultClient);
    WallPostsPostRequest wallPostsPostRequest = new WallPostsPostRequest(); // WallPostsPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.wallPostsPost(wallPostsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WallPostsApi#wallPostsPost");
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
| **wallPostsPostRequest** | [**WallPostsPostRequest**](WallPostsPostRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **422** | Validation error |  -  |

<a id="wallPostsWallPostIdGet"></a>
# **wallPostsWallPostIdGet**
> WallPostsWallPostIdGet200Response wallPostsWallPostIdGet(wallPostId)

View wall post

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WallPostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    WallPostsApi apiInstance = new WallPostsApi(defaultClient);
    String wallPostId = "wallPostId_example"; // String | 
    try {
      WallPostsWallPostIdGet200Response result = apiInstance.wallPostsWallPostIdGet(wallPostId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WallPostsApi#wallPostsWallPostIdGet");
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
| **wallPostId** | **String**|  | |

### Return type

[**WallPostsWallPostIdGet200Response**](WallPostsWallPostIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="wallPostsWallPostIdWallCommentsGet"></a>
# **wallPostsWallPostIdWallCommentsGet**
> WallPostsWallPostIdWallCommentsGet200Response wallPostsWallPostIdWallCommentsGet(wallPostId)

See wall comments to a wall post

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WallPostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    WallPostsApi apiInstance = new WallPostsApi(defaultClient);
    String wallPostId = "wallPostId_example"; // String | 
    try {
      WallPostsWallPostIdWallCommentsGet200Response result = apiInstance.wallPostsWallPostIdWallCommentsGet(wallPostId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WallPostsApi#wallPostsWallPostIdWallCommentsGet");
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
| **wallPostId** | **String**|  | |

### Return type

[**WallPostsWallPostIdWallCommentsGet200Response**](WallPostsWallPostIdWallCommentsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Not authorized to access project |  -  |
| **404** | Wall post not found |  -  |

