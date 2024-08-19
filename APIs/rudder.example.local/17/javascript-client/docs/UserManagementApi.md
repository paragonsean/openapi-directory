# RudderApi.UserManagementApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addUser**](UserManagementApi.md#addUser) | **POST** /usermanagement | Add user
[**deleteUser**](UserManagementApi.md#deleteUser) | **DELETE** /usermanagement/{username} | Delete an user
[**getRole**](UserManagementApi.md#getRole) | **GET** /usermanagement/roles | List all roles
[**getUserInfo**](UserManagementApi.md#getUserInfo) | **GET** /usermanagement/users | List all users
[**reloadUserConf**](UserManagementApi.md#reloadUserConf) | **GET** /usermanagement/users/reload | Reload user
[**updateUser**](UserManagementApi.md#updateUser) | **POST** /usermanagement/update/{username} | Update user&#39;s infos



## addUser

> AddUser200Response addUser(users)

Add user

Add a new user

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.UserManagementApi();
let users = new RudderApi.Users(); // Users | 
apiInstance.addUser(users, (error, data, response) => {
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
 **users** | [**Users**](Users.md)|  | 

### Return type

[**AddUser200Response**](AddUser200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteUser

> DeleteUser200Response deleteUser(username)

Delete an user

Delete the user and his permissions

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.UserManagementApi();
let username = "JaneDoe"; // String | Username of an user (unique)
apiInstance.deleteUser(username, (error, data, response) => {
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
 **username** | **String**| Username of an user (unique) | 

### Return type

[**DeleteUser200Response**](DeleteUser200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRole

> GetRole200Response getRole()

List all roles

Get all available roles and their rights

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.UserManagementApi();
apiInstance.getRole((error, data, response) => {
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

[**GetRole200Response**](GetRole200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserInfo

> GetUserInfo200Response getUserInfo()

List all users

Get the list of all present users and their permissions

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.UserManagementApi();
apiInstance.getUserInfo((error, data, response) => {
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

[**GetUserInfo200Response**](GetUserInfo200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reloadUserConf

> ReloadUserConf200Response reloadUserConf()

Reload user

Reload the users from the file system, in the configuration file

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.UserManagementApi();
apiInstance.reloadUserConf((error, data, response) => {
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

[**ReloadUserConf200Response**](ReloadUserConf200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateUser

> UpdateUser200Response updateUser(username, users)

Update user&#39;s infos

Rename, change password (pre-hashed or not) and change permission of an user. If a parameter is empty, it will be ignored.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.UserManagementApi();
let username = "JaneDoe"; // String | Username of an user (unique)
let users = new RudderApi.Users(); // Users | 
apiInstance.updateUser(username, users, (error, data, response) => {
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
 **username** | **String**| Username of an user (unique) | 
 **users** | [**Users**](Users.md)|  | 

### Return type

[**UpdateUser200Response**](UpdateUser200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

