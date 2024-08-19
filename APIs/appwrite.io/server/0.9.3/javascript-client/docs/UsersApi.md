# Appwrite.UsersApi

All URIs are relative to *https://appwrite.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersCreate**](UsersApi.md#usersCreate) | **POST** /users | Create User
[**usersDelete**](UsersApi.md#usersDelete) | **DELETE** /users/{userId} | Delete User
[**usersDeleteSession**](UsersApi.md#usersDeleteSession) | **DELETE** /users/{userId}/sessions/{sessionId} | Delete User Session
[**usersDeleteSessions**](UsersApi.md#usersDeleteSessions) | **DELETE** /users/{userId}/sessions | Delete User Sessions
[**usersGet**](UsersApi.md#usersGet) | **GET** /users/{userId} | Get User
[**usersGetLogs**](UsersApi.md#usersGetLogs) | **GET** /users/{userId}/logs | Get User Logs
[**usersGetPrefs**](UsersApi.md#usersGetPrefs) | **GET** /users/{userId}/prefs | Get User Preferences
[**usersGetSessions**](UsersApi.md#usersGetSessions) | **GET** /users/{userId}/sessions | Get User Sessions
[**usersList**](UsersApi.md#usersList) | **GET** /users | List Users
[**usersUpdatePrefs**](UsersApi.md#usersUpdatePrefs) | **PATCH** /users/{userId}/prefs | Update User Preferences
[**usersUpdateStatus**](UsersApi.md#usersUpdateStatus) | **PATCH** /users/{userId}/status | Update User Status
[**usersUpdateVerification**](UsersApi.md#usersUpdateVerification) | **PATCH** /users/{userId}/verification | Update Email Verification



## usersCreate

> User usersCreate(opts)

Create User

Create a new user.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.UsersApi();
let opts = {
  'usersCreateRequest': new Appwrite.UsersCreateRequest() // UsersCreateRequest | 
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
 **usersCreateRequest** | [**UsersCreateRequest**](UsersCreateRequest.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersDelete

> usersDelete(userId)

Delete User

Delete a user by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.UsersApi();
let userId = "userId_example"; // String | User unique ID.
apiInstance.usersDelete(userId, (error, data, response) => {
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
 **userId** | **String**| User unique ID. | 

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersDeleteSession

> usersDeleteSession(userId, sessionId)

Delete User Session

Delete a user sessions by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.UsersApi();
let userId = "userId_example"; // String | User unique ID.
let sessionId = "sessionId_example"; // String | User unique session ID.
apiInstance.usersDeleteSession(userId, sessionId, (error, data, response) => {
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
 **userId** | **String**| User unique ID. | 
 **sessionId** | **String**| User unique session ID. | 

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersDeleteSessions

> usersDeleteSessions(userId)

Delete User Sessions

Delete all user&#39;s sessions by using the user&#39;s unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.UsersApi();
let userId = "userId_example"; // String | User unique ID.
apiInstance.usersDeleteSessions(userId, (error, data, response) => {
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
 **userId** | **String**| User unique ID. | 

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersGet

> User usersGet(userId)

Get User

Get a user by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.UsersApi();
let userId = "userId_example"; // String | User unique ID.
apiInstance.usersGet(userId, (error, data, response) => {
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
 **userId** | **String**| User unique ID. | 

### Return type

[**User**](User.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGetLogs

> LogList usersGetLogs(userId)

Get User Logs

Get a user activity logs list by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.UsersApi();
let userId = "userId_example"; // String | User unique ID.
apiInstance.usersGetLogs(userId, (error, data, response) => {
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
 **userId** | **String**| User unique ID. | 

### Return type

[**LogList**](LogList.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGetPrefs

> {String: Object} usersGetPrefs(userId)

Get User Preferences

Get the user preferences by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.UsersApi();
let userId = "userId_example"; // String | User unique ID.
apiInstance.usersGetPrefs(userId, (error, data, response) => {
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
 **userId** | **String**| User unique ID. | 

### Return type

**{String: Object}**

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGetSessions

> SessionList usersGetSessions(userId)

Get User Sessions

Get the user sessions list by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.UsersApi();
let userId = "userId_example"; // String | User unique ID.
apiInstance.usersGetSessions(userId, (error, data, response) => {
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
 **userId** | **String**| User unique ID. | 

### Return type

[**SessionList**](SessionList.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersList

> UserList usersList(opts)

List Users

Get a list of all the project&#39;s users. You can use the query params to filter your results.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.UsersApi();
let opts = {
  'search': "''", // String | Search term to filter your list results. Max length: 256 chars.
  'limit': 25, // Number | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
  'offset': 0, // Number | Results offset. The default value is 0. Use this param to manage pagination.
  'orderType': "'ASC'" // String | Order result by ASC or DESC order.
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
 **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to &#39;&#39;]
 **limit** | **Number**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25]
 **offset** | **Number**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0]
 **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to &#39;ASC&#39;]

### Return type

[**UserList**](UserList.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUpdatePrefs

> {String: Object} usersUpdatePrefs(userId, opts)

Update User Preferences

Update the user preferences by its unique ID. You can pass only the specific settings you wish to update.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.UsersApi();
let userId = "userId_example"; // String | User unique ID.
let opts = {
  'accountUpdatePrefsRequest': new Appwrite.AccountUpdatePrefsRequest() // AccountUpdatePrefsRequest | 
};
apiInstance.usersUpdatePrefs(userId, opts, (error, data, response) => {
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
 **userId** | **String**| User unique ID. | 
 **accountUpdatePrefsRequest** | [**AccountUpdatePrefsRequest**](AccountUpdatePrefsRequest.md)|  | [optional] 

### Return type

**{String: Object}**

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersUpdateStatus

> User usersUpdateStatus(userId, opts)

Update User Status

Update the user status by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.UsersApi();
let userId = "userId_example"; // String | User unique ID.
let opts = {
  'usersUpdateStatusRequest': new Appwrite.UsersUpdateStatusRequest() // UsersUpdateStatusRequest | 
};
apiInstance.usersUpdateStatus(userId, opts, (error, data, response) => {
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
 **userId** | **String**| User unique ID. | 
 **usersUpdateStatusRequest** | [**UsersUpdateStatusRequest**](UsersUpdateStatusRequest.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersUpdateVerification

> User usersUpdateVerification(userId, opts)

Update Email Verification

Update the user email verification status by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.UsersApi();
let userId = "userId_example"; // String | User unique ID.
let opts = {
  'usersUpdateVerificationRequest': new Appwrite.UsersUpdateVerificationRequest() // UsersUpdateVerificationRequest | 
};
apiInstance.usersUpdateVerification(userId, opts, (error, data, response) => {
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
 **userId** | **String**| User unique ID. | 
 **usersUpdateVerificationRequest** | [**UsersUpdateVerificationRequest**](UsersUpdateVerificationRequest.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

