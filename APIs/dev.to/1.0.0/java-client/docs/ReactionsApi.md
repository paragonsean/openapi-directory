# ReactionsApi

All URIs are relative to *https://dev.to/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiReactionsPost**](ReactionsApi.md#apiReactionsPost) | **POST** /api/reactions | create reaction |
| [**apiReactionsTogglePost**](ReactionsApi.md#apiReactionsTogglePost) | **POST** /api/reactions/toggle | toggle reaction |


<a id="apiReactionsPost"></a>
# **apiReactionsPost**
> apiReactionsPost(category, reactableId, reactableType)

create reaction

This endpoint allows the client to create a reaction to a specified reactable (eg, Article, Comment, or User). For examples:         * \&quot;Like\&quot;ing an Article will create a new \&quot;like\&quot; Reaction from the user for that Articles         * \&quot;Like\&quot;ing that Article a second time will return the previous \&quot;like\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String category = "like"; // String | 
    Integer reactableId = 56; // Integer | 
    String reactableType = "Comment"; // String | 
    try {
      apiInstance.apiReactionsPost(category, reactableId, reactableType);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#apiReactionsPost");
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
| **category** | **String**|  | [enum: like, unicorn, exploding_head, raised_hands, fire] |
| **reactableId** | **Integer**|  | |
| **reactableType** | **String**|  | [enum: Comment, Article, User] |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |

<a id="apiReactionsTogglePost"></a>
# **apiReactionsTogglePost**
> apiReactionsTogglePost(category, reactableId, reactableType)

toggle reaction

This endpoint allows the client to toggle the user&#39;s reaction to a specified reactable (eg, Article, Comment, or User). For examples:         * \&quot;Like\&quot;ing an Article will create a new \&quot;like\&quot; Reaction from the user for that Articles         * \&quot;Like\&quot;ing that Article a second time will remove the \&quot;like\&quot; from the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String category = "like"; // String | 
    Integer reactableId = 56; // Integer | 
    String reactableType = "Comment"; // String | 
    try {
      apiInstance.apiReactionsTogglePost(category, reactableId, reactableType);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#apiReactionsTogglePost");
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
| **category** | **String**|  | [enum: like, unicorn, exploding_head, raised_hands, fire] |
| **reactableId** | **Integer**|  | |
| **reactableType** | **String**|  | [enum: Comment, Article, User] |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |

