# SearchApi

All URIs are relative to *https://api.illumidesk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**search**](SearchApi.md#search) | **GET** /v1/{namespace}/search/ | Get a search results |


<a id="search"></a>
# **search**
> List&lt;Object&gt; search(namespace, q, type, limit, offset)

Get a search results

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String q = "q_example"; // String | Search string.
    String type = "users"; // String | Limit results to specific types.
    String limit = "limit_example"; // String | Limit data when getting items.
    String offset = "offset_example"; // String | Offset data when getting items.
    try {
      List<Object> result = apiInstance.search(namespace, q, type, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#search");
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
| **namespace** | **String**| User or team name. | |
| **q** | **String**| Search string. | |
| **type** | **String**| Limit results to specific types. | [optional] [enum: users, projects, servers] |
| **limit** | **String**| Limit data when getting items. | [optional] |
| **offset** | **String**| Offset data when getting items. | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search list. |  -  |

