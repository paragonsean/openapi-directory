# GitHubV3RestApi.EnterpriseAdminApi

All URIs are relative to *http://HOSTNAME/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterpriseAdminAddAuthorizedSshKey**](EnterpriseAdminApi.md#enterpriseAdminAddAuthorizedSshKey) | **POST** /setup/api/settings/authorized-keys | Add an authorized SSH key
[**enterpriseAdminCreateEnterpriseServerLicense**](EnterpriseAdminApi.md#enterpriseAdminCreateEnterpriseServerLicense) | **POST** /setup/api/start | Create a GitHub license
[**enterpriseAdminCreateGlobalWebhook**](EnterpriseAdminApi.md#enterpriseAdminCreateGlobalWebhook) | **POST** /admin/hooks | Create a global webhook
[**enterpriseAdminCreateImpersonationOAuthToken**](EnterpriseAdminApi.md#enterpriseAdminCreateImpersonationOAuthToken) | **POST** /admin/users/{username}/authorizations | Create an impersonation OAuth token
[**enterpriseAdminCreateOrg**](EnterpriseAdminApi.md#enterpriseAdminCreateOrg) | **POST** /admin/organizations | Create an organization
[**enterpriseAdminCreatePreReceiveEnvironment**](EnterpriseAdminApi.md#enterpriseAdminCreatePreReceiveEnvironment) | **POST** /admin/pre-receive-environments | Create a pre-receive environment
[**enterpriseAdminCreatePreReceiveHook**](EnterpriseAdminApi.md#enterpriseAdminCreatePreReceiveHook) | **POST** /admin/pre-receive-hooks | Create a pre-receive hook
[**enterpriseAdminCreateUser**](EnterpriseAdminApi.md#enterpriseAdminCreateUser) | **POST** /admin/users | Create a user
[**enterpriseAdminDeleteGlobalWebhook**](EnterpriseAdminApi.md#enterpriseAdminDeleteGlobalWebhook) | **DELETE** /admin/hooks/{hook_id} | Delete a global webhook
[**enterpriseAdminDeleteImpersonationOAuthToken**](EnterpriseAdminApi.md#enterpriseAdminDeleteImpersonationOAuthToken) | **DELETE** /admin/users/{username}/authorizations | Delete an impersonation OAuth token
[**enterpriseAdminDeletePersonalAccessToken**](EnterpriseAdminApi.md#enterpriseAdminDeletePersonalAccessToken) | **DELETE** /admin/tokens/{token_id} | Delete a personal access token
[**enterpriseAdminDeletePreReceiveEnvironment**](EnterpriseAdminApi.md#enterpriseAdminDeletePreReceiveEnvironment) | **DELETE** /admin/pre-receive-environments/{pre_receive_environment_id} | Delete a pre-receive environment
[**enterpriseAdminDeletePreReceiveHook**](EnterpriseAdminApi.md#enterpriseAdminDeletePreReceiveHook) | **DELETE** /admin/pre-receive-hooks/{pre_receive_hook_id} | Delete a pre-receive hook
[**enterpriseAdminDeletePublicKey**](EnterpriseAdminApi.md#enterpriseAdminDeletePublicKey) | **DELETE** /admin/keys/{key_ids} | Delete a public key
[**enterpriseAdminDeleteUser**](EnterpriseAdminApi.md#enterpriseAdminDeleteUser) | **DELETE** /admin/users/{username} | Delete a user
[**enterpriseAdminDemoteSiteAdministrator**](EnterpriseAdminApi.md#enterpriseAdminDemoteSiteAdministrator) | **DELETE** /users/{username}/site_admin | Demote a site administrator
[**enterpriseAdminEnableOrDisableMaintenanceMode**](EnterpriseAdminApi.md#enterpriseAdminEnableOrDisableMaintenanceMode) | **POST** /setup/api/maintenance | Enable or disable maintenance mode
[**enterpriseAdminGetAllAuthorizedSshKeys**](EnterpriseAdminApi.md#enterpriseAdminGetAllAuthorizedSshKeys) | **GET** /setup/api/settings/authorized-keys | Get all authorized SSH keys
[**enterpriseAdminGetAllStats**](EnterpriseAdminApi.md#enterpriseAdminGetAllStats) | **GET** /enterprise/stats/all | Get all statistics
[**enterpriseAdminGetCommentStats**](EnterpriseAdminApi.md#enterpriseAdminGetCommentStats) | **GET** /enterprise/stats/comments | Get comment statistics
[**enterpriseAdminGetConfigurationStatus**](EnterpriseAdminApi.md#enterpriseAdminGetConfigurationStatus) | **GET** /setup/api/configcheck | Get the configuration status
[**enterpriseAdminGetDownloadStatusForPreReceiveEnvironment**](EnterpriseAdminApi.md#enterpriseAdminGetDownloadStatusForPreReceiveEnvironment) | **GET** /admin/pre-receive-environments/{pre_receive_environment_id}/downloads/latest | Get the download status for a pre-receive environment
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
[**enterpriseAdminGetSettings**](EnterpriseAdminApi.md#enterpriseAdminGetSettings) | **GET** /setup/api/settings | Get settings
[**enterpriseAdminGetUserStats**](EnterpriseAdminApi.md#enterpriseAdminGetUserStats) | **GET** /enterprise/stats/users | Get users statistics
[**enterpriseAdminListGlobalWebhooks**](EnterpriseAdminApi.md#enterpriseAdminListGlobalWebhooks) | **GET** /admin/hooks | List global webhooks
[**enterpriseAdminListPersonalAccessTokens**](EnterpriseAdminApi.md#enterpriseAdminListPersonalAccessTokens) | **GET** /admin/tokens | List personal access tokens
[**enterpriseAdminListPreReceiveEnvironments**](EnterpriseAdminApi.md#enterpriseAdminListPreReceiveEnvironments) | **GET** /admin/pre-receive-environments | List pre-receive environments
[**enterpriseAdminListPreReceiveHooks**](EnterpriseAdminApi.md#enterpriseAdminListPreReceiveHooks) | **GET** /admin/pre-receive-hooks | List pre-receive hooks
[**enterpriseAdminListPreReceiveHooksForOrg**](EnterpriseAdminApi.md#enterpriseAdminListPreReceiveHooksForOrg) | **GET** /orgs/{org}/pre-receive-hooks | List pre-receive hooks for an organization
[**enterpriseAdminListPreReceiveHooksForRepo**](EnterpriseAdminApi.md#enterpriseAdminListPreReceiveHooksForRepo) | **GET** /repos/{owner}/{repo}/pre-receive-hooks | List pre-receive hooks for a repository
[**enterpriseAdminListPublicKeys**](EnterpriseAdminApi.md#enterpriseAdminListPublicKeys) | **GET** /admin/keys | List public keys
[**enterpriseAdminPingGlobalWebhook**](EnterpriseAdminApi.md#enterpriseAdminPingGlobalWebhook) | **POST** /admin/hooks/{hook_id}/pings | Ping a global webhook
[**enterpriseAdminPromoteUserToBeSiteAdministrator**](EnterpriseAdminApi.md#enterpriseAdminPromoteUserToBeSiteAdministrator) | **PUT** /users/{username}/site_admin | Promote a user to be a site administrator
[**enterpriseAdminRemoveAuthorizedSshKey**](EnterpriseAdminApi.md#enterpriseAdminRemoveAuthorizedSshKey) | **DELETE** /setup/api/settings/authorized-keys | Remove an authorized SSH key
[**enterpriseAdminRemovePreReceiveHookEnforcementForOrg**](EnterpriseAdminApi.md#enterpriseAdminRemovePreReceiveHookEnforcementForOrg) | **DELETE** /orgs/{org}/pre-receive-hooks/{pre_receive_hook_id} | Remove pre-receive hook enforcement for an organization
[**enterpriseAdminRemovePreReceiveHookEnforcementForRepo**](EnterpriseAdminApi.md#enterpriseAdminRemovePreReceiveHookEnforcementForRepo) | **DELETE** /repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id} | Remove pre-receive hook enforcement for a repository
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
[**enterpriseAdminUpdateUsernameForUser**](EnterpriseAdminApi.md#enterpriseAdminUpdateUsernameForUser) | **PATCH** /admin/users/{username} | Update the username for a user
[**enterpriseAdminUpgradeLicense**](EnterpriseAdminApi.md#enterpriseAdminUpgradeLicense) | **POST** /setup/api/upgrade | Upgrade a license
[**enterpriseStatsGistsGet**](EnterpriseAdminApi.md#enterpriseStatsGistsGet) | **GET** /enterprise/stats/gists | Get gist statistics



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


## enterpriseAdminCreateEnterpriseServerLicense

> enterpriseAdminCreateEnterpriseServerLicense(license, opts)

Create a GitHub license

When you boot a GitHub instance for the first time, you can use the following endpoint to upload a license.  Note that you need to &#x60;POST&#x60; to [&#x60;/setup/api/configure&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/enterprise-admin#start-a-configuration-process) to start the actual configuration process.  When using this endpoint, your GitHub instance must have a password set. This can be accomplished two ways:  1.  If you&#39;re working directly with the API before accessing the web interface, you must pass in the password parameter to set your password. 2.  If you set up your instance via the web interface before accessing the API, your calls to this endpoint do not need the password parameter.  **Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let license = "license_example"; // String | The content of your _.ghl_ license file.
let opts = {
  'password': "password_example", // String | You **must** provide a password _only if_ you are uploading your license for the first time. If you previously set a password through the web interface, you don't need this parameter.
  'settings': "settings_example" // String | An optional JSON string containing the installation settings. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@2.21/rest/reference/enterprise-admin#get-settings).
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
 **settings** | **String**| An optional JSON string containing the installation settings. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@2.21/rest/reference/enterprise-admin#get-settings). | [optional] 

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

> Authorization enterpriseAdminCreateImpersonationOAuthToken(username, opts)

Create an impersonation OAuth token



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | 
let opts = {
  'enterpriseAdminCreateImpersonationOAuthTokenRequest': new GitHubV3RestApi.EnterpriseAdminCreateImpersonationOAuthTokenRequest() // EnterpriseAdminCreateImpersonationOAuthTokenRequest | 
};
apiInstance.enterpriseAdminCreateImpersonationOAuthToken(username, opts, (error, data, response) => {
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
 **username** | **String**|  | 
 **enterpriseAdminCreateImpersonationOAuthTokenRequest** | [**EnterpriseAdminCreateImpersonationOAuthTokenRequest**](EnterpriseAdminCreateImpersonationOAuthTokenRequest.md)|  | [optional] 

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminCreateOrg

> OrganizationSimple enterpriseAdminCreateOrg(opts)

Create an organization



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let opts = {
  'enterpriseAdminCreateOrgRequest': {"admin":"monalisaoctocat","login":"github","profile_name":"GitHub, Inc."} // EnterpriseAdminCreateOrgRequest | 
};
apiInstance.enterpriseAdminCreateOrg(opts, (error, data, response) => {
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
 **enterpriseAdminCreateOrgRequest** | [**EnterpriseAdminCreateOrgRequest**](EnterpriseAdminCreateOrgRequest.md)|  | [optional] 

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


## enterpriseAdminCreateUser

> SimpleUser enterpriseAdminCreateUser(enterpriseAdminCreateUserRequest)

Create a user

If an external authentication mechanism is used, the login name should match the login name in the external system. If you are using LDAP authentication, you should also [update the LDAP mapping](https://docs.github.com/enterprise-server@2.21/rest/reference/enterprise-admin#update-ldap-mapping-for-a-user) for the user.  The login name will be normalized to only contain alphanumeric characters or single hyphens. For example, if you send &#x60;\&quot;octo_cat\&quot;&#x60; as the login, a user named &#x60;\&quot;octo-cat\&quot;&#x60; will be created.  If the login name or email address is already associated with an account, the server will return a &#x60;422&#x60; response.

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

> enterpriseAdminDeleteGlobalWebhook(accept, hookId)

Delete a global webhook



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let accept = "'application/vnd.github.superpro-preview+json'"; // String | This API is under preview and subject to change.
let hookId = 56; // Number | 
apiInstance.enterpriseAdminDeleteGlobalWebhook(accept, hookId, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.superpro-preview+json&#39;]
 **hookId** | **Number**|  | 

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
let username = "username_example"; // String | 
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
 **username** | **String**|  | 

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
let tokenId = 56; // Number | 
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
 **tokenId** | **Number**|  | 

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
let preReceiveEnvironmentId = 56; // Number | 
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
 **preReceiveEnvironmentId** | **Number**|  | 

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
let preReceiveHookId = 56; // Number | pre_receive_hook_id parameter
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
 **preReceiveHookId** | **Number**| pre_receive_hook_id parameter | 

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
let keyIds = "keyIds_example"; // String | 
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
 **keyIds** | **String**|  | 

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

Deleting a user will delete all their repositories, gists, applications, and personal settings. [Suspending a user](https://docs.github.com/enterprise-server@2.21/rest/reference/enterprise-admin#suspend-a-user) is often a better option.  You can delete any user account except your own.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | 
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
 **username** | **String**|  | 

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
let username = "username_example"; // String | 
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
 **username** | **String**|  | 

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
let preReceiveEnvironmentId = 56; // Number | 
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
 **preReceiveEnvironmentId** | **Number**|  | 

### Return type

[**PreReceiveEnvironmentDownloadStatus**](PreReceiveEnvironmentDownloadStatus.md)

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
let hookId = 56; // Number | 
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
 **hookId** | **Number**|  | 

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
let preReceiveEnvironmentId = 56; // Number | 
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
 **preReceiveEnvironmentId** | **Number**|  | 

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
let preReceiveHookId = 56; // Number | pre_receive_hook_id parameter
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
 **preReceiveHookId** | **Number**| pre_receive_hook_id parameter | 

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
let org = "org_example"; // String | 
let preReceiveHookId = 56; // Number | pre_receive_hook_id parameter
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
 **org** | **String**|  | 
 **preReceiveHookId** | **Number**| pre_receive_hook_id parameter | 

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
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let preReceiveHookId = 56; // Number | pre_receive_hook_id parameter
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **preReceiveHookId** | **Number**| pre_receive_hook_id parameter | 

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


## enterpriseAdminGetSettings

> EnterpriseSettings enterpriseAdminGetSettings()

Get settings



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

> [GlobalHook] enterpriseAdminListGlobalWebhooks(accept, opts)

List global webhooks



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let accept = "'application/vnd.github.superpro-preview+json'"; // String | This API is under preview and subject to change.
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.enterpriseAdminListGlobalWebhooks(accept, opts, (error, data, response) => {
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
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[GlobalHook]**](GlobalHook.md)

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
  'perPage': 30, // Number | Results per page (max 100)
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
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
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
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1, // Number | Page number of the results to fetch.
  'direction': "'desc'", // String | One of `asc` (ascending) or `desc` (descending).
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
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to &#39;desc&#39;]
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
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1, // Number | Page number of the results to fetch.
  'direction': "'desc'", // String | One of `asc` (ascending) or `desc` (descending).
  'sort': "'created'" // String | One of `created` (when the repository was starred) or `updated` (when it was last pushed to) or `name`.
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
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to &#39;desc&#39;]
 **sort** | **String**| One of &#x60;created&#x60; (when the repository was starred) or &#x60;updated&#x60; (when it was last pushed to) or &#x60;name&#x60;. | [optional] [default to &#39;created&#39;]

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
let org = "org_example"; // String | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1, // Number | Page number of the results to fetch.
  'direction': "'desc'", // String | One of `asc` (ascending) or `desc` (descending).
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
 **org** | **String**|  | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to &#39;desc&#39;]
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
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1, // Number | Page number of the results to fetch.
  'direction': "'desc'", // String | One of `asc` (ascending) or `desc` (descending).
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to &#39;desc&#39;]
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
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1, // Number | Page number of the results to fetch.
  'direction': "'desc'", // String | One of `asc` (ascending) or `desc` (descending).
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
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to &#39;desc&#39;]
 **sort** | **String**|  | [optional] [default to &#39;created&#39;]
 **since** | **String**| Only show public keys accessed after the given time. | [optional] 

### Return type

[**[PublicKeyFull]**](PublicKeyFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminPingGlobalWebhook

> enterpriseAdminPingGlobalWebhook(accept, hookId)

Ping a global webhook

This will trigger a [ping event](https://docs.github.com/enterprise-server@2.21/webhooks/#ping-event) to be sent to the webhook.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let accept = "'application/vnd.github.superpro-preview+json'"; // String | This API is under preview and subject to change.
let hookId = 56; // Number | 
apiInstance.enterpriseAdminPingGlobalWebhook(accept, hookId, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.superpro-preview+json&#39;]
 **hookId** | **Number**|  | 

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

Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | 
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
 **username** | **String**|  | 

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


## enterpriseAdminRemovePreReceiveHookEnforcementForOrg

> OrgPreReceiveHook enterpriseAdminRemovePreReceiveHookEnforcementForOrg(org, preReceiveHookId)

Remove pre-receive hook enforcement for an organization

Removes any overrides for this hook at the org level for this org.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let org = "org_example"; // String | 
let preReceiveHookId = 56; // Number | pre_receive_hook_id parameter
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
 **org** | **String**|  | 
 **preReceiveHookId** | **Number**| pre_receive_hook_id parameter | 

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
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let preReceiveHookId = 56; // Number | pre_receive_hook_id parameter
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **preReceiveHookId** | **Number**| pre_receive_hook_id parameter | 

### Return type

[**RepositoryPreReceiveHook**](RepositoryPreReceiveHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseAdminSetSettings

> enterpriseAdminSetSettings(settings)

Set settings

For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@2.21/rest/reference/enterprise-admin#get-settings).  **Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let settings = "settings_example"; // String | A JSON string with the new settings. Note that you only need to pass the specific settings you want to modify. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@2.21/rest/reference/enterprise-admin#get-settings).
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
 **settings** | **String**| A JSON string with the new settings. Note that you only need to pass the specific settings you want to modify. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@2.21/rest/reference/enterprise-admin#get-settings). | 

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
let preReceiveEnvironmentId = 56; // Number | 
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
 **preReceiveEnvironmentId** | **Number**|  | 

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

If your GitHub instance uses [LDAP Sync with Active Directory LDAP servers](https://help.github.com/enterprise/admin/guides/user-management/using-ldap), Active Directory LDAP-authenticated users cannot be suspended through this API. If you attempt to suspend an Active Directory LDAP-authenticated user through this API, it will return a &#x60;403&#x60; response.  You can suspend any user account except your own.  Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | 
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
 **username** | **String**|  | 
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
let teamId = 56; // Number | 
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
 **teamId** | **Number**|  | 

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
let username = "username_example"; // String | 
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
 **username** | **String**|  | 

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

If your GitHub instance uses [LDAP Sync with Active Directory LDAP servers](https://help.github.com/enterprise/admin/guides/user-management/using-ldap), this API is disabled and will return a &#x60;403&#x60; response. Active Directory LDAP-authenticated users cannot be unsuspended using the API.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | 
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
 **username** | **String**|  | 
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
let hookId = 56; // Number | 
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
 **hookId** | **Number**|  | 
 **enterpriseAdminUpdateGlobalWebhookRequest** | [**EnterpriseAdminUpdateGlobalWebhookRequest**](EnterpriseAdminUpdateGlobalWebhookRequest.md)|  | [optional] 

### Return type

[**GlobalHook2**](GlobalHook2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminUpdateLdapMappingForTeam

> LdapMappingTeam enterpriseAdminUpdateLdapMappingForTeam(teamId, opts)

Update LDAP mapping for a team

Updates the [distinguished name](https://www.ldap.com/ldap-dns-and-rdns) (DN) of the LDAP entry to map to a team. [LDAP synchronization](https://help.github.com/enterprise/admin/guides/user-management/using-ldap/#enabling-ldap-sync) must be enabled to map LDAP entries to a team. Use the [Create a team](https://docs.github.com/enterprise-server@2.21/rest/reference/teams/#create-a-team) endpoint to create a team with LDAP mapping.  You can also update the LDAP mapping of a child team.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let teamId = 56; // Number | 
let opts = {
  'enterpriseAdminUpdateLdapMappingForTeamRequest': {"ldap_dn":"cn=Enterprise Ops,ou=teams,dc=github,dc=com"} // EnterpriseAdminUpdateLdapMappingForTeamRequest | 
};
apiInstance.enterpriseAdminUpdateLdapMappingForTeam(teamId, opts, (error, data, response) => {
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
 **teamId** | **Number**|  | 
 **enterpriseAdminUpdateLdapMappingForTeamRequest** | [**EnterpriseAdminUpdateLdapMappingForTeamRequest**](EnterpriseAdminUpdateLdapMappingForTeamRequest.md)|  | [optional] 

### Return type

[**LdapMappingTeam**](LdapMappingTeam.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseAdminUpdateLdapMappingForUser

> LdapMappingUser enterpriseAdminUpdateLdapMappingForUser(username, opts)

Update LDAP mapping for a user



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
let username = "username_example"; // String | 
let opts = {
  'enterpriseAdminUpdateLdapMappingForTeamRequest': {"ldap_dn":"uid=asdf,ou=users,dc=github,dc=com"} // EnterpriseAdminUpdateLdapMappingForTeamRequest | 
};
apiInstance.enterpriseAdminUpdateLdapMappingForUser(username, opts, (error, data, response) => {
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
 **username** | **String**|  | 
 **enterpriseAdminUpdateLdapMappingForTeamRequest** | [**EnterpriseAdminUpdateLdapMappingForTeamRequest**](EnterpriseAdminUpdateLdapMappingForTeamRequest.md)|  | [optional] 

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
let org = "org_example"; // String | 
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
 **org** | **String**|  | 
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
let preReceiveEnvironmentId = 56; // Number | 
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
 **preReceiveEnvironmentId** | **Number**|  | 
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
let preReceiveHookId = 56; // Number | pre_receive_hook_id parameter
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
 **preReceiveHookId** | **Number**| pre_receive_hook_id parameter | 
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
let org = "org_example"; // String | 
let preReceiveHookId = 56; // Number | pre_receive_hook_id parameter
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
 **org** | **String**|  | 
 **preReceiveHookId** | **Number**| pre_receive_hook_id parameter | 
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
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let preReceiveHookId = 56; // Number | pre_receive_hook_id parameter
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **preReceiveHookId** | **Number**| pre_receive_hook_id parameter | 
 **enterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest** | [**EnterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest**](EnterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest.md)|  | [optional] 

### Return type

[**RepositoryPreReceiveHook**](RepositoryPreReceiveHook.md)

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
let username = "username_example"; // String | 
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
 **username** | **String**|  | 
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


## enterpriseStatsGistsGet

> EnterpriseGistOverview enterpriseStatsGistsGet()

Get gist statistics



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EnterpriseAdminApi();
apiInstance.enterpriseStatsGistsGet((error, data, response) => {
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

