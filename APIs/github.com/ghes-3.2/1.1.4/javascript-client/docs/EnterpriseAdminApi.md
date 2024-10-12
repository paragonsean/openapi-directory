# GitHubV3RestApi.EnterpriseAdminApi

All URIs are relative to *https://github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterpriseAdminAddAuthorizedSshKey**](EnterpriseAdminApi.md#enterpriseAdminAddAuthorizedSshKey) | **POST** /setup/api/settings/authorized-keys | Add an authorized SSH key
[**enterpriseAdminAddOrgAccessToSelfHostedRunnerGroupInEnterprise**](EnterpriseAdminApi.md#enterpriseAdminAddOrgAccessToSelfHostedRunnerGroupInEnterprise) | **PUT** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id} | Add organization access to a self-hosted runner group in an enterprise
[**enterpriseAdminAddSelfHostedRunnerToGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminAddSelfHostedRunnerToGroupForEnterprise) | **PUT** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | Add a self-hosted runner to a group for an enterprise
[**enterpriseAdminCreateEnterpriseServerLicense**](EnterpriseAdminApi.md#enterpriseAdminCreateEnterpriseServerLicense) | **POST** /setup/api/start | Create a GitHub license
[**enterpriseAdminCreateGlobalWebhook**](EnterpriseAdminApi.md#enterpriseAdminCreateGlobalWebhook) | **POST** /admin/hooks | Create a global webhook
[**enterpriseAdminCreateImpersonationOAuthToken**](EnterpriseAdminApi.md#enterpriseAdminCreateImpersonationOAuthToken) | **POST** /admin/users/{username}/authorizations | Create an impersonation OAuth token
[**enterpriseAdminCreateOrg**](EnterpriseAdminApi.md#enterpriseAdminCreateOrg) | **POST** /admin/organizations | Create an organization
[**enterpriseAdminCreatePreReceiveEnvironment**](EnterpriseAdminApi.md#enterpriseAdminCreatePreReceiveEnvironment) | **POST** /admin/pre-receive-environments | Create a pre-receive environment
[**enterpriseAdminCreatePreReceiveHook**](EnterpriseAdminApi.md#enterpriseAdminCreatePreReceiveHook) | **POST** /admin/pre-receive-hooks | Create a pre-receive hook
[**enterpriseAdminCreateRegistrationTokenForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminCreateRegistrationTokenForEnterprise) | **POST** /enterprises/{enterprise}/actions/runners/registration-token | Create a registration token for an enterprise
[**enterpriseAdminCreateRemoveTokenForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminCreateRemoveTokenForEnterprise) | **POST** /enterprises/{enterprise}/actions/runners/remove-token | Create a remove token for an enterprise
[**enterpriseAdminCreateSelfHostedRunnerGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminCreateSelfHostedRunnerGroupForEnterprise) | **POST** /enterprises/{enterprise}/actions/runner-groups | Create a self-hosted runner group for an enterprise
[**enterpriseAdminCreateUser**](EnterpriseAdminApi.md#enterpriseAdminCreateUser) | **POST** /admin/users | Create a user
[**enterpriseAdminDeleteGlobalWebhook**](EnterpriseAdminApi.md#enterpriseAdminDeleteGlobalWebhook) | **DELETE** /admin/hooks/{hook_id} | Delete a global webhook
[**enterpriseAdminDeleteImpersonationOAuthToken**](EnterpriseAdminApi.md#enterpriseAdminDeleteImpersonationOAuthToken) | **DELETE** /admin/users/{username}/authorizations | Delete an impersonation OAuth token
[**enterpriseAdminDeletePersonalAccessToken**](EnterpriseAdminApi.md#enterpriseAdminDeletePersonalAccessToken) | **DELETE** /admin/tokens/{token_id} | Delete a personal access token
[**enterpriseAdminDeletePreReceiveEnvironment**](EnterpriseAdminApi.md#enterpriseAdminDeletePreReceiveEnvironment) | **DELETE** /admin/pre-receive-environments/{pre_receive_environment_id} | Delete a pre-receive environment
[**enterpriseAdminDeletePreReceiveHook**](EnterpriseAdminApi.md#enterpriseAdminDeletePreReceiveHook) | **DELETE** /admin/pre-receive-hooks/{pre_receive_hook_id} | Delete a pre-receive hook
[**enterpriseAdminDeletePublicKey**](EnterpriseAdminApi.md#enterpriseAdminDeletePublicKey) | **DELETE** /admin/keys/{key_ids} | Delete a public key
[**enterpriseAdminDeleteSelfHostedRunnerFromEnterprise**](EnterpriseAdminApi.md#enterpriseAdminDeleteSelfHostedRunnerFromEnterprise) | **DELETE** /enterprises/{enterprise}/actions/runners/{runner_id} | Delete a self-hosted runner from an enterprise
[**enterpriseAdminDeleteSelfHostedRunnerGroupFromEnterprise**](EnterpriseAdminApi.md#enterpriseAdminDeleteSelfHostedRunnerGroupFromEnterprise) | **DELETE** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id} | Delete a self-hosted runner group from an enterprise
[**enterpriseAdminDeleteUser**](EnterpriseAdminApi.md#enterpriseAdminDeleteUser) | **DELETE** /admin/users/{username} | Delete a user
[**enterpriseAdminDemoteSiteAdministrator**](EnterpriseAdminApi.md#enterpriseAdminDemoteSiteAdministrator) | **DELETE** /users/{username}/site_admin | Demote a site administrator
[**enterpriseAdminDisableSelectedOrganizationGithubActionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminDisableSelectedOrganizationGithubActionsEnterprise) | **DELETE** /enterprises/{enterprise}/actions/permissions/organizations/{org_id} | Disable a selected organization for GitHub Actions in an enterprise
[**enterpriseAdminEnableOrDisableMaintenanceMode**](EnterpriseAdminApi.md#enterpriseAdminEnableOrDisableMaintenanceMode) | **POST** /setup/api/maintenance | Enable or disable maintenance mode
[**enterpriseAdminEnableSelectedOrganizationGithubActionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminEnableSelectedOrganizationGithubActionsEnterprise) | **PUT** /enterprises/{enterprise}/actions/permissions/organizations/{org_id} | Enable a selected organization for GitHub Actions in an enterprise
[**enterpriseAdminGetAllAuthorizedSshKeys**](EnterpriseAdminApi.md#enterpriseAdminGetAllAuthorizedSshKeys) | **GET** /setup/api/settings/authorized-keys | Get all authorized SSH keys
[**enterpriseAdminGetAllStats**](EnterpriseAdminApi.md#enterpriseAdminGetAllStats) | **GET** /enterprise/stats/all | Get all statistics
[**enterpriseAdminGetAllowedActionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminGetAllowedActionsEnterprise) | **GET** /enterprises/{enterprise}/actions/permissions/selected-actions | Get allowed actions for an enterprise
[**enterpriseAdminGetAnnouncement**](EnterpriseAdminApi.md#enterpriseAdminGetAnnouncement) | **GET** /enterprise/announcement | Get the global announcement banner
[**enterpriseAdminGetCommentStats**](EnterpriseAdminApi.md#enterpriseAdminGetCommentStats) | **GET** /enterprise/stats/comments | Get comment statistics
[**enterpriseAdminGetConfigurationStatus**](EnterpriseAdminApi.md#enterpriseAdminGetConfigurationStatus) | **GET** /setup/api/configcheck | Get the configuration status
[**enterpriseAdminGetDownloadStatusForPreReceiveEnvironment**](EnterpriseAdminApi.md#enterpriseAdminGetDownloadStatusForPreReceiveEnvironment) | **GET** /admin/pre-receive-environments/{pre_receive_environment_id}/downloads/latest | Get the download status for a pre-receive environment
[**enterpriseAdminGetGistStats**](EnterpriseAdminApi.md#enterpriseAdminGetGistStats) | **GET** /enterprise/stats/gists | Get gist statistics
[**enterpriseAdminGetGithubActionsPermissionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminGetGithubActionsPermissionsEnterprise) | **GET** /enterprises/{enterprise}/actions/permissions | Get GitHub Actions permissions for an enterprise
[**enterpriseAdminGetGlobalWebhook**](EnterpriseAdminApi.md#enterpriseAdminGetGlobalWebhook) | **GET** /admin/hooks/{hook_id} | Get a global webhook
[**enterpriseAdminGetHooksStats**](EnterpriseAdminApi.md#enterpriseAdminGetHooksStats) | **GET** /enterprise/stats/hooks | Get hooks statistics
[**enterpriseAdminGetIssueStats**](EnterpriseAdminApi.md#enterpriseAdminGetIssueStats) | **GET** /enterprise/stats/issues | Get issue statistics
[**enterpriseAdminGetLicenseInformation**](EnterpriseAdminApi.md#enterpriseAdminGetLicenseInformation) | **GET** /enterprise/settings/license | Get license information
[**enterpriseAdminGetMaintenanceStatus**](EnterpriseAdminApi.md#enterpriseAdminGetMaintenanceStatus) | **GET** /setup/api/maintenance | Get the maintenance status
[**enterpriseAdminGetMilestoneStats**](EnterpriseAdminApi.md#enterpriseAdminGetMilestoneStats) | **GET** /enterprise/stats/milestones | Get milestone statistics
[**enterpriseAdminGetOrgStats**](EnterpriseAdminApi.md#enterpriseAdminGetOrgStats) | **GET** /enterprise/stats/orgs | Get organization statistics
[**enterpriseAdminGetPagesStats**](EnterpriseAdminApi.md#enterpriseAdminGetPagesStats) | **GET** /enterprise/stats/pages | Get pages statistics
[**enterpriseAdminGetPreReceiveEnvironment**](EnterpriseAdminApi.md#enterpriseAdminGetPreReceiveEnvironment) | **GET** /admin/pre-receive-environments/{pre_receive_environment_id} | Get a pre-receive environment
[**enterpriseAdminGetPreReceiveHook**](EnterpriseAdminApi.md#enterpriseAdminGetPreReceiveHook) | **GET** /admin/pre-receive-hooks/{pre_receive_hook_id} | Get a pre-receive hook
[**enterpriseAdminGetPreReceiveHookForOrg**](EnterpriseAdminApi.md#enterpriseAdminGetPreReceiveHookForOrg) | **GET** /orgs/{org}/pre-receive-hooks/{pre_receive_hook_id} | Get a pre-receive hook for an organization
[**enterpriseAdminGetPreReceiveHookForRepo**](EnterpriseAdminApi.md#enterpriseAdminGetPreReceiveHookForRepo) | **GET** /repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id} | Get a pre-receive hook for a repository
[**enterpriseAdminGetPullRequestStats**](EnterpriseAdminApi.md#enterpriseAdminGetPullRequestStats) | **GET** /enterprise/stats/pulls | Get pull request statistics
[**enterpriseAdminGetRepoStats**](EnterpriseAdminApi.md#enterpriseAdminGetRepoStats) | **GET** /enterprise/stats/repos | Get repository statistics
[**enterpriseAdminGetSelfHostedRunnerForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminGetSelfHostedRunnerForEnterprise) | **GET** /enterprises/{enterprise}/actions/runners/{runner_id} | Get a self-hosted runner for an enterprise
[**enterpriseAdminGetSelfHostedRunnerGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminGetSelfHostedRunnerGroupForEnterprise) | **GET** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id} | Get a self-hosted runner group for an enterprise
[**enterpriseAdminGetSettings**](EnterpriseAdminApi.md#enterpriseAdminGetSettings) | **GET** /setup/api/settings | Get settings
[**enterpriseAdminGetUserStats**](EnterpriseAdminApi.md#enterpriseAdminGetUserStats) | **GET** /enterprise/stats/users | Get users statistics
[**enterpriseAdminListGlobalWebhooks**](EnterpriseAdminApi.md#enterpriseAdminListGlobalWebhooks) | **GET** /admin/hooks | List global webhooks
[**enterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise**](EnterpriseAdminApi.md#enterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise) | **GET** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations | List organization access to a self-hosted runner group in an enterprise
[**enterpriseAdminListPersonalAccessTokens**](EnterpriseAdminApi.md#enterpriseAdminListPersonalAccessTokens) | **GET** /admin/tokens | List personal access tokens
[**enterpriseAdminListPreReceiveEnvironments**](EnterpriseAdminApi.md#enterpriseAdminListPreReceiveEnvironments) | **GET** /admin/pre-receive-environments | List pre-receive environments
[**enterpriseAdminListPreReceiveHooks**](EnterpriseAdminApi.md#enterpriseAdminListPreReceiveHooks) | **GET** /admin/pre-receive-hooks | List pre-receive hooks
[**enterpriseAdminListPreReceiveHooksForOrg**](EnterpriseAdminApi.md#enterpriseAdminListPreReceiveHooksForOrg) | **GET** /orgs/{org}/pre-receive-hooks | List pre-receive hooks for an organization
[**enterpriseAdminListPreReceiveHooksForRepo**](EnterpriseAdminApi.md#enterpriseAdminListPreReceiveHooksForRepo) | **GET** /repos/{owner}/{repo}/pre-receive-hooks | List pre-receive hooks for a repository
[**enterpriseAdminListPublicKeys**](EnterpriseAdminApi.md#enterpriseAdminListPublicKeys) | **GET** /admin/keys | List public keys
[**enterpriseAdminListRunnerApplicationsForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminListRunnerApplicationsForEnterprise) | **GET** /enterprises/{enterprise}/actions/runners/downloads | List runner applications for an enterprise
[**enterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise) | **GET** /enterprises/{enterprise}/actions/permissions/organizations | List selected organizations enabled for GitHub Actions in an enterprise
[**enterpriseAdminListSelfHostedRunnerGroupsForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminListSelfHostedRunnerGroupsForEnterprise) | **GET** /enterprises/{enterprise}/actions/runner-groups | List self-hosted runner groups for an enterprise
[**enterpriseAdminListSelfHostedRunnersForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminListSelfHostedRunnersForEnterprise) | **GET** /enterprises/{enterprise}/actions/runners | List self-hosted runners for an enterprise
[**enterpriseAdminListSelfHostedRunnersInGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminListSelfHostedRunnersInGroupForEnterprise) | **GET** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners | List self-hosted runners in a group for an enterprise
[**enterpriseAdminPingGlobalWebhook**](EnterpriseAdminApi.md#enterpriseAdminPingGlobalWebhook) | **POST** /admin/hooks/{hook_id}/pings | Ping a global webhook
[**enterpriseAdminPromoteUserToBeSiteAdministrator**](EnterpriseAdminApi.md#enterpriseAdminPromoteUserToBeSiteAdministrator) | **PUT** /users/{username}/site_admin | Promote a user to be a site administrator
[**enterpriseAdminRemoveAnnouncement**](EnterpriseAdminApi.md#enterpriseAdminRemoveAnnouncement) | **DELETE** /enterprise/announcement | Remove the global announcement banner
[**enterpriseAdminRemoveAuthorizedSshKey**](EnterpriseAdminApi.md#enterpriseAdminRemoveAuthorizedSshKey) | **DELETE** /setup/api/settings/authorized-keys | Remove an authorized SSH key
[**enterpriseAdminRemoveOrgAccessToSelfHostedRunnerGroupInEnterprise**](EnterpriseAdminApi.md#enterpriseAdminRemoveOrgAccessToSelfHostedRunnerGroupInEnterprise) | **DELETE** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id} | Remove organization access to a self-hosted runner group in an enterprise
[**enterpriseAdminRemovePreReceiveHookEnforcementForOrg**](EnterpriseAdminApi.md#enterpriseAdminRemovePreReceiveHookEnforcementForOrg) | **DELETE** /orgs/{org}/pre-receive-hooks/{pre_receive_hook_id} | Remove pre-receive hook enforcement for an organization
[**enterpriseAdminRemovePreReceiveHookEnforcementForRepo**](EnterpriseAdminApi.md#enterpriseAdminRemovePreReceiveHookEnforcementForRepo) | **DELETE** /repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id} | Remove pre-receive hook enforcement for a repository
[**enterpriseAdminRemoveSelfHostedRunnerFromGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminRemoveSelfHostedRunnerFromGroupForEnterprise) | **DELETE** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | Remove a self-hosted runner from a group for an enterprise
[**enterpriseAdminSetAllowedActionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminSetAllowedActionsEnterprise) | **PUT** /enterprises/{enterprise}/actions/permissions/selected-actions | Set allowed actions for an enterprise
[**enterpriseAdminSetAnnouncement**](EnterpriseAdminApi.md#enterpriseAdminSetAnnouncement) | **PATCH** /enterprise/announcement | Set the global announcement banner
[**enterpriseAdminSetGithubActionsPermissionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminSetGithubActionsPermissionsEnterprise) | **PUT** /enterprises/{enterprise}/actions/permissions | Set GitHub Actions permissions for an enterprise
[**enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterprise**](EnterpriseAdminApi.md#enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterprise) | **PUT** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations | Set organization access for a self-hosted runner group in an enterprise
[**enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterprise**](EnterpriseAdminApi.md#enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterprise) | **PUT** /enterprises/{enterprise}/actions/permissions/organizations | Set selected organizations enabled for GitHub Actions in an enterprise
[**enterpriseAdminSetSelfHostedRunnersInGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminSetSelfHostedRunnersInGroupForEnterprise) | **PUT** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners | Set self-hosted runners in a group for an enterprise
[**enterpriseAdminSetSettings**](EnterpriseAdminApi.md#enterpriseAdminSetSettings) | **PUT** /setup/api/settings | Set settings
[**enterpriseAdminStartConfigurationProcess**](EnterpriseAdminApi.md#enterpriseAdminStartConfigurationProcess) | **POST** /setup/api/configure | Start a configuration process
[**enterpriseAdminStartPreReceiveEnvironmentDownload**](EnterpriseAdminApi.md#enterpriseAdminStartPreReceiveEnvironmentDownload) | **POST** /admin/pre-receive-environments/{pre_receive_environment_id}/downloads | Start a pre-receive environment download
[**enterpriseAdminSuspendUser**](EnterpriseAdminApi.md#enterpriseAdminSuspendUser) | **PUT** /users/{username}/suspended | Suspend a user
[**enterpriseAdminSyncLdapMappingForTeam**](EnterpriseAdminApi.md#enterpriseAdminSyncLdapMappingForTeam) | **POST** /admin/ldap/teams/{team_id}/sync | Sync LDAP mapping for a team
[**enterpriseAdminSyncLdapMappingForUser**](EnterpriseAdminApi.md#enterpriseAdminSyncLdapMappingForUser) | **POST** /admin/ldap/users/{username}/sync | Sync LDAP mapping for a user
[**enterpriseAdminUnsuspendUser**](EnterpriseAdminApi.md#enterpriseAdminUnsuspendUser) | **DELETE** /users/{username}/suspended | Unsuspend a user
[**enterpriseAdminUpdateGlobalWebhook**](EnterpriseAdminApi.md#enterpriseAdminUpdateGlobalWebhook) | **PATCH** /admin/hooks/{hook_id} | Update a global webhook
[**enterpriseAdminUpdateLdapMappingForTeam**](EnterpriseAdminApi.md#enterpriseAdminUpdateLdapMappingForTeam) | **PATCH** /admin/ldap/teams/{team_id}/mapping | Update LDAP mapping for a team
[**enterpriseAdminUpdateLdapMappingForUser**](EnterpriseAdminApi.md#enterpriseAdminUpdateLdapMappingForUser) | **PATCH** /admin/ldap/users/{username}/mapping | Update LDAP mapping for a user
[**enterpriseAdminUpdateOrgName**](EnterpriseAdminApi.md#enterpriseAdminUpdateOrgName) | **PATCH** /admin/organizations/{org} | Update an organization name
[**enterpriseAdminUpdatePreReceiveEnvironment**](EnterpriseAdminApi.md#enterpriseAdminUpdatePreReceiveEnvironment) | **PATCH** /admin/pre-receive-environments/{pre_receive_environment_id} | Update a pre-receive environment
[**enterpriseAdminUpdatePreReceiveHook**](EnterpriseAdminApi.md#enterpriseAdminUpdatePreReceiveHook) | **PATCH** /admin/pre-receive-hooks/{pre_receive_hook_id} | Update a pre-receive hook
[**enterpriseAdminUpdatePreReceiveHookEnforcementForOrg**](EnterpriseAdminApi.md#enterpriseAdminUpdatePreReceiveHookEnforcementForOrg) | **PATCH** /orgs/{org}/pre-receive-hooks/{pre_receive_hook_id} | Update pre-receive hook enforcement for an organization
[**enterpriseAdminUpdatePreReceiveHookEnforcementForRepo**](EnterpriseAdminApi.md#enterpriseAdminUpdatePreReceiveHookEnforcementForRepo) | **PATCH** /repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id} | Update pre-receive hook enforcement for a repository
[**enterpriseAdminUpdateSelfHostedRunnerGroupForEnterprise**](EnterpriseAdminApi.md#enterpriseAdminUpdateSelfHostedRunnerGroupForEnterprise) | **PATCH** /enterprises/{enterprise}/actions/runner-groups/{runner_group_id} | Update a self-hosted runner group for an enterprise
[**enterpriseAdminUpdateUsernameForUser**](EnterpriseAdminApi.md#enterpriseAdminUpdateUsernameForUser) | **PATCH** /admin/users/{username} | Update the username for a user
[**enterpriseAdminUpgradeLicense**](EnterpriseAdminApi.md#enterpriseAdminUpgradeLicense) | **POST** /setup/api/upgrade | Upgrade a license



## enterpriseAdminAddAuthorizedSshKey

> [SshKey] enterpriseAdminAddAuthorizedSshKey(authorizedKey)

Add an authorized SSH key

**Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let authorizedKey = "authorizedKey_example"; // String | The public SSH key.
apiInstance.enterpriseAdminAddAuthorizedSshKey(authorizedKey, (error, data, response) => {
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
 **authorizedKey** | **String**| The public SSH key. | 

### Return type

[**[SshKey]**](SshKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## enterpriseAdminAddOrgAccessToSelfHostedRunnerGroupInEnterprise

> enterpriseAdminAddOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, orgId)

Add organization access to a self-hosted runner group in an enterprise

Adds an organization to the list of selected organizations that can access a self-hosted runner group. The runner group must have &#x60;visibility&#x60; set to &#x60;selected&#x60;. For more information, see \&quot;[Create a self-hosted runner group for an enterprise](#create-a-self-hosted-runner-group-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let runnerGroupId = 56; // Number | Unique identifier of the self-hosted runner group.
let orgId = 56; // Number | The unique identifier of the organization.
apiInstance.enterpriseAdminAddOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, orgId, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **runnerGroupId** | **Number**| Unique identifier of the self-hosted runner group. | 
 **orgId** | **Number**| The unique identifier of the organization. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminAddSelfHostedRunnerToGroupForEnterprise

> enterpriseAdminAddSelfHostedRunnerToGroupForEnterprise(enterprise, runnerGroupId, runnerId)

Add a self-hosted runner to a group for an enterprise

Adds a self-hosted runner to a runner group configured in an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let runnerGroupId = 56; // Number | Unique identifier of the self-hosted runner group.
let runnerId = 56; // Number | Unique identifier of the self-hosted runner.
apiInstance.enterpriseAdminAddSelfHostedRunnerToGroupForEnterprise(enterprise, runnerGroupId, runnerId, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **runnerGroupId** | **Number**| Unique identifier of the self-hosted runner group. | 
 **runnerId** | **Number**| Unique identifier of the self-hosted runner. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminCreateEnterpriseServerLicense

> enterpriseAdminCreateEnterpriseServerLicense(license, opts)

Create a GitHub license

When you boot a GitHub instance for the first time, you can use the following endpoint to upload a license.  Note that you need to &#x60;POST&#x60; to [&#x60;/setup/api/configure&#x60;](https://docs.github.com/enterprise-server@3.2/rest/reference/enterprise-admin#start-a-configuration-process) to start the actual configuration process.  When using this endpoint, your GitHub instance must have a password set. This can be accomplished two ways:  1.  If you&#39;re working directly with the API before accessing the web interface, you must pass in the password parameter to set your password. 2.  If you set up your instance via the web interface before accessing the API, your calls to this endpoint do not need the password parameter.  **Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let license = "license_example"; // String | The content of your _.ghl_ license file.
let opts = {
  'password': "password_example", // String | You **must** provide a password _only if_ you are uploading your license for the first time. If you previously set a password through the web interface, you don't need this parameter.
  'settings': "settings_example" // String | An optional JSON string containing the installation settings. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@3.2/rest/reference/enterprise-admin#get-settings).
};
apiInstance.enterpriseAdminCreateEnterpriseServerLicense(license, opts, (error, data, response) => {
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
 **license** | **String**| The content of your _.ghl_ license file. | 
 **password** | **String**| You **must** provide a password _only if_ you are uploading your license for the first time. If you previously set a password through the web interface, you don&#39;t need this parameter. | [optional] 
 **settings** | **String**| An optional JSON string containing the installation settings. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@3.2/rest/reference/enterprise-admin#get-settings). | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## enterpriseAdminCreateGlobalWebhook

> GlobalHook enterpriseAdminCreateGlobalWebhook(accept, enterpriseAdminCreateGlobalWebhookRequest)

Create a global webhook



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let accept = "'application/vnd.github.superpro-preview+json'"; // String | This API is under preview and subject to change.
let enterpriseAdminCreateGlobalWebhookRequest = {"config":{"content_type":"json","secret":"secret","url":"https://example.com/webhook"},"events":["organization","user"],"name":"web"}; // EnterpriseAdminCreateGlobalWebhookRequest | 
apiInstance.enterpriseAdminCreateGlobalWebhook(accept, enterpriseAdminCreateGlobalWebhookRequest, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.superpro-preview+json&#39;]
 **enterpriseAdminCreateGlobalWebhookRequest** | [**EnterpriseAdminCreateGlobalWebhookRequest**](EnterpriseAdminCreateGlobalWebhookRequest.md)|  | 

### Return type

[**GlobalHook**](GlobalHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminCreateImpersonationOAuthToken

> Authorization enterpriseAdminCreateImpersonationOAuthToken(username, enterpriseAdminCreateImpersonationOAuthTokenRequest)

Create an impersonation OAuth token



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let enterpriseAdminCreateImpersonationOAuthTokenRequest = new GitHubV3RestApi.EnterpriseAdminCreateImpersonationOAuthTokenRequest(); // EnterpriseAdminCreateImpersonationOAuthTokenRequest | 
apiInstance.enterpriseAdminCreateImpersonationOAuthToken(username, enterpriseAdminCreateImpersonationOAuthTokenRequest, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **enterpriseAdminCreateImpersonationOAuthTokenRequest** | [**EnterpriseAdminCreateImpersonationOAuthTokenRequest**](EnterpriseAdminCreateImpersonationOAuthTokenRequest.md)|  | 

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminCreateOrg

> OrganizationSimple enterpriseAdminCreateOrg(enterpriseAdminCreateOrgRequest)

Create an organization



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterpriseAdminCreateOrgRequest = {"admin":"monalisaoctocat","login":"github","profile_name":"GitHub, Inc."}; // EnterpriseAdminCreateOrgRequest | 
apiInstance.enterpriseAdminCreateOrg(enterpriseAdminCreateOrgRequest, (error, data, response) => {
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
 **enterpriseAdminCreateOrgRequest** | [**EnterpriseAdminCreateOrgRequest**](EnterpriseAdminCreateOrgRequest.md)|  | 

### Return type

[**OrganizationSimple**](OrganizationSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminCreatePreReceiveEnvironment

> PreReceiveEnvironment enterpriseAdminCreatePreReceiveEnvironment(enterpriseAdminCreatePreReceiveEnvironmentRequest)

Create a pre-receive environment



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterpriseAdminCreatePreReceiveEnvironmentRequest = {"image_url":"https://my_file_server/path/to/devtools_env.tar.gz","name":"DevTools Hook Env"}; // EnterpriseAdminCreatePreReceiveEnvironmentRequest | 
apiInstance.enterpriseAdminCreatePreReceiveEnvironment(enterpriseAdminCreatePreReceiveEnvironmentRequest, (error, data, response) => {
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
 **enterpriseAdminCreatePreReceiveEnvironmentRequest** | [**EnterpriseAdminCreatePreReceiveEnvironmentRequest**](EnterpriseAdminCreatePreReceiveEnvironmentRequest.md)|  | 

### Return type

[**PreReceiveEnvironment**](PreReceiveEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminCreatePreReceiveHook

> PreReceiveHook enterpriseAdminCreatePreReceiveHook(enterpriseAdminCreatePreReceiveHookRequest)

Create a pre-receive hook



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterpriseAdminCreatePreReceiveHookRequest = {"allow_downstream_configuration":false,"enforcement":"disabled","environment":{"id":2},"name":"Check Commits","script":"scripts/commit_check.sh","script_repository":{"full_name":"DevIT/hooks"}}; // EnterpriseAdminCreatePreReceiveHookRequest | 
apiInstance.enterpriseAdminCreatePreReceiveHook(enterpriseAdminCreatePreReceiveHookRequest, (error, data, response) => {
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
 **enterpriseAdminCreatePreReceiveHookRequest** | [**EnterpriseAdminCreatePreReceiveHookRequest**](EnterpriseAdminCreatePreReceiveHookRequest.md)|  | 

### Return type

[**PreReceiveHook**](PreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminCreateRegistrationTokenForEnterprise

> AuthenticationToken enterpriseAdminCreateRegistrationTokenForEnterprise(enterprise)

Create a registration token for an enterprise

Returns a token that you can pass to the &#x60;config&#x60; script. The token expires after one hour.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.  #### Example using registration token  Configure your self-hosted runner, replacing &#x60;TOKEN&#x60; with the registration token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh --url https://github.com/enterprises/octo-enterprise --token TOKEN &#x60;&#x60;&#x60;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
apiInstance.enterpriseAdminCreateRegistrationTokenForEnterprise(enterprise, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 

### Return type

[**AuthenticationToken**](AuthenticationToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminCreateRemoveTokenForEnterprise

> AuthenticationToken enterpriseAdminCreateRemoveTokenForEnterprise(enterprise)

Create a remove token for an enterprise

Returns a token that you can pass to the &#x60;config&#x60; script to remove a self-hosted runner from an enterprise. The token expires after one hour.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.  #### Example using remove token  To remove your self-hosted runner from an enterprise, replace &#x60;TOKEN&#x60; with the remove token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh remove --token TOKEN &#x60;&#x60;&#x60;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
apiInstance.enterpriseAdminCreateRemoveTokenForEnterprise(enterprise, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 

### Return type

[**AuthenticationToken**](AuthenticationToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminCreateSelfHostedRunnerGroupForEnterprise

> RunnerGroupsEnterprise enterpriseAdminCreateSelfHostedRunnerGroupForEnterprise(enterprise, enterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest)

Create a self-hosted runner group for an enterprise

Creates a new self-hosted runner group for an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let enterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest = {"name":"Expensive hardware runners","runners":[9,2],"selected_organization_ids":[32,91],"visibility":"selected"}; // EnterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest | 
apiInstance.enterpriseAdminCreateSelfHostedRunnerGroupForEnterprise(enterprise, enterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **enterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest** | [**EnterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest**](EnterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest.md)|  | 

### Return type

[**RunnerGroupsEnterprise**](RunnerGroupsEnterprise.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminCreateUser

> SimpleUser enterpriseAdminCreateUser(enterpriseAdminCreateUserRequest)

Create a user

If an external authentication mechanism is used, the login name should match the login name in the external system. If you are using LDAP authentication, you should also [update the LDAP mapping](https://docs.github.com/enterprise-server@3.2/rest/reference/enterprise-admin#update-ldap-mapping-for-a-user) for the user.  The login name will be normalized to only contain alphanumeric characters or single hyphens. For example, if you send &#x60;\&quot;octo_cat\&quot;&#x60; as the login, a user named &#x60;\&quot;octo-cat\&quot;&#x60; will be created.  If the login name or email address is already associated with an account, the server will return a &#x60;422&#x60; response.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterpriseAdminCreateUserRequest = {"email":"octocat@github.com","login":"monalisa"}; // EnterpriseAdminCreateUserRequest | 
apiInstance.enterpriseAdminCreateUser(enterpriseAdminCreateUserRequest, (error, data, response) => {
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
 **enterpriseAdminCreateUserRequest** | [**EnterpriseAdminCreateUserRequest**](EnterpriseAdminCreateUserRequest.md)|  | 

### Return type

[**SimpleUser**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminDeleteGlobalWebhook

> enterpriseAdminDeleteGlobalWebhook(hookId)

Delete a global webhook



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let hookId = 56; // Number | The unique identifier of the hook.
apiInstance.enterpriseAdminDeleteGlobalWebhook(hookId, (error, data, response) => {
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
 **hookId** | **Number**| The unique identifier of the hook. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminDeleteImpersonationOAuthToken

> enterpriseAdminDeleteImpersonationOAuthToken(username)

Delete an impersonation OAuth token



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.enterpriseAdminDeleteImpersonationOAuthToken(username, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminDeletePersonalAccessToken

> enterpriseAdminDeletePersonalAccessToken(tokenId)

Delete a personal access token

Deletes a personal access token. Returns a &#x60;403 - Forbidden&#x60; status when a personal access token is in use. For example, if you access this endpoint with the same personal access token that you are trying to delete, you will receive this error.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let tokenId = 56; // Number | The unique identifier of the token.
apiInstance.enterpriseAdminDeletePersonalAccessToken(tokenId, (error, data, response) => {
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
 **tokenId** | **Number**| The unique identifier of the token. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminDeletePreReceiveEnvironment

> enterpriseAdminDeletePreReceiveEnvironment(preReceiveEnvironmentId)

Delete a pre-receive environment

If you attempt to delete an environment that cannot be deleted, you will receive a &#x60;422 Unprocessable Entity&#x60; response.  The possible error messages are:  *   _Cannot modify or delete the default environment_ *   _Cannot delete environment that has hooks_ *   _Cannot delete environment when download is in progress_

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let preReceiveEnvironmentId = 56; // Number | The unique identifier of the pre-receive environment.
apiInstance.enterpriseAdminDeletePreReceiveEnvironment(preReceiveEnvironmentId, (error, data, response) => {
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
 **preReceiveEnvironmentId** | **Number**| The unique identifier of the pre-receive environment. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminDeletePreReceiveHook

> enterpriseAdminDeletePreReceiveHook(preReceiveHookId)

Delete a pre-receive hook



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let preReceiveHookId = 56; // Number | The unique identifier of the pre-receive hook.
apiInstance.enterpriseAdminDeletePreReceiveHook(preReceiveHookId, (error, data, response) => {
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
 **preReceiveHookId** | **Number**| The unique identifier of the pre-receive hook. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminDeletePublicKey

> enterpriseAdminDeletePublicKey(keyIds)

Delete a public key



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let keyIds = "keyIds_example"; // String | The unique identifier of the key.
apiInstance.enterpriseAdminDeletePublicKey(keyIds, (error, data, response) => {
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
 **keyIds** | **String**| The unique identifier of the key. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminDeleteSelfHostedRunnerFromEnterprise

> enterpriseAdminDeleteSelfHostedRunnerFromEnterprise(enterprise, runnerId)

Delete a self-hosted runner from an enterprise

Forces the removal of a self-hosted runner from an enterprise. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let runnerId = 56; // Number | Unique identifier of the self-hosted runner.
apiInstance.enterpriseAdminDeleteSelfHostedRunnerFromEnterprise(enterprise, runnerId, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **runnerId** | **Number**| Unique identifier of the self-hosted runner. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminDeleteSelfHostedRunnerGroupFromEnterprise

> enterpriseAdminDeleteSelfHostedRunnerGroupFromEnterprise(enterprise, runnerGroupId)

Delete a self-hosted runner group from an enterprise

Deletes a self-hosted runner group for an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let runnerGroupId = 56; // Number | Unique identifier of the self-hosted runner group.
apiInstance.enterpriseAdminDeleteSelfHostedRunnerGroupFromEnterprise(enterprise, runnerGroupId, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **runnerGroupId** | **Number**| Unique identifier of the self-hosted runner group. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminDeleteUser

> enterpriseAdminDeleteUser(username)

Delete a user

Deleting a user will delete all their repositories, gists, applications, and personal settings. [Suspending a user](https://docs.github.com/enterprise-server@3.2/rest/reference/enterprise-admin#suspend-a-user) is often a better option.  You can delete any user account except your own.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.enterpriseAdminDeleteUser(username, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminDemoteSiteAdministrator

> enterpriseAdminDemoteSiteAdministrator(username)

Demote a site administrator

You can demote any user account except your own.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.enterpriseAdminDemoteSiteAdministrator(username, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminDisableSelectedOrganizationGithubActionsEnterprise

> enterpriseAdminDisableSelectedOrganizationGithubActionsEnterprise(enterprise, orgId)

Disable a selected organization for GitHub Actions in an enterprise

Removes an organization from the list of selected organizations that are enabled for GitHub Actions in an enterprise. To use this endpoint, the enterprise permission policy for &#x60;enabled_organizations&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let orgId = 56; // Number | The unique identifier of the organization.
apiInstance.enterpriseAdminDisableSelectedOrganizationGithubActionsEnterprise(enterprise, orgId, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **orgId** | **Number**| The unique identifier of the organization. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminEnableOrDisableMaintenanceMode

> MaintenanceStatus enterpriseAdminEnableOrDisableMaintenanceMode(maintenance)

Enable or disable maintenance mode

**Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let maintenance = "maintenance_example"; // String | A JSON string with the attributes `enabled` and `when`.  The possible values for `enabled` are `true` and `false`. When it's `false`, the attribute `when` is ignored and the maintenance mode is turned off. `when` defines the time period when the maintenance was enabled.  The possible values for `when` are `now` or any date parseable by [mojombo/chronic](https://github.com/mojombo/chronic).
apiInstance.enterpriseAdminEnableOrDisableMaintenanceMode(maintenance, (error, data, response) => {
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
 **maintenance** | **String**| A JSON string with the attributes &#x60;enabled&#x60; and &#x60;when&#x60;.  The possible values for &#x60;enabled&#x60; are &#x60;true&#x60; and &#x60;false&#x60;. When it&#39;s &#x60;false&#x60;, the attribute &#x60;when&#x60; is ignored and the maintenance mode is turned off. &#x60;when&#x60; defines the time period when the maintenance was enabled.  The possible values for &#x60;when&#x60; are &#x60;now&#x60; or any date parseable by [mojombo/chronic](https://github.com/mojombo/chronic). | 

### Return type

[**MaintenanceStatus**](MaintenanceStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## enterpriseAdminEnableSelectedOrganizationGithubActionsEnterprise

> enterpriseAdminEnableSelectedOrganizationGithubActionsEnterprise(enterprise, orgId)

Enable a selected organization for GitHub Actions in an enterprise

Adds an organization to the list of selected organizations that are enabled for GitHub Actions in an enterprise. To use this endpoint, the enterprise permission policy for &#x60;enabled_organizations&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let orgId = 56; // Number | The unique identifier of the organization.
apiInstance.enterpriseAdminEnableSelectedOrganizationGithubActionsEnterprise(enterprise, orgId, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **orgId** | **Number**| The unique identifier of the organization. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminGetAllAuthorizedSshKeys

> [SshKey] enterpriseAdminGetAllAuthorizedSshKeys()

Get all authorized SSH keys



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetAllAuthorizedSshKeys((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[SshKey]**](SshKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminGetAllStats

> EnterpriseOverview enterpriseAdminGetAllStats()

Get all statistics



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetAllStats((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetAllowedActionsEnterprise

> SelectedActions enterpriseAdminGetAllowedActionsEnterprise(enterprise)

Get allowed actions for an enterprise

Gets the selected actions that are allowed in an enterprise. To use this endpoint, the enterprise permission policy for &#x60;allowed_actions&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
apiInstance.enterpriseAdminGetAllowedActionsEnterprise(enterprise, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 

### Return type

[**SelectedActions**](SelectedActions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminGetAnnouncement

> Announcement enterpriseAdminGetAnnouncement()

Get the global announcement banner

Gets the current message and expiration date of the global announcement banner in your enterprise.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetAnnouncement((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetCommentStats

> EnterpriseCommentOverview enterpriseAdminGetCommentStats()

Get comment statistics



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetCommentStats((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetConfigurationStatus

> ConfigurationStatus enterpriseAdminGetConfigurationStatus()

Get the configuration status

This endpoint allows you to check the status of the most recent configuration process:  Note that you may need to wait several seconds after you start a process before you can check its status.  The different statuses are:  | Status        | Description                       | | ------------- | --------------------------------- | | &#x60;PENDING&#x60;     | The job has not started yet       | | &#x60;CONFIGURING&#x60; | The job is running                | | &#x60;DONE&#x60;        | The job has finished correctly    | | &#x60;FAILED&#x60;      | The job has finished unexpectedly |

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetConfigurationStatus((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetDownloadStatusForPreReceiveEnvironment

> PreReceiveEnvironmentDownloadStatus enterpriseAdminGetDownloadStatusForPreReceiveEnvironment(preReceiveEnvironmentId)

Get the download status for a pre-receive environment

In addition to seeing the download status at the \&quot;[Get a pre-receive environment](#get-a-pre-receive-environment)\&quot; endpoint, there is also this separate endpoint for just the download status.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let preReceiveEnvironmentId = 56; // Number | The unique identifier of the pre-receive environment.
apiInstance.enterpriseAdminGetDownloadStatusForPreReceiveEnvironment(preReceiveEnvironmentId, (error, data, response) => {
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
 **preReceiveEnvironmentId** | **Number**| The unique identifier of the pre-receive environment. | 

### Return type

[**PreReceiveEnvironmentDownloadStatus**](PreReceiveEnvironmentDownloadStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminGetGistStats

> EnterpriseGistOverview enterpriseAdminGetGistStats()

Get gist statistics



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetGistStats((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetGithubActionsPermissionsEnterprise

> ActionsEnterprisePermissions enterpriseAdminGetGithubActionsPermissionsEnterprise(enterprise)

Get GitHub Actions permissions for an enterprise

Gets the GitHub Actions permissions policy for organizations and allowed actions in an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
apiInstance.enterpriseAdminGetGithubActionsPermissionsEnterprise(enterprise, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 

### Return type

[**ActionsEnterprisePermissions**](ActionsEnterprisePermissions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminGetGlobalWebhook

> GlobalHook enterpriseAdminGetGlobalWebhook(accept, hookId)

Get a global webhook



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let accept = "'application/vnd.github.superpro-preview+json'"; // String | This API is under preview and subject to change.
let hookId = 56; // Number | The unique identifier of the hook.
apiInstance.enterpriseAdminGetGlobalWebhook(accept, hookId, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.superpro-preview+json&#39;]
 **hookId** | **Number**| The unique identifier of the hook. | 

### Return type

[**GlobalHook**](GlobalHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminGetHooksStats

> EnterpriseHookOverview enterpriseAdminGetHooksStats()

Get hooks statistics

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetHooksStats((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetIssueStats

> EnterpriseIssueOverview enterpriseAdminGetIssueStats()

Get issue statistics



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetIssueStats((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetLicenseInformation

> LicenseInfo enterpriseAdminGetLicenseInformation()

Get license information



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetLicenseInformation((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetMaintenanceStatus

> MaintenanceStatus enterpriseAdminGetMaintenanceStatus()

Get the maintenance status

Check your installation&#39;s maintenance status:

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetMaintenanceStatus((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetMilestoneStats

> EnterpriseMilestoneOverview enterpriseAdminGetMilestoneStats()

Get milestone statistics



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetMilestoneStats((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetOrgStats

> EnterpriseOrganizationOverview enterpriseAdminGetOrgStats()

Get organization statistics



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetOrgStats((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetPagesStats

> EnterprisePageOverview enterpriseAdminGetPagesStats()

Get pages statistics



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetPagesStats((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetPreReceiveEnvironment

> PreReceiveEnvironment enterpriseAdminGetPreReceiveEnvironment(preReceiveEnvironmentId)

Get a pre-receive environment



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let preReceiveEnvironmentId = 56; // Number | The unique identifier of the pre-receive environment.
apiInstance.enterpriseAdminGetPreReceiveEnvironment(preReceiveEnvironmentId, (error, data, response) => {
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
 **preReceiveEnvironmentId** | **Number**| The unique identifier of the pre-receive environment. | 

### Return type

[**PreReceiveEnvironment**](PreReceiveEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminGetPreReceiveHook

> PreReceiveHook enterpriseAdminGetPreReceiveHook(preReceiveHookId)

Get a pre-receive hook



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let preReceiveHookId = 56; // Number | The unique identifier of the pre-receive hook.
apiInstance.enterpriseAdminGetPreReceiveHook(preReceiveHookId, (error, data, response) => {
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
 **preReceiveHookId** | **Number**| The unique identifier of the pre-receive hook. | 

### Return type

[**PreReceiveHook**](PreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminGetPreReceiveHookForOrg

> OrgPreReceiveHook enterpriseAdminGetPreReceiveHookForOrg(org, preReceiveHookId)

Get a pre-receive hook for an organization



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let preReceiveHookId = 56; // Number | The unique identifier of the pre-receive hook.
apiInstance.enterpriseAdminGetPreReceiveHookForOrg(org, preReceiveHookId, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **preReceiveHookId** | **Number**| The unique identifier of the pre-receive hook. | 

### Return type

[**OrgPreReceiveHook**](OrgPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminGetPreReceiveHookForRepo

> RepositoryPreReceiveHook enterpriseAdminGetPreReceiveHookForRepo(owner, repo, preReceiveHookId)

Get a pre-receive hook for a repository



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let preReceiveHookId = 56; // Number | The unique identifier of the pre-receive hook.
apiInstance.enterpriseAdminGetPreReceiveHookForRepo(owner, repo, preReceiveHookId, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **preReceiveHookId** | **Number**| The unique identifier of the pre-receive hook. | 

### Return type

[**RepositoryPreReceiveHook**](RepositoryPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminGetPullRequestStats

> EnterprisePullRequestOverview enterpriseAdminGetPullRequestStats()

Get pull request statistics



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetPullRequestStats((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetRepoStats

> EnterpriseRepositoryOverview enterpriseAdminGetRepoStats()

Get repository statistics

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetRepoStats((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetSelfHostedRunnerForEnterprise

> Runner enterpriseAdminGetSelfHostedRunnerForEnterprise(enterprise, runnerId)

Get a self-hosted runner for an enterprise

Gets a specific self-hosted runner configured in an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let runnerId = 56; // Number | Unique identifier of the self-hosted runner.
apiInstance.enterpriseAdminGetSelfHostedRunnerForEnterprise(enterprise, runnerId, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **runnerId** | **Number**| Unique identifier of the self-hosted runner. | 

### Return type

[**Runner**](Runner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminGetSelfHostedRunnerGroupForEnterprise

> RunnerGroupsEnterprise enterpriseAdminGetSelfHostedRunnerGroupForEnterprise(enterprise, runnerGroupId)

Get a self-hosted runner group for an enterprise

Gets a specific self-hosted runner group for an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let runnerGroupId = 56; // Number | Unique identifier of the self-hosted runner group.
apiInstance.enterpriseAdminGetSelfHostedRunnerGroupForEnterprise(enterprise, runnerGroupId, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **runnerGroupId** | **Number**| Unique identifier of the self-hosted runner group. | 

### Return type

[**RunnerGroupsEnterprise**](RunnerGroupsEnterprise.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminGetSettings

> EnterpriseSettings enterpriseAdminGetSettings()

Get settings

Gets the settings for your instance. To change settings, see the [Set settings endpoint](https://docs.github.com/enterprise-server@3.2/rest/reference/enterprise-admin#set-settings).  **Note:** You cannot retrieve the management console password with the Enterprise administration API.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetSettings((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminGetUserStats

> EnterpriseUserOverview enterpriseAdminGetUserStats()

Get users statistics



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminGetUserStats((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## enterpriseAdminListGlobalWebhooks

> [GlobalHook] enterpriseAdminListGlobalWebhooks(opts)

List global webhooks



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.enterpriseAdminListGlobalWebhooks(opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[GlobalHook]**](GlobalHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise

> EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response enterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, opts)

List organization access to a self-hosted runner group in an enterprise

Lists the organizations with access to a self-hosted runner group.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let runnerGroupId = 56; // Number | Unique identifier of the self-hosted runner group.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.enterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, opts, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **runnerGroupId** | **Number**| Unique identifier of the self-hosted runner group. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response**](EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminListPersonalAccessTokens

> [Authorization] enterpriseAdminListPersonalAccessTokens(opts)

List personal access tokens

Lists personal access tokens for all users, including admin users.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.enterpriseAdminListPersonalAccessTokens(opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Authorization]**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminListPreReceiveEnvironments

> [PreReceiveEnvironment] enterpriseAdminListPreReceiveEnvironments(opts)

List pre-receive environments



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1, // Number | Page number of the results to fetch.
  'direction': "'desc'", // String | The direction to sort the results by.
  'sort': "'created'" // String | 
};
apiInstance.enterpriseAdminListPreReceiveEnvironments(opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **direction** | **String**| The direction to sort the results by. | [optional] [default to &#39;desc&#39;]
 **sort** | **String**|  | [optional] [default to &#39;created&#39;]

### Return type

[**[PreReceiveEnvironment]**](PreReceiveEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminListPreReceiveHooks

> [PreReceiveHook] enterpriseAdminListPreReceiveHooks(opts)

List pre-receive hooks



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1, // Number | Page number of the results to fetch.
  'direction': "'desc'", // String | The direction to sort the results by.
  'sort': "'created'" // String | The property to sort the results by.
};
apiInstance.enterpriseAdminListPreReceiveHooks(opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **direction** | **String**| The direction to sort the results by. | [optional] [default to &#39;desc&#39;]
 **sort** | **String**| The property to sort the results by. | [optional] [default to &#39;created&#39;]

### Return type

[**[PreReceiveHook]**](PreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminListPreReceiveHooksForOrg

> [OrgPreReceiveHook] enterpriseAdminListPreReceiveHooksForOrg(org, opts)

List pre-receive hooks for an organization

List all pre-receive hooks that are enabled or testing for this organization as well as any disabled hooks that can be configured at the organization level. Globally disabled pre-receive hooks that do not allow downstream configuration are not listed.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1, // Number | Page number of the results to fetch.
  'direction': "'desc'", // String | The direction to sort the results by.
  'sort': "'created'" // String | The sort order for the response collection.
};
apiInstance.enterpriseAdminListPreReceiveHooksForOrg(org, opts, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **direction** | **String**| The direction to sort the results by. | [optional] [default to &#39;desc&#39;]
 **sort** | **String**| The sort order for the response collection. | [optional] [default to &#39;created&#39;]

### Return type

[**[OrgPreReceiveHook]**](OrgPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminListPreReceiveHooksForRepo

> [RepositoryPreReceiveHook] enterpriseAdminListPreReceiveHooksForRepo(owner, repo, opts)

List pre-receive hooks for a repository

List all pre-receive hooks that are enabled or testing for this repository as well as any disabled hooks that are allowed to be enabled at the repository level. Pre-receive hooks that are disabled at a higher level and are not configurable will not be listed.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1, // Number | Page number of the results to fetch.
  'direction': "'desc'", // String | The direction to sort the results by.
  'sort': "'created'" // String | 
};
apiInstance.enterpriseAdminListPreReceiveHooksForRepo(owner, repo, opts, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **direction** | **String**| The direction to sort the results by. | [optional] [default to &#39;desc&#39;]
 **sort** | **String**|  | [optional] [default to &#39;created&#39;]

### Return type

[**[RepositoryPreReceiveHook]**](RepositoryPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminListPublicKeys

> [PublicKeyFull] enterpriseAdminListPublicKeys(opts)

List public keys



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1, // Number | Page number of the results to fetch.
  'direction': "'desc'", // String | The direction to sort the results by.
  'sort': "'created'", // String | 
  'since': "since_example" // String | Only show public keys accessed after the given time.
};
apiInstance.enterpriseAdminListPublicKeys(opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **direction** | **String**| The direction to sort the results by. | [optional] [default to &#39;desc&#39;]
 **sort** | **String**|  | [optional] [default to &#39;created&#39;]
 **since** | **String**| Only show public keys accessed after the given time. | [optional] 

### Return type

[**[PublicKeyFull]**](PublicKeyFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminListRunnerApplicationsForEnterprise

> [RunnerApplication] enterpriseAdminListRunnerApplicationsForEnterprise(enterprise)

List runner applications for an enterprise

Lists binaries for the runner application that you can download and run.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
apiInstance.enterpriseAdminListRunnerApplicationsForEnterprise(enterprise, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 

### Return type

[**[RunnerApplication]**](RunnerApplication.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise

> EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response enterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise(enterprise, opts)

List selected organizations enabled for GitHub Actions in an enterprise

Lists the organizations that are selected to have GitHub Actions enabled in an enterprise. To use this endpoint, the enterprise permission policy for &#x60;enabled_organizations&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.enterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise(enterprise, opts, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response**](EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminListSelfHostedRunnerGroupsForEnterprise

> EnterpriseAdminListSelfHostedRunnerGroupsForEnterprise200Response enterpriseAdminListSelfHostedRunnerGroupsForEnterprise(enterprise, opts)

List self-hosted runner groups for an enterprise

Lists all self-hosted runner groups for an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.enterpriseAdminListSelfHostedRunnerGroupsForEnterprise(enterprise, opts, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**EnterpriseAdminListSelfHostedRunnerGroupsForEnterprise200Response**](EnterpriseAdminListSelfHostedRunnerGroupsForEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminListSelfHostedRunnersForEnterprise

> EnterpriseAdminListSelfHostedRunnersForEnterprise200Response enterpriseAdminListSelfHostedRunnersForEnterprise(enterprise, opts)

List self-hosted runners for an enterprise

Lists all self-hosted runners configured for an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.enterpriseAdminListSelfHostedRunnersForEnterprise(enterprise, opts, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**EnterpriseAdminListSelfHostedRunnersForEnterprise200Response**](EnterpriseAdminListSelfHostedRunnersForEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminListSelfHostedRunnersInGroupForEnterprise

> EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise200Response enterpriseAdminListSelfHostedRunnersInGroupForEnterprise(enterprise, runnerGroupId, opts)

List self-hosted runners in a group for an enterprise

Lists the self-hosted runners that are in a specific enterprise group.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let runnerGroupId = 56; // Number | Unique identifier of the self-hosted runner group.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.enterpriseAdminListSelfHostedRunnersInGroupForEnterprise(enterprise, runnerGroupId, opts, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **runnerGroupId** | **Number**| Unique identifier of the self-hosted runner group. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise200Response**](EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminPingGlobalWebhook

> enterpriseAdminPingGlobalWebhook(hookId)

Ping a global webhook

This will trigger a [ping event](https://docs.github.com/enterprise-server@3.2/webhooks/#ping-event) to be sent to the webhook.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let hookId = 56; // Number | The unique identifier of the hook.
apiInstance.enterpriseAdminPingGlobalWebhook(hookId, (error, data, response) => {
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
 **hookId** | **Number**| The unique identifier of the hook. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminPromoteUserToBeSiteAdministrator

> enterpriseAdminPromoteUserToBeSiteAdministrator(username)

Promote a user to be a site administrator

Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@3.2/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.enterpriseAdminPromoteUserToBeSiteAdministrator(username, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminRemoveAnnouncement

> enterpriseAdminRemoveAnnouncement()

Remove the global announcement banner

Removes the global announcement banner in your enterprise.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminRemoveAnnouncement((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## enterpriseAdminRemoveAuthorizedSshKey

> [SshKey] enterpriseAdminRemoveAuthorizedSshKey(authorizedKey)

Remove an authorized SSH key

**Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let authorizedKey = "authorizedKey_example"; // String | The public SSH key.
apiInstance.enterpriseAdminRemoveAuthorizedSshKey(authorizedKey, (error, data, response) => {
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
 **authorizedKey** | **String**| The public SSH key. | 

### Return type

[**[SshKey]**](SshKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## enterpriseAdminRemoveOrgAccessToSelfHostedRunnerGroupInEnterprise

> enterpriseAdminRemoveOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, orgId)

Remove organization access to a self-hosted runner group in an enterprise

Removes an organization from the list of selected organizations that can access a self-hosted runner group. The runner group must have &#x60;visibility&#x60; set to &#x60;selected&#x60;. For more information, see \&quot;[Create a self-hosted runner group for an enterprise](#create-a-self-hosted-runner-group-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let runnerGroupId = 56; // Number | Unique identifier of the self-hosted runner group.
let orgId = 56; // Number | The unique identifier of the organization.
apiInstance.enterpriseAdminRemoveOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, orgId, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **runnerGroupId** | **Number**| Unique identifier of the self-hosted runner group. | 
 **orgId** | **Number**| The unique identifier of the organization. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminRemovePreReceiveHookEnforcementForOrg

> OrgPreReceiveHook enterpriseAdminRemovePreReceiveHookEnforcementForOrg(org, preReceiveHookId)

Remove pre-receive hook enforcement for an organization

Removes any overrides for this hook at the org level for this org.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let preReceiveHookId = 56; // Number | The unique identifier of the pre-receive hook.
apiInstance.enterpriseAdminRemovePreReceiveHookEnforcementForOrg(org, preReceiveHookId, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **preReceiveHookId** | **Number**| The unique identifier of the pre-receive hook. | 

### Return type

[**OrgPreReceiveHook**](OrgPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminRemovePreReceiveHookEnforcementForRepo

> RepositoryPreReceiveHook enterpriseAdminRemovePreReceiveHookEnforcementForRepo(owner, repo, preReceiveHookId)

Remove pre-receive hook enforcement for a repository

Deletes any overridden enforcement on this repository for the specified hook.  Responds with effective values inherited from owner and/or global level.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let preReceiveHookId = 56; // Number | The unique identifier of the pre-receive hook.
apiInstance.enterpriseAdminRemovePreReceiveHookEnforcementForRepo(owner, repo, preReceiveHookId, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **preReceiveHookId** | **Number**| The unique identifier of the pre-receive hook. | 

### Return type

[**RepositoryPreReceiveHook**](RepositoryPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminRemoveSelfHostedRunnerFromGroupForEnterprise

> enterpriseAdminRemoveSelfHostedRunnerFromGroupForEnterprise(enterprise, runnerGroupId, runnerId)

Remove a self-hosted runner from a group for an enterprise

Removes a self-hosted runner from a group configured in an enterprise. The runner is then returned to the default group.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let runnerGroupId = 56; // Number | Unique identifier of the self-hosted runner group.
let runnerId = 56; // Number | Unique identifier of the self-hosted runner.
apiInstance.enterpriseAdminRemoveSelfHostedRunnerFromGroupForEnterprise(enterprise, runnerGroupId, runnerId, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **runnerGroupId** | **Number**| Unique identifier of the self-hosted runner group. | 
 **runnerId** | **Number**| Unique identifier of the self-hosted runner. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enterpriseAdminSetAllowedActionsEnterprise

> enterpriseAdminSetAllowedActionsEnterprise(enterprise, selectedActions)

Set allowed actions for an enterprise

Sets the actions that are allowed in an enterprise. To use this endpoint, the enterprise permission policy for &#x60;allowed_actions&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let selectedActions = new GitHubV3RestApi.SelectedActions(); // SelectedActions | 
apiInstance.enterpriseAdminSetAllowedActionsEnterprise(enterprise, selectedActions, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **selectedActions** | [**SelectedActions**](SelectedActions.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## enterpriseAdminSetAnnouncement

> Announcement enterpriseAdminSetAnnouncement(announcement)

Set the global announcement banner

Sets the message and expiration time for the global announcement banner in your enterprise.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let announcement = new GitHubV3RestApi.Announcement(); // Announcement | 
apiInstance.enterpriseAdminSetAnnouncement(announcement, (error, data, response) => {
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
 **announcement** | [**Announcement**](Announcement.md)|  | 

### Return type

[**Announcement**](Announcement.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminSetGithubActionsPermissionsEnterprise

> enterpriseAdminSetGithubActionsPermissionsEnterprise(enterprise, enterpriseAdminSetGithubActionsPermissionsEnterpriseRequest)

Set GitHub Actions permissions for an enterprise

Sets the GitHub Actions permissions policy for organizations and allowed actions in an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let enterpriseAdminSetGithubActionsPermissionsEnterpriseRequest = {"allowed_actions":"selected","enabled_organizations":"all"}; // EnterpriseAdminSetGithubActionsPermissionsEnterpriseRequest | 
apiInstance.enterpriseAdminSetGithubActionsPermissionsEnterprise(enterprise, enterpriseAdminSetGithubActionsPermissionsEnterpriseRequest, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **enterpriseAdminSetGithubActionsPermissionsEnterpriseRequest** | [**EnterpriseAdminSetGithubActionsPermissionsEnterpriseRequest**](EnterpriseAdminSetGithubActionsPermissionsEnterpriseRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterprise

> enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest)

Set organization access for a self-hosted runner group in an enterprise

Replaces the list of organizations that have access to a self-hosted runner configured in an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let runnerGroupId = 56; // Number | Unique identifier of the self-hosted runner group.
let enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest = {"selected_organization_ids":[32,91]}; // EnterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest | 
apiInstance.enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterprise(enterprise, runnerGroupId, enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **runnerGroupId** | **Number**| Unique identifier of the self-hosted runner group. | 
 **enterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest** | [**EnterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest**](EnterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterprise

> enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterprise(enterprise, enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest)

Set selected organizations enabled for GitHub Actions in an enterprise

Replaces the list of selected organizations that are enabled for GitHub Actions in an enterprise. To use this endpoint, the enterprise permission policy for &#x60;enabled_organizations&#x60; must be configured to &#x60;selected&#x60;. For more information, see \&quot;[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest = {"selected_organization_ids":[32,91]}; // EnterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest | 
apiInstance.enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterprise(enterprise, enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **enterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest** | [**EnterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest**](EnterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## enterpriseAdminSetSelfHostedRunnersInGroupForEnterprise

> enterpriseAdminSetSelfHostedRunnersInGroupForEnterprise(enterprise, runnerGroupId, enterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest)

Set self-hosted runners in a group for an enterprise

Replaces the list of self-hosted runners that are part of an enterprise runner group.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let runnerGroupId = 56; // Number | Unique identifier of the self-hosted runner group.
let enterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest = {"runners":[9,2]}; // EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest | 
apiInstance.enterpriseAdminSetSelfHostedRunnersInGroupForEnterprise(enterprise, runnerGroupId, enterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **runnerGroupId** | **Number**| Unique identifier of the self-hosted runner group. | 
 **enterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest** | [**EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest**](EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## enterpriseAdminSetSettings

> enterpriseAdminSetSettings(settings)

Set settings

Applies settings on your instance. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@3.2/rest/reference/enterprise-admin#get-settings).  **Notes:**  - The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode). - You cannot set the management console password with the Enterprise administration API. Use the &#x60;ghe-set-password&#x60; utility to change the management console password. For more information, see \&quot;[Command-line utilities](https://docs.github.com/enterprise-server@3.2/admin/configuration/configuring-your-enterprise/command-line-utilities#ghe-set-password).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let settings = "settings_example"; // String | A JSON string with the new settings. Note that you only need to pass the specific settings you want to modify. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@3.2/rest/reference/enterprise-admin#get-settings).
apiInstance.enterpriseAdminSetSettings(settings, (error, data, response) => {
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
 **settings** | **String**| A JSON string with the new settings. Note that you only need to pass the specific settings you want to modify. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@3.2/rest/reference/enterprise-admin#get-settings). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## enterpriseAdminStartConfigurationProcess

> enterpriseAdminStartConfigurationProcess()

Start a configuration process

This endpoint allows you to start a configuration process at any time for your updated settings to take effect:

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseAdminStartConfigurationProcess((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## enterpriseAdminStartPreReceiveEnvironmentDownload

> PreReceiveEnvironmentDownloadStatus enterpriseAdminStartPreReceiveEnvironmentDownload(preReceiveEnvironmentId)

Start a pre-receive environment download

Triggers a new download of the environment tarball from the environment&#39;s &#x60;image_url&#x60;. When the download is finished, the newly downloaded tarball will overwrite the existing environment.  If a download cannot be triggered, you will receive a &#x60;422 Unprocessable Entity&#x60; response.  The possible error messages are:  * _Cannot modify or delete the default environment_ * _Can not start a new download when a download is in progress_

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let preReceiveEnvironmentId = 56; // Number | The unique identifier of the pre-receive environment.
apiInstance.enterpriseAdminStartPreReceiveEnvironmentDownload(preReceiveEnvironmentId, (error, data, response) => {
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
 **preReceiveEnvironmentId** | **Number**| The unique identifier of the pre-receive environment. | 

### Return type

[**PreReceiveEnvironmentDownloadStatus**](PreReceiveEnvironmentDownloadStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminSuspendUser

> enterpriseAdminSuspendUser(username, opts)

Suspend a user

If your GitHub instance uses [LDAP Sync with Active Directory LDAP servers](https://docs.github.com/enterprise-server@3.2/admin/identity-and-access-management/using-ldap-for-enterprise-iam/using-ldap), Active Directory LDAP-authenticated users cannot be suspended through this API. If you attempt to suspend an Active Directory LDAP-authenticated user through this API, it will return a &#x60;403&#x60; response.  You can suspend any user account except your own.  Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@3.2/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let opts = {
  'enterpriseAdminSuspendUserRequest': new GitHubV3RestApi.EnterpriseAdminSuspendUserRequest() // EnterpriseAdminSuspendUserRequest | 
};
apiInstance.enterpriseAdminSuspendUser(username, opts, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **enterpriseAdminSuspendUserRequest** | [**EnterpriseAdminSuspendUserRequest**](EnterpriseAdminSuspendUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## enterpriseAdminSyncLdapMappingForTeam

> EnterpriseAdminSyncLdapMappingForTeam201Response enterpriseAdminSyncLdapMappingForTeam(teamId)

Sync LDAP mapping for a team

Note that this API call does not automatically initiate an LDAP sync. Rather, if a &#x60;201&#x60; is returned, the sync job is queued successfully, and is performed when the instance is ready.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let teamId = 56; // Number | The unique identifier of the team.
apiInstance.enterpriseAdminSyncLdapMappingForTeam(teamId, (error, data, response) => {
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
 **teamId** | **Number**| The unique identifier of the team. | 

### Return type

[**EnterpriseAdminSyncLdapMappingForTeam201Response**](EnterpriseAdminSyncLdapMappingForTeam201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminSyncLdapMappingForUser

> EnterpriseAdminSyncLdapMappingForTeam201Response enterpriseAdminSyncLdapMappingForUser(username)

Sync LDAP mapping for a user

Note that this API call does not automatically initiate an LDAP sync. Rather, if a &#x60;201&#x60; is returned, the sync job is queued successfully, and is performed when the instance is ready.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.enterpriseAdminSyncLdapMappingForUser(username, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

[**EnterpriseAdminSyncLdapMappingForTeam201Response**](EnterpriseAdminSyncLdapMappingForTeam201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminUnsuspendUser

> enterpriseAdminUnsuspendUser(username, opts)

Unsuspend a user

If your GitHub instance uses [LDAP Sync with Active Directory LDAP servers](https://docs.github.com/enterprise-server@3.2/admin/identity-and-access-management/using-ldap-for-enterprise-iam/using-ldap), this API is disabled and will return a &#x60;403&#x60; response. Active Directory LDAP-authenticated users cannot be unsuspended using the API.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let opts = {
  'enterpriseAdminUnsuspendUserRequest': new GitHubV3RestApi.EnterpriseAdminUnsuspendUserRequest() // EnterpriseAdminUnsuspendUserRequest | 
};
apiInstance.enterpriseAdminUnsuspendUser(username, opts, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **enterpriseAdminUnsuspendUserRequest** | [**EnterpriseAdminUnsuspendUserRequest**](EnterpriseAdminUnsuspendUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## enterpriseAdminUpdateGlobalWebhook

> GlobalHook2 enterpriseAdminUpdateGlobalWebhook(accept, hookId, opts)

Update a global webhook

Parameters that are not provided will be overwritten with the default value or removed if no default exists.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let accept = "'application/vnd.github.superpro-preview+json'"; // String | This API is under preview and subject to change.
let hookId = 56; // Number | The unique identifier of the hook.
let opts = {
  'enterpriseAdminUpdateGlobalWebhookRequest': {"config":{"url":"https://example.com/webhook"},"events":["organization"]} // EnterpriseAdminUpdateGlobalWebhookRequest | 
};
apiInstance.enterpriseAdminUpdateGlobalWebhook(accept, hookId, opts, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.superpro-preview+json&#39;]
 **hookId** | **Number**| The unique identifier of the hook. | 
 **enterpriseAdminUpdateGlobalWebhookRequest** | [**EnterpriseAdminUpdateGlobalWebhookRequest**](EnterpriseAdminUpdateGlobalWebhookRequest.md)|  | [optional] 

### Return type

[**GlobalHook2**](GlobalHook2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminUpdateLdapMappingForTeam

> LdapMappingTeam enterpriseAdminUpdateLdapMappingForTeam(teamId, enterpriseAdminUpdateLdapMappingForTeamRequest)

Update LDAP mapping for a team

Updates the [distinguished name](https://www.ldap.com/ldap-dns-and-rdns) (DN) of the LDAP entry to map to a team. [LDAP synchronization](https://docs.github.com/enterprise-server@3.2/admin/identity-and-access-management/authenticating-users-for-your-github-enterprise-server-instance/using-ldap#enabling-ldap-sync) must be enabled to map LDAP entries to a team. Use the [Create a team](https://docs.github.com/enterprise-server@3.2/rest/reference/teams/#create-a-team) endpoint to create a team with LDAP mapping.  If you pass the &#x60;hellcat-preview&#x60; media type, you can also update the LDAP mapping of a child team.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let teamId = 56; // Number | The unique identifier of the team.
let enterpriseAdminUpdateLdapMappingForTeamRequest = {"ldap_dn":"cn=Enterprise Ops,ou=teams,dc=github,dc=com"}; // EnterpriseAdminUpdateLdapMappingForTeamRequest | 
apiInstance.enterpriseAdminUpdateLdapMappingForTeam(teamId, enterpriseAdminUpdateLdapMappingForTeamRequest, (error, data, response) => {
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
 **teamId** | **Number**| The unique identifier of the team. | 
 **enterpriseAdminUpdateLdapMappingForTeamRequest** | [**EnterpriseAdminUpdateLdapMappingForTeamRequest**](EnterpriseAdminUpdateLdapMappingForTeamRequest.md)|  | 

### Return type

[**LdapMappingTeam**](LdapMappingTeam.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminUpdateLdapMappingForUser

> LdapMappingUser enterpriseAdminUpdateLdapMappingForUser(username, enterpriseAdminUpdateLdapMappingForTeamRequest)

Update LDAP mapping for a user



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let enterpriseAdminUpdateLdapMappingForTeamRequest = {"ldap_dn":"uid=asdf,ou=users,dc=github,dc=com"}; // EnterpriseAdminUpdateLdapMappingForTeamRequest | 
apiInstance.enterpriseAdminUpdateLdapMappingForUser(username, enterpriseAdminUpdateLdapMappingForTeamRequest, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **enterpriseAdminUpdateLdapMappingForTeamRequest** | [**EnterpriseAdminUpdateLdapMappingForTeamRequest**](EnterpriseAdminUpdateLdapMappingForTeamRequest.md)|  | 

### Return type

[**LdapMappingUser**](LdapMappingUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminUpdateOrgName

> EnterpriseAdminUpdateOrgName202Response enterpriseAdminUpdateOrgName(org, enterpriseAdminUpdateOrgNameRequest)

Update an organization name



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let enterpriseAdminUpdateOrgNameRequest = {"login":"the-new-octocats"}; // EnterpriseAdminUpdateOrgNameRequest | 
apiInstance.enterpriseAdminUpdateOrgName(org, enterpriseAdminUpdateOrgNameRequest, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **enterpriseAdminUpdateOrgNameRequest** | [**EnterpriseAdminUpdateOrgNameRequest**](EnterpriseAdminUpdateOrgNameRequest.md)|  | 

### Return type

[**EnterpriseAdminUpdateOrgName202Response**](EnterpriseAdminUpdateOrgName202Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminUpdatePreReceiveEnvironment

> PreReceiveEnvironment enterpriseAdminUpdatePreReceiveEnvironment(preReceiveEnvironmentId, opts)

Update a pre-receive environment

You cannot modify the default environment. If you attempt to modify the default environment, you will receive a &#x60;422 Unprocessable Entity&#x60; response.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let preReceiveEnvironmentId = 56; // Number | The unique identifier of the pre-receive environment.
let opts = {
  'enterpriseAdminUpdatePreReceiveEnvironmentRequest': new GitHubV3RestApi.EnterpriseAdminUpdatePreReceiveEnvironmentRequest() // EnterpriseAdminUpdatePreReceiveEnvironmentRequest | 
};
apiInstance.enterpriseAdminUpdatePreReceiveEnvironment(preReceiveEnvironmentId, opts, (error, data, response) => {
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
 **preReceiveEnvironmentId** | **Number**| The unique identifier of the pre-receive environment. | 
 **enterpriseAdminUpdatePreReceiveEnvironmentRequest** | [**EnterpriseAdminUpdatePreReceiveEnvironmentRequest**](EnterpriseAdminUpdatePreReceiveEnvironmentRequest.md)|  | [optional] 

### Return type

[**PreReceiveEnvironment**](PreReceiveEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminUpdatePreReceiveHook

> PreReceiveHook enterpriseAdminUpdatePreReceiveHook(preReceiveHookId, opts)

Update a pre-receive hook



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let preReceiveHookId = 56; // Number | The unique identifier of the pre-receive hook.
let opts = {
  'enterpriseAdminUpdatePreReceiveHookRequest': {"allow_downstream_configuration":true,"environment":{"id":1},"name":"Check Commits"} // EnterpriseAdminUpdatePreReceiveHookRequest | 
};
apiInstance.enterpriseAdminUpdatePreReceiveHook(preReceiveHookId, opts, (error, data, response) => {
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
 **preReceiveHookId** | **Number**| The unique identifier of the pre-receive hook. | 
 **enterpriseAdminUpdatePreReceiveHookRequest** | [**EnterpriseAdminUpdatePreReceiveHookRequest**](EnterpriseAdminUpdatePreReceiveHookRequest.md)|  | [optional] 

### Return type

[**PreReceiveHook**](PreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminUpdatePreReceiveHookEnforcementForOrg

> OrgPreReceiveHook enterpriseAdminUpdatePreReceiveHookEnforcementForOrg(org, preReceiveHookId, opts)

Update pre-receive hook enforcement for an organization

For pre-receive hooks which are allowed to be configured at the org level, you can set &#x60;enforcement&#x60; and &#x60;allow_downstream_configuration&#x60;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let preReceiveHookId = 56; // Number | The unique identifier of the pre-receive hook.
let opts = {
  'enterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest': {"allow_downstream_configuration":false,"enforcement":"enabled"} // EnterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest | 
};
apiInstance.enterpriseAdminUpdatePreReceiveHookEnforcementForOrg(org, preReceiveHookId, opts, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **preReceiveHookId** | **Number**| The unique identifier of the pre-receive hook. | 
 **enterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest** | [**EnterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest**](EnterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest.md)|  | [optional] 

### Return type

[**OrgPreReceiveHook**](OrgPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminUpdatePreReceiveHookEnforcementForRepo

> RepositoryPreReceiveHook enterpriseAdminUpdatePreReceiveHookEnforcementForRepo(owner, repo, preReceiveHookId, opts)

Update pre-receive hook enforcement for a repository

For pre-receive hooks which are allowed to be configured at the repo level, you can set &#x60;enforcement&#x60;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let preReceiveHookId = 56; // Number | The unique identifier of the pre-receive hook.
let opts = {
  'enterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest': {"enforcement":"enabled"} // EnterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest | 
};
apiInstance.enterpriseAdminUpdatePreReceiveHookEnforcementForRepo(owner, repo, preReceiveHookId, opts, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **preReceiveHookId** | **Number**| The unique identifier of the pre-receive hook. | 
 **enterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest** | [**EnterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest**](EnterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest.md)|  | [optional] 

### Return type

[**RepositoryPreReceiveHook**](RepositoryPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminUpdateSelfHostedRunnerGroupForEnterprise

> RunnerGroupsEnterprise enterpriseAdminUpdateSelfHostedRunnerGroupForEnterprise(enterprise, runnerGroupId, opts)

Update a self-hosted runner group for an enterprise

Updates the &#x60;name&#x60; and &#x60;visibility&#x60; of a self-hosted runner group in an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let runnerGroupId = 56; // Number | Unique identifier of the self-hosted runner group.
let opts = {
  'enterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest': {"name":"Expensive hardware runners","visibility":"selected"} // EnterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest | 
};
apiInstance.enterpriseAdminUpdateSelfHostedRunnerGroupForEnterprise(enterprise, runnerGroupId, opts, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **runnerGroupId** | **Number**| Unique identifier of the self-hosted runner group. | 
 **enterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest** | [**EnterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest**](EnterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest.md)|  | [optional] 

### Return type

[**RunnerGroupsEnterprise**](RunnerGroupsEnterprise.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminUpdateUsernameForUser

> EnterpriseAdminUpdateOrgName202Response enterpriseAdminUpdateUsernameForUser(username, enterpriseAdminUpdateUsernameForUserRequest)

Update the username for a user



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let enterpriseAdminUpdateUsernameForUserRequest = {"login":"thenewmonalisa"}; // EnterpriseAdminUpdateUsernameForUserRequest | 
apiInstance.enterpriseAdminUpdateUsernameForUser(username, enterpriseAdminUpdateUsernameForUserRequest, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **enterpriseAdminUpdateUsernameForUserRequest** | [**EnterpriseAdminUpdateUsernameForUserRequest**](EnterpriseAdminUpdateUsernameForUserRequest.md)|  | 

### Return type

[**EnterpriseAdminUpdateOrgName202Response**](EnterpriseAdminUpdateOrgName202Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminUpgradeLicense

> enterpriseAdminUpgradeLicense(opts)

Upgrade a license

This API upgrades your license and also triggers the configuration process.  **Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let opts = {
  'license': "license_example" // String | The content of your new _.ghl_ license file.
};
apiInstance.enterpriseAdminUpgradeLicense(opts, (error, data, response) => {
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
 **license** | **String**| The content of your new _.ghl_ license file. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

