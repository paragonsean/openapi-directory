# DeploymentsApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEnvironment**](DeploymentsApi.md#createEnvironment) | **POST** /repositories/{workspace}/{repo_slug}/environments | Create an environment |
| [**deleteEnvironmentForRepository**](DeploymentsApi.md#deleteEnvironmentForRepository) | **DELETE** /repositories/{workspace}/{repo_slug}/environments/{environment_uuid} | Delete an environment |
| [**getDeploymentForRepository**](DeploymentsApi.md#getDeploymentForRepository) | **GET** /repositories/{workspace}/{repo_slug}/deployments/{deployment_uuid} | Get a deployment |
| [**getDeploymentsForRepository**](DeploymentsApi.md#getDeploymentsForRepository) | **GET** /repositories/{workspace}/{repo_slug}/deployments | List deployments |
| [**getEnvironmentForRepository**](DeploymentsApi.md#getEnvironmentForRepository) | **GET** /repositories/{workspace}/{repo_slug}/environments/{environment_uuid} | Get an environment |
| [**getEnvironmentsForRepository**](DeploymentsApi.md#getEnvironmentsForRepository) | **GET** /repositories/{workspace}/{repo_slug}/environments | List environments |
| [**repositoriesWorkspaceRepoSlugDeployKeysGet**](DeploymentsApi.md#repositoriesWorkspaceRepoSlugDeployKeysGet) | **GET** /repositories/{workspace}/{repo_slug}/deploy-keys | List repository deploy keys |
| [**repositoriesWorkspaceRepoSlugDeployKeysKeyIdDelete**](DeploymentsApi.md#repositoriesWorkspaceRepoSlugDeployKeysKeyIdDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id} | Delete a repository deploy key |
| [**repositoriesWorkspaceRepoSlugDeployKeysKeyIdGet**](DeploymentsApi.md#repositoriesWorkspaceRepoSlugDeployKeysKeyIdGet) | **GET** /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id} | Get a repository deploy key |
| [**repositoriesWorkspaceRepoSlugDeployKeysKeyIdPut**](DeploymentsApi.md#repositoriesWorkspaceRepoSlugDeployKeysKeyIdPut) | **PUT** /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id} | Update a repository deploy key |
| [**repositoriesWorkspaceRepoSlugDeployKeysPost**](DeploymentsApi.md#repositoriesWorkspaceRepoSlugDeployKeysPost) | **POST** /repositories/{workspace}/{repo_slug}/deploy-keys | Add a repository deploy key |
| [**updateEnvironmentForRepository**](DeploymentsApi.md#updateEnvironmentForRepository) | **POST** /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes | Update an environment |
| [**workspacesWorkspaceProjectsProjectKeyDeployKeysGet**](DeploymentsApi.md#workspacesWorkspaceProjectsProjectKeyDeployKeysGet) | **GET** /workspaces/{workspace}/projects/{project_key}/deploy-keys | List project deploy keys |
| [**workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdDelete**](DeploymentsApi.md#workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdDelete) | **DELETE** /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id} | Delete a deploy key from a project |
| [**workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdGet**](DeploymentsApi.md#workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdGet) | **GET** /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id} | Get a project deploy key |
| [**workspacesWorkspaceProjectsProjectKeyDeployKeysPost**](DeploymentsApi.md#workspacesWorkspaceProjectsProjectKeyDeployKeysPost) | **POST** /workspaces/{workspace}/projects/{project_key}/deploy-keys | Create a project deploy key |


<a id="createEnvironment"></a>
# **createEnvironment**
> DeploymentEnvironment createEnvironment(workspace, repoSlug, deploymentEnvironment)

Create an environment

Create an environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    DeploymentEnvironment deploymentEnvironment = new DeploymentEnvironment(); // DeploymentEnvironment | The environment to create.
    try {
      DeploymentEnvironment result = apiInstance.createEnvironment(workspace, repoSlug, deploymentEnvironment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#createEnvironment");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **deploymentEnvironment** | [**DeploymentEnvironment**](DeploymentEnvironment.md)| The environment to create. | |

### Return type

[**DeploymentEnvironment**](DeploymentEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The environment was created. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **404** | The account or repository does not exist. |  -  |
| **409** | An environment host with the provided name already exists. |  -  |

<a id="deleteEnvironmentForRepository"></a>
# **deleteEnvironmentForRepository**
> deleteEnvironmentForRepository(workspace, repoSlug, environmentUuid)

Delete an environment

Delete an environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String environmentUuid = "environmentUuid_example"; // String | The environment UUID.
    try {
      apiInstance.deleteEnvironmentForRepository(workspace, repoSlug, environmentUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deleteEnvironmentForRepository");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **environmentUuid** | **String**| The environment UUID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The environment was deleted. |  -  |
| **404** | No account or repository with the UUID provided exists. |  -  |

<a id="getDeploymentForRepository"></a>
# **getDeploymentForRepository**
> Deployment getDeploymentForRepository(workspace, repoSlug, deploymentUuid)

Get a deployment

Retrieve a deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String deploymentUuid = "deploymentUuid_example"; // String | The deployment UUID.
    try {
      Deployment result = apiInstance.getDeploymentForRepository(workspace, repoSlug, deploymentUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#getDeploymentForRepository");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **deploymentUuid** | **String**| The deployment UUID. | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deployment. |  -  |
| **404** | No account, repository or deployment with the UUID provided exists. |  -  |

<a id="getDeploymentsForRepository"></a>
# **getDeploymentsForRepository**
> PaginatedDeployments getDeploymentsForRepository(workspace, repoSlug)

List deployments

Find deployments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    try {
      PaginatedDeployments result = apiInstance.getDeploymentsForRepository(workspace, repoSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#getDeploymentsForRepository");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |

### Return type

[**PaginatedDeployments**](PaginatedDeployments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The matching deployments. |  -  |

<a id="getEnvironmentForRepository"></a>
# **getEnvironmentForRepository**
> DeploymentEnvironment getEnvironmentForRepository(workspace, repoSlug, environmentUuid)

Get an environment

Retrieve an environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String environmentUuid = "environmentUuid_example"; // String | The environment UUID.
    try {
      DeploymentEnvironment result = apiInstance.getEnvironmentForRepository(workspace, repoSlug, environmentUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#getEnvironmentForRepository");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **environmentUuid** | **String**| The environment UUID. | |

### Return type

[**DeploymentEnvironment**](DeploymentEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The environment. |  -  |
| **404** | No account, repository or environment with the UUID provided exists. |  -  |

<a id="getEnvironmentsForRepository"></a>
# **getEnvironmentsForRepository**
> PaginatedEnvironments getEnvironmentsForRepository(workspace, repoSlug)

List environments

Find environments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    try {
      PaginatedEnvironments result = apiInstance.getEnvironmentsForRepository(workspace, repoSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#getEnvironmentsForRepository");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |

### Return type

[**PaginatedEnvironments**](PaginatedEnvironments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The matching environments. |  -  |

<a id="repositoriesWorkspaceRepoSlugDeployKeysGet"></a>
# **repositoriesWorkspaceRepoSlugDeployKeysGet**
> PaginatedDeployKeys repositoriesWorkspaceRepoSlugDeployKeysGet(repoSlug, workspace)

List repository deploy keys

Returns all deploy-keys belonging to a repository.  Example: &#x60;&#x60;&#x60; $ curl -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys  Output: {     \&quot;pagelen\&quot;: 10,     \&quot;values\&quot;: [         {             \&quot;id\&quot;: 123,             \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\&quot;,             \&quot;label\&quot;: \&quot;mykey\&quot;,             \&quot;type\&quot;: \&quot;deploy_key\&quot;,             \&quot;created_on\&quot;: \&quot;2018-08-15T23:50:59.993890+00:00\&quot;,             \&quot;repository\&quot;: {                 \&quot;full_name\&quot;: \&quot;mleu/test\&quot;,                 \&quot;name\&quot;: \&quot;test\&quot;,                 \&quot;type\&quot;: \&quot;repository\&quot;,                 \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;             },             \&quot;links\&quot;:{                 \&quot;self\&quot;:{                     \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/123\&quot;                 }             }             \&quot;last_used\&quot;: null,             \&quot;comment\&quot;: \&quot;mleu@C02W454JHTD8\&quot;         }     ],     \&quot;page\&quot;: 1,     \&quot;size\&quot;: 1 } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

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

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedDeployKeys result = apiInstance.repositoriesWorkspaceRepoSlugDeployKeysGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#repositoriesWorkspaceRepoSlugDeployKeysGet");
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

[**PaginatedDeployKeys**](PaginatedDeployKeys.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deploy keys matching the repository |  -  |
| **403** | If the specified user or repository is not accessible to the current user |  -  |
| **404** | If the specified user or repository does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugDeployKeysKeyIdDelete"></a>
# **repositoriesWorkspaceRepoSlugDeployKeysKeyIdDelete**
> repositoriesWorkspaceRepoSlugDeployKeysKeyIdDelete(keyId, repoSlug, workspace)

Delete a repository deploy key

This deletes a deploy key from a repository.  Example: &#x60;&#x60;&#x60; $ curl -XDELETE \\ -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/1234 &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

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

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String keyId = "keyId_example"; // String | The key ID matching the deploy key.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugDeployKeysKeyIdDelete(keyId, repoSlug, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#repositoriesWorkspaceRepoSlugDeployKeysKeyIdDelete");
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
| **keyId** | **String**| The key ID matching the deploy key. | |
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
| **204** | The key has been deleted |  -  |
| **403** | If the current user does not have permission to delete a key for the specified user |  -  |
| **404** | If the specified user, repository, or deploy key does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugDeployKeysKeyIdGet"></a>
# **repositoriesWorkspaceRepoSlugDeployKeysKeyIdGet**
> DeployKey repositoriesWorkspaceRepoSlugDeployKeysKeyIdGet(keyId, repoSlug, workspace)

Get a repository deploy key

Returns the deploy key belonging to a specific key.  Example: &#x60;&#x60;&#x60; $ curl -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-key/1234  Output: {     \&quot;comment\&quot;: \&quot;mleu@C02W454JHTD8\&quot;,     \&quot;last_used\&quot;: null,     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-key/1234\&quot;         }     },     \&quot;repository\&quot;: {         \&quot;full_name\&quot;: \&quot;mleu/test\&quot;,         \&quot;name\&quot;: \&quot;test\&quot;,         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;     },     \&quot;label\&quot;: \&quot;mykey\&quot;,     \&quot;created_on\&quot;: \&quot;2018-08-15T23:50:59.993890+00:00\&quot;,     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\&quot;,     \&quot;id\&quot;: 1234,     \&quot;type\&quot;: \&quot;deploy_key\&quot; } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

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

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String keyId = "keyId_example"; // String | The key ID matching the deploy key.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      DeployKey result = apiInstance.repositoriesWorkspaceRepoSlugDeployKeysKeyIdGet(keyId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#repositoriesWorkspaceRepoSlugDeployKeysKeyIdGet");
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
| **keyId** | **String**| The key ID matching the deploy key. | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deploy key matching the key ID |  -  |
| **403** | If the specified user or repository is not accessible to the current user |  -  |
| **404** | If the specified user or repository does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugDeployKeysKeyIdPut"></a>
# **repositoriesWorkspaceRepoSlugDeployKeysKeyIdPut**
> DeployKey repositoriesWorkspaceRepoSlugDeployKeysKeyIdPut(keyId, repoSlug, workspace)

Update a repository deploy key

Create a new deploy key in a repository.  The same key needs to be passed in but the comment and label can change.  Example: &#x60;&#x60;&#x60; $ curl -XPUT \\ -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ -H \&quot;Content-type: application/json\&quot; \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/1234 -d \\ &#39;{     \&quot;label\&quot;: \&quot;newlabel\&quot;,     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5 newcomment\&quot;, }&#39;  Output: {     \&quot;comment\&quot;: \&quot;newcomment\&quot;,     \&quot;last_used\&quot;: null,     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/1234\&quot;         }     },     \&quot;repository\&quot;: {         \&quot;full_name\&quot;: \&quot;mleu/test\&quot;,         \&quot;name\&quot;: \&quot;test\&quot;,         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;     },     \&quot;label\&quot;: \&quot;newlabel\&quot;,     \&quot;created_on\&quot;: \&quot;2018-08-15T23:50:59.993890+00:00\&quot;,     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\&quot;,     \&quot;id\&quot;: 1234,     \&quot;type\&quot;: \&quot;deploy_key\&quot; } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

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

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String keyId = "keyId_example"; // String | The key ID matching the deploy key.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      DeployKey result = apiInstance.repositoriesWorkspaceRepoSlugDeployKeysKeyIdPut(keyId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#repositoriesWorkspaceRepoSlugDeployKeysKeyIdPut");
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
| **keyId** | **String**| The key ID matching the deploy key. | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The newly updated deploy key. |  -  |
| **400** | If the submitted key or related value is invalid |  -  |
| **403** | If the current user does not have permission to add a key for the specified user |  -  |
| **404** | If the specified user, repository, or deploy key does not exist |  -  |

<a id="repositoriesWorkspaceRepoSlugDeployKeysPost"></a>
# **repositoriesWorkspaceRepoSlugDeployKeysPost**
> DeployKey repositoriesWorkspaceRepoSlugDeployKeysPost(repoSlug, workspace)

Add a repository deploy key

Create a new deploy key in a repository. Note: If authenticating a deploy key with an OAuth consumer, any changes to the OAuth consumer will subsequently invalidate the deploy key.   Example: &#x60;&#x60;&#x60; $ curl -XPOST \\ -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ -H \&quot;Content-type: application/json\&quot; \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys -d \\ &#39;{     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5 mleu@C02W454JHTD8\&quot;,     \&quot;label\&quot;: \&quot;mydeploykey\&quot; }&#39;  Output: {     \&quot;id\&quot;: 123,     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\&quot;,     \&quot;label\&quot;: \&quot;mydeploykey\&quot;,     \&quot;type\&quot;: \&quot;deploy_key\&quot;,     \&quot;created_on\&quot;: \&quot;2018-08-15T23:50:59.993890+00:00\&quot;,     \&quot;repository\&quot;: {         \&quot;full_name\&quot;: \&quot;mleu/test\&quot;,         \&quot;name\&quot;: \&quot;test\&quot;,         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;     },     \&quot;links\&quot;:{         \&quot;self\&quot;:{             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/123\&quot;         }     }     \&quot;last_used\&quot;: null,     \&quot;comment\&quot;: \&quot;mleu@C02W454JHTD8\&quot; } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

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

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      DeployKey result = apiInstance.repositoriesWorkspaceRepoSlugDeployKeysPost(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#repositoriesWorkspaceRepoSlugDeployKeysPost");
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

[**DeployKey**](DeployKey.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deploy key that was created |  -  |
| **400** | Invalid deploy key inputs |  -  |
| **403** | If the specified user or repository is not accessible to the current user |  -  |
| **404** | If the specified user or repository does not exist |  -  |

<a id="updateEnvironmentForRepository"></a>
# **updateEnvironmentForRepository**
> updateEnvironmentForRepository(workspace, repoSlug, environmentUuid)

Update an environment

Update an environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String environmentUuid = "environmentUuid_example"; // String | The environment UUID.
    try {
      apiInstance.updateEnvironmentForRepository(workspace, repoSlug, environmentUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#updateEnvironmentForRepository");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **environmentUuid** | **String**| The environment UUID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The environment update request was accepted. |  -  |
| **404** | No account, repository or environment with the UUID provided exists. |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyDeployKeysGet"></a>
# **workspacesWorkspaceProjectsProjectKeyDeployKeysGet**
> PaginatedProjectDeployKeys workspacesWorkspaceProjectsProjectKeyDeployKeysGet(projectKey, workspace)

List project deploy keys

Returns all deploy keys belonging to a project.  Example: &#x60;&#x60;&#x60; $ curl -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys  Output: {     \&quot;pagelen\&quot;:10,     \&quot;values\&quot;:[         {             \&quot;comment\&quot;:\&quot;thakseth@C02W454JHTD8\&quot;,             \&quot;last_used\&quot;:null,             \&quot;links\&quot;:{                 \&quot;self\&quot;:{                     \&quot;href\&quot;:\&quot;https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys/1234\&quot;                 }             },             \&quot;label\&quot;:\&quot;test\&quot;,             \&quot;project\&quot;:{                 \&quot;links\&quot;:{                     \&quot;self\&quot;:{                         \&quot;href\&quot;:\&quot;https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT\&quot;                     }                 },                 \&quot;type\&quot;:\&quot;project\&quot;,                 \&quot;name\&quot;:\&quot;cooperative standard\&quot;,                 \&quot;key\&quot;:\&quot;TEST_PROJECT\&quot;,                 \&quot;uuid\&quot;:\&quot;{3b3e510b-7f2b-414d-a2b7-76c4e405c1c0}\&quot;             },             \&quot;created_on\&quot;:\&quot;2021-07-28T21:20:19.491721+00:00\&quot;,             \&quot;key\&quot;:\&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDX5yfMOEw6HG9jKTYTisbmDTJ4MCUTSVGr5e4OWvY3UuI2A6F8SdzQqa2f5BABA/4g5Sk5awJrYHlNu3EzV1V2I44tR3A4fnZAG71ZKyDPi1wvdO7UYmFgxV/Vd18H9QZFFjICGDM7W0PT2mI0kON/jN3qNWi+GiB/xgaeQKSqynysdysDp8lnnI/8Sh3ikURP9UP83ShRCpAXszOUNaa+UUlcYQYBDLIGowsg51c4PCkC3DNhAMxppkNRKoSOWwyl+oRVXHSDylkiJSBHW3HH4Q6WHieD54kGrjbhWBKdnnxKX7QAAZBDseY+t01N36m6/ljvXSUEcBWtHxBYye0r\&quot;,             \&quot;type\&quot;:\&quot;project_deploy_key\&quot;,             \&quot;id\&quot;:1234         }     ],     \&quot;page\&quot;:1,     \&quot;size\&quot;:1 } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

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

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedProjectDeployKeys result = apiInstance.workspacesWorkspaceProjectsProjectKeyDeployKeysGet(projectKey, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#workspacesWorkspaceProjectsProjectKeyDeployKeysGet");
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

[**PaginatedProjectDeployKeys**](PaginatedProjectDeployKeys.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deploy keys matching the project |  -  |
| **403** | If the specified workspace or project is not accessible to the current user |  -  |
| **404** | If the specified workspace or project does not exist |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdDelete"></a>
# **workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdDelete**
> workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdDelete(keyId, projectKey, workspace)

Delete a deploy key from a project

This deletes a deploy key from a project.  Example: &#x60;&#x60;&#x60; $ curl -XDELETE \\ -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ https://api.bitbucket.org/2.0/workspaces/jzeng/projects/JZ/deploy-keys/1234 &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

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

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String keyId = "keyId_example"; // String | The key ID matching the project deploy key.
    String projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdDelete(keyId, projectKey, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdDelete");
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
| **keyId** | **String**| The key ID matching the project deploy key. | |
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
| **204** | The project deploy key has been deleted |  -  |
| **403** | If the current user does not have permission to delete a key for the specified project |  -  |
| **404** | If the specified workspace, project, or project deploy key does not exist |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdGet"></a>
# **workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdGet**
> ProjectDeployKey workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdGet(keyId, projectKey, workspace)

Get a project deploy key

Returns the deploy key belonging to a specific key ID.  Example: &#x60;&#x60;&#x60; $ curl -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys/1234  Output: {     \&quot;pagelen\&quot;:10,     \&quot;values\&quot;:[         {             \&quot;comment\&quot;:\&quot;thakseth@C02W454JHTD8\&quot;,             \&quot;last_used\&quot;:null,             \&quot;links\&quot;:{                 \&quot;self\&quot;:{                     \&quot;href\&quot;:\&quot;https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys/1234\&quot;                 }             },             \&quot;label\&quot;:\&quot;test\&quot;,             \&quot;project\&quot;:{                 \&quot;links\&quot;:{                     \&quot;self\&quot;:{                         \&quot;href\&quot;:\&quot;https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT\&quot;                     }                 },                 \&quot;type\&quot;:\&quot;project\&quot;,                 \&quot;name\&quot;:\&quot;cooperative standard\&quot;,                 \&quot;key\&quot;:\&quot;TEST_PROJECT\&quot;,                 \&quot;uuid\&quot;:\&quot;{3b3e510b-7f2b-414d-a2b7-76c4e405c1c0}\&quot;             },             \&quot;created_on\&quot;:\&quot;2021-07-28T21:20:19.491721+00:00\&quot;,             \&quot;key\&quot;:\&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDX5yfMOEw6HG9jKTYTisbmDTJ4MCUTSVGr5e4OWvY3UuI2A6F8SdzQqa2f5BABA/4g5Sk5awJrYHlNu3EzV1V2I44tR3A4fnZAG71ZKyDPi1wvdO7UYmFgxV/Vd18H9QZFFjICGDM7W0PT2mI0kON/jN3qNWi+GiB/xgaeQKSqynysdysDp8lnnI/8Sh3ikURP9UP83ShRCpAXszOUNaa+UUlcYQYBDLIGowsg51c4PCkC3DNhAMxppkNRKoSOWwyl+oRVXHSDylkiJSBHW3HH4Q6WHieD54kGrjbhWBKdnnxKX7QAAZBDseY+t01N36m6/ljvXSUEcBWtHxBYye0r\&quot;,             \&quot;type\&quot;:\&quot;project_deploy_key\&quot;,             \&quot;id\&quot;:1234         }     ], } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

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

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String keyId = "keyId_example"; // String | The key ID matching the project deploy key.
    String projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      ProjectDeployKey result = apiInstance.workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdGet(keyId, projectKey, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdGet");
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
| **keyId** | **String**| The key ID matching the project deploy key. | |
| **projectKey** | **String**| The project in question. This is the actual &#x60;key&#x60; assigned to the project.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**ProjectDeployKey**](ProjectDeployKey.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project deploy key matching the key ID |  -  |
| **403** | If the specified workspace or project is not accessible to the current user |  -  |
| **404** | If the specified workspace or project does not exist |  -  |

<a id="workspacesWorkspaceProjectsProjectKeyDeployKeysPost"></a>
# **workspacesWorkspaceProjectsProjectKeyDeployKeysPost**
> ProjectDeployKey workspacesWorkspaceProjectsProjectKeyDeployKeysPost(projectKey, workspace)

Create a project deploy key

Create a new deploy key in a project.  Example: &#x60;&#x60;&#x60; $ curl -XPOST \\ -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ -H \&quot;Content-type: application/json\&quot; \\ https://api.bitbucket.org/2.0/workspaces/jzeng/projects/JZ/deploy-keys/ -d \\ &#39;{     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5 mleu@C02W454JHTD8\&quot;,     \&quot;label\&quot;: \&quot;mydeploykey\&quot; }&#39;  Output: {     \&quot;comment\&quot;: \&quot;mleu@C02W454JHTD8\&quot;,     \&quot;last_used\&quot;: null,     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/workspaces/testadfsa/projects/ASDF/deploy-keys/5/\&quot;         }     },     \&quot;label\&quot;: \&quot;myprojectkey\&quot;,     \&quot;project\&quot;: {         ...     },     \&quot;created_on\&quot;: \&quot;2021-08-10T05:28:00.570859+00:00\&quot;,     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\&quot;,     \&quot;type\&quot;: \&quot;project_deploy_key\&quot;,     \&quot;id\&quot;: 5 } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

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

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      ProjectDeployKey result = apiInstance.workspacesWorkspaceProjectsProjectKeyDeployKeysPost(projectKey, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#workspacesWorkspaceProjectsProjectKeyDeployKeysPost");
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

[**ProjectDeployKey**](ProjectDeployKey.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project deploy key that was created |  -  |
| **400** | Invalid deploy key inputs |  -  |
| **403** | If the specified workspace or project is not accessible to the current user |  -  |
| **404** | If the specified workspace or project does not exist |  -  |

