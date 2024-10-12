# BranchingModelApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**repositoriesWorkspaceRepoSlugBranchingModelGet**](BranchingModelApi.md#repositoriesWorkspaceRepoSlugBranchingModelGet) | **GET** /repositories/{workspace}/{repo_slug}/branching-model | Get the branching model for a repository |
| [**repositoriesWorkspaceRepoSlugBranchingModelSettingsGet**](BranchingModelApi.md#repositoriesWorkspaceRepoSlugBranchingModelSettingsGet) | **GET** /repositories/{workspace}/{repo_slug}/branching-model/settings | Get the branching model config for a repository |
| [**repositoriesWorkspaceRepoSlugBranchingModelSettingsPut**](BranchingModelApi.md#repositoriesWorkspaceRepoSlugBranchingModelSettingsPut) | **PUT** /repositories/{workspace}/{repo_slug}/branching-model/settings | Update the branching model config for a repository |
| [**repositoriesWorkspaceRepoSlugEffectiveBranchingModelGet**](BranchingModelApi.md#repositoriesWorkspaceRepoSlugEffectiveBranchingModelGet) | **GET** /repositories/{workspace}/{repo_slug}/effective-branching-model | Get the effective, or currently applied, branching model for a repository |
| [**workspacesWorkspaceProjectsProjectKeyBranchingModelGet**](BranchingModelApi.md#workspacesWorkspaceProjectsProjectKeyBranchingModelGet) | **GET** /workspaces/{workspace}/projects/{project_key}/branching-model | Get the branching model for a project |
| [**workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsGet**](BranchingModelApi.md#workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsGet) | **GET** /workspaces/{workspace}/projects/{project_key}/branching-model/settings | Get the branching model config for a project |
| [**workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsPut**](BranchingModelApi.md#workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsPut) | **PUT** /workspaces/{workspace}/projects/{project_key}/branching-model/settings | Update the branching model config for a project |


<a id="repositoriesWorkspaceRepoSlugBranchingModelGet"></a>
# **repositoriesWorkspaceRepoSlugBranchingModelGet**
> BranchingModel repositoriesWorkspaceRepoSlugBranchingModelGet(repoSlug, workspace)

Get the branching model for a repository

Return the branching model as applied to the repository. This view is read-only. The branching model settings can be changed using the [settings](#api-repositories-workspace-repo-slug-branching-model-settings-get) API.  The returned object:  1. Always has a &#x60;development&#x60; property. &#x60;development.branch&#x60; contains    the actual repository branch object that is considered to be the    &#x60;development&#x60; branch. &#x60;development.branch&#x60; will not be present    if it does not exist. 2. Might have a &#x60;production&#x60; property. &#x60;production&#x60; will not    be present when &#x60;production&#x60; is disabled.    &#x60;production.branch&#x60; contains the actual branch object that is    considered to be the &#x60;production&#x60; branch. &#x60;production.branch&#x60; will    not be present if it does not exist. 3. Always has a &#x60;branch_types&#x60; array which contains all enabled branch    types.  Example body:  &#x60;&#x60;&#x60; {   \&quot;development\&quot;: {     \&quot;name\&quot;: \&quot;master\&quot;,     \&quot;branch\&quot;: {       \&quot;type\&quot;: \&quot;branch\&quot;,       \&quot;name\&quot;: \&quot;master\&quot;,       \&quot;target\&quot;: {         \&quot;hash\&quot;: \&quot;16dffcb0de1b22e249db6799532074cf32efe80f\&quot;       }     },     \&quot;use_mainbranch\&quot;: true   },   \&quot;production\&quot;: {     \&quot;name\&quot;: \&quot;production\&quot;,     \&quot;branch\&quot;: {       \&quot;type\&quot;: \&quot;branch\&quot;,       \&quot;name\&quot;: \&quot;production\&quot;,       \&quot;target\&quot;: {         \&quot;hash\&quot;: \&quot;16dffcb0de1b22e249db6799532074cf32efe80f\&quot;       }     },     \&quot;use_mainbranch\&quot;: false   },   \&quot;branch_types\&quot;: [     {       \&quot;kind\&quot;: \&quot;release\&quot;,       \&quot;prefix\&quot;: \&quot;release/\&quot;     },     {       \&quot;kind\&quot;: \&quot;hotfix\&quot;,       \&quot;prefix\&quot;: \&quot;hotfix/\&quot;     },     {       \&quot;kind\&quot;: \&quot;feature\&quot;,       \&quot;prefix\&quot;: \&quot;feature/\&quot;     },     {       \&quot;kind\&quot;: \&quot;bugfix\&quot;,       \&quot;prefix\&quot;: \&quot;bugfix/\&quot;     }   ],   \&quot;type\&quot;: \&quot;branching_model\&quot;,   \&quot;links\&quot;: {     \&quot;self\&quot;: {       \&quot;href\&quot;: \&quot;https://api.bitbucket.org/.../branching-model\&quot;     }   } } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchingModelApi;

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

    BranchingModelApi apiInstance = new BranchingModelApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      BranchingModel result = apiInstance.repositoriesWorkspaceRepoSlugBranchingModelGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchingModelApi#repositoriesWorkspaceRepoSlugBranchingModelGet");
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

[**BranchingModel**](BranchingModel.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The branching model object |  -  |
| **401** | If the request was not authenticated |  -  |
| **403** | If the authenticated user does not have read access to the repository |  -  |
| **404** | If the repository does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugBranchingModelSettingsGet"></a>
# **repositoriesWorkspaceRepoSlugBranchingModelSettingsGet**
> BranchingModelSettings repositoriesWorkspaceRepoSlugBranchingModelSettingsGet(repoSlug, workspace)

Get the branching model config for a repository

Return the branching model configuration for a repository. The returned object:  1. Always has a &#x60;development&#x60; property for the development branch. 2. Always a &#x60;production&#x60; property for the production branch. The    production branch can be disabled. 3. The &#x60;branch_types&#x60; contains all the branch types.  This is the raw configuration for the branching model. A client wishing to see the branching model with its actual current branches may find the [active model API](/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-workspace-repo-slug-branching-model-get) more useful.  Example body:  &#x60;&#x60;&#x60; {   \&quot;development\&quot;: {     \&quot;is_valid\&quot;: true,     \&quot;name\&quot;: null,     \&quot;use_mainbranch\&quot;: true   },   \&quot;production\&quot;: {     \&quot;is_valid\&quot;: true,     \&quot;name\&quot;: \&quot;production\&quot;,     \&quot;use_mainbranch\&quot;: false,     \&quot;enabled\&quot;: false   },   \&quot;branch_types\&quot;: [     {       \&quot;kind\&quot;: \&quot;release\&quot;,       \&quot;enabled\&quot;: true,       \&quot;prefix\&quot;: \&quot;release/\&quot;     },     {       \&quot;kind\&quot;: \&quot;hotfix\&quot;,       \&quot;enabled\&quot;: true,       \&quot;prefix\&quot;: \&quot;hotfix/\&quot;     },     {       \&quot;kind\&quot;: \&quot;feature\&quot;,       \&quot;enabled\&quot;: true,       \&quot;prefix\&quot;: \&quot;feature/\&quot;     },     {       \&quot;kind\&quot;: \&quot;bugfix\&quot;,       \&quot;enabled\&quot;: false,       \&quot;prefix\&quot;: \&quot;bugfix/\&quot;     }   ],   \&quot;type\&quot;: \&quot;branching_model_settings\&quot;,   \&quot;links\&quot;: {     \&quot;self\&quot;: {       \&quot;href\&quot;: \&quot;https://api.bitbucket.org/.../branching-model/settings\&quot;     }   } } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchingModelApi;

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

    BranchingModelApi apiInstance = new BranchingModelApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      BranchingModelSettings result = apiInstance.repositoriesWorkspaceRepoSlugBranchingModelSettingsGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchingModelApi#repositoriesWorkspaceRepoSlugBranchingModelSettingsGet");
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

[**BranchingModelSettings**](BranchingModelSettings.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The branching model configuration |  -  |
| **401** | If the request was not authenticated |  -  |
| **403** | If the authenticated user does not have admin access to the repository |  -  |
| **404** | If the repository does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugBranchingModelSettingsPut"></a>
# **repositoriesWorkspaceRepoSlugBranchingModelSettingsPut**
> BranchingModelSettings repositoriesWorkspaceRepoSlugBranchingModelSettingsPut(repoSlug, workspace)

Update the branching model config for a repository

Update the branching model configuration for a repository.  The &#x60;development&#x60; branch can be configured to a specific branch or to track the main branch. When set to a specific branch it must currently exist. Only the passed properties will be updated. The properties not passed will be left unchanged. A request without a &#x60;development&#x60; property will leave the development branch unchanged.  It is possible for the &#x60;development&#x60; branch to be invalid. This happens when it points at a specific branch that has been deleted. This is indicated in the &#x60;is_valid&#x60; field for the branch. It is not possible to update the settings for &#x60;development&#x60; if that would leave the branch in an invalid state. Such a request will be rejected.  The &#x60;production&#x60; branch can be a specific branch, the main branch or disabled. When set to a specific branch it must currently exist. The &#x60;enabled&#x60; property can be used to enable (&#x60;true&#x60;) or disable (&#x60;false&#x60;) it. Only the passed properties will be updated. The properties not passed will be left unchanged. A request without a &#x60;production&#x60; property will leave the production branch unchanged.  It is possible for the &#x60;production&#x60; branch to be invalid. This happens when it points at a specific branch that has been deleted. This is indicated in the &#x60;is_valid&#x60; field for the branch. A request that would leave &#x60;production&#x60; enabled and invalid will be rejected. It is possible to update &#x60;production&#x60; and make it invalid if it would also be left disabled.  The &#x60;branch_types&#x60; property contains the branch types to be updated. Only the branch types passed will be updated. All updates will be rejected if it would leave the branching model in an invalid state. For branch types this means that:  1. The prefixes for all enabled branch types are valid. For example,    it is not possible to use &#39;*&#39; inside a Git prefix. 2. A prefix of an enabled branch type must not be a prefix of another    enabled branch type. This is to ensure that a branch can be easily    classified by its prefix unambiguously.  It is possible to store an invalid prefix if that branch type would be left disabled. Only the passed properties will be updated. The properties not passed will be left unchanged. Each branch type must have a &#x60;kind&#x60; property to identify it.  Example Body:  &#x60;&#x60;&#x60;     {       \&quot;development\&quot;: {         \&quot;use_mainbranch\&quot;: true       },       \&quot;production\&quot;: {         \&quot;enabled\&quot;: true,         \&quot;use_mainbranch\&quot;: false,         \&quot;name\&quot;: \&quot;production\&quot;       },       \&quot;branch_types\&quot;: [         {           \&quot;kind\&quot;: \&quot;bugfix\&quot;,           \&quot;enabled\&quot;: true,           \&quot;prefix\&quot;: \&quot;bugfix/\&quot;         },         {           \&quot;kind\&quot;: \&quot;feature\&quot;,           \&quot;enabled\&quot;: true,           \&quot;prefix\&quot;: \&quot;feature/\&quot;         },         {           \&quot;kind\&quot;: \&quot;hotfix\&quot;,           \&quot;prefix\&quot;: \&quot;hotfix/\&quot;         },         {           \&quot;kind\&quot;: \&quot;release\&quot;,           \&quot;enabled\&quot;: false,         }       ]     } &#x60;&#x60;&#x60;  There is currently a side effect when using this API endpoint. If the repository is inheriting branching model settings from its project, updating the branching model for this repository will disable the project setting inheritance.   We have deprecated this side effect and will remove it on 1 August 2022.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchingModelApi;

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

    BranchingModelApi apiInstance = new BranchingModelApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      BranchingModelSettings result = apiInstance.repositoriesWorkspaceRepoSlugBranchingModelSettingsPut(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchingModelApi#repositoriesWorkspaceRepoSlugBranchingModelSettingsPut");
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

[**BranchingModelSettings**](BranchingModelSettings.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated branching model configuration |  -  |
| **400** | If the request contains invalid branching model configuration |  -  |
| **401** | If the request was not authenticated |  -  |
| **403** | If the authenticated user does not have admin access to the repository |  -  |
| **404** | If the repository does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugEffectiveBranchingModelGet"></a>
# **repositoriesWorkspaceRepoSlugEffectiveBranchingModelGet**
> EffectiveRepoBranchingModel repositoriesWorkspaceRepoSlugEffectiveBranchingModelGet(repoSlug, workspace)

Get the effective, or currently applied, branching model for a repository



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchingModelApi;

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

    BranchingModelApi apiInstance = new BranchingModelApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      EffectiveRepoBranchingModel result = apiInstance.repositoriesWorkspaceRepoSlugEffectiveBranchingModelGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchingModelApi#repositoriesWorkspaceRepoSlugEffectiveBranchingModelGet");
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

[**EffectiveRepoBranchingModel**](EffectiveRepoBranchingModel.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The effective branching model object |  -  |
| **401** | If the request was not authenticated |  -  |
| **403** | If the authenticated user does not have read access to the repository |  -  |
| **404** | If the repository does not exist |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyBranchingModelGet"></a>
# **workspacesWorkspaceProjectsProjectKeyBranchingModelGet**
> ProjectBranchingModel workspacesWorkspaceProjectsProjectKeyBranchingModelGet(projectKey, workspace)

Get the branching model for a project

Return the branching model set at the project level. This view is read-only. The branching model settings can be changed using the [settings](#api-workspaces-workspace-projects-project-key-branching-model-settings-get) API.  The returned object:  1. Always has a &#x60;development&#x60; property. &#x60;development.name&#x60; is    the user-specified branch that can be inherited by an individual repository&#39;s    branching model. 2. Might have a &#x60;production&#x60; property. &#x60;production&#x60; will not    be present when &#x60;production&#x60; is disabled.    &#x60;production.name&#x60; is the user-specified branch that can be    inherited by an individual repository&#39;s branching model. 3. Always has a &#x60;branch_types&#x60; array which contains all enabled branch    types.  Example body:  &#x60;&#x60;&#x60; {   \&quot;development\&quot;: {     \&quot;name\&quot;: \&quot;master\&quot;,     \&quot;use_mainbranch\&quot;: true   },   \&quot;production\&quot;: {     \&quot;name\&quot;: \&quot;production\&quot;,     \&quot;use_mainbranch\&quot;: false   },   \&quot;branch_types\&quot;: [     {       \&quot;kind\&quot;: \&quot;release\&quot;,       \&quot;prefix\&quot;: \&quot;release/\&quot;     },     {       \&quot;kind\&quot;: \&quot;hotfix\&quot;,       \&quot;prefix\&quot;: \&quot;hotfix/\&quot;     },     {       \&quot;kind\&quot;: \&quot;feature\&quot;,       \&quot;prefix\&quot;: \&quot;feature/\&quot;     },     {       \&quot;kind\&quot;: \&quot;bugfix\&quot;,       \&quot;prefix\&quot;: \&quot;bugfix/\&quot;     }   ],   \&quot;type\&quot;: \&quot;project_branching_model\&quot;,   \&quot;links\&quot;: {     \&quot;self\&quot;: {       \&quot;href\&quot;: \&quot;https://api.bitbucket.org/.../branching-model\&quot;     }   } } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchingModelApi;

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

    BranchingModelApi apiInstance = new BranchingModelApi(defaultClient);
    String projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      ProjectBranchingModel result = apiInstance.workspacesWorkspaceProjectsProjectKeyBranchingModelGet(projectKey, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchingModelApi#workspacesWorkspaceProjectsProjectKeyBranchingModelGet");
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

[**ProjectBranchingModel**](ProjectBranchingModel.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The branching model object |  -  |
| **401** | If the request was not authenticated |  -  |
| **403** | If the authenticated user does not have read access to the project |  -  |
| **404** | If the project does not exist |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsGet"></a>
# **workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsGet**
> BranchingModelSettings workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsGet(projectKey, workspace)

Get the branching model config for a project

Return the branching model configuration for a project. The returned object:  1. Always has a &#x60;development&#x60; property for the development branch. 2. Always a &#x60;production&#x60; property for the production branch. The    production branch can be disabled. 3. The &#x60;branch_types&#x60; contains all the branch types.   This is the raw configuration for the branching model. A client wishing to see the branching model with its actual current branches may find the [active model API](#api-workspaces-workspace-projects-project-key-branching-model-get) more useful.  Example body:  &#x60;&#x60;&#x60; {   \&quot;development\&quot;: {     \&quot;name\&quot;: null,     \&quot;use_mainbranch\&quot;: true   },   \&quot;production\&quot;: {     \&quot;name\&quot;: \&quot;production\&quot;,     \&quot;use_mainbranch\&quot;: false,     \&quot;enabled\&quot;: false   },   \&quot;branch_types\&quot;: [     {       \&quot;kind\&quot;: \&quot;release\&quot;,       \&quot;enabled\&quot;: true,       \&quot;prefix\&quot;: \&quot;release/\&quot;     },     {       \&quot;kind\&quot;: \&quot;hotfix\&quot;,       \&quot;enabled\&quot;: true,       \&quot;prefix\&quot;: \&quot;hotfix/\&quot;     },     {       \&quot;kind\&quot;: \&quot;feature\&quot;,       \&quot;enabled\&quot;: true,       \&quot;prefix\&quot;: \&quot;feature/\&quot;     },     {       \&quot;kind\&quot;: \&quot;bugfix\&quot;,       \&quot;enabled\&quot;: false,       \&quot;prefix\&quot;: \&quot;bugfix/\&quot;     }   ],   \&quot;type\&quot;: \&quot;branching_model_settings\&quot;,   \&quot;links\&quot;: {     \&quot;self\&quot;: {       \&quot;href\&quot;: \&quot;https://api.bitbucket.org/.../branching-model/settings\&quot;     }   } } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchingModelApi;

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

    BranchingModelApi apiInstance = new BranchingModelApi(defaultClient);
    String projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      BranchingModelSettings result = apiInstance.workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsGet(projectKey, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchingModelApi#workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsGet");
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

[**BranchingModelSettings**](BranchingModelSettings.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The branching model configuration |  -  |
| **401** | If the request was not authenticated |  -  |
| **403** | If the authenticated user does not have admin access to the project |  -  |
| **404** | If the project does not exist |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsPut"></a>
# **workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsPut**
> BranchingModelSettings workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsPut(projectKey, workspace)

Update the branching model config for a project

Update the branching model configuration for a project.  The &#x60;development&#x60; branch can be configured to a specific branch or to track the main branch. Any branch name can be supplied, but will only successfully be applied to a repository via inheritance if that branch exists for that repository. Only the passed properties will be updated. The properties not passed will be left unchanged. A request without a &#x60;development&#x60; property will leave the development branch unchanged.  The &#x60;production&#x60; branch can be a specific branch, the main branch or disabled. Any branch name can be supplied, but will only successfully be applied to a repository via inheritance if that branch exists for that repository. The &#x60;enabled&#x60; property can be used to enable (&#x60;true&#x60;) or disable (&#x60;false&#x60;) it. Only the passed properties will be updated. The properties not passed will be left unchanged. A request without a &#x60;production&#x60; property will leave the production branch unchanged.  The &#x60;branch_types&#x60; property contains the branch types to be updated. Only the branch types passed will be updated. All updates will be rejected if it would leave the branching model in an invalid state. For branch types this means that:  1. The prefixes for all enabled branch types are valid. For example,    it is not possible to use &#39;*&#39; inside a Git prefix. 2. A prefix of an enabled branch type must not be a prefix of another    enabled branch type. This is to ensure that a branch can be easily    classified by its prefix unambiguously.  It is possible to store an invalid prefix if that branch type would be left disabled. Only the passed properties will be updated. The properties not passed will be left unchanged. Each branch type must have a &#x60;kind&#x60; property to identify it.  Example Body:  &#x60;&#x60;&#x60;     {       \&quot;development\&quot;: {         \&quot;use_mainbranch\&quot;: true       },       \&quot;production\&quot;: {         \&quot;enabled\&quot;: true,         \&quot;use_mainbranch\&quot;: false,         \&quot;name\&quot;: \&quot;production\&quot;       },       \&quot;branch_types\&quot;: [         {           \&quot;kind\&quot;: \&quot;bugfix\&quot;,           \&quot;enabled\&quot;: true,           \&quot;prefix\&quot;: \&quot;bugfix/\&quot;         },         {           \&quot;kind\&quot;: \&quot;feature\&quot;,           \&quot;enabled\&quot;: true,           \&quot;prefix\&quot;: \&quot;feature/\&quot;         },         {           \&quot;kind\&quot;: \&quot;hotfix\&quot;,           \&quot;prefix\&quot;: \&quot;hotfix/\&quot;         },         {           \&quot;kind\&quot;: \&quot;release\&quot;,           \&quot;enabled\&quot;: false,         }       ]     } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchingModelApi;

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

    BranchingModelApi apiInstance = new BranchingModelApi(defaultClient);
    String projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      BranchingModelSettings result = apiInstance.workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsPut(projectKey, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchingModelApi#workspacesWorkspaceProjectsProjectKeyBranchingModelSettingsPut");
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

[**BranchingModelSettings**](BranchingModelSettings.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated branching model configuration |  -  |
| **400** | If the request contains an invalid branching model configuration |  -  |
| **401** | If the request was not authenticated |  -  |
| **403** | If the authenticated user does not have admin access to the project |  -  |
| **404** | If the project does not exist |  -  |

