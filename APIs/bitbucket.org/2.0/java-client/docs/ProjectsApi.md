# ProjectsApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspacesWorkspaceProjectsPost**](ProjectsApi.md#workspacesWorkspaceProjectsPost) | **POST** /workspaces/{workspace}/projects | Create a project in a workspace |
| [**workspacesWorkspaceProjectsProjectKeyDefaultReviewersGet**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyDefaultReviewersGet) | **GET** /workspaces/{workspace}/projects/{project_key}/default-reviewers | List the default reviewers in a project |
| [**workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserDelete**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserDelete) | **DELETE** /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user} | Remove the specific user from the project&#39;s default reviewers |
| [**workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserGet**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserGet) | **GET** /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user} | Get a default reviewer |
| [**workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserPut**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserPut) | **PUT** /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user} | Add the specific user as a default reviewer for the project |
| [**workspacesWorkspaceProjectsProjectKeyDelete**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyDelete) | **DELETE** /workspaces/{workspace}/projects/{project_key} | Delete a project for a workspace |
| [**workspacesWorkspaceProjectsProjectKeyGet**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyGet) | **GET** /workspaces/{workspace}/projects/{project_key} | Get a project for a workspace |
| [**workspacesWorkspaceProjectsProjectKeyPut**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyPut) | **PUT** /workspaces/{workspace}/projects/{project_key} | Update a project for a workspace |


<a id="workspacesWorkspaceProjectsPost"></a>
# **workspacesWorkspaceProjectsPost**
> Project workspacesWorkspaceProjectsPost(workspace, project)

Create a project in a workspace

Creates a new project.  Note that the avatar has to be embedded as either a data-url or a URL to an external image as shown in the examples below:  &#x60;&#x60;&#x60; $ body&#x3D;$(cat &lt;&lt; EOF {     \&quot;name\&quot;: \&quot;Mars Project\&quot;,     \&quot;key\&quot;: \&quot;MARS\&quot;,     \&quot;description\&quot;: \&quot;Software for colonizing mars.\&quot;,     \&quot;links\&quot;: {         \&quot;avatar\&quot;: {             \&quot;href\&quot;: \&quot;data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/...\&quot;         }     },     \&quot;is_private\&quot;: false } EOF ) $ curl -H \&quot;Content-Type: application/json\&quot; \\        -X POST \\        -d \&quot;$body\&quot; \\        https://api.bitbucket.org/2.0/teams/teams-in-space/projects/ | jq . {   // Serialized project document } &#x60;&#x60;&#x60;  or even:  &#x60;&#x60;&#x60; $ body&#x3D;$(cat &lt;&lt; EOF {     \&quot;name\&quot;: \&quot;Mars Project\&quot;,     \&quot;key\&quot;: \&quot;MARS\&quot;,     \&quot;description\&quot;: \&quot;Software for colonizing mars.\&quot;,     \&quot;links\&quot;: {         \&quot;avatar\&quot;: {             \&quot;href\&quot;: \&quot;http://i.imgur.com/72tRx4w.gif\&quot;         }     },     \&quot;is_private\&quot;: false } EOF ) $ curl -H \&quot;Content-Type: application/json\&quot; \\        -X POST \\        -d \&quot;$body\&quot; \\        https://api.bitbucket.org/2.0/teams/teams-in-space/projects/ | jq . {   // Serialized project document } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    Project project = new Project(); // Project | 
    try {
      Project result = apiInstance.workspacesWorkspaceProjectsPost(workspace, project);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#workspacesWorkspaceProjectsPost");
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
| **project** | [**Project**](Project.md)|  | |

### Return type

[**Project**](Project.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A new project has been created. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **403** | The requesting user isn&#39;t authorized to create the project. |  -  |
| **404** | A workspace doesn&#39;t exist at this location. |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyDefaultReviewersGet"></a>
# **workspacesWorkspaceProjectsProjectKeyDefaultReviewersGet**
> PaginatedDefaultReviewerAndType workspacesWorkspaceProjectsProjectKeyDefaultReviewersGet(projectKey, workspace)

List the default reviewers in a project

Return a list of all default reviewers for a project. This is a list of users that will be added as default reviewers to pull requests for any repository within the project.  Example: &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/.../projects/.../default-reviewers | jq . {     \&quot;pagelen\&quot;: 10,     \&quot;values\&quot;: [         {             \&quot;user\&quot;: {                 \&quot;display_name\&quot;: \&quot;Davis Lee\&quot;,                 \&quot;uuid\&quot;: \&quot;{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\&quot;             },             \&quot;reviewer_type\&quot;: \&quot;project\&quot;,             \&quot;type\&quot;: \&quot;default_reviewer\&quot;         },         {             \&quot;user\&quot;: {                 \&quot;display_name\&quot;: \&quot;Jorge Rodriguez\&quot;,                 \&quot;uuid\&quot;: \&quot;{1aa43376-260d-4a0b-9660-f62672b9655d}\&quot;             },             \&quot;reviewer_type\&quot;: \&quot;project\&quot;,             \&quot;type\&quot;: \&quot;default_reviewer\&quot;         }     ],     \&quot;page\&quot;: 1,     \&quot;size\&quot;: 2 } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedDefaultReviewerAndType result = apiInstance.workspacesWorkspaceProjectsProjectKeyDefaultReviewersGet(projectKey, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#workspacesWorkspaceProjectsProjectKeyDefaultReviewersGet");
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

[**PaginatedDefaultReviewerAndType**](PaginatedDefaultReviewerAndType.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of project default reviewers |  -  |
| **403** | If the authenticated user does not have admin access to the project |  -  |
| **404** | If the workspace or project does not exist at this location |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserDelete"></a>
# **workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserDelete**
> workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserDelete(projectKey, selectedUser, workspace)

Remove the specific user from the project&#39;s default reviewers

Removes a default reviewer from the project.  Example: &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/.../default-reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D  HTTP/1.1 204 &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectKey = "projectKey_example"; // String | The project in question. This can either be the actual `key` assigned to the project or the `UUID` (surrounded by curly-braces (`{}`)). 
    String selectedUser = "selectedUser_example"; // String | This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: `{account UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserDelete(projectKey, selectedUser, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserDelete");
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
| **projectKey** | **String**| The project in question. This can either be the actual &#x60;key&#x60; assigned to the project or the &#x60;UUID&#x60; (surrounded by curly-braces (&#x60;{}&#x60;)).  | |
| **selectedUser** | **String**| This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;.  | |
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
| **204** | The specified user was removed from the list of project default reviewers |  -  |
| **400** | If the specified user is not a default reviewer for the project |  -  |
| **403** | If the authenticated user does not have admin access to the project |  -  |
| **404** | If the specified user, project, or workspace does not exist |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserGet"></a>
# **workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserGet**
> User workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserGet(projectKey, selectedUser, workspace)

Get a default reviewer

Returns the specified default reviewer.  Example: &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/.../default-reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D {     \&quot;display_name\&quot;: \&quot;Davis Lee\&quot;,     \&quot;type\&quot;: \&quot;user\&quot;,     \&quot;uuid\&quot;: \&quot;{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\&quot; } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectKey = "projectKey_example"; // String | The project in question. This can either be the actual `key` assigned to the project or the `UUID` (surrounded by curly-braces (`{}`)). 
    String selectedUser = "selectedUser_example"; // String | This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: `{account UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      User result = apiInstance.workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserGet(projectKey, selectedUser, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserGet");
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
| **projectKey** | **String**| The project in question. This can either be the actual &#x60;key&#x60; assigned to the project or the &#x60;UUID&#x60; (surrounded by curly-braces (&#x60;{}&#x60;)).  | |
| **selectedUser** | **String**| This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified user that is a default reviewer |  -  |
| **400** | If the specified user is not a default reviewer for the project |  -  |
| **403** | If the authenticated user does not have admin access to the project |  -  |
| **404** | If the specified user, project, or workspace does not exist |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserPut"></a>
# **workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserPut**
> User workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserPut(projectKey, selectedUser, workspace)

Add the specific user as a default reviewer for the project

Adds the specified user to the project&#39;s list of default reviewers. The method is idempotent. Accepts an optional body containing the &#x60;uuid&#x60; of the user to be added.  Example: &#x60;&#x60;&#x60; $ curl -XPUT https://api.bitbucket.org/2.0/.../default-reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D -d { &#39;uuid&#39;: &#39;{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}&#39; }  HTTP/1.1 204 &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectKey = "projectKey_example"; // String | The project in question. This can either be the actual `key` assigned to the project or the `UUID` (surrounded by curly-braces (`{}`)). 
    String selectedUser = "selectedUser_example"; // String | This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: `{account UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      User result = apiInstance.workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserPut(projectKey, selectedUser, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserPut");
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
| **projectKey** | **String**| The project in question. This can either be the actual &#x60;key&#x60; assigned to the project or the &#x60;UUID&#x60; (surrounded by curly-braces (&#x60;{}&#x60;)).  | |
| **selectedUser** | **String**| This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The specified user was added as a project default reviewer |  -  |
| **400** | If the specified user cannot be added as a default reviewer for the project |  -  |
| **403** | If the authenticated user does not have admin access to the project |  -  |
| **404** | If the specified user, project, or workspace does not exist |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyDelete"></a>
# **workspacesWorkspaceProjectsProjectKeyDelete**
> workspacesWorkspaceProjectsProjectKeyDelete(projectKey, workspace)

Delete a project for a workspace

Deletes this project. This is an irreversible operation.  You cannot delete a project that still contains repositories. To delete the project, [delete](/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-delete) or transfer the repositories first.  Example: &#x60;&#x60;&#x60; $ curl -X DELETE https://api.bitbucket.org/2.0/bbworkspace1/PROJ &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.workspacesWorkspaceProjectsProjectKeyDelete(projectKey, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#workspacesWorkspaceProjectsProjectKeyDelete");
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

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful deletion. |  -  |
| **403** | The requesting user isn&#39;t authorized to delete the project or the project isn&#39;t empty. |  -  |
| **404** | A project isn&#39;t hosted at this location. |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyGet"></a>
# **workspacesWorkspaceProjectsProjectKeyGet**
> Project workspacesWorkspaceProjectsProjectKeyGet(projectKey, workspace)

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
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Project result = apiInstance.workspacesWorkspaceProjectsProjectKeyGet(projectKey, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#workspacesWorkspaceProjectsProjectKeyGet");
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

<a id="workspacesWorkspaceProjectsProjectKeyPut"></a>
# **workspacesWorkspaceProjectsProjectKeyPut**
> Project workspacesWorkspaceProjectsProjectKeyPut(projectKey, workspace, project)

Update a project for a workspace

Since this endpoint can be used to both update and to create a project, the request body depends on the intent.  #### Creation  See the POST documentation for the project collection for an example of the request body.  Note: The &#x60;key&#x60; should not be specified in the body of request (since it is already present in the URL). The &#x60;name&#x60; is required, everything else is optional.  #### Update  See the POST documentation for the project collection for an example of the request body.  Note: The key is not required in the body (since it is already in the URL). The key may be specified in the body, if the intent is to change the key itself. In such a scenario, the location of the project is changed and is returned in the &#x60;Location&#x60; header of the response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    Project project = new Project(); // Project | 
    try {
      Project result = apiInstance.workspacesWorkspaceProjectsProjectKeyPut(projectKey, workspace, project);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#workspacesWorkspaceProjectsProjectKeyPut");
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
| **project** | [**Project**](Project.md)|  | |

### Return type

[**Project**](Project.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The existing project is has been updated. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **201** | A new project has been created. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **403** | The requesting user isn&#39;t authorized to update or create the project. |  -  |
| **404** | A workspace doesn&#39;t exist at the location. Note that the project&#39;s absence from this location doesn&#39;t raise a 404, since a PUT at a non-existent location can be used to create a new project. |  -  |

