# AppsPermissionsUsersApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsPermissionsUsersList**](AppsPermissionsUsersApi.md#appsPermissionsUsersList) | **GET** /apps.permissions.users.list |  |
| [**appsPermissionsUsersRequest**](AppsPermissionsUsersApi.md#appsPermissionsUsersRequest) | **GET** /apps.permissions.users.request |  |


<a id="appsPermissionsUsersList"></a>
# **appsPermissionsUsersList**
> DefaultSuccessTemplate appsPermissionsUsersList(token, cursor, limit)



Returns list of user grants and corresponding scopes this app has on a team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsPermissionsUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AppsPermissionsUsersApi apiInstance = new AppsPermissionsUsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String cursor = "cursor_example"; // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
    Integer limit = 56; // Integer | The maximum number of items to return.
    try {
      DefaultSuccessTemplate result = apiInstance.appsPermissionsUsersList(token, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsPermissionsUsersApi#appsPermissionsUsersList");
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
| **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] |
| **limit** | **Integer**| The maximum number of items to return. | [optional] |

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
| **200** | Typical successful paginated response |  -  |
| **0** | Typical error response |  -  |

<a id="appsPermissionsUsersRequest"></a>
# **appsPermissionsUsersRequest**
> DefaultSuccessTemplate appsPermissionsUsersRequest(token, scopes, triggerId, user)



Enables an app to trigger a permissions modal to grant an app access to a user access scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsPermissionsUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AppsPermissionsUsersApi apiInstance = new AppsPermissionsUsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String scopes = "scopes_example"; // String | A comma separated list of user scopes to request for
    String triggerId = "triggerId_example"; // String | Token used to trigger the request
    String user = "user_example"; // String | The user this scope is being requested for
    try {
      DefaultSuccessTemplate result = apiInstance.appsPermissionsUsersRequest(token, scopes, triggerId, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsPermissionsUsersApi#appsPermissionsUsersRequest");
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
| **scopes** | **String**| A comma separated list of user scopes to request for | |
| **triggerId** | **String**| Token used to trigger the request | |
| **user** | **String**| The user this scope is being requested for | |

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
| **200** | Standard success response when used with a user token |  -  |
| **0** | Standard failure response when trigger_id is invalid |  -  |

