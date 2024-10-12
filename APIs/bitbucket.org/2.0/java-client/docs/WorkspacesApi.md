# WorkspacesApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userPermissionsWorkspacesGet**](WorkspacesApi.md#userPermissionsWorkspacesGet) | **GET** /user/permissions/workspaces | List workspaces for the current user |
| [**workspacesGet**](WorkspacesApi.md#workspacesGet) | **GET** /workspaces | List workspaces for user |
| [**workspacesWorkspaceGet**](WorkspacesApi.md#workspacesWorkspaceGet) | **GET** /workspaces/{workspace} | Get a workspace |
| [**workspacesWorkspaceHooksGet**](WorkspacesApi.md#workspacesWorkspaceHooksGet) | **GET** /workspaces/{workspace}/hooks | List webhooks for a workspace |
| [**workspacesWorkspaceHooksPost**](WorkspacesApi.md#workspacesWorkspaceHooksPost) | **POST** /workspaces/{workspace}/hooks | Create a webhook for a workspace |
| [**workspacesWorkspaceHooksUidDelete**](WorkspacesApi.md#workspacesWorkspaceHooksUidDelete) | **DELETE** /workspaces/{workspace}/hooks/{uid} | Delete a webhook for a workspace |
| [**workspacesWorkspaceHooksUidGet**](WorkspacesApi.md#workspacesWorkspaceHooksUidGet) | **GET** /workspaces/{workspace}/hooks/{uid} | Get a webhook for a workspace |
| [**workspacesWorkspaceHooksUidPut**](WorkspacesApi.md#workspacesWorkspaceHooksUidPut) | **PUT** /workspaces/{workspace}/hooks/{uid} | Update a webhook for a workspace |
| [**workspacesWorkspaceMembersGet**](WorkspacesApi.md#workspacesWorkspaceMembersGet) | **GET** /workspaces/{workspace}/members | List users in a workspace |
| [**workspacesWorkspaceMembersMemberGet**](WorkspacesApi.md#workspacesWorkspaceMembersMemberGet) | **GET** /workspaces/{workspace}/members/{member} | Get user membership for a workspace |
| [**workspacesWorkspacePermissionsGet**](WorkspacesApi.md#workspacesWorkspacePermissionsGet) | **GET** /workspaces/{workspace}/permissions | List user permissions in a workspace |
| [**workspacesWorkspacePermissionsRepositoriesGet**](WorkspacesApi.md#workspacesWorkspacePermissionsRepositoriesGet) | **GET** /workspaces/{workspace}/permissions/repositories | List all repository permissions for a workspace |
| [**workspacesWorkspacePermissionsRepositoriesRepoSlugGet**](WorkspacesApi.md#workspacesWorkspacePermissionsRepositoriesRepoSlugGet) | **GET** /workspaces/{workspace}/permissions/repositories/{repo_slug} | List a repository permissions for a workspace |
| [**workspacesWorkspaceProjectsGet**](WorkspacesApi.md#workspacesWorkspaceProjectsGet) | **GET** /workspaces/{workspace}/projects | List projects in a workspace |
| [**workspacesWorkspaceProjectsProjectKeyGet_0**](WorkspacesApi.md#workspacesWorkspaceProjectsProjectKeyGet_0) | **GET** /workspaces/{workspace}/projects/{project_key} | Get a project for a workspace |


<a id="userPermissionsWorkspacesGet"></a>
# **userPermissionsWorkspacesGet**
> PaginatedWorkspaceMemberships userPermissionsWorkspacesGet(q, sort)

List workspaces for the current user

Returns an object for each workspace the caller is a member of, and their effective role - the highest level of privilege the caller has. If a user is a member of multiple groups with distinct roles, only the highest level is returned.  Permissions can be:  * &#x60;owner&#x60; * &#x60;collaborator&#x60; * &#x60;member&#x60;  **The &#x60;collaborator&#x60; role is being removed from the Bitbucket Cloud API. For more information, see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**  Example:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/user/permissions/workspaces  {   \&quot;pagelen\&quot;: 10,   \&quot;page\&quot;: 1,   \&quot;size\&quot;: 1,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;workspace_membership\&quot;,       \&quot;permission\&quot;: \&quot;owner\&quot;,       \&quot;last_accessed\&quot;: \&quot;2019-03-07T12:35:02.900024+00:00\&quot;,       \&quot;added_on\&quot;: \&quot;2018-10-11T17:42:02.961424+00:00\&quot;,       \&quot;user\&quot;: {         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;uuid\&quot;: \&quot;{470c176d-3574-44ea-bb41-89e8638bcca4}\&quot;,         \&quot;nickname\&quot;: \&quot;evzijst\&quot;,         \&quot;display_name\&quot;: \&quot;Erik van Zijst\&quot;,       },       \&quot;workspace\&quot;: {         \&quot;type\&quot;: \&quot;workspace\&quot;,         \&quot;uuid\&quot;: \&quot;{a15fb181-db1f-48f7-b41f-e1eff06929d6}\&quot;,         \&quot;slug\&quot;: \&quot;bbworkspace1\&quot;,         \&quot;name\&quot;: \&quot;Atlassian Bitbucket\&quot;,       }     }   ] } &#x60;&#x60;&#x60;  Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by workspace or permission by adding the following query string parameters:  * &#x60;q&#x3D;workspace.slug&#x3D;\&quot;bbworkspace1\&quot;&#x60; or &#x60;q&#x3D;permission&#x3D;\&quot;owner\&quot;&#x60; * &#x60;sort&#x3D;workspace.slug&#x60;  Note that the query parameter values need to be URL escaped so that &#x60;&#x3D;&#x60; would become &#x60;%3D&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String q = "q_example"; // String |  Query string to narrow down the response. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for details.
    String sort = "sort_example"; // String |  Name of a response property to sort results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results) for details. 
    try {
      PaginatedWorkspaceMemberships result = apiInstance.userPermissionsWorkspacesGet(q, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#userPermissionsWorkspacesGet");
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
| **q** | **String**|  Query string to narrow down the response. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for details. | [optional] |
| **sort** | **String**|  Name of a response property to sort results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results) for details.  | [optional] |

### Return type

[**PaginatedWorkspaceMemberships**](PaginatedWorkspaceMemberships.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All of the workspace memberships for the authenticated user. |  -  |
| **401** | The request wasn&#39;t authenticated. |  -  |

<a id="workspacesGet"></a>
# **workspacesGet**
> PaginatedWorkspaces workspacesGet(role, q, sort)

List workspaces for user

Returns a list of workspaces accessible by the authenticated user.  Example:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/workspaces  {   \&quot;pagelen\&quot;: 10,   \&quot;page\&quot;: 1,   \&quot;size\&quot;: 1,   \&quot;values\&quot;: [     {         \&quot;uuid\&quot;: \&quot;{a15fb181-db1f-48f7-b41f-e1eff06929d6}\&quot;,         \&quot;links\&quot;: {             \&quot;owners\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/workspaces/bbworkspace1/members?q&#x3D;permission%3D%22owner%22\&quot;             },             \&quot;self\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/workspaces/bbworkspace1\&quot;             },             \&quot;repositories\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/bbworkspace1\&quot;             },             \&quot;snippets\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/snippets/bbworkspace1\&quot;             },             \&quot;html\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/bbworkspace1/\&quot;             },             \&quot;avatar\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/workspaces/bbworkspace1/avatar/?ts&#x3D;1543465801\&quot;             },             \&quot;members\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/workspaces/bbworkspace1/members\&quot;             },             \&quot;projects\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/workspaces/bbworkspace1/projects\&quot;             }         },         \&quot;created_on\&quot;: \&quot;2018-11-14T19:15:05.058566+00:00\&quot;,         \&quot;type\&quot;: \&quot;workspace\&quot;,         \&quot;slug\&quot;: \&quot;bbworkspace1\&quot;,         \&quot;is_private\&quot;: true,         \&quot;name\&quot;: \&quot;Atlassian Bitbucket\&quot;     }   ] } &#x60;&#x60;&#x60;  Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by workspace or permission by adding the following query string parameters:  * &#x60;q&#x3D;slug&#x3D;\&quot;bbworkspace1\&quot;&#x60; or &#x60;q&#x3D;is_private&#x3D;true&#x60; * &#x60;sort&#x3D;created_on&#x60;  Note that the query parameter values need to be URL escaped so that &#x60;&#x3D;&#x60; would become &#x60;%3D&#x60;.  **The &#x60;collaborator&#x60; role is being removed from the Bitbucket Cloud API. For more information, see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String role = "owner"; // String |              Filters the workspaces based on the authenticated user's role on each workspace.              * **member**: returns a list of all the workspaces which the caller is a member of                 at least one workspace group or repository             * **collaborator**: returns a list of workspaces which the caller has write access                 to at least one repository in the workspace             * **owner**: returns a list of workspaces which the caller has administrator access             
    String q = "q_example"; // String |  Query string to narrow down the response. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for details.
    String sort = "sort_example"; // String |  Name of a response property to sort results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results) for details. 
    try {
      PaginatedWorkspaces result = apiInstance.workspacesGet(role, q, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesGet");
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
| **role** | **String**|              Filters the workspaces based on the authenticated user&#39;s role on each workspace.              * **member**: returns a list of all the workspaces which the caller is a member of                 at least one workspace group or repository             * **collaborator**: returns a list of workspaces which the caller has write access                 to at least one repository in the workspace             * **owner**: returns a list of workspaces which the caller has administrator access              | [optional] [enum: owner, collaborator, member] |
| **q** | **String**|  Query string to narrow down the response. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for details. | [optional] |
| **sort** | **String**|  Name of a response property to sort results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results) for details.  | [optional] |

### Return type

[**PaginatedWorkspaces**](PaginatedWorkspaces.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of workspaces accessible by the authenticated user. |  -  |
| **401** | The request wasn&#39;t authenticated. |  -  |

<a id="workspacesWorkspaceGet"></a>
# **workspacesWorkspaceGet**
> Workspace workspacesWorkspaceGet(workspace)

Get a workspace

Returns the requested workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Workspace result = apiInstance.workspacesWorkspaceGet(workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspaceGet");
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

[**Workspace**](Workspace.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The workspace. |  -  |
| **404** | If no workspace exists for the specified name or UUID. |  -  |

<a id="workspacesWorkspaceHooksGet"></a>
# **workspacesWorkspaceHooksGet**
> PaginatedWebhookSubscriptions workspacesWorkspaceHooksGet(workspace)

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
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedWebhookSubscriptions result = apiInstance.workspacesWorkspaceHooksGet(workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspaceHooksGet");
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

<a id="workspacesWorkspaceHooksPost"></a>
# **workspacesWorkspaceHooksPost**
> WebhookSubscription workspacesWorkspaceHooksPost(workspace)

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
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      WebhookSubscription result = apiInstance.workspacesWorkspaceHooksPost(workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspaceHooksPost");
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

<a id="workspacesWorkspaceHooksUidDelete"></a>
# **workspacesWorkspaceHooksUidDelete**
> workspacesWorkspaceHooksUidDelete(uid, workspace)

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
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String uid = "uid_example"; // String | Installed webhook's ID
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.workspacesWorkspaceHooksUidDelete(uid, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspaceHooksUidDelete");
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

<a id="workspacesWorkspaceHooksUidGet"></a>
# **workspacesWorkspaceHooksUidGet**
> WebhookSubscription workspacesWorkspaceHooksUidGet(uid, workspace)

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
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String uid = "uid_example"; // String | Installed webhook's ID
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      WebhookSubscription result = apiInstance.workspacesWorkspaceHooksUidGet(uid, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspaceHooksUidGet");
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

<a id="workspacesWorkspaceHooksUidPut"></a>
# **workspacesWorkspaceHooksUidPut**
> WebhookSubscription workspacesWorkspaceHooksUidPut(uid, workspace)

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
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String uid = "uid_example"; // String | Installed webhook's ID
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      WebhookSubscription result = apiInstance.workspacesWorkspaceHooksUidPut(uid, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspaceHooksUidPut");
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

<a id="workspacesWorkspaceMembersGet"></a>
# **workspacesWorkspaceMembersGet**
> PaginatedWorkspaceMemberships workspacesWorkspaceMembersGet(workspace)

List users in a workspace

Returns all members of the requested workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedWorkspaceMemberships result = apiInstance.workspacesWorkspaceMembersGet(workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspaceMembersGet");
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

[**PaginatedWorkspaceMemberships**](PaginatedWorkspaceMemberships.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of users that are part of a workspace. |  -  |
| **401** | The request wasn&#39;t authenticated. |  -  |

<a id="workspacesWorkspaceMembersMemberGet"></a>
# **workspacesWorkspaceMembersMemberGet**
> WorkspaceMembership workspacesWorkspaceMembersMemberGet(member, workspace)

Get user membership for a workspace

Returns the workspace membership, which includes a &#x60;User&#x60; object for the member and a &#x60;Workspace&#x60; object for the requested workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String member = "member_example"; // String | Member's UUID or Atlassian ID.
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      WorkspaceMembership result = apiInstance.workspacesWorkspaceMembersMemberGet(member, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspaceMembersMemberGet");
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
| **member** | **String**| Member&#39;s UUID or Atlassian ID. | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**WorkspaceMembership**](WorkspaceMembership.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user that is part of a workspace. |  -  |
| **401** | The request wasn&#39;t authenticated. |  -  |
| **404** | A workspace cannot be found, or a user cannot be found, or the user is not a a member of the workspace. |  -  |

<a id="workspacesWorkspacePermissionsGet"></a>
# **workspacesWorkspacePermissionsGet**
> PaginatedWorkspaceMemberships workspacesWorkspacePermissionsGet(workspace, q)

List user permissions in a workspace

Returns the list of members in a workspace and their permission levels. Permission can be: * &#x60;owner&#x60; * &#x60;collaborator&#x60; * &#x60;member&#x60;  **The &#x60;collaborator&#x60; role is being removed from the Bitbucket Cloud API. For more information, see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**  Example:  &#x60;&#x60;&#x60; $ curl -X https://api.bitbucket.org/2.0/workspaces/bbworkspace1/permissions  {     \&quot;pagelen\&quot;: 10,     \&quot;values\&quot;: [         {             \&quot;permission\&quot;: \&quot;owner\&quot;,             \&quot;type\&quot;: \&quot;workspace_membership\&quot;,             \&quot;user\&quot;: {                 \&quot;type\&quot;: \&quot;user\&quot;,                 \&quot;uuid\&quot;: \&quot;{470c176d-3574-44ea-bb41-89e8638bcca4}\&quot;,                 \&quot;display_name\&quot;: \&quot;Erik van Zijst\&quot;,             },             \&quot;workspace\&quot;: {                 \&quot;type\&quot;: \&quot;workspace\&quot;,                 \&quot;uuid\&quot;: \&quot;{a15fb181-db1f-48f7-b41f-e1eff06929d6}\&quot;,                 \&quot;slug\&quot;: \&quot;bbworkspace1\&quot;,                 \&quot;name\&quot;: \&quot;Atlassian Bitbucket\&quot;,             }         },         {             \&quot;permission\&quot;: \&quot;member\&quot;,             \&quot;type\&quot;: \&quot;workspace_membership\&quot;,             \&quot;user\&quot;: {                 \&quot;type\&quot;: \&quot;user\&quot;,                 \&quot;nickname\&quot;: \&quot;seanaty\&quot;,                 \&quot;display_name\&quot;: \&quot;Sean Conaty\&quot;,                 \&quot;uuid\&quot;: \&quot;{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\&quot;             },             \&quot;workspace\&quot;: {                 \&quot;type\&quot;: \&quot;workspace\&quot;,                 \&quot;uuid\&quot;: \&quot;{a15fb181-db1f-48f7-b41f-e1eff06929d6}\&quot;,                 \&quot;slug\&quot;: \&quot;bbworkspace1\&quot;,                 \&quot;name\&quot;: \&quot;Atlassian Bitbucket\&quot;,             }         }     ],     \&quot;page\&quot;: 1,     \&quot;size\&quot;: 2 } &#x60;&#x60;&#x60;  Results may be further [filtered](/cloud/bitbucket/rest/intro/#filtering) by permission by adding the following query string parameters:  * &#x60;q&#x3D;permission&#x3D;\&quot;owner\&quot;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String q = "q_example"; // String |  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).
    try {
      PaginatedWorkspaceMemberships result = apiInstance.workspacesWorkspacePermissionsGet(workspace, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspacePermissionsGet");
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
| **q** | **String**|  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). | [optional] |

### Return type

[**PaginatedWorkspaceMemberships**](PaginatedWorkspaceMemberships.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of users that are part of a workspace, along with their permission. |  -  |
| **401** | The request wasn&#39;t authenticated. |  -  |

<a id="workspacesWorkspacePermissionsRepositoriesGet"></a>
# **workspacesWorkspacePermissionsRepositoriesGet**
> PaginatedRepositoryPermissions workspacesWorkspacePermissionsRepositoriesGet(workspace, q, sort)

List all repository permissions for a workspace

Returns an object for each repository permission for all of a workspace&#39;s repositories.  Permissions returned are effective permissions: the highest level of permission the user has. This does not distinguish between direct and indirect (group) privileges.  Only users with admin permission for the team may access this resource.  Permissions can be:  * &#x60;admin&#x60; * &#x60;write&#x60; * &#x60;read&#x60;  Example:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/workspaces/atlassian_tutorial/permissions/repositories  {   \&quot;pagelen\&quot;: 10,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;repository_permission\&quot;,       \&quot;user\&quot;: {         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;display_name\&quot;: \&quot;Erik van Zijst\&quot;,         \&quot;uuid\&quot;: \&quot;{d301aafa-d676-4ee0-88be-962be7417567}\&quot;       },       \&quot;repository\&quot;: {         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;name\&quot;: \&quot;geordi\&quot;,         \&quot;full_name\&quot;: \&quot;atlassian_tutorial/geordi\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;       },       \&quot;permission\&quot;: \&quot;admin\&quot;     },     {       \&quot;type\&quot;: \&quot;repository_permission\&quot;,       \&quot;user\&quot;: {         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;display_name\&quot;: \&quot;Sean Conaty\&quot;,         \&quot;uuid\&quot;: \&quot;{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\&quot;       },       \&quot;repository\&quot;: {         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;name\&quot;: \&quot;geordi\&quot;,         \&quot;full_name\&quot;: \&quot;atlassian_tutorial/geordi\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;       },       \&quot;permission\&quot;: \&quot;write\&quot;     },     {       \&quot;type\&quot;: \&quot;repository_permission\&quot;,       \&quot;user\&quot;: {         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;display_name\&quot;: \&quot;Jeff Zeng\&quot;,         \&quot;uuid\&quot;: \&quot;{47f92a9a-c3a3-4d0b-bc4e-782a969c5c72}\&quot;       },       \&quot;repository\&quot;: {         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;name\&quot;: \&quot;whee\&quot;,         \&quot;full_name\&quot;: \&quot;atlassian_tutorial/whee\&quot;,         \&quot;uuid\&quot;: \&quot;{30ba25e9-51ff-4555-8dd0-fc7ee2fa0895}\&quot;       },       \&quot;permission\&quot;: \&quot;admin\&quot;     }   ],   \&quot;page\&quot;: 1,   \&quot;size\&quot;: 3 } &#x60;&#x60;&#x60;  Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by repository, user, or permission by adding the following query string parameters:  * &#x60;q&#x3D;repository.name&#x3D;\&quot;geordi\&quot;&#x60; or &#x60;q&#x3D;permission&gt;\&quot;read\&quot;&#x60; * &#x60;sort&#x3D;user.display_name&#x60;  Note that the query parameter values need to be URL escaped so that &#x60;&#x3D;&#x60; would become &#x60;%3D&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String q = "q_example"; // String |  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).
    String sort = "sort_example"; // String |  Name of a response property sort the result by as per [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results). 
    try {
      PaginatedRepositoryPermissions result = apiInstance.workspacesWorkspacePermissionsRepositoriesGet(workspace, q, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspacePermissionsRepositoriesGet");
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
| **q** | **String**|  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). | [optional] |
| **sort** | **String**|  Name of a response property sort the result by as per [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results).  | [optional] |

### Return type

[**PaginatedRepositoryPermissions**](PaginatedRepositoryPermissions.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of workspace&#39;s repository permissions. |  -  |
| **403** | The requesting user isn&#39;t an admin of the workspace. |  -  |

<a id="workspacesWorkspacePermissionsRepositoriesRepoSlugGet"></a>
# **workspacesWorkspacePermissionsRepositoriesRepoSlugGet**
> PaginatedRepositoryPermissions workspacesWorkspacePermissionsRepositoriesRepoSlugGet(repoSlug, workspace, q, sort)

List a repository permissions for a workspace

Returns an object for the repository permission of each user in the requested repository.  Permissions returned are effective permissions: the highest level of permission the user has. This does not distinguish between direct and indirect (group) privileges.  Only users with admin permission for the repository may access this resource.  Permissions can be:  * &#x60;admin&#x60; * &#x60;write&#x60; * &#x60;read&#x60;  Example:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/workspaces/atlassian_tutorial/permissions/repositories/geordi  {   \&quot;pagelen\&quot;: 10,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;repository_permission\&quot;,       \&quot;user\&quot;: {         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;display_name\&quot;: \&quot;Erik van Zijst\&quot;,         \&quot;uuid\&quot;: \&quot;{d301aafa-d676-4ee0-88be-962be7417567}\&quot;       },       \&quot;repository\&quot;: {         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;name\&quot;: \&quot;geordi\&quot;,         \&quot;full_name\&quot;: \&quot;atlassian_tutorial/geordi\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;       },       \&quot;permission\&quot;: \&quot;admin\&quot;     },     {       \&quot;type\&quot;: \&quot;repository_permission\&quot;,       \&quot;user\&quot;: {         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;display_name\&quot;: \&quot;Sean Conaty\&quot;,         \&quot;uuid\&quot;: \&quot;{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\&quot;       },       \&quot;repository\&quot;: {         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;name\&quot;: \&quot;geordi\&quot;,         \&quot;full_name\&quot;: \&quot;atlassian_tutorial/geordi\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;       },       \&quot;permission\&quot;: \&quot;write\&quot;     }   ],   \&quot;page\&quot;: 1,   \&quot;size\&quot;: 2 } &#x60;&#x60;&#x60;  Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by user, or permission by adding the following query string parameters:  * &#x60;q&#x3D;permission&gt;\&quot;read\&quot;&#x60; * &#x60;sort&#x3D;user.display_name&#x60;  Note that the query parameter values need to be URL escaped so that &#x60;&#x3D;&#x60; would become &#x60;%3D&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String q = "q_example"; // String |  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).
    String sort = "sort_example"; // String |  Name of a response property sort the result by as per [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results). 
    try {
      PaginatedRepositoryPermissions result = apiInstance.workspacesWorkspacePermissionsRepositoriesRepoSlugGet(repoSlug, workspace, q, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspacePermissionsRepositoriesRepoSlugGet");
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
| **q** | **String**|  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). | [optional] |
| **sort** | **String**|  Name of a response property sort the result by as per [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results).  | [optional] |

### Return type

[**PaginatedRepositoryPermissions**](PaginatedRepositoryPermissions.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The repository permission for all users in this repository. |  -  |
| **403** | The requesting user isn&#39;t an admin of the repository. |  -  |

<a id="workspacesWorkspaceProjectsGet"></a>
# **workspacesWorkspaceProjectsGet**
> PaginatedProjects workspacesWorkspaceProjectsGet(workspace)

List projects in a workspace

Returns the list of projects in this workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedProjects result = apiInstance.workspacesWorkspaceProjectsGet(workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspaceProjectsGet");
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

[**PaginatedProjects**](PaginatedProjects.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of projects in this workspace. |  -  |
| **404** | A workspace doesn&#39;t exist at this location. |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyGet_0"></a>
# **workspacesWorkspaceProjectsProjectKeyGet_0**
> Project workspacesWorkspaceProjectsProjectKeyGet_0(projectKey, workspace)

Get a project for a workspace

Returns the requested project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

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

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Project result = apiInstance.workspacesWorkspaceProjectsProjectKeyGet_0(projectKey, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspaceProjectsProjectKeyGet_0");
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
| **projectKey** | **String**| The project in question. This is the actual &#x60;key&#x60; assigned to the project.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Project**](Project.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project that is part of a workspace. |  -  |
| **401** | The request wasn&#39;t authenticated. |  -  |
| **403** | The requesting user isn&#39;t authorized to access the project. |  -  |
| **404** | A project isn&#39;t hosted at this location. |  -  |

