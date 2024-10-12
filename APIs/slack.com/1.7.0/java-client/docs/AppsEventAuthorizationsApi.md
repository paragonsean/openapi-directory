# AppsEventAuthorizationsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsEventAuthorizationsList**](AppsEventAuthorizationsApi.md#appsEventAuthorizationsList) | **GET** /apps.event.authorizations.list |  |


<a id="appsEventAuthorizationsList"></a>
# **appsEventAuthorizationsList**
> DefaultSuccessTemplate appsEventAuthorizationsList(token, eventContext, cursor, limit)



Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsEventAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AppsEventAuthorizationsApi apiInstance = new AppsEventAuthorizationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `authorizations:read`
    String eventContext = "eventContext_example"; // String | 
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    try {
      DefaultSuccessTemplate result = apiInstance.appsEventAuthorizationsList(token, eventContext, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsEventAuthorizationsApi#appsEventAuthorizationsList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;authorizations:read&#x60; | |
| **eventContext** | **String**|  | |
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

