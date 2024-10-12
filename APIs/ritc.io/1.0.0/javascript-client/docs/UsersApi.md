# Ritc.UsersApi

All URIs are relative to *https://api.ritc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addAdminUser**](UsersApi.md#addAdminUser) | **POST** /users/admin | 
[**addAppUser**](UsersApi.md#addAppUser) | **POST** /users | 
[**addAppUserToChannel**](UsersApi.md#addAppUserToChannel) | **POST** /users/{user_id}/channels | 
[**addAppUserToRule**](UsersApi.md#addAppUserToRule) | **POST** /users/{user_id}/rules/{rule_id} | 
[**authenticateAppUserForChannel**](UsersApi.md#authenticateAppUserForChannel) | **POST** /users/authenticate/{user_id}/channel/{channel_id} | 
[**getAdminUser**](UsersApi.md#getAdminUser) | **GET** /users/admin/{user_id} | 
[**getAppUser**](UsersApi.md#getAppUser) | **GET** /users/{user_id} | 
[**getAppUserChannel**](UsersApi.md#getAppUserChannel) | **GET** /users/{user_id}/channels/{channel_id} | 
[**getAppUserRule**](UsersApi.md#getAppUserRule) | **GET** /users/{user_id}/rules/{rule_id} | 
[**listAdminUsers**](UsersApi.md#listAdminUsers) | **GET** /users/admin | 
[**listAppUserChannels**](UsersApi.md#listAppUserChannels) | **GET** /users/{user_id}/channels | 
[**listAppUserRules**](UsersApi.md#listAppUserRules) | **GET** /users/{user_id}/rules | 
[**listAppUsers**](UsersApi.md#listAppUsers) | **GET** /users | 
[**removeAdminUser**](UsersApi.md#removeAdminUser) | **DELETE** /users/admin/{user_id} | 
[**removeAppUser**](UsersApi.md#removeAppUser) | **DELETE** /users/{user_id} | 
[**removeAppUserFromChannel**](UsersApi.md#removeAppUserFromChannel) | **DELETE** /users/{user_id}/channels/{channel_id} | 
[**removeAppUserFromRule**](UsersApi.md#removeAppUserFromRule) | **DELETE** /users/{user_id}/rules/{rule_id} | 
[**runRuleForAppUser**](UsersApi.md#runRuleForAppUser) | **POST** /users/{user_id}/rules/{rule_id}/run | 
[**updateAdminUser**](UsersApi.md#updateAdminUser) | **PATCH** /users/admin/{user_id} | 
[**updateAppUser**](UsersApi.md#updateAppUser) | **PATCH** /users/{user_id} | 



## addAdminUser

> AdminUserResponse addAdminUser(adminUserObject)



Create a new admin user

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let adminUserObject = new Ritc.AdminUser(); // AdminUser | Admin User information
apiInstance.addAdminUser(adminUserObject, (error, data, response) => {
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
 **adminUserObject** | [**AdminUser**](AdminUser.md)| Admin User information | 

### Return type

[**AdminUserResponse**](AdminUserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addAppUser

> AppUserResponse addAppUser(appUserObject)



Create a new App User

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let appUserObject = new Ritc.AppUser(); // AppUser | App User information
apiInstance.addAppUser(appUserObject, (error, data, response) => {
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
 **appUserObject** | [**AppUser**](AppUser.md)| App User information | 

### Return type

[**AppUserResponse**](AppUserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addAppUserToChannel

> UserChannel addAppUserToChannel(userId, channelId)



Assign a channel to a user

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of user
let channelId = "channelId_example"; // String | Id of Channel
apiInstance.addAppUserToChannel(userId, channelId, (error, data, response) => {
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
 **userId** | **String**| Id of user | 
 **channelId** | **String**| Id of Channel | 

### Return type

[**UserChannel**](UserChannel.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addAppUserToRule

> RuleShortResponse addAppUserToRule(userId, ruleId)



Assign a user to a rule

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of User
let ruleId = "ruleId_example"; // String | Id of Rule
apiInstance.addAppUserToRule(userId, ruleId, (error, data, response) => {
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
 **userId** | **String**| Id of User | 
 **ruleId** | **String**| Id of Rule | 

### Return type

[**RuleShortResponse**](RuleShortResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authenticateAppUserForChannel

> [AuthorizeUrlResponse] authenticateAppUserForChannel(userId, channelId)



Authenticate a user for a channel

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of User
let channelId = "channelId_example"; // String | Id of Channel
apiInstance.authenticateAppUserForChannel(userId, channelId, (error, data, response) => {
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
 **userId** | **String**| Id of User | 
 **channelId** | **String**| Id of Channel | 

### Return type

[**[AuthorizeUrlResponse]**](AuthorizeUrlResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAdminUser

> [AdminUserResponse] getAdminUser(userId)



Get an admin user

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of Admin_User
apiInstance.getAdminUser(userId, (error, data, response) => {
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
 **userId** | **String**| Id of Admin_User | 

### Return type

[**[AdminUserResponse]**](AdminUserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAppUser

> [AppUserResponse] getAppUser(userId)



Get an App User

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of App User
apiInstance.getAppUser(userId, (error, data, response) => {
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
 **userId** | **String**| Id of App User | 

### Return type

[**[AppUserResponse]**](AppUserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAppUserChannel

> [UserChannel] getAppUserChannel(userId, channelId)



Get a user channel

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of User
let channelId = "channelId_example"; // String | Id of Channel
apiInstance.getAppUserChannel(userId, channelId, (error, data, response) => {
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
 **userId** | **String**| Id of User | 
 **channelId** | **String**| Id of Channel | 

### Return type

[**[UserChannel]**](UserChannel.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAppUserRule

> [RuleFullResponse] getAppUserRule(userId, ruleId)



Get a user

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of User
let ruleId = "ruleId_example"; // String | Id of Rule
apiInstance.getAppUserRule(userId, ruleId, (error, data, response) => {
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
 **userId** | **String**| Id of User | 
 **ruleId** | **String**| Id of Rule | 

### Return type

[**[RuleFullResponse]**](RuleFullResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAdminUsers

> [AdminUserResponse] listAdminUsers()



Admin users

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
apiInstance.listAdminUsers((error, data, response) => {
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

[**[AdminUserResponse]**](AdminUserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAppUserChannels

> [UserChannel] listAppUserChannels(userId)



Channels available to a User

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of user
apiInstance.listAppUserChannels(userId, (error, data, response) => {
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
 **userId** | **String**| Id of user | 

### Return type

[**[UserChannel]**](UserChannel.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAppUserRules

> [RuleShortResponse] listAppUserRules(userId)



Rules for a User

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of user
apiInstance.listAppUserRules(userId, (error, data, response) => {
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
 **userId** | **String**| Id of user | 

### Return type

[**[RuleShortResponse]**](RuleShortResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAppUsers

> [AppUserResponse] listAppUsers()



Users

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
apiInstance.listAppUsers((error, data, response) => {
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

[**[AppUserResponse]**](AppUserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeAdminUser

> removeAdminUser(userId)



Remove an admin user

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of Admin_User
apiInstance.removeAdminUser(userId, (error, data, response) => {
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
 **userId** | **String**| Id of Admin_User | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeAppUser

> removeAppUser(userId)



Remove a user

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of user
apiInstance.removeAppUser(userId, (error, data, response) => {
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
 **userId** | **String**| Id of user | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeAppUserFromChannel

> removeAppUserFromChannel(userId, channelId)



Remove a user channel assignment

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of User
let channelId = "channelId_example"; // String | Id of Channel
apiInstance.removeAppUserFromChannel(userId, channelId, (error, data, response) => {
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
 **userId** | **String**| Id of User | 
 **channelId** | **String**| Id of Channel | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeAppUserFromRule

> removeAppUserFromRule(userId, ruleId)



Remove a rule user

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of User
let ruleId = "ruleId_example"; // String | Id of Rule
apiInstance.removeAppUserFromRule(userId, ruleId, (error, data, response) => {
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
 **userId** | **String**| Id of User | 
 **ruleId** | **String**| Id of Rule | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runRuleForAppUser

> Object runRuleForAppUser(userId, ruleId)



Run rule for a user

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of User
let ruleId = "ruleId_example"; // String | Id of Rule
apiInstance.runRuleForAppUser(userId, ruleId, (error, data, response) => {
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
 **userId** | **String**| Id of User | 
 **ruleId** | **String**| Id of Rule | 

### Return type

**Object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAdminUser

> AdminUserResponse updateAdminUser(userId, adminUserObject)



Update information about an admin user

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of user
let adminUserObject = new Ritc.AdminUser(); // AdminUser | Admin User information
apiInstance.updateAdminUser(userId, adminUserObject, (error, data, response) => {
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
 **userId** | **String**| Id of user | 
 **adminUserObject** | [**AdminUser**](AdminUser.md)| Admin User information | 

### Return type

[**AdminUserResponse**](AdminUserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAppUser

> AppUserResponse updateAppUser(userId, appUserObject)



Update information about an App User

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.UsersApi();
let userId = "userId_example"; // String | Id of user
let appUserObject = new Ritc.AppUser(); // AppUser | App User information
apiInstance.updateAppUser(userId, appUserObject, (error, data, response) => {
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
 **userId** | **String**| Id of user | 
 **appUserObject** | [**AppUser**](AppUser.md)| App User information | 

### Return type

[**AppUserResponse**](AppUserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

