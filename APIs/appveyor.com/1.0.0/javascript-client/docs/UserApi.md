# AppVeyorRestApi.UserApi

All URIs are relative to *https://ci.appveyor.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelUserInvitation**](UserApi.md#cancelUserInvitation) | **DELETE** /users/invitations/{userInvitationId} | Cancel user invitation
[**deleteUser**](UserApi.md#deleteUser) | **DELETE** /users/{userId} | Delete user
[**getUser**](UserApi.md#getUser) | **GET** /users/{userId} | Get user
[**getUserInvitations**](UserApi.md#getUserInvitations) | **GET** /users/invitations | Get user invitations
[**getUsers**](UserApi.md#getUsers) | **GET** /users | Get users
[**inviteUser**](UserApi.md#inviteUser) | **POST** /users/invitations | Invite user
[**joinAccount**](UserApi.md#joinAccount) | **PUT** /user/join-account | Join Account
[**updateUser**](UserApi.md#updateUser) | **PUT** /users | Update user



## cancelUserInvitation

> cancelUserInvitation(userInvitationId)

Cancel user invitation

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.UserApi();
let userInvitationId = "userInvitationId_example"; // String | User Invitation ID
apiInstance.cancelUserInvitation(userInvitationId, (error, data, response) => {
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
 **userInvitationId** | **String**| User Invitation ID | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## deleteUser

> deleteUser(userId)

Delete user

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.UserApi();
let userId = 56; // Number | User ID
apiInstance.deleteUser(userId, (error, data, response) => {
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
 **userId** | **Number**| User ID | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getUser

> UserAccountRolesResults getUser(userId)

Get user

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.UserApi();
let userId = 56; // Number | User ID
apiInstance.getUser(userId, (error, data, response) => {
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
 **userId** | **Number**| User ID | 

### Return type

[**UserAccountRolesResults**](UserAccountRolesResults.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getUserInvitations

> [UserInvitationModel] getUserInvitations()

Get user invitations

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.UserApi();
apiInstance.getUserInvitations((error, data, response) => {
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

[**[UserInvitationModel]**](UserInvitationModel.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getUsers

> [UserAccount] getUsers()

Get users

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.UserApi();
apiInstance.getUsers((error, data, response) => {
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

[**[UserAccount]**](UserAccount.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## inviteUser

> inviteUser(body)

Invite user

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.UserApi();
let body = new AppVeyorRestApi.InviteUserRequest(); // InviteUserRequest | 
apiInstance.inviteUser(body, (error, data, response) => {
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
 **body** | [**InviteUserRequest**](InviteUserRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## joinAccount

> SessionModel joinAccount(body)

Join Account

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.UserApi();
let body = new AppVeyorRestApi.JoinAccountRequest(); // JoinAccountRequest | 
apiInstance.joinAccount(body, (error, data, response) => {
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
 **body** | [**JoinAccountRequest**](JoinAccountRequest.md)|  | 

### Return type

[**SessionModel**](SessionModel.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## updateUser

> updateUser(body)

Update user

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.UserApi();
let body = new AppVeyorRestApi.UserAccount(); // UserAccount | 
apiInstance.updateUser(body, (error, data, response) => {
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
 **body** | [**UserAccount**](UserAccount.md)|  | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml

