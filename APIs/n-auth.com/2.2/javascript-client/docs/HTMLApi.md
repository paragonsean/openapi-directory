# NextAuthApi.HTMLApi

All URIs are relative to *https://api.nextauth.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHtmlEnrol**](HTMLApi.md#getHtmlEnrol) | **GET** /servers/{serverid}/sessions/html/enrol | Generate HTML to enrol a new user
[**getHtmlFooter**](HTMLApi.md#getHtmlFooter) | **GET** /servers/{serverid}/sessions/html/footer | Generic HTML to add to footer. Required for login/logout/enrol functionality.
[**getHtmlLogin**](HTMLApi.md#getHtmlLogin) | **GET** /servers/{serverid}/sessions/html/login | Generate HTML for the login block
[**getSession_0**](HTMLApi.md#getSession_0) | **GET** /servers/{serverid}/sessions/ | Check if the user is logged in
[**logout_0**](HTMLApi.md#logout_0) | **POST** /servers/{serverid}/sessions/logout | Force a logout on the given session



## getHtmlEnrol

> String getHtmlEnrol(serverid, xNonce, opts)

Generate HTML to enrol a new user

Generate HTML to enrol a new user. Required permission: &#39;sessions&#39;. 

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

let apiInstance = new NextAuthApi.HTMLApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
let opts = {
  'name': "name_example", // String | Name to forward to the nextAuth app for this account
  'userid': "userid_example" // String | User name to register this user under
};
apiInstance.getHtmlEnrol(serverid, xNonce, opts, (error, data, response) => {
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
 **name** | **String**| Name to forward to the nextAuth app for this account | [optional] 
 **userid** | **String**| User name to register this user under | [optional] 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html


## getHtmlFooter

> String getHtmlFooter(serverid, xNonce, opts)

Generic HTML to add to footer. Required for login/logout/enrol functionality.

HTML to add to footer of HTML page. Required permission: &#39;sessions&#39;. 

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

let apiInstance = new NextAuthApi.HTMLApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
let opts = {
  'htmlFooterBody': new NextAuthApi.HtmlFooterBody() // HtmlFooterBody | Additional sessions that should be monitored through the websocket.
};
apiInstance.getHtmlFooter(serverid, xNonce, opts, (error, data, response) => {
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
 **htmlFooterBody** | [**HtmlFooterBody**](HtmlFooterBody.md)| Additional sessions that should be monitored through the websocket. | [optional] 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/html


## getHtmlLogin

> String getHtmlLogin(serverid, xNonce, opts)

Generate HTML for the login block

Generate HTML for the login block. Required permission: &#39;sessions&#39;. 

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

let apiInstance = new NextAuthApi.HTMLApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
let opts = {
  'userContext': new NextAuthApi.UserContext() // UserContext | Session information to display to user.
};
apiInstance.getHtmlLogin(serverid, xNonce, opts, (error, data, response) => {
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
 **userContext** | [**UserContext**](UserContext.md)| Session information to display to user. | [optional] 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/html


## getSession_0

> LoginStatus getSession_0(serverid, xNonce)

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

let apiInstance = new NextAuthApi.HTMLApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
apiInstance.getSession_0(serverid, xNonce, (error, data, response) => {
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


## logout_0

> logout_0(serverid, xNonce)

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

let apiInstance = new NextAuthApi.HTMLApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
apiInstance.logout_0(serverid, xNonce, (error, data, response) => {
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

