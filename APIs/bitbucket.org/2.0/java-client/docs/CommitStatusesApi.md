# CommitStatusesApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyGet**](CommitStatusesApi.md#repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyGet) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key} | Get a build status for a commit |
| [**repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyPut**](CommitStatusesApi.md#repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyPut) | **PUT** /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key} | Update a build status for a commit |
| [**repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildPost**](CommitStatusesApi.md#repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildPost) | **POST** /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build | Create a build status for a commit |
| [**repositoriesWorkspaceRepoSlugCommitCommitStatusesGet**](CommitStatusesApi.md#repositoriesWorkspaceRepoSlugCommitCommitStatusesGet) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses | List commit statuses for a commit |
| [**repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdStatusesGet_0**](CommitStatusesApi.md#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdStatusesGet_0) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/statuses | List commit statuses for a pull request |


<a id="repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyGet"></a>
# **repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyGet**
> Commitstatus repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyGet(commit, key, repoSlug, workspace)

Get a build status for a commit

Returns the specified build status for a commit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitStatusesApi;

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

    CommitStatusesApi apiInstance = new CommitStatusesApi(defaultClient);
    String commit = "commit_example"; // String | The commit's SHA1.
    String key = "key_example"; // String | The build status' unique key
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Commitstatus result = apiInstance.repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyGet(commit, key, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitStatusesApi#repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyGet");
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
| **key** | **String**| The build status&#39; unique key | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Commitstatus**](Commitstatus.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The build status object with the specified key. |  -  |
| **401** | If the repository is private and the request was not authenticated. |  -  |
| **404** | If the repository, commit, or build status key does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyPut"></a>
# **repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyPut**
> Commitstatus repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyPut(commit, key, repoSlug, workspace, commitstatus)

Update a build status for a commit

Used to update the current status of a build status object on the specific commit.  This operation can also be used to change other properties of the build status:  * &#x60;state&#x60; * &#x60;name&#x60; * &#x60;description&#x60; * &#x60;url&#x60; * &#x60;refname&#x60;  The &#x60;key&#x60; cannot be changed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitStatusesApi;

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

    CommitStatusesApi apiInstance = new CommitStatusesApi(defaultClient);
    String commit = "commit_example"; // String | The commit's SHA1.
    String key = "key_example"; // String | The build status' unique key
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    Commitstatus commitstatus = new Commitstatus(); // Commitstatus | The updated build status object
    try {
      Commitstatus result = apiInstance.repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyPut(commit, key, repoSlug, workspace, commitstatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitStatusesApi#repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildKeyPut");
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
| **key** | **String**| The build status&#39; unique key | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **commitstatus** | [**Commitstatus**](Commitstatus.md)| The updated build status object | [optional] |

### Return type

[**Commitstatus**](Commitstatus.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated build status object. |  -  |
| **401** | If the repository is private and the request was not authenticated. |  -  |
| **404** | If the repository or build does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildPost"></a>
# **repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildPost**
> Commitstatus repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildPost(commit, repoSlug, workspace, commitstatus)

Create a build status for a commit

Creates a new build status against the specified commit.  If the specified key already exists, the existing status object will be overwritten.  Example:  &#x60;&#x60;&#x60; curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-repo/commit/e10dae226959c2194f2b07b077c07762d93821cf/statuses/build/           -X POST -u jdoe -H &#39;Content-Type: application/json&#39;           -d &#39;{     \&quot;key\&quot;: \&quot;MY-BUILD\&quot;,     \&quot;state\&quot;: \&quot;SUCCESSFUL\&quot;,     \&quot;description\&quot;: \&quot;42 tests passed\&quot;,     \&quot;url\&quot;: \&quot;https://www.example.org/my-build-result\&quot;   }&#39; &#x60;&#x60;&#x60;  When creating a new commit status, you can use a URI template for the URL. Templates are URLs that contain variable names that Bitbucket will evaluate at runtime whenever the URL is displayed anywhere similar to parameter substitution in [Bitbucket Connect](https://developer.atlassian.com/bitbucket/concepts/context-parameters.html). For example, one could use &#x60;https://foo.com/builds/{repository.full_name}&#x60; which Bitbucket will turn into &#x60;https://foo.com/builds/foo/bar&#x60; at render time. The context variables available are &#x60;repository&#x60; and &#x60;commit&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitStatusesApi;

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

    CommitStatusesApi apiInstance = new CommitStatusesApi(defaultClient);
    String commit = "commit_example"; // String | The commit's SHA1.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    Commitstatus commitstatus = new Commitstatus(); // Commitstatus | The new commit status object.
    try {
      Commitstatus result = apiInstance.repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildPost(commit, repoSlug, workspace, commitstatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitStatusesApi#repositoriesWorkspaceRepoSlugCommitCommitStatusesBuildPost");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **commitstatus** | [**Commitstatus**](Commitstatus.md)| The new commit status object. | [optional] |

### Return type

[**Commitstatus**](Commitstatus.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The newly created build status object. |  -  |
| **401** | If the repository is private and the request was not authenticated. |  -  |
| **404** | If the repository, commit, or build status key does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugCommitCommitStatusesGet"></a>
# **repositoriesWorkspaceRepoSlugCommitCommitStatusesGet**
> PaginatedCommitstatuses repositoriesWorkspaceRepoSlugCommitCommitStatusesGet(commit, repoSlug, workspace, q, sort)

List commit statuses for a commit

Returns all statuses (e.g. build results) for a specific commit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitStatusesApi;

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

    CommitStatusesApi apiInstance = new CommitStatusesApi(defaultClient);
    String commit = "commit_example"; // String | The commit's SHA1.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String q = "q_example"; // String | Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). 
    String sort = "sort_example"; // String | Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). Defaults to `created_on`. 
    try {
      PaginatedCommitstatuses result = apiInstance.repositoriesWorkspaceRepoSlugCommitCommitStatusesGet(commit, repoSlug, workspace, q, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitStatusesApi#repositoriesWorkspaceRepoSlugCommitCommitStatusesGet");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **q** | **String**| Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).  | [optional] |
| **sort** | **String**| Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). Defaults to &#x60;created_on&#x60;.  | [optional] |

### Return type

[**PaginatedCommitstatuses**](PaginatedCommitstatuses.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of all commit statuses for this commit. |  -  |
| **401** | If the repository is private and the request was not authenticated. |  -  |
| **404** | If the repository or commit does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdStatusesGet_0"></a>
# **repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdStatusesGet_0**
> PaginatedCommitstatuses repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdStatusesGet_0(pullRequestId, repoSlug, workspace, q, sort)

List commit statuses for a pull request

Returns all statuses (e.g. build results) for the given pull request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitStatusesApi;

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

    CommitStatusesApi apiInstance = new CommitStatusesApi(defaultClient);
    Integer pullRequestId = 56; // Integer | The id of the pull request.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String q = "q_example"; // String | Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). 
    String sort = "sort_example"; // String | Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). Defaults to `created_on`. 
    try {
      PaginatedCommitstatuses result = apiInstance.repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdStatusesGet_0(pullRequestId, repoSlug, workspace, q, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitStatusesApi#repositoriesWorkspaceRepoSlugPullrequestsPullRequestIdStatusesGet_0");
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
| **pullRequestId** | **Integer**| The id of the pull request. | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **q** | **String**| Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).  | [optional] |
| **sort** | **String**| Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). Defaults to &#x60;created_on&#x60;.  | [optional] |

### Return type

[**PaginatedCommitstatuses**](PaginatedCommitstatuses.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of all commit statuses for this pull request. |  -  |
| **401** | If the repository is private and the request was not authenticated. |  -  |
| **404** | If the specified repository or pull request does not exist. |  -  |

