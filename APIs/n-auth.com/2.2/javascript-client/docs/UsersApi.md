# NextAuthApi.UsersApi

All URIs are relative to *https://api.nextauth.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUser**](UsersApi.md#deleteUser) | **DELETE** /servers/{serverid}/users/{userid}/ | Delete a specific user
[**deleteUserAccounts**](UsersApi.md#deleteUserAccounts) | **DELETE** /servers/{serverid}/users/{userid}/accounts | Delete all accounts of a specific user
[**deleteUserAttribute**](UsersApi.md#deleteUserAttribute) | **DELETE** /servers/{serverid}/users/{userid}/attributes/{attributekey} | Delete specific attribute of a specific user
[**deleteUserAttributes**](UsersApi.md#deleteUserAttributes) | **DELETE** /servers/{serverid}/users/{userid}/attributes/ | Delete all attributes of a specific user
[**getUser**](UsersApi.md#getUser) | **GET** /servers/{serverid}/users/{userid}/accounts | Get all accounts of a specific user
[**getUserAttributes**](UsersApi.md#getUserAttributes) | **GET** /servers/{serverid}/users/{userid}/attributes/ | Get all attributes of a specific user
[**getUsers**](UsersApi.md#getUsers) | **GET** /servers/{serverid}/users/ | Get all users
[**registerUser**](UsersApi.md#registerUser) | **POST** /servers/{serverid}/sessions/registeruser | Register a userid for the currently logged in account.
[**setUserAttributes**](UsersApi.md#setUserAttributes) | **POST** /servers/{serverid}/users/{userid}/attributes/ | Set all attributes of a specific user
[**updateUserAttributes**](UsersApi.md#updateUserAttributes) | **PUT** /servers/{serverid}/users/{userid}/attributes/ | Update specified attributes of a specific user



## deleteUser

> deleteUser(serverid, userid)

Delete a specific user

Delete a user. Required permission: &#39;users&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.UsersApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let userid = "userid_example"; // String | User name
apiInstance.deleteUser(serverid, userid, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **userid** | **String**| User name | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteUserAccounts

> deleteUserAccounts(serverid, userid)

Delete all accounts of a specific user

Delete all accounts corresponding to this user. The user itself is not deleted. Required permission: &#39;accounts&#39; or &#39;users&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.UsersApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let userid = "userid_example"; // String | User name
apiInstance.deleteUserAccounts(serverid, userid, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **userid** | **String**| User name | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteUserAttribute

> deleteUserAttribute(serverid, userid, attributekey)

Delete specific attribute of a specific user

Delete attribute with the specified key of a specific user. Required permission: &#39;users&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.UsersApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let userid = "userid_example"; // String | User name
let attributekey = "attributekey_example"; // String | Key of the attribute
apiInstance.deleteUserAttribute(serverid, userid, attributekey, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **userid** | **String**| User name | 
 **attributekey** | **String**| Key of the attribute | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteUserAttributes

> deleteUserAttributes(serverid, userid)

Delete all attributes of a specific user

Delete all attributes of a specific user. Required permission: &#39;users&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.UsersApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let userid = "userid_example"; // String | User name
apiInstance.deleteUserAttributes(serverid, userid, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **userid** | **String**| User name | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getUser

> Accounts getUser(serverid, userid, opts)

Get all accounts of a specific user

Returns an array containing all accounts corresponding to this user. Required permission: &#39;sessions&#39; or &#39;users&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.UsersApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let userid = "userid_example"; // String | User name
let opts = {
  'limit': 56, // Number | Limit the number of results
  'marker': 56, // Number | Offset in the result list
  'sort': "sort_example" // String | Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc*
};
apiInstance.getUser(serverid, userid, opts, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **userid** | **String**| User name | 
 **limit** | **Number**| Limit the number of results | [optional] 
 **marker** | **Number**| Offset in the result list | [optional] 
 **sort** | **String**| Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc* | [optional] 

### Return type

[**Accounts**](Accounts.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserAttributes

> String getUserAttributes(serverid, userid)

Get all attributes of a specific user

Returns an array containing all attributes corresponding to this user. Required permission: &#39;sessions&#39; or &#39;users&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.UsersApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let userid = "userid_example"; // String | User name
apiInstance.getUserAttributes(serverid, userid, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **userid** | **String**| User name | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## getUsers

> Users getUsers(serverid, opts)

Get all users

Returns an array of arrays containing all accounts corresponding to all users. Required permission: &#39;users&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.UsersApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let opts = {
  'filter': "filter_example", // String | Filter users based on an attribute. Takes the format *attributename=attributevalue*. You can filter for multiple values at once, e.g. *group=in:group1,group2*
  'search': "search_example", // String | Search for a username LIKE %search%
  'limit': 56, // Number | Limit the number of results
  'marker': 56, // Number | Offset in the result list
  'sort': "sort_example" // String | Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc*
};
apiInstance.getUsers(serverid, opts, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **filter** | **String**| Filter users based on an attribute. Takes the format *attributename&#x3D;attributevalue*. You can filter for multiple values at once, e.g. *group&#x3D;in:group1,group2* | [optional] 
 **search** | **String**| Search for a username LIKE %search% | [optional] 
 **limit** | **Number**| Limit the number of results | [optional] 
 **marker** | **Number**| Offset in the result list | [optional] 
 **sort** | **String**| Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc* | [optional] 

### Return type

[**Users**](Users.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registerUser

> registerUser(serverid, xNonce, userid)

Register a userid for the currently logged in account.

Register a user for the currently logged in account. You can also directly pass a user name when generating an ENROL qr code. Required permission: &#39;users&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.UsersApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
let userid = "userid_example"; // String | Username to register
apiInstance.registerUser(serverid, xNonce, userid, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **xNonce** | **String**| Nonce to identify the browser/webserver session | 
 **userid** | **String**| Username to register | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setUserAttributes

> setUserAttributes(serverid, userid, attributes)

Set all attributes of a specific user

Set the attributes of a specific user. Prior attributes with keys that are not provided in the body of the request will be deleted. Creates the user if not exists. Required permission: &#39;users&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.UsersApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let userid = "userid_example"; // String | User name
let attributes = {key: null}; // Object | Array of attributes
apiInstance.setUserAttributes(serverid, userid, attributes, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **userid** | **String**| User name | 
 **attributes** | **Object**| Array of attributes | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateUserAttributes

> updateUserAttributes(serverid, userid, attributes)

Update specified attributes of a specific user

Update the specified attributes of a specific user. Prior attributes with keys that are not provided in the body of the request will not be deleted. Required permission: &#39;users&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.UsersApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let userid = "userid_example"; // String | User name
let attributes = {key: null}; // Object | Array of attributes
apiInstance.updateUserAttributes(serverid, userid, attributes, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **userid** | **String**| User name | 
 **attributes** | **Object**| Array of attributes | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

