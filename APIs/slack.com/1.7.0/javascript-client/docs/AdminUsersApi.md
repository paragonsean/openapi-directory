# SlackWebApi.AdminUsersApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminUsersAssign**](AdminUsersApi.md#adminUsersAssign) | **POST** /admin.users.assign | 
[**adminUsersInvite**](AdminUsersApi.md#adminUsersInvite) | **POST** /admin.users.invite | 
[**adminUsersList**](AdminUsersApi.md#adminUsersList) | **GET** /admin.users.list | 
[**adminUsersRemove**](AdminUsersApi.md#adminUsersRemove) | **POST** /admin.users.remove | 
[**adminUsersSetAdmin**](AdminUsersApi.md#adminUsersSetAdmin) | **POST** /admin.users.setAdmin | 
[**adminUsersSetExpiration**](AdminUsersApi.md#adminUsersSetExpiration) | **POST** /admin.users.setExpiration | 
[**adminUsersSetOwner**](AdminUsersApi.md#adminUsersSetOwner) | **POST** /admin.users.setOwner | 
[**adminUsersSetRegular**](AdminUsersApi.md#adminUsersSetRegular) | **POST** /admin.users.setRegular | 



## adminUsersAssign

> DefaultSuccessTemplate adminUsersAssign(token, teamId, userId, opts)



Add an Enterprise user to a workspace.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
let teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
let userId = "userId_example"; // String | The ID of the user to add to the workspace.
let opts = {
  'channelIds': "channelIds_example", // String | Comma separated values of channel IDs to add user in the new workspace.
  'isRestricted': true, // Boolean | True if user should be added to the workspace as a guest.
  'isUltraRestricted': true // Boolean | True if user should be added to the workspace as a single-channel guest.
};
apiInstance.adminUsersAssign(token, teamId, userId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | 
 **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | 
 **userId** | **String**| The ID of the user to add to the workspace. | 
 **channelIds** | **String**| Comma separated values of channel IDs to add user in the new workspace. | [optional] 
 **isRestricted** | **Boolean**| True if user should be added to the workspace as a guest. | [optional] 
 **isUltraRestricted** | **Boolean**| True if user should be added to the workspace as a single-channel guest. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminUsersInvite

> DefaultSuccessTemplate adminUsersInvite(token, channelIds, email, teamId, opts)



Invite a user to a workspace.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
let channelIds = "channelIds_example"; // String | A comma-separated list of `channel_id`s for this user to join. At least one channel is required.
let email = "email_example"; // String | The email address of the person to invite.
let teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
let opts = {
  'customMessage': "customMessage_example", // String | An optional message to send to the user in the invite email.
  'guestExpirationTs': "guestExpirationTs_example", // String | Timestamp when guest account should be disabled. Only include this timestamp if you are inviting a guest user and you want their account to expire on a certain date.
  'isRestricted': true, // Boolean | Is this user a multi-channel guest user? (default: false)
  'isUltraRestricted': true, // Boolean | Is this user a single channel guest user? (default: false)
  'realName': "realName_example", // String | Full name of the user.
  'resend': true // Boolean | Allow this invite to be resent in the future if a user has not signed up yet. (default: false)
};
apiInstance.adminUsersInvite(token, channelIds, email, teamId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | 
 **channelIds** | **String**| A comma-separated list of &#x60;channel_id&#x60;s for this user to join. At least one channel is required. | 
 **email** | **String**| The email address of the person to invite. | 
 **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | 
 **customMessage** | **String**| An optional message to send to the user in the invite email. | [optional] 
 **guestExpirationTs** | **String**| Timestamp when guest account should be disabled. Only include this timestamp if you are inviting a guest user and you want their account to expire on a certain date. | [optional] 
 **isRestricted** | **Boolean**| Is this user a multi-channel guest user? (default: false) | [optional] 
 **isUltraRestricted** | **Boolean**| Is this user a single channel guest user? (default: false) | [optional] 
 **realName** | **String**| Full name of the user. | [optional] 
 **resend** | **Boolean**| Allow this invite to be resent in the future if a user has not signed up yet. (default: false) | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminUsersList

> DefaultSuccessTemplate adminUsersList(token, teamId, opts)



List users on a workspace

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.users:read`
let teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
let opts = {
  'cursor': "cursor_example", // String | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.
  'limit': 56 // Number | Limit for how many users to be retrieved per page
};
apiInstance.adminUsersList(token, teamId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:read&#x60; | 
 **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | 
 **cursor** | **String**| Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page. | [optional] 
 **limit** | **Number**| Limit for how many users to be retrieved per page | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminUsersRemove

> DefaultSuccessTemplate adminUsersRemove(token, teamId, userId)



Remove a user from a workspace.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
let teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
let userId = "userId_example"; // String | The ID of the user to remove.
apiInstance.adminUsersRemove(token, teamId, userId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | 
 **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | 
 **userId** | **String**| The ID of the user to remove. | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminUsersSetAdmin

> DefaultSuccessTemplate adminUsersSetAdmin(token, teamId, userId)



Set an existing guest, regular user, or owner to be an admin user.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
let teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
let userId = "userId_example"; // String | The ID of the user to designate as an admin.
apiInstance.adminUsersSetAdmin(token, teamId, userId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | 
 **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | 
 **userId** | **String**| The ID of the user to designate as an admin. | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminUsersSetExpiration

> DefaultSuccessTemplate adminUsersSetExpiration(token, expirationTs, teamId, userId)



Set an expiration for a guest user

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
let expirationTs = 56; // Number | Timestamp when guest account should be disabled.
let teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
let userId = "userId_example"; // String | The ID of the user to set an expiration for.
apiInstance.adminUsersSetExpiration(token, expirationTs, teamId, userId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | 
 **expirationTs** | **Number**| Timestamp when guest account should be disabled. | 
 **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | 
 **userId** | **String**| The ID of the user to set an expiration for. | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminUsersSetOwner

> DefaultSuccessTemplate adminUsersSetOwner(token, teamId, userId)



Set an existing guest, regular user, or admin user to be a workspace owner.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
let teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
let userId = "userId_example"; // String | Id of the user to promote to owner.
apiInstance.adminUsersSetOwner(token, teamId, userId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | 
 **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | 
 **userId** | **String**| Id of the user to promote to owner. | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminUsersSetRegular

> DefaultSuccessTemplate adminUsersSetRegular(token, teamId, userId)



Set an existing guest user, admin user, or owner to be a regular user.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
let teamId = "teamId_example"; // String | The ID (`T1234`) of the workspace.
let userId = "userId_example"; // String | The ID of the user to designate as a regular user.
apiInstance.adminUsersSetRegular(token, teamId, userId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | 
 **teamId** | **String**| The ID (&#x60;T1234&#x60;) of the workspace. | 
 **userId** | **String**| The ID of the user to designate as a regular user. | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

