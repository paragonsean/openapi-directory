# PipelinesApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeploymentVariable**](PipelinesApi.md#createDeploymentVariable) | **POST** /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables | Create a variable for an environment |
| [**createPipelineForRepository**](PipelinesApi.md#createPipelineForRepository) | **POST** /repositories/{workspace}/{repo_slug}/pipelines | Run a pipeline |
| [**createPipelineVariableForTeam**](PipelinesApi.md#createPipelineVariableForTeam) | **POST** /teams/{username}/pipelines_config/variables | Create a variable for a user |
| [**createPipelineVariableForUser**](PipelinesApi.md#createPipelineVariableForUser) | **POST** /users/{selected_user}/pipelines_config/variables | Create a variable for a user |
| [**createPipelineVariableForWorkspace**](PipelinesApi.md#createPipelineVariableForWorkspace) | **POST** /workspaces/{workspace}/pipelines-config/variables | Create a variable for a workspace |
| [**createRepositoryPipelineKnownHost**](PipelinesApi.md#createRepositoryPipelineKnownHost) | **POST** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts | Create a known host |
| [**createRepositoryPipelineSchedule**](PipelinesApi.md#createRepositoryPipelineSchedule) | **POST** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules | Create a schedule |
| [**createRepositoryPipelineVariable**](PipelinesApi.md#createRepositoryPipelineVariable) | **POST** /repositories/{workspace}/{repo_slug}/pipelines_config/variables | Create a variable for a repository |
| [**deleteDeploymentVariable**](PipelinesApi.md#deleteDeploymentVariable) | **DELETE** /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid} | Delete a variable for an environment |
| [**deletePipelineVariableForTeam**](PipelinesApi.md#deletePipelineVariableForTeam) | **DELETE** /teams/{username}/pipelines_config/variables/{variable_uuid} | Delete a variable for a team |
| [**deletePipelineVariableForUser**](PipelinesApi.md#deletePipelineVariableForUser) | **DELETE** /users/{selected_user}/pipelines_config/variables/{variable_uuid} | Delete a variable for a user |
| [**deletePipelineVariableForWorkspace**](PipelinesApi.md#deletePipelineVariableForWorkspace) | **DELETE** /workspaces/{workspace}/pipelines-config/variables/{variable_uuid} | Delete a variable for a workspace |
| [**deleteRepositoryPipelineCache**](PipelinesApi.md#deleteRepositoryPipelineCache) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid} | Delete a cache |
| [**deleteRepositoryPipelineCaches**](PipelinesApi.md#deleteRepositoryPipelineCaches) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines-config/caches | Delete caches |
| [**deleteRepositoryPipelineKeyPair**](PipelinesApi.md#deleteRepositoryPipelineKeyPair) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair | Delete SSH key pair |
| [**deleteRepositoryPipelineKnownHost**](PipelinesApi.md#deleteRepositoryPipelineKnownHost) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid} | Delete a known host |
| [**deleteRepositoryPipelineSchedule**](PipelinesApi.md#deleteRepositoryPipelineSchedule) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid} | Delete a schedule |
| [**deleteRepositoryPipelineVariable**](PipelinesApi.md#deleteRepositoryPipelineVariable) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid} | Delete a variable for a repository |
| [**getDeploymentVariables**](PipelinesApi.md#getDeploymentVariables) | **GET** /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables | List variables for an environment |
| [**getOIDCConfiguration**](PipelinesApi.md#getOIDCConfiguration) | **GET** /workspaces/{workspace}/pipelines-config/identity/oidc/.well-known/openid-configuration | Get OpenID configuration for OIDC in Pipelines |
| [**getOIDCKeys**](PipelinesApi.md#getOIDCKeys) | **GET** /workspaces/{workspace}/pipelines-config/identity/oidc/keys.json | Get keys for OIDC in Pipelines |
| [**getPipelineContainerLog**](PipelinesApi.md#getPipelineContainerLog) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid} | Get the logs for the build container or a service container for a given step of a pipeline. |
| [**getPipelineForRepository**](PipelinesApi.md#getPipelineForRepository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid} | Get a pipeline |
| [**getPipelineStepForRepository**](PipelinesApi.md#getPipelineStepForRepository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid} | Get a step of a pipeline |
| [**getPipelineStepLogForRepository**](PipelinesApi.md#getPipelineStepLogForRepository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log | Get log file for a step |
| [**getPipelineStepsForRepository**](PipelinesApi.md#getPipelineStepsForRepository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps | List steps for a pipeline |
| [**getPipelineTestReportTestCaseReasons**](PipelinesApi.md#getPipelineTestReportTestCaseReasons) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases/{test_case_uuid}/test_case_reasons | Get test case reasons (output) for a given test case in a step of a pipeline. |
| [**getPipelineTestReportTestCases**](PipelinesApi.md#getPipelineTestReportTestCases) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases | Get test cases for a given step of a pipeline. |
| [**getPipelineTestReports**](PipelinesApi.md#getPipelineTestReports) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports | Get a summary of test reports for a given step of a pipeline. |
| [**getPipelineVariableForTeam**](PipelinesApi.md#getPipelineVariableForTeam) | **GET** /teams/{username}/pipelines_config/variables/{variable_uuid} | Get a variable for a team |
| [**getPipelineVariableForUser**](PipelinesApi.md#getPipelineVariableForUser) | **GET** /users/{selected_user}/pipelines_config/variables/{variable_uuid} | Get a variable for a user |
| [**getPipelineVariableForWorkspace**](PipelinesApi.md#getPipelineVariableForWorkspace) | **GET** /workspaces/{workspace}/pipelines-config/variables/{variable_uuid} | Get variable for a workspace |
| [**getPipelineVariablesForTeam**](PipelinesApi.md#getPipelineVariablesForTeam) | **GET** /teams/{username}/pipelines_config/variables | List variables for an account |
| [**getPipelineVariablesForUser**](PipelinesApi.md#getPipelineVariablesForUser) | **GET** /users/{selected_user}/pipelines_config/variables | List variables for a user |
| [**getPipelineVariablesForWorkspace**](PipelinesApi.md#getPipelineVariablesForWorkspace) | **GET** /workspaces/{workspace}/pipelines-config/variables | List variables for a workspace |
| [**getPipelinesForRepository**](PipelinesApi.md#getPipelinesForRepository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines | List pipelines |
| [**getRepositoryPipelineCacheContentURI**](PipelinesApi.md#getRepositoryPipelineCacheContentURI) | **GET** /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}/content-uri | Get cache content URI |
| [**getRepositoryPipelineCaches**](PipelinesApi.md#getRepositoryPipelineCaches) | **GET** /repositories/{workspace}/{repo_slug}/pipelines-config/caches | List caches |
| [**getRepositoryPipelineConfig**](PipelinesApi.md#getRepositoryPipelineConfig) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config | Get configuration |
| [**getRepositoryPipelineKnownHost**](PipelinesApi.md#getRepositoryPipelineKnownHost) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid} | Get a known host |
| [**getRepositoryPipelineKnownHosts**](PipelinesApi.md#getRepositoryPipelineKnownHosts) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts | List known hosts |
| [**getRepositoryPipelineSchedule**](PipelinesApi.md#getRepositoryPipelineSchedule) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid} | Get a schedule |
| [**getRepositoryPipelineScheduleExecutions**](PipelinesApi.md#getRepositoryPipelineScheduleExecutions) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}/executions | List executions of a schedule |
| [**getRepositoryPipelineSchedules**](PipelinesApi.md#getRepositoryPipelineSchedules) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules | List schedules |
| [**getRepositoryPipelineSshKeyPair**](PipelinesApi.md#getRepositoryPipelineSshKeyPair) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair | Get SSH key pair |
| [**getRepositoryPipelineVariable**](PipelinesApi.md#getRepositoryPipelineVariable) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid} | Get a variable for a repository |
| [**getRepositoryPipelineVariables**](PipelinesApi.md#getRepositoryPipelineVariables) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/variables | List variables for a repository |
| [**stopPipeline**](PipelinesApi.md#stopPipeline) | **POST** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline | Stop a pipeline |
| [**updateDeploymentVariable**](PipelinesApi.md#updateDeploymentVariable) | **PUT** /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid} | Update a variable for an environment |
| [**updatePipelineVariableForTeam**](PipelinesApi.md#updatePipelineVariableForTeam) | **PUT** /teams/{username}/pipelines_config/variables/{variable_uuid} | Update a variable for a team |
| [**updatePipelineVariableForUser**](PipelinesApi.md#updatePipelineVariableForUser) | **PUT** /users/{selected_user}/pipelines_config/variables/{variable_uuid} | Update a variable for a user |
| [**updatePipelineVariableForWorkspace**](PipelinesApi.md#updatePipelineVariableForWorkspace) | **PUT** /workspaces/{workspace}/pipelines-config/variables/{variable_uuid} | Update variable for a workspace |
| [**updateRepositoryBuildNumber**](PipelinesApi.md#updateRepositoryBuildNumber) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/build_number | Update the next build number |
| [**updateRepositoryPipelineConfig**](PipelinesApi.md#updateRepositoryPipelineConfig) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config | Update configuration |
| [**updateRepositoryPipelineKeyPair**](PipelinesApi.md#updateRepositoryPipelineKeyPair) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair | Update SSH key pair |
| [**updateRepositoryPipelineKnownHost**](PipelinesApi.md#updateRepositoryPipelineKnownHost) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid} | Update a known host |
| [**updateRepositoryPipelineSchedule**](PipelinesApi.md#updateRepositoryPipelineSchedule) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid} | Update a schedule |
| [**updateRepositoryPipelineVariable**](PipelinesApi.md#updateRepositoryPipelineVariable) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid} | Update a variable for a repository |


<a id="createDeploymentVariable"></a>
# **createDeploymentVariable**
> DeploymentVariable createDeploymentVariable(workspace, repoSlug, environmentUuid, deploymentVariable)

Create a variable for an environment

Create a deployment environment level variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String environmentUuid = "environmentUuid_example"; // String | The environment.
    DeploymentVariable deploymentVariable = new DeploymentVariable(); // DeploymentVariable | The variable to create
    try {
      DeploymentVariable result = apiInstance.createDeploymentVariable(workspace, repoSlug, environmentUuid, deploymentVariable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#createDeploymentVariable");
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
| **environmentUuid** | **String**| The environment. | |
| **deploymentVariable** | [**DeploymentVariable**](DeploymentVariable.md)| The variable to create | |

### Return type

[**DeploymentVariable**](DeploymentVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The variable was created. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **404** | The account, repository, environment or variable with the given UUID was not found. |  -  |
| **409** | A variable with the provided key already exists. |  -  |

<a id="createPipelineForRepository"></a>
# **createPipelineForRepository**
> Pipeline createPipelineForRepository(workspace, repoSlug, pipeline)

Run a pipeline

Endpoint to create and initiate a pipeline. There are a couple of different options to initiate a pipeline, where the payload of the request will determine which type of pipeline will be instantiated. # Trigger a Pipeline for a branch One way to trigger pipelines is by specifying the branch for which you want to trigger a pipeline. The specified branch will be used to determine which pipeline definition from the &#x60;bitbucket-pipelines.yml&#x60; file will be applied to initiate the pipeline. The pipeline will then do a clone of the repository and checkout the latest revision of the specified branch.  ### Example  &#x60;&#x60;&#x60; $ curl -X POST -is -u username:password \\   -H &#39;Content-Type: application/json&#39; \\  https://api.bitbucket.org/2.0/repositories/jeroendr/meat-demo2/pipelines/ \\   -d &#39;   {     \&quot;target\&quot;: {       \&quot;ref_type\&quot;: \&quot;branch\&quot;,       \&quot;type\&quot;: \&quot;pipeline_ref_target\&quot;,       \&quot;ref_name\&quot;: \&quot;master\&quot;     }   }&#39; &#x60;&#x60;&#x60; # Trigger a Pipeline for a commit on a branch or tag You can initiate a pipeline for a specific commit and in the context of a specified reference (e.g. a branch, tag or bookmark). The specified reference will be used to determine which pipeline definition from the bitbucket-pipelines.yml file will be applied to initiate the pipeline. The pipeline will clone the repository and then do a checkout the specified reference.  The following reference types are supported:  * &#x60;branch&#x60; * &#x60;named_branch&#x60; * &#x60;bookmark&#x60;  * &#x60;tag&#x60;  ### Example  &#x60;&#x60;&#x60; $ curl -X POST -is -u username:password \\   -H &#39;Content-Type: application/json&#39; \\   https://api.bitbucket.org/2.0/repositories/jeroendr/meat-demo2/pipelines/ \\   -d &#39;   {     \&quot;target\&quot;: {       \&quot;commit\&quot;: {         \&quot;type\&quot;: \&quot;commit\&quot;,         \&quot;hash\&quot;: \&quot;ce5b7431602f7cbba007062eeb55225c6e18e956\&quot;       },       \&quot;ref_type\&quot;: \&quot;branch\&quot;,       \&quot;type\&quot;: \&quot;pipeline_ref_target\&quot;,       \&quot;ref_name\&quot;: \&quot;master\&quot;     }   }&#39; &#x60;&#x60;&#x60; # Trigger a specific pipeline definition for a commit You can trigger a specific pipeline that is defined in your &#x60;bitbucket-pipelines.yml&#x60; file for a specific commit. In addition to the commit revision, you specify the type and pattern of the selector that identifies the pipeline definition. The resulting pipeline will then clone the repository and checkout the specified revision.  ### Example  &#x60;&#x60;&#x60; $ curl -X POST -is -u username:password \\   -H &#39;Content-Type: application/json&#39; \\  https://api.bitbucket.org/2.0/repositories/jeroendr/meat-demo2/pipelines/ \\  -d &#39;   {      \&quot;target\&quot;: {       \&quot;commit\&quot;: {          \&quot;hash\&quot;:\&quot;a3c4e02c9a3755eccdc3764e6ea13facdf30f923\&quot;,          \&quot;type\&quot;:\&quot;commit\&quot;        },         \&quot;selector\&quot;: {            \&quot;type\&quot;:\&quot;custom\&quot;,               \&quot;pattern\&quot;:\&quot;Deploy to production\&quot;           },         \&quot;type\&quot;:\&quot;pipeline_commit_target\&quot;    }   }&#39; &#x60;&#x60;&#x60; # Trigger a specific pipeline definition for a commit on a branch or tag You can trigger a specific pipeline that is defined in your &#x60;bitbucket-pipelines.yml&#x60; file for a specific commit in the context of a specified reference. In addition to the commit revision, you specify the type and pattern of the selector that identifies the pipeline definition, as well as the reference information. The resulting pipeline will then clone the repository a checkout the specified reference.  ### Example  &#x60;&#x60;&#x60; $ curl -X POST -is -u username:password \\   -H &#39;Content-Type: application/json&#39; \\  https://api.bitbucket.org/2.0/repositories/jeroendr/meat-demo2/pipelines/ \\  -d &#39;   {      \&quot;target\&quot;: {       \&quot;commit\&quot;: {          \&quot;hash\&quot;:\&quot;a3c4e02c9a3755eccdc3764e6ea13facdf30f923\&quot;,          \&quot;type\&quot;:\&quot;commit\&quot;        },        \&quot;selector\&quot;: {           \&quot;type\&quot;: \&quot;custom\&quot;,           \&quot;pattern\&quot;: \&quot;Deploy to production\&quot;        },        \&quot;type\&quot;: \&quot;pipeline_ref_target\&quot;,        \&quot;ref_name\&quot;: \&quot;master\&quot;,        \&quot;ref_type\&quot;: \&quot;branch\&quot;      }   }&#39; &#x60;&#x60;&#x60;   # Trigger a custom pipeline with variables In addition to triggering a custom pipeline that is defined in your &#x60;bitbucket-pipelines.yml&#x60; file as shown in the examples above, you can specify variables that will be available for your build. In the request, provide a list of variables, specifying the following for each variable: key, value, and whether it should be secured or not (this field is optional and defaults to not secured).  ### Example  &#x60;&#x60;&#x60; $ curl -X POST -is -u username:password \\   -H &#39;Content-Type: application/json&#39; \\  https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \\  -d &#39;   {     \&quot;target\&quot;: {       \&quot;type\&quot;: \&quot;pipeline_ref_target\&quot;,       \&quot;ref_type\&quot;: \&quot;branch\&quot;,       \&quot;ref_name\&quot;: \&quot;master\&quot;,       \&quot;selector\&quot;: {         \&quot;type\&quot;: \&quot;custom\&quot;,         \&quot;pattern\&quot;: \&quot;Deploy to production\&quot;       }     },     \&quot;variables\&quot;: [       {         \&quot;key\&quot;: \&quot;var1key\&quot;,         \&quot;value\&quot;: \&quot;var1value\&quot;,         \&quot;secured\&quot;: true       },       {         \&quot;key\&quot;: \&quot;var2key\&quot;,         \&quot;value\&quot;: \&quot;var2value\&quot;       }     ]   }&#39; &#x60;&#x60;&#x60;  # Trigger a pull request pipeline  You can also initiate a pipeline for a specific pull request.  ### Example  &#x60;&#x60;&#x60; $ curl -X POST -is -u username:password \\   -H &#39;Content-Type: application/json&#39; \\  https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \\  -d &#39;   {  \&quot;target\&quot;: {       \&quot;type\&quot;: \&quot;pipeline_pullrequest_target\&quot;,    \&quot;source\&quot;: \&quot;pull-request-branch\&quot;,       \&quot;destination\&quot;: \&quot;master\&quot;,       \&quot;destination_commit\&quot;: {         \&quot;hash\&quot; : \&quot;9f848b7\&quot;       },       \&quot;commit\&quot;: {        \&quot;hash\&quot; : \&quot;1a372fc\&quot;       },       \&quot;pullrequest\&quot; : {        \&quot;id\&quot; : \&quot;3\&quot;       },    \&quot;selector\&quot;: {         \&quot;type\&quot;: \&quot;pull-requests\&quot;,         \&quot;pattern\&quot;: \&quot;**\&quot;       }     }   }&#39; &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    Pipeline pipeline = new Pipeline(); // Pipeline | The pipeline to initiate.
    try {
      Pipeline result = apiInstance.createPipelineForRepository(workspace, repoSlug, pipeline);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#createPipelineForRepository");
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
| **pipeline** | [**Pipeline**](Pipeline.md)| The pipeline to initiate. | |

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The initiated pipeline. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **400** | The account or repository is not enabled, the yml file does not exist in the repository for the given revision, or the request body contained invalid properties. |  -  |
| **404** | The account or repository was not found. |  -  |

<a id="createPipelineVariableForTeam"></a>
# **createPipelineVariableForTeam**
> PipelineVariable createPipelineVariableForTeam(username, pipelineVariable)

Create a variable for a user

Create an account level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String username = "username_example"; // String | The account.
    PipelineVariable pipelineVariable = new PipelineVariable(); // PipelineVariable | The variable to create.
    try {
      PipelineVariable result = apiInstance.createPipelineVariableForTeam(username, pipelineVariable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#createPipelineVariableForTeam");
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
| **username** | **String**| The account. | |
| **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The variable to create. | [optional] |

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created variable. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **404** | The account does not exist. |  -  |
| **409** | A variable with the provided key already exists. |  -  |

<a id="createPipelineVariableForUser"></a>
# **createPipelineVariableForUser**
> PipelineVariable createPipelineVariableForUser(selectedUser, pipelineVariable)

Create a variable for a user

Create a user level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
    PipelineVariable pipelineVariable = new PipelineVariable(); // PipelineVariable | The variable to create.
    try {
      PipelineVariable result = apiInstance.createPipelineVariableForUser(selectedUser, pipelineVariable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#createPipelineVariableForUser");
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
| **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | |
| **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The variable to create. | [optional] |

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created variable. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **404** | The account does not exist. |  -  |
| **409** | A variable with the provided key already exists. |  -  |

<a id="createPipelineVariableForWorkspace"></a>
# **createPipelineVariableForWorkspace**
> PipelineVariable createPipelineVariableForWorkspace(workspace, pipelineVariable)

Create a variable for a workspace

Create a workspace level variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    PipelineVariable pipelineVariable = new PipelineVariable(); // PipelineVariable | The variable to create.
    try {
      PipelineVariable result = apiInstance.createPipelineVariableForWorkspace(workspace, pipelineVariable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#createPipelineVariableForWorkspace");
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
| **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The variable to create. | [optional] |

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created variable. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **404** | The workspace does not exist. |  -  |
| **409** | A variable with the provided key already exists. |  -  |

<a id="createRepositoryPipelineKnownHost"></a>
# **createRepositoryPipelineKnownHost**
> PipelineKnownHost createRepositoryPipelineKnownHost(workspace, repoSlug, pipelineKnownHost)

Create a known host

Create a repository level known host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    PipelineKnownHost pipelineKnownHost = new PipelineKnownHost(); // PipelineKnownHost | The known host to create.
    try {
      PipelineKnownHost result = apiInstance.createRepositoryPipelineKnownHost(workspace, repoSlug, pipelineKnownHost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#createRepositoryPipelineKnownHost");
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
| **pipelineKnownHost** | [**PipelineKnownHost**](PipelineKnownHost.md)| The known host to create. | |

### Return type

[**PipelineKnownHost**](PipelineKnownHost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The known host was created. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **404** | The account or repository does not exist. |  -  |
| **409** | A known host with the provided hostname already exists. |  -  |

<a id="createRepositoryPipelineSchedule"></a>
# **createRepositoryPipelineSchedule**
> PipelineSchedule createRepositoryPipelineSchedule(workspace, repoSlug, pipelineSchedulePostRequestBody)

Create a schedule

Create a schedule for the given repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    PipelineSchedulePostRequestBody pipelineSchedulePostRequestBody = new PipelineSchedulePostRequestBody(); // PipelineSchedulePostRequestBody | The schedule to create.
    try {
      PipelineSchedule result = apiInstance.createRepositoryPipelineSchedule(workspace, repoSlug, pipelineSchedulePostRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#createRepositoryPipelineSchedule");
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
| **pipelineSchedulePostRequestBody** | [**PipelineSchedulePostRequestBody**](PipelineSchedulePostRequestBody.md)| The schedule to create. | |

### Return type

[**PipelineSchedule**](PipelineSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created schedule. |  -  |
| **400** | There were errors validating the request. |  -  |
| **401** | The maximum limit of schedules for this repository was reached. |  -  |
| **404** | The account or repository was not found. |  -  |

<a id="createRepositoryPipelineVariable"></a>
# **createRepositoryPipelineVariable**
> PipelineVariable createRepositoryPipelineVariable(workspace, repoSlug, pipelineVariable)

Create a variable for a repository

Create a repository level variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    PipelineVariable pipelineVariable = new PipelineVariable(); // PipelineVariable | The variable to create.
    try {
      PipelineVariable result = apiInstance.createRepositoryPipelineVariable(workspace, repoSlug, pipelineVariable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#createRepositoryPipelineVariable");
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
| **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The variable to create. | |

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The variable was created. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **404** | The account or repository does not exist. |  -  |
| **409** | A variable with the provided key already exists. |  -  |

<a id="deleteDeploymentVariable"></a>
# **deleteDeploymentVariable**
> deleteDeploymentVariable(workspace, repoSlug, environmentUuid, variableUuid)

Delete a variable for an environment

Delete a deployment environment level variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String environmentUuid = "environmentUuid_example"; // String | The environment.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable to delete.
    try {
      apiInstance.deleteDeploymentVariable(workspace, repoSlug, environmentUuid, variableUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#deleteDeploymentVariable");
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
| **environmentUuid** | **String**| The environment. | |
| **variableUuid** | **String**| The UUID of the variable to delete. | |

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
| **204** | The variable was deleted. |  -  |
| **404** | The account, repository, environment or variable with given UUID was not found. |  -  |

<a id="deletePipelineVariableForTeam"></a>
# **deletePipelineVariableForTeam**
> deletePipelineVariableForTeam(username, variableUuid)

Delete a variable for a team

Delete a team level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String username = "username_example"; // String | The account.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable to delete.
    try {
      apiInstance.deletePipelineVariableForTeam(username, variableUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#deletePipelineVariableForTeam");
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
| **username** | **String**| The account. | |
| **variableUuid** | **String**| The UUID of the variable to delete. | |

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
| **204** | The variable was deleted |  -  |
| **404** | The account or the variable with the provided UUID does not exist. |  -  |

<a id="deletePipelineVariableForUser"></a>
# **deletePipelineVariableForUser**
> deletePipelineVariableForUser(selectedUser, variableUuid)

Delete a variable for a user

Delete an account level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable to delete.
    try {
      apiInstance.deletePipelineVariableForUser(selectedUser, variableUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#deletePipelineVariableForUser");
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
| **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | |
| **variableUuid** | **String**| The UUID of the variable to delete. | |

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
| **204** | The variable was deleted |  -  |
| **404** | The account or the variable with the provided UUID does not exist. |  -  |

<a id="deletePipelineVariableForWorkspace"></a>
# **deletePipelineVariableForWorkspace**
> deletePipelineVariableForWorkspace(workspace, variableUuid)

Delete a variable for a workspace

Delete a workspace level variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable to delete.
    try {
      apiInstance.deletePipelineVariableForWorkspace(workspace, variableUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#deletePipelineVariableForWorkspace");
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
| **variableUuid** | **String**| The UUID of the variable to delete. | |

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
| **204** | The variable was deleted |  -  |
| **404** | The workspace or the variable with the provided UUID does not exist. |  -  |

<a id="deleteRepositoryPipelineCache"></a>
# **deleteRepositoryPipelineCache**
> deleteRepositoryPipelineCache(workspace, repoSlug, cacheUuid)

Delete a cache

Delete a repository cache.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | The account.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String cacheUuid = "cacheUuid_example"; // String | The UUID of the cache to delete.
    try {
      apiInstance.deleteRepositoryPipelineCache(workspace, repoSlug, cacheUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#deleteRepositoryPipelineCache");
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
| **workspace** | **String**| The account. | |
| **repoSlug** | **String**| The repository. | |
| **cacheUuid** | **String**| The UUID of the cache to delete. | |

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
| **204** | The cache was deleted. |  -  |
| **404** | The workspace, repository or cache_uuid with given UUID was not found. |  -  |

<a id="deleteRepositoryPipelineCaches"></a>
# **deleteRepositoryPipelineCaches**
> deleteRepositoryPipelineCaches(workspace, repoSlug, name)

Delete caches

Delete repository cache versions by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | The account.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String name = "name_example"; // String | The cache name.
    try {
      apiInstance.deleteRepositoryPipelineCaches(workspace, repoSlug, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#deleteRepositoryPipelineCaches");
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
| **workspace** | **String**| The account. | |
| **repoSlug** | **String**| The repository. | |
| **name** | **String**| The cache name. | |

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
| **204** | The caches were deleted. |  -  |
| **404** | The workspace, repository or cache name was not found. |  -  |

<a id="deleteRepositoryPipelineKeyPair"></a>
# **deleteRepositoryPipelineKeyPair**
> deleteRepositoryPipelineKeyPair(workspace, repoSlug)

Delete SSH key pair

Delete the repository SSH key pair.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    try {
      apiInstance.deleteRepositoryPipelineKeyPair(workspace, repoSlug);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#deleteRepositoryPipelineKeyPair");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The SSH key pair was deleted. |  -  |
| **404** | The account, repository or SSH key pair was not found. |  -  |

<a id="deleteRepositoryPipelineKnownHost"></a>
# **deleteRepositoryPipelineKnownHost**
> deleteRepositoryPipelineKnownHost(workspace, repoSlug, knownHostUuid)

Delete a known host

Delete a repository level known host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String knownHostUuid = "knownHostUuid_example"; // String | The UUID of the known host to delete.
    try {
      apiInstance.deleteRepositoryPipelineKnownHost(workspace, repoSlug, knownHostUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#deleteRepositoryPipelineKnownHost");
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
| **knownHostUuid** | **String**| The UUID of the known host to delete. | |

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
| **204** | The known host was deleted. |  -  |
| **404** | The account, repository or known host with given UUID was not found. |  -  |

<a id="deleteRepositoryPipelineSchedule"></a>
# **deleteRepositoryPipelineSchedule**
> deleteRepositoryPipelineSchedule(workspace, repoSlug, scheduleUuid)

Delete a schedule

Delete a schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String scheduleUuid = "scheduleUuid_example"; // String | The uuid of the schedule.
    try {
      apiInstance.deleteRepositoryPipelineSchedule(workspace, repoSlug, scheduleUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#deleteRepositoryPipelineSchedule");
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
| **scheduleUuid** | **String**| The uuid of the schedule. | |

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
| **204** | The schedule was deleted. |  -  |
| **404** | The account, repository or schedule was not found. |  -  |

<a id="deleteRepositoryPipelineVariable"></a>
# **deleteRepositoryPipelineVariable**
> deleteRepositoryPipelineVariable(workspace, repoSlug, variableUuid)

Delete a variable for a repository

Delete a repository level variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable to delete.
    try {
      apiInstance.deleteRepositoryPipelineVariable(workspace, repoSlug, variableUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#deleteRepositoryPipelineVariable");
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
| **variableUuid** | **String**| The UUID of the variable to delete. | |

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
| **204** | The variable was deleted. |  -  |
| **404** | The account, repository or variable with given UUID was not found. |  -  |

<a id="getDeploymentVariables"></a>
# **getDeploymentVariables**
> PaginatedDeploymentVariable getDeploymentVariables(workspace, repoSlug, environmentUuid)

List variables for an environment

Find deployment environment level variables.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String environmentUuid = "environmentUuid_example"; // String | The environment.
    try {
      PaginatedDeploymentVariable result = apiInstance.getDeploymentVariables(workspace, repoSlug, environmentUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getDeploymentVariables");
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
| **environmentUuid** | **String**| The environment. | |

### Return type

[**PaginatedDeploymentVariable**](PaginatedDeploymentVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved deployment variables. |  -  |

<a id="getOIDCConfiguration"></a>
# **getOIDCConfiguration**
> getOIDCConfiguration(workspace)

Get OpenID configuration for OIDC in Pipelines

This is part of OpenID Connect for Pipelines, see https://support.atlassian.com/bitbucket-cloud/docs/integrate-pipelines-with-resource-servers-using-oidc/

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    try {
      apiInstance.getOIDCConfiguration(workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getOIDCConfiguration");
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
| **200** | The OpenID configuration |  -  |
| **404** | The workspace was not found. |  -  |

<a id="getOIDCKeys"></a>
# **getOIDCKeys**
> getOIDCKeys(workspace)

Get keys for OIDC in Pipelines

This is part of OpenID Connect for Pipelines, see https://support.atlassian.com/bitbucket-cloud/docs/integrate-pipelines-with-resource-servers-using-oidc/

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    try {
      apiInstance.getOIDCKeys(workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getOIDCKeys");
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
| **200** | The keys in JSON web key format |  -  |
| **404** | The workspace was not found. |  -  |

<a id="getPipelineContainerLog"></a>
# **getPipelineContainerLog**
> getPipelineContainerLog(workspace, repoSlug, pipelineUuid, stepUuid, logUuid)

Get the logs for the build container or a service container for a given step of a pipeline.

Retrieve the log file for a build container or service container.  This endpoint supports (and encourages!) the use of [HTTP Range requests](https://tools.ietf.org/html/rfc7233) to deal with potentially very large log files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
    String stepUuid = "stepUuid_example"; // String | The UUID of the step.
    String logUuid = "logUuid_example"; // String | For the main build container specify the step UUID; for a service container specify the service container UUID
    try {
      apiInstance.getPipelineContainerLog(workspace, repoSlug, pipelineUuid, stepUuid, logUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineContainerLog");
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
| **pipelineUuid** | **String**| The UUID of the pipeline. | |
| **stepUuid** | **String**| The UUID of the step. | |
| **logUuid** | **String**| For the main build container specify the step UUID; for a service container specify the service container UUID | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The raw log file for the build container or service container. |  -  |
| **404** | No account, repository, pipeline, step or log exist for the provided path. |  -  |

<a id="getPipelineForRepository"></a>
# **getPipelineForRepository**
> Pipeline getPipelineForRepository(workspace, repoSlug, pipelineUuid)

Get a pipeline

Retrieve a specified pipeline

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String pipelineUuid = "pipelineUuid_example"; // String | The pipeline UUID.
    try {
      Pipeline result = apiInstance.getPipelineForRepository(workspace, repoSlug, pipelineUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineForRepository");
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
| **pipelineUuid** | **String**| The pipeline UUID. | |

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pipeline. |  -  |
| **404** | No account, repository or pipeline with the UUID provided exists. |  -  |

<a id="getPipelineStepForRepository"></a>
# **getPipelineStepForRepository**
> PipelineStep getPipelineStepForRepository(workspace, repoSlug, pipelineUuid, stepUuid)

Get a step of a pipeline

Retrieve a given step of a pipeline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
    String stepUuid = "stepUuid_example"; // String | The UUID of the step.
    try {
      PipelineStep result = apiInstance.getPipelineStepForRepository(workspace, repoSlug, pipelineUuid, stepUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineStepForRepository");
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
| **pipelineUuid** | **String**| The UUID of the pipeline. | |
| **stepUuid** | **String**| The UUID of the step. | |

### Return type

[**PipelineStep**](PipelineStep.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The step. |  -  |
| **404** | No account, repository, pipeline or step with the UUID provided exists for the pipeline with the UUID provided. |  -  |

<a id="getPipelineStepLogForRepository"></a>
# **getPipelineStepLogForRepository**
> getPipelineStepLogForRepository(workspace, repoSlug, pipelineUuid, stepUuid)

Get log file for a step

Retrieve the log file for a given step of a pipeline.  This endpoint supports (and encourages!) the use of [HTTP Range requests](https://tools.ietf.org/html/rfc7233) to deal with potentially very large log files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
    String stepUuid = "stepUuid_example"; // String | The UUID of the step.
    try {
      apiInstance.getPipelineStepLogForRepository(workspace, repoSlug, pipelineUuid, stepUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineStepLogForRepository");
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
| **pipelineUuid** | **String**| The UUID of the pipeline. | |
| **stepUuid** | **String**| The UUID of the step. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The raw log file for this pipeline step. |  -  |
| **304** | The log has the same etag as the provided If-None-Match header. |  -  |
| **404** | A pipeline with the given UUID does not exist, a step with the given UUID does not exist in the pipeline or a log file does not exist for the given step. |  -  |
| **416** | The requested range does not exist for requests that specified the [HTTP Range header](https://tools.ietf.org/html/rfc7233#section-3.1). |  -  |

<a id="getPipelineStepsForRepository"></a>
# **getPipelineStepsForRepository**
> PaginatedPipelineSteps getPipelineStepsForRepository(workspace, repoSlug, pipelineUuid)

List steps for a pipeline

Find steps for the given pipeline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
    try {
      PaginatedPipelineSteps result = apiInstance.getPipelineStepsForRepository(workspace, repoSlug, pipelineUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineStepsForRepository");
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
| **pipelineUuid** | **String**| The UUID of the pipeline. | |

### Return type

[**PaginatedPipelineSteps**](PaginatedPipelineSteps.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The steps. |  -  |

<a id="getPipelineTestReportTestCaseReasons"></a>
# **getPipelineTestReportTestCaseReasons**
> getPipelineTestReportTestCaseReasons(workspace, repoSlug, pipelineUuid, stepUuid, testCaseUuid)

Get test case reasons (output) for a given test case in a step of a pipeline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
    String stepUuid = "stepUuid_example"; // String | The UUID of the step.
    String testCaseUuid = "testCaseUuid_example"; // String | The UUID of the test case.
    try {
      apiInstance.getPipelineTestReportTestCaseReasons(workspace, repoSlug, pipelineUuid, stepUuid, testCaseUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineTestReportTestCaseReasons");
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
| **pipelineUuid** | **String**| The UUID of the pipeline. | |
| **stepUuid** | **String**| The UUID of the step. | |
| **testCaseUuid** | **String**| The UUID of the test case. | |

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
| **200** | Test case reasons (output). |  -  |
| **404** | No account, repository, pipeline, step or test case with the UUID provided exists for the pipeline with the UUID provided. |  -  |

<a id="getPipelineTestReportTestCases"></a>
# **getPipelineTestReportTestCases**
> getPipelineTestReportTestCases(workspace, repoSlug, pipelineUuid, stepUuid)

Get test cases for a given step of a pipeline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
    String stepUuid = "stepUuid_example"; // String | The UUID of the step.
    try {
      apiInstance.getPipelineTestReportTestCases(workspace, repoSlug, pipelineUuid, stepUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineTestReportTestCases");
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
| **pipelineUuid** | **String**| The UUID of the pipeline. | |
| **stepUuid** | **String**| The UUID of the step. | |

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
| **200** | Test cases for this pipeline step. |  -  |
| **404** | No account, repository, pipeline, step or test reports exist for the provided path. |  -  |

<a id="getPipelineTestReports"></a>
# **getPipelineTestReports**
> getPipelineTestReports(workspace, repoSlug, pipelineUuid, stepUuid)

Get a summary of test reports for a given step of a pipeline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
    String stepUuid = "stepUuid_example"; // String | The UUID of the step.
    try {
      apiInstance.getPipelineTestReports(workspace, repoSlug, pipelineUuid, stepUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineTestReports");
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
| **pipelineUuid** | **String**| The UUID of the pipeline. | |
| **stepUuid** | **String**| The UUID of the step. | |

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
| **200** | A summary of test reports for this pipeline step. |  -  |
| **404** | No account, repository, pipeline, step or test reports exist for the provided path. |  -  |

<a id="getPipelineVariableForTeam"></a>
# **getPipelineVariableForTeam**
> PipelineVariable getPipelineVariableForTeam(username, variableUuid)

Get a variable for a team

Retrieve a team level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String username = "username_example"; // String | The account.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable to retrieve.
    try {
      PipelineVariable result = apiInstance.getPipelineVariableForTeam(username, variableUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineVariableForTeam");
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
| **username** | **String**| The account. | |
| **variableUuid** | **String**| The UUID of the variable to retrieve. | |

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The variable. |  -  |
| **404** | The account or variable with the given UUID was not found. |  -  |

<a id="getPipelineVariableForUser"></a>
# **getPipelineVariableForUser**
> PipelineVariable getPipelineVariableForUser(selectedUser, variableUuid)

Get a variable for a user

Retrieve a user level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable to retrieve.
    try {
      PipelineVariable result = apiInstance.getPipelineVariableForUser(selectedUser, variableUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineVariableForUser");
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
| **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | |
| **variableUuid** | **String**| The UUID of the variable to retrieve. | |

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The variable. |  -  |
| **404** | The account or variable with the given UUID was not found. |  -  |

<a id="getPipelineVariableForWorkspace"></a>
# **getPipelineVariableForWorkspace**
> PipelineVariable getPipelineVariableForWorkspace(workspace, variableUuid)

Get variable for a workspace

Retrieve a workspace level variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable to retrieve.
    try {
      PipelineVariable result = apiInstance.getPipelineVariableForWorkspace(workspace, variableUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineVariableForWorkspace");
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
| **variableUuid** | **String**| The UUID of the variable to retrieve. | |

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The variable. |  -  |
| **404** | The workspace or variable with the given UUID was not found. |  -  |

<a id="getPipelineVariablesForTeam"></a>
# **getPipelineVariablesForTeam**
> PaginatedPipelineVariables getPipelineVariablesForTeam(username)

List variables for an account

Find account level variables. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String username = "username_example"; // String | The account.
    try {
      PaginatedPipelineVariables result = apiInstance.getPipelineVariablesForTeam(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineVariablesForTeam");
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
| **username** | **String**| The account. | |

### Return type

[**PaginatedPipelineVariables**](PaginatedPipelineVariables.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The found account level variables. |  -  |

<a id="getPipelineVariablesForUser"></a>
# **getPipelineVariablesForUser**
> PaginatedPipelineVariables getPipelineVariablesForUser(selectedUser)

List variables for a user

Find user level variables. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
    try {
      PaginatedPipelineVariables result = apiInstance.getPipelineVariablesForUser(selectedUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineVariablesForUser");
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
| **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | |

### Return type

[**PaginatedPipelineVariables**](PaginatedPipelineVariables.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The found user level variables. |  -  |

<a id="getPipelineVariablesForWorkspace"></a>
# **getPipelineVariablesForWorkspace**
> PaginatedPipelineVariables getPipelineVariablesForWorkspace(workspace)

List variables for a workspace

Find workspace level variables.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    try {
      PaginatedPipelineVariables result = apiInstance.getPipelineVariablesForWorkspace(workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelineVariablesForWorkspace");
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

### Return type

[**PaginatedPipelineVariables**](PaginatedPipelineVariables.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The found workspace level variables. |  -  |

<a id="getPipelinesForRepository"></a>
# **getPipelinesForRepository**
> PaginatedPipelines getPipelinesForRepository(workspace, repoSlug)

List pipelines

Find pipelines

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    try {
      PaginatedPipelines result = apiInstance.getPipelinesForRepository(workspace, repoSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getPipelinesForRepository");
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

[**PaginatedPipelines**](PaginatedPipelines.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The matching pipelines. |  -  |

<a id="getRepositoryPipelineCacheContentURI"></a>
# **getRepositoryPipelineCacheContentURI**
> PipelineCacheContentUri getRepositoryPipelineCacheContentURI(workspace, repoSlug, cacheUuid)

Get cache content URI

Retrieve the URI of the content of the specified cache.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | The account.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String cacheUuid = "cacheUuid_example"; // String | The UUID of the cache.
    try {
      PipelineCacheContentUri result = apiInstance.getRepositoryPipelineCacheContentURI(workspace, repoSlug, cacheUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getRepositoryPipelineCacheContentURI");
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
| **workspace** | **String**| The account. | |
| **repoSlug** | **String**| The repository. | |
| **cacheUuid** | **String**| The UUID of the cache. | |

### Return type

[**PipelineCacheContentUri**](PipelineCacheContentUri.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cache content uri. |  -  |
| **404** | The workspace, repository or cache_uuid with given UUID was not found. |  -  |

<a id="getRepositoryPipelineCaches"></a>
# **getRepositoryPipelineCaches**
> PaginatedPipelineCaches getRepositoryPipelineCaches(workspace, repoSlug)

List caches

Retrieve the repository pipelines caches.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | The account.
    String repoSlug = "repoSlug_example"; // String | The repository.
    try {
      PaginatedPipelineCaches result = apiInstance.getRepositoryPipelineCaches(workspace, repoSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getRepositoryPipelineCaches");
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
| **workspace** | **String**| The account. | |
| **repoSlug** | **String**| The repository. | |

### Return type

[**PaginatedPipelineCaches**](PaginatedPipelineCaches.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of caches for the given repository. |  -  |
| **404** | The account or repository was not found. |  -  |

<a id="getRepositoryPipelineConfig"></a>
# **getRepositoryPipelineConfig**
> PipelinesConfig getRepositoryPipelineConfig(workspace, repoSlug)

Get configuration

Retrieve the repository pipelines configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | The account.
    String repoSlug = "repoSlug_example"; // String | The repository.
    try {
      PipelinesConfig result = apiInstance.getRepositoryPipelineConfig(workspace, repoSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getRepositoryPipelineConfig");
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
| **workspace** | **String**| The account. | |
| **repoSlug** | **String**| The repository. | |

### Return type

[**PipelinesConfig**](PipelinesConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The repository pipelines configuration. |  -  |

<a id="getRepositoryPipelineKnownHost"></a>
# **getRepositoryPipelineKnownHost**
> PipelineKnownHost getRepositoryPipelineKnownHost(workspace, repoSlug, knownHostUuid)

Get a known host

Retrieve a repository level known host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String knownHostUuid = "knownHostUuid_example"; // String | The UUID of the known host to retrieve.
    try {
      PipelineKnownHost result = apiInstance.getRepositoryPipelineKnownHost(workspace, repoSlug, knownHostUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getRepositoryPipelineKnownHost");
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
| **knownHostUuid** | **String**| The UUID of the known host to retrieve. | |

### Return type

[**PipelineKnownHost**](PipelineKnownHost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The known host. |  -  |
| **404** | The account, repository or known host with the specified UUID was not found. |  -  |

<a id="getRepositoryPipelineKnownHosts"></a>
# **getRepositoryPipelineKnownHosts**
> PaginatedPipelineKnownHosts getRepositoryPipelineKnownHosts(workspace, repoSlug)

List known hosts

Find repository level known hosts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    try {
      PaginatedPipelineKnownHosts result = apiInstance.getRepositoryPipelineKnownHosts(workspace, repoSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getRepositoryPipelineKnownHosts");
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

[**PaginatedPipelineKnownHosts**](PaginatedPipelineKnownHosts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved known hosts. |  -  |

<a id="getRepositoryPipelineSchedule"></a>
# **getRepositoryPipelineSchedule**
> PipelineSchedule getRepositoryPipelineSchedule(workspace, repoSlug, scheduleUuid)

Get a schedule

Retrieve a schedule by its UUID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String scheduleUuid = "scheduleUuid_example"; // String | The uuid of the schedule.
    try {
      PipelineSchedule result = apiInstance.getRepositoryPipelineSchedule(workspace, repoSlug, scheduleUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getRepositoryPipelineSchedule");
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
| **scheduleUuid** | **String**| The uuid of the schedule. | |

### Return type

[**PipelineSchedule**](PipelineSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested schedule. |  -  |
| **404** | The account, repository or schedule was not found. |  -  |

<a id="getRepositoryPipelineScheduleExecutions"></a>
# **getRepositoryPipelineScheduleExecutions**
> PaginatedPipelineScheduleExecutions getRepositoryPipelineScheduleExecutions(workspace, repoSlug, scheduleUuid)

List executions of a schedule

Retrieve the executions of a given schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String scheduleUuid = "scheduleUuid_example"; // String | The uuid of the schedule.
    try {
      PaginatedPipelineScheduleExecutions result = apiInstance.getRepositoryPipelineScheduleExecutions(workspace, repoSlug, scheduleUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getRepositoryPipelineScheduleExecutions");
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
| **scheduleUuid** | **String**| The uuid of the schedule. | |

### Return type

[**PaginatedPipelineScheduleExecutions**](PaginatedPipelineScheduleExecutions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of executions of a schedule. |  -  |
| **404** | The account or repository was not found. |  -  |

<a id="getRepositoryPipelineSchedules"></a>
# **getRepositoryPipelineSchedules**
> PaginatedPipelineSchedules getRepositoryPipelineSchedules(workspace, repoSlug)

List schedules

Retrieve the configured schedules for the given repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    try {
      PaginatedPipelineSchedules result = apiInstance.getRepositoryPipelineSchedules(workspace, repoSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getRepositoryPipelineSchedules");
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

[**PaginatedPipelineSchedules**](PaginatedPipelineSchedules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of schedules. |  -  |
| **404** | The account or repository was not found. |  -  |

<a id="getRepositoryPipelineSshKeyPair"></a>
# **getRepositoryPipelineSshKeyPair**
> PipelineSshKeyPair getRepositoryPipelineSshKeyPair(workspace, repoSlug)

Get SSH key pair

Retrieve the repository SSH key pair excluding the SSH private key. The private key is a write only field and will never be exposed in the logs or the REST API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    try {
      PipelineSshKeyPair result = apiInstance.getRepositoryPipelineSshKeyPair(workspace, repoSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getRepositoryPipelineSshKeyPair");
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

[**PipelineSshKeyPair**](PipelineSshKeyPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SSH key pair. |  -  |
| **404** | The account, repository or SSH key pair was not found. |  -  |

<a id="getRepositoryPipelineVariable"></a>
# **getRepositoryPipelineVariable**
> PipelineVariable getRepositoryPipelineVariable(workspace, repoSlug, variableUuid)

Get a variable for a repository

Retrieve a repository level variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable to retrieve.
    try {
      PipelineVariable result = apiInstance.getRepositoryPipelineVariable(workspace, repoSlug, variableUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getRepositoryPipelineVariable");
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
| **variableUuid** | **String**| The UUID of the variable to retrieve. | |

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The variable. |  -  |
| **404** | The account, repository or variable with the specified UUID was not found. |  -  |

<a id="getRepositoryPipelineVariables"></a>
# **getRepositoryPipelineVariables**
> PaginatedPipelineVariables getRepositoryPipelineVariables(workspace, repoSlug)

List variables for a repository

Find repository level variables.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    try {
      PaginatedPipelineVariables result = apiInstance.getRepositoryPipelineVariables(workspace, repoSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#getRepositoryPipelineVariables");
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

[**PaginatedPipelineVariables**](PaginatedPipelineVariables.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved variables. |  -  |

<a id="stopPipeline"></a>
# **stopPipeline**
> stopPipeline(workspace, repoSlug, pipelineUuid)

Stop a pipeline

Signal the stop of a pipeline and all of its steps that not have completed yet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String pipelineUuid = "pipelineUuid_example"; // String | The UUID of the pipeline.
    try {
      apiInstance.stopPipeline(workspace, repoSlug, pipelineUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#stopPipeline");
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
| **pipelineUuid** | **String**| The UUID of the pipeline. | |

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
| **204** | The pipeline has been signaled to stop. |  -  |
| **400** | The specified pipeline has already completed. |  -  |
| **404** | Either the account, repository or pipeline with the given UUID does not exist. |  -  |

<a id="updateDeploymentVariable"></a>
# **updateDeploymentVariable**
> DeploymentVariable updateDeploymentVariable(workspace, repoSlug, environmentUuid, variableUuid, deploymentVariable)

Update a variable for an environment

Update a deployment environment level variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String environmentUuid = "environmentUuid_example"; // String | The environment.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable to update.
    DeploymentVariable deploymentVariable = new DeploymentVariable(); // DeploymentVariable | The updated deployment variable.
    try {
      DeploymentVariable result = apiInstance.updateDeploymentVariable(workspace, repoSlug, environmentUuid, variableUuid, deploymentVariable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#updateDeploymentVariable");
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
| **environmentUuid** | **String**| The environment. | |
| **variableUuid** | **String**| The UUID of the variable to update. | |
| **deploymentVariable** | [**DeploymentVariable**](DeploymentVariable.md)| The updated deployment variable. | |

### Return type

[**DeploymentVariable**](DeploymentVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deployment variable was updated. |  -  |
| **404** | The account, repository, environment or variable with the given UUID was not found. |  -  |

<a id="updatePipelineVariableForTeam"></a>
# **updatePipelineVariableForTeam**
> PipelineVariable updatePipelineVariableForTeam(username, variableUuid, pipelineVariable)

Update a variable for a team

Update a team level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String username = "username_example"; // String | The account.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable.
    PipelineVariable pipelineVariable = new PipelineVariable(); // PipelineVariable | The updated variable.
    try {
      PipelineVariable result = apiInstance.updatePipelineVariableForTeam(username, variableUuid, pipelineVariable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#updatePipelineVariableForTeam");
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
| **username** | **String**| The account. | |
| **variableUuid** | **String**| The UUID of the variable. | |
| **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The updated variable. | |

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The variable was updated. |  -  |
| **404** | The account or the variable was not found. |  -  |

<a id="updatePipelineVariableForUser"></a>
# **updatePipelineVariableForUser**
> PipelineVariable updatePipelineVariableForUser(selectedUser, variableUuid, pipelineVariable)

Update a variable for a user

Update a user level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable.
    PipelineVariable pipelineVariable = new PipelineVariable(); // PipelineVariable | The updated variable.
    try {
      PipelineVariable result = apiInstance.updatePipelineVariableForUser(selectedUser, variableUuid, pipelineVariable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#updatePipelineVariableForUser");
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
| **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | |
| **variableUuid** | **String**| The UUID of the variable. | |
| **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The updated variable. | |

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The variable was updated. |  -  |
| **404** | The account or the variable was not found. |  -  |

<a id="updatePipelineVariableForWorkspace"></a>
# **updatePipelineVariableForWorkspace**
> PipelineVariable updatePipelineVariableForWorkspace(workspace, variableUuid, pipelineVariable)

Update variable for a workspace

Update a workspace level variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable.
    PipelineVariable pipelineVariable = new PipelineVariable(); // PipelineVariable | The updated variable.
    try {
      PipelineVariable result = apiInstance.updatePipelineVariableForWorkspace(workspace, variableUuid, pipelineVariable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#updatePipelineVariableForWorkspace");
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
| **variableUuid** | **String**| The UUID of the variable. | |
| **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The updated variable. | |

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The variable was updated. |  -  |
| **404** | The workspace or the variable was not found. |  -  |

<a id="updateRepositoryBuildNumber"></a>
# **updateRepositoryBuildNumber**
> PipelineBuildNumber updateRepositoryBuildNumber(workspace, repoSlug, pipelineBuildNumber)

Update the next build number

Update the next build number that should be assigned to a pipeline. The next build number that will be configured has to be strictly higher than the current latest build number for this repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    PipelineBuildNumber pipelineBuildNumber = new PipelineBuildNumber(); // PipelineBuildNumber | The build number to update.
    try {
      PipelineBuildNumber result = apiInstance.updateRepositoryBuildNumber(workspace, repoSlug, pipelineBuildNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#updateRepositoryBuildNumber");
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
| **pipelineBuildNumber** | [**PipelineBuildNumber**](PipelineBuildNumber.md)| The build number to update. | |

### Return type

[**PipelineBuildNumber**](PipelineBuildNumber.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The build number has been configured. |  -  |
| **400** | The update failed because the next number was invalid (it should be higher than the current number). |  -  |
| **404** | The account or repository was not found. |  -  |

<a id="updateRepositoryPipelineConfig"></a>
# **updateRepositoryPipelineConfig**
> PipelinesConfig updateRepositoryPipelineConfig(workspace, repoSlug, pipelinesConfig)

Update configuration

Update the pipelines configuration for a repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    PipelinesConfig pipelinesConfig = new PipelinesConfig(); // PipelinesConfig | The updated repository pipelines configuration.
    try {
      PipelinesConfig result = apiInstance.updateRepositoryPipelineConfig(workspace, repoSlug, pipelinesConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#updateRepositoryPipelineConfig");
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
| **pipelinesConfig** | [**PipelinesConfig**](PipelinesConfig.md)| The updated repository pipelines configuration. | |

### Return type

[**PipelinesConfig**](PipelinesConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The repository pipelines configuration was updated. |  -  |

<a id="updateRepositoryPipelineKeyPair"></a>
# **updateRepositoryPipelineKeyPair**
> PipelineSshKeyPair updateRepositoryPipelineKeyPair(workspace, repoSlug, pipelineSshKeyPair)

Update SSH key pair

Create or update the repository SSH key pair. The private key will be set as a default SSH identity in your build container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    PipelineSshKeyPair pipelineSshKeyPair = new PipelineSshKeyPair(); // PipelineSshKeyPair | The created or updated SSH key pair.
    try {
      PipelineSshKeyPair result = apiInstance.updateRepositoryPipelineKeyPair(workspace, repoSlug, pipelineSshKeyPair);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#updateRepositoryPipelineKeyPair");
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
| **pipelineSshKeyPair** | [**PipelineSshKeyPair**](PipelineSshKeyPair.md)| The created or updated SSH key pair. | |

### Return type

[**PipelineSshKeyPair**](PipelineSshKeyPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SSH key pair was created or updated. |  -  |
| **404** | The account, repository or SSH key pair was not found. |  -  |

<a id="updateRepositoryPipelineKnownHost"></a>
# **updateRepositoryPipelineKnownHost**
> PipelineKnownHost updateRepositoryPipelineKnownHost(workspace, repoSlug, knownHostUuid, pipelineKnownHost)

Update a known host

Update a repository level known host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String knownHostUuid = "knownHostUuid_example"; // String | The UUID of the known host to update.
    PipelineKnownHost pipelineKnownHost = new PipelineKnownHost(); // PipelineKnownHost | The updated known host.
    try {
      PipelineKnownHost result = apiInstance.updateRepositoryPipelineKnownHost(workspace, repoSlug, knownHostUuid, pipelineKnownHost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#updateRepositoryPipelineKnownHost");
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
| **knownHostUuid** | **String**| The UUID of the known host to update. | |
| **pipelineKnownHost** | [**PipelineKnownHost**](PipelineKnownHost.md)| The updated known host. | |

### Return type

[**PipelineKnownHost**](PipelineKnownHost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The known host was updated. |  -  |
| **404** | The account, repository or known host with the given UUID was not found. |  -  |

<a id="updateRepositoryPipelineSchedule"></a>
# **updateRepositoryPipelineSchedule**
> PipelineSchedule updateRepositoryPipelineSchedule(workspace, repoSlug, scheduleUuid, pipelineSchedulePutRequestBody)

Update a schedule

Update a schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String scheduleUuid = "scheduleUuid_example"; // String | The uuid of the schedule.
    PipelineSchedulePutRequestBody pipelineSchedulePutRequestBody = new PipelineSchedulePutRequestBody(); // PipelineSchedulePutRequestBody | The schedule to update.
    try {
      PipelineSchedule result = apiInstance.updateRepositoryPipelineSchedule(workspace, repoSlug, scheduleUuid, pipelineSchedulePutRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#updateRepositoryPipelineSchedule");
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
| **scheduleUuid** | **String**| The uuid of the schedule. | |
| **pipelineSchedulePutRequestBody** | [**PipelineSchedulePutRequestBody**](PipelineSchedulePutRequestBody.md)| The schedule to update. | |

### Return type

[**PipelineSchedule**](PipelineSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The schedule is updated. |  -  |
| **404** | The account, repository or schedule was not found. |  -  |

<a id="updateRepositoryPipelineVariable"></a>
# **updateRepositoryPipelineVariable**
> PipelineVariable updateRepositoryPipelineVariable(workspace, repoSlug, variableUuid, pipelineVariable)

Update a variable for a repository

Update a repository level variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String variableUuid = "variableUuid_example"; // String | The UUID of the variable to update.
    PipelineVariable pipelineVariable = new PipelineVariable(); // PipelineVariable | The updated variable
    try {
      PipelineVariable result = apiInstance.updateRepositoryPipelineVariable(workspace, repoSlug, variableUuid, pipelineVariable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#updateRepositoryPipelineVariable");
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
| **variableUuid** | **String**| The UUID of the variable to update. | |
| **pipelineVariable** | [**PipelineVariable**](PipelineVariable.md)| The updated variable | |

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The variable was updated. |  -  |
| **404** | The account, repository or variable with the given UUID was not found. |  -  |

