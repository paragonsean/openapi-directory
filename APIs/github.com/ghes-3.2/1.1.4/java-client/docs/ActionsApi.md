# ActionsApi

All URIs are relative to *https://github.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**actionsAddRepoAccessToSelfHostedRunnerGroupInOrg**](ActionsApi.md#actionsAddRepoAccessToSelfHostedRunnerGroupInOrg) | **PUT** /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id} | Add repository access to a self-hosted runner group in an organization |
| [**actionsAddSelectedRepoToOrgSecret**](ActionsApi.md#actionsAddSelectedRepoToOrgSecret) | **PUT** /orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id} | Add selected repository to an organization secret |
| [**actionsAddSelfHostedRunnerToGroupForOrg**](ActionsApi.md#actionsAddSelfHostedRunnerToGroupForOrg) | **PUT** /orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | Add a self-hosted runner to a group for an organization |
| [**actionsCancelWorkflowRun**](ActionsApi.md#actionsCancelWorkflowRun) | **POST** /repos/{owner}/{repo}/actions/runs/{run_id}/cancel | Cancel a workflow run |
| [**actionsCreateOrUpdateEnvironmentSecret**](ActionsApi.md#actionsCreateOrUpdateEnvironmentSecret) | **PUT** /repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name} | Create or update an environment secret |
| [**actionsCreateOrUpdateOrgSecret**](ActionsApi.md#actionsCreateOrUpdateOrgSecret) | **PUT** /orgs/{org}/actions/secrets/{secret_name} | Create or update an organization secret |
| [**actionsCreateOrUpdateRepoSecret**](ActionsApi.md#actionsCreateOrUpdateRepoSecret) | **PUT** /repos/{owner}/{repo}/actions/secrets/{secret_name} | Create or update a repository secret |
| [**actionsCreateRegistrationTokenForOrg**](ActionsApi.md#actionsCreateRegistrationTokenForOrg) | **POST** /orgs/{org}/actions/runners/registration-token | Create a registration token for an organization |
| [**actionsCreateRegistrationTokenForRepo**](ActionsApi.md#actionsCreateRegistrationTokenForRepo) | **POST** /repos/{owner}/{repo}/actions/runners/registration-token | Create a registration token for a repository |
| [**actionsCreateRemoveTokenForOrg**](ActionsApi.md#actionsCreateRemoveTokenForOrg) | **POST** /orgs/{org}/actions/runners/remove-token | Create a remove token for an organization |
| [**actionsCreateRemoveTokenForRepo**](ActionsApi.md#actionsCreateRemoveTokenForRepo) | **POST** /repos/{owner}/{repo}/actions/runners/remove-token | Create a remove token for a repository |
| [**actionsCreateSelfHostedRunnerGroupForOrg**](ActionsApi.md#actionsCreateSelfHostedRunnerGroupForOrg) | **POST** /orgs/{org}/actions/runner-groups | Create a self-hosted runner group for an organization |
| [**actionsCreateWorkflowDispatch**](ActionsApi.md#actionsCreateWorkflowDispatch) | **POST** /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches | Create a workflow dispatch event |
| [**actionsDeleteArtifact**](ActionsApi.md#actionsDeleteArtifact) | **DELETE** /repos/{owner}/{repo}/actions/artifacts/{artifact_id} | Delete an artifact |
| [**actionsDeleteEnvironmentSecret**](ActionsApi.md#actionsDeleteEnvironmentSecret) | **DELETE** /repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name} | Delete an environment secret |
| [**actionsDeleteOrgSecret**](ActionsApi.md#actionsDeleteOrgSecret) | **DELETE** /orgs/{org}/actions/secrets/{secret_name} | Delete an organization secret |
| [**actionsDeleteRepoSecret**](ActionsApi.md#actionsDeleteRepoSecret) | **DELETE** /repos/{owner}/{repo}/actions/secrets/{secret_name} | Delete a repository secret |
| [**actionsDeleteSelfHostedRunnerFromOrg**](ActionsApi.md#actionsDeleteSelfHostedRunnerFromOrg) | **DELETE** /orgs/{org}/actions/runners/{runner_id} | Delete a self-hosted runner from an organization |
| [**actionsDeleteSelfHostedRunnerFromRepo**](ActionsApi.md#actionsDeleteSelfHostedRunnerFromRepo) | **DELETE** /repos/{owner}/{repo}/actions/runners/{runner_id} | Delete a self-hosted runner from a repository |
| [**actionsDeleteSelfHostedRunnerGroupFromOrg**](ActionsApi.md#actionsDeleteSelfHostedRunnerGroupFromOrg) | **DELETE** /orgs/{org}/actions/runner-groups/{runner_group_id} | Delete a self-hosted runner group from an organization |
| [**actionsDeleteWorkflowRun**](ActionsApi.md#actionsDeleteWorkflowRun) | **DELETE** /repos/{owner}/{repo}/actions/runs/{run_id} | Delete a workflow run |
| [**actionsDeleteWorkflowRunLogs**](ActionsApi.md#actionsDeleteWorkflowRunLogs) | **DELETE** /repos/{owner}/{repo}/actions/runs/{run_id}/logs | Delete workflow run logs |
| [**actionsDisableSelectedRepositoryGithubActionsOrganization**](ActionsApi.md#actionsDisableSelectedRepositoryGithubActionsOrganization) | **DELETE** /orgs/{org}/actions/permissions/repositories/{repository_id} | Disable a selected repository for GitHub Actions in an organization |
| [**actionsDisableWorkflow**](ActionsApi.md#actionsDisableWorkflow) | **PUT** /repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable | Disable a workflow |
| [**actionsDownloadArtifact**](ActionsApi.md#actionsDownloadArtifact) | **GET** /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format} | Download an artifact |
| [**actionsDownloadJobLogsForWorkflowRun**](ActionsApi.md#actionsDownloadJobLogsForWorkflowRun) | **GET** /repos/{owner}/{repo}/actions/jobs/{job_id}/logs | Download job logs for a workflow run |
| [**actionsDownloadWorkflowRunLogs**](ActionsApi.md#actionsDownloadWorkflowRunLogs) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/logs | Download workflow run logs |
| [**actionsEnableSelectedRepositoryGithubActionsOrganization**](ActionsApi.md#actionsEnableSelectedRepositoryGithubActionsOrganization) | **PUT** /orgs/{org}/actions/permissions/repositories/{repository_id} | Enable a selected repository for GitHub Actions in an organization |
| [**actionsEnableWorkflow**](ActionsApi.md#actionsEnableWorkflow) | **PUT** /repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable | Enable a workflow |
| [**actionsGetAllowedActionsOrganization**](ActionsApi.md#actionsGetAllowedActionsOrganization) | **GET** /orgs/{org}/actions/permissions/selected-actions | Get allowed actions for an organization |
| [**actionsGetAllowedActionsRepository**](ActionsApi.md#actionsGetAllowedActionsRepository) | **GET** /repos/{owner}/{repo}/actions/permissions/selected-actions | Get allowed actions for a repository |
| [**actionsGetArtifact**](ActionsApi.md#actionsGetArtifact) | **GET** /repos/{owner}/{repo}/actions/artifacts/{artifact_id} | Get an artifact |
| [**actionsGetEnvironmentPublicKey**](ActionsApi.md#actionsGetEnvironmentPublicKey) | **GET** /repositories/{repository_id}/environments/{environment_name}/secrets/public-key | Get an environment public key |
| [**actionsGetEnvironmentSecret**](ActionsApi.md#actionsGetEnvironmentSecret) | **GET** /repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name} | Get an environment secret |
| [**actionsGetGithubActionsPermissionsOrganization**](ActionsApi.md#actionsGetGithubActionsPermissionsOrganization) | **GET** /orgs/{org}/actions/permissions | Get GitHub Actions permissions for an organization |
| [**actionsGetGithubActionsPermissionsRepository**](ActionsApi.md#actionsGetGithubActionsPermissionsRepository) | **GET** /repos/{owner}/{repo}/actions/permissions | Get GitHub Actions permissions for a repository |
| [**actionsGetJobForWorkflowRun**](ActionsApi.md#actionsGetJobForWorkflowRun) | **GET** /repos/{owner}/{repo}/actions/jobs/{job_id} | Get a job for a workflow run |
| [**actionsGetOrgPublicKey**](ActionsApi.md#actionsGetOrgPublicKey) | **GET** /orgs/{org}/actions/secrets/public-key | Get an organization public key |
| [**actionsGetOrgSecret**](ActionsApi.md#actionsGetOrgSecret) | **GET** /orgs/{org}/actions/secrets/{secret_name} | Get an organization secret |
| [**actionsGetPendingDeploymentsForRun**](ActionsApi.md#actionsGetPendingDeploymentsForRun) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments | Get pending deployments for a workflow run |
| [**actionsGetRepoPublicKey**](ActionsApi.md#actionsGetRepoPublicKey) | **GET** /repos/{owner}/{repo}/actions/secrets/public-key | Get a repository public key |
| [**actionsGetRepoSecret**](ActionsApi.md#actionsGetRepoSecret) | **GET** /repos/{owner}/{repo}/actions/secrets/{secret_name} | Get a repository secret |
| [**actionsGetReviewsForRun**](ActionsApi.md#actionsGetReviewsForRun) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/approvals | Get the review history for a workflow run |
| [**actionsGetSelfHostedRunnerForOrg**](ActionsApi.md#actionsGetSelfHostedRunnerForOrg) | **GET** /orgs/{org}/actions/runners/{runner_id} | Get a self-hosted runner for an organization |
| [**actionsGetSelfHostedRunnerForRepo**](ActionsApi.md#actionsGetSelfHostedRunnerForRepo) | **GET** /repos/{owner}/{repo}/actions/runners/{runner_id} | Get a self-hosted runner for a repository |
| [**actionsGetSelfHostedRunnerGroupForOrg**](ActionsApi.md#actionsGetSelfHostedRunnerGroupForOrg) | **GET** /orgs/{org}/actions/runner-groups/{runner_group_id} | Get a self-hosted runner group for an organization |
| [**actionsGetWorkflow**](ActionsApi.md#actionsGetWorkflow) | **GET** /repos/{owner}/{repo}/actions/workflows/{workflow_id} | Get a workflow |
| [**actionsGetWorkflowRun**](ActionsApi.md#actionsGetWorkflowRun) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id} | Get a workflow run |
| [**actionsListArtifactsForRepo**](ActionsApi.md#actionsListArtifactsForRepo) | **GET** /repos/{owner}/{repo}/actions/artifacts | List artifacts for a repository |
| [**actionsListEnvironmentSecrets**](ActionsApi.md#actionsListEnvironmentSecrets) | **GET** /repositories/{repository_id}/environments/{environment_name}/secrets | List environment secrets |
| [**actionsListJobsForWorkflowRun**](ActionsApi.md#actionsListJobsForWorkflowRun) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/jobs | List jobs for a workflow run |
| [**actionsListOrgSecrets**](ActionsApi.md#actionsListOrgSecrets) | **GET** /orgs/{org}/actions/secrets | List organization secrets |
| [**actionsListRepoAccessToSelfHostedRunnerGroupInOrg**](ActionsApi.md#actionsListRepoAccessToSelfHostedRunnerGroupInOrg) | **GET** /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories | List repository access to a self-hosted runner group in an organization |
| [**actionsListRepoSecrets**](ActionsApi.md#actionsListRepoSecrets) | **GET** /repos/{owner}/{repo}/actions/secrets | List repository secrets |
| [**actionsListRepoWorkflows**](ActionsApi.md#actionsListRepoWorkflows) | **GET** /repos/{owner}/{repo}/actions/workflows | List repository workflows |
| [**actionsListRunnerApplicationsForOrg**](ActionsApi.md#actionsListRunnerApplicationsForOrg) | **GET** /orgs/{org}/actions/runners/downloads | List runner applications for an organization |
| [**actionsListRunnerApplicationsForRepo**](ActionsApi.md#actionsListRunnerApplicationsForRepo) | **GET** /repos/{owner}/{repo}/actions/runners/downloads | List runner applications for a repository |
| [**actionsListSelectedReposForOrgSecret**](ActionsApi.md#actionsListSelectedReposForOrgSecret) | **GET** /orgs/{org}/actions/secrets/{secret_name}/repositories | List selected repositories for an organization secret |
| [**actionsListSelectedRepositoriesEnabledGithubActionsOrganization**](ActionsApi.md#actionsListSelectedRepositoriesEnabledGithubActionsOrganization) | **GET** /orgs/{org}/actions/permissions/repositories | List selected repositories enabled for GitHub Actions in an organization |
| [**actionsListSelfHostedRunnerGroupsForOrg**](ActionsApi.md#actionsListSelfHostedRunnerGroupsForOrg) | **GET** /orgs/{org}/actions/runner-groups | List self-hosted runner groups for an organization |
| [**actionsListSelfHostedRunnersForOrg**](ActionsApi.md#actionsListSelfHostedRunnersForOrg) | **GET** /orgs/{org}/actions/runners | List self-hosted runners for an organization |
| [**actionsListSelfHostedRunnersForRepo**](ActionsApi.md#actionsListSelfHostedRunnersForRepo) | **GET** /repos/{owner}/{repo}/actions/runners | List self-hosted runners for a repository |
| [**actionsListSelfHostedRunnersInGroupForOrg**](ActionsApi.md#actionsListSelfHostedRunnersInGroupForOrg) | **GET** /orgs/{org}/actions/runner-groups/{runner_group_id}/runners | List self-hosted runners in a group for an organization |
| [**actionsListWorkflowRunArtifacts**](ActionsApi.md#actionsListWorkflowRunArtifacts) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/artifacts | List workflow run artifacts |
| [**actionsListWorkflowRuns**](ActionsApi.md#actionsListWorkflowRuns) | **GET** /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs | List workflow runs for a workflow |
| [**actionsListWorkflowRunsForRepo**](ActionsApi.md#actionsListWorkflowRunsForRepo) | **GET** /repos/{owner}/{repo}/actions/runs | List workflow runs for a repository |
| [**actionsReRunWorkflow**](ActionsApi.md#actionsReRunWorkflow) | **POST** /repos/{owner}/{repo}/actions/runs/{run_id}/rerun | Re-run a workflow |
| [**actionsRemoveRepoAccessToSelfHostedRunnerGroupInOrg**](ActionsApi.md#actionsRemoveRepoAccessToSelfHostedRunnerGroupInOrg) | **DELETE** /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id} | Remove repository access to a self-hosted runner group in an organization |
| [**actionsRemoveSelectedRepoFromOrgSecret**](ActionsApi.md#actionsRemoveSelectedRepoFromOrgSecret) | **DELETE** /orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id} | Remove selected repository from an organization secret |
| [**actionsRemoveSelfHostedRunnerFromGroupForOrg**](ActionsApi.md#actionsRemoveSelfHostedRunnerFromGroupForOrg) | **DELETE** /orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | Remove a self-hosted runner from a group for an organization |
| [**actionsReviewPendingDeploymentsForRun**](ActionsApi.md#actionsReviewPendingDeploymentsForRun) | **POST** /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments | Review pending deployments for a workflow run |
| [**actionsSetAllowedActionsOrganization**](ActionsApi.md#actionsSetAllowedActionsOrganization) | **PUT** /orgs/{org}/actions/permissions/selected-actions | Set allowed actions for an organization |
| [**actionsSetAllowedActionsRepository**](ActionsApi.md#actionsSetAllowedActionsRepository) | **PUT** /repos/{owner}/{repo}/actions/permissions/selected-actions | Set allowed actions for a repository |
| [**actionsSetGithubActionsPermissionsOrganization**](ActionsApi.md#actionsSetGithubActionsPermissionsOrganization) | **PUT** /orgs/{org}/actions/permissions | Set GitHub Actions permissions for an organization |
| [**actionsSetGithubActionsPermissionsRepository**](ActionsApi.md#actionsSetGithubActionsPermissionsRepository) | **PUT** /repos/{owner}/{repo}/actions/permissions | Set GitHub Actions permissions for a repository |
| [**actionsSetRepoAccessToSelfHostedRunnerGroupInOrg**](ActionsApi.md#actionsSetRepoAccessToSelfHostedRunnerGroupInOrg) | **PUT** /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories | Set repository access for a self-hosted runner group in an organization |
| [**actionsSetSelectedReposForOrgSecret**](ActionsApi.md#actionsSetSelectedReposForOrgSecret) | **PUT** /orgs/{org}/actions/secrets/{secret_name}/repositories | Set selected repositories for an organization secret |
| [**actionsSetSelectedRepositoriesEnabledGithubActionsOrganization**](ActionsApi.md#actionsSetSelectedRepositoriesEnabledGithubActionsOrganization) | **PUT** /orgs/{org}/actions/permissions/repositories | Set selected repositories enabled for GitHub Actions in an organization |
| [**actionsSetSelfHostedRunnersInGroupForOrg**](ActionsApi.md#actionsSetSelfHostedRunnersInGroupForOrg) | **PUT** /orgs/{org}/actions/runner-groups/{runner_group_id}/runners | Set self-hosted runners in a group for an organization |
| [**actionsUpdateSelfHostedRunnerGroupForOrg**](ActionsApi.md#actionsUpdateSelfHostedRunnerGroupForOrg) | **PATCH** /orgs/{org}/actions/runner-groups/{runner_group_id} | Update a self-hosted runner group for an organization |


<a id="actionsAddRepoAccessToSelfHostedRunnerGroupInOrg"></a>
# **actionsAddRepoAccessToSelfHostedRunnerGroupInOrg**
> actionsAddRepoAccessToSelfHostedRunnerGroupInOrg(org, runnerGroupId, repositoryId)

Add repository access to a self-hosted runner group in an organization

Adds a repository to the list of selected repositories that can access a self-hosted runner group. The runner group must have &#x60;visibility&#x60; set to &#x60;selected&#x60;. For more information, see \&quot;[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization).\&quot; You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    Integer repositoryId = 56; // Integer | The unique identifier of the repository.
    try {
      apiInstance.actionsAddRepoAccessToSelfHostedRunnerGroupInOrg(org, runnerGroupId, repositoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsAddRepoAccessToSelfHostedRunnerGroupInOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **repositoryId** | **Integer**| The unique identifier of the repository. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsAddSelectedRepoToOrgSecret"></a>
# **actionsAddSelectedRepoToOrgSecret**
> actionsAddSelectedRepoToOrgSecret(org, secretName, repositoryId)

Add selected repository to an organization secret

Adds a repository to an organization secret when the &#x60;visibility&#x60; for repository access is set to &#x60;selected&#x60;. The visibility is set when you [Create or update an organization secret](https://docs.github.com/enterprise-server@3.2/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    String secretName = "secretName_example"; // String | The name of the secret.
    Integer repositoryId = 56; // Integer | 
    try {
      apiInstance.actionsAddSelectedRepoToOrgSecret(org, secretName, repositoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsAddSelectedRepoToOrgSecret");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **secretName** | **String**| The name of the secret. | |
| **repositoryId** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content when repository was added to the selected list |  -  |
| **409** | Conflict when visibility type is not set to selected |  -  |

<a id="actionsAddSelfHostedRunnerToGroupForOrg"></a>
# **actionsAddSelfHostedRunnerToGroupForOrg**
> actionsAddSelfHostedRunnerToGroupForOrg(org, runnerGroupId, runnerId)

Add a self-hosted runner to a group for an organization

Adds a self-hosted runner to a runner group configured in an organization. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    try {
      apiInstance.actionsAddSelfHostedRunnerToGroupForOrg(org, runnerGroupId, runnerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsAddSelfHostedRunnerToGroupForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **runnerId** | **Integer**| Unique identifier of the self-hosted runner. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsCancelWorkflowRun"></a>
# **actionsCancelWorkflowRun**
> Object actionsCancelWorkflowRun(owner, repo, runId)

Cancel a workflow run

Cancels a workflow run using its &#x60;id&#x60;. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer runId = 56; // Integer | The unique identifier of the workflow run.
    try {
      Object result = apiInstance.actionsCancelWorkflowRun(owner, repo, runId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsCancelWorkflowRun");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **runId** | **Integer**| The unique identifier of the workflow run. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Response |  -  |
| **409** | Conflict |  -  |

<a id="actionsCreateOrUpdateEnvironmentSecret"></a>
# **actionsCreateOrUpdateEnvironmentSecret**
> Object actionsCreateOrUpdateEnvironmentSecret(repositoryId, environmentName, secretName, actionsCreateOrUpdateEnvironmentSecretRequest)

Create or update an environment secret

Creates or updates an environment secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.  #### Example encrypting a secret using Node.js  Encrypt your secret using the [libsodium-wrappers](https://www.npmjs.com/package/libsodium-wrappers) library.  &#x60;&#x60;&#x60; const sodium &#x3D; require(&#39;libsodium-wrappers&#39;) const secret &#x3D; &#39;plain-text-secret&#39; // replace with the secret you want to encrypt const key &#x3D; &#39;base64-encoded-public-key&#39; // replace with the Base64 encoded public key  //Check if libsodium is ready and then proceed. sodium.ready.then(() &#x3D;&gt; {   // Convert Secret &amp; Base64 key to Uint8Array.   let binkey &#x3D; sodium.from_base64(key, sodium.base64_variants.ORIGINAL)   let binsec &#x3D; sodium.from_string(secret)    //Encrypt the secret using LibSodium   let encBytes &#x3D; sodium.crypto_box_seal(binsec, binkey)    // Convert encrypted Uint8Array to Base64   let output &#x3D; sodium.to_base64(encBytes, sodium.base64_variants.ORIGINAL)    console.log(output) }); &#x60;&#x60;&#x60;  #### Example encrypting a secret using Python  Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/latest/public/#nacl-public-sealedbox) with Python 3.  &#x60;&#x60;&#x60; from base64 import b64encode from nacl import encoding, public  def encrypt(public_key: str, secret_value: str) -&gt; str:   \&quot;\&quot;\&quot;Encrypt a Unicode string using the public key.\&quot;\&quot;\&quot;   public_key &#x3D; public.PublicKey(public_key.encode(\&quot;utf-8\&quot;), encoding.Base64Encoder())   sealed_box &#x3D; public.SealedBox(public_key)   encrypted &#x3D; sealed_box.encrypt(secret_value.encode(\&quot;utf-8\&quot;))   return b64encode(encrypted).decode(\&quot;utf-8\&quot;) &#x60;&#x60;&#x60;  #### Example encrypting a secret using C#  Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.  &#x60;&#x60;&#x60; var secretValue &#x3D; System.Text.Encoding.UTF8.GetBytes(\&quot;mySecret\&quot;); var publicKey &#x3D; Convert.FromBase64String(\&quot;2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU&#x3D;\&quot;);  var sealedPublicKeyBox &#x3D; Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);  Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox)); &#x60;&#x60;&#x60;  #### Example encrypting a secret using Ruby  Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.  &#x60;&#x60;&#x60;ruby require \&quot;rbnacl\&quot; require \&quot;base64\&quot;  key &#x3D; Base64.decode64(\&quot;+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0&#x3D;\&quot;) public_key &#x3D; RbNaCl::PublicKey.new(key)  box &#x3D; RbNaCl::Boxes::Sealed.from_public_key(public_key) encrypted_secret &#x3D; box.encrypt(\&quot;my_secret\&quot;)  # Print the base64 encoded secret puts Base64.strict_encode64(encrypted_secret) &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    Integer repositoryId = 56; // Integer | The unique identifier of the repository.
    String environmentName = "environmentName_example"; // String | The name of the environment.
    String secretName = "secretName_example"; // String | The name of the secret.
    ActionsCreateOrUpdateEnvironmentSecretRequest actionsCreateOrUpdateEnvironmentSecretRequest = new ActionsCreateOrUpdateEnvironmentSecretRequest(); // ActionsCreateOrUpdateEnvironmentSecretRequest | 
    try {
      Object result = apiInstance.actionsCreateOrUpdateEnvironmentSecret(repositoryId, environmentName, secretName, actionsCreateOrUpdateEnvironmentSecretRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsCreateOrUpdateEnvironmentSecret");
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
| **repositoryId** | **Integer**| The unique identifier of the repository. | |
| **environmentName** | **String**| The name of the environment. | |
| **secretName** | **String**| The name of the secret. | |
| **actionsCreateOrUpdateEnvironmentSecretRequest** | [**ActionsCreateOrUpdateEnvironmentSecretRequest**](ActionsCreateOrUpdateEnvironmentSecretRequest.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response when creating a secret |  -  |
| **204** | Response when updating a secret |  -  |

<a id="actionsCreateOrUpdateOrgSecret"></a>
# **actionsCreateOrUpdateOrgSecret**
> Object actionsCreateOrUpdateOrgSecret(org, secretName, actionsCreateOrUpdateOrgSecretRequest)

Create or update an organization secret

Creates or updates an organization secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.  #### Example encrypting a secret using Node.js  Encrypt your secret using the [libsodium-wrappers](https://www.npmjs.com/package/libsodium-wrappers) library.  &#x60;&#x60;&#x60; const sodium &#x3D; require(&#39;libsodium-wrappers&#39;) const secret &#x3D; &#39;plain-text-secret&#39; // replace with the secret you want to encrypt const key &#x3D; &#39;base64-encoded-public-key&#39; // replace with the Base64 encoded public key  //Check if libsodium is ready and then proceed. sodium.ready.then(() &#x3D;&gt; {   // Convert Secret &amp; Base64 key to Uint8Array.   let binkey &#x3D; sodium.from_base64(key, sodium.base64_variants.ORIGINAL)   let binsec &#x3D; sodium.from_string(secret)    //Encrypt the secret using LibSodium   let encBytes &#x3D; sodium.crypto_box_seal(binsec, binkey)    // Convert encrypted Uint8Array to Base64   let output &#x3D; sodium.to_base64(encBytes, sodium.base64_variants.ORIGINAL)    console.log(output) }); &#x60;&#x60;&#x60;  #### Example encrypting a secret using Python  Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/latest/public/#nacl-public-sealedbox) with Python 3.  &#x60;&#x60;&#x60; from base64 import b64encode from nacl import encoding, public  def encrypt(public_key: str, secret_value: str) -&gt; str:   \&quot;\&quot;\&quot;Encrypt a Unicode string using the public key.\&quot;\&quot;\&quot;   public_key &#x3D; public.PublicKey(public_key.encode(\&quot;utf-8\&quot;), encoding.Base64Encoder())   sealed_box &#x3D; public.SealedBox(public_key)   encrypted &#x3D; sealed_box.encrypt(secret_value.encode(\&quot;utf-8\&quot;))   return b64encode(encrypted).decode(\&quot;utf-8\&quot;) &#x60;&#x60;&#x60;  #### Example encrypting a secret using C#  Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.  &#x60;&#x60;&#x60; var secretValue &#x3D; System.Text.Encoding.UTF8.GetBytes(\&quot;mySecret\&quot;); var publicKey &#x3D; Convert.FromBase64String(\&quot;2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU&#x3D;\&quot;);  var sealedPublicKeyBox &#x3D; Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);  Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox)); &#x60;&#x60;&#x60;  #### Example encrypting a secret using Ruby  Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.  &#x60;&#x60;&#x60;ruby require \&quot;rbnacl\&quot; require \&quot;base64\&quot;  key &#x3D; Base64.decode64(\&quot;+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0&#x3D;\&quot;) public_key &#x3D; RbNaCl::PublicKey.new(key)  box &#x3D; RbNaCl::Boxes::Sealed.from_public_key(public_key) encrypted_secret &#x3D; box.encrypt(\&quot;my_secret\&quot;)  # Print the base64 encoded secret puts Base64.strict_encode64(encrypted_secret) &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    String secretName = "secretName_example"; // String | The name of the secret.
    ActionsCreateOrUpdateOrgSecretRequest actionsCreateOrUpdateOrgSecretRequest = new ActionsCreateOrUpdateOrgSecretRequest(); // ActionsCreateOrUpdateOrgSecretRequest | 
    try {
      Object result = apiInstance.actionsCreateOrUpdateOrgSecret(org, secretName, actionsCreateOrUpdateOrgSecretRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsCreateOrUpdateOrgSecret");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **secretName** | **String**| The name of the secret. | |
| **actionsCreateOrUpdateOrgSecretRequest** | [**ActionsCreateOrUpdateOrgSecretRequest**](ActionsCreateOrUpdateOrgSecretRequest.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response when creating a secret |  -  |
| **204** | Response when updating a secret |  -  |

<a id="actionsCreateOrUpdateRepoSecret"></a>
# **actionsCreateOrUpdateRepoSecret**
> Object actionsCreateOrUpdateRepoSecret(owner, repo, secretName, actionsCreateOrUpdateRepoSecretRequest)

Create or update a repository secret

Creates or updates a repository secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.  #### Example encrypting a secret using Node.js  Encrypt your secret using the [libsodium-wrappers](https://www.npmjs.com/package/libsodium-wrappers) library.  &#x60;&#x60;&#x60; const sodium &#x3D; require(&#39;libsodium-wrappers&#39;) const secret &#x3D; &#39;plain-text-secret&#39; // replace with the secret you want to encrypt const key &#x3D; &#39;base64-encoded-public-key&#39; // replace with the Base64 encoded public key  //Check if libsodium is ready and then proceed. sodium.ready.then(() &#x3D;&gt; {   // Convert Secret &amp; Base64 key to Uint8Array.   let binkey &#x3D; sodium.from_base64(key, sodium.base64_variants.ORIGINAL)   let binsec &#x3D; sodium.from_string(secret)    //Encrypt the secret using LibSodium   let encBytes &#x3D; sodium.crypto_box_seal(binsec, binkey)    // Convert encrypted Uint8Array to Base64   let output &#x3D; sodium.to_base64(encBytes, sodium.base64_variants.ORIGINAL)    console.log(output) }); &#x60;&#x60;&#x60;  #### Example encrypting a secret using Python  Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/latest/public/#nacl-public-sealedbox) with Python 3.  &#x60;&#x60;&#x60; from base64 import b64encode from nacl import encoding, public  def encrypt(public_key: str, secret_value: str) -&gt; str:   \&quot;\&quot;\&quot;Encrypt a Unicode string using the public key.\&quot;\&quot;\&quot;   public_key &#x3D; public.PublicKey(public_key.encode(\&quot;utf-8\&quot;), encoding.Base64Encoder())   sealed_box &#x3D; public.SealedBox(public_key)   encrypted &#x3D; sealed_box.encrypt(secret_value.encode(\&quot;utf-8\&quot;))   return b64encode(encrypted).decode(\&quot;utf-8\&quot;) &#x60;&#x60;&#x60;  #### Example encrypting a secret using C#  Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.  &#x60;&#x60;&#x60; var secretValue &#x3D; System.Text.Encoding.UTF8.GetBytes(\&quot;mySecret\&quot;); var publicKey &#x3D; Convert.FromBase64String(\&quot;2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU&#x3D;\&quot;);  var sealedPublicKeyBox &#x3D; Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);  Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox)); &#x60;&#x60;&#x60;  #### Example encrypting a secret using Ruby  Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.  &#x60;&#x60;&#x60;ruby require \&quot;rbnacl\&quot; require \&quot;base64\&quot;  key &#x3D; Base64.decode64(\&quot;+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0&#x3D;\&quot;) public_key &#x3D; RbNaCl::PublicKey.new(key)  box &#x3D; RbNaCl::Boxes::Sealed.from_public_key(public_key) encrypted_secret &#x3D; box.encrypt(\&quot;my_secret\&quot;)  # Print the base64 encoded secret puts Base64.strict_encode64(encrypted_secret) &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    String secretName = "secretName_example"; // String | The name of the secret.
    ActionsCreateOrUpdateRepoSecretRequest actionsCreateOrUpdateRepoSecretRequest = new ActionsCreateOrUpdateRepoSecretRequest(); // ActionsCreateOrUpdateRepoSecretRequest | 
    try {
      Object result = apiInstance.actionsCreateOrUpdateRepoSecret(owner, repo, secretName, actionsCreateOrUpdateRepoSecretRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsCreateOrUpdateRepoSecret");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **secretName** | **String**| The name of the secret. | |
| **actionsCreateOrUpdateRepoSecretRequest** | [**ActionsCreateOrUpdateRepoSecretRequest**](ActionsCreateOrUpdateRepoSecretRequest.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response when creating a secret |  -  |
| **204** | Response when updating a secret |  -  |

<a id="actionsCreateRegistrationTokenForOrg"></a>
# **actionsCreateRegistrationTokenForOrg**
> AuthenticationToken actionsCreateRegistrationTokenForOrg(org)

Create a registration token for an organization

Returns a token that you can pass to the &#x60;config&#x60; script. The token expires after one hour.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.  #### Example using registration token  Configure your self-hosted runner, replacing &#x60;TOKEN&#x60; with the registration token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh --url https://github.com/octo-org --token TOKEN &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    try {
      AuthenticationToken result = apiInstance.actionsCreateRegistrationTokenForOrg(org);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsCreateRegistrationTokenForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |

### Return type

[**AuthenticationToken**](AuthenticationToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="actionsCreateRegistrationTokenForRepo"></a>
# **actionsCreateRegistrationTokenForRepo**
> AuthenticationToken actionsCreateRegistrationTokenForRepo(owner, repo)

Create a registration token for a repository

Returns a token that you can pass to the &#x60;config&#x60; script. The token expires after one hour. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint.  #### Example using registration token   Configure your self-hosted runner, replacing &#x60;TOKEN&#x60; with the registration token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh --url https://github.com/octo-org/octo-repo-artifacts --token TOKEN &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    try {
      AuthenticationToken result = apiInstance.actionsCreateRegistrationTokenForRepo(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsCreateRegistrationTokenForRepo");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |

### Return type

[**AuthenticationToken**](AuthenticationToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="actionsCreateRemoveTokenForOrg"></a>
# **actionsCreateRemoveTokenForOrg**
> AuthenticationToken actionsCreateRemoveTokenForOrg(org)

Create a remove token for an organization

Returns a token that you can pass to the &#x60;config&#x60; script to remove a self-hosted runner from an organization. The token expires after one hour.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.  #### Example using remove token  To remove your self-hosted runner from an organization, replace &#x60;TOKEN&#x60; with the remove token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh remove --token TOKEN &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    try {
      AuthenticationToken result = apiInstance.actionsCreateRemoveTokenForOrg(org);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsCreateRemoveTokenForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |

### Return type

[**AuthenticationToken**](AuthenticationToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="actionsCreateRemoveTokenForRepo"></a>
# **actionsCreateRemoveTokenForRepo**
> AuthenticationToken actionsCreateRemoveTokenForRepo(owner, repo)

Create a remove token for a repository

Returns a token that you can pass to remove a self-hosted runner from a repository. The token expires after one hour. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint.  #### Example using remove token   To remove your self-hosted runner from a repository, replace TOKEN with the remove token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh remove --token TOKEN &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    try {
      AuthenticationToken result = apiInstance.actionsCreateRemoveTokenForRepo(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsCreateRemoveTokenForRepo");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |

### Return type

[**AuthenticationToken**](AuthenticationToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="actionsCreateSelfHostedRunnerGroupForOrg"></a>
# **actionsCreateSelfHostedRunnerGroupForOrg**
> RunnerGroupsOrg actionsCreateSelfHostedRunnerGroupForOrg(org, actionsCreateSelfHostedRunnerGroupForOrgRequest)

Create a self-hosted runner group for an organization

The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see \&quot;[GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products).\&quot;  Creates a new self-hosted runner group for an organization.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    ActionsCreateSelfHostedRunnerGroupForOrgRequest actionsCreateSelfHostedRunnerGroupForOrgRequest = new ActionsCreateSelfHostedRunnerGroupForOrgRequest(); // ActionsCreateSelfHostedRunnerGroupForOrgRequest | 
    try {
      RunnerGroupsOrg result = apiInstance.actionsCreateSelfHostedRunnerGroupForOrg(org, actionsCreateSelfHostedRunnerGroupForOrgRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsCreateSelfHostedRunnerGroupForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **actionsCreateSelfHostedRunnerGroupForOrgRequest** | [**ActionsCreateSelfHostedRunnerGroupForOrgRequest**](ActionsCreateSelfHostedRunnerGroupForOrgRequest.md)|  | |

### Return type

[**RunnerGroupsOrg**](RunnerGroupsOrg.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="actionsCreateWorkflowDispatch"></a>
# **actionsCreateWorkflowDispatch**
> actionsCreateWorkflowDispatch(owner, repo, workflowId, actionsCreateWorkflowDispatchRequest)

Create a workflow dispatch event

You can use this endpoint to manually trigger a GitHub Actions workflow run. You can replace &#x60;workflow_id&#x60; with the workflow file name. For example, you could use &#x60;main.yaml&#x60;.  You must configure your GitHub Actions workflow to run when the [&#x60;workflow_dispatch&#x60; webhook](/developers/webhooks-and-events/webhook-events-and-payloads#workflow_dispatch) event occurs. The &#x60;inputs&#x60; are configured in the workflow file. For more information about how to configure the &#x60;workflow_dispatch&#x60; event in the workflow file, see \&quot;[Events that trigger workflows](/actions/reference/events-that-trigger-workflows#workflow_dispatch).\&quot;  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint. For more information, see \&quot;[Creating a personal access token for the command line](https://docs.github.com/articles/creating-a-personal-access-token-for-the-command-line).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    ActionsGetWorkflowWorkflowIdParameter workflowId = new ActionsGetWorkflowWorkflowIdParameter(); // ActionsGetWorkflowWorkflowIdParameter | The ID of the workflow. You can also pass the workflow file name as a string.
    ActionsCreateWorkflowDispatchRequest actionsCreateWorkflowDispatchRequest = new ActionsCreateWorkflowDispatchRequest(); // ActionsCreateWorkflowDispatchRequest | 
    try {
      apiInstance.actionsCreateWorkflowDispatch(owner, repo, workflowId, actionsCreateWorkflowDispatchRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsCreateWorkflowDispatch");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **workflowId** | [**ActionsGetWorkflowWorkflowIdParameter**](.md)| The ID of the workflow. You can also pass the workflow file name as a string. | |
| **actionsCreateWorkflowDispatchRequest** | [**ActionsCreateWorkflowDispatchRequest**](ActionsCreateWorkflowDispatchRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsDeleteArtifact"></a>
# **actionsDeleteArtifact**
> actionsDeleteArtifact(owner, repo, artifactId)

Delete an artifact

Deletes an artifact for a workflow run. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer artifactId = 56; // Integer | The unique identifier of the artifact.
    try {
      apiInstance.actionsDeleteArtifact(owner, repo, artifactId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDeleteArtifact");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **artifactId** | **Integer**| The unique identifier of the artifact. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsDeleteEnvironmentSecret"></a>
# **actionsDeleteEnvironmentSecret**
> actionsDeleteEnvironmentSecret(repositoryId, environmentName, secretName)

Delete an environment secret

Deletes a secret in an environment using the secret name. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    Integer repositoryId = 56; // Integer | The unique identifier of the repository.
    String environmentName = "environmentName_example"; // String | The name of the environment.
    String secretName = "secretName_example"; // String | The name of the secret.
    try {
      apiInstance.actionsDeleteEnvironmentSecret(repositoryId, environmentName, secretName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDeleteEnvironmentSecret");
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
| **repositoryId** | **Integer**| The unique identifier of the repository. | |
| **environmentName** | **String**| The name of the environment. | |
| **secretName** | **String**| The name of the secret. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Default response |  -  |

<a id="actionsDeleteOrgSecret"></a>
# **actionsDeleteOrgSecret**
> actionsDeleteOrgSecret(org, secretName)

Delete an organization secret

Deletes a secret in an organization using the secret name. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    String secretName = "secretName_example"; // String | The name of the secret.
    try {
      apiInstance.actionsDeleteOrgSecret(org, secretName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDeleteOrgSecret");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **secretName** | **String**| The name of the secret. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsDeleteRepoSecret"></a>
# **actionsDeleteRepoSecret**
> actionsDeleteRepoSecret(owner, repo, secretName)

Delete a repository secret

Deletes a secret in a repository using the secret name. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    String secretName = "secretName_example"; // String | The name of the secret.
    try {
      apiInstance.actionsDeleteRepoSecret(owner, repo, secretName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDeleteRepoSecret");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **secretName** | **String**| The name of the secret. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsDeleteSelfHostedRunnerFromOrg"></a>
# **actionsDeleteSelfHostedRunnerFromOrg**
> actionsDeleteSelfHostedRunnerFromOrg(org, runnerId)

Delete a self-hosted runner from an organization

Forces the removal of a self-hosted runner from an organization. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    try {
      apiInstance.actionsDeleteSelfHostedRunnerFromOrg(org, runnerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDeleteSelfHostedRunnerFromOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **runnerId** | **Integer**| Unique identifier of the self-hosted runner. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsDeleteSelfHostedRunnerFromRepo"></a>
# **actionsDeleteSelfHostedRunnerFromRepo**
> actionsDeleteSelfHostedRunnerFromRepo(owner, repo, runnerId)

Delete a self-hosted runner from a repository

Forces the removal of a self-hosted runner from a repository. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    try {
      apiInstance.actionsDeleteSelfHostedRunnerFromRepo(owner, repo, runnerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDeleteSelfHostedRunnerFromRepo");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **runnerId** | **Integer**| Unique identifier of the self-hosted runner. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsDeleteSelfHostedRunnerGroupFromOrg"></a>
# **actionsDeleteSelfHostedRunnerGroupFromOrg**
> actionsDeleteSelfHostedRunnerGroupFromOrg(org, runnerGroupId)

Delete a self-hosted runner group from an organization

Deletes a self-hosted runner group for an organization. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    try {
      apiInstance.actionsDeleteSelfHostedRunnerGroupFromOrg(org, runnerGroupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDeleteSelfHostedRunnerGroupFromOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsDeleteWorkflowRun"></a>
# **actionsDeleteWorkflowRun**
> actionsDeleteWorkflowRun(owner, repo, runId)

Delete a workflow run

Delete a specific workflow run. Anyone with write access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer runId = 56; // Integer | The unique identifier of the workflow run.
    try {
      apiInstance.actionsDeleteWorkflowRun(owner, repo, runId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDeleteWorkflowRun");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **runId** | **Integer**| The unique identifier of the workflow run. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsDeleteWorkflowRunLogs"></a>
# **actionsDeleteWorkflowRunLogs**
> actionsDeleteWorkflowRunLogs(owner, repo, runId)

Delete workflow run logs

Deletes all logs for a workflow run. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer runId = 56; // Integer | The unique identifier of the workflow run.
    try {
      apiInstance.actionsDeleteWorkflowRunLogs(owner, repo, runId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDeleteWorkflowRunLogs");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **runId** | **Integer**| The unique identifier of the workflow run. | |

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
| **204** | Response |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Error |  -  |

<a id="actionsDisableSelectedRepositoryGithubActionsOrganization"></a>
# **actionsDisableSelectedRepositoryGithubActionsOrganization**
> actionsDisableSelectedRepositoryGithubActionsOrganization(org, repositoryId)

Disable a selected repository for GitHub Actions in an organization

Removes a repository from the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for &#x60;enabled_repositories&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).\&quot;  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;administration&#x60; organization permission to use this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer repositoryId = 56; // Integer | The unique identifier of the repository.
    try {
      apiInstance.actionsDisableSelectedRepositoryGithubActionsOrganization(org, repositoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDisableSelectedRepositoryGithubActionsOrganization");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **repositoryId** | **Integer**| The unique identifier of the repository. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsDisableWorkflow"></a>
# **actionsDisableWorkflow**
> actionsDisableWorkflow(owner, repo, workflowId)

Disable a workflow

Disables a workflow and sets the &#x60;state&#x60; of the workflow to &#x60;disabled_manually&#x60;. You can replace &#x60;workflow_id&#x60; with the workflow file name. For example, you could use &#x60;main.yaml&#x60;.  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    ActionsGetWorkflowWorkflowIdParameter workflowId = new ActionsGetWorkflowWorkflowIdParameter(); // ActionsGetWorkflowWorkflowIdParameter | The ID of the workflow. You can also pass the workflow file name as a string.
    try {
      apiInstance.actionsDisableWorkflow(owner, repo, workflowId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDisableWorkflow");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **workflowId** | [**ActionsGetWorkflowWorkflowIdParameter**](.md)| The ID of the workflow. You can also pass the workflow file name as a string. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsDownloadArtifact"></a>
# **actionsDownloadArtifact**
> actionsDownloadArtifact(owner, repo, artifactId, archiveFormat)

Download an artifact

Gets a redirect URL to download an archive for a repository. This URL expires after 1 minute. Look for &#x60;Location:&#x60; in the response header to find the URL for the download. The &#x60;:archive_format&#x60; must be &#x60;zip&#x60;. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer artifactId = 56; // Integer | The unique identifier of the artifact.
    String archiveFormat = "archiveFormat_example"; // String | 
    try {
      apiInstance.actionsDownloadArtifact(owner, repo, artifactId, archiveFormat);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDownloadArtifact");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **artifactId** | **Integer**| The unique identifier of the artifact. | |
| **archiveFormat** | **String**|  | |

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
| **302** | Response |  * Location -  <br>  |
| **410** | Gone |  -  |

<a id="actionsDownloadJobLogsForWorkflowRun"></a>
# **actionsDownloadJobLogsForWorkflowRun**
> actionsDownloadJobLogsForWorkflowRun(owner, repo, jobId)

Download job logs for a workflow run

Gets a redirect URL to download a plain text file of logs for a workflow job. This link expires after 1 minute. Look for &#x60;Location:&#x60; in the response header to find the URL for the download. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer jobId = 56; // Integer | The unique identifier of the job.
    try {
      apiInstance.actionsDownloadJobLogsForWorkflowRun(owner, repo, jobId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDownloadJobLogsForWorkflowRun");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **jobId** | **Integer**| The unique identifier of the job. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Response |  * Location -  <br>  |

<a id="actionsDownloadWorkflowRunLogs"></a>
# **actionsDownloadWorkflowRunLogs**
> actionsDownloadWorkflowRunLogs(owner, repo, runId)

Download workflow run logs

Gets a redirect URL to download an archive of log files for a workflow run. This link expires after 1 minute. Look for &#x60;Location:&#x60; in the response header to find the URL for the download. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer runId = 56; // Integer | The unique identifier of the workflow run.
    try {
      apiInstance.actionsDownloadWorkflowRunLogs(owner, repo, runId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsDownloadWorkflowRunLogs");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **runId** | **Integer**| The unique identifier of the workflow run. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Response |  * Location -  <br>  |

<a id="actionsEnableSelectedRepositoryGithubActionsOrganization"></a>
# **actionsEnableSelectedRepositoryGithubActionsOrganization**
> actionsEnableSelectedRepositoryGithubActionsOrganization(org, repositoryId)

Enable a selected repository for GitHub Actions in an organization

Adds a repository to the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for &#x60;enabled_repositories&#x60; must be must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).\&quot;  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;administration&#x60; organization permission to use this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer repositoryId = 56; // Integer | The unique identifier of the repository.
    try {
      apiInstance.actionsEnableSelectedRepositoryGithubActionsOrganization(org, repositoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsEnableSelectedRepositoryGithubActionsOrganization");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **repositoryId** | **Integer**| The unique identifier of the repository. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsEnableWorkflow"></a>
# **actionsEnableWorkflow**
> actionsEnableWorkflow(owner, repo, workflowId)

Enable a workflow

Enables a workflow and sets the &#x60;state&#x60; of the workflow to &#x60;active&#x60;. You can replace &#x60;workflow_id&#x60; with the workflow file name. For example, you could use &#x60;main.yaml&#x60;.  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    ActionsGetWorkflowWorkflowIdParameter workflowId = new ActionsGetWorkflowWorkflowIdParameter(); // ActionsGetWorkflowWorkflowIdParameter | The ID of the workflow. You can also pass the workflow file name as a string.
    try {
      apiInstance.actionsEnableWorkflow(owner, repo, workflowId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsEnableWorkflow");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **workflowId** | [**ActionsGetWorkflowWorkflowIdParameter**](.md)| The ID of the workflow. You can also pass the workflow file name as a string. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsGetAllowedActionsOrganization"></a>
# **actionsGetAllowedActionsOrganization**
> SelectedActions actionsGetAllowedActionsOrganization(org)

Get allowed actions for an organization

Gets the selected actions that are allowed in an organization. To use this endpoint, the organization permission policy for &#x60;allowed_actions&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).\&quot;\&quot;  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;administration&#x60; organization permission to use this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    try {
      SelectedActions result = apiInstance.actionsGetAllowedActionsOrganization(org);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetAllowedActionsOrganization");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |

### Return type

[**SelectedActions**](SelectedActions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetAllowedActionsRepository"></a>
# **actionsGetAllowedActionsRepository**
> SelectedActions actionsGetAllowedActionsRepository(owner, repo)

Get allowed actions for a repository

Gets the settings for selected actions that are allowed in a repository. To use this endpoint, the repository policy for &#x60;allowed_actions&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for a repository](#set-github-actions-permissions-for-a-repository).\&quot;  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;administration&#x60; repository permission to use this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    try {
      SelectedActions result = apiInstance.actionsGetAllowedActionsRepository(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetAllowedActionsRepository");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |

### Return type

[**SelectedActions**](SelectedActions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetArtifact"></a>
# **actionsGetArtifact**
> Artifact actionsGetArtifact(owner, repo, artifactId)

Get an artifact

Gets a specific artifact for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer artifactId = 56; // Integer | The unique identifier of the artifact.
    try {
      Artifact result = apiInstance.actionsGetArtifact(owner, repo, artifactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetArtifact");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **artifactId** | **Integer**| The unique identifier of the artifact. | |

### Return type

[**Artifact**](Artifact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetEnvironmentPublicKey"></a>
# **actionsGetEnvironmentPublicKey**
> ActionsPublicKey actionsGetEnvironmentPublicKey(repositoryId, environmentName)

Get an environment public key

Get the public key for an environment, which you need to encrypt environment secrets. You need to encrypt a secret before you can create or update secrets. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    Integer repositoryId = 56; // Integer | The unique identifier of the repository.
    String environmentName = "environmentName_example"; // String | The name of the environment.
    try {
      ActionsPublicKey result = apiInstance.actionsGetEnvironmentPublicKey(repositoryId, environmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetEnvironmentPublicKey");
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
| **repositoryId** | **Integer**| The unique identifier of the repository. | |
| **environmentName** | **String**| The name of the environment. | |

### Return type

[**ActionsPublicKey**](ActionsPublicKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetEnvironmentSecret"></a>
# **actionsGetEnvironmentSecret**
> ActionsSecret actionsGetEnvironmentSecret(repositoryId, environmentName, secretName)

Get an environment secret

Gets a single environment secret without revealing its encrypted value. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    Integer repositoryId = 56; // Integer | The unique identifier of the repository.
    String environmentName = "environmentName_example"; // String | The name of the environment.
    String secretName = "secretName_example"; // String | The name of the secret.
    try {
      ActionsSecret result = apiInstance.actionsGetEnvironmentSecret(repositoryId, environmentName, secretName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetEnvironmentSecret");
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
| **repositoryId** | **Integer**| The unique identifier of the repository. | |
| **environmentName** | **String**| The name of the environment. | |
| **secretName** | **String**| The name of the secret. | |

### Return type

[**ActionsSecret**](ActionsSecret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetGithubActionsPermissionsOrganization"></a>
# **actionsGetGithubActionsPermissionsOrganization**
> ActionsOrganizationPermissions actionsGetGithubActionsPermissionsOrganization(org)

Get GitHub Actions permissions for an organization

Gets the GitHub Actions permissions policy for repositories and allowed actions in an organization.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;administration&#x60; organization permission to use this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    try {
      ActionsOrganizationPermissions result = apiInstance.actionsGetGithubActionsPermissionsOrganization(org);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetGithubActionsPermissionsOrganization");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |

### Return type

[**ActionsOrganizationPermissions**](ActionsOrganizationPermissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetGithubActionsPermissionsRepository"></a>
# **actionsGetGithubActionsPermissionsRepository**
> ActionsRepositoryPermissions actionsGetGithubActionsPermissionsRepository(owner, repo)

Get GitHub Actions permissions for a repository

Gets the GitHub Actions permissions policy for a repository, including whether GitHub Actions is enabled and the actions allowed to run in the repository.  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;administration&#x60; repository permission to use this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    try {
      ActionsRepositoryPermissions result = apiInstance.actionsGetGithubActionsPermissionsRepository(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetGithubActionsPermissionsRepository");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |

### Return type

[**ActionsRepositoryPermissions**](ActionsRepositoryPermissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetJobForWorkflowRun"></a>
# **actionsGetJobForWorkflowRun**
> Job actionsGetJobForWorkflowRun(owner, repo, jobId)

Get a job for a workflow run

Gets a specific job in a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer jobId = 56; // Integer | The unique identifier of the job.
    try {
      Job result = apiInstance.actionsGetJobForWorkflowRun(owner, repo, jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetJobForWorkflowRun");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **jobId** | **Integer**| The unique identifier of the job. | |

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetOrgPublicKey"></a>
# **actionsGetOrgPublicKey**
> ActionsPublicKey actionsGetOrgPublicKey(org)

Get an organization public key

Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    try {
      ActionsPublicKey result = apiInstance.actionsGetOrgPublicKey(org);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetOrgPublicKey");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |

### Return type

[**ActionsPublicKey**](ActionsPublicKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetOrgSecret"></a>
# **actionsGetOrgSecret**
> OrganizationActionsSecret actionsGetOrgSecret(org, secretName)

Get an organization secret

Gets a single organization secret without revealing its encrypted value. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    String secretName = "secretName_example"; // String | The name of the secret.
    try {
      OrganizationActionsSecret result = apiInstance.actionsGetOrgSecret(org, secretName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetOrgSecret");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **secretName** | **String**| The name of the secret. | |

### Return type

[**OrganizationActionsSecret**](OrganizationActionsSecret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetPendingDeploymentsForRun"></a>
# **actionsGetPendingDeploymentsForRun**
> List&lt;PendingDeployment&gt; actionsGetPendingDeploymentsForRun(owner, repo, runId)

Get pending deployments for a workflow run

Get all deployment environments for a workflow run that are waiting for protection rules to pass.  Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer runId = 56; // Integer | The unique identifier of the workflow run.
    try {
      List<PendingDeployment> result = apiInstance.actionsGetPendingDeploymentsForRun(owner, repo, runId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetPendingDeploymentsForRun");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **runId** | **Integer**| The unique identifier of the workflow run. | |

### Return type

[**List&lt;PendingDeployment&gt;**](PendingDeployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetRepoPublicKey"></a>
# **actionsGetRepoPublicKey**
> ActionsPublicKey actionsGetRepoPublicKey(owner, repo)

Get a repository public key

Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    try {
      ActionsPublicKey result = apiInstance.actionsGetRepoPublicKey(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetRepoPublicKey");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |

### Return type

[**ActionsPublicKey**](ActionsPublicKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetRepoSecret"></a>
# **actionsGetRepoSecret**
> ActionsSecret actionsGetRepoSecret(owner, repo, secretName)

Get a repository secret

Gets a single repository secret without revealing its encrypted value. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    String secretName = "secretName_example"; // String | The name of the secret.
    try {
      ActionsSecret result = apiInstance.actionsGetRepoSecret(owner, repo, secretName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetRepoSecret");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **secretName** | **String**| The name of the secret. | |

### Return type

[**ActionsSecret**](ActionsSecret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetReviewsForRun"></a>
# **actionsGetReviewsForRun**
> List&lt;EnvironmentApprovals&gt; actionsGetReviewsForRun(owner, repo, runId)

Get the review history for a workflow run

Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer runId = 56; // Integer | The unique identifier of the workflow run.
    try {
      List<EnvironmentApprovals> result = apiInstance.actionsGetReviewsForRun(owner, repo, runId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetReviewsForRun");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **runId** | **Integer**| The unique identifier of the workflow run. | |

### Return type

[**List&lt;EnvironmentApprovals&gt;**](EnvironmentApprovals.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetSelfHostedRunnerForOrg"></a>
# **actionsGetSelfHostedRunnerForOrg**
> Runner actionsGetSelfHostedRunnerForOrg(org, runnerId)

Get a self-hosted runner for an organization

Gets a specific self-hosted runner configured in an organization.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    try {
      Runner result = apiInstance.actionsGetSelfHostedRunnerForOrg(org, runnerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetSelfHostedRunnerForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **runnerId** | **Integer**| Unique identifier of the self-hosted runner. | |

### Return type

[**Runner**](Runner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetSelfHostedRunnerForRepo"></a>
# **actionsGetSelfHostedRunnerForRepo**
> Runner actionsGetSelfHostedRunnerForRepo(owner, repo, runnerId)

Get a self-hosted runner for a repository

Gets a specific self-hosted runner configured in a repository.  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    try {
      Runner result = apiInstance.actionsGetSelfHostedRunnerForRepo(owner, repo, runnerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetSelfHostedRunnerForRepo");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **runnerId** | **Integer**| Unique identifier of the self-hosted runner. | |

### Return type

[**Runner**](Runner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetSelfHostedRunnerGroupForOrg"></a>
# **actionsGetSelfHostedRunnerGroupForOrg**
> RunnerGroupsOrg actionsGetSelfHostedRunnerGroupForOrg(org, runnerGroupId)

Get a self-hosted runner group for an organization

Gets a specific self-hosted runner group for an organization. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    try {
      RunnerGroupsOrg result = apiInstance.actionsGetSelfHostedRunnerGroupForOrg(org, runnerGroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetSelfHostedRunnerGroupForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |

### Return type

[**RunnerGroupsOrg**](RunnerGroupsOrg.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetWorkflow"></a>
# **actionsGetWorkflow**
> Workflow actionsGetWorkflow(owner, repo, workflowId)

Get a workflow

Gets a specific workflow. You can replace &#x60;workflow_id&#x60; with the workflow file name. For example, you could use &#x60;main.yaml&#x60;. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    ActionsGetWorkflowWorkflowIdParameter workflowId = new ActionsGetWorkflowWorkflowIdParameter(); // ActionsGetWorkflowWorkflowIdParameter | The ID of the workflow. You can also pass the workflow file name as a string.
    try {
      Workflow result = apiInstance.actionsGetWorkflow(owner, repo, workflowId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetWorkflow");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **workflowId** | [**ActionsGetWorkflowWorkflowIdParameter**](.md)| The ID of the workflow. You can also pass the workflow file name as a string. | |

### Return type

[**Workflow**](Workflow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsGetWorkflowRun"></a>
# **actionsGetWorkflowRun**
> WorkflowRun actionsGetWorkflowRun(owner, repo, runId, excludePullRequests)

Get a workflow run

Gets a specific workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer runId = 56; // Integer | The unique identifier of the workflow run.
    Boolean excludePullRequests = false; // Boolean | If `true` pull requests are omitted from the response (empty array).
    try {
      WorkflowRun result = apiInstance.actionsGetWorkflowRun(owner, repo, runId, excludePullRequests);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGetWorkflowRun");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **runId** | **Integer**| The unique identifier of the workflow run. | |
| **excludePullRequests** | **Boolean**| If &#x60;true&#x60; pull requests are omitted from the response (empty array). | [optional] [default to false] |

### Return type

[**WorkflowRun**](WorkflowRun.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsListArtifactsForRepo"></a>
# **actionsListArtifactsForRepo**
> ActionsListArtifactsForRepo200Response actionsListArtifactsForRepo(owner, repo, perPage, page, name)

List artifacts for a repository

Lists all artifacts for a repository. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    String name = "name_example"; // String | Filters artifacts by exact match on their name field.
    try {
      ActionsListArtifactsForRepo200Response result = apiInstance.actionsListArtifactsForRepo(owner, repo, perPage, page, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListArtifactsForRepo");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **name** | **String**| Filters artifacts by exact match on their name field. | [optional] |

### Return type

[**ActionsListArtifactsForRepo200Response**](ActionsListArtifactsForRepo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="actionsListEnvironmentSecrets"></a>
# **actionsListEnvironmentSecrets**
> ActionsListRepoSecrets200Response actionsListEnvironmentSecrets(repositoryId, environmentName, perPage, page)

List environment secrets

Lists all secrets available in an environment without revealing their encrypted values. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    Integer repositoryId = 56; // Integer | The unique identifier of the repository.
    String environmentName = "environmentName_example"; // String | The name of the environment.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      ActionsListRepoSecrets200Response result = apiInstance.actionsListEnvironmentSecrets(repositoryId, environmentName, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListEnvironmentSecrets");
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
| **repositoryId** | **Integer**| The unique identifier of the repository. | |
| **environmentName** | **String**| The name of the environment. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**ActionsListRepoSecrets200Response**](ActionsListRepoSecrets200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="actionsListJobsForWorkflowRun"></a>
# **actionsListJobsForWorkflowRun**
> ActionsListJobsForWorkflowRun200Response actionsListJobsForWorkflowRun(owner, repo, runId, filter, perPage, page)

List jobs for a workflow run

Lists jobs for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@3.2/rest/overview/resources-in-the-rest-api#parameters).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer runId = 56; // Integer | The unique identifier of the workflow run.
    String filter = "latest"; // String | Filters jobs by their `completed_at` timestamp. `latest` returns jobs from the most recent execution of the workflow run. `all` returns all jobs for a workflow run, including from old executions of the workflow run.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      ActionsListJobsForWorkflowRun200Response result = apiInstance.actionsListJobsForWorkflowRun(owner, repo, runId, filter, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListJobsForWorkflowRun");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **runId** | **Integer**| The unique identifier of the workflow run. | |
| **filter** | **String**| Filters jobs by their &#x60;completed_at&#x60; timestamp. &#x60;latest&#x60; returns jobs from the most recent execution of the workflow run. &#x60;all&#x60; returns all jobs for a workflow run, including from old executions of the workflow run. | [optional] [default to latest] [enum: latest, all] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**ActionsListJobsForWorkflowRun200Response**](ActionsListJobsForWorkflowRun200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="actionsListOrgSecrets"></a>
# **actionsListOrgSecrets**
> ActionsListOrgSecrets200Response actionsListOrgSecrets(org, perPage, page)

List organization secrets

Lists all secrets available in an organization without revealing their encrypted values. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      ActionsListOrgSecrets200Response result = apiInstance.actionsListOrgSecrets(org, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListOrgSecrets");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**ActionsListOrgSecrets200Response**](ActionsListOrgSecrets200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="actionsListRepoAccessToSelfHostedRunnerGroupInOrg"></a>
# **actionsListRepoAccessToSelfHostedRunnerGroupInOrg**
> ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response actionsListRepoAccessToSelfHostedRunnerGroupInOrg(org, runnerGroupId, page, perPage)

List repository access to a self-hosted runner group in an organization

The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see \&quot;[GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products).\&quot;  Lists the repositories with access to a self-hosted runner group configured in an organization.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    Integer page = 1; // Integer | Page number of the results to fetch.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    try {
      ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response result = apiInstance.actionsListRepoAccessToSelfHostedRunnerGroupInOrg(org, runnerGroupId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListRepoAccessToSelfHostedRunnerGroupInOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |

### Return type

[**ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response**](ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsListRepoSecrets"></a>
# **actionsListRepoSecrets**
> ActionsListRepoSecrets200Response actionsListRepoSecrets(owner, repo, perPage, page)

List repository secrets

Lists all secrets available in a repository without revealing their encrypted values. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      ActionsListRepoSecrets200Response result = apiInstance.actionsListRepoSecrets(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListRepoSecrets");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**ActionsListRepoSecrets200Response**](ActionsListRepoSecrets200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="actionsListRepoWorkflows"></a>
# **actionsListRepoWorkflows**
> ActionsListRepoWorkflows200Response actionsListRepoWorkflows(owner, repo, perPage, page)

List repository workflows

Lists the workflows in a repository. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      ActionsListRepoWorkflows200Response result = apiInstance.actionsListRepoWorkflows(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListRepoWorkflows");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**ActionsListRepoWorkflows200Response**](ActionsListRepoWorkflows200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="actionsListRunnerApplicationsForOrg"></a>
# **actionsListRunnerApplicationsForOrg**
> List&lt;RunnerApplication&gt; actionsListRunnerApplicationsForOrg(org)

List runner applications for an organization

Lists binaries for the runner application that you can download and run.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    try {
      List<RunnerApplication> result = apiInstance.actionsListRunnerApplicationsForOrg(org);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListRunnerApplicationsForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |

### Return type

[**List&lt;RunnerApplication&gt;**](RunnerApplication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsListRunnerApplicationsForRepo"></a>
# **actionsListRunnerApplicationsForRepo**
> List&lt;RunnerApplication&gt; actionsListRunnerApplicationsForRepo(owner, repo)

List runner applications for a repository

Lists binaries for the runner application that you can download and run.  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    try {
      List<RunnerApplication> result = apiInstance.actionsListRunnerApplicationsForRepo(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListRunnerApplicationsForRepo");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |

### Return type

[**List&lt;RunnerApplication&gt;**](RunnerApplication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsListSelectedReposForOrgSecret"></a>
# **actionsListSelectedReposForOrgSecret**
> ActionsListSelectedReposForOrgSecret200Response actionsListSelectedReposForOrgSecret(org, secretName, page, perPage)

List selected repositories for an organization secret

Lists all repositories that have been selected when the &#x60;visibility&#x60; for repository access to a secret is set to &#x60;selected&#x60;. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    String secretName = "secretName_example"; // String | The name of the secret.
    Integer page = 1; // Integer | Page number of the results to fetch.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    try {
      ActionsListSelectedReposForOrgSecret200Response result = apiInstance.actionsListSelectedReposForOrgSecret(org, secretName, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListSelectedReposForOrgSecret");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **secretName** | **String**| The name of the secret. | |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |

### Return type

[**ActionsListSelectedReposForOrgSecret200Response**](ActionsListSelectedReposForOrgSecret200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsListSelectedRepositoriesEnabledGithubActionsOrganization"></a>
# **actionsListSelectedRepositoriesEnabledGithubActionsOrganization**
> ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response actionsListSelectedRepositoriesEnabledGithubActionsOrganization(org, perPage, page)

List selected repositories enabled for GitHub Actions in an organization

Lists the selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for &#x60;enabled_repositories&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).\&quot;  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;administration&#x60; organization permission to use this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response result = apiInstance.actionsListSelectedRepositoriesEnabledGithubActionsOrganization(org, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListSelectedRepositoriesEnabledGithubActionsOrganization");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response**](ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsListSelfHostedRunnerGroupsForOrg"></a>
# **actionsListSelfHostedRunnerGroupsForOrg**
> ActionsListSelfHostedRunnerGroupsForOrg200Response actionsListSelfHostedRunnerGroupsForOrg(org, perPage, page)

List self-hosted runner groups for an organization

Lists all self-hosted runner groups configured in an organization and inherited from an enterprise. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      ActionsListSelfHostedRunnerGroupsForOrg200Response result = apiInstance.actionsListSelfHostedRunnerGroupsForOrg(org, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListSelfHostedRunnerGroupsForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**ActionsListSelfHostedRunnerGroupsForOrg200Response**](ActionsListSelfHostedRunnerGroupsForOrg200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsListSelfHostedRunnersForOrg"></a>
# **actionsListSelfHostedRunnersForOrg**
> ActionsListSelfHostedRunnersForOrg200Response actionsListSelfHostedRunnersForOrg(org, perPage, page)

List self-hosted runners for an organization

Lists all self-hosted runners configured in an organization.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      ActionsListSelfHostedRunnersForOrg200Response result = apiInstance.actionsListSelfHostedRunnersForOrg(org, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListSelfHostedRunnersForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**ActionsListSelfHostedRunnersForOrg200Response**](ActionsListSelfHostedRunnersForOrg200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="actionsListSelfHostedRunnersForRepo"></a>
# **actionsListSelfHostedRunnersForRepo**
> ActionsListSelfHostedRunnersForOrg200Response actionsListSelfHostedRunnersForRepo(owner, repo, perPage, page)

List self-hosted runners for a repository

Lists all self-hosted runners configured in a repository. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      ActionsListSelfHostedRunnersForOrg200Response result = apiInstance.actionsListSelfHostedRunnersForRepo(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListSelfHostedRunnersForRepo");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**ActionsListSelfHostedRunnersForOrg200Response**](ActionsListSelfHostedRunnersForOrg200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="actionsListSelfHostedRunnersInGroupForOrg"></a>
# **actionsListSelfHostedRunnersInGroupForOrg**
> EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise200Response actionsListSelfHostedRunnersInGroupForOrg(org, runnerGroupId, perPage, page)

List self-hosted runners in a group for an organization

Lists self-hosted runners that are in a specific organization group. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise200Response result = apiInstance.actionsListSelfHostedRunnersInGroupForOrg(org, runnerGroupId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListSelfHostedRunnersInGroupForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise200Response**](EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="actionsListWorkflowRunArtifacts"></a>
# **actionsListWorkflowRunArtifacts**
> ActionsListArtifactsForRepo200Response actionsListWorkflowRunArtifacts(owner, repo, runId, perPage, page)

List workflow run artifacts

Lists artifacts for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer runId = 56; // Integer | The unique identifier of the workflow run.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      ActionsListArtifactsForRepo200Response result = apiInstance.actionsListWorkflowRunArtifacts(owner, repo, runId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListWorkflowRunArtifacts");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **runId** | **Integer**| The unique identifier of the workflow run. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**ActionsListArtifactsForRepo200Response**](ActionsListArtifactsForRepo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="actionsListWorkflowRuns"></a>
# **actionsListWorkflowRuns**
> ActionsListWorkflowRunsForRepo200Response actionsListWorkflowRuns(owner, repo, workflowId, actor, branch, event, status, perPage, page, created, excludePullRequests)

List workflow runs for a workflow

List all workflow runs for a workflow. You can replace &#x60;workflow_id&#x60; with the workflow file name. For example, you could use &#x60;main.yaml&#x60;. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@3.2/rest/overview/resources-in-the-rest-api#parameters).  Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    ActionsGetWorkflowWorkflowIdParameter workflowId = new ActionsGetWorkflowWorkflowIdParameter(); // ActionsGetWorkflowWorkflowIdParameter | The ID of the workflow. You can also pass the workflow file name as a string.
    String actor = "actor_example"; // String | Returns someone's workflow runs. Use the login for the user who created the `push` associated with the check suite or workflow run.
    String branch = "branch_example"; // String | Returns workflow runs associated with a branch. Use the name of the branch of the `push`.
    String event = "event_example"; // String | Returns workflow run triggered by the event you specify. For example, `push`, `pull_request` or `issue`. For more information, see \"[Events that trigger workflows](https://docs.github.com/en/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows).\"
    String status = "completed"; // String | Returns workflow runs with the check run `status` or `conclusion` that you specify. For example, a conclusion can be `success` or a status can be `in_progress`. Only GitHub can set a status of `waiting` or `requested`.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    OffsetDateTime created = OffsetDateTime.now(); // OffsetDateTime | Returns workflow runs created within the given date-time range. For more information on the syntax, see \"[Understanding the search syntax](https://docs.github.com/enterprise-server@3.2/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\"
    Boolean excludePullRequests = false; // Boolean | If `true` pull requests are omitted from the response (empty array).
    try {
      ActionsListWorkflowRunsForRepo200Response result = apiInstance.actionsListWorkflowRuns(owner, repo, workflowId, actor, branch, event, status, perPage, page, created, excludePullRequests);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListWorkflowRuns");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **workflowId** | [**ActionsGetWorkflowWorkflowIdParameter**](.md)| The ID of the workflow. You can also pass the workflow file name as a string. | |
| **actor** | **String**| Returns someone&#39;s workflow runs. Use the login for the user who created the &#x60;push&#x60; associated with the check suite or workflow run. | [optional] |
| **branch** | **String**| Returns workflow runs associated with a branch. Use the name of the branch of the &#x60;push&#x60;. | [optional] |
| **event** | **String**| Returns workflow run triggered by the event you specify. For example, &#x60;push&#x60;, &#x60;pull_request&#x60; or &#x60;issue&#x60;. For more information, see \&quot;[Events that trigger workflows](https://docs.github.com/en/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows).\&quot; | [optional] |
| **status** | **String**| Returns workflow runs with the check run &#x60;status&#x60; or &#x60;conclusion&#x60; that you specify. For example, a conclusion can be &#x60;success&#x60; or a status can be &#x60;in_progress&#x60;. Only GitHub can set a status of &#x60;waiting&#x60; or &#x60;requested&#x60;. | [optional] [enum: completed, action_required, cancelled, failure, neutral, skipped, stale, success, timed_out, in_progress, queued, requested, waiting] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **created** | **OffsetDateTime**| Returns workflow runs created within the given date-time range. For more information on the syntax, see \&quot;[Understanding the search syntax](https://docs.github.com/enterprise-server@3.2/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\&quot; | [optional] |
| **excludePullRequests** | **Boolean**| If &#x60;true&#x60; pull requests are omitted from the response (empty array). | [optional] [default to false] |

### Return type

[**ActionsListWorkflowRunsForRepo200Response**](ActionsListWorkflowRunsForRepo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="actionsListWorkflowRunsForRepo"></a>
# **actionsListWorkflowRunsForRepo**
> ActionsListWorkflowRunsForRepo200Response actionsListWorkflowRunsForRepo(owner, repo, actor, branch, event, status, perPage, page, created, excludePullRequests)

List workflow runs for a repository

Lists all workflow runs for a repository. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@3.2/rest/overview/resources-in-the-rest-api#parameters).  Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    String actor = "actor_example"; // String | Returns someone's workflow runs. Use the login for the user who created the `push` associated with the check suite or workflow run.
    String branch = "branch_example"; // String | Returns workflow runs associated with a branch. Use the name of the branch of the `push`.
    String event = "event_example"; // String | Returns workflow run triggered by the event you specify. For example, `push`, `pull_request` or `issue`. For more information, see \"[Events that trigger workflows](https://docs.github.com/en/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows).\"
    String status = "completed"; // String | Returns workflow runs with the check run `status` or `conclusion` that you specify. For example, a conclusion can be `success` or a status can be `in_progress`. Only GitHub can set a status of `waiting` or `requested`.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    OffsetDateTime created = OffsetDateTime.now(); // OffsetDateTime | Returns workflow runs created within the given date-time range. For more information on the syntax, see \"[Understanding the search syntax](https://docs.github.com/enterprise-server@3.2/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\"
    Boolean excludePullRequests = false; // Boolean | If `true` pull requests are omitted from the response (empty array).
    try {
      ActionsListWorkflowRunsForRepo200Response result = apiInstance.actionsListWorkflowRunsForRepo(owner, repo, actor, branch, event, status, perPage, page, created, excludePullRequests);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsListWorkflowRunsForRepo");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **actor** | **String**| Returns someone&#39;s workflow runs. Use the login for the user who created the &#x60;push&#x60; associated with the check suite or workflow run. | [optional] |
| **branch** | **String**| Returns workflow runs associated with a branch. Use the name of the branch of the &#x60;push&#x60;. | [optional] |
| **event** | **String**| Returns workflow run triggered by the event you specify. For example, &#x60;push&#x60;, &#x60;pull_request&#x60; or &#x60;issue&#x60;. For more information, see \&quot;[Events that trigger workflows](https://docs.github.com/en/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows).\&quot; | [optional] |
| **status** | **String**| Returns workflow runs with the check run &#x60;status&#x60; or &#x60;conclusion&#x60; that you specify. For example, a conclusion can be &#x60;success&#x60; or a status can be &#x60;in_progress&#x60;. Only GitHub can set a status of &#x60;waiting&#x60; or &#x60;requested&#x60;. | [optional] [enum: completed, action_required, cancelled, failure, neutral, skipped, stale, success, timed_out, in_progress, queued, requested, waiting] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **created** | **OffsetDateTime**| Returns workflow runs created within the given date-time range. For more information on the syntax, see \&quot;[Understanding the search syntax](https://docs.github.com/enterprise-server@3.2/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\&quot; | [optional] |
| **excludePullRequests** | **Boolean**| If &#x60;true&#x60; pull requests are omitted from the response (empty array). | [optional] [default to false] |

### Return type

[**ActionsListWorkflowRunsForRepo200Response**](ActionsListWorkflowRunsForRepo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="actionsReRunWorkflow"></a>
# **actionsReRunWorkflow**
> Object actionsReRunWorkflow(owner, repo, runId, body)

Re-run a workflow

Re-runs your workflow run using its &#x60;id&#x60;. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer runId = 56; // Integer | The unique identifier of the workflow run.
    Object body = null; // Object | 
    try {
      Object result = apiInstance.actionsReRunWorkflow(owner, repo, runId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsReRunWorkflow");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **runId** | **Integer**| The unique identifier of the workflow run. | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="actionsRemoveRepoAccessToSelfHostedRunnerGroupInOrg"></a>
# **actionsRemoveRepoAccessToSelfHostedRunnerGroupInOrg**
> actionsRemoveRepoAccessToSelfHostedRunnerGroupInOrg(org, runnerGroupId, repositoryId)

Remove repository access to a self-hosted runner group in an organization

Removes a repository from the list of selected repositories that can access a self-hosted runner group. The runner group must have &#x60;visibility&#x60; set to &#x60;selected&#x60;. For more information, see \&quot;[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization).\&quot; You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    Integer repositoryId = 56; // Integer | The unique identifier of the repository.
    try {
      apiInstance.actionsRemoveRepoAccessToSelfHostedRunnerGroupInOrg(org, runnerGroupId, repositoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsRemoveRepoAccessToSelfHostedRunnerGroupInOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **repositoryId** | **Integer**| The unique identifier of the repository. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsRemoveSelectedRepoFromOrgSecret"></a>
# **actionsRemoveSelectedRepoFromOrgSecret**
> actionsRemoveSelectedRepoFromOrgSecret(org, secretName, repositoryId)

Remove selected repository from an organization secret

Removes a repository from an organization secret when the &#x60;visibility&#x60; for repository access is set to &#x60;selected&#x60;. The visibility is set when you [Create or update an organization secret](https://docs.github.com/enterprise-server@3.2/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    String secretName = "secretName_example"; // String | The name of the secret.
    Integer repositoryId = 56; // Integer | 
    try {
      apiInstance.actionsRemoveSelectedRepoFromOrgSecret(org, secretName, repositoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsRemoveSelectedRepoFromOrgSecret");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **secretName** | **String**| The name of the secret. | |
| **repositoryId** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response when repository was removed from the selected list |  -  |
| **409** | Conflict when visibility type not set to selected |  -  |

<a id="actionsRemoveSelfHostedRunnerFromGroupForOrg"></a>
# **actionsRemoveSelfHostedRunnerFromGroupForOrg**
> actionsRemoveSelfHostedRunnerFromGroupForOrg(org, runnerGroupId, runnerId)

Remove a self-hosted runner from a group for an organization

Removes a self-hosted runner from a group configured in an organization. The runner is then returned to the default group. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    try {
      apiInstance.actionsRemoveSelfHostedRunnerFromGroupForOrg(org, runnerGroupId, runnerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsRemoveSelfHostedRunnerFromGroupForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **runnerId** | **Integer**| Unique identifier of the self-hosted runner. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsReviewPendingDeploymentsForRun"></a>
# **actionsReviewPendingDeploymentsForRun**
> List&lt;Deployment&gt; actionsReviewPendingDeploymentsForRun(owner, repo, runId, actionsReviewPendingDeploymentsForRunRequest)

Review pending deployments for a workflow run

Approve or reject pending deployments that are waiting on approval by a required reviewer.  Required reviewers with read access to the repository contents and deployments can use this endpoint. Required reviewers must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer runId = 56; // Integer | The unique identifier of the workflow run.
    ActionsReviewPendingDeploymentsForRunRequest actionsReviewPendingDeploymentsForRunRequest = new ActionsReviewPendingDeploymentsForRunRequest(); // ActionsReviewPendingDeploymentsForRunRequest | 
    try {
      List<Deployment> result = apiInstance.actionsReviewPendingDeploymentsForRun(owner, repo, runId, actionsReviewPendingDeploymentsForRunRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsReviewPendingDeploymentsForRun");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **runId** | **Integer**| The unique identifier of the workflow run. | |
| **actionsReviewPendingDeploymentsForRunRequest** | [**ActionsReviewPendingDeploymentsForRunRequest**](ActionsReviewPendingDeploymentsForRunRequest.md)|  | |

### Return type

[**List&lt;Deployment&gt;**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="actionsSetAllowedActionsOrganization"></a>
# **actionsSetAllowedActionsOrganization**
> actionsSetAllowedActionsOrganization(org, selectedActions)

Set allowed actions for an organization

Sets the actions that are allowed in an organization. To use this endpoint, the organization permission policy for &#x60;allowed_actions&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).\&quot;  If the organization belongs to an enterprise that has &#x60;selected&#x60; actions set at the enterprise level, then you cannot override any of the enterprise&#39;s allowed actions settings.  To use the &#x60;patterns_allowed&#x60; setting for private repositories, the organization must belong to an enterprise. If the organization does not belong to an enterprise, then the &#x60;patterns_allowed&#x60; setting only applies to public repositories in the organization.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;administration&#x60; organization permission to use this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    SelectedActions selectedActions = new SelectedActions(); // SelectedActions | 
    try {
      apiInstance.actionsSetAllowedActionsOrganization(org, selectedActions);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsSetAllowedActionsOrganization");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **selectedActions** | [**SelectedActions**](SelectedActions.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsSetAllowedActionsRepository"></a>
# **actionsSetAllowedActionsRepository**
> actionsSetAllowedActionsRepository(owner, repo, selectedActions)

Set allowed actions for a repository

Sets the actions that are allowed in a repository. To use this endpoint, the repository permission policy for &#x60;allowed_actions&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for a repository](#set-github-actions-permissions-for-a-repository).\&quot;  If the repository belongs to an organization or enterprise that has &#x60;selected&#x60; actions set at the organization or enterprise levels, then you cannot override any of the allowed actions settings.  To use the &#x60;patterns_allowed&#x60; setting for private repositories, the repository must belong to an enterprise. If the repository does not belong to an enterprise, then the &#x60;patterns_allowed&#x60; setting only applies to public repositories.  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;administration&#x60; repository permission to use this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    SelectedActions selectedActions = new SelectedActions(); // SelectedActions | 
    try {
      apiInstance.actionsSetAllowedActionsRepository(owner, repo, selectedActions);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsSetAllowedActionsRepository");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **selectedActions** | [**SelectedActions**](SelectedActions.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsSetGithubActionsPermissionsOrganization"></a>
# **actionsSetGithubActionsPermissionsOrganization**
> actionsSetGithubActionsPermissionsOrganization(org, actionsSetGithubActionsPermissionsOrganizationRequest)

Set GitHub Actions permissions for an organization

Sets the GitHub Actions permissions policy for repositories and allowed actions in an organization.  If the organization belongs to an enterprise that has set restrictive permissions at the enterprise level, such as &#x60;allowed_actions&#x60; to &#x60;selected&#x60; actions, then you cannot override them for the organization.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;administration&#x60; organization permission to use this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    ActionsSetGithubActionsPermissionsOrganizationRequest actionsSetGithubActionsPermissionsOrganizationRequest = new ActionsSetGithubActionsPermissionsOrganizationRequest(); // ActionsSetGithubActionsPermissionsOrganizationRequest | 
    try {
      apiInstance.actionsSetGithubActionsPermissionsOrganization(org, actionsSetGithubActionsPermissionsOrganizationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsSetGithubActionsPermissionsOrganization");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **actionsSetGithubActionsPermissionsOrganizationRequest** | [**ActionsSetGithubActionsPermissionsOrganizationRequest**](ActionsSetGithubActionsPermissionsOrganizationRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsSetGithubActionsPermissionsRepository"></a>
# **actionsSetGithubActionsPermissionsRepository**
> actionsSetGithubActionsPermissionsRepository(owner, repo, actionsSetGithubActionsPermissionsRepositoryRequest)

Set GitHub Actions permissions for a repository

Sets the GitHub Actions permissions policy for enabling GitHub Actions and allowed actions in the repository.  If the repository belongs to an organization or enterprise that has set restrictive permissions at the organization or enterprise levels, such as &#x60;allowed_actions&#x60; to &#x60;selected&#x60; actions, then you cannot override them for the repository.  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;administration&#x60; repository permission to use this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    ActionsSetGithubActionsPermissionsRepositoryRequest actionsSetGithubActionsPermissionsRepositoryRequest = new ActionsSetGithubActionsPermissionsRepositoryRequest(); // ActionsSetGithubActionsPermissionsRepositoryRequest | 
    try {
      apiInstance.actionsSetGithubActionsPermissionsRepository(owner, repo, actionsSetGithubActionsPermissionsRepositoryRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsSetGithubActionsPermissionsRepository");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **actionsSetGithubActionsPermissionsRepositoryRequest** | [**ActionsSetGithubActionsPermissionsRepositoryRequest**](ActionsSetGithubActionsPermissionsRepositoryRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsSetRepoAccessToSelfHostedRunnerGroupInOrg"></a>
# **actionsSetRepoAccessToSelfHostedRunnerGroupInOrg**
> actionsSetRepoAccessToSelfHostedRunnerGroupInOrg(org, runnerGroupId, actionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest)

Set repository access for a self-hosted runner group in an organization

Replaces the list of repositories that have access to a self-hosted runner group configured in an organization. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest actionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest = new ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest(); // ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest | 
    try {
      apiInstance.actionsSetRepoAccessToSelfHostedRunnerGroupInOrg(org, runnerGroupId, actionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsSetRepoAccessToSelfHostedRunnerGroupInOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **actionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest** | [**ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest**](ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsSetSelectedReposForOrgSecret"></a>
# **actionsSetSelectedReposForOrgSecret**
> actionsSetSelectedReposForOrgSecret(org, secretName, actionsSetSelectedReposForOrgSecretRequest)

Set selected repositories for an organization secret

Replaces all repositories for an organization secret when the &#x60;visibility&#x60; for repository access is set to &#x60;selected&#x60;. The visibility is set when you [Create or update an organization secret](https://docs.github.com/enterprise-server@3.2/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    String secretName = "secretName_example"; // String | The name of the secret.
    ActionsSetSelectedReposForOrgSecretRequest actionsSetSelectedReposForOrgSecretRequest = new ActionsSetSelectedReposForOrgSecretRequest(); // ActionsSetSelectedReposForOrgSecretRequest | 
    try {
      apiInstance.actionsSetSelectedReposForOrgSecret(org, secretName, actionsSetSelectedReposForOrgSecretRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsSetSelectedReposForOrgSecret");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **secretName** | **String**| The name of the secret. | |
| **actionsSetSelectedReposForOrgSecretRequest** | [**ActionsSetSelectedReposForOrgSecretRequest**](ActionsSetSelectedReposForOrgSecretRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsSetSelectedRepositoriesEnabledGithubActionsOrganization"></a>
# **actionsSetSelectedRepositoriesEnabledGithubActionsOrganization**
> actionsSetSelectedRepositoriesEnabledGithubActionsOrganization(org, actionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest)

Set selected repositories enabled for GitHub Actions in an organization

Replaces the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for &#x60;enabled_repositories&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).\&quot;  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;administration&#x60; organization permission to use this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest actionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest = new ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest(); // ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest | 
    try {
      apiInstance.actionsSetSelectedRepositoriesEnabledGithubActionsOrganization(org, actionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsSetSelectedRepositoriesEnabledGithubActionsOrganization");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **actionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest** | [**ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest**](ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsSetSelfHostedRunnersInGroupForOrg"></a>
# **actionsSetSelfHostedRunnersInGroupForOrg**
> actionsSetSelfHostedRunnersInGroupForOrg(org, runnerGroupId, enterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest)

Set self-hosted runners in a group for an organization

Replaces the list of self-hosted runners that are part of an organization runner group. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest enterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest = new EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest(); // EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest | 
    try {
      apiInstance.actionsSetSelfHostedRunnersInGroupForOrg(org, runnerGroupId, enterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsSetSelfHostedRunnersInGroupForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **enterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest** | [**EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest**](EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="actionsUpdateSelfHostedRunnerGroupForOrg"></a>
# **actionsUpdateSelfHostedRunnerGroupForOrg**
> RunnerGroupsOrg actionsUpdateSelfHostedRunnerGroupForOrg(org, runnerGroupId, actionsUpdateSelfHostedRunnerGroupForOrgRequest)

Update a self-hosted runner group for an organization

Updates the &#x60;name&#x60; and &#x60;visibility&#x60; of a self-hosted runner group in an organization. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    ActionsUpdateSelfHostedRunnerGroupForOrgRequest actionsUpdateSelfHostedRunnerGroupForOrgRequest = new ActionsUpdateSelfHostedRunnerGroupForOrgRequest(); // ActionsUpdateSelfHostedRunnerGroupForOrgRequest | 
    try {
      RunnerGroupsOrg result = apiInstance.actionsUpdateSelfHostedRunnerGroupForOrg(org, runnerGroupId, actionsUpdateSelfHostedRunnerGroupForOrgRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsUpdateSelfHostedRunnerGroupForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **actionsUpdateSelfHostedRunnerGroupForOrgRequest** | [**ActionsUpdateSelfHostedRunnerGroupForOrgRequest**](ActionsUpdateSelfHostedRunnerGroupForOrgRequest.md)|  | |

### Return type

[**RunnerGroupsOrg**](RunnerGroupsOrg.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

