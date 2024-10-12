# BitbucketApi.PipelinesApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDeploymentVariable**](PipelinesApi.md#createDeploymentVariable) | **POST** /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables | Create a variable for an environment
[**createPipelineForRepository**](PipelinesApi.md#createPipelineForRepository) | **POST** /repositories/{workspace}/{repo_slug}/pipelines | Run a pipeline
[**createPipelineVariableForTeam**](PipelinesApi.md#createPipelineVariableForTeam) | **POST** /teams/{username}/pipelines_config/variables | Create a variable for a user
[**createPipelineVariableForUser**](PipelinesApi.md#createPipelineVariableForUser) | **POST** /users/{selected_user}/pipelines_config/variables | Create a variable for a user
[**createPipelineVariableForWorkspace**](PipelinesApi.md#createPipelineVariableForWorkspace) | **POST** /workspaces/{workspace}/pipelines-config/variables | Create a variable for a workspace
[**createRepositoryPipelineKnownHost**](PipelinesApi.md#createRepositoryPipelineKnownHost) | **POST** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts | Create a known host
[**createRepositoryPipelineSchedule**](PipelinesApi.md#createRepositoryPipelineSchedule) | **POST** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules | Create a schedule
[**createRepositoryPipelineVariable**](PipelinesApi.md#createRepositoryPipelineVariable) | **POST** /repositories/{workspace}/{repo_slug}/pipelines_config/variables | Create a variable for a repository
[**deleteDeploymentVariable**](PipelinesApi.md#deleteDeploymentVariable) | **DELETE** /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid} | Delete a variable for an environment
[**deletePipelineVariableForTeam**](PipelinesApi.md#deletePipelineVariableForTeam) | **DELETE** /teams/{username}/pipelines_config/variables/{variable_uuid} | Delete a variable for a team
[**deletePipelineVariableForUser**](PipelinesApi.md#deletePipelineVariableForUser) | **DELETE** /users/{selected_user}/pipelines_config/variables/{variable_uuid} | Delete a variable for a user
[**deletePipelineVariableForWorkspace**](PipelinesApi.md#deletePipelineVariableForWorkspace) | **DELETE** /workspaces/{workspace}/pipelines-config/variables/{variable_uuid} | Delete a variable for a workspace
[**deleteRepositoryPipelineCache**](PipelinesApi.md#deleteRepositoryPipelineCache) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid} | Delete a cache
[**deleteRepositoryPipelineCaches**](PipelinesApi.md#deleteRepositoryPipelineCaches) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines-config/caches | Delete caches
[**deleteRepositoryPipelineKeyPair**](PipelinesApi.md#deleteRepositoryPipelineKeyPair) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair | Delete SSH key pair
[**deleteRepositoryPipelineKnownHost**](PipelinesApi.md#deleteRepositoryPipelineKnownHost) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid} | Delete a known host
[**deleteRepositoryPipelineSchedule**](PipelinesApi.md#deleteRepositoryPipelineSchedule) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid} | Delete a schedule
[**deleteRepositoryPipelineVariable**](PipelinesApi.md#deleteRepositoryPipelineVariable) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid} | Delete a variable for a repository
[**getDeploymentVariables**](PipelinesApi.md#getDeploymentVariables) | **GET** /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables | List variables for an environment
[**getOIDCConfiguration**](PipelinesApi.md#getOIDCConfiguration) | **GET** /workspaces/{workspace}/pipelines-config/identity/oidc/.well-known/openid-configuration | Get OpenID configuration for OIDC in Pipelines
[**getOIDCKeys**](PipelinesApi.md#getOIDCKeys) | **GET** /workspaces/{workspace}/pipelines-config/identity/oidc/keys.json | Get keys for OIDC in Pipelines
[**getPipelineContainerLog**](PipelinesApi.md#getPipelineContainerLog) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid} | Get the logs for the build container or a service container for a given step of a pipeline.
[**getPipelineForRepository**](PipelinesApi.md#getPipelineForRepository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid} | Get a pipeline
[**getPipelineStepForRepository**](PipelinesApi.md#getPipelineStepForRepository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid} | Get a step of a pipeline
[**getPipelineStepLogForRepository**](PipelinesApi.md#getPipelineStepLogForRepository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log | Get log file for a step
[**getPipelineStepsForRepository**](PipelinesApi.md#getPipelineStepsForRepository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps | List steps for a pipeline
[**getPipelineTestReportTestCaseReasons**](PipelinesApi.md#getPipelineTestReportTestCaseReasons) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases/{test_case_uuid}/test_case_reasons | Get test case reasons (output) for a given test case in a step of a pipeline.
[**getPipelineTestReportTestCases**](PipelinesApi.md#getPipelineTestReportTestCases) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases | Get test cases for a given step of a pipeline.
[**getPipelineTestReports**](PipelinesApi.md#getPipelineTestReports) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports | Get a summary of test reports for a given step of a pipeline.
[**getPipelineVariableForTeam**](PipelinesApi.md#getPipelineVariableForTeam) | **GET** /teams/{username}/pipelines_config/variables/{variable_uuid} | Get a variable for a team
[**getPipelineVariableForUser**](PipelinesApi.md#getPipelineVariableForUser) | **GET** /users/{selected_user}/pipelines_config/variables/{variable_uuid} | Get a variable for a user
[**getPipelineVariableForWorkspace**](PipelinesApi.md#getPipelineVariableForWorkspace) | **GET** /workspaces/{workspace}/pipelines-config/variables/{variable_uuid} | Get variable for a workspace
[**getPipelineVariablesForTeam**](PipelinesApi.md#getPipelineVariablesForTeam) | **GET** /teams/{username}/pipelines_config/variables | List variables for an account
[**getPipelineVariablesForUser**](PipelinesApi.md#getPipelineVariablesForUser) | **GET** /users/{selected_user}/pipelines_config/variables | List variables for a user
[**getPipelineVariablesForWorkspace**](PipelinesApi.md#getPipelineVariablesForWorkspace) | **GET** /workspaces/{workspace}/pipelines-config/variables | List variables for a workspace
[**getPipelinesForRepository**](PipelinesApi.md#getPipelinesForRepository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines | List pipelines
[**getRepositoryPipelineCacheContentURI**](PipelinesApi.md#getRepositoryPipelineCacheContentURI) | **GET** /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}/content-uri | Get cache content URI
[**getRepositoryPipelineCaches**](PipelinesApi.md#getRepositoryPipelineCaches) | **GET** /repositories/{workspace}/{repo_slug}/pipelines-config/caches | List caches
[**getRepositoryPipelineConfig**](PipelinesApi.md#getRepositoryPipelineConfig) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config | Get configuration
[**getRepositoryPipelineKnownHost**](PipelinesApi.md#getRepositoryPipelineKnownHost) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid} | Get a known host
[**getRepositoryPipelineKnownHosts**](PipelinesApi.md#getRepositoryPipelineKnownHosts) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts | List known hosts
[**getRepositoryPipelineSchedule**](PipelinesApi.md#getRepositoryPipelineSchedule) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid} | Get a schedule
[**getRepositoryPipelineScheduleExecutions**](PipelinesApi.md#getRepositoryPipelineScheduleExecutions) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}/executions | List executions of a schedule
[**getRepositoryPipelineSchedules**](PipelinesApi.md#getRepositoryPipelineSchedules) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules | List schedules
[**getRepositoryPipelineSshKeyPair**](PipelinesApi.md#getRepositoryPipelineSshKeyPair) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair | Get SSH key pair
[**getRepositoryPipelineVariable**](PipelinesApi.md#getRepositoryPipelineVariable) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid} | Get a variable for a repository
[**getRepositoryPipelineVariables**](PipelinesApi.md#getRepositoryPipelineVariables) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/variables | List variables for a repository
[**stopPipeline**](PipelinesApi.md#stopPipeline) | **POST** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline | Stop a pipeline
[**updateDeploymentVariable**](PipelinesApi.md#updateDeploymentVariable) | **PUT** /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid} | Update a variable for an environment
[**updatePipelineVariableForTeam**](PipelinesApi.md#updatePipelineVariableForTeam) | **PUT** /teams/{username}/pipelines_config/variables/{variable_uuid} | Update a variable for a team
[**updatePipelineVariableForUser**](PipelinesApi.md#updatePipelineVariableForUser) | **PUT** /users/{selected_user}/pipelines_config/variables/{variable_uuid} | Update a variable for a user
[**updatePipelineVariableForWorkspace**](PipelinesApi.md#updatePipelineVariableForWorkspace) | **PUT** /workspaces/{workspace}/pipelines-config/variables/{variable_uuid} | Update variable for a workspace
[**updateRepositoryBuildNumber**](PipelinesApi.md#updateRepositoryBuildNumber) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/build_number | Update the next build number
[**updateRepositoryPipelineConfig**](PipelinesApi.md#updateRepositoryPipelineConfig) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config | Update configuration
[**updateRepositoryPipelineKeyPair**](PipelinesApi.md#updateRepositoryPipelineKeyPair) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair | Update SSH key pair
[**updateRepositoryPipelineKnownHost**](PipelinesApi.md#updateRepositoryPipelineKnownHost) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid} | Update a known host
[**updateRepositoryPipelineSchedule**](PipelinesApi.md#updateRepositoryPipelineSchedule) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid} | Update a schedule
[**updateRepositoryPipelineVariable**](PipelinesApi.md#updateRepositoryPipelineVariable) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid} | Update a variable for a repository



## createDeploymentVariable

> DeploymentVariable createDeploymentVariable(workspace, repoSlug, environmentUuid, deploymentVariable)

Create a variable for an environment

Create a deployment environment level variable.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let environmentUuid = "environmentUuid_example"; // String | The environment.
let deploymentVariable = new BitbucketApi.DeploymentVariable(); // DeploymentVariable | The variable to create
apiInstance.createDeploymentVariable(workspace, repoSlug, environmentUuid, deploymentVariable, (error, data, response) => {
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
 **environmentUuid** | **String**| The environment. | 
 **deploymentVariable** | [**DeploymentVariable**](DeploymentVariable.md)| The variable to create | 

### Return type

[**DeploymentVariable**](DeploymentVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPipelineForRepository

> Pipeline createPipelineForRepository(workspace, repoSlug, pipeline)

Run a pipeline

Endpoint to create and initiate a pipeline. There are a couple of different options to initiate a pipeline, where the payload of the request will determine which type of pipeline will be instantiated. # Trigger a Pipeline for a branch One way to trigger pipelines is by specifying the branch for which you want to trigger a pipeline. The specified branch will be used to determine which pipeline definition from the &#x60;bitbucket-pipelines.yml&#x60; file will be applied to initiate the pipeline. The pipeline will then do a clone of the repository and checkout the latest revision of the specified branch.  ### Example  &#x60;&#x60;&#x60; $ curl -X POST -is -u username:password \\   -H &#39;Content-Type: application/json&#39; \\  https://api.bitbucket.org/2.0/repositories/jeroendr/meat-demo2/pipelines/ \\   -d &#39;   {     \&quot;target\&quot;: {       \&quot;ref_type\&quot;: \&quot;branch\&quot;,       \&quot;type\&quot;: \&quot;pipeline_ref_target\&quot;,       \&quot;ref_name\&quot;: \&quot;master\&quot;     }   }&#39; &#x60;&#x60;&#x60; # Trigger a Pipeline for a commit on a branch or tag You can initiate a pipeline for a specific commit and in the context of a specified reference (e.g. a branch, tag or bookmark). The specified reference will be used to determine which pipeline definition from the bitbucket-pipelines.yml file will be applied to initiate the pipeline. The pipeline will clone the repository and then do a checkout the specified reference.  The following reference types are supported:  * &#x60;branch&#x60; * &#x60;named_branch&#x60; * &#x60;bookmark&#x60;  * &#x60;tag&#x60;  ### Example  &#x60;&#x60;&#x60; $ curl -X POST -is -u username:password \\   -H &#39;Content-Type: application/json&#39; \\   https://api.bitbucket.org/2.0/repositories/jeroendr/meat-demo2/pipelines/ \\   -d &#39;   {     \&quot;target\&quot;: {       \&quot;commit\&quot;: {         \&quot;type\&quot;: \&quot;commit\&quot;,         \&quot;hash\&quot;: \&quot;ce5b7431602f7cbba007062eeb55225c6e18e956\&quot;       },       \&quot;ref_type\&quot;: \&quot;branch\&quot;,       \&quot;type\&quot;: \&quot;pipeline_ref_target\&quot;,       \&quot;ref_name\&quot;: \&quot;master\&quot;     }   }&#39; &#x60;&#x60;&#x60; # Trigger a specific pipeline definition for a commit You can trigger a specific pipeline that is defined in your &#x60;bitbucket-pipelines.yml&#x60; file for a specific commit. In addition to the commit revision, you specify the type and pattern of the selector that identifies the pipeline definition. The resulting pipeline will then clone the repository and checkout the specified revision.  ### Example  &#x60;&#x60;&#x60; $ curl -X POST -is -u username:password \\   -H &#39;Content-Type: application/json&#39; \\  https://api.bitbucket.org/2.0/repositories/jeroendr/meat-demo2/pipelines/ \\  -d &#39;   {      \&quot;target\&quot;: {       \&quot;commit\&quot;: {          \&quot;hash\&quot;:\&quot;a3c4e02c9a3755eccdc3764e6ea13facdf30f923\&quot;,          \&quot;type\&quot;:\&quot;commit\&quot;        },         \&quot;selector\&quot;: {            \&quot;type\&quot;:\&quot;custom\&quot;,               \&quot;pattern\&quot;:\&quot;Deploy to production\&quot;           },         \&quot;type\&quot;:\&quot;pipeline_commit_target\&quot;    }   }&#39; &#x60;&#x60;&#x60; # Trigger a specific pipeline definition for a commit on a branch or tag You can trigger a specific pipeline that is defined in your &#x60;bitbucket-pipelines.yml&#x60; file for a specific commit in the context of a specified reference. In addition to the commit revision, you specify the type and pattern of the selector that identifies the pipeline definition, as well as the reference information. The resulting pipeline will then clone the repository a checkout the specified reference.  ### Example  &#x60;&#x60;&#x60; $ curl -X POST -is -u username:password \\   -H &#39;Content-Type: application/json&#39; \\  https://api.bitbucket.org/2.0/repositories/jeroendr/meat-demo2/pipelines/ \\  -d &#39;   {      \&quot;target\&quot;: {       \&quot;commit\&quot;: {          \&quot;hash\&quot;:\&quot;a3c4e02c9a3755eccdc3764e6ea13facdf30f923\&quot;,          \&quot;type\&quot;:\&quot;commit\&quot;        },        \&quot;selector\&quot;: {           \&quot;type\&quot;: \&quot;custom\&quot;,           \&quot;pattern\&quot;: \&quot;Deploy to production\&quot;        },        \&quot;type\&quot;: \&quot;pipeline_ref_target\&quot;,        \&quot;ref_name\&quot;: \&quot;master\&quot;,        \&quot;ref_type\&quot;: \&quot;branch\&quot;      }   }&#39; &#x60;&#x60;&#x60;   # Trigger a custom pipeline with variables In addition to triggering a custom pipeline that is defined in your &#x60;bitbucket-pipelines.yml&#x60; file as shown in the examples above, you can specify variables that will be available for your build. In the request, provide a list of variables, specifying the following for each variable: key, value, and whether it should be secured or not (this field is optional and defaults to not secured).  ### Example  &#x60;&#x60;&#x60; $ curl -X POST -is -u username:password \\   -H &#39;Content-Type: application/json&#39; \\  https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \\  -d &#39;   {     \&quot;target\&quot;: {       \&quot;type\&quot;: \&quot;pipeline_ref_target\&quot;,       \&quot;ref_type\&quot;: \&quot;branch\&quot;,       \&quot;ref_name\&quot;: \&quot;master\&quot;,       \&quot;selector\&quot;: {         \&quot;type\&quot;: \&quot;custom\&quot;,         \&quot;pattern\&quot;: \&quot;Deploy to production\&quot;       }     },     \&quot;variables\&quot;: [       {         \&quot;key\&quot;: \&quot;var1key\&quot;,         \&quot;value\&quot;: \&quot;var1value\&quot;,         \&quot;secured\&quot;: true       },       {         \&quot;key\&quot;: \&quot;var2key\&quot;,         \&quot;value\&quot;: \&quot;var2value\&quot;       }     ]   }&#39; &#x60;&#x60;&#x60;  # Trigger a pull request pipeline  You can also initiate a pipeline for a specific pull request.  ### Example  &#x60;&#x60;&#x60; $ curl -X POST -is -u username:password \\   -H &#39;Content-Type: application/json&#39; \\  https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \\  -d &#39;   {  \&quot;target\&quot;: {       \&quot;type\&quot;: \&quot;pipeline_pullrequest_target\&quot;,    \&quot;source\&quot;: \&quot;pull-request-branch\&quot;,       \&quot;destination\&quot;: \&quot;master\&quot;,       \&quot;destination_commit\&quot;: {         \&quot;hash\&quot; : \&quot;9f848b7\&quot;       },       \&quot;commit\&quot;: {        \&quot;hash\&quot; : \&quot;1a372fc\&quot;       },       \&quot;pullrequest\&quot; : {        \&quot;id\&quot; : \&quot;3\&quot;       },    \&quot;selector\&quot;: {         \&quot;type\&quot;: \&quot;pull-requests\&quot;,         \&quot;pattern\&quot;: \&quot;**\&quot;       }     }   }&#39; &#x60;&#x60;&#x60; 

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipeline = new BitbucketApi.Pipeline(); // Pipeline | The pipeline to initiate.
apiInstance.createPipelineForRepository(workspace, repoSlug, pipeline, (error, data, response) => {
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
 **pipeline** | [**Pipeline**](Pipeline.md)| The pipeline to initiate. | 

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPipelineVariableForTeam

> PipelineVariable createPipelineVariableForTeam(username, opts)

Create a variable for a user

Create an account level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let username = "username_example"; // String | The account.
let opts = {
  'pipelineVariable': new BitbucketApi.PipelineVariable() // PipelineVariable | The variable to create.
};
apiInstance.createPipelineVariableForTeam(username, opts, (error, data, response) => {
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
 **username** | **String**| The account. | 
 **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The variable to create. | [optional] 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPipelineVariableForUser

> PipelineVariable createPipelineVariableForUser(selectedUser, opts)

Create a variable for a user

Create a user level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
let opts = {
  'pipelineVariable': new BitbucketApi.PipelineVariable() // PipelineVariable | The variable to create.
};
apiInstance.createPipelineVariableForUser(selectedUser, opts, (error, data, response) => {
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
 **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | 
 **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The variable to create. | [optional] 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPipelineVariableForWorkspace

> PipelineVariable createPipelineVariableForWorkspace(workspace, opts)

Create a variable for a workspace

Create a workspace level variable.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let opts = {
  'pipelineVariable': new BitbucketApi.PipelineVariable() // PipelineVariable | The variable to create.
};
apiInstance.createPipelineVariableForWorkspace(workspace, opts, (error, data, response) => {
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
 **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The variable to create. | [optional] 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRepositoryPipelineKnownHost

> PipelineKnownHost createRepositoryPipelineKnownHost(workspace, repoSlug, pipelineKnownHost)

Create a known host

Create a repository level known host.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineKnownHost = new BitbucketApi.PipelineKnownHost(); // PipelineKnownHost | The known host to create.
apiInstance.createRepositoryPipelineKnownHost(workspace, repoSlug, pipelineKnownHost, (error, data, response) => {
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
 **pipelineKnownHost** | [**PipelineKnownHost**](PipelineKnownHost.md)| The known host to create. | 

### Return type

[**PipelineKnownHost**](PipelineKnownHost.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRepositoryPipelineSchedule

> PipelineSchedule createRepositoryPipelineSchedule(workspace, repoSlug, pipelineSchedulePostRequestBody)

Create a schedule

Create a schedule for the given repository.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineSchedulePostRequestBody = new BitbucketApi.PipelineSchedulePostRequestBody(); // PipelineSchedulePostRequestBody | The schedule to create.
apiInstance.createRepositoryPipelineSchedule(workspace, repoSlug, pipelineSchedulePostRequestBody, (error, data, response) => {
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
 **pipelineSchedulePostRequestBody** | [**PipelineSchedulePostRequestBody**](PipelineSchedulePostRequestBody.md)| The schedule to create. | 

### Return type

[**PipelineSchedule**](PipelineSchedule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRepositoryPipelineVariable

> PipelineVariable createRepositoryPipelineVariable(workspace, repoSlug, pipelineVariable)

Create a variable for a repository

Create a repository level variable.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineVariable = new BitbucketApi.PipelineVariable(); // PipelineVariable | The variable to create.
apiInstance.createRepositoryPipelineVariable(workspace, repoSlug, pipelineVariable, (error, data, response) => {
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
 **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The variable to create. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDeploymentVariable

> deleteDeploymentVariable(workspace, repoSlug, environmentUuid, variableUuid)

Delete a variable for an environment

Delete a deployment environment level variable.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let environmentUuid = "environmentUuid_example"; // String | The environment.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable to delete.
apiInstance.deleteDeploymentVariable(workspace, repoSlug, environmentUuid, variableUuid, (error, data, response) => {
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
 **environmentUuid** | **String**| The environment. | 
 **variableUuid** | **String**| The UUID of the variable to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePipelineVariableForTeam

> deletePipelineVariableForTeam(username, variableUuid)

Delete a variable for a team

Delete a team level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let username = "username_example"; // String | The account.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable to delete.
apiInstance.deletePipelineVariableForTeam(username, variableUuid, (error, data, response) => {
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
 **username** | **String**| The account. | 
 **variableUuid** | **String**| The UUID of the variable to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePipelineVariableForUser

> deletePipelineVariableForUser(selectedUser, variableUuid)

Delete a variable for a user

Delete an account level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable to delete.
apiInstance.deletePipelineVariableForUser(selectedUser, variableUuid, (error, data, response) => {
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
 **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | 
 **variableUuid** | **String**| The UUID of the variable to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePipelineVariableForWorkspace

> deletePipelineVariableForWorkspace(workspace, variableUuid)

Delete a variable for a workspace

Delete a workspace level variable.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable to delete.
apiInstance.deletePipelineVariableForWorkspace(workspace, variableUuid, (error, data, response) => {
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
 **variableUuid** | **String**| The UUID of the variable to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRepositoryPipelineCache

> deleteRepositoryPipelineCache(workspace, repoSlug, cacheUuid)

Delete a cache

Delete a repository cache.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | The account.
let repoSlug = "repoSlug_example"; // String | The repository.
let cacheUuid = "cacheUuid_example"; // String | The UUID of the cache to delete.
apiInstance.deleteRepositoryPipelineCache(workspace, repoSlug, cacheUuid, (error, data, response) => {
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
 **workspace** | **String**| The account. | 
 **repoSlug** | **String**| The repository. | 
 **cacheUuid** | **String**| The UUID of the cache to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRepositoryPipelineCaches

> deleteRepositoryPipelineCaches(workspace, repoSlug, name)

Delete caches

Delete repository cache versions by name.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | The account.
let repoSlug = "repoSlug_example"; // String | The repository.
let name = "name_example"; // String | The cache name.
apiInstance.deleteRepositoryPipelineCaches(workspace, repoSlug, name, (error, data, response) => {
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
 **workspace** | **String**| The account. | 
 **repoSlug** | **String**| The repository. | 
 **name** | **String**| The cache name. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRepositoryPipelineKeyPair

> deleteRepositoryPipelineKeyPair(workspace, repoSlug)

Delete SSH key pair

Delete the repository SSH key pair.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
apiInstance.deleteRepositoryPipelineKeyPair(workspace, repoSlug, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRepositoryPipelineKnownHost

> deleteRepositoryPipelineKnownHost(workspace, repoSlug, knownHostUuid)

Delete a known host

Delete a repository level known host.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let knownHostUuid = "knownHostUuid_example"; // String | The UUID of the known host to delete.
apiInstance.deleteRepositoryPipelineKnownHost(workspace, repoSlug, knownHostUuid, (error, data, response) => {
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
 **knownHostUuid** | **String**| The UUID of the known host to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRepositoryPipelineSchedule

> deleteRepositoryPipelineSchedule(workspace, repoSlug, scheduleUuid)

Delete a schedule

Delete a schedule.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let scheduleUuid = "scheduleUuid_example"; // String | The uuid of the schedule.
apiInstance.deleteRepositoryPipelineSchedule(workspace, repoSlug, scheduleUuid, (error, data, response) => {
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
 **scheduleUuid** | **String**| The uuid of the schedule. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRepositoryPipelineVariable

> deleteRepositoryPipelineVariable(workspace, repoSlug, variableUuid)

Delete a variable for a repository

Delete a repository level variable.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable to delete.
apiInstance.deleteRepositoryPipelineVariable(workspace, repoSlug, variableUuid, (error, data, response) => {
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
 **variableUuid** | **String**| The UUID of the variable to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeploymentVariables

> PaginatedDeploymentVariable getDeploymentVariables(workspace, repoSlug, environmentUuid)

List variables for an environment

Find deployment environment level variables.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let environmentUuid = "environmentUuid_example"; // String | The environment.
apiInstance.getDeploymentVariables(workspace, repoSlug, environmentUuid, (error, data, response) => {
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
 **environmentUuid** | **String**| The environment. | 

### Return type

[**PaginatedDeploymentVariable**](PaginatedDeploymentVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOIDCConfiguration

> getOIDCConfiguration(workspace)

Get OpenID configuration for OIDC in Pipelines

This is part of OpenID Connect for Pipelines, see https://support.atlassian.com/bitbucket-cloud/docs/integrate-pipelines-with-resource-servers-using-oidc/

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
apiInstance.getOIDCConfiguration(workspace, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOIDCKeys

> getOIDCKeys(workspace)

Get keys for OIDC in Pipelines

This is part of OpenID Connect for Pipelines, see https://support.atlassian.com/bitbucket-cloud/docs/integrate-pipelines-with-resource-servers-using-oidc/

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
apiInstance.getOIDCKeys(workspace, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPipelineContainerLog

> getPipelineContainerLog(workspace, repoSlug, pipelineUuid, stepUuid, logUuid)

Get the logs for the build container or a service container for a given step of a pipeline.

Retrieve the log file for a build container or service container.  This endpoint supports (and encourages!) the use of [HTTP Range requests](https://tools.ietf.org/html/rfc7233) to deal with potentially very large log files.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
let stepUuid = "stepUuid_example"; // String | The UUID of the step.
let logUuid = "logUuid_example"; // String | For the main build container specify the step UUID; for a service container specify the service container UUID
apiInstance.getPipelineContainerLog(workspace, repoSlug, pipelineUuid, stepUuid, logUuid, (error, data, response) => {
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
 **pipelineUuid** | **String**| The UUID of the pipeline. | 
 **stepUuid** | **String**| The UUID of the step. | 
 **logUuid** | **String**| For the main build container specify the step UUID; for a service container specify the service container UUID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getPipelineForRepository

> Pipeline getPipelineForRepository(workspace, repoSlug, pipelineUuid)

Get a pipeline

Retrieve a specified pipeline

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineUuid = "pipelineUuid_example"; // String | The pipeline UUID.
apiInstance.getPipelineForRepository(workspace, repoSlug, pipelineUuid, (error, data, response) => {
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
 **pipelineUuid** | **String**| The pipeline UUID. | 

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPipelineStepForRepository

> PipelineStep getPipelineStepForRepository(workspace, repoSlug, pipelineUuid, stepUuid)

Get a step of a pipeline

Retrieve a given step of a pipeline.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
let stepUuid = "stepUuid_example"; // String | The UUID of the step.
apiInstance.getPipelineStepForRepository(workspace, repoSlug, pipelineUuid, stepUuid, (error, data, response) => {
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
 **pipelineUuid** | **String**| The UUID of the pipeline. | 
 **stepUuid** | **String**| The UUID of the step. | 

### Return type

[**PipelineStep**](PipelineStep.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPipelineStepLogForRepository

> getPipelineStepLogForRepository(workspace, repoSlug, pipelineUuid, stepUuid)

Get log file for a step

Retrieve the log file for a given step of a pipeline.  This endpoint supports (and encourages!) the use of [HTTP Range requests](https://tools.ietf.org/html/rfc7233) to deal with potentially very large log files.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
let stepUuid = "stepUuid_example"; // String | The UUID of the step.
apiInstance.getPipelineStepLogForRepository(workspace, repoSlug, pipelineUuid, stepUuid, (error, data, response) => {
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
 **pipelineUuid** | **String**| The UUID of the pipeline. | 
 **stepUuid** | **String**| The UUID of the step. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getPipelineStepsForRepository

> PaginatedPipelineSteps getPipelineStepsForRepository(workspace, repoSlug, pipelineUuid)

List steps for a pipeline

Find steps for the given pipeline.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
apiInstance.getPipelineStepsForRepository(workspace, repoSlug, pipelineUuid, (error, data, response) => {
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
 **pipelineUuid** | **String**| The UUID of the pipeline. | 

### Return type

[**PaginatedPipelineSteps**](PaginatedPipelineSteps.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPipelineTestReportTestCaseReasons

> getPipelineTestReportTestCaseReasons(workspace, repoSlug, pipelineUuid, stepUuid, testCaseUuid)

Get test case reasons (output) for a given test case in a step of a pipeline.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
let stepUuid = "stepUuid_example"; // String | The UUID of the step.
let testCaseUuid = "testCaseUuid_example"; // String | The UUID of the test case.
apiInstance.getPipelineTestReportTestCaseReasons(workspace, repoSlug, pipelineUuid, stepUuid, testCaseUuid, (error, data, response) => {
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
 **pipelineUuid** | **String**| The UUID of the pipeline. | 
 **stepUuid** | **String**| The UUID of the step. | 
 **testCaseUuid** | **String**| The UUID of the test case. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPipelineTestReportTestCases

> getPipelineTestReportTestCases(workspace, repoSlug, pipelineUuid, stepUuid)

Get test cases for a given step of a pipeline.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
let stepUuid = "stepUuid_example"; // String | The UUID of the step.
apiInstance.getPipelineTestReportTestCases(workspace, repoSlug, pipelineUuid, stepUuid, (error, data, response) => {
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
 **pipelineUuid** | **String**| The UUID of the pipeline. | 
 **stepUuid** | **String**| The UUID of the step. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPipelineTestReports

> getPipelineTestReports(workspace, repoSlug, pipelineUuid, stepUuid)

Get a summary of test reports for a given step of a pipeline.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
let stepUuid = "stepUuid_example"; // String | The UUID of the step.
apiInstance.getPipelineTestReports(workspace, repoSlug, pipelineUuid, stepUuid, (error, data, response) => {
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
 **pipelineUuid** | **String**| The UUID of the pipeline. | 
 **stepUuid** | **String**| The UUID of the step. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPipelineVariableForTeam

> PipelineVariable getPipelineVariableForTeam(username, variableUuid)

Get a variable for a team

Retrieve a team level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let username = "username_example"; // String | The account.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable to retrieve.
apiInstance.getPipelineVariableForTeam(username, variableUuid, (error, data, response) => {
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
 **username** | **String**| The account. | 
 **variableUuid** | **String**| The UUID of the variable to retrieve. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPipelineVariableForUser

> PipelineVariable getPipelineVariableForUser(selectedUser, variableUuid)

Get a variable for a user

Retrieve a user level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable to retrieve.
apiInstance.getPipelineVariableForUser(selectedUser, variableUuid, (error, data, response) => {
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
 **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | 
 **variableUuid** | **String**| The UUID of the variable to retrieve. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPipelineVariableForWorkspace

> PipelineVariable getPipelineVariableForWorkspace(workspace, variableUuid)

Get variable for a workspace

Retrieve a workspace level variable.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable to retrieve.
apiInstance.getPipelineVariableForWorkspace(workspace, variableUuid, (error, data, response) => {
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
 **variableUuid** | **String**| The UUID of the variable to retrieve. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPipelineVariablesForTeam

> PaginatedPipelineVariables getPipelineVariablesForTeam(username)

List variables for an account

Find account level variables. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let username = "username_example"; // String | The account.
apiInstance.getPipelineVariablesForTeam(username, (error, data, response) => {
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
 **username** | **String**| The account. | 

### Return type

[**PaginatedPipelineVariables**](PaginatedPipelineVariables.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPipelineVariablesForUser

> PaginatedPipelineVariables getPipelineVariablesForUser(selectedUser)

List variables for a user

Find user level variables. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
apiInstance.getPipelineVariablesForUser(selectedUser, (error, data, response) => {
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
 **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | 

### Return type

[**PaginatedPipelineVariables**](PaginatedPipelineVariables.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPipelineVariablesForWorkspace

> PaginatedPipelineVariables getPipelineVariablesForWorkspace(workspace)

List variables for a workspace

Find workspace level variables.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
apiInstance.getPipelineVariablesForWorkspace(workspace, (error, data, response) => {
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

### Return type

[**PaginatedPipelineVariables**](PaginatedPipelineVariables.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPipelinesForRepository

> PaginatedPipelines getPipelinesForRepository(workspace, repoSlug)

List pipelines

Find pipelines

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
apiInstance.getPipelinesForRepository(workspace, repoSlug, (error, data, response) => {
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

[**PaginatedPipelines**](PaginatedPipelines.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepositoryPipelineCacheContentURI

> PipelineCacheContentUri getRepositoryPipelineCacheContentURI(workspace, repoSlug, cacheUuid)

Get cache content URI

Retrieve the URI of the content of the specified cache.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | The account.
let repoSlug = "repoSlug_example"; // String | The repository.
let cacheUuid = "cacheUuid_example"; // String | The UUID of the cache.
apiInstance.getRepositoryPipelineCacheContentURI(workspace, repoSlug, cacheUuid, (error, data, response) => {
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
 **workspace** | **String**| The account. | 
 **repoSlug** | **String**| The repository. | 
 **cacheUuid** | **String**| The UUID of the cache. | 

### Return type

[**PipelineCacheContentUri**](PipelineCacheContentUri.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepositoryPipelineCaches

> PaginatedPipelineCaches getRepositoryPipelineCaches(workspace, repoSlug)

List caches

Retrieve the repository pipelines caches.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | The account.
let repoSlug = "repoSlug_example"; // String | The repository.
apiInstance.getRepositoryPipelineCaches(workspace, repoSlug, (error, data, response) => {
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
 **workspace** | **String**| The account. | 
 **repoSlug** | **String**| The repository. | 

### Return type

[**PaginatedPipelineCaches**](PaginatedPipelineCaches.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepositoryPipelineConfig

> PipelinesConfig getRepositoryPipelineConfig(workspace, repoSlug)

Get configuration

Retrieve the repository pipelines configuration.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | The account.
let repoSlug = "repoSlug_example"; // String | The repository.
apiInstance.getRepositoryPipelineConfig(workspace, repoSlug, (error, data, response) => {
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
 **workspace** | **String**| The account. | 
 **repoSlug** | **String**| The repository. | 

### Return type

[**PipelinesConfig**](PipelinesConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepositoryPipelineKnownHost

> PipelineKnownHost getRepositoryPipelineKnownHost(workspace, repoSlug, knownHostUuid)

Get a known host

Retrieve a repository level known host.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let knownHostUuid = "knownHostUuid_example"; // String | The UUID of the known host to retrieve.
apiInstance.getRepositoryPipelineKnownHost(workspace, repoSlug, knownHostUuid, (error, data, response) => {
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
 **knownHostUuid** | **String**| The UUID of the known host to retrieve. | 

### Return type

[**PipelineKnownHost**](PipelineKnownHost.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepositoryPipelineKnownHosts

> PaginatedPipelineKnownHosts getRepositoryPipelineKnownHosts(workspace, repoSlug)

List known hosts

Find repository level known hosts.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
apiInstance.getRepositoryPipelineKnownHosts(workspace, repoSlug, (error, data, response) => {
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

[**PaginatedPipelineKnownHosts**](PaginatedPipelineKnownHosts.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepositoryPipelineSchedule

> PipelineSchedule getRepositoryPipelineSchedule(workspace, repoSlug, scheduleUuid)

Get a schedule

Retrieve a schedule by its UUID.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let scheduleUuid = "scheduleUuid_example"; // String | The uuid of the schedule.
apiInstance.getRepositoryPipelineSchedule(workspace, repoSlug, scheduleUuid, (error, data, response) => {
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
 **scheduleUuid** | **String**| The uuid of the schedule. | 

### Return type

[**PipelineSchedule**](PipelineSchedule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepositoryPipelineScheduleExecutions

> PaginatedPipelineScheduleExecutions getRepositoryPipelineScheduleExecutions(workspace, repoSlug, scheduleUuid)

List executions of a schedule

Retrieve the executions of a given schedule.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let scheduleUuid = "scheduleUuid_example"; // String | The uuid of the schedule.
apiInstance.getRepositoryPipelineScheduleExecutions(workspace, repoSlug, scheduleUuid, (error, data, response) => {
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
 **scheduleUuid** | **String**| The uuid of the schedule. | 

### Return type

[**PaginatedPipelineScheduleExecutions**](PaginatedPipelineScheduleExecutions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepositoryPipelineSchedules

> PaginatedPipelineSchedules getRepositoryPipelineSchedules(workspace, repoSlug)

List schedules

Retrieve the configured schedules for the given repository.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
apiInstance.getRepositoryPipelineSchedules(workspace, repoSlug, (error, data, response) => {
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

[**PaginatedPipelineSchedules**](PaginatedPipelineSchedules.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepositoryPipelineSshKeyPair

> PipelineSshKeyPair getRepositoryPipelineSshKeyPair(workspace, repoSlug)

Get SSH key pair

Retrieve the repository SSH key pair excluding the SSH private key. The private key is a write only field and will never be exposed in the logs or the REST API.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
apiInstance.getRepositoryPipelineSshKeyPair(workspace, repoSlug, (error, data, response) => {
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

[**PipelineSshKeyPair**](PipelineSshKeyPair.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepositoryPipelineVariable

> PipelineVariable getRepositoryPipelineVariable(workspace, repoSlug, variableUuid)

Get a variable for a repository

Retrieve a repository level variable.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable to retrieve.
apiInstance.getRepositoryPipelineVariable(workspace, repoSlug, variableUuid, (error, data, response) => {
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
 **variableUuid** | **String**| The UUID of the variable to retrieve. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepositoryPipelineVariables

> PaginatedPipelineVariables getRepositoryPipelineVariables(workspace, repoSlug)

List variables for a repository

Find repository level variables.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
apiInstance.getRepositoryPipelineVariables(workspace, repoSlug, (error, data, response) => {
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

[**PaginatedPipelineVariables**](PaginatedPipelineVariables.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopPipeline

> stopPipeline(workspace, repoSlug, pipelineUuid)

Stop a pipeline

Signal the stop of a pipeline and all of its steps that not have completed yet.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
apiInstance.stopPipeline(workspace, repoSlug, pipelineUuid, (error, data, response) => {
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
 **pipelineUuid** | **String**| The UUID of the pipeline. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeploymentVariable

> DeploymentVariable updateDeploymentVariable(workspace, repoSlug, environmentUuid, variableUuid, deploymentVariable)

Update a variable for an environment

Update a deployment environment level variable.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let environmentUuid = "environmentUuid_example"; // String | The environment.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable to update.
let deploymentVariable = new BitbucketApi.DeploymentVariable(); // DeploymentVariable | The updated deployment variable.
apiInstance.updateDeploymentVariable(workspace, repoSlug, environmentUuid, variableUuid, deploymentVariable, (error, data, response) => {
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
 **environmentUuid** | **String**| The environment. | 
 **variableUuid** | **String**| The UUID of the variable to update. | 
 **deploymentVariable** | [**DeploymentVariable**](DeploymentVariable.md)| The updated deployment variable. | 

### Return type

[**DeploymentVariable**](DeploymentVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePipelineVariableForTeam

> PipelineVariable updatePipelineVariableForTeam(username, variableUuid, pipelineVariable)

Update a variable for a team

Update a team level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let username = "username_example"; // String | The account.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable.
let pipelineVariable = new BitbucketApi.PipelineVariable(); // PipelineVariable | The updated variable.
apiInstance.updatePipelineVariableForTeam(username, variableUuid, pipelineVariable, (error, data, response) => {
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
 **username** | **String**| The account. | 
 **variableUuid** | **String**| The UUID of the variable. | 
 **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The updated variable. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePipelineVariableForUser

> PipelineVariable updatePipelineVariableForUser(selectedUser, variableUuid, pipelineVariable)

Update a variable for a user

Update a user level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable.
let pipelineVariable = new BitbucketApi.PipelineVariable(); // PipelineVariable | The updated variable.
apiInstance.updatePipelineVariableForUser(selectedUser, variableUuid, pipelineVariable, (error, data, response) => {
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
 **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | 
 **variableUuid** | **String**| The UUID of the variable. | 
 **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The updated variable. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePipelineVariableForWorkspace

> PipelineVariable updatePipelineVariableForWorkspace(workspace, variableUuid, pipelineVariable)

Update variable for a workspace

Update a workspace level variable.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable.
let pipelineVariable = new BitbucketApi.PipelineVariable(); // PipelineVariable | The updated variable.
apiInstance.updatePipelineVariableForWorkspace(workspace, variableUuid, pipelineVariable, (error, data, response) => {
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
 **variableUuid** | **String**| The UUID of the variable. | 
 **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The updated variable. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRepositoryBuildNumber

> PipelineBuildNumber updateRepositoryBuildNumber(workspace, repoSlug, pipelineBuildNumber)

Update the next build number

Update the next build number that should be assigned to a pipeline. The next build number that will be configured has to be strictly higher than the current latest build number for this repository.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineBuildNumber = new BitbucketApi.PipelineBuildNumber(); // PipelineBuildNumber | The build number to update.
apiInstance.updateRepositoryBuildNumber(workspace, repoSlug, pipelineBuildNumber, (error, data, response) => {
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
 **pipelineBuildNumber** | [**PipelineBuildNumber**](PipelineBuildNumber.md)| The build number to update. | 

### Return type

[**PipelineBuildNumber**](PipelineBuildNumber.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRepositoryPipelineConfig

> PipelinesConfig updateRepositoryPipelineConfig(workspace, repoSlug, pipelinesConfig)

Update configuration

Update the pipelines configuration for a repository.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelinesConfig = new BitbucketApi.PipelinesConfig(); // PipelinesConfig | The updated repository pipelines configuration.
apiInstance.updateRepositoryPipelineConfig(workspace, repoSlug, pipelinesConfig, (error, data, response) => {
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
 **pipelinesConfig** | [**PipelinesConfig**](PipelinesConfig.md)| The updated repository pipelines configuration. | 

### Return type

[**PipelinesConfig**](PipelinesConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRepositoryPipelineKeyPair

> PipelineSshKeyPair updateRepositoryPipelineKeyPair(workspace, repoSlug, pipelineSshKeyPair)

Update SSH key pair

Create or update the repository SSH key pair. The private key will be set as a default SSH identity in your build container.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let pipelineSshKeyPair = new BitbucketApi.PipelineSshKeyPair(); // PipelineSshKeyPair | The created or updated SSH key pair.
apiInstance.updateRepositoryPipelineKeyPair(workspace, repoSlug, pipelineSshKeyPair, (error, data, response) => {
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
 **pipelineSshKeyPair** | [**PipelineSshKeyPair**](PipelineSshKeyPair.md)| The created or updated SSH key pair. | 

### Return type

[**PipelineSshKeyPair**](PipelineSshKeyPair.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRepositoryPipelineKnownHost

> PipelineKnownHost updateRepositoryPipelineKnownHost(workspace, repoSlug, knownHostUuid, pipelineKnownHost)

Update a known host

Update a repository level known host.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let knownHostUuid = "knownHostUuid_example"; // String | The UUID of the known host to update.
let pipelineKnownHost = new BitbucketApi.PipelineKnownHost(); // PipelineKnownHost | The updated known host.
apiInstance.updateRepositoryPipelineKnownHost(workspace, repoSlug, knownHostUuid, pipelineKnownHost, (error, data, response) => {
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
 **knownHostUuid** | **String**| The UUID of the known host to update. | 
 **pipelineKnownHost** | [**PipelineKnownHost**](PipelineKnownHost.md)| The updated known host. | 

### Return type

[**PipelineKnownHost**](PipelineKnownHost.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRepositoryPipelineSchedule

> PipelineSchedule updateRepositoryPipelineSchedule(workspace, repoSlug, scheduleUuid, pipelineSchedulePutRequestBody)

Update a schedule

Update a schedule.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let scheduleUuid = "scheduleUuid_example"; // String | The uuid of the schedule.
let pipelineSchedulePutRequestBody = new BitbucketApi.PipelineSchedulePutRequestBody(); // PipelineSchedulePutRequestBody | The schedule to update.
apiInstance.updateRepositoryPipelineSchedule(workspace, repoSlug, scheduleUuid, pipelineSchedulePutRequestBody, (error, data, response) => {
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
 **scheduleUuid** | **String**| The uuid of the schedule. | 
 **pipelineSchedulePutRequestBody** | [**PipelineSchedulePutRequestBody**](PipelineSchedulePutRequestBody.md)| The schedule to update. | 

### Return type

[**PipelineSchedule**](PipelineSchedule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRepositoryPipelineVariable

> PipelineVariable updateRepositoryPipelineVariable(workspace, repoSlug, variableUuid, pipelineVariable)

Update a variable for a repository

Update a repository level variable.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PipelinesApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let variableUuid = "variableUuid_example"; // String | The UUID of the variable to update.
let pipelineVariable = new BitbucketApi.PipelineVariable(); // PipelineVariable | The updated variable
apiInstance.updateRepositoryPipelineVariable(workspace, repoSlug, variableUuid, pipelineVariable, (error, data, response) => {
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
 **variableUuid** | **String**| The UUID of the variable to update. | 
 **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The updated variable | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

