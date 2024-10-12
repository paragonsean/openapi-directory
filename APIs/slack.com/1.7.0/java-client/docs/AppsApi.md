# AppsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsEventAuthorizationsList_0**](AppsApi.md#appsEventAuthorizationsList_0) | **GET** /apps.event.authorizations.list |  |
| [**appsPermissionsInfo_0**](AppsApi.md#appsPermissionsInfo_0) | **GET** /apps.permissions.info |  |
| [**appsPermissionsRequest_0**](AppsApi.md#appsPermissionsRequest_0) | **GET** /apps.permissions.request |  |
| [**appsPermissionsResourcesList_0**](AppsApi.md#appsPermissionsResourcesList_0) | **GET** /apps.permissions.resources.list |  |
| [**appsPermissionsScopesList_0**](AppsApi.md#appsPermissionsScopesList_0) | **GET** /apps.permissions.scopes.list |  |
| [**appsPermissionsUsersList_0**](AppsApi.md#appsPermissionsUsersList_0) | **GET** /apps.permissions.users.list |  |
| [**appsPermissionsUsersRequest_0**](AppsApi.md#appsPermissionsUsersRequest_0) | **GET** /apps.permissions.users.request |  |
| [**appsUninstall**](AppsApi.md#appsUninstall) | **GET** /apps.uninstall |  |


<a id="appsEventAuthorizationsList_0"></a>
# **appsEventAuthorizationsList_0**
> DefaultSuccessTemplate appsEventAuthorizationsList_0(token, eventContext, cursor, limit)



Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `authorizations:read`
    String eventContext = "eventContext_example"; // String | 
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    try {
      DefaultSuccessTemplate result = apiInstance.appsEventAuthorizationsList_0(token, eventContext, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsEventAuthorizationsList_0");
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

<a id="appsPermissionsInfo_0"></a>
# **appsPermissionsInfo_0**
> AppsPermissionsInfoSchema appsPermissionsInfo_0(token)



Returns list of permissions this app has on a team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    try {
      AppsPermissionsInfoSchema result = apiInstance.appsPermissionsInfo_0(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsPermissionsInfo_0");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | [optional] |

### Return type

[**AppsPermissionsInfoSchema**](AppsPermissionsInfoSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Standard success response when used with a user token |  -  |
| **0** | Standard failure response when used with an invalid token |  -  |

<a id="appsPermissionsRequest_0"></a>
# **appsPermissionsRequest_0**
> AppsPermissionsRequestSchema appsPermissionsRequest_0(token, scopes, triggerId)



Allows an app to request additional scopes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String scopes = "scopes_example"; // String | A comma separated list of scopes to request for
    String triggerId = "triggerId_example"; // String | Token used to trigger the permissions API
    try {
      AppsPermissionsRequestSchema result = apiInstance.appsPermissionsRequest_0(token, scopes, triggerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsPermissionsRequest_0");
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
| **scopes** | **String**| A comma separated list of scopes to request for | |
| **triggerId** | **String**| Token used to trigger the permissions API | |

### Return type

[**AppsPermissionsRequestSchema**](AppsPermissionsRequestSchema.md)

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

<a id="appsPermissionsResourcesList_0"></a>
# **appsPermissionsResourcesList_0**
> AppsPermissionsResourcesListSuccessSchema appsPermissionsResourcesList_0(token, cursor, limit)



Returns list of resource grants this app has on a team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String cursor = "cursor_example"; // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
    Integer limit = 56; // Integer | The maximum number of items to return.
    try {
      AppsPermissionsResourcesListSuccessSchema result = apiInstance.appsPermissionsResourcesList_0(token, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsPermissionsResourcesList_0");
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

[**AppsPermissionsResourcesListSuccessSchema**](AppsPermissionsResourcesListSuccessSchema.md)

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

<a id="appsPermissionsScopesList_0"></a>
# **appsPermissionsScopesList_0**
> ApiPermissionsScopesListSuccessSchema appsPermissionsScopesList_0(token)



Returns list of scopes this app has on a team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    try {
      ApiPermissionsScopesListSuccessSchema result = apiInstance.appsPermissionsScopesList_0(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsPermissionsScopesList_0");
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

<a id="appsPermissionsUsersList_0"></a>
# **appsPermissionsUsersList_0**
> DefaultSuccessTemplate appsPermissionsUsersList_0(token, cursor, limit)



Returns list of user grants and corresponding scopes this app has on a team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String cursor = "cursor_example"; // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
    Integer limit = 56; // Integer | The maximum number of items to return.
    try {
      DefaultSuccessTemplate result = apiInstance.appsPermissionsUsersList_0(token, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsPermissionsUsersList_0");
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

<a id="appsPermissionsUsersRequest_0"></a>
# **appsPermissionsUsersRequest_0**
> DefaultSuccessTemplate appsPermissionsUsersRequest_0(token, scopes, triggerId, user)



Enables an app to trigger a permissions modal to grant an app access to a user access scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String scopes = "scopes_example"; // String | A comma separated list of user scopes to request for
    String triggerId = "triggerId_example"; // String | Token used to trigger the request
    String user = "user_example"; // String | The user this scope is being requested for
    try {
      DefaultSuccessTemplate result = apiInstance.appsPermissionsUsersRequest_0(token, scopes, triggerId, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsPermissionsUsersRequest_0");
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

<a id="appsUninstall"></a>
# **appsUninstall**
> AppsUninstallSchema appsUninstall(token, clientId, clientSecret)



Uninstalls your app from a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String clientId = "clientId_example"; // String | Issued when you created your application.
    String clientSecret = "clientSecret_example"; // String | Issued when you created your application.
    try {
      AppsUninstallSchema result = apiInstance.appsUninstall(token, clientId, clientSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsUninstall");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | [optional] |
| **clientId** | **String**| Issued when you created your application. | [optional] |
| **clientSecret** | **String**| Issued when you created your application. | [optional] |

### Return type

[**AppsUninstallSchema**](AppsUninstallSchema.md)

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

