# Scim.UsersApi

All URIs are relative to *https://api.citrixonline.com/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUsers**](UsersApi.md#createUsers) | **POST** /Users | Create User
[**deleteUser**](UsersApi.md#deleteUser) | **DELETE** /Users/{userKey} | Delete User
[**getMe**](UsersApi.md#getMe) | **GET** /Users/me | Get Current User
[**getUser**](UsersApi.md#getUser) | **GET** /Users/{userKey} | Get User
[**getUsers**](UsersApi.md#getUsers) | **GET** /Users | Get Users
[**replaceMe**](UsersApi.md#replaceMe) | **PUT** /Users/me | Replace Current User
[**replaceUser**](UsersApi.md#replaceUser) | **PUT** /Users/{userKey} | Replace User
[**updateMe**](UsersApi.md#updateMe) | **PATCH** /Users/me | Update Current User
[**updateUser**](UsersApi.md#updateUser) | **PATCH** /Users/{userKey} | Update User



## createUsers

> User createUsers(authorization, body)

Create User

Creates a new organization user and adds them to the user domain. The user email domain must match an existing organization email domain.

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.UsersApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let body = new Scim.UserDefinition(); // UserDefinition | The details of the user to create
apiInstance.createUsers(authorization, body, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **body** | [**UserDefinition**](UserDefinition.md)| The details of the user to create | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteUser

> deleteUser(authorization, userKey)

Delete User

Deletes a user from the organization (but not from the account).

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.UsersApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let userKey = 789; // Number | The key of the user to query. The user must be in the organization domain
apiInstance.deleteUser(authorization, userKey, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **userKey** | **Number**| The key of the user to query. The user must be in the organization domain | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMe

> User getMe(authorization)

Get Current User

Queries the identity of the current authenticated user.

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.UsersApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
apiInstance.getMe(authorization, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUser

> User getUser(authorization, userKey)

Get User

Queries user identity in the organization domain.

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.UsersApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let userKey = 789; // Number | The key of the user to query. The user must be in the organization domain
apiInstance.getUser(authorization, userKey, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **userKey** | **Number**| The key of the user to query. The user must be in the organization domain | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsers

> UserCollection getUsers(authorization, opts)

Get Users

Queries multiple user identities in the organization domain. Filtering is available.

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.UsersApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let opts = {
  'filter': "filter_example" // String |  Without a filter, all users in a user domain are returned. The filter parameter must be a properly formed SCIM filter using either the operator eq (equals) or the operator sw (starts with). The filter works for userName, displayName, name.givenName, and name.familyName attributes. For example, /Users?filter=name.familyName%20eq%20%%22Smith%22
};
apiInstance.getUsers(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **filter** | **String**|  Without a filter, all users in a user domain are returned. The filter parameter must be a properly formed SCIM filter using either the operator eq (equals) or the operator sw (starts with). The filter works for userName, displayName, name.givenName, and name.familyName attributes. For example, /Users?filter&#x3D;name.familyName%20eq%20%%22Smith%22 | [optional] 

### Return type

[**UserCollection**](UserCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replaceMe

> User replaceMe(authorization, body)

Replace Current User

Changes the current authenticated user&#39;s displayName, locale, timezone, username and password. The request must include the full user definition (to modify one or more values without sending the full definition, see Update User). The replaced user email domain must be an existing organization email domain. 

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.UsersApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let body = new Scim.UserDefinition(); // UserDefinition | The new user data
apiInstance.replaceMe(authorization, body, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **body** | [**UserDefinition**](UserDefinition.md)| The new user data | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replaceUser

> User replaceUser(authorization, userKey, body)

Replace User

Changes an existing user&#39;s displayName, locale, timezone, username and password. The request must include the full user definition (to modify one or more values without sending the full definition, see Update User). The replaced user email domain must be an existing organization email domain.

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.UsersApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let userKey = 789; // Number | The key of the user to query. The user must be in the organization domain
let body = new Scim.UserDefinition(); // UserDefinition | The new user data
apiInstance.replaceUser(authorization, userKey, body, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **userKey** | **Number**| The key of the user to query. The user must be in the organization domain | 
 **body** | [**UserDefinition**](UserDefinition.md)| The new user data | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMe

> User updateMe(authorization, body)

Update Current User

Changes a limited set (or all if you choose) of the current authenticated user&#39;s data. The updated user email domain must be an existing organization email domain. 

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.UsersApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let body = new Scim.UserDefinition(); // UserDefinition | The new user data
apiInstance.updateMe(authorization, body, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **body** | [**UserDefinition**](UserDefinition.md)| The new user data | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUser

> User updateUser(authorization, userKey, body)

Update User

Changes a limited set (or all if you choose) of the user&#39;s data. The updated user email domain must be an existing organization email domain.

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.UsersApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let userKey = 789; // Number | The key of the user to query. The user must be in the organization domain
let body = new Scim.UserDefinition(); // UserDefinition | The new user data
apiInstance.updateUser(authorization, userKey, body, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **userKey** | **Number**| The key of the user to query. The user must be in the organization domain | 
 **body** | [**UserDefinition**](UserDefinition.md)| The new user data | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

