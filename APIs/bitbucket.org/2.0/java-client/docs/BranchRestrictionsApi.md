# BranchRestrictionsApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**repositoriesWorkspaceRepoSlugBranchRestrictionsGet**](BranchRestrictionsApi.md#repositoriesWorkspaceRepoSlugBranchRestrictionsGet) | **GET** /repositories/{workspace}/{repo_slug}/branch-restrictions | List branch restrictions |
| [**repositoriesWorkspaceRepoSlugBranchRestrictionsIdDelete**](BranchRestrictionsApi.md#repositoriesWorkspaceRepoSlugBranchRestrictionsIdDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/branch-restrictions/{id} | Delete a branch restriction rule |
| [**repositoriesWorkspaceRepoSlugBranchRestrictionsIdGet**](BranchRestrictionsApi.md#repositoriesWorkspaceRepoSlugBranchRestrictionsIdGet) | **GET** /repositories/{workspace}/{repo_slug}/branch-restrictions/{id} | Get a branch restriction rule |
| [**repositoriesWorkspaceRepoSlugBranchRestrictionsIdPut**](BranchRestrictionsApi.md#repositoriesWorkspaceRepoSlugBranchRestrictionsIdPut) | **PUT** /repositories/{workspace}/{repo_slug}/branch-restrictions/{id} | Update a branch restriction rule |
| [**repositoriesWorkspaceRepoSlugBranchRestrictionsPost**](BranchRestrictionsApi.md#repositoriesWorkspaceRepoSlugBranchRestrictionsPost) | **POST** /repositories/{workspace}/{repo_slug}/branch-restrictions | Create a branch restriction rule |


<a id="repositoriesWorkspaceRepoSlugBranchRestrictionsGet"></a>
# **repositoriesWorkspaceRepoSlugBranchRestrictionsGet**
> PaginatedBranchrestrictions repositoriesWorkspaceRepoSlugBranchRestrictionsGet(repoSlug, workspace, kind, pattern)

List branch restrictions

Returns a paginated list of all branch restrictions on the repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchRestrictionsApi;

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

    BranchRestrictionsApi apiInstance = new BranchRestrictionsApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String kind = "kind_example"; // String | Branch restrictions of this type
    String pattern = "pattern_example"; // String | Branch restrictions applied to branches of this pattern
    try {
      PaginatedBranchrestrictions result = apiInstance.repositoriesWorkspaceRepoSlugBranchRestrictionsGet(repoSlug, workspace, kind, pattern);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchRestrictionsApi#repositoriesWorkspaceRepoSlugBranchRestrictionsGet");
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
| **kind** | **String**| Branch restrictions of this type | [optional] |
| **pattern** | **String**| Branch restrictions applied to branches of this pattern | [optional] |

### Return type

[**PaginatedBranchrestrictions**](PaginatedBranchrestrictions.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of branch restrictions |  -  |
| **401** | If the request was not authenticated |  -  |
| **403** | If the authenticated user does not have admin access to the repository |  -  |
| **404** | If the repository does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugBranchRestrictionsIdDelete"></a>
# **repositoriesWorkspaceRepoSlugBranchRestrictionsIdDelete**
> repositoriesWorkspaceRepoSlugBranchRestrictionsIdDelete(id, repoSlug, workspace)

Delete a branch restriction rule

Deletes an existing branch restriction rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchRestrictionsApi;

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

    BranchRestrictionsApi apiInstance = new BranchRestrictionsApi(defaultClient);
    String id = "id_example"; // String | The restriction rule's id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugBranchRestrictionsIdDelete(id, repoSlug, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchRestrictionsApi#repositoriesWorkspaceRepoSlugBranchRestrictionsIdDelete");
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
| **id** | **String**| The restriction rule&#39;s id | |
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
| **204** |  |  -  |
| **401** | If the request was not authenticated |  -  |
| **403** | If the authenticated user does not have admin access to the repository |  -  |
| **404** | If the repository or branch restriction id does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugBranchRestrictionsIdGet"></a>
# **repositoriesWorkspaceRepoSlugBranchRestrictionsIdGet**
> Branchrestriction repositoriesWorkspaceRepoSlugBranchRestrictionsIdGet(id, repoSlug, workspace)

Get a branch restriction rule

Returns a specific branch restriction rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchRestrictionsApi;

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

    BranchRestrictionsApi apiInstance = new BranchRestrictionsApi(defaultClient);
    String id = "id_example"; // String | The restriction rule's id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Branchrestriction result = apiInstance.repositoriesWorkspaceRepoSlugBranchRestrictionsIdGet(id, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchRestrictionsApi#repositoriesWorkspaceRepoSlugBranchRestrictionsIdGet");
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
| **id** | **String**| The restriction rule&#39;s id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Branchrestriction**](Branchrestriction.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The branch restriction rule |  -  |
| **401** | If the request was not authenticated |  -  |
| **403** | If the authenticated user does not have admin access to the repository |  -  |
| **404** | If the repository or branch restriction id does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugBranchRestrictionsIdPut"></a>
# **repositoriesWorkspaceRepoSlugBranchRestrictionsIdPut**
> Branchrestriction repositoriesWorkspaceRepoSlugBranchRestrictionsIdPut(id, repoSlug, workspace, branchrestriction)

Update a branch restriction rule

Updates an existing branch restriction rule.  Fields not present in the request body are ignored.  See [&#x60;POST&#x60;](/cloud/bitbucket/rest/api-group-branch-restrictions/#api-repositories-workspace-repo-slug-branch-restrictions-post) for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchRestrictionsApi;

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

    BranchRestrictionsApi apiInstance = new BranchRestrictionsApi(defaultClient);
    String id = "id_example"; // String | The restriction rule's id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    Branchrestriction branchrestriction = new Branchrestriction(); // Branchrestriction | The new version of the existing rule
    try {
      Branchrestriction result = apiInstance.repositoriesWorkspaceRepoSlugBranchRestrictionsIdPut(id, repoSlug, workspace, branchrestriction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchRestrictionsApi#repositoriesWorkspaceRepoSlugBranchRestrictionsIdPut");
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
| **id** | **String**| The restriction rule&#39;s id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **branchrestriction** | [**Branchrestriction**](Branchrestriction.md)| The new version of the existing rule | |

### Return type

[**Branchrestriction**](Branchrestriction.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated branch restriction rule |  -  |
| **401** | If the request was not authenticated |  -  |
| **403** | If the authenticated user does not have admin access to the repository |  -  |
| **404** | If the repository or branch restriction id does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugBranchRestrictionsPost"></a>
# **repositoriesWorkspaceRepoSlugBranchRestrictionsPost**
> Branchrestriction repositoriesWorkspaceRepoSlugBranchRestrictionsPost(repoSlug, workspace, branchrestriction)

Create a branch restriction rule

Creates a new branch restriction rule for a repository.  &#x60;kind&#x60; describes what will be restricted. Allowed values include: &#x60;push&#x60;, &#x60;force&#x60;, &#x60;delete&#x60; and &#x60;restrict_merges&#x60;.  Different kinds of branch restrictions have different requirements:  * &#x60;push&#x60; and &#x60;restrict_merges&#x60; require &#x60;users&#x60; and &#x60;groups&#x60; to be   specified. Empty lists are allowed, in which case permission is   denied for everybody.  The restriction applies to all branches that match. There are two ways to match a branch. It is configured in &#x60;branch_match_kind&#x60;:  1. &#x60;glob&#x60;: Matches a branch against the &#x60;pattern&#x60;. A &#x60;&#39;*&#39;&#x60; in    &#x60;pattern&#x60; will expand to match zero or more characters, and every    other character matches itself. For example, &#x60;&#39;foo*&#39;&#x60; will match    &#x60;&#39;foo&#39;&#x60; and &#x60;&#39;foobar&#39;&#x60;, but not &#x60;&#39;barfoo&#39;&#x60;. &#x60;&#39;*&#39;&#x60; will match all    branches. 2. &#x60;branching_model&#x60;: Matches a branch against the repository&#39;s    branching model. The &#x60;branch_type&#x60; controls the type of branch    to match. Allowed values include: &#x60;production&#x60;, &#x60;development&#x60;,    &#x60;bugfix&#x60;, &#x60;release&#x60;, &#x60;feature&#x60; and &#x60;hotfix&#x60;.  The combination of &#x60;kind&#x60; and match must be unique. This means that two &#x60;glob&#x60; restrictions in a repository cannot have the same &#x60;kind&#x60; and &#x60;pattern&#x60;. Additionally, two &#x60;branching_model&#x60; restrictions in a repository cannot have the same &#x60;kind&#x60; and &#x60;branch_type&#x60;.  &#x60;users&#x60; and &#x60;groups&#x60; are lists of users and groups that are except from the restriction. They can only be configured in &#x60;push&#x60; and &#x60;restrict_merges&#x60; restrictions. The &#x60;push&#x60; restriction stops a user pushing to matching branches unless that user is in &#x60;users&#x60; or is a member of a group in &#x60;groups&#x60;. The &#x60;restrict_merges&#x60; stops a user merging pull requests to matching branches unless that user is in &#x60;users&#x60; or is a member of a group in &#x60;groups&#x60;. Adding new users or groups to an existing restriction should be done via &#x60;PUT&#x60;.  Note that branch restrictions with overlapping matchers is allowed, but the resulting behavior may be surprising.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchRestrictionsApi;

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

    BranchRestrictionsApi apiInstance = new BranchRestrictionsApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    Branchrestriction branchrestriction = new Branchrestriction(); // Branchrestriction | The new rule
    try {
      Branchrestriction result = apiInstance.repositoriesWorkspaceRepoSlugBranchRestrictionsPost(repoSlug, workspace, branchrestriction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchRestrictionsApi#repositoriesWorkspaceRepoSlugBranchRestrictionsPost");
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
| **branchrestriction** | [**Branchrestriction**](Branchrestriction.md)| The new rule | |

### Return type

[**Branchrestriction**](Branchrestriction.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A paginated list of branch restrictions |  -  |
| **401** | If the request was not authenticated |  -  |
| **403** | If the authenticated user does not have admin access to the repository |  -  |
| **404** | If the repository does not exist |  -  |

