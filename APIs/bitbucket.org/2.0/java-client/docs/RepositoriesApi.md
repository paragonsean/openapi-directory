# RepositoriesApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**repositoriesGet**](RepositoriesApi.md#repositoriesGet) | **GET** /repositories | List public repositories |
| [**repositoriesWorkspaceGet**](RepositoriesApi.md#repositoriesWorkspaceGet) | **GET** /repositories/{workspace} | List repositories in a workspace |
| [**repositoriesWorkspaceRepoSlugDelete**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugDelete) | **DELETE** /repositories/{workspace}/{repo_slug} | Delete a repository |
| [**repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet_0**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet_0) | **GET** /repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path} | List commits that modified a file |
| [**repositoriesWorkspaceRepoSlugForksGet**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugForksGet) | **GET** /repositories/{workspace}/{repo_slug}/forks | List repository forks |
| [**repositoriesWorkspaceRepoSlugForksPost**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugForksPost) | **POST** /repositories/{workspace}/{repo_slug}/forks | Fork a repository |
| [**repositoriesWorkspaceRepoSlugGet**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugGet) | **GET** /repositories/{workspace}/{repo_slug} | Get a repository |
| [**repositoriesWorkspaceRepoSlugHooksGet**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugHooksGet) | **GET** /repositories/{workspace}/{repo_slug}/hooks | List webhooks for a repository |
| [**repositoriesWorkspaceRepoSlugHooksPost**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugHooksPost) | **POST** /repositories/{workspace}/{repo_slug}/hooks | Create a webhook for a repository |
| [**repositoriesWorkspaceRepoSlugHooksUidDelete**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugHooksUidDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/hooks/{uid} | Delete a webhook for a repository |
| [**repositoriesWorkspaceRepoSlugHooksUidGet**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugHooksUidGet) | **GET** /repositories/{workspace}/{repo_slug}/hooks/{uid} | Get a webhook for a repository |
| [**repositoriesWorkspaceRepoSlugHooksUidPut**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugHooksUidPut) | **PUT** /repositories/{workspace}/{repo_slug}/hooks/{uid} | Update a webhook for a repository |
| [**repositoriesWorkspaceRepoSlugOverrideSettingsGet**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugOverrideSettingsGet) | **GET** /repositories/{workspace}/{repo_slug}/override-settings | Retrieve the inheritance state for repository settings |
| [**repositoriesWorkspaceRepoSlugOverrideSettingsPut**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugOverrideSettingsPut) | **PUT** /repositories/{workspace}/{repo_slug}/override-settings | Set the inheritance state for repository settings                  |
| [**repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGet**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGet) | **GET** /repositories/{workspace}/{repo_slug}/permissions-config/groups | List explicit group permissions for a repository |
| [**repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugDelete**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug} | Delete an explicit group permission for a repository |
| [**repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugGet**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugGet) | **GET** /repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug} | Get an explicit group permission for a repository |
| [**repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugPut**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugPut) | **PUT** /repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug} | Update an explicit group permission for a repository |
| [**repositoriesWorkspaceRepoSlugPermissionsConfigUsersGet**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugPermissionsConfigUsersGet) | **GET** /repositories/{workspace}/{repo_slug}/permissions-config/users | List explicit user permissions for a repository |
| [**repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdDelete**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id} | Delete an explicit user permission for a repository |
| [**repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdGet**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdGet) | **GET** /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id} | Get an explicit user permission for a repository |
| [**repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdPut**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdPut) | **PUT** /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id} | Update an explicit user permission for a repository |
| [**repositoriesWorkspaceRepoSlugPost**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugPost) | **POST** /repositories/{workspace}/{repo_slug} | Create a repository |
| [**repositoriesWorkspaceRepoSlugPut**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugPut) | **PUT** /repositories/{workspace}/{repo_slug} | Update a repository |
| [**repositoriesWorkspaceRepoSlugSrcCommitPathGet_0**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugSrcCommitPathGet_0) | **GET** /repositories/{workspace}/{repo_slug}/src/{commit}/{path} | Get file or directory contents |
| [**repositoriesWorkspaceRepoSlugSrcGet_0**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugSrcGet_0) | **GET** /repositories/{workspace}/{repo_slug}/src | Get the root directory of the main branch |
| [**repositoriesWorkspaceRepoSlugSrcPost_0**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugSrcPost_0) | **POST** /repositories/{workspace}/{repo_slug}/src | Create a commit by uploading a file |
| [**repositoriesWorkspaceRepoSlugWatchersGet**](RepositoriesApi.md#repositoriesWorkspaceRepoSlugWatchersGet) | **GET** /repositories/{workspace}/{repo_slug}/watchers | List repositories watchers |
| [**userPermissionsRepositoriesGet**](RepositoriesApi.md#userPermissionsRepositoriesGet) | **GET** /user/permissions/repositories | List repository permissions for a user |


<a id="repositoriesGet"></a>
# **repositoriesGet**
> PaginatedRepositories repositoriesGet(after, role, q, sort)

List public repositories

Returns a paginated list of all public repositories.  This endpoint also supports filtering and sorting of the results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String after = "after_example"; // String | Filter the results to include only repositories created on or after this [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  timestamp. Example: `YYYY-MM-DDTHH:mm:ss.sssZ`
    String role = "admin"; // String | Filters the result based on the authenticated user's role on each repository.  * **member**: returns repositories to which the user has explicit read access * **contributor**: returns repositories to which the user has explicit write access * **admin**: returns repositories to which the user has explicit administrator access * **owner**: returns all repositories owned by the current user 
    String q = "q_example"; // String | Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). `role` parameter must also be specified. 
    String sort = "sort_example"; // String | Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). 
    try {
      PaginatedRepositories result = apiInstance.repositoriesGet(after, role, q, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesGet");
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
| **after** | **String**| Filter the results to include only repositories created on or after this [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  timestamp. Example: &#x60;YYYY-MM-DDTHH:mm:ss.sssZ&#x60; | [optional] |
| **role** | **String**| Filters the result based on the authenticated user&#39;s role on each repository.  * **member**: returns repositories to which the user has explicit read access * **contributor**: returns repositories to which the user has explicit write access * **admin**: returns repositories to which the user has explicit administrator access * **owner**: returns all repositories owned by the current user  | [optional] [enum: admin, contributor, member, owner] |
| **q** | **String**| Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). &#x60;role&#x60; parameter must also be specified.  | [optional] |
| **sort** | **String**| Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).  | [optional] |

### Return type

[**PaginatedRepositories**](PaginatedRepositories.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All public repositories. |  -  |

<a id="repositoriesWorkspaceGet"></a>
# **repositoriesWorkspaceGet**
> PaginatedRepositories repositoriesWorkspaceGet(workspace, role, q, sort)

List repositories in a workspace

Returns a paginated list of all repositories owned by the specified workspace.  The result can be narrowed down based on the authenticated user&#39;s role.  E.g. with &#x60;?role&#x3D;contributor&#x60;, only those repositories that the authenticated user has write access to are returned (this includes any repo the user is an admin on, as that implies write access).  This endpoint also supports filtering and sorting of the results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String role = "admin"; // String |  Filters the result based on the authenticated user's role on each repository.  * **member**: returns repositories to which the user has explicit read access * **contributor**: returns repositories to which the user has explicit write access * **admin**: returns repositories to which the user has explicit administrator access * **owner**: returns all repositories owned by the current user 
    String q = "q_example"; // String |  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). 
    String sort = "sort_example"; // String |  Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).         
    try {
      PaginatedRepositories result = apiInstance.repositoriesWorkspaceGet(workspace, role, q, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceGet");
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
| **role** | **String**|  Filters the result based on the authenticated user&#39;s role on each repository.  * **member**: returns repositories to which the user has explicit read access * **contributor**: returns repositories to which the user has explicit write access * **admin**: returns repositories to which the user has explicit administrator access * **owner**: returns all repositories owned by the current user  | [optional] [enum: admin, contributor, member, owner] |
| **q** | **String**|  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).  | [optional] |
| **sort** | **String**|  Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).          | [optional] |

### Return type

[**PaginatedRepositories**](PaginatedRepositories.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The repositories owned by the specified account. |  -  |
| **404** | If the specified account does not exist. |  -  |
| **410** | If the specified account marked as spam. |  -  |

<a id="repositoriesWorkspaceRepoSlugDelete"></a>
# **repositoriesWorkspaceRepoSlugDelete**
> repositoriesWorkspaceRepoSlugDelete(repoSlug, workspace, redirectTo)

Delete a repository

Deletes the repository. This is an irreversible operation.  This does not affect its forks.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String redirectTo = "redirectTo_example"; // String | If a repository has been moved to a new location, use this parameter to show users a friendly message in the Bitbucket UI that the repository has moved to a new location. However, a GET to this endpoint will still return a 404. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugDelete(repoSlug, workspace, redirectTo);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugDelete");
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
| **redirectTo** | **String**| If a repository has been moved to a new location, use this parameter to show users a friendly message in the Bitbucket UI that the repository has moved to a new location. However, a GET to this endpoint will still return a 404.  | [optional] |

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
| **204** | Indicates successful deletion. |  -  |
| **403** | If the caller either does not have admin access to the repository, or the repository is set to read-only. |  -  |
| **404** | If the repository does not exist. |  -  |

<a id="repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet_0"></a>
# **repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet_0**
> PaginatedFiles repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet_0(commit, path, repoSlug, workspace, renames, q, sort)

List commits that modified a file

Returns a paginated list of commits that modified the specified file.  Commits are returned in reverse chronological order. This is roughly equivalent to the following commands:      $ git log --follow --date-order &lt;sha&gt; &lt;path&gt;  By default, Bitbucket will follow renames and the path name in the returned entries reflects that. This can be turned off using the &#x60;?renames&#x3D;false&#x60; query parameter.  Results are returned in descending chronological order by default, and like most endpoints you can [filter and sort](/cloud/bitbucket/rest/intro/#filtering) the response to only provide exactly the data you want.  For example, if you wanted to find commits made before 2011-05-18 against a file named &#x60;README.rst&#x60;, but you only wanted the path and date, your query would look like this:  &#x60;&#x60;&#x60; $ curl &#39;https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/filehistory/master/README.rst&#39;\\   &#39;?fields&#x3D;values.next,values.path,values.commit.date&amp;q&#x3D;commit.date&lt;&#x3D;2011-05-18&#39; {   \&quot;values\&quot;: [     {       \&quot;commit\&quot;: {         \&quot;date\&quot;: \&quot;2011-05-17T07:32:09+00:00\&quot;       },       \&quot;path\&quot;: \&quot;README.rst\&quot;     },     {       \&quot;commit\&quot;: {         \&quot;date\&quot;: \&quot;2011-05-16T06:33:28+00:00\&quot;       },       \&quot;path\&quot;: \&quot;README.txt\&quot;     },     {       \&quot;commit\&quot;: {         \&quot;date\&quot;: \&quot;2011-05-16T06:15:39+00:00\&quot;       },       \&quot;path\&quot;: \&quot;README.txt\&quot;     }   ] } &#x60;&#x60;&#x60;  In the response you can see that the file was renamed to &#x60;README.rst&#x60; by the commit made on 2011-05-16, and was previously named &#x60;README.txt&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String commit = "commit_example"; // String | The commit's SHA1.
    String path = "path_example"; // String | Path to the file.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String renames = "renames_example"; // String |  When `true`, Bitbucket will follow the history of the file across renames (this is the default behavior). This can be turned off by specifying `false`.
    String q = "q_example"; // String |  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).
    String sort = "sort_example"; // String |  Name of a response property sort the result by as per [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results). 
    try {
      PaginatedFiles result = apiInstance.repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet_0(commit, path, repoSlug, workspace, renames, q, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugFilehistoryCommitPathGet_0");
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
| **commit** | **String**| The commit&#39;s SHA1. | |
| **path** | **String**| Path to the file. | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **renames** | **String**|  When &#x60;true&#x60;, Bitbucket will follow the history of the file across renames (this is the default behavior). This can be turned off by specifying &#x60;false&#x60;. | [optional] |
| **q** | **String**|  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). | [optional] |
| **sort** | **String**|  Name of a response property sort the result by as per [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results).  | [optional] |

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of commits that modified the specified file |  -  |
| **404** | If the repository does not exist. |  -  |

<a id="repositoriesWorkspaceRepoSlugForksGet"></a>
# **repositoriesWorkspaceRepoSlugForksGet**
> PaginatedRepositories repositoriesWorkspaceRepoSlugForksGet(repoSlug, workspace, role, q, sort)

List repository forks

Returns a paginated list of all the forks of the specified repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String role = "admin"; // String | Filters the result based on the authenticated user's role on each repository.  * **member**: returns repositories to which the user has explicit read access * **contributor**: returns repositories to which the user has explicit write access * **admin**: returns repositories to which the user has explicit administrator access * **owner**: returns all repositories owned by the current user 
    String q = "q_example"; // String | Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). 
    String sort = "sort_example"; // String | Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). 
    try {
      PaginatedRepositories result = apiInstance.repositoriesWorkspaceRepoSlugForksGet(repoSlug, workspace, role, q, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugForksGet");
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
| **role** | **String**| Filters the result based on the authenticated user&#39;s role on each repository.  * **member**: returns repositories to which the user has explicit read access * **contributor**: returns repositories to which the user has explicit write access * **admin**: returns repositories to which the user has explicit administrator access * **owner**: returns all repositories owned by the current user  | [optional] [enum: admin, contributor, member, owner] |
| **q** | **String**| Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).  | [optional] |
| **sort** | **String**| Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).  | [optional] |

### Return type

[**PaginatedRepositories**](PaginatedRepositories.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All forks. |  -  |

<a id="repositoriesWorkspaceRepoSlugForksPost"></a>
# **repositoriesWorkspaceRepoSlugForksPost**
> Repository repositoriesWorkspaceRepoSlugForksPost(repoSlug, workspace, repository)

Fork a repository

Creates a new fork of the specified repository.  #### Forking a repository  To create a fork, specify the workspace explicitly as part of the request body:  &#x60;&#x60;&#x60; $ curl -X POST -u jdoe https://api.bitbucket.org/2.0/repositories/atlassian/bbql/forks \\   -H &#39;Content-Type: application/json&#39; -d &#39;{     \&quot;name\&quot;: \&quot;bbql_fork\&quot;,     \&quot;workspace\&quot;: {       \&quot;slug\&quot;: \&quot;atlassian\&quot;     } }&#39; &#x60;&#x60;&#x60;  To fork a repository into the same workspace, also specify a new &#x60;name&#x60;.  When you specify a value for &#x60;name&#x60;, it will also affect the &#x60;slug&#x60;. The &#x60;slug&#x60; is reflected in the repository URL of the new fork. It is derived from &#x60;name&#x60; by substituting non-ASCII characters, removes whitespace, and changes characters to lower case. For example, &#x60;My repo&#x60; would turn into &#x60;my_repo&#x60;.  You need contributor access to create new forks within a workspace.   #### Change the properties of a new fork  By default the fork inherits most of its properties from the parent. However, since the optional POST body document follows the normal &#x60;repository&#x60; JSON schema and you can override the new fork&#39;s properties.  Properties that can be overridden include:  * description * fork_policy * language * mainbranch * is_private (note that a private repo&#39;s fork_policy might prohibit   the creation of public forks, in which &#x60;is_private&#x3D;False&#x60; would fail) * has_issues (to initialize or disable the new repo&#39;s issue tracker --   note that the actual contents of the parent repository&#39;s issue   tracker are not copied during forking) * has_wiki (to initialize or disable the new repo&#39;s wiki --   note that the actual contents of the parent repository&#39;s wiki are not   copied during forking) * project (when forking into a private project, the fork&#39;s &#x60;is_private&#x60;   must be &#x60;true&#x60;)  Properties that cannot be modified include:  * scm * parent * full_name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    Repository repository = new Repository(); // Repository | A repository object. This can be left blank.
    try {
      Repository result = apiInstance.repositoriesWorkspaceRepoSlugForksPost(repoSlug, workspace, repository);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugForksPost");
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
| **repository** | [**Repository**](Repository.md)| A repository object. This can be left blank. | [optional] |

### Return type

[**Repository**](Repository.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The newly created fork. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |

<a id="repositoriesWorkspaceRepoSlugGet"></a>
# **repositoriesWorkspaceRepoSlugGet**
> Repository repositoriesWorkspaceRepoSlugGet(repoSlug, workspace)

Get a repository

Returns the object describing this repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Repository result = apiInstance.repositoriesWorkspaceRepoSlugGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugGet");
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

[**Repository**](Repository.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The repository object. |  -  |
| **403** | If the repository is private and the authenticated user does not have access to it. |  -  |
| **404** | If no repository exists at this location. |  -  |

<a id="repositoriesWorkspaceRepoSlugHooksGet"></a>
# **repositoriesWorkspaceRepoSlugHooksGet**
> PaginatedWebhookSubscriptions repositoriesWorkspaceRepoSlugHooksGet(repoSlug, workspace)

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
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedWebhookSubscriptions result = apiInstance.repositoriesWorkspaceRepoSlugHooksGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugHooksGet");
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

<a id="repositoriesWorkspaceRepoSlugHooksPost"></a>
# **repositoriesWorkspaceRepoSlugHooksPost**
> WebhookSubscription repositoriesWorkspaceRepoSlugHooksPost(repoSlug, workspace)

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
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      WebhookSubscription result = apiInstance.repositoriesWorkspaceRepoSlugHooksPost(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugHooksPost");
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

<a id="repositoriesWorkspaceRepoSlugHooksUidDelete"></a>
# **repositoriesWorkspaceRepoSlugHooksUidDelete**
> repositoriesWorkspaceRepoSlugHooksUidDelete(repoSlug, uid, workspace)

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
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String uid = "uid_example"; // String | Installed webhook's ID
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugHooksUidDelete(repoSlug, uid, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugHooksUidDelete");
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

<a id="repositoriesWorkspaceRepoSlugHooksUidGet"></a>
# **repositoriesWorkspaceRepoSlugHooksUidGet**
> WebhookSubscription repositoriesWorkspaceRepoSlugHooksUidGet(repoSlug, uid, workspace)

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
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String uid = "uid_example"; // String | Installed webhook's ID
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      WebhookSubscription result = apiInstance.repositoriesWorkspaceRepoSlugHooksUidGet(repoSlug, uid, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugHooksUidGet");
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

<a id="repositoriesWorkspaceRepoSlugHooksUidPut"></a>
# **repositoriesWorkspaceRepoSlugHooksUidPut**
> WebhookSubscription repositoriesWorkspaceRepoSlugHooksUidPut(repoSlug, uid, workspace)

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
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String uid = "uid_example"; // String | Installed webhook's ID
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      WebhookSubscription result = apiInstance.repositoriesWorkspaceRepoSlugHooksUidPut(repoSlug, uid, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugHooksUidPut");
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

<a id="repositoriesWorkspaceRepoSlugOverrideSettingsGet"></a>
# **repositoriesWorkspaceRepoSlugOverrideSettingsGet**
> RepositoryInheritanceState repositoriesWorkspaceRepoSlugOverrideSettingsGet(repoSlug, workspace)

Retrieve the inheritance state for repository settings



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      RepositoryInheritanceState result = apiInstance.repositoriesWorkspaceRepoSlugOverrideSettingsGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugOverrideSettingsGet");
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

[**RepositoryInheritanceState**](RepositoryInheritanceState.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The repository setting inheritance state |  -  |
| **404** | If no repository exists at this location |  -  |

<a id="repositoriesWorkspaceRepoSlugOverrideSettingsPut"></a>
# **repositoriesWorkspaceRepoSlugOverrideSettingsPut**
> repositoriesWorkspaceRepoSlugOverrideSettingsPut(repoSlug, workspace)

Set the inheritance state for repository settings                 



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugOverrideSettingsPut(repoSlug, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugOverrideSettingsPut");
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

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The repository setting inheritance state was set and no content returned |  -  |
| **404** | If no repository exists at this location |  -  |

<a id="repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGet"></a>
# **repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGet**
> PaginatedRepositoryGroupPermissions repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGet(repoSlug, workspace)

List explicit group permissions for a repository

Returns a paginated list of explicit group permissions for the given repository. This endpoint does not support BBQL features.  Example:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/groups  HTTP/1.1 200 Location: https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/groups  {   \&quot;pagelen\&quot;: 10,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;repository_group_permission\&quot;,       \&quot;group\&quot;: {         \&quot;type\&quot;: \&quot;group\&quot;,         \&quot;name\&quot;: \&quot;Administrators\&quot;,         \&quot;slug\&quot;: \&quot;administrators\&quot;       },       \&quot;permission\&quot;: \&quot;admin\&quot;,       \&quot;links\&quot;: {         \&quot;self\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/                    geordi/permissions-config/groups/administrators\&quot;         }       }     },     {       \&quot;type\&quot;: \&quot;repository_group_permission\&quot;,       \&quot;group\&quot;: {         \&quot;type\&quot;: \&quot;group\&quot;,         \&quot;name\&quot;: \&quot;Developers\&quot;,         \&quot;slug\&quot;: \&quot;developers\&quot;       },       \&quot;permission\&quot;: \&quot;read\&quot;,       \&quot;links\&quot;: {         \&quot;self\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/                    geordi/permissions-config/groups/developers\&quot;         }       }     }   ],   \&quot;page\&quot;: 1,   \&quot;size\&quot;: 2 } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedRepositoryGroupPermissions result = apiInstance.repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGet");
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

[**PaginatedRepositoryGroupPermissions**](PaginatedRepositoryGroupPermissions.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated of explicit group permissions on the repository. |  -  |
| **401** | The user couldn&#39;t be authenticated. |  -  |
| **403** | The requesting user isn&#39;t an admin of the repository. |  -  |
| **404** | One or both of the workspace and repository doesn&#39;t exist for the given identifiers. |  -  |

<a id="repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugDelete"></a>
# **repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugDelete**
> repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugDelete(groupSlug, repoSlug, workspace)

Delete an explicit group permission for a repository

Deletes the repository group permission between the requested repository and group, if one exists.  Only users with admin permission for the repository may access this resource.  Example:  $ curl -X DELETE https://api.bitbucket.org/2.0/repositories/atlassian_tutorial /geordi/permissions-config/groups/developers   HTTP/1.1 204

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String groupSlug = "groupSlug_example"; // String | Slug of the requested group.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugDelete(groupSlug, repoSlug, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugDelete");
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
| **groupSlug** | **String**| Slug of the requested group. | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
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
| **204** | Group permission deleted |  -  |
| **401** | The user couldn&#39;t be authenticated. |  -  |
| **403** | The requesting user isn&#39;t an admin of the repository, or the authentication method was not via app password. |  -  |
| **404** | The workspace does not exist, the repository does not exist, or the group does not exist. |  -  |

<a id="repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugGet"></a>
# **repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugGet**
> RepositoryGroupPermission repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugGet(groupSlug, repoSlug, workspace)

Get an explicit group permission for a repository

Returns the group permission for a given group slug and repository  Only users with admin permission for the repository may access this resource.  Permissions can be:  * &#x60;admin&#x60; * &#x60;write&#x60; * &#x60;read&#x60; * &#x60;none&#x60;  Example:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/groups/developers  HTTP/1.1 200 Location: https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/groups/developers  {     \&quot;type\&quot;: \&quot;repository_group_permission\&quot;,     \&quot;group\&quot;: {         \&quot;type\&quot;: \&quot;group\&quot;,         \&quot;name\&quot;: \&quot;Developers\&quot;,         \&quot;slug\&quot;: \&quot;developers\&quot;     },     \&quot;repository\&quot;: {         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;name\&quot;: \&quot;geordi\&quot;,         \&quot;full_name\&quot;: \&quot;atlassian_tutorial/geordi\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;     },     \&quot;permission\&quot;: \&quot;read\&quot;,     \&quot;links\&quot;: {       \&quot;self\&quot;: {         \&quot;href\&quot;:         \&quot;https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/groups/developers\&quot;       }     } } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String groupSlug = "groupSlug_example"; // String | Slug of the requested group.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      RepositoryGroupPermission result = apiInstance.repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugGet(groupSlug, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugGet");
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
| **groupSlug** | **String**| Slug of the requested group. | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**RepositoryGroupPermission**](RepositoryGroupPermission.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group permission for group slug and repository |  -  |
| **401** | The user couldn&#39;t be authenticated. |  -  |
| **403** | The requesting user isn&#39;t an admin of the repository. |  -  |
| **404** | The given user, workspace, and/or repository could not be found |  -  |

<a id="repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugPut"></a>
# **repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugPut**
> RepositoryGroupPermission repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugPut(groupSlug, repoSlug, workspace)

Update an explicit group permission for a repository

Updates the group permission if it exists.  Only users with admin permission for the repository may access this resource.  The only authentication method supported for this endpoint is via app passwords.  Permissions can be:  * &#x60;admin&#x60; * &#x60;write&#x60; * &#x60;read&#x60;  Example: &#x60;&#x60;&#x60; $ curl -X PUT -H \&quot;Content-Type: application/json\&quot; https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/groups/developers -d &#39;{     \&quot;permission\&quot;: \&quot;write\&quot; }&#39;  HTTP/1.1 200 Location: https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/groups/developers  {     \&quot;type\&quot;: \&quot;repository_group_permission\&quot;,     \&quot;group\&quot;: {         \&quot;type\&quot;: \&quot;group\&quot;,         \&quot;name\&quot;: \&quot;Developers\&quot;,         \&quot;slug\&quot;: \&quot;developers\&quot;     },     \&quot;repository\&quot;: {         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;name\&quot;: \&quot;geordi\&quot;,         \&quot;full_name\&quot;: \&quot;atlassian_tutorial/geordi\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;     },     \&quot;permission\&quot;: \&quot;write\&quot;,     \&quot;links\&quot;: {       \&quot;self\&quot;: {         \&quot;href\&quot;:         \&quot;https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/groups/developers\&quot;       }     } } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String groupSlug = "groupSlug_example"; // String | Slug of the requested group.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      RepositoryGroupPermission result = apiInstance.repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugPut(groupSlug, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugPermissionsConfigGroupsGroupSlugPut");
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
| **groupSlug** | **String**| Slug of the requested group. | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**RepositoryGroupPermission**](RepositoryGroupPermission.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group permission updated |  -  |
| **400** | No permission value was provided or the value is invalid(not one of read, write, or admin) |  -  |
| **401** | The user couldn&#39;t be authenticated. |  -  |
| **402** | You have reached your plan&#39;s user limit and must upgrade before giving access to additional users. |  -  |
| **403** | The requesting user isn&#39;t an admin of the repository, or the authentication method was not via app password. |  -  |
| **404** | The workspace does not exist, the repository does not exist, or the group does not exist. |  -  |

<a id="repositoriesWorkspaceRepoSlugPermissionsConfigUsersGet"></a>
# **repositoriesWorkspaceRepoSlugPermissionsConfigUsersGet**
> PaginatedRepositoryUserPermissions repositoriesWorkspaceRepoSlugPermissionsConfigUsersGet(repoSlug, workspace)

List explicit user permissions for a repository

Returns a paginated list of explicit user permissions for the given repository. This endpoint does not support BBQL features.  Example:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/users  {   \&quot;pagelen\&quot;: 10,   \&quot;values\&quot;: [     {         \&quot;type\&quot;: \&quot;repository_user_permission\&quot;,         \&quot;user\&quot;: {             \&quot;type\&quot;: \&quot;user\&quot;,             \&quot;display_name\&quot;: \&quot;Colin Cameron\&quot;,             \&quot;uuid\&quot;: \&quot;{d301aafa-d676-4ee0-88be-962be7417567}\&quot;,             \&quot;account_id\&quot;: \&quot;557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\&quot;         },         \&quot;permission\&quot;: \&quot;admin\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/                      permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\&quot;           }         }     },     {       \&quot;type\&quot;: \&quot;repository_user_permission\&quot;,       \&quot;user\&quot;: {         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;display_name\&quot;: \&quot;Sean Conaty\&quot;,         \&quot;uuid\&quot;: \&quot;{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\&quot;,         \&quot;account_id\&quot;: \&quot;557058:ba8948b2-49da-43a9-9e8b-e7249b8e324c\&quot;       },       \&quot;permission\&quot;: \&quot;write\&quot;,       \&quot;links\&quot;: {         \&quot;self\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0//repositories/atlassian_tutorial/geordi/                    permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324c\&quot;         }       }     }   ],   \&quot;page\&quot;: 1,   \&quot;size\&quot;: 2 } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedRepositoryUserPermissions result = apiInstance.repositoriesWorkspaceRepoSlugPermissionsConfigUsersGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugPermissionsConfigUsersGet");
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

[**PaginatedRepositoryUserPermissions**](PaginatedRepositoryUserPermissions.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated of explicit user permissions on the repository. |  -  |
| **401** | The user couldn&#39;t be authenticated. |  -  |
| **403** | The requesting user isn&#39;t an admin of the repository. |  -  |
| **404** | No repository exists for the given repository slug and workspace. |  -  |

<a id="repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdDelete"></a>
# **repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdDelete**
> repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdDelete(repoSlug, selectedUserId, workspace)

Delete an explicit user permission for a repository

Deletes the repository user permission between the requested repository and user, if one exists.  Only users with admin permission for the repository may access this resource.  The only authentication method for this endpoint is via app passwords.  &#x60;&#x60;&#x60; $ curl -X DELETE https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/ permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a   HTTP/1.1 204 &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String selectedUserId = "selectedUserId_example"; // String | This can either be the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`, OR an Atlassian Account ID. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdDelete(repoSlug, selectedUserId, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdDelete");
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
| **selectedUserId** | **String**| This can either be the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;, OR an Atlassian Account ID.  | |
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
| **204** | The repository user permission was deleted and no content returned. |  -  |
| **401** | The user couldn&#39;t be authenticated. |  -  |
| **403** | The requesting user isn&#39;t an admin of the repository, or the authentication method was not via app password. |  -  |
| **404** | One or more of the workspace, repository, and user doesn&#39;t exist for the given identifiers. |  -  |

<a id="repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdGet"></a>
# **repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdGet**
> RepositoryUserPermission repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdGet(repoSlug, selectedUserId, workspace)

Get an explicit user permission for a repository

Returns the explicit user permission for a given user and repository.  Only users with admin permission for the repository may access this resource.  Permissions can be:  * &#x60;admin&#x60; * &#x60;write&#x60; * &#x60;read&#x60; * &#x60;none&#x60;  Example:  &#x60;&#x60;&#x60; $ curl &#39;https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/         permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a&#39;  HTTP/1.1 200 Location: &#39;https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/            permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a&#39;  {     \&quot;type\&quot;: \&quot;repository_user_permission\&quot;,     \&quot;user\&quot;: {         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;display_name\&quot;: \&quot;Colin Cameron\&quot;,         \&quot;uuid\&quot;: \&quot;{d301aafa-d676-4ee0-88be-962be7417567}\&quot;,         \&quot;account_id\&quot;: \&quot;557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\&quot;     },     \&quot;repository\&quot;: {         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;name\&quot;: \&quot;geordi\&quot;,         \&quot;full_name\&quot;: \&quot;atlassian_tutorial/geordi\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;     },     \&quot;permission\&quot;: \&quot;admin\&quot;,     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/                      permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\&quot;         }     } } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String selectedUserId = "selectedUserId_example"; // String | This can either be the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`, OR an Atlassian Account ID. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      RepositoryUserPermission result = apiInstance.repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdGet(repoSlug, selectedUserId, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdGet");
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
| **selectedUserId** | **String**| This can either be the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;, OR an Atlassian Account ID.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**RepositoryUserPermission**](RepositoryUserPermission.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Explicit user permission for user and repository |  -  |
| **401** | The user couldn&#39;t be authenticated. |  -  |
| **403** | The requesting user isn&#39;t an admin of the repository. |  -  |
| **404** | One or both of the workspace and repository doesn&#39;t exist for the given identifiers. |  -  |

<a id="repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdPut"></a>
# **repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdPut**
> RepositoryUserPermission repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdPut(repoSlug, selectedUserId, workspace)

Update an explicit user permission for a repository

Updates the explicit user permission for a given user and repository. The selected user must be a member of the workspace, and cannot be the workspace owner. Only users with admin permission for the repository may access this resource.  The only authentication method for this endpoint is via app passwords.  Permissions can be:  * &#x60;admin&#x60; * &#x60;write&#x60; * &#x60;read&#x60;  Example:  &#x60;&#x60;&#x60; $ curl -X PUT -H \&quot;Content-Type: application/json\&quot; &#39;https://api.bitbucket.org/2.0/repositories/ atlassian_tutorial/geordi/permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a&#39; -d         &#39;{     \&quot;permission\&quot;: \&quot;write\&quot; }&#39;  HTTP/1.1 200 Location: &#39;https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/ permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a&#39;   {     \&quot;type\&quot;: \&quot;repository_user_permission\&quot;,     \&quot;user\&quot;: {         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;display_name\&quot;: \&quot;Colin Cameron\&quot;,         \&quot;uuid\&quot;: \&quot;{d301aafa-d676-4ee0-88be-962be7417567}\&quot;,         \&quot;account_id\&quot;: \&quot;557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\&quot;     },     \&quot;repository\&quot;: {         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;name\&quot;: \&quot;geordi\&quot;,         \&quot;full_name\&quot;: \&quot;atlassian_tutorial/geordi\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;     },     \&quot;permission\&quot;: \&quot;write\&quot;,     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/                      permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\&quot;         }     } } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String selectedUserId = "selectedUserId_example"; // String | This can either be the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`, OR an Atlassian Account ID. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      RepositoryUserPermission result = apiInstance.repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdPut(repoSlug, selectedUserId, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugPermissionsConfigUsersSelectedUserIdPut");
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
| **selectedUserId** | **String**| This can either be the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;, OR an Atlassian Account ID.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**RepositoryUserPermission**](RepositoryUserPermission.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Explicit user permission updated |  -  |
| **400** | No permission value was provided or the value is invalid (not one of read, write, or admin), or the selected user is not a valid user to update. |  -  |
| **401** | The user couldn&#39;t be authenticated. |  -  |
| **402** | You have reached your plan&#39;s user limit and must upgrade before giving access to additional users. |  -  |
| **403** | The requesting user isn&#39;t an admin of the repository, or the authentication method was not via app password. |  -  |
| **404** | One or more of the workspace, repository, and selected user doesn&#39;t exist for the given identifiers. |  -  |

<a id="repositoriesWorkspaceRepoSlugPost"></a>
# **repositoriesWorkspaceRepoSlugPost**
> Repository repositoriesWorkspaceRepoSlugPost(repoSlug, workspace, repository)

Create a repository

Creates a new repository.  Note: In order to set the project for the newly created repository, pass in either the project key or the project UUID as part of the request body as shown in the examples below:  &#x60;&#x60;&#x60; $ curl -X POST -H \&quot;Content-Type: application/json\&quot; -d &#39;{     \&quot;scm\&quot;: \&quot;git\&quot;,     \&quot;project\&quot;: {         \&quot;key\&quot;: \&quot;MARS\&quot;     } }&#39; https://api.bitbucket.org/2.0/repositories/teamsinspace/hablanding &#x60;&#x60;&#x60;  or  &#x60;&#x60;&#x60; $ curl -X POST -H \&quot;Content-Type: application/json\&quot; -d &#39;{     \&quot;scm\&quot;: \&quot;git\&quot;,     \&quot;project\&quot;: {         \&quot;key\&quot;: \&quot;{ba516952-992a-4c2d-acbd-17d502922f96}\&quot;     } }&#39; https://api.bitbucket.org/2.0/repositories/teamsinspace/hablanding &#x60;&#x60;&#x60;  The project must be assigned for all repositories. If the project is not provided, the repository is automatically assigned to the oldest project in the workspace.  Note: In the examples above, the workspace ID &#x60;teamsinspace&#x60;, and/or the repository name &#x60;hablanding&#x60; can be replaced by UUIDs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    Repository repository = new Repository(); // Repository | The repository that is to be created. Note that most object elements are optional. Elements \"owner\" and \"full_name\" are ignored as the URL implies them.
    try {
      Repository result = apiInstance.repositoriesWorkspaceRepoSlugPost(repoSlug, workspace, repository);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugPost");
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
| **repository** | [**Repository**](Repository.md)| The repository that is to be created. Note that most object elements are optional. Elements \&quot;owner\&quot; and \&quot;full_name\&quot; are ignored as the URL implies them. | [optional] |

### Return type

[**Repository**](Repository.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The newly created repository. |  -  |
| **400** | If the input document was invalid, or if the caller lacks the privilege to create repositories under the targeted account. |  -  |
| **401** | If the request was not authenticated. |  -  |

<a id="repositoriesWorkspaceRepoSlugPut"></a>
# **repositoriesWorkspaceRepoSlugPut**
> Repository repositoriesWorkspaceRepoSlugPut(repoSlug, workspace, repository)

Update a repository

Since this endpoint can be used to both update and to create a repository, the request body depends on the intent.  #### Creation  See the POST documentation for the repository endpoint for an example of the request body.  #### Update  Note: Changing the &#x60;name&#x60; of the repository will cause the location to be changed. This is because the URL of the repo is derived from the name (a process called slugification). In such a scenario, it is possible for the request to fail if the newly created slug conflicts with an existing repository&#39;s slug. But if there is no conflict, the new location will be returned in the &#x60;Location&#x60; header of the response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    Repository repository = new Repository(); // Repository | The repository that is to be updated.  Note that the elements \"owner\" and \"full_name\" are ignored since the URL implies them. 
    try {
      Repository result = apiInstance.repositoriesWorkspaceRepoSlugPut(repoSlug, workspace, repository);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugPut");
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
| **repository** | [**Repository**](Repository.md)| The repository that is to be updated.  Note that the elements \&quot;owner\&quot; and \&quot;full_name\&quot; are ignored since the URL implies them.  | [optional] |

### Return type

[**Repository**](Repository.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The existing repository has been updated |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **201** | A new repository has been created |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **400** | If the input document was invalid, or if the caller lacks the privilege to create repositories under the targeted account. |  -  |
| **401** | If the request was not authenticated. |  -  |

<a id="repositoriesWorkspaceRepoSlugSrcCommitPathGet_0"></a>
# **repositoriesWorkspaceRepoSlugSrcCommitPathGet_0**
> PaginatedTreeentries repositoriesWorkspaceRepoSlugSrcCommitPathGet_0(commit, path, repoSlug, workspace, format, q, sort, maxDepth)

Get file or directory contents

This endpoints is used to retrieve the contents of a single file, or the contents of a directory at a specified revision.  #### Raw file contents  When &#x60;path&#x60; points to a file, this endpoint returns the raw contents. The response&#39;s Content-Type is derived from the filename extension (not from the contents). The file contents are not processed and no character encoding/recoding is performed and as a result no character encoding is included as part of the Content-Type.  The &#x60;Content-Disposition&#x60; header will be \&quot;attachment\&quot; to prevent browsers from running executable files.  If the file is managed by LFS, then a 301 redirect pointing to Atlassian&#39;s media services platform is returned.  The response includes an ETag that is based on the contents of the file and its attributes. This means that an empty &#x60;__init__.py&#x60; always returns the same ETag, regardless on the directory it lives in, or the commit it is on.  #### File meta data  When the request for a file path includes the query parameter &#x60;?format&#x3D;meta&#x60;, instead of returning the file&#39;s raw contents, Bitbucket instead returns the JSON object describing the file&#39;s properties:  &#x60;&#x60;&#x60;javascript $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests/__init__.py?format&#x3D;meta {   \&quot;links\&quot;: {     \&quot;self\&quot;: {       \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py\&quot;     },     \&quot;meta\&quot;: {       \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py?format&#x3D;meta\&quot;     }   },   \&quot;path\&quot;: \&quot;tests/__init__.py\&quot;,   \&quot;commit\&quot;: {     \&quot;type\&quot;: \&quot;commit\&quot;,     \&quot;hash\&quot;: \&quot;eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;,     \&quot;links\&quot;: {       \&quot;self\&quot;: {         \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;       },       \&quot;html\&quot;: {         \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;       }     }   },   \&quot;attributes\&quot;: [],   \&quot;type\&quot;: \&quot;commit_file\&quot;,   \&quot;size\&quot;: 0 } &#x60;&#x60;&#x60;  File objects contain an &#x60;attributes&#x60; element that contains a list of possible modifiers. Currently defined values are:  * &#x60;link&#x60; -- indicates that the entry is a symbolic link. The contents     of the file represent the path the link points to. * &#x60;executable&#x60; -- indicates that the file has the executable bit set. * &#x60;subrepository&#x60; -- indicates that the entry points to a submodule or     subrepo. The contents of the file is the SHA1 of the repository     pointed to. * &#x60;binary&#x60; -- indicates whether Bitbucket thinks the file is binary.  This endpoint can provide an alternative to how a HEAD request can be used to check for the existence of a file, or a file&#39;s size without incurring the overhead of receiving its full contents.   #### Directory listings  When &#x60;path&#x60; points to a directory instead of a file, the response is a paginated list of directory and file objects in the same order as the underlying SCM system would return them.  For example:  &#x60;&#x60;&#x60;javascript $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests {   \&quot;pagelen\&quot;: 10,   \&quot;values\&quot;: [     {       \&quot;path\&quot;: \&quot;tests/test_project\&quot;,       \&quot;type\&quot;: \&quot;commit_directory\&quot;,       \&quot;links\&quot;: {         \&quot;self\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/\&quot;         },         \&quot;meta\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/?format&#x3D;meta\&quot;         }       },       \&quot;commit\&quot;: {         \&quot;type\&quot;: \&quot;commit\&quot;,         \&quot;hash\&quot;: \&quot;eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;           },           \&quot;html\&quot;: {             \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;           }         }       }     },     {       \&quot;links\&quot;: {         \&quot;self\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py\&quot;         },         \&quot;meta\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py?format&#x3D;meta\&quot;         }       },       \&quot;path\&quot;: \&quot;tests/__init__.py\&quot;,       \&quot;commit\&quot;: {         \&quot;type\&quot;: \&quot;commit\&quot;,         \&quot;hash\&quot;: \&quot;eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;           },           \&quot;html\&quot;: {             \&quot;href\&quot;: \&quot;https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\&quot;           }         }       },       \&quot;attributes\&quot;: [],       \&quot;type\&quot;: \&quot;commit_file\&quot;,       \&quot;size\&quot;: 0     }   ],   \&quot;page\&quot;: 1,   \&quot;size\&quot;: 2 } &#x60;&#x60;&#x60;  When listing the contents of the repo&#39;s root directory, the use of a trailing slash at the end of the URL is required.  The response by default is not recursive, meaning that only the direct contents of a path are returned. The response does not recurse down into subdirectories. In order to \&quot;walk\&quot; the entire directory tree, the client can either parse each response and follow the &#x60;self&#x60; links of each &#x60;commit_directory&#x60; object, or can specify a &#x60;max_depth&#x60; to recurse to.  The max_depth parameter will do a breadth-first search to return the contents of the subdirectories up to the depth specified. Breadth-first search was chosen as it leads to the least amount of file system operations for git. If the &#x60;max_depth&#x60; parameter is specified to be too large, the call will time out and return a 555.  Each returned object is either a &#x60;commit_file&#x60;, or a &#x60;commit_directory&#x60;, both of which contain a &#x60;path&#x60; element. This path is the absolute path from the root of the repository. Each object also contains a &#x60;commit&#x60; object which embeds the commit the file is on. Note that this is merely the commit that was used in the URL. It is *not* the commit that last modified the file.  Directory objects have 2 representations. Their &#x60;self&#x60; link returns the paginated contents of the directory. The &#x60;meta&#x60; link on the other hand returns the actual &#x60;directory&#x60; object itself, e.g.:  &#x60;&#x60;&#x60;javascript {   \&quot;path\&quot;: \&quot;tests/test_project\&quot;,   \&quot;type\&quot;: \&quot;commit_directory\&quot;,   \&quot;links\&quot;: {     \&quot;self\&quot;: {       \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/\&quot;     },     \&quot;meta\&quot;: {       \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/?format&#x3D;meta\&quot;     }   },   \&quot;commit\&quot;: { ... } } &#x60;&#x60;&#x60;  #### Querying, filtering and sorting  Like most API endpoints, this API supports the Bitbucket querying/filtering syntax and so you could filter a directory listing to only include entries that match certain criteria. For instance, to list all binary files over 1kb use the expression:  &#x60;size &gt; 1024 and attributes &#x3D; \&quot;binary\&quot;&#x60;  which after urlencoding yields the query string:  &#x60;?q&#x3D;size%3E1024+and+attributes%3D%22binary%22&#x60;  To change the ordering of the response, use the &#x60;?sort&#x60; parameter:  &#x60;.../src/eefd5ef/?sort&#x3D;-size&#x60;  See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String commit = "commit_example"; // String | The commit's SHA1.
    String path = "path_example"; // String | Path to the file.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String format = "meta"; // String | If 'meta' is provided, returns the (json) meta data for the contents of the file.  If 'rendered' is provided, returns the contents of a non-binary file in HTML-formatted rendered markup. Since Git does not generally track what text encoding scheme is used, this endpoint attempts to detect the most appropriate character encoding. While usually correct, determining the character encoding can be ambiguous which in exceptional cases can lead to misinterpretation of the characters. As such, the raw element in the response object should not be treated as equivalent to the file's actual contents.
    String q = "q_example"; // String | Optional filter expression as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).
    String sort = "sort_example"; // String | Optional sorting parameter as per [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results).
    Integer maxDepth = 56; // Integer | If provided, returns the contents of the repository and its subdirectories recursively until the specified max_depth of nested directories. When omitted, this defaults to 1.
    try {
      PaginatedTreeentries result = apiInstance.repositoriesWorkspaceRepoSlugSrcCommitPathGet_0(commit, path, repoSlug, workspace, format, q, sort, maxDepth);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugSrcCommitPathGet_0");
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
| **commit** | **String**| The commit&#39;s SHA1. | |
| **path** | **String**| Path to the file. | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **format** | **String**| If &#39;meta&#39; is provided, returns the (json) meta data for the contents of the file.  If &#39;rendered&#39; is provided, returns the contents of a non-binary file in HTML-formatted rendered markup. Since Git does not generally track what text encoding scheme is used, this endpoint attempts to detect the most appropriate character encoding. While usually correct, determining the character encoding can be ambiguous which in exceptional cases can lead to misinterpretation of the characters. As such, the raw element in the response object should not be treated as equivalent to the file&#39;s actual contents. | [optional] [enum: meta, rendered] |
| **q** | **String**| Optional filter expression as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). | [optional] |
| **sort** | **String**| Optional sorting parameter as per [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results). | [optional] |
| **maxDepth** | **Integer**| If provided, returns the contents of the repository and its subdirectories recursively until the specified max_depth of nested directories. When omitted, this defaults to 1. | [optional] |

### Return type

[**PaginatedTreeentries**](PaginatedTreeentries.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If the path matches a file, then the raw contents of the file are returned.  If the &#x60;format&#x3D;meta&#x60; query parameter is provided, a json document containing the file&#39;s meta data is returned.  If the &#x60;format&#x3D;rendered&#x60; query parameter is provided, the contents of the file in HTML-formated rendered markup is returned. If the path matches a directory, then a paginated list of file and directory entries is returned (if the &#x60;format&#x3D;meta&#x60; query parameter was provided, then the json document containing the directory&#39;s meta data is returned.)  |  -  |
| **404** | If the path or commit in the URL does not exist. |  -  |
| **555** | If the call times out, possibly because the specified recursion depth is too large. |  -  |

<a id="repositoriesWorkspaceRepoSlugSrcGet_0"></a>
# **repositoriesWorkspaceRepoSlugSrcGet_0**
> PaginatedTreeentries repositoriesWorkspaceRepoSlugSrcGet_0(repoSlug, workspace, format)

Get the root directory of the main branch

This endpoint redirects the client to the directory listing of the root directory on the main branch.  This is equivalent to directly hitting [/2.0/repositories/{username}/{repo_slug}/src/{commit}/{path}](src/%7Bcommit%7D/%7Bpath%7D) without having to know the name or SHA1 of the repo&#39;s main branch.  To create new commits, [POST to this endpoint](#post)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String format = "meta"; // String | Instead of returning the file's contents, return the (json) meta data for it.
    try {
      PaginatedTreeentries result = apiInstance.repositoriesWorkspaceRepoSlugSrcGet_0(repoSlug, workspace, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugSrcGet_0");
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
| **format** | **String**| Instead of returning the file&#39;s contents, return the (json) meta data for it. | [optional] [enum: meta] |

### Return type

[**PaginatedTreeentries**](PaginatedTreeentries.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If the path matches a file, then the raw contents of the file are returned (unless the &#x60;format&#x3D;meta&#x60; query parameter was provided, in which case a json document containing the file&#39;s meta data is returned). If the path matches a directory, then a paginated list of file and directory entries is returned (if the &#x60;format&#x3D;meta&#x60; query parameter was provided, then the json document containing the directory&#39;s meta data is returned).  |  -  |
| **404** | If the path or commit in the URL does not exist. |  -  |

<a id="repositoriesWorkspaceRepoSlugSrcPost_0"></a>
# **repositoriesWorkspaceRepoSlugSrcPost_0**
> repositoriesWorkspaceRepoSlugSrcPost_0(repoSlug, workspace, message, author, parents, files, branch)

Create a commit by uploading a file

This endpoint is used to create new commits in the repository by uploading files.  To add a new file to a repository:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \\   -F /repo/path/to/image.png&#x3D;@image.png &#x60;&#x60;&#x60;  This will create a new commit on top of the main branch, inheriting the contents of the main branch, but adding (or overwriting) the &#x60;image.png&#x60; file to the repository in the &#x60;/repo/path/to&#x60; directory.  To create a commit that deletes files, use the &#x60;files&#x60; parameter:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \\   -F files&#x3D;/file/to/delete/1.txt \\   -F files&#x3D;/file/to/delete/2.txt &#x60;&#x60;&#x60;  You can add/modify/delete multiple files in a request. Rename/move a file by deleting the old path and adding the content at the new path.  This endpoint accepts &#x60;multipart/form-data&#x60; (as in the examples above), as well as &#x60;application/x-www-form-urlencoded&#x60;.  #### multipart/form-data  A &#x60;multipart/form-data&#x60; post contains a series of \&quot;form fields\&quot; that identify both the individual files that are being uploaded, as well as additional, optional meta data.  Files are uploaded in file form fields (those that have a &#x60;Content-Disposition&#x60; parameter) whose field names point to the remote path in the repository where the file should be stored. Path field names are always interpreted to be absolute from the root of the repository, regardless whether the client uses a leading slash (as the above &#x60;curl&#x60; example did).  File contents are treated as bytes and are not decoded as text.  The commit message, as well as other non-file meta data for the request, is sent along as normal form field elements. Meta data fields share the same namespace as the file objects. For &#x60;multipart/form-data&#x60; bodies that should not lead to any ambiguity, as the &#x60;Content-Disposition&#x60; header will contain the &#x60;filename&#x60; parameter to distinguish between a file named \&quot;message\&quot; and the commit message field.  #### application/x-www-form-urlencoded  It is also possible to upload new files using a simple &#x60;application/x-www-form-urlencoded&#x60; POST. This can be convenient when uploading pure text files:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src \\   --data-urlencode \&quot;/path/to/me.txt&#x3D;Lorem ipsum.\&quot; \\   --data-urlencode \&quot;message&#x3D;Initial commit\&quot; \\   --data-urlencode \&quot;author&#x3D;Erik van Zijst &lt;erik.van.zijst@gmail.com&gt;\&quot; &#x60;&#x60;&#x60;  There could be a field name clash if a client were to upload a file named \&quot;message\&quot;, as this filename clashes with the meta data property for the commit message. To avoid this and to upload files whose names clash with the meta data properties, use a leading slash for the files, e.g. &#x60;curl --data-urlencode \&quot;/message&#x3D;file contents\&quot;&#x60;.  When an explicit slash is omitted for a file whose path matches that of a meta data parameter, then it is interpreted as meta data, not as a file.  #### Executables and links  While this API aims to facilitate the most common use cases, it is possible to perform some more advanced operations like creating a new symlink in the repository, or creating an executable file.  Files can be supplied with a &#x60;x-attributes&#x60; value in the &#x60;Content-Disposition&#x60; header. For example, to upload an executable file, as well as create a symlink from &#x60;README.txt&#x60; to &#x60;README&#x60;:  &#x60;&#x60;&#x60; --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D; Content-Type: text/plain; charset&#x3D;\&quot;us-ascii\&quot; MIME-Version: 1.0 Content-Transfer-Encoding: 7bit Content-ID: \&quot;bin/shutdown.sh\&quot; Content-Disposition: attachment; filename&#x3D;\&quot;shutdown.sh\&quot;; x-attributes:\&quot;executable\&quot;  #!/bin/sh halt  --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D; Content-Type: text/plain; charset&#x3D;\&quot;us-ascii\&quot; MIME-Version: 1.0 Content-Transfer-Encoding: 7bit Content-ID: \&quot;/README.txt\&quot; Content-Disposition: attachment; filename&#x3D;\&quot;README.txt\&quot;; x-attributes:\&quot;link\&quot;  README --&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;1438169132528273974&#x3D;&#x3D;-- &#x60;&#x60;&#x60;  Links are files that contain the target path and have &#x60;x-attributes:\&quot;link\&quot;&#x60; set.  When overwriting links with files, or vice versa, the newly uploaded file determines both the new contents, as well as the attributes. That means uploading a file without specifying &#x60;x-attributes&#x3D;\&quot;link\&quot;&#x60; will create a regular file, even if the parent commit hosted a symlink at the same path.  The same applies to executables. When modifying an existing executable file, the form-data file element must include &#x60;x-attributes&#x3D;\&quot;executable\&quot;&#x60; in order to preserve the executable status of the file.  Note that this API does not support the creation or manipulation of subrepos / submodules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String message = "message_example"; // String | The commit message. When omitted, Bitbucket uses a canned string.
    String author = "author_example"; // String |  The raw string to be used as the new commit's author. This string follows the format `Erik van Zijst <evzijst@atlassian.com>`.  When omitted, Bitbucket uses the authenticated user's full/display name and primary email address. Commits cannot be created anonymously.
    String parents = "parents_example"; // String |  A comma-separated list of SHA1s of the commits that should be the parents of the newly created commit.  When omitted, the new commit will inherit from and become a child of the main branch's tip/HEAD commit.  When more than one SHA1 is provided, the first SHA1 identifies the commit from which the content will be inherited.\".
    String files = "files_example"; // String |  Optional field that declares the files that the request is manipulating. When adding a new file to a repo, or when overwriting an existing file, the client can just upload the full contents of the file in a normal form field and the use of this `files` meta data field is redundant. However, when the `files` field contains a file path that does not have a corresponding, identically-named form field, then Bitbucket interprets that as the client wanting to replace the named file with the null set and the file is deleted instead.  Paths in the repo that are referenced in neither files nor an individual file field, remain unchanged and carry over from the parent to the new commit.  This API does not support renaming as an explicit feature. To rename a file, simply delete it and recreate it under the new name in the same commit. 
    String branch = "branch_example"; // String |  The name of the branch that the new commit should be created on. When omitted, the commit will be created on top of the main branch and will become the main branch's new head.  When a branch name is provided that already exists in the repo, then the commit will be created on top of that branch. In this case, *if* a parent SHA1 was also provided, then it is asserted that the parent is the branch's tip/HEAD at the time the request is made. When this is not the case, a 409 is returned.  When a new branch name is specified (that does not already exist in the repo), and no parent SHA1s are provided, then the new commit will inherit from the current main branch's tip/HEAD commit, but not advance the main branch. The new commit will be the new branch. When the request *also* specifies a parent SHA1, then the new commit and branch are created directly on top of the parent commit, regardless of the state of the main branch.  When a branch name is not specified, but a parent SHA1 is provided, then Bitbucket asserts that it represents the main branch's current HEAD/tip, or a 409 is returned.  When a branch name is not specified and the repo is empty, the new commit will become the repo's root commit and will be on the main branch.  When a branch name is specified and the repo is empty, the new commit will become the repo's root commit and also define the repo's main branch going forward.  This API cannot be used to create additional root commits in non-empty repos.  The branch field cannot be repeated.  As a side effect, this API can be used to create a new branch without modifying any files, by specifying a new branch name in this field, together with `parents`, but omitting the `files` fields, while not sending any files. This will create a new commit and branch with the same contents as the first parent. The diff of this commit against its first parent will be empty. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugSrcPost_0(repoSlug, workspace, message, author, parents, files, branch);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugSrcPost_0");
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
| **message** | **String**| The commit message. When omitted, Bitbucket uses a canned string. | [optional] |
| **author** | **String**|  The raw string to be used as the new commit&#39;s author. This string follows the format &#x60;Erik van Zijst &lt;evzijst@atlassian.com&gt;&#x60;.  When omitted, Bitbucket uses the authenticated user&#39;s full/display name and primary email address. Commits cannot be created anonymously. | [optional] |
| **parents** | **String**|  A comma-separated list of SHA1s of the commits that should be the parents of the newly created commit.  When omitted, the new commit will inherit from and become a child of the main branch&#39;s tip/HEAD commit.  When more than one SHA1 is provided, the first SHA1 identifies the commit from which the content will be inherited.\&quot;. | [optional] |
| **files** | **String**|  Optional field that declares the files that the request is manipulating. When adding a new file to a repo, or when overwriting an existing file, the client can just upload the full contents of the file in a normal form field and the use of this &#x60;files&#x60; meta data field is redundant. However, when the &#x60;files&#x60; field contains a file path that does not have a corresponding, identically-named form field, then Bitbucket interprets that as the client wanting to replace the named file with the null set and the file is deleted instead.  Paths in the repo that are referenced in neither files nor an individual file field, remain unchanged and carry over from the parent to the new commit.  This API does not support renaming as an explicit feature. To rename a file, simply delete it and recreate it under the new name in the same commit.  | [optional] |
| **branch** | **String**|  The name of the branch that the new commit should be created on. When omitted, the commit will be created on top of the main branch and will become the main branch&#39;s new head.  When a branch name is provided that already exists in the repo, then the commit will be created on top of that branch. In this case, *if* a parent SHA1 was also provided, then it is asserted that the parent is the branch&#39;s tip/HEAD at the time the request is made. When this is not the case, a 409 is returned.  When a new branch name is specified (that does not already exist in the repo), and no parent SHA1s are provided, then the new commit will inherit from the current main branch&#39;s tip/HEAD commit, but not advance the main branch. The new commit will be the new branch. When the request *also* specifies a parent SHA1, then the new commit and branch are created directly on top of the parent commit, regardless of the state of the main branch.  When a branch name is not specified, but a parent SHA1 is provided, then Bitbucket asserts that it represents the main branch&#39;s current HEAD/tip, or a 409 is returned.  When a branch name is not specified and the repo is empty, the new commit will become the repo&#39;s root commit and will be on the main branch.  When a branch name is specified and the repo is empty, the new commit will become the repo&#39;s root commit and also define the repo&#39;s main branch going forward.  This API cannot be used to create additional root commits in non-empty repos.  The branch field cannot be repeated.  As a side effect, this API can be used to create a new branch without modifying any files, by specifying a new branch name in this field, together with &#x60;parents&#x60;, but omitting the &#x60;files&#x60; fields, while not sending any files. This will create a new commit and branch with the same contents as the first parent. The diff of this commit against its first parent will be empty.  | [optional] |

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
| **201** |   |  -  |
| **403** | If the authenticated user does not have write or admin access |  -  |
| **404** | If the repository does not exist. |  -  |

<a id="repositoriesWorkspaceRepoSlugWatchersGet"></a>
# **repositoriesWorkspaceRepoSlugWatchersGet**
> PaginatedAccounts repositoriesWorkspaceRepoSlugWatchersGet(repoSlug, workspace)

List repositories watchers

Returns a paginated list of all the watchers on the specified repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedAccounts result = apiInstance.repositoriesWorkspaceRepoSlugWatchersGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesWorkspaceRepoSlugWatchersGet");
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

[**PaginatedAccounts**](PaginatedAccounts.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of all the watchers on the specified repository. |  -  |

<a id="userPermissionsRepositoriesGet"></a>
# **userPermissionsRepositoriesGet**
> PaginatedRepositoryPermissions userPermissionsRepositoriesGet(q, sort)

List repository permissions for a user

Returns an object for each repository the caller has explicit access to and their effective permission — the highest level of permission the caller has. This does not return public repositories that the user was not granted any specific permission in, and does not distinguish between explicit and implicit privileges.  Permissions can be:  * &#x60;admin&#x60; * &#x60;write&#x60; * &#x60;read&#x60;  Example:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/user/permissions/repositories  {   \&quot;pagelen\&quot;: 10,   \&quot;values\&quot;: [     {       \&quot;type\&quot;: \&quot;repository_permission\&quot;,       \&quot;user\&quot;: {         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;nickname\&quot;: \&quot;evzijst\&quot;,         \&quot;display_name\&quot;: \&quot;Erik van Zijst\&quot;,         \&quot;uuid\&quot;: \&quot;{d301aafa-d676-4ee0-88be-962be7417567}\&quot;       },       \&quot;repository\&quot;: {         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;name\&quot;: \&quot;geordi\&quot;,         \&quot;full_name\&quot;: \&quot;bitbucket/geordi\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;       },       \&quot;permission\&quot;: \&quot;admin\&quot;     }   ],   \&quot;page\&quot;: 1,   \&quot;size\&quot;: 1 } &#x60;&#x60;&#x60;  Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by repository or permission by adding the following query string parameters:  * &#x60;q&#x3D;repository.name&#x3D;\&quot;geordi\&quot;&#x60; or &#x60;q&#x3D;permission&gt;\&quot;read\&quot;&#x60; * &#x60;sort&#x3D;repository.name&#x60;  Note that the query parameter values need to be URL escaped so that &#x60;&#x3D;&#x60; would become &#x60;%3D&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

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

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String q = "q_example"; // String |  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).
    String sort = "sort_example"; // String |  Name of a response property sort the result by as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).
    try {
      PaginatedRepositoryPermissions result = apiInstance.userPermissionsRepositoriesGet(q, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#userPermissionsRepositoriesGet");
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
| **q** | **String**|  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). | [optional] |
| **sort** | **String**|  Name of a response property sort the result by as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). | [optional] |

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
| **200** | Repository permissions for the repositories a caller has explicit access to. |  -  |

