# IllumiDesk.UsersApi

All URIs are relative to *https://api.illumidesk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**me**](UsersApi.md#me) | **GET** /v1/me | A convenience endpoint that is equivalent to GET /v1/users/profiles/&lt;my user id&gt;/
[**userAvatarDelete**](UsersApi.md#userAvatarDelete) | **DELETE** /v1/users/{user}/avatar/ | Delete avatar
[**userAvatarGet**](UsersApi.md#userAvatarGet) | **GET** /v1/users/{user}/avatar/ | Retrieve user&#39;s avatar
[**userAvatarSet**](UsersApi.md#userAvatarSet) | **POST** /v1/users/{user}/avatar/ | Add user avatar
[**userAvatarUpdate**](UsersApi.md#userAvatarUpdate) | **PATCH** /v1/users/{user}/avatar/ | Update a project file
[**usersApiKeyList**](UsersApi.md#usersApiKeyList) | **GET** /v1/users/{user}/api-key/ | Retrieve account&#39;s API key
[**usersCreate**](UsersApi.md#usersCreate) | **POST** /v1/users/profiles/ | Create new user
[**usersDelete**](UsersApi.md#usersDelete) | **DELETE** /v1/users/profiles/{user}/ | Delete a user
[**usersEmailsCreate**](UsersApi.md#usersEmailsCreate) | **POST** /v1/users/{user}/emails/ | Create an email address
[**usersEmailsDelete**](UsersApi.md#usersEmailsDelete) | **DELETE** /v1/users/{user}/emails/{email_id}/ | Delete an email address
[**usersEmailsList**](UsersApi.md#usersEmailsList) | **GET** /v1/users/{user}/emails/ | Retrieve account email addresses
[**usersEmailsRead**](UsersApi.md#usersEmailsRead) | **GET** /v1/users/{user}/emails/{email_id}/ | Retrieve a user&#39;s email addresses
[**usersEmailsReplace**](UsersApi.md#usersEmailsReplace) | **PUT** /v1/users/{user}/emails/{email_id}/ | Replace an email address
[**usersEmailsUpdate**](UsersApi.md#usersEmailsUpdate) | **PATCH** /v1/users/{user}/emails/{email_id}/ | Update an email address
[**usersList**](UsersApi.md#usersList) | **GET** /v1/users/profiles/ | Get user list
[**usersRead**](UsersApi.md#usersRead) | **GET** /v1/users/profiles/{user}/ | Retrieve a user
[**usersSshKeyList**](UsersApi.md#usersSshKeyList) | **GET** /v1/users/{user}/ssh-key/ | Retrieve an SSH key
[**usersSshKeyReset**](UsersApi.md#usersSshKeyReset) | **POST** /v1/users/{user}/ssh-key/reset/ | Recreate an SSH key
[**usersUpdate**](UsersApi.md#usersUpdate) | **PATCH** /v1/users/profiles/{user}/ | Update a user



## me

> User me()

A convenience endpoint that is equivalent to GET /v1/users/profiles/&lt;my user id&gt;/

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
apiInstance.me((error, data, response) => {
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

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## userAvatarDelete

> userAvatarDelete(user)

Delete avatar

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let user = "user_example"; // String | User unique identifier expressed as UUID or username.
apiInstance.userAvatarDelete(user, (error, data, response) => {
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
 **user** | **String**| User unique identifier expressed as UUID or username. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## userAvatarGet

> userAvatarGet(user)

Retrieve user&#39;s avatar

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let user = "user_example"; // String | User unique identifier expressed as UUIDor username.
apiInstance.userAvatarGet(user, (error, data, response) => {
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
 **user** | **String**| User unique identifier expressed as UUIDor username. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## userAvatarSet

> User userAvatarSet(user)

Add user avatar

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let user = "user_example"; // String | User unique identifier expressed as UUID or username.
apiInstance.userAvatarSet(user, (error, data, response) => {
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
 **user** | **String**| User unique identifier expressed as UUID or username. | 

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## userAvatarUpdate

> User userAvatarUpdate(user)

Update a project file

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let user = "user_example"; // String | User unique identifier expressed as UUID or username.
apiInstance.userAvatarUpdate(user, (error, data, response) => {
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
 **user** | **String**| User unique identifier expressed as UUID or username. | 

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## usersApiKeyList

> usersApiKeyList(user)

Retrieve account&#39;s API key

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let user = "user_example"; // String | User unique identifier expressed as UUID or username.
apiInstance.usersApiKeyList(user, (error, data, response) => {
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
 **user** | **String**| User unique identifier expressed as UUID or username. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersCreate

> User usersCreate(opts)

Create new user

Only admin users can create new users. New users have active status by default.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let opts = {
  'userData': new IllumiDesk.UserData() // UserData | 
};
apiInstance.usersCreate(opts, (error, data, response) => {
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
 **userData** | [**UserData**](UserData.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## usersDelete

> usersDelete(user)

Delete a user

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let user = "user_example"; // String | User identifier expressed as UUID or username.
apiInstance.usersDelete(user, (error, data, response) => {
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
 **user** | **String**| User identifier expressed as UUID or username. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## usersEmailsCreate

> Email usersEmailsCreate(user, opts)

Create an email address

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let user = "user_example"; // String | User unique identifier expressed as UUID or username.
let opts = {
  'emailData': new IllumiDesk.EmailData() // EmailData | 
};
apiInstance.usersEmailsCreate(user, opts, (error, data, response) => {
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
 **user** | **String**| User unique identifier expressed as UUID or username. | 
 **emailData** | [**EmailData**](EmailData.md)|  | [optional] 

### Return type

[**Email**](Email.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## usersEmailsDelete

> usersEmailsDelete(emailId, user)

Delete an email address

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let emailId = "emailId_example"; // String | Email unique identifier expressed as UUID.
let user = "user_example"; // String | User unique identifier expressed as UUID or username.
apiInstance.usersEmailsDelete(emailId, user, (error, data, response) => {
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
 **emailId** | **String**| Email unique identifier expressed as UUID. | 
 **user** | **String**| User unique identifier expressed as UUID or username. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## usersEmailsList

> [Email] usersEmailsList(user, opts)

Retrieve account email addresses

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let user = "user_example"; // String | User unique identifier as expressed as UUID or username.
let opts = {
  'limit': "limit_example", // String | Limite when getting email list.
  'offset': "offset_example", // String | Offset when getting email list.
  'ordering': "ordering_example" // String | Ordering when getting email list.
};
apiInstance.usersEmailsList(user, opts, (error, data, response) => {
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
 **user** | **String**| User unique identifier as expressed as UUID or username. | 
 **limit** | **String**| Limite when getting email list. | [optional] 
 **offset** | **String**| Offset when getting email list. | [optional] 
 **ordering** | **String**| Ordering when getting email list. | [optional] 

### Return type

[**[Email]**](Email.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## usersEmailsRead

> Email usersEmailsRead(emailId, user)

Retrieve a user&#39;s email addresses

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let emailId = "emailId_example"; // String | Email unique identifier expressed as UUID.
let user = "user_example"; // String | User unique identifier expressed as UUID or username.
apiInstance.usersEmailsRead(emailId, user, (error, data, response) => {
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
 **emailId** | **String**| Email unique identifier expressed as UUID. | 
 **user** | **String**| User unique identifier expressed as UUID or username. | 

### Return type

[**Email**](Email.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## usersEmailsReplace

> Email usersEmailsReplace(emailId, user, opts)

Replace an email address

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let emailId = "emailId_example"; // String | Email unique identifier expressed as UUID.
let user = "user_example"; // String | User unique identifier expressed as UUID or username.
let opts = {
  'emailData': new IllumiDesk.EmailData() // EmailData | 
};
apiInstance.usersEmailsReplace(emailId, user, opts, (error, data, response) => {
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
 **emailId** | **String**| Email unique identifier expressed as UUID. | 
 **user** | **String**| User unique identifier expressed as UUID or username. | 
 **emailData** | [**EmailData**](EmailData.md)|  | [optional] 

### Return type

[**Email**](Email.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## usersEmailsUpdate

> Email usersEmailsUpdate(emailId, user, opts)

Update an email address

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let emailId = "emailId_example"; // String | Email unique identifier expressed as UUID.
let user = "user_example"; // String | User unique identifier expressed as UUID or username.
let opts = {
  'emailData': new IllumiDesk.EmailData() // EmailData | 
};
apiInstance.usersEmailsUpdate(emailId, user, opts, (error, data, response) => {
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
 **emailId** | **String**| Email unique identifier expressed as UUID. | 
 **user** | **String**| User unique identifier expressed as UUID or username. | 
 **emailData** | [**EmailData**](EmailData.md)|  | [optional] 

### Return type

[**Email**](Email.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## usersList

> [User] usersList(opts)

Get user list

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let opts = {
  'limit': "limit_example", // String | Limit user list.
  'offset': "offset_example", // String | Offset when getting users.
  'username': "username_example", // String | User username.
  'email': "email_example", // String | User email.
  'ordering': "ordering_example" // String | Ordering when getting users.
};
apiInstance.usersList(opts, (error, data, response) => {
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
 **limit** | **String**| Limit user list. | [optional] 
 **offset** | **String**| Offset when getting users. | [optional] 
 **username** | **String**| User username. | [optional] 
 **email** | **String**| User email. | [optional] 
 **ordering** | **String**| Ordering when getting users. | [optional] 

### Return type

[**[User]**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## usersRead

> User usersRead(user)

Retrieve a user

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let user = "user_example"; // String | Unique identifier expressed as UUID or username.
apiInstance.usersRead(user, (error, data, response) => {
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
 **user** | **String**| Unique identifier expressed as UUID or username. | 

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## usersSshKeyList

> usersSshKeyList(user)

Retrieve an SSH key

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let user = "user_example"; // String | User unique identifier expressed as UUID or username.
apiInstance.usersSshKeyList(user, (error, data, response) => {
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
 **user** | **String**| User unique identifier expressed as UUID or username. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersSshKeyReset

> usersSshKeyReset(user)

Recreate an SSH key

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let user = "user_example"; // String | User unique identifier expressed as UUID or username.
apiInstance.usersSshKeyReset(user, (error, data, response) => {
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
 **user** | **String**| User unique identifier expressed as UUID or username. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUpdate

> User usersUpdate(user, opts)

Update a user

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.UsersApi();
let user = "user_example"; // String | User unique identifier expressed as UUID or username.
let opts = {
  'userData': new IllumiDesk.UserData() // UserData | 
};
apiInstance.usersUpdate(user, opts, (error, data, response) => {
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
 **user** | **String**| User unique identifier expressed as UUID or username. | 
 **userData** | [**UserData**](UserData.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html

