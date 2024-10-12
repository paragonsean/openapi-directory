# WebhooksApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hookEventsGet**](WebhooksApi.md#hookEventsGet) | **GET** /hook_events | Get a webhook resource |
| [**hookEventsSubjectTypeGet**](WebhooksApi.md#hookEventsSubjectTypeGet) | **GET** /hook_events/{subject_type} | List subscribable webhook types |
| [**repositoriesWorkspaceRepoSlugHooksGet_0**](WebhooksApi.md#repositoriesWorkspaceRepoSlugHooksGet_0) | **GET** /repositories/{workspace}/{repo_slug}/hooks | List webhooks for a repository |
| [**repositoriesWorkspaceRepoSlugHooksPost_0**](WebhooksApi.md#repositoriesWorkspaceRepoSlugHooksPost_0) | **POST** /repositories/{workspace}/{repo_slug}/hooks | Create a webhook for a repository |
| [**repositoriesWorkspaceRepoSlugHooksUidDelete_0**](WebhooksApi.md#repositoriesWorkspaceRepoSlugHooksUidDelete_0) | **DELETE** /repositories/{workspace}/{repo_slug}/hooks/{uid} | Delete a webhook for a repository |
| [**repositoriesWorkspaceRepoSlugHooksUidGet_0**](WebhooksApi.md#repositoriesWorkspaceRepoSlugHooksUidGet_0) | **GET** /repositories/{workspace}/{repo_slug}/hooks/{uid} | Get a webhook for a repository |
| [**repositoriesWorkspaceRepoSlugHooksUidPut_0**](WebhooksApi.md#repositoriesWorkspaceRepoSlugHooksUidPut_0) | **PUT** /repositories/{workspace}/{repo_slug}/hooks/{uid} | Update a webhook for a repository |
| [**workspacesWorkspaceHooksGet_0**](WebhooksApi.md#workspacesWorkspaceHooksGet_0) | **GET** /workspaces/{workspace}/hooks | List webhooks for a workspace |
| [**workspacesWorkspaceHooksPost_0**](WebhooksApi.md#workspacesWorkspaceHooksPost_0) | **POST** /workspaces/{workspace}/hooks | Create a webhook for a workspace |
| [**workspacesWorkspaceHooksUidDelete_0**](WebhooksApi.md#workspacesWorkspaceHooksUidDelete_0) | **DELETE** /workspaces/{workspace}/hooks/{uid} | Delete a webhook for a workspace |
| [**workspacesWorkspaceHooksUidGet_0**](WebhooksApi.md#workspacesWorkspaceHooksUidGet_0) | **GET** /workspaces/{workspace}/hooks/{uid} | Get a webhook for a workspace |
| [**workspacesWorkspaceHooksUidPut_0**](WebhooksApi.md#workspacesWorkspaceHooksUidPut_0) | **PUT** /workspaces/{workspace}/hooks/{uid} | Update a webhook for a workspace |


<a id="hookEventsGet"></a>
# **hookEventsGet**
> SubjectTypes hookEventsGet()

Get a webhook resource

Returns the webhook resource or subject types on which webhooks can be registered.  Each resource/subject type contains an &#x60;events&#x60; link that returns the paginated list of specific events each individual subject type can emit.  This endpoint is publicly accessible and does not require authentication or scopes.  Example:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/hook_events  {     \&quot;repository\&quot;: {         \&quot;links\&quot;: {             \&quot;events\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/hook_events/repository\&quot;             }         }     },     \&quot;workspace\&quot;: {         \&quot;links\&quot;: {             \&quot;events\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/hook_events/workspace\&quot;             }         }     } } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    try {
      SubjectTypes result = apiInstance.hookEventsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#hookEventsGet");
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

[**SubjectTypes**](SubjectTypes.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A mapping of resource/subject types pointing to their individual event types. |  -  |

<a id="hookEventsSubjectTypeGet"></a>
# **hookEventsSubjectTypeGet**
> PaginatedHookEvents hookEventsSubjectTypeGet(subjectType)

List subscribable webhook types

Returns a paginated list of all valid webhook events for the specified entity. **The team and user webhooks are deprecated, and you should use workspace instead. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).**  This is public data that does not require any scopes or authentication.  Example:  NOTE: The following example is a truncated response object for the &#x60;workspace&#x60; &#x60;subject_type&#x60;. We return the same structure for the other &#x60;subject_type&#x60; objects.  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/hook_events/workspace {     \&quot;page\&quot;: 1,     \&quot;pagelen\&quot;: 30,     \&quot;size\&quot;: 21,     \&quot;values\&quot;: [         {             \&quot;category\&quot;: \&quot;Repository\&quot;,             \&quot;description\&quot;: \&quot;Whenever a repository push occurs\&quot;,             \&quot;event\&quot;: \&quot;repo:push\&quot;,             \&quot;label\&quot;: \&quot;Push\&quot;         },         {             \&quot;category\&quot;: \&quot;Repository\&quot;,             \&quot;description\&quot;: \&quot;Whenever a repository fork occurs\&quot;,             \&quot;event\&quot;: \&quot;repo:fork\&quot;,             \&quot;label\&quot;: \&quot;Fork\&quot;         },         {             \&quot;category\&quot;: \&quot;Repository\&quot;,             \&quot;description\&quot;: \&quot;Whenever a repository import occurs\&quot;,             \&quot;event\&quot;: \&quot;repo:imported\&quot;,             \&quot;label\&quot;: \&quot;Import\&quot;         },         ...         {             \&quot;category\&quot;:\&quot;Pull Request\&quot;,             \&quot;label\&quot;:\&quot;Approved\&quot;,             \&quot;description\&quot;:\&quot;When someone has approved a pull request\&quot;,             \&quot;event\&quot;:\&quot;pullrequest:approved\&quot;         },     ] } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String subjectType = "repository"; // String | A resource or subject type.
    try {
      PaginatedHookEvents result = apiInstance.hookEventsSubjectTypeGet(subjectType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#hookEventsSubjectTypeGet");
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
| **subjectType** | **String**| A resource or subject type. | [enum: repository, workspace] |

### Return type

[**PaginatedHookEvents**](PaginatedHookEvents.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of webhook types available to subscribe on. |  -  |
| **404** | If an invalid &#x60;{subject_type}&#x60; value was specified. |  -  |

<a id="repositoriesWorkspaceRepoSlugHooksGet_0"></a>
# **repositoriesWorkspaceRepoSlugHooksGet_0**
> PaginatedWebhookSubscriptions repositoriesWorkspaceRepoSlugHooksGet_0(repoSlug, workspace)

List webhooks for a repository

Returns a paginated list of webhooks installed on this repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedWebhookSubscriptions result = apiInstance.repositoriesWorkspaceRepoSlugHooksGet_0(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#repositoriesWorkspaceRepoSlugHooksGet_0");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**PaginatedWebhookSubscriptions**](PaginatedWebhookSubscriptions.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The paginated list of installed webhooks. |  -  |
| **403** | If the authenticated user does not have permission to access the webhooks. |  -  |
| **404** | If the repository does not exist. |  -  |

<a id="repositoriesWorkspaceRepoSlugHooksPost_0"></a>
# **repositoriesWorkspaceRepoSlugHooksPost_0**
> WebhookSubscription repositoriesWorkspaceRepoSlugHooksPost_0(repoSlug, workspace)

Create a webhook for a repository

Creates a new webhook on the specified repository.  Example:  &#x60;&#x60;&#x60; $ curl -X POST -u credentials -H &#39;Content-Type: application/json&#39;   https://api.bitbucket.org/2.0/repositories/my-workspace/my-repo-slug/hooks   -d &#39;     {       \&quot;description\&quot;: \&quot;Webhook Description\&quot;,       \&quot;url\&quot;: \&quot;https://example.com/\&quot;,       \&quot;active\&quot;: true,       \&quot;events\&quot;: [         \&quot;repo:push\&quot;,         \&quot;issue:created\&quot;,         \&quot;issue:updated\&quot;       ]     }&#39; &#x60;&#x60;&#x60;  Note that this call requires the webhook scope, as well as any scope that applies to the events that the webhook subscribes to. In the example above that means: &#x60;webhook&#x60;, &#x60;repository&#x60; and &#x60;issue&#x60;.  Also note that the &#x60;url&#x60; must properly resolve and cannot be an internal, non-routed address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      WebhookSubscription result = apiInstance.repositoriesWorkspaceRepoSlugHooksPost_0(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#repositoriesWorkspaceRepoSlugHooksPost_0");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | If the webhook was registered successfully. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **403** | If the authenticated user does not have permission to install webhooks on the specified repository. |  -  |
| **404** | If the repository does not exist. |  -  |

<a id="repositoriesWorkspaceRepoSlugHooksUidDelete_0"></a>
# **repositoriesWorkspaceRepoSlugHooksUidDelete_0**
> repositoriesWorkspaceRepoSlugHooksUidDelete_0(repoSlug, uid, workspace)

Delete a webhook for a repository

Deletes the specified webhook subscription from the given repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String uid = "uid_example"; // String | Installed webhook's ID
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugHooksUidDelete_0(repoSlug, uid, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#repositoriesWorkspaceRepoSlugHooksUidDelete_0");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **uid** | **String**| Installed webhook&#39;s ID | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | When the webhook was deleted successfully |  -  |
| **403** | If the authenticated user does not have permission to delete the webhook. |  -  |
| **404** | If the webhook or repository does not exist. |  -  |

<a id="repositoriesWorkspaceRepoSlugHooksUidGet_0"></a>
# **repositoriesWorkspaceRepoSlugHooksUidGet_0**
> WebhookSubscription repositoriesWorkspaceRepoSlugHooksUidGet_0(repoSlug, uid, workspace)

Get a webhook for a repository

Returns the webhook with the specified id installed on the specified repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String uid = "uid_example"; // String | Installed webhook's ID
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      WebhookSubscription result = apiInstance.repositoriesWorkspaceRepoSlugHooksUidGet_0(repoSlug, uid, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#repositoriesWorkspaceRepoSlugHooksUidGet_0");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **uid** | **String**| Installed webhook&#39;s ID | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The webhook subscription object. |  -  |
| **404** | If the webhook or repository does not exist. |  -  |

<a id="repositoriesWorkspaceRepoSlugHooksUidPut_0"></a>
# **repositoriesWorkspaceRepoSlugHooksUidPut_0**
> WebhookSubscription repositoriesWorkspaceRepoSlugHooksUidPut_0(repoSlug, uid, workspace)

Update a webhook for a repository

Updates the specified webhook subscription.  The following properties can be mutated:  * &#x60;description&#x60; * &#x60;url&#x60; * &#x60;active&#x60; * &#x60;events&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String uid = "uid_example"; // String | Installed webhook's ID
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      WebhookSubscription result = apiInstance.repositoriesWorkspaceRepoSlugHooksUidPut_0(repoSlug, uid, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#repositoriesWorkspaceRepoSlugHooksUidPut_0");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **uid** | **String**| Installed webhook&#39;s ID | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The webhook subscription object. |  -  |
| **403** | If the authenticated user does not have permission to update the webhook. |  -  |
| **404** | If the webhook or repository does not exist. |  -  |

<a id="workspacesWorkspaceHooksGet_0"></a>
# **workspacesWorkspaceHooksGet_0**
> PaginatedWebhookSubscriptions workspacesWorkspaceHooksGet_0(workspace)

List webhooks for a workspace

Returns a paginated list of webhooks installed on this workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedWebhookSubscriptions result = apiInstance.workspacesWorkspaceHooksGet_0(workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#workspacesWorkspaceHooksGet_0");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**PaginatedWebhookSubscriptions**](PaginatedWebhookSubscriptions.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The paginated list of installed webhooks. |  -  |
| **403** | If the authenticated user is not an owner on the specified workspace. |  -  |
| **404** | If the specified workspace does not exist. |  -  |

<a id="workspacesWorkspaceHooksPost_0"></a>
# **workspacesWorkspaceHooksPost_0**
> WebhookSubscription workspacesWorkspaceHooksPost_0(workspace)

Create a webhook for a workspace

Creates a new webhook on the specified workspace.  Workspace webhooks are fired for events from all repositories contained by that workspace.  Example:  &#x60;&#x60;&#x60; $ curl -X POST -u credentials -H &#39;Content-Type: application/json&#39;   https://api.bitbucket.org/2.0/workspaces/my-workspace/hooks   -d &#39;     {       \&quot;description\&quot;: \&quot;Webhook Description\&quot;,       \&quot;url\&quot;: \&quot;https://example.com/\&quot;,       \&quot;active\&quot;: true,       \&quot;events\&quot;: [         \&quot;repo:push\&quot;,         \&quot;issue:created\&quot;,         \&quot;issue:updated\&quot;       ]     }&#39; &#x60;&#x60;&#x60;  This call requires the webhook scope, as well as any scope that applies to the events that the webhook subscribes to. In the example above that means: &#x60;webhook&#x60;, &#x60;repository&#x60; and &#x60;issue&#x60;.  The &#x60;url&#x60; must properly resolve and cannot be an internal, non-routed address.  Only workspace owners can install webhooks on workspaces.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      WebhookSubscription result = apiInstance.workspacesWorkspaceHooksPost_0(workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#workspacesWorkspaceHooksPost_0");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | If the webhook was registered successfully. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **403** | If the authenticated user does not have permission to install webhooks on the specified workspace. |  -  |
| **404** | If the specified workspace does not exist. |  -  |

<a id="workspacesWorkspaceHooksUidDelete_0"></a>
# **workspacesWorkspaceHooksUidDelete_0**
> workspacesWorkspaceHooksUidDelete_0(uid, workspace)

Delete a webhook for a workspace

Deletes the specified webhook subscription from the given workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String uid = "uid_example"; // String | Installed webhook's ID
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.workspacesWorkspaceHooksUidDelete_0(uid, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#workspacesWorkspaceHooksUidDelete_0");
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
| **uid** | **String**| Installed webhook&#39;s ID | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | When the webhook was deleted successfully |  -  |
| **403** | If the authenticated user does not have permission to delete the webhook. |  -  |
| **404** | If the webhook or workspace does not exist. |  -  |

<a id="workspacesWorkspaceHooksUidGet_0"></a>
# **workspacesWorkspaceHooksUidGet_0**
> WebhookSubscription workspacesWorkspaceHooksUidGet_0(uid, workspace)

Get a webhook for a workspace

Returns the webhook with the specified id installed on the given workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String uid = "uid_example"; // String | Installed webhook's ID
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      WebhookSubscription result = apiInstance.workspacesWorkspaceHooksUidGet_0(uid, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#workspacesWorkspaceHooksUidGet_0");
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
| **uid** | **String**| Installed webhook&#39;s ID | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The webhook subscription object. |  -  |
| **404** | If the webhook or workspace does not exist. |  -  |

<a id="workspacesWorkspaceHooksUidPut_0"></a>
# **workspacesWorkspaceHooksUidPut_0**
> WebhookSubscription workspacesWorkspaceHooksUidPut_0(uid, workspace)

Update a webhook for a workspace

Updates the specified webhook subscription.  The following properties can be mutated:  * &#x60;description&#x60; * &#x60;url&#x60; * &#x60;active&#x60; * &#x60;events&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String uid = "uid_example"; // String | Installed webhook's ID
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      WebhookSubscription result = apiInstance.workspacesWorkspaceHooksUidPut_0(uid, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#workspacesWorkspaceHooksUidPut_0");
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
| **uid** | **String**| Installed webhook&#39;s ID | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The webhook subscription object. |  -  |
| **403** | If the authenticated user does not have permission to update the webhook. |  -  |
| **404** | If the webhook or workspace does not exist. |  -  |

