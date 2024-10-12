# AppCenterClient.AccountApi

All URIs are relative to *https://api.appcenter.ms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appApiTokensDelete**](AccountApi.md#appApiTokensDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/api_tokens/{api_token_id} | 
[**appApiTokensList**](AccountApi.md#appApiTokensList) | **GET** /v0.1/apps/{owner_name}/{app_name}/api_tokens | 
[**appApiTokensNew**](AccountApi.md#appApiTokensNew) | **POST** /v0.1/apps/{owner_name}/{app_name}/api_tokens | 
[**appInvitationsAccept**](AccountApi.md#appInvitationsAccept) | **POST** /v0.1/user/invitations/apps/{invitation_token}/accept | 
[**appInvitationsCreate**](AccountApi.md#appInvitationsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/invitations | 
[**appInvitationsCreateByEmail**](AccountApi.md#appInvitationsCreateByEmail) | **POST** /v0.1/apps/{owner_name}/{app_name}/invitations/{user_email} | 
[**appInvitationsDelete**](AccountApi.md#appInvitationsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/invitations/{user_email} | 
[**appInvitationsList**](AccountApi.md#appInvitationsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/invitations | 
[**appInvitationsReject**](AccountApi.md#appInvitationsReject) | **POST** /v0.1/user/invitations/apps/{invitation_token}/reject | 
[**appInvitationsUpdatePermissions**](AccountApi.md#appInvitationsUpdatePermissions) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/invitations/{user_email} | 
[**appsCreate**](AccountApi.md#appsCreate) | **POST** /v0.1/apps | 
[**appsCreateForOrg**](AccountApi.md#appsCreateForOrg) | **POST** /v0.1/orgs/{org_name}/apps | 
[**appsDelete**](AccountApi.md#appsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name} | 
[**appsDeleteAvatar**](AccountApi.md#appsDeleteAvatar) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/avatar | 
[**appsGet**](AccountApi.md#appsGet) | **GET** /v0.1/apps/{owner_name}/{app_name} | 
[**appsGetForOrgUser**](AccountApi.md#appsGetForOrgUser) | **GET** /v0.1/orgs/{org_name}/users/{user_name}/apps | 
[**appsGetTeams**](AccountApi.md#appsGetTeams) | **GET** /v0.1/apps/{owner_name}/{app_name}/teams | 
[**appsList**](AccountApi.md#appsList) | **GET** /v0.1/apps | 
[**appsListForOrg**](AccountApi.md#appsListForOrg) | **GET** /v0.1/orgs/{org_name}/apps | 
[**appsListTesters**](AccountApi.md#appsListTesters) | **GET** /v0.1/apps/{owner_name}/{app_name}/testers | 
[**appsRemoveUser**](AccountApi.md#appsRemoveUser) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/users/{user_email} | 
[**appsTransferOwnership**](AccountApi.md#appsTransferOwnership) | **POST** /v0.1/apps/{owner_name}/{app_name}/transfer/{destination_owner_name} | 
[**appsTransferToOrg**](AccountApi.md#appsTransferToOrg) | **POST** /v0.1/apps/{owner_name}/{app_name}/transfer_to_org | 
[**appsUpdate**](AccountApi.md#appsUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name} | 
[**appsUpdateAvatar**](AccountApi.md#appsUpdateAvatar) | **POST** /v0.1/apps/{owner_name}/{app_name}/avatar | 
[**appsUpdateUserPermissions**](AccountApi.md#appsUpdateUserPermissions) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/users/{user_email} | 
[**azureSubscriptionDeleteForApp**](AccountApi.md#azureSubscriptionDeleteForApp) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/azure_subscriptions/{azure_subscription_id} | 
[**azureSubscriptionLinkForApp**](AccountApi.md#azureSubscriptionLinkForApp) | **POST** /v0.1/apps/{owner_name}/{app_name}/azure_subscriptions | 
[**azureSubscriptionListForApp**](AccountApi.md#azureSubscriptionListForApp) | **GET** /v0.1/apps/{owner_name}/{app_name}/azure_subscriptions | 
[**azureSubscriptionListForOrg**](AccountApi.md#azureSubscriptionListForOrg) | **GET** /v0.1/orgs/{org_name}/azure_subscriptions | 
[**azureSubscriptionListForUser**](AccountApi.md#azureSubscriptionListForUser) | **GET** /v0.1/azure_subscriptions | 
[**distributionGroupInvitationsAcceptAll**](AccountApi.md#distributionGroupInvitationsAcceptAll) | **POST** /v0.1/user/invitations/distribution_groups/accept | 
[**distributionGroupsAddApps**](AccountApi.md#distributionGroupsAddApps) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/apps | 
[**distributionGroupsAddUser**](AccountApi.md#distributionGroupsAddUser) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/members | 
[**distributionGroupsAddUsersForOrg**](AccountApi.md#distributionGroupsAddUsersForOrg) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/members | 
[**distributionGroupsBulkDeleteApps**](AccountApi.md#distributionGroupsBulkDeleteApps) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/apps/bulk_delete | 
[**distributionGroupsBulkDeleteUsers**](AccountApi.md#distributionGroupsBulkDeleteUsers) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/members/bulk_delete | 
[**distributionGroupsCreate**](AccountApi.md#distributionGroupsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_groups | 
[**distributionGroupsCreateForOrg**](AccountApi.md#distributionGroupsCreateForOrg) | **POST** /v0.1/orgs/{org_name}/distribution_groups | 
[**distributionGroupsDelete**](AccountApi.md#distributionGroupsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name} | 
[**distributionGroupsDeleteForOrg**](AccountApi.md#distributionGroupsDeleteForOrg) | **DELETE** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name} | 
[**distributionGroupsDetailsForOrg**](AccountApi.md#distributionGroupsDetailsForOrg) | **GET** /v0.1/orgs/{org_name}/distribution_groups_details | 
[**distributionGroupsGet**](AccountApi.md#distributionGroupsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name} | 
[**distributionGroupsGetApps**](AccountApi.md#distributionGroupsGetApps) | **GET** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/apps | 
[**distributionGroupsGetForOrg**](AccountApi.md#distributionGroupsGetForOrg) | **GET** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name} | 
[**distributionGroupsList**](AccountApi.md#distributionGroupsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups | 
[**distributionGroupsListAllTestersForOrg**](AccountApi.md#distributionGroupsListAllTestersForOrg) | **GET** /v0.1/orgs/{org_name}/testers | 
[**distributionGroupsListForOrg**](AccountApi.md#distributionGroupsListForOrg) | **GET** /v0.1/orgs/{org_name}/distribution_groups | 
[**distributionGroupsListUsers**](AccountApi.md#distributionGroupsListUsers) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/members | 
[**distributionGroupsListUsersForOrg**](AccountApi.md#distributionGroupsListUsersForOrg) | **GET** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/members | 
[**distributionGroupsPatchForOrg**](AccountApi.md#distributionGroupsPatchForOrg) | **PATCH** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name} | 
[**distributionGroupsRemoveUser**](AccountApi.md#distributionGroupsRemoveUser) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/members/bulk_delete | 
[**distributionGroupsResendInvite**](AccountApi.md#distributionGroupsResendInvite) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/resend_invite | 
[**distributionGroupsResendSharedInvite**](AccountApi.md#distributionGroupsResendSharedInvite) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/resend_invite | 
[**distributionGroupsUpdate**](AccountApi.md#distributionGroupsUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name} | 
[**invitationsSent**](AccountApi.md#invitationsSent) | **GET** /v0.1/invitations/sent | 
[**orgInvitations**](AccountApi.md#orgInvitations) | **POST** /v0.1/orgs/{org_name}/invitations/{email}/revoke | 
[**orgInvitationsAccept**](AccountApi.md#orgInvitationsAccept) | **POST** /v0.1/user/invitations/orgs/{invitation_token}/accept | 
[**orgInvitationsCreate**](AccountApi.md#orgInvitationsCreate) | **POST** /v0.1/orgs/{org_name}/invitations | 
[**orgInvitationsDelete**](AccountApi.md#orgInvitationsDelete) | **DELETE** /v0.1/orgs/{org_name}/invitations | 
[**orgInvitationsListPending**](AccountApi.md#orgInvitationsListPending) | **GET** /v0.1/orgs/{org_name}/invitations | 
[**orgInvitationsReject**](AccountApi.md#orgInvitationsReject) | **POST** /v0.1/user/invitations/orgs/{invitation_token}/reject | 
[**orgInvitationsSendNewInvitation**](AccountApi.md#orgInvitationsSendNewInvitation) | **POST** /v0.1/orgs/{org_name}/invitations/{email}/resend | 
[**orgInvitationsUpdate**](AccountApi.md#orgInvitationsUpdate) | **PATCH** /v0.1/orgs/{org_name}/invitations/{email} | 
[**organizationDeleteAvatar**](AccountApi.md#organizationDeleteAvatar) | **DELETE** /v0.1/orgs/{org_name}/avatar | 
[**organizationUpdateAvatar**](AccountApi.md#organizationUpdateAvatar) | **POST** /v0.1/orgs/{org_name}/avatar | 
[**organizationsCreateOrUpdate**](AccountApi.md#organizationsCreateOrUpdate) | **POST** /v0.1/orgs | 
[**organizationsDelete**](AccountApi.md#organizationsDelete) | **DELETE** /v0.1/orgs/{org_name} | 
[**organizationsGet**](AccountApi.md#organizationsGet) | **GET** /v0.1/orgs/{org_name} | 
[**organizationsList**](AccountApi.md#organizationsList) | **GET** /v0.1/orgs | 
[**organizationsListAdministered**](AccountApi.md#organizationsListAdministered) | **GET** /v0.1/administeredOrgs | 
[**organizationsUpdate**](AccountApi.md#organizationsUpdate) | **PATCH** /v0.1/orgs/{org_name} | 
[**sharedconnectionConnections**](AccountApi.md#sharedconnectionConnections) | **GET** /v0.1/user/export/serviceConnections | 
[**teamsAddApp**](AccountApi.md#teamsAddApp) | **POST** /v0.1/orgs/{org_name}/teams/{team_name}/apps | 
[**teamsAddUser**](AccountApi.md#teamsAddUser) | **POST** /v0.1/orgs/{org_name}/teams/{team_name}/users | 
[**teamsCreateTeam**](AccountApi.md#teamsCreateTeam) | **POST** /v0.1/orgs/{org_name}/teams | 
[**teamsDelete**](AccountApi.md#teamsDelete) | **DELETE** /v0.1/orgs/{org_name}/teams/{team_name} | 
[**teamsGetTeam**](AccountApi.md#teamsGetTeam) | **GET** /v0.1/orgs/{org_name}/teams/{team_name} | 
[**teamsGetUsers**](AccountApi.md#teamsGetUsers) | **GET** /v0.1/orgs/{org_name}/teams/{team_name}/users | 
[**teamsListAll**](AccountApi.md#teamsListAll) | **GET** /v0.1/orgs/{org_name}/teams | 
[**teamsListApps**](AccountApi.md#teamsListApps) | **GET** /v0.1/orgs/{org_name}/teams/{team_name}/apps | 
[**teamsRemoveApp**](AccountApi.md#teamsRemoveApp) | **DELETE** /v0.1/orgs/{org_name}/teams/{team_name}/apps/{app_name} | 
[**teamsRemoveUser**](AccountApi.md#teamsRemoveUser) | **DELETE** /v0.1/orgs/{org_name}/teams/{team_name}/users/{user_name} | 
[**teamsUpdate**](AccountApi.md#teamsUpdate) | **PATCH** /v0.1/orgs/{org_name}/teams/{team_name} | 
[**teamsUpdatePermissions**](AccountApi.md#teamsUpdatePermissions) | **PATCH** /v0.1/orgs/{org_name}/teams/{team_name}/apps/{app_name} | 
[**userApiTokensDelete**](AccountApi.md#userApiTokensDelete) | **DELETE** /v0.1/api_tokens/{api_token_id} | 
[**userApiTokensList**](AccountApi.md#userApiTokensList) | **GET** /v0.1/api_tokens | 
[**userApiTokensNew**](AccountApi.md#userApiTokensNew) | **POST** /v0.1/api_tokens | 
[**usersGet**](AccountApi.md#usersGet) | **GET** /v0.1/user | 
[**usersGetForOrg**](AccountApi.md#usersGetForOrg) | **GET** /v0.1/orgs/{org_name}/users/{user_name} | 
[**usersGetUserMetadata**](AccountApi.md#usersGetUserMetadata) | **GET** /v0.1/user/metadata/optimizely | 
[**usersList**](AccountApi.md#usersList) | **GET** /v0.1/apps/{owner_name}/{app_name}/users | 
[**usersListForOrg**](AccountApi.md#usersListForOrg) | **GET** /v0.1/orgs/{org_name}/users | 
[**usersRemoveFromOrg**](AccountApi.md#usersRemoveFromOrg) | **DELETE** /v0.1/orgs/{org_name}/users/{user_name} | 
[**usersUpdate**](AccountApi.md#usersUpdate) | **PATCH** /v0.1/user | 
[**usersUpdateOrgRole**](AccountApi.md#usersUpdateOrgRole) | **PATCH** /v0.1/orgs/{org_name}/users/{user_name} | 



## appApiTokensDelete

> appApiTokensDelete(ownerName, appName, apiTokenId)



Delete the App Api Token object with the specific ID

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let apiTokenId = "apiTokenId_example"; // String | The unique ID (UUID) of the api token
apiInstance.appApiTokensDelete(ownerName, appName, apiTokenId, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **apiTokenId** | **String**| The unique ID (UUID) of the api token | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appApiTokensList

> [UserApiTokensList200ResponseInner] appApiTokensList(ownerName, appName)



Returns App API tokens for the app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.appApiTokensList(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[UserApiTokensList200ResponseInner]**](UserApiTokensList200ResponseInner.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appApiTokensNew

> UserApiTokensNew201Response appApiTokensNew(ownerName, appName, opts)



Creates a new App API token

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'userApiTokensNewRequest': new AppCenterClient.UserApiTokensNewRequest() // UserApiTokensNewRequest | Description of the token
};
apiInstance.appApiTokensNew(ownerName, appName, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **userApiTokensNewRequest** | [**UserApiTokensNewRequest**](UserApiTokensNewRequest.md)| Description of the token | [optional] 

### Return type

[**UserApiTokensNew201Response**](UserApiTokensNew201Response.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appInvitationsAccept

> appInvitationsAccept(invitationToken, opts)



Accepts a pending invitation for the specified user

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let invitationToken = "invitationToken_example"; // String | The app invitation token that was sent to the user
let opts = {
  'body': {key: null} // Object | allow empty body for custom http-client lib
};
apiInstance.appInvitationsAccept(invitationToken, opts, (error, data, response) => {
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
 **invitationToken** | **String**| The app invitation token that was sent to the user | 
 **body** | **Object**| allow empty body for custom http-client lib | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appInvitationsCreate

> appInvitationsCreate(ownerName, appName, opts)



Invites a new or existing user to an app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'appInvitationsCreateRequest': new AppCenterClient.AppInvitationsCreateRequest() // AppInvitationsCreateRequest | The email of the user to invite
};
apiInstance.appInvitationsCreate(ownerName, appName, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **appInvitationsCreateRequest** | [**AppInvitationsCreateRequest**](AppInvitationsCreateRequest.md)| The email of the user to invite | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appInvitationsCreateByEmail

> appInvitationsCreateByEmail(ownerName, appName, userEmail, opts)



Invites a new or existing user to an app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let userEmail = "userEmail_example"; // String | The email of the user to invite
let opts = {
  'appInvitationsCreateByEmailRequest': new AppCenterClient.AppInvitationsCreateByEmailRequest() // AppInvitationsCreateByEmailRequest | The role of the user to be added
};
apiInstance.appInvitationsCreateByEmail(ownerName, appName, userEmail, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **userEmail** | **String**| The email of the user to invite | 
 **appInvitationsCreateByEmailRequest** | [**AppInvitationsCreateByEmailRequest**](AppInvitationsCreateByEmailRequest.md)| The role of the user to be added | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appInvitationsDelete

> appInvitationsDelete(ownerName, appName, userEmail)



Removes a user&#39;s invitation to an app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let userEmail = "userEmail_example"; // String | The email of the user to invite
apiInstance.appInvitationsDelete(ownerName, appName, userEmail, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **userEmail** | **String**| The email of the user to invite | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appInvitationsList

> AppInvitationsList200Response appInvitationsList(ownerName, appName)



Gets the pending invitations for the app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.appInvitationsList(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**AppInvitationsList200Response**](AppInvitationsList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appInvitationsReject

> appInvitationsReject(invitationToken, opts)



Rejects a pending invitation for the specified user

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let invitationToken = "invitationToken_example"; // String | The app invitation token that was sent to the user
let opts = {
  'body': {key: null} // Object | allow empty body for custom http-client lib
};
apiInstance.appInvitationsReject(invitationToken, opts, (error, data, response) => {
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
 **invitationToken** | **String**| The app invitation token that was sent to the user | 
 **body** | **Object**| allow empty body for custom http-client lib | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appInvitationsUpdatePermissions

> appInvitationsUpdatePermissions(ownerName, appName, userEmail, appInvitationsUpdatePermissionsRequest)



Update pending invitation permission

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let userEmail = "userEmail_example"; // String | The email of the user to invite
let appInvitationsUpdatePermissionsRequest = new AppCenterClient.AppInvitationsUpdatePermissionsRequest(); // AppInvitationsUpdatePermissionsRequest | The value to update the user permission in the invite.
apiInstance.appInvitationsUpdatePermissions(ownerName, appName, userEmail, appInvitationsUpdatePermissionsRequest, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **userEmail** | **String**| The email of the user to invite | 
 **appInvitationsUpdatePermissionsRequest** | [**AppInvitationsUpdatePermissionsRequest**](AppInvitationsUpdatePermissionsRequest.md)| The value to update the user permission in the invite. | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsCreate

> AppsList200ResponseInner appsCreate(appsCreateRequest)



Creates a new app and returns it to the caller

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let appsCreateRequest = new AppCenterClient.AppsCreateRequest(); // AppsCreateRequest | The data for the app
apiInstance.appsCreate(appsCreateRequest, (error, data, response) => {
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
 **appsCreateRequest** | [**AppsCreateRequest**](AppsCreateRequest.md)| The data for the app | 

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsCreateForOrg

> AppsList200ResponseInner appsCreateForOrg(orgName, appsCreateRequest)



Creates a new app for the organization and returns it to the caller

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let appsCreateRequest = new AppCenterClient.AppsCreateRequest(); // AppsCreateRequest | The data for the app
apiInstance.appsCreateForOrg(orgName, appsCreateRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **appsCreateRequest** | [**AppsCreateRequest**](AppsCreateRequest.md)| The data for the app | 

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsDelete

> appsDelete(appName, ownerName)



Delete an app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let appName = "appName_example"; // String | The name of the application
let ownerName = "ownerName_example"; // String | The name of the owner
apiInstance.appsDelete(appName, ownerName, (error, data, response) => {
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
 **appName** | **String**| The name of the application | 
 **ownerName** | **String**| The name of the owner | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsDeleteAvatar

> AppsList200ResponseInner appsDeleteAvatar(ownerName, appName)



Deletes the uploaded app avatar

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.appsDeleteAvatar(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGet

> AppsList200ResponseInner appsGet(ownerName, appName)



Return a specific app with the given app name which belongs to the given owner.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.appsGet(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetForOrgUser

> [AppsList200ResponseInner] appsGetForOrgUser(orgName, userName)



Get a user apps information from an organization by name

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let userName = "userName_example"; // String | The slug name of the user
apiInstance.appsGetForOrgUser(orgName, userName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **userName** | **String**| The slug name of the user | 

### Return type

[**[AppsList200ResponseInner]**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetTeams

> [AppsGetTeams200ResponseInner] appsGetTeams(appName, ownerName)



Returns the details of all teams that have access to the app.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let appName = "appName_example"; // String | The name of the application
let ownerName = "ownerName_example"; // String | The name of the owner
apiInstance.appsGetTeams(appName, ownerName, (error, data, response) => {
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
 **appName** | **String**| The name of the application | 
 **ownerName** | **String**| The name of the owner | 

### Return type

[**[AppsGetTeams200ResponseInner]**](AppsGetTeams200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsList

> [AppsList200ResponseInner] appsList(opts)



Returns a list of apps

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let opts = {
  'orderBy': "orderBy_example" // String | The name of the attribute by which to order the response by. By default, apps are in order of creation. All results are ordered in ascending order.
};
apiInstance.appsList(opts, (error, data, response) => {
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
 **orderBy** | **String**| The name of the attribute by which to order the response by. By default, apps are in order of creation. All results are ordered in ascending order. | [optional] 

### Return type

[**[AppsList200ResponseInner]**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListForOrg

> [AppsList200ResponseInner] appsListForOrg(orgName)



Returns a list of apps for the organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
apiInstance.appsListForOrg(orgName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 

### Return type

[**[AppsList200ResponseInner]**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListTesters

> [AppInvitationsList200ResponseInvitedBy] appsListTesters(ownerName, appName)



Returns the testers associated with the app specified with the given app name which belongs to the given owner.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.appsListTesters(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[AppInvitationsList200ResponseInvitedBy]**](AppInvitationsList200ResponseInvitedBy.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsRemoveUser

> appsRemoveUser(ownerName, appName, userEmail)



Removes the user from the app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let userEmail = "userEmail_example"; // String | The user email of the user to delete
apiInstance.appsRemoveUser(ownerName, appName, userEmail, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **userEmail** | **String**| The user email of the user to delete | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsTransferOwnership

> AppsList200ResponseInner appsTransferOwnership(ownerName, appName, destinationOwnerName, opts)



Transfers ownership of an app to a different user or organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let destinationOwnerName = "destinationOwnerName_example"; // String | The name of the owner (user or organization) to which the app is being transferred
let opts = {
  'body': {key: null} // Object | allow empty body for custom http-client lib
};
apiInstance.appsTransferOwnership(ownerName, appName, destinationOwnerName, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **destinationOwnerName** | **String**| The name of the owner (user or organization) to which the app is being transferred | 
 **body** | **Object**| allow empty body for custom http-client lib | [optional] 

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream
- **Accept**: application/json


## appsTransferToOrg

> OrganizationsListAdministered200ResponseOrganizations appsTransferToOrg(ownerName, appName, opts)



Transfers ownership of an app to a new organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'body': {key: null} // Object | allow empty body for custom http-client lib
};
apiInstance.appsTransferToOrg(ownerName, appName, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **body** | **Object**| allow empty body for custom http-client lib | [optional] 

### Return type

[**OrganizationsListAdministered200ResponseOrganizations**](OrganizationsListAdministered200ResponseOrganizations.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsUpdate

> AppsList200ResponseInner appsUpdate(appName, ownerName, opts)



Partially updates a single app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let appName = "appName_example"; // String | The name of the application
let ownerName = "ownerName_example"; // String | The name of the owner
let opts = {
  'appsUpdateRequest': new AppCenterClient.AppsUpdateRequest() // AppsUpdateRequest | The partial data for the app
};
apiInstance.appsUpdate(appName, ownerName, opts, (error, data, response) => {
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
 **appName** | **String**| The name of the application | 
 **ownerName** | **String**| The name of the owner | 
 **appsUpdateRequest** | [**AppsUpdateRequest**](AppsUpdateRequest.md)| The partial data for the app | [optional] 

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsUpdateAvatar

> AppsList200ResponseInner appsUpdateAvatar(ownerName, appName, opts)



Sets the app avatar

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'avatar': "/path/to/file" // File | The image for an app avatar to upload.
};
apiInstance.appsUpdateAvatar(ownerName, appName, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **avatar** | **File**| The image for an app avatar to upload. | [optional] 

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## appsUpdateUserPermissions

> appsUpdateUserPermissions(ownerName, appName, userEmail, appsUpdateUserPermissionsRequest)



Update user permission for the app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let userEmail = "userEmail_example"; // String | The user email of the user to patch
let appsUpdateUserPermissionsRequest = new AppCenterClient.AppsUpdateUserPermissionsRequest(); // AppsUpdateUserPermissionsRequest | The value to update the user permission for the app.
apiInstance.appsUpdateUserPermissions(ownerName, appName, userEmail, appsUpdateUserPermissionsRequest, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **userEmail** | **String**| The user email of the user to patch | 
 **appsUpdateUserPermissionsRequest** | [**AppsUpdateUserPermissionsRequest**](AppsUpdateUserPermissionsRequest.md)| The value to update the user permission for the app. | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## azureSubscriptionDeleteForApp

> azureSubscriptionDeleteForApp(azureSubscriptionId, ownerName, appName)



Delete the azure subscriptions for the app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let azureSubscriptionId = "azureSubscriptionId_example"; // String | The unique ID (UUID) of the azure subscription
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.azureSubscriptionDeleteForApp(azureSubscriptionId, ownerName, appName, (error, data, response) => {
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
 **azureSubscriptionId** | **String**| The unique ID (UUID) of the azure subscription | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## azureSubscriptionLinkForApp

> azureSubscriptionLinkForApp(ownerName, appName, azureSubscriptionLinkForAppRequest)



Link azure subscription to an app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let azureSubscriptionLinkForAppRequest = new AppCenterClient.AzureSubscriptionLinkForAppRequest(); // AzureSubscriptionLinkForAppRequest | The azure subscription data needed to be link to the app.
apiInstance.azureSubscriptionLinkForApp(ownerName, appName, azureSubscriptionLinkForAppRequest, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **azureSubscriptionLinkForAppRequest** | [**AzureSubscriptionLinkForAppRequest**](AzureSubscriptionLinkForAppRequest.md)| The azure subscription data needed to be link to the app. | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## azureSubscriptionListForApp

> [AppsList200ResponseInnerAllOfAzureSubscription] azureSubscriptionListForApp(ownerName, appName)



Returns a list of azure subscriptions for the app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.azureSubscriptionListForApp(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[AppsList200ResponseInnerAllOfAzureSubscription]**](AppsList200ResponseInnerAllOfAzureSubscription.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## azureSubscriptionListForOrg

> [AppsList200ResponseInnerAllOfAzureSubscription] azureSubscriptionListForOrg(orgName)



Returns a list of azure subscriptions for the organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
apiInstance.azureSubscriptionListForOrg(orgName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 

### Return type

[**[AppsList200ResponseInnerAllOfAzureSubscription]**](AppsList200ResponseInnerAllOfAzureSubscription.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## azureSubscriptionListForUser

> [AppsList200ResponseInnerAllOfAzureSubscription] azureSubscriptionListForUser()



Returns a list of azure subscriptions for the user

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
apiInstance.azureSubscriptionListForUser((error, data, response) => {
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

[**[AppsList200ResponseInnerAllOfAzureSubscription]**](AppsList200ResponseInnerAllOfAzureSubscription.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## distributionGroupInvitationsAcceptAll

> distributionGroupInvitationsAcceptAll(opts)



Accepts all pending invitations to distribution groups for the specified user

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let opts = {
  'body': {key: null} // Object | allow empty body for custom http-client lib
};
apiInstance.distributionGroupInvitationsAcceptAll(opts, (error, data, response) => {
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
 **body** | **Object**| allow empty body for custom http-client lib | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## distributionGroupsAddApps

> distributionGroupsAddApps(orgName, distributionGroupName, distributionGroupsAddAppsRequest)



Add apps to distribution group in an org

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
let distributionGroupsAddAppsRequest = new AppCenterClient.DistributionGroupsAddAppsRequest(); // DistributionGroupsAddAppsRequest | The name of the apps to be added to the distribution group. The apps have to be owned by the organization.
apiInstance.distributionGroupsAddApps(orgName, distributionGroupName, distributionGroupsAddAppsRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **distributionGroupName** | **String**| The name of the distribution group | 
 **distributionGroupsAddAppsRequest** | [**DistributionGroupsAddAppsRequest**](DistributionGroupsAddAppsRequest.md)| The name of the apps to be added to the distribution group. The apps have to be owned by the organization. | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## distributionGroupsAddUser

> [DistributionGroupsAddUser200ResponseInner] distributionGroupsAddUser(ownerName, appName, distributionGroupName, distributionGroupsAddUserRequest)



Adds the members to the specified distribution group

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
let distributionGroupsAddUserRequest = new AppCenterClient.DistributionGroupsAddUserRequest(); // DistributionGroupsAddUserRequest | The list of members to add
apiInstance.distributionGroupsAddUser(ownerName, appName, distributionGroupName, distributionGroupsAddUserRequest, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **distributionGroupName** | **String**| The name of the distribution group | 
 **distributionGroupsAddUserRequest** | [**DistributionGroupsAddUserRequest**](DistributionGroupsAddUserRequest.md)| The list of members to add | 

### Return type

[**[DistributionGroupsAddUser200ResponseInner]**](DistributionGroupsAddUser200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## distributionGroupsAddUsersForOrg

> [DistributionGroupsAddUser200ResponseInner] distributionGroupsAddUsersForOrg(orgName, distributionGroupName, distributionGroupsAddUserRequest)



Accepts an array of user email addresses to get added to the specified group

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
let distributionGroupsAddUserRequest = new AppCenterClient.DistributionGroupsAddUserRequest(); // DistributionGroupsAddUserRequest | list of user email addresses that should get added as members to the specified group
apiInstance.distributionGroupsAddUsersForOrg(orgName, distributionGroupName, distributionGroupsAddUserRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **distributionGroupName** | **String**| The name of the distribution group | 
 **distributionGroupsAddUserRequest** | [**DistributionGroupsAddUserRequest**](DistributionGroupsAddUserRequest.md)| list of user email addresses that should get added as members to the specified group | 

### Return type

[**[DistributionGroupsAddUser200ResponseInner]**](DistributionGroupsAddUser200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## distributionGroupsBulkDeleteApps

> distributionGroupsBulkDeleteApps(orgName, distributionGroupName, distributionGroupsBulkDeleteAppsRequest)



Delete apps from distribution group in an org

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
let distributionGroupsBulkDeleteAppsRequest = new AppCenterClient.DistributionGroupsBulkDeleteAppsRequest(); // DistributionGroupsBulkDeleteAppsRequest | The name of the apps to be deleted from the distribution group. The apps have to be owned by the organization.
apiInstance.distributionGroupsBulkDeleteApps(orgName, distributionGroupName, distributionGroupsBulkDeleteAppsRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **distributionGroupName** | **String**| The name of the distribution group | 
 **distributionGroupsBulkDeleteAppsRequest** | [**DistributionGroupsBulkDeleteAppsRequest**](DistributionGroupsBulkDeleteAppsRequest.md)| The name of the apps to be deleted from the distribution group. The apps have to be owned by the organization. | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## distributionGroupsBulkDeleteUsers

> distributionGroupsBulkDeleteUsers(orgName, distributionGroupName, distributionGroupsAddUserRequest)



Delete testers from distribution group in an org

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
let distributionGroupsAddUserRequest = new AppCenterClient.DistributionGroupsAddUserRequest(); // DistributionGroupsAddUserRequest | The list of members to add
apiInstance.distributionGroupsBulkDeleteUsers(orgName, distributionGroupName, distributionGroupsAddUserRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **distributionGroupName** | **String**| The name of the distribution group | 
 **distributionGroupsAddUserRequest** | [**DistributionGroupsAddUserRequest**](DistributionGroupsAddUserRequest.md)| The list of members to add | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## distributionGroupsCreate

> DistributionGroupsList200ResponseInner distributionGroupsCreate(ownerName, appName, distributionGroupsCreateRequest)



Creates a new distribution group and returns it to the caller

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let distributionGroupsCreateRequest = new AppCenterClient.DistributionGroupsCreateRequest(); // DistributionGroupsCreateRequest | The attributes to update for the distribution group
apiInstance.distributionGroupsCreate(ownerName, appName, distributionGroupsCreateRequest, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **distributionGroupsCreateRequest** | [**DistributionGroupsCreateRequest**](DistributionGroupsCreateRequest.md)| The attributes to update for the distribution group | 

### Return type

[**DistributionGroupsList200ResponseInner**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## distributionGroupsCreateForOrg

> DistributionGroupsList200ResponseInner distributionGroupsCreateForOrg(orgName, distributionGroupsCreateRequest)



Creates a disribution goup which can be shared across apps under an organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let distributionGroupsCreateRequest = new AppCenterClient.DistributionGroupsCreateRequest(); // DistributionGroupsCreateRequest | The attributes to update for the distribution group
apiInstance.distributionGroupsCreateForOrg(orgName, distributionGroupsCreateRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **distributionGroupsCreateRequest** | [**DistributionGroupsCreateRequest**](DistributionGroupsCreateRequest.md)| The attributes to update for the distribution group | 

### Return type

[**DistributionGroupsList200ResponseInner**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## distributionGroupsDelete

> distributionGroupsDelete(appName, ownerName, distributionGroupName)



Deletes a distribution group

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let appName = "appName_example"; // String | The name of the application
let ownerName = "ownerName_example"; // String | The name of the owner
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
apiInstance.distributionGroupsDelete(appName, ownerName, distributionGroupName, (error, data, response) => {
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
 **appName** | **String**| The name of the application | 
 **ownerName** | **String**| The name of the owner | 
 **distributionGroupName** | **String**| The name of the distribution group | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## distributionGroupsDeleteForOrg

> distributionGroupsDeleteForOrg(orgName, distributionGroupName)



Deletes a single distribution group from an org with a given distribution group name

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
apiInstance.distributionGroupsDeleteForOrg(orgName, distributionGroupName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **distributionGroupName** | **String**| The name of the distribution group | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## distributionGroupsDetailsForOrg

> [DistributionGroupsDetailsForOrg200ResponseInner] distributionGroupsDetailsForOrg(orgName, opts)



Returns a list of distribution groups with details for an organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let opts = {
  'appsLimit': 3.4 // Number | The max number of apps to include in the response
};
apiInstance.distributionGroupsDetailsForOrg(orgName, opts, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **appsLimit** | **Number**| The max number of apps to include in the response | [optional] 

### Return type

[**[DistributionGroupsDetailsForOrg200ResponseInner]**](DistributionGroupsDetailsForOrg200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## distributionGroupsGet

> DistributionGroupsList200ResponseInner distributionGroupsGet(ownerName, appName, distributionGroupName)



Returns a single distribution group for a given distribution group name

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
apiInstance.distributionGroupsGet(ownerName, appName, distributionGroupName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **distributionGroupName** | **String**| The name of the distribution group | 

### Return type

[**DistributionGroupsList200ResponseInner**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## distributionGroupsGetApps

> [DistributionGroupsGetApps200ResponseInner] distributionGroupsGetApps(orgName, distributionGroupName)



Get apps from a distribution group in an org

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
apiInstance.distributionGroupsGetApps(orgName, distributionGroupName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **distributionGroupName** | **String**| The name of the distribution group | 

### Return type

[**[DistributionGroupsGetApps200ResponseInner]**](DistributionGroupsGetApps200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## distributionGroupsGetForOrg

> DistributionGroupsList200ResponseInner distributionGroupsGetForOrg(orgName, distributionGroupName)



Returns a single distribution group in org for a given distribution group name

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
apiInstance.distributionGroupsGetForOrg(orgName, distributionGroupName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **distributionGroupName** | **String**| The name of the distribution group | 

### Return type

[**DistributionGroupsList200ResponseInner**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## distributionGroupsList

> [DistributionGroupsList200ResponseInner] distributionGroupsList(ownerName, appName)



Returns a list of distribution groups in the app specified

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.distributionGroupsList(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[DistributionGroupsList200ResponseInner]**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## distributionGroupsListAllTestersForOrg

> [DistributionGroupsListAllTestersForOrg200ResponseInner] distributionGroupsListAllTestersForOrg(orgName)



Returns a unique list of users including the whole organization members plus testers in any shared group of that org

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
apiInstance.distributionGroupsListAllTestersForOrg(orgName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 

### Return type

[**[DistributionGroupsListAllTestersForOrg200ResponseInner]**](DistributionGroupsListAllTestersForOrg200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## distributionGroupsListForOrg

> [DistributionGroupsList200ResponseInner] distributionGroupsListForOrg(orgName)



Returns a list of distribution groups in the org specified

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
apiInstance.distributionGroupsListForOrg(orgName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 

### Return type

[**[DistributionGroupsList200ResponseInner]**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## distributionGroupsListUsers

> [DistributionGroupsListUsers200ResponseInner] distributionGroupsListUsers(ownerName, appName, distributionGroupName, opts)



Returns a list of member details in the distribution group specified

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
let opts = {
  'excludePendingInvitations': true // Boolean | Whether to exclude pending invitations in the response
};
apiInstance.distributionGroupsListUsers(ownerName, appName, distributionGroupName, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **distributionGroupName** | **String**| The name of the distribution group | 
 **excludePendingInvitations** | **Boolean**| Whether to exclude pending invitations in the response | [optional] 

### Return type

[**[DistributionGroupsListUsers200ResponseInner]**](DistributionGroupsListUsers200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## distributionGroupsListUsersForOrg

> [DistributionGroupsListUsers200ResponseInner] distributionGroupsListUsersForOrg(orgName, distributionGroupName)



Returns a list of member in the distribution group specified

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
apiInstance.distributionGroupsListUsersForOrg(orgName, distributionGroupName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **distributionGroupName** | **String**| The name of the distribution group | 

### Return type

[**[DistributionGroupsListUsers200ResponseInner]**](DistributionGroupsListUsers200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## distributionGroupsPatchForOrg

> DistributionGroupsList200ResponseInner distributionGroupsPatchForOrg(orgName, distributionGroupName, opts)



Update one given distribution group name in an org

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
let opts = {
  'distributionGroupsUpdateRequest': new AppCenterClient.DistributionGroupsUpdateRequest() // DistributionGroupsUpdateRequest | The attributes to update for the distribution group
};
apiInstance.distributionGroupsPatchForOrg(orgName, distributionGroupName, opts, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **distributionGroupName** | **String**| The name of the distribution group | 
 **distributionGroupsUpdateRequest** | [**DistributionGroupsUpdateRequest**](DistributionGroupsUpdateRequest.md)| The attributes to update for the distribution group | [optional] 

### Return type

[**DistributionGroupsList200ResponseInner**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## distributionGroupsRemoveUser

> [DistributionGroupsRemoveUser200ResponseInner] distributionGroupsRemoveUser(ownerName, appName, distributionGroupName, distributionGroupsAddUserRequest)



Remove the users from the distribution group

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
let distributionGroupsAddUserRequest = new AppCenterClient.DistributionGroupsAddUserRequest(); // DistributionGroupsAddUserRequest | The list of members to add
apiInstance.distributionGroupsRemoveUser(ownerName, appName, distributionGroupName, distributionGroupsAddUserRequest, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **distributionGroupName** | **String**| The name of the distribution group | 
 **distributionGroupsAddUserRequest** | [**DistributionGroupsAddUserRequest**](DistributionGroupsAddUserRequest.md)| The list of members to add | 

### Return type

[**[DistributionGroupsRemoveUser200ResponseInner]**](DistributionGroupsRemoveUser200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## distributionGroupsResendInvite

> distributionGroupsResendInvite(ownerName, appName, distributionGroupName, distributionGroupsAddUserRequest)



Resend distribution group app invite notification to previously invited testers

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
let distributionGroupsAddUserRequest = new AppCenterClient.DistributionGroupsAddUserRequest(); // DistributionGroupsAddUserRequest | The list of members to add
apiInstance.distributionGroupsResendInvite(ownerName, appName, distributionGroupName, distributionGroupsAddUserRequest, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **distributionGroupName** | **String**| The name of the distribution group | 
 **distributionGroupsAddUserRequest** | [**DistributionGroupsAddUserRequest**](DistributionGroupsAddUserRequest.md)| The list of members to add | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## distributionGroupsResendSharedInvite

> distributionGroupsResendSharedInvite(orgName, distributionGroupName, distributionGroupsAddUserRequest)



Resend shared distribution group invite notification to previously invited testers

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
let distributionGroupsAddUserRequest = new AppCenterClient.DistributionGroupsAddUserRequest(); // DistributionGroupsAddUserRequest | The list of members to add
apiInstance.distributionGroupsResendSharedInvite(orgName, distributionGroupName, distributionGroupsAddUserRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **distributionGroupName** | **String**| The name of the distribution group | 
 **distributionGroupsAddUserRequest** | [**DistributionGroupsAddUserRequest**](DistributionGroupsAddUserRequest.md)| The list of members to add | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## distributionGroupsUpdate

> DistributionGroupsList200ResponseInner distributionGroupsUpdate(ownerName, appName, distributionGroupName, distributionGroupsUpdateRequest)



Updates the attributes of distribution group

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
let distributionGroupsUpdateRequest = new AppCenterClient.DistributionGroupsUpdateRequest(); // DistributionGroupsUpdateRequest | The attributes to update for the distribution group
apiInstance.distributionGroupsUpdate(ownerName, appName, distributionGroupName, distributionGroupsUpdateRequest, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **distributionGroupName** | **String**| The name of the distribution group | 
 **distributionGroupsUpdateRequest** | [**DistributionGroupsUpdateRequest**](DistributionGroupsUpdateRequest.md)| The attributes to update for the distribution group | 

### Return type

[**DistributionGroupsList200ResponseInner**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## invitationsSent

> [InvitationsSent200ResponseInner] invitationsSent()



Returns all invitations sent by the caller

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
apiInstance.invitationsSent((error, data, response) => {
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

[**[InvitationsSent200ResponseInner]**](InvitationsSent200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgInvitations

> orgInvitations(orgName, email, opts)



Removes a user&#39;s invitation to an organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let email = "email_example"; // String | The email address of the user to send the password reset mail to.
let opts = {
  'body': {key: null} // Object | allow empty body for custom http-client lib
};
apiInstance.orgInvitations(orgName, email, opts, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **email** | **String**| The email address of the user to send the password reset mail to. | 
 **body** | **Object**| allow empty body for custom http-client lib | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orgInvitationsAccept

> orgInvitationsAccept(invitationToken, opts)



Accepts a pending organization invitation for the specified user

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let invitationToken = "invitationToken_example"; // String | The app invitation token that was sent to the user
let opts = {
  'body': {key: null} // Object | allow empty body for custom http-client lib
};
apiInstance.orgInvitationsAccept(invitationToken, opts, (error, data, response) => {
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
 **invitationToken** | **String**| The app invitation token that was sent to the user | 
 **body** | **Object**| allow empty body for custom http-client lib | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orgInvitationsCreate

> orgInvitationsCreate(orgName, appInvitationsCreateRequest)



Invites a new or existing user to an organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let appInvitationsCreateRequest = new AppCenterClient.AppInvitationsCreateRequest(); // AppInvitationsCreateRequest | The email of the user to invite
apiInstance.orgInvitationsCreate(orgName, appInvitationsCreateRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **appInvitationsCreateRequest** | [**AppInvitationsCreateRequest**](AppInvitationsCreateRequest.md)| The email of the user to invite | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orgInvitationsDelete

> orgInvitationsDelete(orgName, orgInvitationsDeleteRequest)



Removes a user&#39;s invitation to an organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let orgInvitationsDeleteRequest = new AppCenterClient.OrgInvitationsDeleteRequest(); // OrgInvitationsDeleteRequest | The email of the user whose invitation should be removed
apiInstance.orgInvitationsDelete(orgName, orgInvitationsDeleteRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **orgInvitationsDeleteRequest** | [**OrgInvitationsDeleteRequest**](OrgInvitationsDeleteRequest.md)| The email of the user whose invitation should be removed | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orgInvitationsListPending

> [OrgInvitationsListPending200ResponseInner] orgInvitationsListPending(orgName)



Gets the pending invitations for the organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
apiInstance.orgInvitationsListPending(orgName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 

### Return type

[**[OrgInvitationsListPending200ResponseInner]**](OrgInvitationsListPending200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgInvitationsReject

> orgInvitationsReject(invitationToken, opts)



Rejects a pending organization invitation

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let invitationToken = "invitationToken_example"; // String | The app invitation token that was sent to the user
let opts = {
  'body': {key: null} // Object | allow empty body for custom http-client lib
};
apiInstance.orgInvitationsReject(invitationToken, opts, (error, data, response) => {
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
 **invitationToken** | **String**| The app invitation token that was sent to the user | 
 **body** | **Object**| allow empty body for custom http-client lib | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orgInvitationsSendNewInvitation

> orgInvitationsSendNewInvitation(orgName, email, opts)



Cancels an existing organization invitation for the user and sends a new one

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let email = "email_example"; // String | The email address of the user to send the password reset mail to.
let opts = {
  'appInvitationsCreateByEmailRequest': new AppCenterClient.AppInvitationsCreateByEmailRequest() // AppInvitationsCreateByEmailRequest | The role of the user to be added
};
apiInstance.orgInvitationsSendNewInvitation(orgName, email, opts, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **email** | **String**| The email address of the user to send the password reset mail to. | 
 **appInvitationsCreateByEmailRequest** | [**AppInvitationsCreateByEmailRequest**](AppInvitationsCreateByEmailRequest.md)| The role of the user to be added | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orgInvitationsUpdate

> orgInvitationsUpdate(orgName, email, orgInvitationsUpdateRequest)



Allows the role of an invited user to be changed

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let email = "email_example"; // String | The email address of the user to send the password reset mail to.
let orgInvitationsUpdateRequest = new AppCenterClient.OrgInvitationsUpdateRequest(); // OrgInvitationsUpdateRequest | The new role of the user
apiInstance.orgInvitationsUpdate(orgName, email, orgInvitationsUpdateRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **email** | **String**| The email address of the user to send the password reset mail to. | 
 **orgInvitationsUpdateRequest** | [**OrgInvitationsUpdateRequest**](OrgInvitationsUpdateRequest.md)| The new role of the user | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## organizationDeleteAvatar

> OrganizationsListAdministered200ResponseOrganizations organizationDeleteAvatar(orgName)



Deletes the uploaded organization avatar

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
apiInstance.organizationDeleteAvatar(orgName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 

### Return type

[**OrganizationsListAdministered200ResponseOrganizations**](OrganizationsListAdministered200ResponseOrganizations.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organizationUpdateAvatar

> OrganizationsListAdministered200ResponseOrganizations organizationUpdateAvatar(orgName, opts)



Sets the organization avatar

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let opts = {
  'avatar': "/path/to/file" // File | The image for an Organization avatar to upload.
};
apiInstance.organizationUpdateAvatar(orgName, opts, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **avatar** | **File**| The image for an Organization avatar to upload. | [optional] 

### Return type

[**OrganizationsListAdministered200ResponseOrganizations**](OrganizationsListAdministered200ResponseOrganizations.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## organizationsCreateOrUpdate

> OrganizationsListAdministered200ResponseOrganizations organizationsCreateOrUpdate(organizationsCreateOrUpdateRequest)



Creates a new organization and returns it to the caller

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let organizationsCreateOrUpdateRequest = new AppCenterClient.OrganizationsCreateOrUpdateRequest(); // OrganizationsCreateOrUpdateRequest | The organization data
apiInstance.organizationsCreateOrUpdate(organizationsCreateOrUpdateRequest, (error, data, response) => {
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
 **organizationsCreateOrUpdateRequest** | [**OrganizationsCreateOrUpdateRequest**](OrganizationsCreateOrUpdateRequest.md)| The organization data | 

### Return type

[**OrganizationsListAdministered200ResponseOrganizations**](OrganizationsListAdministered200ResponseOrganizations.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## organizationsDelete

> organizationsDelete(orgName)



Deletes a single organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
apiInstance.organizationsDelete(orgName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organizationsGet

> OrganizationsListAdministered200ResponseOrganizations organizationsGet(orgName)



Returns the details of a single organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
apiInstance.organizationsGet(orgName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 

### Return type

[**OrganizationsListAdministered200ResponseOrganizations**](OrganizationsListAdministered200ResponseOrganizations.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organizationsList

> [OrganizationsList200ResponseInner] organizationsList()



Returns a list of organizations the requesting user has access to

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
apiInstance.organizationsList((error, data, response) => {
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

[**[OrganizationsList200ResponseInner]**](OrganizationsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organizationsListAdministered

> OrganizationsListAdministered200Response organizationsListAdministered()



Returns a list organizations in which the requesting user is an admin

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
apiInstance.organizationsListAdministered((error, data, response) => {
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

[**OrganizationsListAdministered200Response**](OrganizationsListAdministered200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organizationsUpdate

> OrganizationsListAdministered200ResponseOrganizations organizationsUpdate(orgName, organizationsUpdateRequest)



Returns a list of organizations the requesting user has access to

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let organizationsUpdateRequest = new AppCenterClient.OrganizationsUpdateRequest(); // OrganizationsUpdateRequest | The data for the org
apiInstance.organizationsUpdate(orgName, organizationsUpdateRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **organizationsUpdateRequest** | [**OrganizationsUpdateRequest**](OrganizationsUpdateRequest.md)| The data for the org | 

### Return type

[**OrganizationsListAdministered200ResponseOrganizations**](OrganizationsListAdministered200ResponseOrganizations.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sharedconnectionConnections

> [SharedconnectionConnections200ResponseInner] sharedconnectionConnections()



Gets all service connections of the service type for GDPR export.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
apiInstance.sharedconnectionConnections((error, data, response) => {
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

[**[SharedconnectionConnections200ResponseInner]**](SharedconnectionConnections200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsAddApp

> TeamsListApps200ResponseInner teamsAddApp(orgName, teamName, distributionGroupsAddAppsRequestAppsInner)



Adds an app to a team

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let teamName = "teamName_example"; // String | The team's name
let distributionGroupsAddAppsRequestAppsInner = new AppCenterClient.DistributionGroupsAddAppsRequestAppsInner(); // DistributionGroupsAddAppsRequestAppsInner | The name of the app to be added to the team. The app has to be owned by the organization.
apiInstance.teamsAddApp(orgName, teamName, distributionGroupsAddAppsRequestAppsInner, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **teamName** | **String**| The team&#39;s name | 
 **distributionGroupsAddAppsRequestAppsInner** | [**DistributionGroupsAddAppsRequestAppsInner**](DistributionGroupsAddAppsRequestAppsInner.md)| The name of the app to be added to the team. The app has to be owned by the organization. | 

### Return type

[**TeamsListApps200ResponseInner**](TeamsListApps200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsAddUser

> TeamsGetUsers200Response teamsAddUser(orgName, teamName, orgInvitationsDeleteRequest)



Adds a new user to a team that is owned by an organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let teamName = "teamName_example"; // String | The team's name
let orgInvitationsDeleteRequest = new AppCenterClient.OrgInvitationsDeleteRequest(); // OrgInvitationsDeleteRequest | The email of the user to add to the team
apiInstance.teamsAddUser(orgName, teamName, orgInvitationsDeleteRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **teamName** | **String**| The team&#39;s name | 
 **orgInvitationsDeleteRequest** | [**OrgInvitationsDeleteRequest**](OrgInvitationsDeleteRequest.md)| The email of the user to add to the team | 

### Return type

[**TeamsGetUsers200Response**](TeamsGetUsers200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsCreateTeam

> [TeamsListAll200ResponseInner] teamsCreateTeam(orgName, teamsCreateTeamRequest)



Creates a team and returns it

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let teamsCreateTeamRequest = new AppCenterClient.TeamsCreateTeamRequest(); // TeamsCreateTeamRequest | The information used to create the team
apiInstance.teamsCreateTeam(orgName, teamsCreateTeamRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **teamsCreateTeamRequest** | [**TeamsCreateTeamRequest**](TeamsCreateTeamRequest.md)| The information used to create the team | 

### Return type

[**[TeamsListAll200ResponseInner]**](TeamsListAll200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsDelete

> teamsDelete(orgName, teamName)



Deletes a single team

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let teamName = "teamName_example"; // String | The team's name
apiInstance.teamsDelete(orgName, teamName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **teamName** | **String**| The team&#39;s name | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsGetTeam

> TeamsListAll200ResponseInner teamsGetTeam(orgName, teamName)



Returns the details of a single team

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let teamName = "teamName_example"; // String | The team's name
apiInstance.teamsGetTeam(orgName, teamName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **teamName** | **String**| The team&#39;s name | 

### Return type

[**TeamsListAll200ResponseInner**](TeamsListAll200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsGetUsers

> TeamsGetUsers200Response teamsGetUsers(orgName, teamName)



Returns the users of a team which is owned by an organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let teamName = "teamName_example"; // String | The team's name
apiInstance.teamsGetUsers(orgName, teamName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **teamName** | **String**| The team&#39;s name | 

### Return type

[**TeamsGetUsers200Response**](TeamsGetUsers200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListAll

> [TeamsListAll200ResponseInner] teamsListAll(orgName)



Returns the list of all teams in this org

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
apiInstance.teamsListAll(orgName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 

### Return type

[**[TeamsListAll200ResponseInner]**](TeamsListAll200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListApps

> [TeamsListApps200ResponseInner] teamsListApps(orgName, teamName)



Returns the apps a team has access to

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let teamName = "teamName_example"; // String | The team's name
apiInstance.teamsListApps(orgName, teamName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **teamName** | **String**| The team&#39;s name | 

### Return type

[**[TeamsListApps200ResponseInner]**](TeamsListApps200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsRemoveApp

> teamsRemoveApp(orgName, teamName, appName)



Removes an app from a team

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let teamName = "teamName_example"; // String | The team's name
let appName = "appName_example"; // String | The name of the application
apiInstance.teamsRemoveApp(orgName, teamName, appName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **teamName** | **String**| The team&#39;s name | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsRemoveUser

> teamsRemoveUser(orgName, teamName, userName)



Removes a user from a team that is owned by an organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let teamName = "teamName_example"; // String | The team's name
let userName = "userName_example"; // String | The slug name of the user
apiInstance.teamsRemoveUser(orgName, teamName, userName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **teamName** | **String**| The team&#39;s name | 
 **userName** | **String**| The slug name of the user | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsUpdate

> TeamsListAll200ResponseInner teamsUpdate(orgName, teamName, teamsUpdateRequest)



Updates a single team

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let teamName = "teamName_example"; // String | The team's name
let teamsUpdateRequest = new AppCenterClient.TeamsUpdateRequest(); // TeamsUpdateRequest | The information used to update the team
apiInstance.teamsUpdate(orgName, teamName, teamsUpdateRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **teamName** | **String**| The team&#39;s name | 
 **teamsUpdateRequest** | [**TeamsUpdateRequest**](TeamsUpdateRequest.md)| The information used to update the team | 

### Return type

[**TeamsListAll200ResponseInner**](TeamsListAll200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsUpdatePermissions

> TeamsListApps200ResponseInner teamsUpdatePermissions(orgName, teamName, appName, teamsUpdatePermissionsRequest)



Updates the permissions the team has to the app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let teamName = "teamName_example"; // String | The team's name
let appName = "appName_example"; // String | The name of the application
let teamsUpdatePermissionsRequest = new AppCenterClient.TeamsUpdatePermissionsRequest(); // TeamsUpdatePermissionsRequest | 
apiInstance.teamsUpdatePermissions(orgName, teamName, appName, teamsUpdatePermissionsRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **teamName** | **String**| The team&#39;s name | 
 **appName** | **String**| The name of the application | 
 **teamsUpdatePermissionsRequest** | [**TeamsUpdatePermissionsRequest**](TeamsUpdatePermissionsRequest.md)|  | 

### Return type

[**TeamsListApps200ResponseInner**](TeamsListApps200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## userApiTokensDelete

> userApiTokensDelete(apiTokenId)



Delete the user api_token object with the specific id

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new AppCenterClient.AccountApi();
let apiTokenId = "apiTokenId_example"; // String | The unique ID (UUID) of the api token
apiInstance.userApiTokensDelete(apiTokenId, (error, data, response) => {
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
 **apiTokenId** | **String**| The unique ID (UUID) of the api token | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userApiTokensList

> [UserApiTokensList200ResponseInner] userApiTokensList()



Returns api tokens for the authenticated user

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new AppCenterClient.AccountApi();
apiInstance.userApiTokensList((error, data, response) => {
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

[**[UserApiTokensList200ResponseInner]**](UserApiTokensList200ResponseInner.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userApiTokensNew

> UserApiTokensNew201Response userApiTokensNew(opts)



Creates a new User API token

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new AppCenterClient.AccountApi();
let opts = {
  'userApiTokensNewRequest': new AppCenterClient.UserApiTokensNewRequest() // UserApiTokensNewRequest | Description of the token
};
apiInstance.userApiTokensNew(opts, (error, data, response) => {
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
 **userApiTokensNewRequest** | [**UserApiTokensNewRequest**](UserApiTokensNewRequest.md)| Description of the token | [optional] 

### Return type

[**UserApiTokensNew201Response**](UserApiTokensNew201Response.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersGet

> AppInvitationsList200ResponseInvitedBy usersGet()



Returns the user profile data

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
apiInstance.usersGet((error, data, response) => {
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

[**AppInvitationsList200ResponseInvitedBy**](AppInvitationsList200ResponseInvitedBy.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGetForOrg

> UsersListForOrg200ResponseInner usersGetForOrg(orgName, userName)



Get a user information from an organization by name - if there is explicit permission return it, if not if not return highest implicit permission

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let userName = "userName_example"; // String | The slug name of the user
apiInstance.usersGetForOrg(orgName, userName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **userName** | **String**| The slug name of the user | 

### Return type

[**UsersListForOrg200ResponseInner**](UsersListForOrg200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGetUserMetadata

> UsersGetUserMetadata200Response usersGetUserMetadata()



### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
apiInstance.usersGetUserMetadata((error, data, response) => {
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

[**UsersGetUserMetadata200Response**](UsersGetUserMetadata200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersList

> [AppInvitationsList200ResponseInvitedBy] usersList(ownerName, appName)



Returns the users associated with the app specified with the given app name which belongs to the given owner.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.usersList(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[AppInvitationsList200ResponseInvitedBy]**](AppInvitationsList200ResponseInvitedBy.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersListForOrg

> [UsersListForOrg200ResponseInner] usersListForOrg(orgName)



Returns a list of users that belong to an organization

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
apiInstance.usersListForOrg(orgName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 

### Return type

[**[UsersListForOrg200ResponseInner]**](UsersListForOrg200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersRemoveFromOrg

> usersRemoveFromOrg(orgName, userName)



Removes a user from an organization.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let userName = "userName_example"; // String | The slug name of the user
apiInstance.usersRemoveFromOrg(orgName, userName, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **userName** | **String**| The slug name of the user | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUpdate

> AppInvitationsList200ResponseInvitedBy usersUpdate(usersUpdateRequest)



Updates the user profile and returns the updated user data

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let usersUpdateRequest = new AppCenterClient.UsersUpdateRequest(); // UsersUpdateRequest | The data for the created user
apiInstance.usersUpdate(usersUpdateRequest, (error, data, response) => {
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
 **usersUpdateRequest** | [**UsersUpdateRequest**](UsersUpdateRequest.md)| The data for the created user | 

### Return type

[**AppInvitationsList200ResponseInvitedBy**](AppInvitationsList200ResponseInvitedBy.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersUpdateOrgRole

> UsersListForOrg200ResponseInner usersUpdateOrgRole(orgName, userName, orgInvitationsUpdateRequest)



Updates the given organization user

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.AccountApi();
let orgName = "orgName_example"; // String | The organization's name
let userName = "userName_example"; // String | The slug name of the user
let orgInvitationsUpdateRequest = new AppCenterClient.OrgInvitationsUpdateRequest(); // OrgInvitationsUpdateRequest | 
apiInstance.usersUpdateOrgRole(orgName, userName, orgInvitationsUpdateRequest, (error, data, response) => {
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
 **orgName** | **String**| The organization&#39;s name | 
 **userName** | **String**| The slug name of the user | 
 **orgInvitationsUpdateRequest** | [**OrgInvitationsUpdateRequest**](OrgInvitationsUpdateRequest.md)|  | 

### Return type

[**UsersListForOrg200ResponseInner**](UsersListForOrg200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

