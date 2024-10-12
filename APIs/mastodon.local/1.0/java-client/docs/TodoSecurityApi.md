# TodoSecurityApi

All URIs are relative to *http://mastodon.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1AccountsPost**](TodoSecurityApi.md#apiV1AccountsPost) | **POST** /api/v1/accounts |  |


<a id="apiV1AccountsPost"></a>
# **apiV1AccountsPost**
> apiV1AccountsPost(apiV1AccountsPostRequest)



Creates a user and account records. Returns an account access token for the app that initiated the request. The app should save this token for later, and should wait for the user to confirm their account by clicking a link in their email inbox.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TodoSecurityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    TodoSecurityApi apiInstance = new TodoSecurityApi(defaultClient);
    ApiV1AccountsPostRequest apiV1AccountsPostRequest = new ApiV1AccountsPostRequest(); // ApiV1AccountsPostRequest | 
    try {
      apiInstance.apiV1AccountsPost(apiV1AccountsPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TodoSecurityApi#apiV1AccountsPost");
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
| **apiV1AccountsPostRequest** | [**ApiV1AccountsPostRequest**](ApiV1AccountsPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

