# FollowedTagsApi

All URIs are relative to *https://dev.to/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFollowedTags**](FollowedTagsApi.md#getFollowedTags) | **GET** /api/follows/tags | Followed Tags |


<a id="getFollowedTags"></a>
# **getFollowedTags**
> List&lt;FollowedTag&gt; getFollowedTags()

Followed Tags

This endpoint allows the client to retrieve a list of the tags they follow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FollowedTagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    FollowedTagsApi apiInstance = new FollowedTagsApi(defaultClient);
    try {
      List<FollowedTag> result = apiInstance.getFollowedTags();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FollowedTagsApi#getFollowedTags");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;FollowedTag&gt;**](FollowedTag.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of followed tags |  -  |
| **401** | unauthorized |  -  |

