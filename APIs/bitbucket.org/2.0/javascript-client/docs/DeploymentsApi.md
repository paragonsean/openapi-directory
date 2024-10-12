# BitbucketApi.DeploymentsApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEnvironment**](DeploymentsApi.md#createEnvironment) | **POST** /repositories/{workspace}/{repo_slug}/environments | Create an environment
[**deleteEnvironmentForRepository**](DeploymentsApi.md#deleteEnvironmentForRepository) | **DELETE** /repositories/{workspace}/{repo_slug}/environments/{environment_uuid} | Delete an environment
[**getDeploymentForRepository**](DeploymentsApi.md#getDeploymentForRepository) | **GET** /repositories/{workspace}/{repo_slug}/deployments/{deployment_uuid} | Get a deployment
[**getDeploymentsForRepository**](DeploymentsApi.md#getDeploymentsForRepository) | **GET** /repositories/{workspace}/{repo_slug}/deployments | List deployments
[**getEnvironmentForRepository**](DeploymentsApi.md#getEnvironmentForRepository) | **GET** /repositories/{workspace}/{repo_slug}/environments/{environment_uuid} | Get an environment
[**getEnvironmentsForRepository**](DeploymentsApi.md#getEnvironmentsForRepository) | **GET** /repositories/{workspace}/{repo_slug}/environments | List environments
[**repositoriesWorkspaceRepoSlugDeployKeysGet**](DeploymentsApi.md#repositoriesWorkspaceRepoSlugDeployKeysGet) | **GET** /repositories/{workspace}/{repo_slug}/deploy-keys | List repository deploy keys
[**repositoriesWorkspaceRepoSlugDeployKeysKeyIdDelete**](DeploymentsApi.md#repositoriesWorkspaceRepoSlugDeployKeysKeyIdDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id} | Delete a repository deploy key
[**repositoriesWorkspaceRepoSlugDeployKeysKeyIdGet**](DeploymentsApi.md#repositoriesWorkspaceRepoSlugDeployKeysKeyIdGet) | **GET** /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id} | Get a repository deploy key
[**repositoriesWorkspaceRepoSlugDeployKeysKeyIdPut**](DeploymentsApi.md#repositoriesWorkspaceRepoSlugDeployKeysKeyIdPut) | **PUT** /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id} | Update a repository deploy key
[**repositoriesWorkspaceRepoSlugDeployKeysPost**](DeploymentsApi.md#repositoriesWorkspaceRepoSlugDeployKeysPost) | **POST** /repositories/{workspace}/{repo_slug}/deploy-keys | Add a repository deploy key
[**updateEnvironmentForRepository**](DeploymentsApi.md#updateEnvironmentForRepository) | **POST** /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes | Update an environment
[**workspacesWorkspaceProjectsProjectKeyDeployKeysGet**](DeploymentsApi.md#workspacesWorkspaceProjectsProjectKeyDeployKeysGet) | **GET** /workspaces/{workspace}/projects/{project_key}/deploy-keys | List project deploy keys
[**workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdDelete**](DeploymentsApi.md#workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdDelete) | **DELETE** /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id} | Delete a deploy key from a project
[**workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdGet**](DeploymentsApi.md#workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdGet) | **GET** /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id} | Get a project deploy key
[**workspacesWorkspaceProjectsProjectKeyDeployKeysPost**](DeploymentsApi.md#workspacesWorkspaceProjectsProjectKeyDeployKeysPost) | **POST** /workspaces/{workspace}/projects/{project_key}/deploy-keys | Create a project deploy key



## createEnvironment

> DeploymentEnvironment createEnvironment(workspace, repoSlug, deploymentEnvironment)

Create an environment

Create an environment.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.DeploymentsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let deploymentEnvironment = new BitbucketApi.DeploymentEnvironment(); // DeploymentEnvironment | The environment to create.
apiInstance.createEnvironment(workspace, repoSlug, deploymentEnvironment, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **deploymentEnvironment** | [**DeploymentEnvironment**](DeploymentEnvironment.md)| The environment to create. | 

### Return type

[**DeploymentEnvironment**](DeploymentEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteEnvironmentForRepository

> deleteEnvironmentForRepository(workspace, repoSlug, environmentUuid)

Delete an environment

Delete an environment

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.DeploymentsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let environmentUuid = "environmentUuid_example"; // String | The environment UUID.
apiInstance.deleteEnvironmentForRepository(workspace, repoSlug, environmentUuid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **environmentUuid** | **String**| The environment UUID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeploymentForRepository

> Deployment getDeploymentForRepository(workspace, repoSlug, deploymentUuid)

Get a deployment

Retrieve a deployment

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.DeploymentsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let deploymentUuid = "deploymentUuid_example"; // String | The deployment UUID.
apiInstance.getDeploymentForRepository(workspace, repoSlug, deploymentUuid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **deploymentUuid** | **String**| The deployment UUID. | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeploymentsForRepository

> PaginatedDeployments getDeploymentsForRepository(workspace, repoSlug)

List deployments

Find deployments

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.DeploymentsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
apiInstance.getDeploymentsForRepository(workspace, repoSlug, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 

### Return type

[**PaginatedDeployments**](PaginatedDeployments.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEnvironmentForRepository

> DeploymentEnvironment getEnvironmentForRepository(workspace, repoSlug, environmentUuid)

Get an environment

Retrieve an environment

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.DeploymentsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let environmentUuid = "environmentUuid_example"; // String | The environment UUID.
apiInstance.getEnvironmentForRepository(workspace, repoSlug, environmentUuid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **environmentUuid** | **String**| The environment UUID. | 

### Return type

[**DeploymentEnvironment**](DeploymentEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEnvironmentsForRepository

> PaginatedEnvironments getEnvironmentsForRepository(workspace, repoSlug)

List environments

Find environments

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.DeploymentsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
apiInstance.getEnvironmentsForRepository(workspace, repoSlug, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 

### Return type

[**PaginatedEnvironments**](PaginatedEnvironments.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugDeployKeysGet

> PaginatedDeployKeys repositoriesWorkspaceRepoSlugDeployKeysGet(repoSlug, workspace)

List repository deploy keys

Returns all deploy-keys belonging to a repository.  Example: &#x60;&#x60;&#x60; $ curl -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys  Output: {     \&quot;pagelen\&quot;: 10,     \&quot;values\&quot;: [         {             \&quot;id\&quot;: 123,             \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\&quot;,             \&quot;label\&quot;: \&quot;mykey\&quot;,             \&quot;type\&quot;: \&quot;deploy_key\&quot;,             \&quot;created_on\&quot;: \&quot;2018-08-15T23:50:59.993890+00:00\&quot;,             \&quot;repository\&quot;: {                 \&quot;full_name\&quot;: \&quot;mleu/test\&quot;,                 \&quot;name\&quot;: \&quot;test\&quot;,                 \&quot;type\&quot;: \&quot;repository\&quot;,                 \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;             },             \&quot;links\&quot;:{                 \&quot;self\&quot;:{                     \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/123\&quot;                 }             }             \&quot;last_used\&quot;: null,             \&quot;comment\&quot;: \&quot;mleu@C02W454JHTD8\&quot;         }     ],     \&quot;page\&quot;: 1,     \&quot;size\&quot;: 1 } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.DeploymentsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugDeployKeysGet(repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**PaginatedDeployKeys**](PaginatedDeployKeys.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugDeployKeysKeyIdDelete

> repositoriesWorkspaceRepoSlugDeployKeysKeyIdDelete(keyId, repoSlug, workspace)

Delete a repository deploy key

This deletes a deploy key from a repository.  Example: &#x60;&#x60;&#x60; $ curl -XDELETE \\ -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/1234 &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.DeploymentsApi();
let keyId = "keyId_example"; // String | The key ID matching the deploy key.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugDeployKeysKeyIdDelete(keyId, repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyId** | **String**| The key ID matching the deploy key. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugDeployKeysKeyIdGet

> DeployKey repositoriesWorkspaceRepoSlugDeployKeysKeyIdGet(keyId, repoSlug, workspace)

Get a repository deploy key

Returns the deploy key belonging to a specific key.  Example: &#x60;&#x60;&#x60; $ curl -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-key/1234  Output: {     \&quot;comment\&quot;: \&quot;mleu@C02W454JHTD8\&quot;,     \&quot;last_used\&quot;: null,     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-key/1234\&quot;         }     },     \&quot;repository\&quot;: {         \&quot;full_name\&quot;: \&quot;mleu/test\&quot;,         \&quot;name\&quot;: \&quot;test\&quot;,         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;     },     \&quot;label\&quot;: \&quot;mykey\&quot;,     \&quot;created_on\&quot;: \&quot;2018-08-15T23:50:59.993890+00:00\&quot;,     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\&quot;,     \&quot;id\&quot;: 1234,     \&quot;type\&quot;: \&quot;deploy_key\&quot; } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.DeploymentsApi();
let keyId = "keyId_example"; // String | The key ID matching the deploy key.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugDeployKeysKeyIdGet(keyId, repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyId** | **String**| The key ID matching the deploy key. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugDeployKeysKeyIdPut

> DeployKey repositoriesWorkspaceRepoSlugDeployKeysKeyIdPut(keyId, repoSlug, workspace)

Update a repository deploy key

Create a new deploy key in a repository.  The same key needs to be passed in but the comment and label can change.  Example: &#x60;&#x60;&#x60; $ curl -XPUT \\ -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ -H \&quot;Content-type: application/json\&quot; \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/1234 -d \\ &#39;{     \&quot;label\&quot;: \&quot;newlabel\&quot;,     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5 newcomment\&quot;, }&#39;  Output: {     \&quot;comment\&quot;: \&quot;newcomment\&quot;,     \&quot;last_used\&quot;: null,     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/1234\&quot;         }     },     \&quot;repository\&quot;: {         \&quot;full_name\&quot;: \&quot;mleu/test\&quot;,         \&quot;name\&quot;: \&quot;test\&quot;,         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;     },     \&quot;label\&quot;: \&quot;newlabel\&quot;,     \&quot;created_on\&quot;: \&quot;2018-08-15T23:50:59.993890+00:00\&quot;,     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\&quot;,     \&quot;id\&quot;: 1234,     \&quot;type\&quot;: \&quot;deploy_key\&quot; } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.DeploymentsApi();
let keyId = "keyId_example"; // String | The key ID matching the deploy key.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugDeployKeysKeyIdPut(keyId, repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyId** | **String**| The key ID matching the deploy key. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugDeployKeysPost

> DeployKey repositoriesWorkspaceRepoSlugDeployKeysPost(repoSlug, workspace)

Add a repository deploy key

Create a new deploy key in a repository. Note: If authenticating a deploy key with an OAuth consumer, any changes to the OAuth consumer will subsequently invalidate the deploy key.   Example: &#x60;&#x60;&#x60; $ curl -XPOST \\ -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ -H \&quot;Content-type: application/json\&quot; \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys -d \\ &#39;{     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5 mleu@C02W454JHTD8\&quot;,     \&quot;label\&quot;: \&quot;mydeploykey\&quot; }&#39;  Output: {     \&quot;id\&quot;: 123,     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\&quot;,     \&quot;label\&quot;: \&quot;mydeploykey\&quot;,     \&quot;type\&quot;: \&quot;deploy_key\&quot;,     \&quot;created_on\&quot;: \&quot;2018-08-15T23:50:59.993890+00:00\&quot;,     \&quot;repository\&quot;: {         \&quot;full_name\&quot;: \&quot;mleu/test\&quot;,         \&quot;name\&quot;: \&quot;test\&quot;,         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;     },     \&quot;links\&quot;:{         \&quot;self\&quot;:{             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/123\&quot;         }     }     \&quot;last_used\&quot;: null,     \&quot;comment\&quot;: \&quot;mleu@C02W454JHTD8\&quot; } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.DeploymentsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugDeployKeysPost(repoSlug, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateEnvironmentForRepository

> updateEnvironmentForRepository(workspace, repoSlug, environmentUuid)

Update an environment

Update an environment

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.DeploymentsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let environmentUuid = "environmentUuid_example"; // String | The environment UUID.
apiInstance.updateEnvironmentForRepository(workspace, repoSlug, environmentUuid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **environmentUuid** | **String**| The environment UUID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesWorkspaceProjectsProjectKeyDeployKeysGet

> PaginatedProjectDeployKeys workspacesWorkspaceProjectsProjectKeyDeployKeysGet(projectKey, workspace)

List project deploy keys

Returns all deploy keys belonging to a project.  Example: &#x60;&#x60;&#x60; $ curl -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys  Output: {     \&quot;pagelen\&quot;:10,     \&quot;values\&quot;:[         {             \&quot;comment\&quot;:\&quot;thakseth@C02W454JHTD8\&quot;,             \&quot;last_used\&quot;:null,             \&quot;links\&quot;:{                 \&quot;self\&quot;:{                     \&quot;href\&quot;:\&quot;https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys/1234\&quot;                 }             },             \&quot;label\&quot;:\&quot;test\&quot;,             \&quot;project\&quot;:{                 \&quot;links\&quot;:{                     \&quot;self\&quot;:{                         \&quot;href\&quot;:\&quot;https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT\&quot;                     }                 },                 \&quot;type\&quot;:\&quot;project\&quot;,                 \&quot;name\&quot;:\&quot;cooperative standard\&quot;,                 \&quot;key\&quot;:\&quot;TEST_PROJECT\&quot;,                 \&quot;uuid\&quot;:\&quot;{3b3e510b-7f2b-414d-a2b7-76c4e405c1c0}\&quot;             },             \&quot;created_on\&quot;:\&quot;2021-07-28T21:20:19.491721+00:00\&quot;,             \&quot;key\&quot;:\&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDX5yfMOEw6HG9jKTYTisbmDTJ4MCUTSVGr5e4OWvY3UuI2A6F8SdzQqa2f5BABA/4g5Sk5awJrYHlNu3EzV1V2I44tR3A4fnZAG71ZKyDPi1wvdO7UYmFgxV/Vd18H9QZFFjICGDM7W0PT2mI0kON/jN3qNWi+GiB/xgaeQKSqynysdysDp8lnnI/8Sh3ikURP9UP83ShRCpAXszOUNaa+UUlcYQYBDLIGowsg51c4PCkC3DNhAMxppkNRKoSOWwyl+oRVXHSDylkiJSBHW3HH4Q6WHieD54kGrjbhWBKdnnxKX7QAAZBDseY+t01N36m6/ljvXSUEcBWtHxBYye0r\&quot;,             \&quot;type\&quot;:\&quot;project_deploy_key\&quot;,             \&quot;id\&quot;:1234         }     ],     \&quot;page\&quot;:1,     \&quot;size\&quot;:1 } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.DeploymentsApi();
let projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.workspacesWorkspaceProjectsProjectKeyDeployKeysGet(projectKey, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectKey** | **String**| The project in question. This is the actual &#x60;key&#x60; assigned to the project.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**PaginatedProjectDeployKeys**](PaginatedProjectDeployKeys.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdDelete

> workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdDelete(keyId, projectKey, workspace)

Delete a deploy key from a project

This deletes a deploy key from a project.  Example: &#x60;&#x60;&#x60; $ curl -XDELETE \\ -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ https://api.bitbucket.org/2.0/workspaces/jzeng/projects/JZ/deploy-keys/1234 &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.DeploymentsApi();
let keyId = "keyId_example"; // String | The key ID matching the project deploy key.
let projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdDelete(keyId, projectKey, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyId** | **String**| The key ID matching the project deploy key. | 
 **projectKey** | **String**| The project in question. This is the actual &#x60;key&#x60; assigned to the project.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdGet

> ProjectDeployKey workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdGet(keyId, projectKey, workspace)

Get a project deploy key

Returns the deploy key belonging to a specific key ID.  Example: &#x60;&#x60;&#x60; $ curl -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys/1234  Output: {     \&quot;pagelen\&quot;:10,     \&quot;values\&quot;:[         {             \&quot;comment\&quot;:\&quot;thakseth@C02W454JHTD8\&quot;,             \&quot;last_used\&quot;:null,             \&quot;links\&quot;:{                 \&quot;self\&quot;:{                     \&quot;href\&quot;:\&quot;https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys/1234\&quot;                 }             },             \&quot;label\&quot;:\&quot;test\&quot;,             \&quot;project\&quot;:{                 \&quot;links\&quot;:{                     \&quot;self\&quot;:{                         \&quot;href\&quot;:\&quot;https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT\&quot;                     }                 },                 \&quot;type\&quot;:\&quot;project\&quot;,                 \&quot;name\&quot;:\&quot;cooperative standard\&quot;,                 \&quot;key\&quot;:\&quot;TEST_PROJECT\&quot;,                 \&quot;uuid\&quot;:\&quot;{3b3e510b-7f2b-414d-a2b7-76c4e405c1c0}\&quot;             },             \&quot;created_on\&quot;:\&quot;2021-07-28T21:20:19.491721+00:00\&quot;,             \&quot;key\&quot;:\&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDX5yfMOEw6HG9jKTYTisbmDTJ4MCUTSVGr5e4OWvY3UuI2A6F8SdzQqa2f5BABA/4g5Sk5awJrYHlNu3EzV1V2I44tR3A4fnZAG71ZKyDPi1wvdO7UYmFgxV/Vd18H9QZFFjICGDM7W0PT2mI0kON/jN3qNWi+GiB/xgaeQKSqynysdysDp8lnnI/8Sh3ikURP9UP83ShRCpAXszOUNaa+UUlcYQYBDLIGowsg51c4PCkC3DNhAMxppkNRKoSOWwyl+oRVXHSDylkiJSBHW3HH4Q6WHieD54kGrjbhWBKdnnxKX7QAAZBDseY+t01N36m6/ljvXSUEcBWtHxBYye0r\&quot;,             \&quot;type\&quot;:\&quot;project_deploy_key\&quot;,             \&quot;id\&quot;:1234         }     ], } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.DeploymentsApi();
let keyId = "keyId_example"; // String | The key ID matching the project deploy key.
let projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.workspacesWorkspaceProjectsProjectKeyDeployKeysKeyIdGet(keyId, projectKey, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyId** | **String**| The key ID matching the project deploy key. | 
 **projectKey** | **String**| The project in question. This is the actual &#x60;key&#x60; assigned to the project.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**ProjectDeployKey**](ProjectDeployKey.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesWorkspaceProjectsProjectKeyDeployKeysPost

> ProjectDeployKey workspacesWorkspaceProjectsProjectKeyDeployKeysPost(projectKey, workspace)

Create a project deploy key

Create a new deploy key in a project.  Example: &#x60;&#x60;&#x60; $ curl -XPOST \\ -H \&quot;Authorization &lt;auth header&gt;\&quot; \\ -H \&quot;Content-type: application/json\&quot; \\ https://api.bitbucket.org/2.0/workspaces/jzeng/projects/JZ/deploy-keys/ -d \\ &#39;{     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5 mleu@C02W454JHTD8\&quot;,     \&quot;label\&quot;: \&quot;mydeploykey\&quot; }&#39;  Output: {     \&quot;comment\&quot;: \&quot;mleu@C02W454JHTD8\&quot;,     \&quot;last_used\&quot;: null,     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/workspaces/testadfsa/projects/ASDF/deploy-keys/5/\&quot;         }     },     \&quot;label\&quot;: \&quot;myprojectkey\&quot;,     \&quot;project\&quot;: {         ...     },     \&quot;created_on\&quot;: \&quot;2021-08-10T05:28:00.570859+00:00\&quot;,     \&quot;key\&quot;: \&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\&quot;,     \&quot;type\&quot;: \&quot;project_deploy_key\&quot;,     \&quot;id\&quot;: 5 } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.DeploymentsApi();
let projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.workspacesWorkspaceProjectsProjectKeyDeployKeysPost(projectKey, workspace, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectKey** | **String**| The project in question. This is the actual &#x60;key&#x60; assigned to the project.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**ProjectDeployKey**](ProjectDeployKey.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

