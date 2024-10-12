# NextAuthApi.AccountsApi

All URIs are relative to *https://api.nextauth.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAccount**](AccountsApi.md#deleteAccount) | **DELETE** /servers/{serverid}/accounts/{accountid}/ | Delete specific account
[**deleteUserAccounts_0**](AccountsApi.md#deleteUserAccounts_0) | **DELETE** /servers/{serverid}/users/{userid}/accounts | Delete all accounts of a specific user
[**getAccount**](AccountsApi.md#getAccount) | **GET** /servers/{serverid}/accounts/{accountid}/ | Get specific account
[**getAllAccounts**](AccountsApi.md#getAllAccounts) | **GET** /servers/{serverid}/accounts/ | Get all accounts
[**getUser_0**](AccountsApi.md#getUser_0) | **GET** /servers/{serverid}/users/{userid}/accounts | Get all accounts of a specific user
[**updateAccount**](AccountsApi.md#updateAccount) | **PUT** /servers/{serverid}/accounts/{accountid}/ | Update specific account
[**updateAccountUser**](AccountsApi.md#updateAccountUser) | **PUT** /servers/{serverid}/accounts/{accountid}/user | Update user of the given account.



## deleteAccount

> deleteAccount(serverid, accountid)

Delete specific account

Delete an account. Required permission: &#39;accounts&#39;.

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

let apiInstance = new NextAuthApi.AccountsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let accountid = 56; // Number | Account id
apiInstance.deleteAccount(serverid, accountid, (error, data, response) => {
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
 **accountid** | **Number**| Account id | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteUserAccounts_0

> deleteUserAccounts_0(serverid, userid)

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

let apiInstance = new NextAuthApi.AccountsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let userid = "userid_example"; // String | User name
apiInstance.deleteUserAccounts_0(serverid, userid, (error, data, response) => {
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


## getAccount

> Account getAccount(serverid, accountid)

Get specific account

Returns the account. Required permission: &#39;sessions&#39; or &#39;accounts&#39;.

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

let apiInstance = new NextAuthApi.AccountsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let accountid = 56; // Number | Account id
apiInstance.getAccount(serverid, accountid, (error, data, response) => {
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
 **accountid** | **Number**| Account id | 

### Return type

[**Account**](Account.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllAccounts

> Accounts getAllAccounts(serverid, opts)

Get all accounts

Returns all account. Required permission &#39;accounts&#39;.

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

let apiInstance = new NextAuthApi.AccountsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let opts = {
  'filter': "filter_example", // String | Filter users based on an attribute. Takes the format *attributename=attributevalue*. You can filter for multiple values at once, e.g. *group=in:group1,group2*
  'limit': 56, // Number | Limit the number of results
  'marker': 56, // Number | Offset in the result list
  'sort': "sort_example" // String | Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc*
};
apiInstance.getAllAccounts(serverid, opts, (error, data, response) => {
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


## getUser_0

> Accounts getUser_0(serverid, userid, opts)

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

let apiInstance = new NextAuthApi.AccountsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let userid = "userid_example"; // String | User name
let opts = {
  'limit': 56, // Number | Limit the number of results
  'marker': 56, // Number | Offset in the result list
  'sort': "sort_example" // String | Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc*
};
apiInstance.getUser_0(serverid, userid, opts, (error, data, response) => {
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


## updateAccount

> Account updateAccount(serverid, accountid, blocked)

Update specific account

Update an account. The only available change is (un)blocking the account. Required permission: &#39;accounts&#39;. 

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

let apiInstance = new NextAuthApi.AccountsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let accountid = 56; // Number | Account id
let blocked = true; // Boolean | True if the account is blocked
apiInstance.updateAccount(serverid, accountid, blocked, (error, data, response) => {
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
 **accountid** | **Number**| Account id | 
 **blocked** | **Boolean**| True if the account is blocked | 

### Return type

[**Account**](Account.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAccountUser

> Account updateAccountUser(serverid, accountid, userid)

Update user of the given account.

Update the user of the given account. Required permission: &#39;accounts&#39;.

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

let apiInstance = new NextAuthApi.AccountsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let accountid = 56; // Number | Account id
let userid = "userid_example"; // String | User name
apiInstance.updateAccountUser(serverid, accountid, userid, (error, data, response) => {
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
 **accountid** | **Number**| Account id | 
 **userid** | **String**| User name | 

### Return type

[**Account**](Account.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

