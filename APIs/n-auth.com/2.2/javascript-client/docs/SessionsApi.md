# NextAuthApi.SessionsApi

All URIs are relative to *https://api.nextauth.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getQrLogin**](SessionsApi.md#getQrLogin) | **GET** /servers/{serverid}/sessions/qr/login | Generate data for a login qr code
[**getSession**](SessionsApi.md#getSession) | **GET** /servers/{serverid}/sessions/ | Check if the user is logged in
[**logout**](SessionsApi.md#logout) | **POST** /servers/{serverid}/sessions/logout | Force a logout on the given session
[**provokeLogin**](SessionsApi.md#provokeLogin) | **POST** /servers/{serverid}/sessions/provokelogin | Push a login confirmation to the user&#39;s app
[**provokeLoginOnAccount**](SessionsApi.md#provokeLoginOnAccount) | **POST** /servers/{serverid}/accounts/{accountid}/provokelogin | Push a login confirmation to the user&#39;s app
[**provokeLoginOnUser**](SessionsApi.md#provokeLoginOnUser) | **POST** /servers/{serverid}/users/{userid}/provokelogin | Push a login confirmation to the user&#39;s app



## getQrLogin

> File getQrLogin(serverid, xNonce, opts)

Generate data for a login qr code

Returns the data for a login qr code. Required permission: &#39;sessions&#39;.

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

let apiInstance = new NextAuthApi.SessionsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
let opts = {
  'img': "img_example", // String | \"png\" for a PNG image, not set for raw data in the qr code
  's': 56, // Number | size in pixels of the qr code, defaults to 500
  'userContext': new NextAuthApi.UserContext() // UserContext | Session information to display to user.
};
apiInstance.getQrLogin(serverid, xNonce, opts, (error, data, response) => {
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
 **img** | **String**| \&quot;png\&quot; for a PNG image, not set for raw data in the qr code | [optional] 
 **s** | **Number**| size in pixels of the qr code, defaults to 500 | [optional] 
 **userContext** | [**UserContext**](UserContext.md)| Session information to display to user. | [optional] 

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream


## getSession

> LoginStatus getSession(serverid, xNonce)

Check if the user is logged in

Based on the browser/webserver session identifier, check if the user is logged in and return the associated username. This also returns additional information: the data for the login qr code and whether or not a loggin can be provoked directly from the server. Required permission: &#39;sessions&#39;.

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

let apiInstance = new NextAuthApi.SessionsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
apiInstance.getSession(serverid, xNonce, (error, data, response) => {
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

### Return type

[**LoginStatus**](LoginStatus.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## logout

> logout(serverid, xNonce)

Force a logout on the given session

Force a logout on the given session. Required permission: &#39;sessions&#39;.

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

let apiInstance = new NextAuthApi.SessionsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
apiInstance.logout(serverid, xNonce, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## provokeLogin

> provokeLogin(serverid, xNonce, opts)

Push a login confirmation to the user&#39;s app

Push a login to the nextAuth app for the user to confirm, based on last account that successfully logged in for the given session. Required permission: &#39;sessions&#39;. 

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

let apiInstance = new NextAuthApi.SessionsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
let opts = {
  'userContext': new NextAuthApi.UserContext() // UserContext | Session information to display to user.
};
apiInstance.provokeLogin(serverid, xNonce, opts, (error, data, response) => {
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
 **userContext** | [**UserContext**](UserContext.md)| Session information to display to user. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## provokeLoginOnAccount

> provokeLoginOnAccount(serverid, xNonce, accountid, opts)

Push a login confirmation to the user&#39;s app

Push a login to the nextAuth app for the user to confirm, based on the given account (app instance). Required permission: &#39;sessions&#39; or &#39;accounts&#39;.

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

let apiInstance = new NextAuthApi.SessionsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Base64 encoded nonce to identify the browser/webserver session
let accountid = 56; // Number | Account id
let opts = {
  'userContext': new NextAuthApi.UserContext() // UserContext | Session information to display to user
};
apiInstance.provokeLoginOnAccount(serverid, xNonce, accountid, opts, (error, data, response) => {
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
 **xNonce** | **String**| Base64 encoded nonce to identify the browser/webserver session | 
 **accountid** | **Number**| Account id | 
 **userContext** | [**UserContext**](UserContext.md)| Session information to display to user | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## provokeLoginOnUser

> provokeLoginOnUser(serverid, xNonce, userid, opts)

Push a login confirmation to the user&#39;s app

Push a login to the nextAuth app for the user to confirm, based on the given userid. Required permission: &#39;sessions&#39; or &#39;users&#39;.

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

let apiInstance = new NextAuthApi.SessionsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
let userid = "userid_example"; // String | User name
let opts = {
  'userContext': new NextAuthApi.UserContext() // UserContext | Session information to display to user.
};
apiInstance.provokeLoginOnUser(serverid, xNonce, userid, opts, (error, data, response) => {
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
 **userid** | **String**| User name | 
 **userContext** | [**UserContext**](UserContext.md)| Session information to display to user. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

