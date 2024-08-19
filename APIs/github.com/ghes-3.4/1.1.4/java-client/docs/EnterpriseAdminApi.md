# EnterpriseAdminApi

All URIs are relative to *https://github.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**enterpriseAdminAddAuthorizedSshKey**](EnterpriseAdminApi.md#enterpriseAdminAddAuthorizedSshKey) | **POST** /setup/api/settings/authorized-keys | Add an authorized SSH key |
| [**enterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterprise) | **POST** /enterprises/{enterprise}/actions/runners/{runner_id}/labels | Add custom labels to a self-hosted runner for an enterprise |
| [**enterpriseAdminAddOrgAccessToSelfHostedRunnerGroupInEnterprise**](EnterpriseAdminApi.md#enterpriseAdminAddOrgAccessToSelfHostedRunnerGroupInEnterprise) | **PUT** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id} | Add organization access to a self-hosted runner group in an enterprise |
| [**enterpriseAdminAddSelfHostedRunnerToGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminAddSelfHostedRunnerToGroupForEnterprise) | **PUT** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | Add a self-hosted runner to a group for an enterprise |
| [**enterpriseAdminCreateEnterpriseServerLicense**](EnterpriseAdminApi.md#enterpriseAdminCreateEnterpriseServerLicense) | **POST** /setup/api/start | Create a GitHub license |
| [**enterpriseAdminCreateGlobalWebhook**](EnterpriseAdminApi.md#enterpriseAdminCreateGlobalWebhook) | **POST** /admin/hooks | Create a global webhook |
| [**enterpriseAdminCreateImpersonationOAuthToken**](EnterpriseAdminApi.md#enterpriseAdminCreateImpersonationOAuthToken) | **POST** /admin/users/{username}/authorizations | Create an impersonation OAuth token |
| [**enterpriseAdminCreateOrg**](EnterpriseAdminApi.md#enterpriseAdminCreateOrg) | **POST** /admin/organizations | Create an organization |
| [**enterpriseAdminCreatePreReceiveEnvironment**](EnterpriseAdminApi.md#enterpriseAdminCreatePreReceiveEnvironment) | **POST** /admin/pre-receive-environments | Create a pre-receive environment |
| [**enterpriseAdminCreatePreReceiveHook**](EnterpriseAdminApi.md#enterpriseAdminCreatePreReceiveHook) | **POST** /admin/pre-receive-hooks | Create a pre-receive hook |
| [**enterpriseAdminCreateRegistrationTokenForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminCreateRegistrationTokenForEnterprise) | **POST** /enterprises/{enterprise}/actions/runners/registration-token | Create a registration token for an enterprise |
| [**enterpriseAdminCreateRemoveTokenForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminCreateRemoveTokenForEnterprise) | **POST** /enterprises/{enterprise}/actions/runners/remove-token | Create a remove token for an enterprise |
| [**enterpriseAdminCreateSelfHostedRunnerGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminCreateSelfHostedRunnerGroupForEnterprise) | **POST** /enterprises/{enterprise}/actions/runner-groups | Create a self-hosted runner group for an enterprise |
| [**enterpriseAdminCreateUser**](EnterpriseAdminApi.md#enterpriseAdminCreateUser) | **POST** /admin/users | Create a user |
| [**enterpriseAdminDeleteGlobalWebhook**](EnterpriseAdminApi.md#enterpriseAdminDeleteGlobalWebhook) | **DELETE** /admin/hooks/{hook_id} | Delete a global webhook |
| [**enterpriseAdminDeleteImpersonationOAuthToken**](EnterpriseAdminApi.md#enterpriseAdminDeleteImpersonationOAuthToken) | **DELETE** /admin/users/{username}/authorizations | Delete an impersonation OAuth token |
| [**enterpriseAdminDeletePersonalAccessToken**](EnterpriseAdminApi.md#enterpriseAdminDeletePersonalAccessToken) | **DELETE** /admin/tokens/{token_id} | Delete a personal access token |
| [**enterpriseAdminDeletePreReceiveEnvironment**](EnterpriseAdminApi.md#enterpriseAdminDeletePreReceiveEnvironment) | **DELETE** /admin/pre-receive-environments/{pre_receive_environment_id} | Delete a pre-receive environment |
| [**enterpriseAdminDeletePreReceiveHook**](EnterpriseAdminApi.md#enterpriseAdminDeletePreReceiveHook) | **DELETE** /admin/pre-receive-hooks/{pre_receive_hook_id} | Delete a pre-receive hook |
| [**enterpriseAdminDeletePublicKey**](EnterpriseAdminApi.md#enterpriseAdminDeletePublicKey) | **DELETE** /admin/keys/{key_ids} | Delete a public key |
| [**enterpriseAdminDeleteSelfHostedRunnerFromEnterprise**](EnterpriseAdminApi.md#enterpriseAdminDeleteSelfHostedRunnerFromEnterprise) | **DELETE** /enterprises/{enterprise}/actions/runners/{runner_id} | Delete a self-hosted runner from an enterprise |
| [**enterpriseAdminDeleteSelfHostedRunnerGroupFromEnterprise**](EnterpriseAdminApi.md#enterpriseAdminDeleteSelfHostedRunnerGroupFromEnterprise) | **DELETE** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id} | Delete a self-hosted runner group from an enterprise |
| [**enterpriseAdminDeleteUser**](EnterpriseAdminApi.md#enterpriseAdminDeleteUser) | **DELETE** /admin/users/{username} | Delete a user |
| [**enterpriseAdminDemoteSiteAdministrator**](EnterpriseAdminApi.md#enterpriseAdminDemoteSiteAdministrator) | **DELETE** /users/{username}/site_admin | Demote a site administrator |
| [**enterpriseAdminDisableSelectedOrganizationGithubActionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminDisableSelectedOrganizationGithubActionsEnterprise) | **DELETE** /enterprises/{enterprise}/actions/permissions/organizations/{org_id} | Disable a selected organization for GitHub Actions in an enterprise |
| [**enterpriseAdminEnableOrDisableMaintenanceMode**](EnterpriseAdminApi.md#enterpriseAdminEnableOrDisableMaintenanceMode) | **POST** /setup/api/maintenance | Enable or disable maintenance mode |
| [**enterpriseAdminEnableSelectedOrganizationGithubActionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminEnableSelectedOrganizationGithubActionsEnterprise) | **PUT** /enterprises/{enterprise}/actions/permissions/organizations/{org_id} | Enable a selected organization for GitHub Actions in an enterprise |
| [**enterpriseAdminGetAllAuthorizedSshKeys**](EnterpriseAdminApi.md#enterpriseAdminGetAllAuthorizedSshKeys) | **GET** /setup/api/settings/authorized-keys | Get all authorized SSH keys |
| [**enterpriseAdminGetAllStats**](EnterpriseAdminApi.md#enterpriseAdminGetAllStats) | **GET** /enterprise/stats/all | Get all statistics |
| [**enterpriseAdminGetAllowedActionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminGetAllowedActionsEnterprise) | **GET** /enterprises/{enterprise}/actions/permissions/selected-actions | Get allowed actions for an enterprise |
| [**enterpriseAdminGetAnnouncement**](EnterpriseAdminApi.md#enterpriseAdminGetAnnouncement) | **GET** /enterprise/announcement | Get the global announcement banner |
| [**enterpriseAdminGetAuditLog**](EnterpriseAdminApi.md#enterpriseAdminGetAuditLog) | **GET** /enterprises/{enterprise}/audit-log | Get the audit log for an enterprise |
| [**enterpriseAdminGetCommentStats**](EnterpriseAdminApi.md#enterpriseAdminGetCommentStats) | **GET** /enterprise/stats/comments | Get comment statistics |
| [**enterpriseAdminGetConfigurationStatus**](EnterpriseAdminApi.md#enterpriseAdminGetConfigurationStatus) | **GET** /setup/api/configcheck | Get the configuration status |
| [**enterpriseAdminGetDownloadStatusForPreReceiveEnvironment**](EnterpriseAdminApi.md#enterpriseAdminGetDownloadStatusForPreReceiveEnvironment) | **GET** /admin/pre-receive-environments/{pre_receive_environment_id}/downloads/latest | Get the download status for a pre-receive environment |
| [**enterpriseAdminGetGistStats**](EnterpriseAdminApi.md#enterpriseAdminGetGistStats) | **GET** /enterprise/stats/gists | Get gist statistics |
| [**enterpriseAdminGetGithubActionsPermissionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminGetGithubActionsPermissionsEnterprise) | **GET** /enterprises/{enterprise}/actions/permissions | Get GitHub Actions permissions for an enterprise |
| [**enterpriseAdminGetGlobalWebhook**](EnterpriseAdminApi.md#enterpriseAdminGetGlobalWebhook) | **GET** /admin/hooks/{hook_id} | Get a global webhook |
| [**enterpriseAdminGetHooksStats**](EnterpriseAdminApi.md#enterpriseAdminGetHooksStats) | **GET** /enterprise/stats/hooks | Get hooks statistics |
| [**enterpriseAdminGetIssueStats**](EnterpriseAdminApi.md#enterpriseAdminGetIssueStats) | **GET** /enterprise/stats/issues | Get issue statistics |
| [**enterpriseAdminGetLicenseInformation**](EnterpriseAdminApi.md#enterpriseAdminGetLicenseInformation) | **GET** /enterprise/settings/license | Get license information |
| [**enterpriseAdminGetMaintenanceStatus**](EnterpriseAdminApi.md#enterpriseAdminGetMaintenanceStatus) | **GET** /setup/api/maintenance | Get the maintenance status |
| [**enterpriseAdminGetMilestoneStats**](EnterpriseAdminApi.md#enterpriseAdminGetMilestoneStats) | **GET** /enterprise/stats/milestones | Get milestone statistics |
| [**enterpriseAdminGetOrgStats**](EnterpriseAdminApi.md#enterpriseAdminGetOrgStats) | **GET** /enterprise/stats/orgs | Get organization statistics |
| [**enterpriseAdminGetPagesStats**](EnterpriseAdminApi.md#enterpriseAdminGetPagesStats) | **GET** /enterprise/stats/pages | Get pages statistics |
| [**enterpriseAdminGetPreReceiveEnvironment**](EnterpriseAdminApi.md#enterpriseAdminGetPreReceiveEnvironment) | **GET** /admin/pre-receive-environments/{pre_receive_environment_id} | Get a pre-receive environment |
| [**enterpriseAdminGetPreReceiveHook**](EnterpriseAdminApi.md#enterpriseAdminGetPreReceiveHook) | **GET** /admin/pre-receive-hooks/{pre_receive_hook_id} | Get a pre-receive hook |
| [**enterpriseAdminGetPreReceiveHookForOrg**](EnterpriseAdminApi.md#enterpriseAdminGetPreReceiveHookForOrg) | **GET** /orgs/{org}/pre-receive-hooks/{pre_receive_hook_id} | Get a pre-receive hook for an organization |
| [**enterpriseAdminGetPreReceiveHookForRepo**](EnterpriseAdminApi.md#enterpriseAdminGetPreReceiveHookForRepo) | **GET** /repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id} | Get a pre-receive hook for a repository |
| [**enterpriseAdminGetPullRequestStats**](EnterpriseAdminApi.md#enterpriseAdminGetPullRequestStats) | **GET** /enterprise/stats/pulls | Get pull request statistics |
| [**enterpriseAdminGetRepoStats**](EnterpriseAdminApi.md#enterpriseAdminGetRepoStats) | **GET** /enterprise/stats/repos | Get repository statistics |
| [**enterpriseAdminGetSelfHostedRunnerForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminGetSelfHostedRunnerForEnterprise) | **GET** /enterprises/{enterprise}/actions/runners/{runner_id} | Get a self-hosted runner for an enterprise |
| [**enterpriseAdminGetSelfHostedRunnerGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminGetSelfHostedRunnerGroupForEnterprise) | **GET** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id} | Get a self-hosted runner group for an enterprise |
| [**enterpriseAdminGetSettings**](EnterpriseAdminApi.md#enterpriseAdminGetSettings) | **GET** /setup/api/settings | Get settings |
| [**enterpriseAdminGetUserStats**](EnterpriseAdminApi.md#enterpriseAdminGetUserStats) | **GET** /enterprise/stats/users | Get users statistics |
| [**enterpriseAdminListGlobalWebhooks**](EnterpriseAdminApi.md#enterpriseAdminListGlobalWebhooks) | **GET** /admin/hooks | List global webhooks |
| [**enterpriseAdminListLabelsForSelfHostedRunnerForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminListLabelsForSelfHostedRunnerForEnterprise) | **GET** /enterprises/{enterprise}/actions/runners/{runner_id}/labels | List labels for a self-hosted runner for an enterprise |
| [**enterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise**](EnterpriseAdminApi.md#enterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise) | **GET** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations | List organization access to a self-hosted runner group in an enterprise |
| [**enterpriseAdminListPersonalAccessTokens**](EnterpriseAdminApi.md#enterpriseAdminListPersonalAccessTokens) | **GET** /admin/tokens | List personal access tokens |
| [**enterpriseAdminListPreReceiveEnvironments**](EnterpriseAdminApi.md#enterpriseAdminListPreReceiveEnvironments) | **GET** /admin/pre-receive-environments | List pre-receive environments |
| [**enterpriseAdminListPreReceiveHooks**](EnterpriseAdminApi.md#enterpriseAdminListPreReceiveHooks) | **GET** /admin/pre-receive-hooks | List pre-receive hooks |
| [**enterpriseAdminListPreReceiveHooksForOrg**](EnterpriseAdminApi.md#enterpriseAdminListPreReceiveHooksForOrg) | **GET** /orgs/{org}/pre-receive-hooks | List pre-receive hooks for an organization |
| [**enterpriseAdminListPreReceiveHooksForRepo**](EnterpriseAdminApi.md#enterpriseAdminListPreReceiveHooksForRepo) | **GET** /repos/{owner}/{repo}/pre-receive-hooks | List pre-receive hooks for a repository |
| [**enterpriseAdminListPublicKeys**](EnterpriseAdminApi.md#enterpriseAdminListPublicKeys) | **GET** /admin/keys | List public keys |
| [**enterpriseAdminListRunnerApplicationsForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminListRunnerApplicationsForEnterprise) | **GET** /enterprises/{enterprise}/actions/runners/downloads | List runner applications for an enterprise |
| [**enterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise) | **GET** /enterprises/{enterprise}/actions/permissions/organizations | List selected organizations enabled for GitHub Actions in an enterprise |
| [**enterpriseAdminListSelfHostedRunnerGroupsForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminListSelfHostedRunnerGroupsForEnterprise) | **GET** /enterprises/{enterprise}/actions/runner-groups | List self-hosted runner groups for an enterprise |
| [**enterpriseAdminListSelfHostedRunnersForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminListSelfHostedRunnersForEnterprise) | **GET** /enterprises/{enterprise}/actions/runners | List self-hosted runners for an enterprise |
| [**enterpriseAdminListSelfHostedRunnersInGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminListSelfHostedRunnersInGroupForEnterprise) | **GET** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners | List self-hosted runners in a group for an enterprise |
| [**enterpriseAdminPingGlobalWebhook**](EnterpriseAdminApi.md#enterpriseAdminPingGlobalWebhook) | **POST** /admin/hooks/{hook_id}/pings | Ping a global webhook |
| [**enterpriseAdminPromoteUserToBeSiteAdministrator**](EnterpriseAdminApi.md#enterpriseAdminPromoteUserToBeSiteAdministrator) | **PUT** /users/{username}/site_admin | Promote a user to be a site administrator |
| [**enterpriseAdminRemoveAllCustomLabelsFromSelfHostedRunnerForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminRemoveAllCustomLabelsFromSelfHostedRunnerForEnterprise) | **DELETE** /enterprises/{enterprise}/actions/runners/{runner_id}/labels | Remove all custom labels from a self-hosted runner for an enterprise |
| [**enterpriseAdminRemoveAnnouncement**](EnterpriseAdminApi.md#enterpriseAdminRemoveAnnouncement) | **DELETE** /enterprise/announcement | Remove the global announcement banner |
| [**enterpriseAdminRemoveAuthorizedSshKey**](EnterpriseAdminApi.md#enterpriseAdminRemoveAuthorizedSshKey) | **DELETE** /setup/api/settings/authorized-keys | Remove an authorized SSH key |
| [**enterpriseAdminRemoveCustomLabelFromSelfHostedRunnerForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminRemoveCustomLabelFromSelfHostedRunnerForEnterprise) | **DELETE** /enterprises/{enterprise}/actions/runners/{runner_id}/labels/{name} | Remove a custom label from a self-hosted runner for an enterprise |
| [**enterpriseAdminRemoveOrgAccessToSelfHostedRunnerGroupInEnterprise**](EnterpriseAdminApi.md#enterpriseAdminRemoveOrgAccessToSelfHostedRunnerGroupInEnterprise) | **DELETE** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id} | Remove organization access to a self-hosted runner group in an enterprise |
| [**enterpriseAdminRemovePreReceiveHookEnforcementForOrg**](EnterpriseAdminApi.md#enterpriseAdminRemovePreReceiveHookEnforcementForOrg) | **DELETE** /orgs/{org}/pre-receive-hooks/{pre_receive_hook_id} | Remove pre-receive hook enforcement for an organization |
| [**enterpriseAdminRemovePreReceiveHookEnforcementForRepo**](EnterpriseAdminApi.md#enterpriseAdminRemovePreReceiveHookEnforcementForRepo) | **DELETE** /repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id} | Remove pre-receive hook enforcement for a repository |
| [**enterpriseAdminRemoveSelfHostedRunnerFromGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminRemoveSelfHostedRunnerFromGroupForEnterprise) | **DELETE** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | Remove a self-hosted runner from a group for an enterprise |
| [**enterpriseAdminSetAllowedActionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminSetAllowedActionsEnterprise) | **PUT** /enterprises/{enterprise}/actions/permissions/selected-actions | Set allowed actions for an enterprise |
| [**enterpriseAdminSetAnnouncement**](EnterpriseAdminApi.md#enterpriseAdminSetAnnouncement) | **PATCH** /enterprise/announcement | Set the global announcement banner |
| [**enterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterprise) | **PUT** /enterprises/{enterprise}/actions/runners/{runner_id}/labels | Set custom labels for a self-hosted runner for an enterprise |
| [**enterpriseAdminSetGithubActionsPermissionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminSetGithubActionsPermissionsEnterprise) | **PUT** /enterprises/{enterprise}/actions/permissions | Set GitHub Actions permissions for an enterprise |
| [**enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterprise**](EnterpriseAdminApi.md#enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterprise) | **PUT** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations | Set organization access for a self-hosted runner group in an enterprise |
| [**enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterprise) | **PUT** /enterprises/{enterprise}/actions/permissions/organizations | Set selected organizations enabled for GitHub Actions in an enterprise |
| [**enterpriseAdminSetSelfHostedRunnersInGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminSetSelfHostedRunnersInGroupForEnterprise) | **PUT** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners | Set self-hosted runners in a group for an enterprise |
| [**enterpriseAdminSetSettings**](EnterpriseAdminApi.md#enterpriseAdminSetSettings) | **PUT** /setup/api/settings | Set settings |
| [**enterpriseAdminStartConfigurationProcess**](EnterpriseAdminApi.md#enterpriseAdminStartConfigurationProcess) | **POST** /setup/api/configure | Start a configuration process |
| [**enterpriseAdminStartPreReceiveEnvironmentDownload**](EnterpriseAdminApi.md#enterpriseAdminStartPreReceiveEnvironmentDownload) | **POST** /admin/pre-receive-environments/{pre_receive_environment_id}/downloads | Start a pre-receive environment download |
| [**enterpriseAdminSuspendUser**](EnterpriseAdminApi.md#enterpriseAdminSuspendUser) | **PUT** /users/{username}/suspended | Suspend a user |
| [**enterpriseAdminSyncLdapMappingForTeam**](EnterpriseAdminApi.md#enterpriseAdminSyncLdapMappingForTeam) | **POST** /admin/ldap/teams/{team_id}/sync | Sync LDAP mapping for a team |
| [**enterpriseAdminSyncLdapMappingForUser**](EnterpriseAdminApi.md#enterpriseAdminSyncLdapMappingForUser) | **POST** /admin/ldap/users/{username}/sync | Sync LDAP mapping for a user |
| [**enterpriseAdminUnsuspendUser**](EnterpriseAdminApi.md#enterpriseAdminUnsuspendUser) | **DELETE** /users/{username}/suspended | Unsuspend a user |
| [**enterpriseAdminUpdateGlobalWebhook**](EnterpriseAdminApi.md#enterpriseAdminUpdateGlobalWebhook) | **PATCH** /admin/hooks/{hook_id} | Update a global webhook |
| [**enterpriseAdminUpdateLdapMappingForTeam**](EnterpriseAdminApi.md#enterpriseAdminUpdateLdapMappingForTeam) | **PATCH** /admin/ldap/teams/{team_id}/mapping | Update LDAP mapping for a team |
| [**enterpriseAdminUpdateLdapMappingForUser**](EnterpriseAdminApi.md#enterpriseAdminUpdateLdapMappingForUser) | **PATCH** /admin/ldap/users/{username}/mapping | Update LDAP mapping for a user |
| [**enterpriseAdminUpdateOrgName**](EnterpriseAdminApi.md#enterpriseAdminUpdateOrgName) | **PATCH** /admin/organizations/{org} | Update an organization name |
| [**enterpriseAdminUpdatePreReceiveEnvironment**](EnterpriseAdminApi.md#enterpriseAdminUpdatePreReceiveEnvironment) | **PATCH** /admin/pre-receive-environments/{pre_receive_environment_id} | Update a pre-receive environment |
| [**enterpriseAdminUpdatePreReceiveHook**](EnterpriseAdminApi.md#enterpriseAdminUpdatePreReceiveHook) | **PATCH** /admin/pre-receive-hooks/{pre_receive_hook_id} | Update a pre-receive hook |
| [**enterpriseAdminUpdatePreReceiveHookEnforcementForOrg**](EnterpriseAdminApi.md#enterpriseAdminUpdatePreReceiveHookEnforcementForOrg) | **PATCH** /orgs/{org}/pre-receive-hooks/{pre_receive_hook_id} | Update pre-receive hook enforcement for an organization |
| [**enterpriseAdminUpdatePreReceiveHookEnforcementForRepo**](EnterpriseAdminApi.md#enterpriseAdminUpdatePreReceiveHookEnforcementForRepo) | **PATCH** /repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id} | Update pre-receive hook enforcement for a repository |
| [**enterpriseAdminUpdateSelfHostedRunnerGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminUpdateSelfHostedRunnerGroupForEnterprise) | **PATCH** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id} | Update a self-hosted runner group for an enterprise |
| [**enterpriseAdminUpdateUsernameForUser**](EnterpriseAdminApi.md#enterpriseAdminUpdateUsernameForUser) | **PATCH** /admin/users/{username} | Update the username for a user |
| [**enterpriseAdminUpgradeLicense**](EnterpriseAdminApi.md#enterpriseAdminUpgradeLicense) | **POST** /setup/api/upgrade | Upgrade a license |


<a id="enterpriseAdminAddAuthorizedSshKey"></a>
# **enterpriseAdminAddAuthorizedSshKey**
> List&lt;SshKey&gt; enterpriseAdminAddAuthorizedSshKey(authorizedKey)

Add an authorized SSH key

**Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String authorizedKey = "authorizedKey_example"; // String | The public SSH key.
    try {
      List<SshKey> result = apiInstance.enterpriseAdminAddAuthorizedSshKey(authorizedKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminAddAuthorizedSshKey");
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
| **authorizedKey** | **String**| The public SSH key. | |

### Return type

[**List&lt;SshKey&gt;**](SshKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="enterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterprise"></a>
# **enterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterprise**
> EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response enterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterprise(enterprise, runnerId, enterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterpriseRequest)

Add custom labels to a self-hosted runner for an enterprise

Add custom labels to a self-hosted runner configured in an enterprise.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    EnterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterpriseRequest enterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterpriseRequest = new EnterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterpriseRequest(); // EnterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterpriseRequest | 
    try {
      EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response result = apiInstance.enterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterprise(enterprise, runnerId, enterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterpriseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **runnerId** | **Integer**| Unique identifier of the self-hosted runner. | |
| **enterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterpriseRequest** | [**EnterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterpriseRequest**](EnterpriseAdminAddCustomLabelsToSelfHostedRunnerForEnterpriseRequest.md)|  | |

### Return type

[**EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response**](EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="enterpriseAdminAddOrgAccessToSelfHostedRunnerGroupInEnterprise"></a>
# **enterpriseAdminAddOrgAccessToSelfHostedRunnerGroupInEnterprise**
> enterpriseAdminAddOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, orgId)

Add organization access to a self-hosted runner group in an enterprise

Adds an organization to the list of selected organizations that can access a self-hosted runner group. The runner group must have &#x60;visibility&#x60; set to &#x60;selected&#x60;. For more information, see \&quot;[Create a self-hosted runner group for an enterprise](#create-a-self-hosted-runner-group-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    Integer orgId = 56; // Integer | The unique identifier of the organization.
    try {
      apiInstance.enterpriseAdminAddOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, orgId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminAddOrgAccessToSelfHostedRunnerGroupInEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **orgId** | **Integer**| The unique identifier of the organization. | |

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

<a id="enterpriseAdminAddSelfHostedRunnerToGroupForEnterprise"></a>
# **enterpriseAdminAddSelfHostedRunnerToGroupForEnterprise**
> enterpriseAdminAddSelfHostedRunnerToGroupForEnterprise(enterprise, runnerGroupId, runnerId)

Add a self-hosted runner to a group for an enterprise

Adds a self-hosted runner to a runner group configured in an enterprise.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    try {
      apiInstance.enterpriseAdminAddSelfHostedRunnerToGroupForEnterprise(enterprise, runnerGroupId, runnerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminAddSelfHostedRunnerToGroupForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
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

<a id="enterpriseAdminCreateEnterpriseServerLicense"></a>
# **enterpriseAdminCreateEnterpriseServerLicense**
> enterpriseAdminCreateEnterpriseServerLicense(license, password, settings)

Create a GitHub license

When you boot a GitHub instance for the first time, you can use the following endpoint to upload a license.  Note that you need to &#x60;POST&#x60; to [&#x60;/setup/api/configure&#x60;](https://docs.github.com/enterprise-server@3.4/rest/reference/enterprise-admin#start-a-configuration-process) to start the actual configuration process.  When using this endpoint, your GitHub instance must have a password set. This can be accomplished two ways:  1.  If you&#39;re working directly with the API before accessing the web interface, you must pass in the password parameter to set your password. 2.  If you set up your instance via the web interface before accessing the API, your calls to this endpoint do not need the password parameter.  **Note:** The request body for this operation must be submitted as &#x60;multipart/form-data&#x60; data. You can can reference the license file by prefixing the filename with the &#x60;@&#x60; symbol using &#x60;curl&#x60;. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#-F).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String license = "license_example"; // String | The content of your _.ghl_ license file.
    String password = "password_example"; // String | You **must** provide a password _only if_ you are uploading your license for the first time. If you previously set a password through the web interface, you don't need this parameter.
    String settings = "settings_example"; // String | An optional JSON string containing the installation settings. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@3.4/rest/reference/enterprise-admin#get-settings).
    try {
      apiInstance.enterpriseAdminCreateEnterpriseServerLicense(license, password, settings);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminCreateEnterpriseServerLicense");
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
| **license** | **String**| The content of your _.ghl_ license file. | |
| **password** | **String**| You **must** provide a password _only if_ you are uploading your license for the first time. If you previously set a password through the web interface, you don&#39;t need this parameter. | [optional] |
| **settings** | **String**| An optional JSON string containing the installation settings. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@3.4/rest/reference/enterprise-admin#get-settings). | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Response |  -  |

<a id="enterpriseAdminCreateGlobalWebhook"></a>
# **enterpriseAdminCreateGlobalWebhook**
> GlobalHook enterpriseAdminCreateGlobalWebhook(enterpriseAdminCreateGlobalWebhookRequest)

Create a global webhook



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    EnterpriseAdminCreateGlobalWebhookRequest enterpriseAdminCreateGlobalWebhookRequest = new EnterpriseAdminCreateGlobalWebhookRequest(); // EnterpriseAdminCreateGlobalWebhookRequest | 
    try {
      GlobalHook result = apiInstance.enterpriseAdminCreateGlobalWebhook(enterpriseAdminCreateGlobalWebhookRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminCreateGlobalWebhook");
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
| **enterpriseAdminCreateGlobalWebhookRequest** | [**EnterpriseAdminCreateGlobalWebhookRequest**](EnterpriseAdminCreateGlobalWebhookRequest.md)|  | |

### Return type

[**GlobalHook**](GlobalHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="enterpriseAdminCreateImpersonationOAuthToken"></a>
# **enterpriseAdminCreateImpersonationOAuthToken**
> Authorization enterpriseAdminCreateImpersonationOAuthToken(username, enterpriseAdminCreateImpersonationOAuthTokenRequest)

Create an impersonation OAuth token



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String username = "username_example"; // String | The handle for the GitHub user account.
    EnterpriseAdminCreateImpersonationOAuthTokenRequest enterpriseAdminCreateImpersonationOAuthTokenRequest = new EnterpriseAdminCreateImpersonationOAuthTokenRequest(); // EnterpriseAdminCreateImpersonationOAuthTokenRequest | 
    try {
      Authorization result = apiInstance.enterpriseAdminCreateImpersonationOAuthToken(username, enterpriseAdminCreateImpersonationOAuthTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminCreateImpersonationOAuthToken");
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
| **username** | **String**| The handle for the GitHub user account. | |
| **enterpriseAdminCreateImpersonationOAuthTokenRequest** | [**EnterpriseAdminCreateImpersonationOAuthTokenRequest**](EnterpriseAdminCreateImpersonationOAuthTokenRequest.md)|  | |

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response when getting an existing impersonation OAuth token |  -  |
| **201** | Response when creating a new impersonation OAuth token |  -  |

<a id="enterpriseAdminCreateOrg"></a>
# **enterpriseAdminCreateOrg**
> OrganizationSimple enterpriseAdminCreateOrg(enterpriseAdminCreateOrgRequest)

Create an organization



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    EnterpriseAdminCreateOrgRequest enterpriseAdminCreateOrgRequest = new EnterpriseAdminCreateOrgRequest(); // EnterpriseAdminCreateOrgRequest | 
    try {
      OrganizationSimple result = apiInstance.enterpriseAdminCreateOrg(enterpriseAdminCreateOrgRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminCreateOrg");
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
| **enterpriseAdminCreateOrgRequest** | [**EnterpriseAdminCreateOrgRequest**](EnterpriseAdminCreateOrgRequest.md)|  | |

### Return type

[**OrganizationSimple**](OrganizationSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="enterpriseAdminCreatePreReceiveEnvironment"></a>
# **enterpriseAdminCreatePreReceiveEnvironment**
> PreReceiveEnvironment enterpriseAdminCreatePreReceiveEnvironment(enterpriseAdminCreatePreReceiveEnvironmentRequest)

Create a pre-receive environment



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    EnterpriseAdminCreatePreReceiveEnvironmentRequest enterpriseAdminCreatePreReceiveEnvironmentRequest = new EnterpriseAdminCreatePreReceiveEnvironmentRequest(); // EnterpriseAdminCreatePreReceiveEnvironmentRequest | 
    try {
      PreReceiveEnvironment result = apiInstance.enterpriseAdminCreatePreReceiveEnvironment(enterpriseAdminCreatePreReceiveEnvironmentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminCreatePreReceiveEnvironment");
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
| **enterpriseAdminCreatePreReceiveEnvironmentRequest** | [**EnterpriseAdminCreatePreReceiveEnvironmentRequest**](EnterpriseAdminCreatePreReceiveEnvironmentRequest.md)|  | |

### Return type

[**PreReceiveEnvironment**](PreReceiveEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="enterpriseAdminCreatePreReceiveHook"></a>
# **enterpriseAdminCreatePreReceiveHook**
> PreReceiveHook enterpriseAdminCreatePreReceiveHook(enterpriseAdminCreatePreReceiveHookRequest)

Create a pre-receive hook



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    EnterpriseAdminCreatePreReceiveHookRequest enterpriseAdminCreatePreReceiveHookRequest = new EnterpriseAdminCreatePreReceiveHookRequest(); // EnterpriseAdminCreatePreReceiveHookRequest | 
    try {
      PreReceiveHook result = apiInstance.enterpriseAdminCreatePreReceiveHook(enterpriseAdminCreatePreReceiveHookRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminCreatePreReceiveHook");
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
| **enterpriseAdminCreatePreReceiveHookRequest** | [**EnterpriseAdminCreatePreReceiveHookRequest**](EnterpriseAdminCreatePreReceiveHookRequest.md)|  | |

### Return type

[**PreReceiveHook**](PreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="enterpriseAdminCreateRegistrationTokenForEnterprise"></a>
# **enterpriseAdminCreateRegistrationTokenForEnterprise**
> AuthenticationToken enterpriseAdminCreateRegistrationTokenForEnterprise(enterprise)

Create a registration token for an enterprise

Returns a token that you can pass to the &#x60;config&#x60; script. The token expires after one hour.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.  #### Example using registration token  Configure your self-hosted runner, replacing &#x60;TOKEN&#x60; with the registration token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh --url https://github.com/enterprises/octo-enterprise --token TOKEN &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    try {
      AuthenticationToken result = apiInstance.enterpriseAdminCreateRegistrationTokenForEnterprise(enterprise);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminCreateRegistrationTokenForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |

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

<a id="enterpriseAdminCreateRemoveTokenForEnterprise"></a>
# **enterpriseAdminCreateRemoveTokenForEnterprise**
> AuthenticationToken enterpriseAdminCreateRemoveTokenForEnterprise(enterprise)

Create a remove token for an enterprise

Returns a token that you can pass to the &#x60;config&#x60; script to remove a self-hosted runner from an enterprise. The token expires after one hour.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.  #### Example using remove token  To remove your self-hosted runner from an enterprise, replace &#x60;TOKEN&#x60; with the remove token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh remove --token TOKEN &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    try {
      AuthenticationToken result = apiInstance.enterpriseAdminCreateRemoveTokenForEnterprise(enterprise);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminCreateRemoveTokenForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |

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

<a id="enterpriseAdminCreateSelfHostedRunnerGroupForEnterprise"></a>
# **enterpriseAdminCreateSelfHostedRunnerGroupForEnterprise**
> RunnerGroupsEnterprise enterpriseAdminCreateSelfHostedRunnerGroupForEnterprise(enterprise, enterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest)

Create a self-hosted runner group for an enterprise

Creates a new self-hosted runner group for an enterprise.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    EnterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest enterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest = new EnterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest(); // EnterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest | 
    try {
      RunnerGroupsEnterprise result = apiInstance.enterpriseAdminCreateSelfHostedRunnerGroupForEnterprise(enterprise, enterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminCreateSelfHostedRunnerGroupForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **enterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest** | [**EnterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest**](EnterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest.md)|  | |

### Return type

[**RunnerGroupsEnterprise**](RunnerGroupsEnterprise.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="enterpriseAdminCreateUser"></a>
# **enterpriseAdminCreateUser**
> SimpleUser enterpriseAdminCreateUser(enterpriseAdminCreateUserRequest)

Create a user

If an external authentication mechanism is used, the login name should match the login name in the external system. If you are using LDAP authentication, you should also [update the LDAP mapping](https://docs.github.com/enterprise-server@3.4/rest/reference/enterprise-admin#update-ldap-mapping-for-a-user) for the user.  The login name will be normalized to only contain alphanumeric characters or single hyphens. For example, if you send &#x60;\&quot;octo_cat\&quot;&#x60; as the login, a user named &#x60;\&quot;octo-cat\&quot;&#x60; will be created.  If the login name or email address is already associated with an account, the server will return a &#x60;422&#x60; response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    EnterpriseAdminCreateUserRequest enterpriseAdminCreateUserRequest = new EnterpriseAdminCreateUserRequest(); // EnterpriseAdminCreateUserRequest | 
    try {
      SimpleUser result = apiInstance.enterpriseAdminCreateUser(enterpriseAdminCreateUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminCreateUser");
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
| **enterpriseAdminCreateUserRequest** | [**EnterpriseAdminCreateUserRequest**](EnterpriseAdminCreateUserRequest.md)|  | |

### Return type

[**SimpleUser**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="enterpriseAdminDeleteGlobalWebhook"></a>
# **enterpriseAdminDeleteGlobalWebhook**
> enterpriseAdminDeleteGlobalWebhook(hookId)

Delete a global webhook



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer hookId = 56; // Integer | The unique identifier of the hook.
    try {
      apiInstance.enterpriseAdminDeleteGlobalWebhook(hookId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminDeleteGlobalWebhook");
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
| **hookId** | **Integer**| The unique identifier of the hook. | |

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

<a id="enterpriseAdminDeleteImpersonationOAuthToken"></a>
# **enterpriseAdminDeleteImpersonationOAuthToken**
> enterpriseAdminDeleteImpersonationOAuthToken(username)

Delete an impersonation OAuth token



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String username = "username_example"; // String | The handle for the GitHub user account.
    try {
      apiInstance.enterpriseAdminDeleteImpersonationOAuthToken(username);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminDeleteImpersonationOAuthToken");
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
| **username** | **String**| The handle for the GitHub user account. | |

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

<a id="enterpriseAdminDeletePersonalAccessToken"></a>
# **enterpriseAdminDeletePersonalAccessToken**
> enterpriseAdminDeletePersonalAccessToken(tokenId)

Delete a personal access token

Deletes a personal access token. Returns a &#x60;403 - Forbidden&#x60; status when a personal access token is in use. For example, if you access this endpoint with the same personal access token that you are trying to delete, you will receive this error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer tokenId = 56; // Integer | The unique identifier of the token.
    try {
      apiInstance.enterpriseAdminDeletePersonalAccessToken(tokenId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminDeletePersonalAccessToken");
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
| **tokenId** | **Integer**| The unique identifier of the token. | |

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

<a id="enterpriseAdminDeletePreReceiveEnvironment"></a>
# **enterpriseAdminDeletePreReceiveEnvironment**
> enterpriseAdminDeletePreReceiveEnvironment(preReceiveEnvironmentId)

Delete a pre-receive environment

If you attempt to delete an environment that cannot be deleted, you will receive a &#x60;422 Unprocessable Entity&#x60; response.  The possible error messages are:  *   _Cannot modify or delete the default environment_ *   _Cannot delete environment that has hooks_ *   _Cannot delete environment when download is in progress_

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer preReceiveEnvironmentId = 56; // Integer | The unique identifier of the pre-receive environment.
    try {
      apiInstance.enterpriseAdminDeletePreReceiveEnvironment(preReceiveEnvironmentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminDeletePreReceiveEnvironment");
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
| **preReceiveEnvironmentId** | **Integer**| The unique identifier of the pre-receive environment. | |

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
| **422** | Client Errors |  -  |

<a id="enterpriseAdminDeletePreReceiveHook"></a>
# **enterpriseAdminDeletePreReceiveHook**
> enterpriseAdminDeletePreReceiveHook(preReceiveHookId)

Delete a pre-receive hook



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer preReceiveHookId = 56; // Integer | The unique identifier of the pre-receive hook.
    try {
      apiInstance.enterpriseAdminDeletePreReceiveHook(preReceiveHookId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminDeletePreReceiveHook");
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
| **preReceiveHookId** | **Integer**| The unique identifier of the pre-receive hook. | |

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

<a id="enterpriseAdminDeletePublicKey"></a>
# **enterpriseAdminDeletePublicKey**
> enterpriseAdminDeletePublicKey(keyIds)

Delete a public key



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String keyIds = "keyIds_example"; // String | The unique identifier of the key.
    try {
      apiInstance.enterpriseAdminDeletePublicKey(keyIds);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminDeletePublicKey");
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
| **keyIds** | **String**| The unique identifier of the key. | |

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

<a id="enterpriseAdminDeleteSelfHostedRunnerFromEnterprise"></a>
# **enterpriseAdminDeleteSelfHostedRunnerFromEnterprise**
> enterpriseAdminDeleteSelfHostedRunnerFromEnterprise(enterprise, runnerId)

Delete a self-hosted runner from an enterprise

Forces the removal of a self-hosted runner from an enterprise. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    try {
      apiInstance.enterpriseAdminDeleteSelfHostedRunnerFromEnterprise(enterprise, runnerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminDeleteSelfHostedRunnerFromEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
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

<a id="enterpriseAdminDeleteSelfHostedRunnerGroupFromEnterprise"></a>
# **enterpriseAdminDeleteSelfHostedRunnerGroupFromEnterprise**
> enterpriseAdminDeleteSelfHostedRunnerGroupFromEnterprise(enterprise, runnerGroupId)

Delete a self-hosted runner group from an enterprise

Deletes a self-hosted runner group for an enterprise.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    try {
      apiInstance.enterpriseAdminDeleteSelfHostedRunnerGroupFromEnterprise(enterprise, runnerGroupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminDeleteSelfHostedRunnerGroupFromEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
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

<a id="enterpriseAdminDeleteUser"></a>
# **enterpriseAdminDeleteUser**
> enterpriseAdminDeleteUser(username)

Delete a user

Deleting a user will delete all their repositories, gists, applications, and personal settings. [Suspending a user](https://docs.github.com/enterprise-server@3.4/rest/reference/enterprise-admin#suspend-a-user) is often a better option.  You can delete any user account except your own.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String username = "username_example"; // String | The handle for the GitHub user account.
    try {
      apiInstance.enterpriseAdminDeleteUser(username);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminDeleteUser");
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
| **username** | **String**| The handle for the GitHub user account. | |

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

<a id="enterpriseAdminDemoteSiteAdministrator"></a>
# **enterpriseAdminDemoteSiteAdministrator**
> enterpriseAdminDemoteSiteAdministrator(username)

Demote a site administrator

You can demote any user account except your own.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String username = "username_example"; // String | The handle for the GitHub user account.
    try {
      apiInstance.enterpriseAdminDemoteSiteAdministrator(username);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminDemoteSiteAdministrator");
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
| **username** | **String**| The handle for the GitHub user account. | |

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

<a id="enterpriseAdminDisableSelectedOrganizationGithubActionsEnterprise"></a>
# **enterpriseAdminDisableSelectedOrganizationGithubActionsEnterprise**
> enterpriseAdminDisableSelectedOrganizationGithubActionsEnterprise(enterprise, orgId)

Disable a selected organization for GitHub Actions in an enterprise

Removes an organization from the list of selected organizations that are enabled for GitHub Actions in an enterprise. To use this endpoint, the enterprise permission policy for &#x60;enabled_organizations&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer orgId = 56; // Integer | The unique identifier of the organization.
    try {
      apiInstance.enterpriseAdminDisableSelectedOrganizationGithubActionsEnterprise(enterprise, orgId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminDisableSelectedOrganizationGithubActionsEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **orgId** | **Integer**| The unique identifier of the organization. | |

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

<a id="enterpriseAdminEnableOrDisableMaintenanceMode"></a>
# **enterpriseAdminEnableOrDisableMaintenanceMode**
> MaintenanceStatus enterpriseAdminEnableOrDisableMaintenanceMode(maintenance)

Enable or disable maintenance mode

**Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String maintenance = "maintenance_example"; // String | A JSON string with the attributes `enabled` and `when`.  The possible values for `enabled` are `true` and `false`. When it's `false`, the attribute `when` is ignored and the maintenance mode is turned off. `when` defines the time period when the maintenance was enabled.  The possible values for `when` are `now` or any date parseable by [mojombo/chronic](https://github.com/mojombo/chronic).
    try {
      MaintenanceStatus result = apiInstance.enterpriseAdminEnableOrDisableMaintenanceMode(maintenance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminEnableOrDisableMaintenanceMode");
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
| **maintenance** | **String**| A JSON string with the attributes &#x60;enabled&#x60; and &#x60;when&#x60;.  The possible values for &#x60;enabled&#x60; are &#x60;true&#x60; and &#x60;false&#x60;. When it&#39;s &#x60;false&#x60;, the attribute &#x60;when&#x60; is ignored and the maintenance mode is turned off. &#x60;when&#x60; defines the time period when the maintenance was enabled.  The possible values for &#x60;when&#x60; are &#x60;now&#x60; or any date parseable by [mojombo/chronic](https://github.com/mojombo/chronic). | |

### Return type

[**MaintenanceStatus**](MaintenanceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminEnableSelectedOrganizationGithubActionsEnterprise"></a>
# **enterpriseAdminEnableSelectedOrganizationGithubActionsEnterprise**
> enterpriseAdminEnableSelectedOrganizationGithubActionsEnterprise(enterprise, orgId)

Enable a selected organization for GitHub Actions in an enterprise

Adds an organization to the list of selected organizations that are enabled for GitHub Actions in an enterprise. To use this endpoint, the enterprise permission policy for &#x60;enabled_organizations&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer orgId = 56; // Integer | The unique identifier of the organization.
    try {
      apiInstance.enterpriseAdminEnableSelectedOrganizationGithubActionsEnterprise(enterprise, orgId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminEnableSelectedOrganizationGithubActionsEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **orgId** | **Integer**| The unique identifier of the organization. | |

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

<a id="enterpriseAdminGetAllAuthorizedSshKeys"></a>
# **enterpriseAdminGetAllAuthorizedSshKeys**
> List&lt;SshKey&gt; enterpriseAdminGetAllAuthorizedSshKeys()

Get all authorized SSH keys



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      List<SshKey> result = apiInstance.enterpriseAdminGetAllAuthorizedSshKeys();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetAllAuthorizedSshKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;SshKey&gt;**](SshKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetAllStats"></a>
# **enterpriseAdminGetAllStats**
> EnterpriseOverview enterpriseAdminGetAllStats()

Get all statistics



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      EnterpriseOverview result = apiInstance.enterpriseAdminGetAllStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetAllStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnterpriseOverview**](EnterpriseOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetAllowedActionsEnterprise"></a>
# **enterpriseAdminGetAllowedActionsEnterprise**
> SelectedActions enterpriseAdminGetAllowedActionsEnterprise(enterprise)

Get allowed actions for an enterprise

Gets the selected actions that are allowed in an enterprise. To use this endpoint, the enterprise permission policy for &#x60;allowed_actions&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    try {
      SelectedActions result = apiInstance.enterpriseAdminGetAllowedActionsEnterprise(enterprise);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetAllowedActionsEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |

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

<a id="enterpriseAdminGetAnnouncement"></a>
# **enterpriseAdminGetAnnouncement**
> Announcement enterpriseAdminGetAnnouncement()

Get the global announcement banner

Gets the current message and expiration date of the global announcement banner in your enterprise.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      Announcement result = apiInstance.enterpriseAdminGetAnnouncement();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetAnnouncement");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Announcement**](Announcement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetAuditLog"></a>
# **enterpriseAdminGetAuditLog**
> List&lt;AuditLogEvent&gt; enterpriseAdminGetAuditLog(enterprise, phrase, include, after, before, order, page, perPage)

Get the audit log for an enterprise

Gets the audit log for an enterprise. To use this endpoint, you must be an enterprise admin, and you must use an access token with the &#x60;admin:enterprise&#x60; scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    String phrase = "phrase_example"; // String | A search phrase. For more information, see [Searching the audit log](https://docs.github.com/enterprise-server@3.4/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/searching-the-audit-log-for-your-enterprise#searching-the-audit-log).
    String include = "web"; // String | The event types to include:  - `web` - returns web (non-Git) events. - `git` - returns Git events. - `all` - returns both web and Git events.  The default is `web`.
    String after = "after_example"; // String | A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for events after this cursor.
    String before = "before_example"; // String | A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for events before this cursor.
    String order = "desc"; // String | The order of audit log events. To list newest events first, specify `desc`. To list oldest events first, specify `asc`.  The default is `desc`.
    Integer page = 1; // Integer | Page number of the results to fetch.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    try {
      List<AuditLogEvent> result = apiInstance.enterpriseAdminGetAuditLog(enterprise, phrase, include, after, before, order, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetAuditLog");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **phrase** | **String**| A search phrase. For more information, see [Searching the audit log](https://docs.github.com/enterprise-server@3.4/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/searching-the-audit-log-for-your-enterprise#searching-the-audit-log). | [optional] |
| **include** | **String**| The event types to include:  - &#x60;web&#x60; - returns web (non-Git) events. - &#x60;git&#x60; - returns Git events. - &#x60;all&#x60; - returns both web and Git events.  The default is &#x60;web&#x60;. | [optional] [enum: web, git, all] |
| **after** | **String**| A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for events after this cursor. | [optional] |
| **before** | **String**| A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for events before this cursor. | [optional] |
| **order** | **String**| The order of audit log events. To list newest events first, specify &#x60;desc&#x60;. To list oldest events first, specify &#x60;asc&#x60;.  The default is &#x60;desc&#x60;. | [optional] [enum: desc, asc] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |

### Return type

[**List&lt;AuditLogEvent&gt;**](AuditLogEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetCommentStats"></a>
# **enterpriseAdminGetCommentStats**
> EnterpriseCommentOverview enterpriseAdminGetCommentStats()

Get comment statistics



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      EnterpriseCommentOverview result = apiInstance.enterpriseAdminGetCommentStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetCommentStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnterpriseCommentOverview**](EnterpriseCommentOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetConfigurationStatus"></a>
# **enterpriseAdminGetConfigurationStatus**
> ConfigurationStatus enterpriseAdminGetConfigurationStatus()

Get the configuration status

This endpoint allows you to check the status of the most recent configuration process:  Note that you may need to wait several seconds after you start a process before you can check its status.  The different statuses are:  | Status        | Description                       | | ------------- | --------------------------------- | | &#x60;PENDING&#x60;     | The job has not started yet       | | &#x60;CONFIGURING&#x60; | The job is running                | | &#x60;DONE&#x60;        | The job has finished correctly    | | &#x60;FAILED&#x60;      | The job has finished unexpectedly |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      ConfigurationStatus result = apiInstance.enterpriseAdminGetConfigurationStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetConfigurationStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationStatus**](ConfigurationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetDownloadStatusForPreReceiveEnvironment"></a>
# **enterpriseAdminGetDownloadStatusForPreReceiveEnvironment**
> PreReceiveEnvironmentDownloadStatus enterpriseAdminGetDownloadStatusForPreReceiveEnvironment(preReceiveEnvironmentId)

Get the download status for a pre-receive environment

In addition to seeing the download status at the \&quot;[Get a pre-receive environment](#get-a-pre-receive-environment)\&quot; endpoint, there is also this separate endpoint for just the download status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer preReceiveEnvironmentId = 56; // Integer | The unique identifier of the pre-receive environment.
    try {
      PreReceiveEnvironmentDownloadStatus result = apiInstance.enterpriseAdminGetDownloadStatusForPreReceiveEnvironment(preReceiveEnvironmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetDownloadStatusForPreReceiveEnvironment");
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
| **preReceiveEnvironmentId** | **Integer**| The unique identifier of the pre-receive environment. | |

### Return type

[**PreReceiveEnvironmentDownloadStatus**](PreReceiveEnvironmentDownloadStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetGistStats"></a>
# **enterpriseAdminGetGistStats**
> EnterpriseGistOverview enterpriseAdminGetGistStats()

Get gist statistics



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      EnterpriseGistOverview result = apiInstance.enterpriseAdminGetGistStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetGistStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnterpriseGistOverview**](EnterpriseGistOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetGithubActionsPermissionsEnterprise"></a>
# **enterpriseAdminGetGithubActionsPermissionsEnterprise**
> ActionsEnterprisePermissions enterpriseAdminGetGithubActionsPermissionsEnterprise(enterprise)

Get GitHub Actions permissions for an enterprise

Gets the GitHub Actions permissions policy for organizations and allowed actions in an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    try {
      ActionsEnterprisePermissions result = apiInstance.enterpriseAdminGetGithubActionsPermissionsEnterprise(enterprise);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetGithubActionsPermissionsEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |

### Return type

[**ActionsEnterprisePermissions**](ActionsEnterprisePermissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetGlobalWebhook"></a>
# **enterpriseAdminGetGlobalWebhook**
> GlobalHook enterpriseAdminGetGlobalWebhook(hookId)

Get a global webhook



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer hookId = 56; // Integer | The unique identifier of the hook.
    try {
      GlobalHook result = apiInstance.enterpriseAdminGetGlobalWebhook(hookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetGlobalWebhook");
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
| **hookId** | **Integer**| The unique identifier of the hook. | |

### Return type

[**GlobalHook**](GlobalHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetHooksStats"></a>
# **enterpriseAdminGetHooksStats**
> EnterpriseHookOverview enterpriseAdminGetHooksStats()

Get hooks statistics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      EnterpriseHookOverview result = apiInstance.enterpriseAdminGetHooksStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetHooksStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnterpriseHookOverview**](EnterpriseHookOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetIssueStats"></a>
# **enterpriseAdminGetIssueStats**
> EnterpriseIssueOverview enterpriseAdminGetIssueStats()

Get issue statistics



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      EnterpriseIssueOverview result = apiInstance.enterpriseAdminGetIssueStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetIssueStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnterpriseIssueOverview**](EnterpriseIssueOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetLicenseInformation"></a>
# **enterpriseAdminGetLicenseInformation**
> LicenseInfo enterpriseAdminGetLicenseInformation()

Get license information



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      LicenseInfo result = apiInstance.enterpriseAdminGetLicenseInformation();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetLicenseInformation");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LicenseInfo**](LicenseInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetMaintenanceStatus"></a>
# **enterpriseAdminGetMaintenanceStatus**
> MaintenanceStatus enterpriseAdminGetMaintenanceStatus()

Get the maintenance status

Check your installation&#39;s maintenance status:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      MaintenanceStatus result = apiInstance.enterpriseAdminGetMaintenanceStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetMaintenanceStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MaintenanceStatus**](MaintenanceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetMilestoneStats"></a>
# **enterpriseAdminGetMilestoneStats**
> EnterpriseMilestoneOverview enterpriseAdminGetMilestoneStats()

Get milestone statistics



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      EnterpriseMilestoneOverview result = apiInstance.enterpriseAdminGetMilestoneStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetMilestoneStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnterpriseMilestoneOverview**](EnterpriseMilestoneOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetOrgStats"></a>
# **enterpriseAdminGetOrgStats**
> EnterpriseOrganizationOverview enterpriseAdminGetOrgStats()

Get organization statistics



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      EnterpriseOrganizationOverview result = apiInstance.enterpriseAdminGetOrgStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetOrgStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnterpriseOrganizationOverview**](EnterpriseOrganizationOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetPagesStats"></a>
# **enterpriseAdminGetPagesStats**
> EnterprisePageOverview enterpriseAdminGetPagesStats()

Get pages statistics



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      EnterprisePageOverview result = apiInstance.enterpriseAdminGetPagesStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetPagesStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnterprisePageOverview**](EnterprisePageOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetPreReceiveEnvironment"></a>
# **enterpriseAdminGetPreReceiveEnvironment**
> PreReceiveEnvironment enterpriseAdminGetPreReceiveEnvironment(preReceiveEnvironmentId)

Get a pre-receive environment



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer preReceiveEnvironmentId = 56; // Integer | The unique identifier of the pre-receive environment.
    try {
      PreReceiveEnvironment result = apiInstance.enterpriseAdminGetPreReceiveEnvironment(preReceiveEnvironmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetPreReceiveEnvironment");
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
| **preReceiveEnvironmentId** | **Integer**| The unique identifier of the pre-receive environment. | |

### Return type

[**PreReceiveEnvironment**](PreReceiveEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetPreReceiveHook"></a>
# **enterpriseAdminGetPreReceiveHook**
> PreReceiveHook enterpriseAdminGetPreReceiveHook(preReceiveHookId)

Get a pre-receive hook



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer preReceiveHookId = 56; // Integer | The unique identifier of the pre-receive hook.
    try {
      PreReceiveHook result = apiInstance.enterpriseAdminGetPreReceiveHook(preReceiveHookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetPreReceiveHook");
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
| **preReceiveHookId** | **Integer**| The unique identifier of the pre-receive hook. | |

### Return type

[**PreReceiveHook**](PreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetPreReceiveHookForOrg"></a>
# **enterpriseAdminGetPreReceiveHookForOrg**
> OrgPreReceiveHook enterpriseAdminGetPreReceiveHookForOrg(org, preReceiveHookId)

Get a pre-receive hook for an organization



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer preReceiveHookId = 56; // Integer | The unique identifier of the pre-receive hook.
    try {
      OrgPreReceiveHook result = apiInstance.enterpriseAdminGetPreReceiveHookForOrg(org, preReceiveHookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetPreReceiveHookForOrg");
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
| **preReceiveHookId** | **Integer**| The unique identifier of the pre-receive hook. | |

### Return type

[**OrgPreReceiveHook**](OrgPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetPreReceiveHookForRepo"></a>
# **enterpriseAdminGetPreReceiveHookForRepo**
> RepositoryPreReceiveHook enterpriseAdminGetPreReceiveHookForRepo(owner, repo, preReceiveHookId)

Get a pre-receive hook for a repository



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer preReceiveHookId = 56; // Integer | The unique identifier of the pre-receive hook.
    try {
      RepositoryPreReceiveHook result = apiInstance.enterpriseAdminGetPreReceiveHookForRepo(owner, repo, preReceiveHookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetPreReceiveHookForRepo");
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
| **preReceiveHookId** | **Integer**| The unique identifier of the pre-receive hook. | |

### Return type

[**RepositoryPreReceiveHook**](RepositoryPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetPullRequestStats"></a>
# **enterpriseAdminGetPullRequestStats**
> EnterprisePullRequestOverview enterpriseAdminGetPullRequestStats()

Get pull request statistics



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      EnterprisePullRequestOverview result = apiInstance.enterpriseAdminGetPullRequestStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetPullRequestStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnterprisePullRequestOverview**](EnterprisePullRequestOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetRepoStats"></a>
# **enterpriseAdminGetRepoStats**
> EnterpriseRepositoryOverview enterpriseAdminGetRepoStats()

Get repository statistics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      EnterpriseRepositoryOverview result = apiInstance.enterpriseAdminGetRepoStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetRepoStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnterpriseRepositoryOverview**](EnterpriseRepositoryOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetSelfHostedRunnerForEnterprise"></a>
# **enterpriseAdminGetSelfHostedRunnerForEnterprise**
> Runner enterpriseAdminGetSelfHostedRunnerForEnterprise(enterprise, runnerId)

Get a self-hosted runner for an enterprise

Gets a specific self-hosted runner configured in an enterprise.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    try {
      Runner result = apiInstance.enterpriseAdminGetSelfHostedRunnerForEnterprise(enterprise, runnerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetSelfHostedRunnerForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
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

<a id="enterpriseAdminGetSelfHostedRunnerGroupForEnterprise"></a>
# **enterpriseAdminGetSelfHostedRunnerGroupForEnterprise**
> RunnerGroupsEnterprise enterpriseAdminGetSelfHostedRunnerGroupForEnterprise(enterprise, runnerGroupId)

Get a self-hosted runner group for an enterprise

Gets a specific self-hosted runner group for an enterprise.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    try {
      RunnerGroupsEnterprise result = apiInstance.enterpriseAdminGetSelfHostedRunnerGroupForEnterprise(enterprise, runnerGroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetSelfHostedRunnerGroupForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |

### Return type

[**RunnerGroupsEnterprise**](RunnerGroupsEnterprise.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetSettings"></a>
# **enterpriseAdminGetSettings**
> EnterpriseSettings enterpriseAdminGetSettings()

Get settings

Gets the settings for your instance. To change settings, see the [Set settings endpoint](https://docs.github.com/enterprise-server@3.4/rest/reference/enterprise-admin#set-settings).  **Note:** You cannot retrieve the management console password with the Enterprise administration API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      EnterpriseSettings result = apiInstance.enterpriseAdminGetSettings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnterpriseSettings**](EnterpriseSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminGetUserStats"></a>
# **enterpriseAdminGetUserStats**
> EnterpriseUserOverview enterpriseAdminGetUserStats()

Get users statistics



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      EnterpriseUserOverview result = apiInstance.enterpriseAdminGetUserStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminGetUserStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnterpriseUserOverview**](EnterpriseUserOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminListGlobalWebhooks"></a>
# **enterpriseAdminListGlobalWebhooks**
> List&lt;GlobalHook&gt; enterpriseAdminListGlobalWebhooks(perPage, page)

List global webhooks



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<GlobalHook> result = apiInstance.enterpriseAdminListGlobalWebhooks(perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListGlobalWebhooks");
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
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;GlobalHook&gt;**](GlobalHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="enterpriseAdminListLabelsForSelfHostedRunnerForEnterprise"></a>
# **enterpriseAdminListLabelsForSelfHostedRunnerForEnterprise**
> EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response enterpriseAdminListLabelsForSelfHostedRunnerForEnterprise(enterprise, runnerId)

List labels for a self-hosted runner for an enterprise

Lists all labels for a self-hosted runner configured in an enterprise.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    try {
      EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response result = apiInstance.enterpriseAdminListLabelsForSelfHostedRunnerForEnterprise(enterprise, runnerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListLabelsForSelfHostedRunnerForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **runnerId** | **Integer**| Unique identifier of the self-hosted runner. | |

### Return type

[**EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response**](EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="enterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise"></a>
# **enterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise**
> EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response enterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, perPage, page)

List organization access to a self-hosted runner group in an enterprise

Lists the organizations with access to a self-hosted runner group.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response result = apiInstance.enterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response**](EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminListPersonalAccessTokens"></a>
# **enterpriseAdminListPersonalAccessTokens**
> List&lt;Authorization&gt; enterpriseAdminListPersonalAccessTokens(perPage, page)

List personal access tokens

Lists personal access tokens for all users, including admin users.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Authorization> result = apiInstance.enterpriseAdminListPersonalAccessTokens(perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListPersonalAccessTokens");
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
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Authorization&gt;**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="enterpriseAdminListPreReceiveEnvironments"></a>
# **enterpriseAdminListPreReceiveEnvironments**
> List&lt;PreReceiveEnvironment&gt; enterpriseAdminListPreReceiveEnvironments(perPage, page, direction, sort)

List pre-receive environments



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    String direction = "asc"; // String | The direction to sort the results by.
    String sort = "created"; // String | 
    try {
      List<PreReceiveEnvironment> result = apiInstance.enterpriseAdminListPreReceiveEnvironments(perPage, page, direction, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListPreReceiveEnvironments");
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
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **direction** | **String**| The direction to sort the results by. | [optional] [default to desc] [enum: asc, desc] |
| **sort** | **String**|  | [optional] [default to created] [enum: created, updated, name] |

### Return type

[**List&lt;PreReceiveEnvironment&gt;**](PreReceiveEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminListPreReceiveHooks"></a>
# **enterpriseAdminListPreReceiveHooks**
> List&lt;PreReceiveHook&gt; enterpriseAdminListPreReceiveHooks(perPage, page, direction, sort)

List pre-receive hooks



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    String direction = "asc"; // String | The direction to sort the results by.
    String sort = "created"; // String | The property to sort the results by.
    try {
      List<PreReceiveHook> result = apiInstance.enterpriseAdminListPreReceiveHooks(perPage, page, direction, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListPreReceiveHooks");
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
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **direction** | **String**| The direction to sort the results by. | [optional] [default to desc] [enum: asc, desc] |
| **sort** | **String**| The property to sort the results by. | [optional] [default to created] [enum: created, updated, name] |

### Return type

[**List&lt;PreReceiveHook&gt;**](PreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminListPreReceiveHooksForOrg"></a>
# **enterpriseAdminListPreReceiveHooksForOrg**
> List&lt;OrgPreReceiveHook&gt; enterpriseAdminListPreReceiveHooksForOrg(org, perPage, page, direction, sort)

List pre-receive hooks for an organization

List all pre-receive hooks that are enabled or testing for this organization as well as any disabled hooks that can be configured at the organization level. Globally disabled pre-receive hooks that do not allow downstream configuration are not listed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    String direction = "asc"; // String | The direction to sort the results by.
    String sort = "created"; // String | The sort order for the response collection.
    try {
      List<OrgPreReceiveHook> result = apiInstance.enterpriseAdminListPreReceiveHooksForOrg(org, perPage, page, direction, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListPreReceiveHooksForOrg");
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
| **direction** | **String**| The direction to sort the results by. | [optional] [default to desc] [enum: asc, desc] |
| **sort** | **String**| The sort order for the response collection. | [optional] [default to created] [enum: created, updated, name] |

### Return type

[**List&lt;OrgPreReceiveHook&gt;**](OrgPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminListPreReceiveHooksForRepo"></a>
# **enterpriseAdminListPreReceiveHooksForRepo**
> List&lt;RepositoryPreReceiveHook&gt; enterpriseAdminListPreReceiveHooksForRepo(owner, repo, perPage, page, direction, sort)

List pre-receive hooks for a repository

List all pre-receive hooks that are enabled or testing for this repository as well as any disabled hooks that are allowed to be enabled at the repository level. Pre-receive hooks that are disabled at a higher level and are not configurable will not be listed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    String direction = "asc"; // String | The direction to sort the results by.
    String sort = "created"; // String | 
    try {
      List<RepositoryPreReceiveHook> result = apiInstance.enterpriseAdminListPreReceiveHooksForRepo(owner, repo, perPage, page, direction, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListPreReceiveHooksForRepo");
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
| **direction** | **String**| The direction to sort the results by. | [optional] [default to desc] [enum: asc, desc] |
| **sort** | **String**|  | [optional] [default to created] [enum: created, updated, name] |

### Return type

[**List&lt;RepositoryPreReceiveHook&gt;**](RepositoryPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminListPublicKeys"></a>
# **enterpriseAdminListPublicKeys**
> List&lt;PublicKeyFull&gt; enterpriseAdminListPublicKeys(perPage, page, direction, sort, since)

List public keys



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    String direction = "asc"; // String | The direction to sort the results by.
    String sort = "created"; // String | 
    String since = "since_example"; // String | Only show public keys accessed after the given time.
    try {
      List<PublicKeyFull> result = apiInstance.enterpriseAdminListPublicKeys(perPage, page, direction, sort, since);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListPublicKeys");
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
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **direction** | **String**| The direction to sort the results by. | [optional] [default to desc] [enum: asc, desc] |
| **sort** | **String**|  | [optional] [default to created] [enum: created, updated, accessed] |
| **since** | **String**| Only show public keys accessed after the given time. | [optional] |

### Return type

[**List&lt;PublicKeyFull&gt;**](PublicKeyFull.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="enterpriseAdminListRunnerApplicationsForEnterprise"></a>
# **enterpriseAdminListRunnerApplicationsForEnterprise**
> List&lt;RunnerApplication&gt; enterpriseAdminListRunnerApplicationsForEnterprise(enterprise)

List runner applications for an enterprise

Lists binaries for the runner application that you can download and run.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    try {
      List<RunnerApplication> result = apiInstance.enterpriseAdminListRunnerApplicationsForEnterprise(enterprise);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListRunnerApplicationsForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |

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

<a id="enterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise"></a>
# **enterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise**
> EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response enterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise(enterprise, perPage, page)

List selected organizations enabled for GitHub Actions in an enterprise

Lists the organizations that are selected to have GitHub Actions enabled in an enterprise. To use this endpoint, the enterprise permission policy for &#x60;enabled_organizations&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response result = apiInstance.enterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise(enterprise, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response**](EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminListSelfHostedRunnerGroupsForEnterprise"></a>
# **enterpriseAdminListSelfHostedRunnerGroupsForEnterprise**
> EnterpriseAdminListSelfHostedRunnerGroupsForEnterprise200Response enterpriseAdminListSelfHostedRunnerGroupsForEnterprise(enterprise, perPage, page)

List self-hosted runner groups for an enterprise

Lists all self-hosted runner groups for an enterprise.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      EnterpriseAdminListSelfHostedRunnerGroupsForEnterprise200Response result = apiInstance.enterpriseAdminListSelfHostedRunnerGroupsForEnterprise(enterprise, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListSelfHostedRunnerGroupsForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**EnterpriseAdminListSelfHostedRunnerGroupsForEnterprise200Response**](EnterpriseAdminListSelfHostedRunnerGroupsForEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminListSelfHostedRunnersForEnterprise"></a>
# **enterpriseAdminListSelfHostedRunnersForEnterprise**
> EnterpriseAdminListSelfHostedRunnersForEnterprise200Response enterpriseAdminListSelfHostedRunnersForEnterprise(enterprise, perPage, page)

List self-hosted runners for an enterprise

Lists all self-hosted runners configured for an enterprise.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      EnterpriseAdminListSelfHostedRunnersForEnterprise200Response result = apiInstance.enterpriseAdminListSelfHostedRunnersForEnterprise(enterprise, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListSelfHostedRunnersForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**EnterpriseAdminListSelfHostedRunnersForEnterprise200Response**](EnterpriseAdminListSelfHostedRunnersForEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="enterpriseAdminListSelfHostedRunnersInGroupForEnterprise"></a>
# **enterpriseAdminListSelfHostedRunnersInGroupForEnterprise**
> EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise200Response enterpriseAdminListSelfHostedRunnersInGroupForEnterprise(enterprise, runnerGroupId, perPage, page)

List self-hosted runners in a group for an enterprise

Lists the self-hosted runners that are in a specific enterprise group.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise200Response result = apiInstance.enterpriseAdminListSelfHostedRunnersInGroupForEnterprise(enterprise, runnerGroupId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminListSelfHostedRunnersInGroupForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
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

<a id="enterpriseAdminPingGlobalWebhook"></a>
# **enterpriseAdminPingGlobalWebhook**
> enterpriseAdminPingGlobalWebhook(hookId)

Ping a global webhook

This will trigger a [ping event](https://docs.github.com/enterprise-server@3.4/webhooks/#ping-event) to be sent to the webhook.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer hookId = 56; // Integer | The unique identifier of the hook.
    try {
      apiInstance.enterpriseAdminPingGlobalWebhook(hookId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminPingGlobalWebhook");
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
| **hookId** | **Integer**| The unique identifier of the hook. | |

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

<a id="enterpriseAdminPromoteUserToBeSiteAdministrator"></a>
# **enterpriseAdminPromoteUserToBeSiteAdministrator**
> enterpriseAdminPromoteUserToBeSiteAdministrator(username)

Promote a user to be a site administrator

Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String username = "username_example"; // String | The handle for the GitHub user account.
    try {
      apiInstance.enterpriseAdminPromoteUserToBeSiteAdministrator(username);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminPromoteUserToBeSiteAdministrator");
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
| **username** | **String**| The handle for the GitHub user account. | |

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

<a id="enterpriseAdminRemoveAllCustomLabelsFromSelfHostedRunnerForEnterprise"></a>
# **enterpriseAdminRemoveAllCustomLabelsFromSelfHostedRunnerForEnterprise**
> EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response enterpriseAdminRemoveAllCustomLabelsFromSelfHostedRunnerForEnterprise(enterprise, runnerId)

Remove all custom labels from a self-hosted runner for an enterprise

Remove all custom labels from a self-hosted runner configured in an enterprise. Returns the remaining read-only labels from the runner.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    try {
      EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response result = apiInstance.enterpriseAdminRemoveAllCustomLabelsFromSelfHostedRunnerForEnterprise(enterprise, runnerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminRemoveAllCustomLabelsFromSelfHostedRunnerForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **runnerId** | **Integer**| Unique identifier of the self-hosted runner. | |

### Return type

[**EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response**](EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="enterpriseAdminRemoveAnnouncement"></a>
# **enterpriseAdminRemoveAnnouncement**
> enterpriseAdminRemoveAnnouncement()

Remove the global announcement banner

Removes the global announcement banner in your enterprise.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      apiInstance.enterpriseAdminRemoveAnnouncement();
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminRemoveAnnouncement");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="enterpriseAdminRemoveAuthorizedSshKey"></a>
# **enterpriseAdminRemoveAuthorizedSshKey**
> List&lt;SshKey&gt; enterpriseAdminRemoveAuthorizedSshKey(authorizedKey)

Remove an authorized SSH key

**Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String authorizedKey = "authorizedKey_example"; // String | The public SSH key.
    try {
      List<SshKey> result = apiInstance.enterpriseAdminRemoveAuthorizedSshKey(authorizedKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminRemoveAuthorizedSshKey");
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
| **authorizedKey** | **String**| The public SSH key. | |

### Return type

[**List&lt;SshKey&gt;**](SshKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminRemoveCustomLabelFromSelfHostedRunnerForEnterprise"></a>
# **enterpriseAdminRemoveCustomLabelFromSelfHostedRunnerForEnterprise**
> EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response enterpriseAdminRemoveCustomLabelFromSelfHostedRunnerForEnterprise(enterprise, runnerId, name)

Remove a custom label from a self-hosted runner for an enterprise

Remove a custom label from a self-hosted runner configured in an enterprise. Returns the remaining labels from the runner.  This endpoint returns a &#x60;404 Not Found&#x60; status if the custom label is not present on the runner.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    String name = "name_example"; // String | The name of a self-hosted runner's custom label.
    try {
      EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response result = apiInstance.enterpriseAdminRemoveCustomLabelFromSelfHostedRunnerForEnterprise(enterprise, runnerId, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminRemoveCustomLabelFromSelfHostedRunnerForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **runnerId** | **Integer**| Unique identifier of the self-hosted runner. | |
| **name** | **String**| The name of a self-hosted runner&#39;s custom label. | |

### Return type

[**EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response**](EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="enterpriseAdminRemoveOrgAccessToSelfHostedRunnerGroupInEnterprise"></a>
# **enterpriseAdminRemoveOrgAccessToSelfHostedRunnerGroupInEnterprise**
> enterpriseAdminRemoveOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, orgId)

Remove organization access to a self-hosted runner group in an enterprise

Removes an organization from the list of selected organizations that can access a self-hosted runner group. The runner group must have &#x60;visibility&#x60; set to &#x60;selected&#x60;. For more information, see \&quot;[Create a self-hosted runner group for an enterprise](#create-a-self-hosted-runner-group-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    Integer orgId = 56; // Integer | The unique identifier of the organization.
    try {
      apiInstance.enterpriseAdminRemoveOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, orgId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminRemoveOrgAccessToSelfHostedRunnerGroupInEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **orgId** | **Integer**| The unique identifier of the organization. | |

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

<a id="enterpriseAdminRemovePreReceiveHookEnforcementForOrg"></a>
# **enterpriseAdminRemovePreReceiveHookEnforcementForOrg**
> OrgPreReceiveHook enterpriseAdminRemovePreReceiveHookEnforcementForOrg(org, preReceiveHookId)

Remove pre-receive hook enforcement for an organization

Removes any overrides for this hook at the org level for this org.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer preReceiveHookId = 56; // Integer | The unique identifier of the pre-receive hook.
    try {
      OrgPreReceiveHook result = apiInstance.enterpriseAdminRemovePreReceiveHookEnforcementForOrg(org, preReceiveHookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminRemovePreReceiveHookEnforcementForOrg");
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
| **preReceiveHookId** | **Integer**| The unique identifier of the pre-receive hook. | |

### Return type

[**OrgPreReceiveHook**](OrgPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminRemovePreReceiveHookEnforcementForRepo"></a>
# **enterpriseAdminRemovePreReceiveHookEnforcementForRepo**
> RepositoryPreReceiveHook enterpriseAdminRemovePreReceiveHookEnforcementForRepo(owner, repo, preReceiveHookId)

Remove pre-receive hook enforcement for a repository

Deletes any overridden enforcement on this repository for the specified hook.  Responds with effective values inherited from owner and/or global level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer preReceiveHookId = 56; // Integer | The unique identifier of the pre-receive hook.
    try {
      RepositoryPreReceiveHook result = apiInstance.enterpriseAdminRemovePreReceiveHookEnforcementForRepo(owner, repo, preReceiveHookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminRemovePreReceiveHookEnforcementForRepo");
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
| **preReceiveHookId** | **Integer**| The unique identifier of the pre-receive hook. | |

### Return type

[**RepositoryPreReceiveHook**](RepositoryPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Responds with effective values inherited from owner and/or global level. |  -  |

<a id="enterpriseAdminRemoveSelfHostedRunnerFromGroupForEnterprise"></a>
# **enterpriseAdminRemoveSelfHostedRunnerFromGroupForEnterprise**
> enterpriseAdminRemoveSelfHostedRunnerFromGroupForEnterprise(enterprise, runnerGroupId, runnerId)

Remove a self-hosted runner from a group for an enterprise

Removes a self-hosted runner from a group configured in an enterprise. The runner is then returned to the default group.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    try {
      apiInstance.enterpriseAdminRemoveSelfHostedRunnerFromGroupForEnterprise(enterprise, runnerGroupId, runnerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminRemoveSelfHostedRunnerFromGroupForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
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

<a id="enterpriseAdminSetAllowedActionsEnterprise"></a>
# **enterpriseAdminSetAllowedActionsEnterprise**
> enterpriseAdminSetAllowedActionsEnterprise(enterprise, selectedActions)

Set allowed actions for an enterprise

Sets the actions that are allowed in an enterprise. To use this endpoint, the enterprise permission policy for &#x60;allowed_actions&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    SelectedActions selectedActions = new SelectedActions(); // SelectedActions | 
    try {
      apiInstance.enterpriseAdminSetAllowedActionsEnterprise(enterprise, selectedActions);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminSetAllowedActionsEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **selectedActions** | [**SelectedActions**](SelectedActions.md)|  | |

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

<a id="enterpriseAdminSetAnnouncement"></a>
# **enterpriseAdminSetAnnouncement**
> Announcement enterpriseAdminSetAnnouncement(announcement)

Set the global announcement banner

Sets the message and expiration time for the global announcement banner in your enterprise.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Announcement announcement = new Announcement(); // Announcement | 
    try {
      Announcement result = apiInstance.enterpriseAdminSetAnnouncement(announcement);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminSetAnnouncement");
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
| **announcement** | [**Announcement**](Announcement.md)|  | |

### Return type

[**Announcement**](Announcement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterprise"></a>
# **enterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterprise**
> EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response enterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterprise(enterprise, runnerId, enterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterpriseRequest)

Set custom labels for a self-hosted runner for an enterprise

Remove all previous custom labels and set the new custom labels for a specific self-hosted runner configured in an enterprise.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerId = 56; // Integer | Unique identifier of the self-hosted runner.
    EnterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterpriseRequest enterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterpriseRequest = new EnterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterpriseRequest(); // EnterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterpriseRequest | 
    try {
      EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response result = apiInstance.enterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterprise(enterprise, runnerId, enterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterpriseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **runnerId** | **Integer**| Unique identifier of the self-hosted runner. | |
| **enterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterpriseRequest** | [**EnterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterpriseRequest**](EnterpriseAdminSetCustomLabelsForSelfHostedRunnerForEnterpriseRequest.md)|  | |

### Return type

[**EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response**](EnterpriseAdminListLabelsForSelfHostedRunnerForEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="enterpriseAdminSetGithubActionsPermissionsEnterprise"></a>
# **enterpriseAdminSetGithubActionsPermissionsEnterprise**
> enterpriseAdminSetGithubActionsPermissionsEnterprise(enterprise, enterpriseAdminSetGithubActionsPermissionsEnterpriseRequest)

Set GitHub Actions permissions for an enterprise

Sets the GitHub Actions permissions policy for organizations and allowed actions in an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    EnterpriseAdminSetGithubActionsPermissionsEnterpriseRequest enterpriseAdminSetGithubActionsPermissionsEnterpriseRequest = new EnterpriseAdminSetGithubActionsPermissionsEnterpriseRequest(); // EnterpriseAdminSetGithubActionsPermissionsEnterpriseRequest | 
    try {
      apiInstance.enterpriseAdminSetGithubActionsPermissionsEnterprise(enterprise, enterpriseAdminSetGithubActionsPermissionsEnterpriseRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminSetGithubActionsPermissionsEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **enterpriseAdminSetGithubActionsPermissionsEnterpriseRequest** | [**EnterpriseAdminSetGithubActionsPermissionsEnterpriseRequest**](EnterpriseAdminSetGithubActionsPermissionsEnterpriseRequest.md)|  | |

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

<a id="enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterprise"></a>
# **enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterprise**
> enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest)

Set organization access for a self-hosted runner group in an enterprise

Replaces the list of organizations that have access to a self-hosted runner configured in an enterprise.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    EnterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest = new EnterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest(); // EnterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest | 
    try {
      apiInstance.enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest** | [**EnterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest**](EnterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest.md)|  | |

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

<a id="enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterprise"></a>
# **enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterprise**
> enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterprise(enterprise, enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest)

Set selected organizations enabled for GitHub Actions in an enterprise

Replaces the list of selected organizations that are enabled for GitHub Actions in an enterprise. To use this endpoint, the enterprise permission policy for &#x60;enabled_organizations&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    EnterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest = new EnterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest(); // EnterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest | 
    try {
      apiInstance.enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterprise(enterprise, enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest** | [**EnterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest**](EnterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest.md)|  | |

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

<a id="enterpriseAdminSetSelfHostedRunnersInGroupForEnterprise"></a>
# **enterpriseAdminSetSelfHostedRunnersInGroupForEnterprise**
> enterpriseAdminSetSelfHostedRunnersInGroupForEnterprise(enterprise, runnerGroupId, enterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest)

Set self-hosted runners in a group for an enterprise

Replaces the list of self-hosted runners that are part of an enterprise runner group.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest enterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest = new EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest(); // EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest | 
    try {
      apiInstance.enterpriseAdminSetSelfHostedRunnersInGroupForEnterprise(enterprise, runnerGroupId, enterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminSetSelfHostedRunnersInGroupForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
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

<a id="enterpriseAdminSetSettings"></a>
# **enterpriseAdminSetSettings**
> enterpriseAdminSetSettings(settings)

Set settings

Applies settings on your instance. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@3.4/rest/reference/enterprise-admin#get-settings).  **Notes:**  - The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode). - You cannot set the management console password with the Enterprise administration API. Use the &#x60;ghe-set-password&#x60; utility to change the management console password. For more information, see \&quot;[Command-line utilities](https://docs.github.com/enterprise-server@3.4/admin/configuration/configuring-your-enterprise/command-line-utilities#ghe-set-password).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String settings = "settings_example"; // String | A JSON string with the new settings. Note that you only need to pass the specific settings you want to modify. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@3.4/rest/reference/enterprise-admin#get-settings).
    try {
      apiInstance.enterpriseAdminSetSettings(settings);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminSetSettings");
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
| **settings** | **String**| A JSON string with the new settings. Note that you only need to pass the specific settings you want to modify. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@3.4/rest/reference/enterprise-admin#get-settings). | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="enterpriseAdminStartConfigurationProcess"></a>
# **enterpriseAdminStartConfigurationProcess**
> enterpriseAdminStartConfigurationProcess()

Start a configuration process

This endpoint allows you to start a configuration process at any time for your updated settings to take effect:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    try {
      apiInstance.enterpriseAdminStartConfigurationProcess();
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminStartConfigurationProcess");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **202** | Response |  -  |

<a id="enterpriseAdminStartPreReceiveEnvironmentDownload"></a>
# **enterpriseAdminStartPreReceiveEnvironmentDownload**
> PreReceiveEnvironmentDownloadStatus enterpriseAdminStartPreReceiveEnvironmentDownload(preReceiveEnvironmentId)

Start a pre-receive environment download

Triggers a new download of the environment tarball from the environment&#39;s &#x60;image_url&#x60;. When the download is finished, the newly downloaded tarball will overwrite the existing environment.  If a download cannot be triggered, you will receive a &#x60;422 Unprocessable Entity&#x60; response.  The possible error messages are:  * _Cannot modify or delete the default environment_ * _Can not start a new download when a download is in progress_

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer preReceiveEnvironmentId = 56; // Integer | The unique identifier of the pre-receive environment.
    try {
      PreReceiveEnvironmentDownloadStatus result = apiInstance.enterpriseAdminStartPreReceiveEnvironmentDownload(preReceiveEnvironmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminStartPreReceiveEnvironmentDownload");
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
| **preReceiveEnvironmentId** | **Integer**| The unique identifier of the pre-receive environment. | |

### Return type

[**PreReceiveEnvironmentDownloadStatus**](PreReceiveEnvironmentDownloadStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Response |  -  |
| **422** | Client Errors |  -  |

<a id="enterpriseAdminSuspendUser"></a>
# **enterpriseAdminSuspendUser**
> enterpriseAdminSuspendUser(username, enterpriseAdminSuspendUserRequest)

Suspend a user

If your GitHub instance uses [LDAP Sync with Active Directory LDAP servers](https://docs.github.com/enterprise-server@3.4/admin/identity-and-access-management/using-ldap-for-enterprise-iam/using-ldap), Active Directory LDAP-authenticated users cannot be suspended through this API. If you attempt to suspend an Active Directory LDAP-authenticated user through this API, it will return a &#x60;403&#x60; response.  You can suspend any user account except your own.  Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String username = "username_example"; // String | The handle for the GitHub user account.
    EnterpriseAdminSuspendUserRequest enterpriseAdminSuspendUserRequest = new EnterpriseAdminSuspendUserRequest(); // EnterpriseAdminSuspendUserRequest | 
    try {
      apiInstance.enterpriseAdminSuspendUser(username, enterpriseAdminSuspendUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminSuspendUser");
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
| **username** | **String**| The handle for the GitHub user account. | |
| **enterpriseAdminSuspendUserRequest** | [**EnterpriseAdminSuspendUserRequest**](EnterpriseAdminSuspendUserRequest.md)|  | [optional] |

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

<a id="enterpriseAdminSyncLdapMappingForTeam"></a>
# **enterpriseAdminSyncLdapMappingForTeam**
> EnterpriseAdminSyncLdapMappingForTeam201Response enterpriseAdminSyncLdapMappingForTeam(teamId)

Sync LDAP mapping for a team

Note that this API call does not automatically initiate an LDAP sync. Rather, if a &#x60;201&#x60; is returned, the sync job is queued successfully, and is performed when the instance is ready.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer teamId = 56; // Integer | The unique identifier of the team.
    try {
      EnterpriseAdminSyncLdapMappingForTeam201Response result = apiInstance.enterpriseAdminSyncLdapMappingForTeam(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminSyncLdapMappingForTeam");
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
| **teamId** | **Integer**| The unique identifier of the team. | |

### Return type

[**EnterpriseAdminSyncLdapMappingForTeam201Response**](EnterpriseAdminSyncLdapMappingForTeam201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="enterpriseAdminSyncLdapMappingForUser"></a>
# **enterpriseAdminSyncLdapMappingForUser**
> EnterpriseAdminSyncLdapMappingForTeam201Response enterpriseAdminSyncLdapMappingForUser(username)

Sync LDAP mapping for a user

Note that this API call does not automatically initiate an LDAP sync. Rather, if a &#x60;201&#x60; is returned, the sync job is queued successfully, and is performed when the instance is ready.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String username = "username_example"; // String | The handle for the GitHub user account.
    try {
      EnterpriseAdminSyncLdapMappingForTeam201Response result = apiInstance.enterpriseAdminSyncLdapMappingForUser(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminSyncLdapMappingForUser");
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
| **username** | **String**| The handle for the GitHub user account. | |

### Return type

[**EnterpriseAdminSyncLdapMappingForTeam201Response**](EnterpriseAdminSyncLdapMappingForTeam201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="enterpriseAdminUnsuspendUser"></a>
# **enterpriseAdminUnsuspendUser**
> enterpriseAdminUnsuspendUser(username, enterpriseAdminUnsuspendUserRequest)

Unsuspend a user

If your GitHub instance uses [LDAP Sync with Active Directory LDAP servers](https://docs.github.com/enterprise-server@3.4/admin/identity-and-access-management/using-ldap-for-enterprise-iam/using-ldap), this API is disabled and will return a &#x60;403&#x60; response. Active Directory LDAP-authenticated users cannot be unsuspended using the API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String username = "username_example"; // String | The handle for the GitHub user account.
    EnterpriseAdminUnsuspendUserRequest enterpriseAdminUnsuspendUserRequest = new EnterpriseAdminUnsuspendUserRequest(); // EnterpriseAdminUnsuspendUserRequest | 
    try {
      apiInstance.enterpriseAdminUnsuspendUser(username, enterpriseAdminUnsuspendUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminUnsuspendUser");
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
| **username** | **String**| The handle for the GitHub user account. | |
| **enterpriseAdminUnsuspendUserRequest** | [**EnterpriseAdminUnsuspendUserRequest**](EnterpriseAdminUnsuspendUserRequest.md)|  | [optional] |

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

<a id="enterpriseAdminUpdateGlobalWebhook"></a>
# **enterpriseAdminUpdateGlobalWebhook**
> GlobalHook2 enterpriseAdminUpdateGlobalWebhook(hookId, enterpriseAdminUpdateGlobalWebhookRequest)

Update a global webhook

Parameters that are not provided will be overwritten with the default value or removed if no default exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer hookId = 56; // Integer | The unique identifier of the hook.
    EnterpriseAdminUpdateGlobalWebhookRequest enterpriseAdminUpdateGlobalWebhookRequest = new EnterpriseAdminUpdateGlobalWebhookRequest(); // EnterpriseAdminUpdateGlobalWebhookRequest | 
    try {
      GlobalHook2 result = apiInstance.enterpriseAdminUpdateGlobalWebhook(hookId, enterpriseAdminUpdateGlobalWebhookRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminUpdateGlobalWebhook");
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
| **hookId** | **Integer**| The unique identifier of the hook. | |
| **enterpriseAdminUpdateGlobalWebhookRequest** | [**EnterpriseAdminUpdateGlobalWebhookRequest**](EnterpriseAdminUpdateGlobalWebhookRequest.md)|  | |

### Return type

[**GlobalHook2**](GlobalHook2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminUpdateLdapMappingForTeam"></a>
# **enterpriseAdminUpdateLdapMappingForTeam**
> LdapMappingTeam enterpriseAdminUpdateLdapMappingForTeam(teamId, enterpriseAdminUpdateLdapMappingForTeamRequest)

Update LDAP mapping for a team

Updates the [distinguished name](https://www.ldap.com/ldap-dns-and-rdns) (DN) of the LDAP entry to map to a team. [LDAP synchronization](https://docs.github.com/enterprise-server@3.4/admin/identity-and-access-management/using-ldap-for-enterprise-iam/using-ldap#enabling-ldap-sync) must be enabled to map LDAP entries to a team. Use the [Create a team](https://docs.github.com/enterprise-server@3.4/rest/reference/teams/#create-a-team) endpoint to create a team with LDAP mapping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer teamId = 56; // Integer | The unique identifier of the team.
    EnterpriseAdminUpdateLdapMappingForTeamRequest enterpriseAdminUpdateLdapMappingForTeamRequest = new EnterpriseAdminUpdateLdapMappingForTeamRequest(); // EnterpriseAdminUpdateLdapMappingForTeamRequest | 
    try {
      LdapMappingTeam result = apiInstance.enterpriseAdminUpdateLdapMappingForTeam(teamId, enterpriseAdminUpdateLdapMappingForTeamRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminUpdateLdapMappingForTeam");
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
| **teamId** | **Integer**| The unique identifier of the team. | |
| **enterpriseAdminUpdateLdapMappingForTeamRequest** | [**EnterpriseAdminUpdateLdapMappingForTeamRequest**](EnterpriseAdminUpdateLdapMappingForTeamRequest.md)|  | |

### Return type

[**LdapMappingTeam**](LdapMappingTeam.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminUpdateLdapMappingForUser"></a>
# **enterpriseAdminUpdateLdapMappingForUser**
> LdapMappingUser enterpriseAdminUpdateLdapMappingForUser(username, enterpriseAdminUpdateLdapMappingForTeamRequest)

Update LDAP mapping for a user



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String username = "username_example"; // String | The handle for the GitHub user account.
    EnterpriseAdminUpdateLdapMappingForTeamRequest enterpriseAdminUpdateLdapMappingForTeamRequest = new EnterpriseAdminUpdateLdapMappingForTeamRequest(); // EnterpriseAdminUpdateLdapMappingForTeamRequest | 
    try {
      LdapMappingUser result = apiInstance.enterpriseAdminUpdateLdapMappingForUser(username, enterpriseAdminUpdateLdapMappingForTeamRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminUpdateLdapMappingForUser");
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
| **username** | **String**| The handle for the GitHub user account. | |
| **enterpriseAdminUpdateLdapMappingForTeamRequest** | [**EnterpriseAdminUpdateLdapMappingForTeamRequest**](EnterpriseAdminUpdateLdapMappingForTeamRequest.md)|  | |

### Return type

[**LdapMappingUser**](LdapMappingUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminUpdateOrgName"></a>
# **enterpriseAdminUpdateOrgName**
> EnterpriseAdminUpdateOrgName202Response enterpriseAdminUpdateOrgName(org, enterpriseAdminUpdateOrgNameRequest)

Update an organization name



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    EnterpriseAdminUpdateOrgNameRequest enterpriseAdminUpdateOrgNameRequest = new EnterpriseAdminUpdateOrgNameRequest(); // EnterpriseAdminUpdateOrgNameRequest | 
    try {
      EnterpriseAdminUpdateOrgName202Response result = apiInstance.enterpriseAdminUpdateOrgName(org, enterpriseAdminUpdateOrgNameRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminUpdateOrgName");
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
| **enterpriseAdminUpdateOrgNameRequest** | [**EnterpriseAdminUpdateOrgNameRequest**](EnterpriseAdminUpdateOrgNameRequest.md)|  | |

### Return type

[**EnterpriseAdminUpdateOrgName202Response**](EnterpriseAdminUpdateOrgName202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Response |  -  |

<a id="enterpriseAdminUpdatePreReceiveEnvironment"></a>
# **enterpriseAdminUpdatePreReceiveEnvironment**
> PreReceiveEnvironment enterpriseAdminUpdatePreReceiveEnvironment(preReceiveEnvironmentId, enterpriseAdminUpdatePreReceiveEnvironmentRequest)

Update a pre-receive environment

You cannot modify the default environment. If you attempt to modify the default environment, you will receive a &#x60;422 Unprocessable Entity&#x60; response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer preReceiveEnvironmentId = 56; // Integer | The unique identifier of the pre-receive environment.
    EnterpriseAdminUpdatePreReceiveEnvironmentRequest enterpriseAdminUpdatePreReceiveEnvironmentRequest = new EnterpriseAdminUpdatePreReceiveEnvironmentRequest(); // EnterpriseAdminUpdatePreReceiveEnvironmentRequest | 
    try {
      PreReceiveEnvironment result = apiInstance.enterpriseAdminUpdatePreReceiveEnvironment(preReceiveEnvironmentId, enterpriseAdminUpdatePreReceiveEnvironmentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminUpdatePreReceiveEnvironment");
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
| **preReceiveEnvironmentId** | **Integer**| The unique identifier of the pre-receive environment. | |
| **enterpriseAdminUpdatePreReceiveEnvironmentRequest** | [**EnterpriseAdminUpdatePreReceiveEnvironmentRequest**](EnterpriseAdminUpdatePreReceiveEnvironmentRequest.md)|  | [optional] |

### Return type

[**PreReceiveEnvironment**](PreReceiveEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Client Errors |  -  |

<a id="enterpriseAdminUpdatePreReceiveHook"></a>
# **enterpriseAdminUpdatePreReceiveHook**
> PreReceiveHook enterpriseAdminUpdatePreReceiveHook(preReceiveHookId, enterpriseAdminUpdatePreReceiveHookRequest)

Update a pre-receive hook



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    Integer preReceiveHookId = 56; // Integer | The unique identifier of the pre-receive hook.
    EnterpriseAdminUpdatePreReceiveHookRequest enterpriseAdminUpdatePreReceiveHookRequest = new EnterpriseAdminUpdatePreReceiveHookRequest(); // EnterpriseAdminUpdatePreReceiveHookRequest | 
    try {
      PreReceiveHook result = apiInstance.enterpriseAdminUpdatePreReceiveHook(preReceiveHookId, enterpriseAdminUpdatePreReceiveHookRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminUpdatePreReceiveHook");
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
| **preReceiveHookId** | **Integer**| The unique identifier of the pre-receive hook. | |
| **enterpriseAdminUpdatePreReceiveHookRequest** | [**EnterpriseAdminUpdatePreReceiveHookRequest**](EnterpriseAdminUpdatePreReceiveHookRequest.md)|  | [optional] |

### Return type

[**PreReceiveHook**](PreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminUpdatePreReceiveHookEnforcementForOrg"></a>
# **enterpriseAdminUpdatePreReceiveHookEnforcementForOrg**
> OrgPreReceiveHook enterpriseAdminUpdatePreReceiveHookEnforcementForOrg(org, preReceiveHookId, enterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest)

Update pre-receive hook enforcement for an organization

For pre-receive hooks which are allowed to be configured at the org level, you can set &#x60;enforcement&#x60; and &#x60;allow_downstream_configuration&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    Integer preReceiveHookId = 56; // Integer | The unique identifier of the pre-receive hook.
    EnterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest enterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest = new EnterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest(); // EnterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest | 
    try {
      OrgPreReceiveHook result = apiInstance.enterpriseAdminUpdatePreReceiveHookEnforcementForOrg(org, preReceiveHookId, enterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminUpdatePreReceiveHookEnforcementForOrg");
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
| **preReceiveHookId** | **Integer**| The unique identifier of the pre-receive hook. | |
| **enterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest** | [**EnterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest**](EnterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest.md)|  | [optional] |

### Return type

[**OrgPreReceiveHook**](OrgPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminUpdatePreReceiveHookEnforcementForRepo"></a>
# **enterpriseAdminUpdatePreReceiveHookEnforcementForRepo**
> RepositoryPreReceiveHook enterpriseAdminUpdatePreReceiveHookEnforcementForRepo(owner, repo, preReceiveHookId, enterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest)

Update pre-receive hook enforcement for a repository

For pre-receive hooks which are allowed to be configured at the repo level, you can set &#x60;enforcement&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer preReceiveHookId = 56; // Integer | The unique identifier of the pre-receive hook.
    EnterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest enterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest = new EnterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest(); // EnterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest | 
    try {
      RepositoryPreReceiveHook result = apiInstance.enterpriseAdminUpdatePreReceiveHookEnforcementForRepo(owner, repo, preReceiveHookId, enterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminUpdatePreReceiveHookEnforcementForRepo");
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
| **preReceiveHookId** | **Integer**| The unique identifier of the pre-receive hook. | |
| **enterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest** | [**EnterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest**](EnterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest.md)|  | [optional] |

### Return type

[**RepositoryPreReceiveHook**](RepositoryPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminUpdateSelfHostedRunnerGroupForEnterprise"></a>
# **enterpriseAdminUpdateSelfHostedRunnerGroupForEnterprise**
> RunnerGroupsEnterprise enterpriseAdminUpdateSelfHostedRunnerGroupForEnterprise(enterprise, runnerGroupId, enterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest)

Update a self-hosted runner group for an enterprise

Updates the &#x60;name&#x60; and &#x60;visibility&#x60; of a self-hosted runner group in an enterprise.  You must authenticate using an access token with the &#x60;manage_runners:enterprise&#x60; scope to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    Integer runnerGroupId = 56; // Integer | Unique identifier of the self-hosted runner group.
    EnterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest enterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest = new EnterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest(); // EnterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest | 
    try {
      RunnerGroupsEnterprise result = apiInstance.enterpriseAdminUpdateSelfHostedRunnerGroupForEnterprise(enterprise, runnerGroupId, enterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminUpdateSelfHostedRunnerGroupForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **runnerGroupId** | **Integer**| Unique identifier of the self-hosted runner group. | |
| **enterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest** | [**EnterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest**](EnterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest.md)|  | [optional] |

### Return type

[**RunnerGroupsEnterprise**](RunnerGroupsEnterprise.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="enterpriseAdminUpdateUsernameForUser"></a>
# **enterpriseAdminUpdateUsernameForUser**
> EnterpriseAdminUpdateOrgName202Response enterpriseAdminUpdateUsernameForUser(username, enterpriseAdminUpdateUsernameForUserRequest)

Update the username for a user



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String username = "username_example"; // String | The handle for the GitHub user account.
    EnterpriseAdminUpdateUsernameForUserRequest enterpriseAdminUpdateUsernameForUserRequest = new EnterpriseAdminUpdateUsernameForUserRequest(); // EnterpriseAdminUpdateUsernameForUserRequest | 
    try {
      EnterpriseAdminUpdateOrgName202Response result = apiInstance.enterpriseAdminUpdateUsernameForUser(username, enterpriseAdminUpdateUsernameForUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminUpdateUsernameForUser");
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
| **username** | **String**| The handle for the GitHub user account. | |
| **enterpriseAdminUpdateUsernameForUserRequest** | [**EnterpriseAdminUpdateUsernameForUserRequest**](EnterpriseAdminUpdateUsernameForUserRequest.md)|  | |

### Return type

[**EnterpriseAdminUpdateOrgName202Response**](EnterpriseAdminUpdateOrgName202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Response |  -  |

<a id="enterpriseAdminUpgradeLicense"></a>
# **enterpriseAdminUpgradeLicense**
> enterpriseAdminUpgradeLicense(license)

Upgrade a license

This API upgrades your license and also triggers the configuration process.  **Note:** The request body for this operation must be submitted as &#x60;multipart/form-data&#x60; data. You can can reference the license file by prefixing the filename with the &#x60;@&#x60; symbol using &#x60;curl&#x60;. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#-F).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    EnterpriseAdminApi apiInstance = new EnterpriseAdminApi(defaultClient);
    String license = "license_example"; // String | The content of your new _.ghl_ license file.
    try {
      apiInstance.enterpriseAdminUpgradeLicense(license);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseAdminApi#enterpriseAdminUpgradeLicense");
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
| **license** | **String**| The content of your new _.ghl_ license file. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Response |  -  |

