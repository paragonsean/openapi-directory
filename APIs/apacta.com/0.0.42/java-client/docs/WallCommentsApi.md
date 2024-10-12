# WallCommentsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**wallCommentsPost**](WallCommentsApi.md#wallCommentsPost) | **POST** /wall_comments | Add wall comment |
| [**wallCommentsWallCommentIdGet**](WallCommentsApi.md#wallCommentsWallCommentIdGet) | **GET** /wall_comments/{wall_comment_id} | View wall comment |


<a id="wallCommentsPost"></a>
# **wallCommentsPost**
> ClockingRecordsPost201Response wallCommentsPost(wallCommentsPostRequest)

Add wall comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WallCommentsApi;

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

    WallCommentsApi apiInstance = new WallCommentsApi(defaultClient);
    WallCommentsPostRequest wallCommentsPostRequest = new WallCommentsPostRequest(); // WallCommentsPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.wallCommentsPost(wallCommentsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WallCommentsApi#wallCommentsPost");
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
| **wallCommentsPostRequest** | [**WallCommentsPostRequest**](WallCommentsPostRequest.md)|  | [optional] |

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

<a id="wallCommentsWallCommentIdGet"></a>
# **wallCommentsWallCommentIdGet**
> WallCommentsWallCommentIdGet200Response wallCommentsWallCommentIdGet(wallCommentId)

View wall comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WallCommentsApi;

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

    WallCommentsApi apiInstance = new WallCommentsApi(defaultClient);
    String wallCommentId = "wallCommentId_example"; // String | 
    try {
      WallCommentsWallCommentIdGet200Response result = apiInstance.wallCommentsWallCommentIdGet(wallCommentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WallCommentsApi#wallCommentsWallCommentIdGet");
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
| **wallCommentId** | **String**|  | |

### Return type

[**WallCommentsWallCommentIdGet200Response**](WallCommentsWallCommentIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

