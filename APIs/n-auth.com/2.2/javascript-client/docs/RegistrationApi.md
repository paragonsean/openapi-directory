# NextAuthApi.RegistrationApi

All URIs are relative to *https://api.nextauth.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getQrEnrol**](RegistrationApi.md#getQrEnrol) | **GET** /servers/{serverid}/sessions/qr/enrol | Generate data for an enrol qr code
[**getServerVash**](RegistrationApi.md#getServerVash) | **GET** /servers/{serverid}/vash | Visual hash of this server
[**registerUser_0**](RegistrationApi.md#registerUser_0) | **POST** /servers/{serverid}/sessions/registeruser | Register a userid for the currently logged in account.
[**updateAccountUser_0**](RegistrationApi.md#updateAccountUser_0) | **PUT** /servers/{serverid}/accounts/{accountid}/user | Update user of the given account.



## getQrEnrol

> File getQrEnrol(serverid, xNonce, name, opts)

Generate data for an enrol qr code

Returns the data for an enrol qr code. Required permission: &#39;sessions&#39;.

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

let apiInstance = new NextAuthApi.RegistrationApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
let name = "name_example"; // String | Name to forward to the nextAuth app for this account
let opts = {
  'userid': "userid_example", // String | User name to register this user under
  'img': "img_example", // String | 'png' for a PNG image, not set for raw data in the qr code
  's': 56 // Number | size in pixels of the qr code, defaults to 500
};
apiInstance.getQrEnrol(serverid, xNonce, name, opts, (error, data, response) => {
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
 **xNonce** | **String**| Nonce to identify the browser/webserver session | 
 **name** | **String**| Name to forward to the nextAuth app for this account | 
 **userid** | **String**| User name to register this user under | [optional] 
 **img** | **String**| &#39;png&#39; for a PNG image, not set for raw data in the qr code | [optional] 
 **s** | **Number**| size in pixels of the qr code, defaults to 500 | [optional] 

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getServerVash

> File getServerVash(serverid)

Visual hash of this server

Returns a PNG of the visual hash corresponding to this server. This visual hash is used during the registration process (optional), for the user to verify that (s)he is registering with the right server in the nextAuth app. For single-server nextAuth-enabled apps (white label or mobile SDK), the public key of the server is typically pinned within the app and hence this visual hash is not displayed to the user. Required permission: &#39;sessions&#39; or &#39;servers&#39;.

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

let apiInstance = new NextAuthApi.RegistrationApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
apiInstance.getServerVash(serverid, (error, data, response) => {
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

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## registerUser_0

> registerUser_0(serverid, xNonce, userid)

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

let apiInstance = new NextAuthApi.RegistrationApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
let userid = "userid_example"; // String | Username to register
apiInstance.registerUser_0(serverid, xNonce, userid, (error, data, response) => {
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


## updateAccountUser_0

> Account updateAccountUser_0(serverid, accountid, userid)

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

let apiInstance = new NextAuthApi.RegistrationApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let accountid = 56; // Number | Account id
let userid = "userid_example"; // String | User name
apiInstance.updateAccountUser_0(serverid, accountid, userid, (error, data, response) => {
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

