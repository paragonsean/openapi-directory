# AppsPermissionsScopesApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsPermissionsScopesList**](AppsPermissionsScopesApi.md#appsPermissionsScopesList) | **GET** /apps.permissions.scopes.list |  |


<a id="appsPermissionsScopesList"></a>
# **appsPermissionsScopesList**
> ApiPermissionsScopesListSuccessSchema appsPermissionsScopesList(token)



Returns list of scopes this app has on a team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsPermissionsScopesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AppsPermissionsScopesApi apiInstance = new AppsPermissionsScopesApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    try {
      ApiPermissionsScopesListSuccessSchema result = apiInstance.appsPermissionsScopesList(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsPermissionsScopesApi#appsPermissionsScopesList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | |

### Return type

[**ApiPermissionsScopesListSuccessSchema**](ApiPermissionsScopesListSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical successful paginated response |  -  |
| **0** | Typical error response |  -  |

