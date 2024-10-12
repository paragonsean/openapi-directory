# IoEIoTApiToCreateEndUserApplications.AuthenticationApi

All URIs are relative to *https://ioe2api.ijenko.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authAccountLogin**](AuthenticationApi.md#authAccountLogin) | **POST** /auth/login | Get a token using login+password
[**authRefreshToken**](AuthenticationApi.md#authRefreshToken) | **POST** /auth/refresh | Refresh a token
[**authResetPassword**](AuthenticationApi.md#authResetPassword) | **POST** /auth/reset-password | Ask for a new password
[**authRevokeToken**](AuthenticationApi.md#authRevokeToken) | **POST** /auth/revoke | Revoke a token



## authAccountLogin

> AuthTokens authAccountLogin(loginInfo)

Get a token using login+password

Get an access+refresh tokens pair from login and password information.  The *access token* obtained with this request can then be used in an &#x60;Access-Token&#x60; HTTP header or in a &#x60;token&#x60; URL query parameter in requests that require authentication.  The *refresh token* can be used with &#x60;/auth/refresh&#x60; when the *access token* expires to retrieve a new *access token*. The lifetime of the refresh token is the maximum lifetime of this authentication request.  The default lifetime of the *refresh token* is defined by the &#x60;appId&#x60; used. The &#x60;ttl&#x60; input parameter allows to request a *refresh token* with a shorter lifetime.  To implement *logout*, use &#x60;/auth/revoke&#x60;. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.AuthenticationApi();
let loginInfo = new IoEIoTApiToCreateEndUserApplications.AuthLogin(); // AuthLogin | Login information.
apiInstance.authAccountLogin(loginInfo, (error, data, response) => {
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
 **loginInfo** | [**AuthLogin**](AuthLogin.md)| Login information. | 

### Return type

[**AuthTokens**](AuthTokens.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## authRefreshToken

> AuthTokens authRefreshToken(refreshInfo)

Refresh a token

Get a new *access token* using a valid *refresh token*.  This is a **replacement** of the *access token*: if an existing *access token* was still not expired, it is invalidated. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.AuthenticationApi();
let refreshInfo = new IoEIoTApiToCreateEndUserApplications.AuthRefresh(); // AuthRefresh | Refresh token information.
apiInstance.authRefreshToken(refreshInfo, (error, data, response) => {
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
 **refreshInfo** | [**AuthRefresh**](AuthRefresh.md)| Refresh token information. | 

### Return type

[**AuthTokens**](AuthTokens.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## authResetPassword

> authResetPassword(resetPasswordInfo)

Ask for a new password

Trigger the request of a new password.  The account administrator will receive an e-mail with an URL pointing to a form to allow him/her to enter a new password. The old password is still functional until a new one is submitted.  Either the login or e-mail of the account must be given. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.AuthenticationApi();
let resetPasswordInfo = new IoEIoTApiToCreateEndUserApplications.AuthResetPassword(); // AuthResetPassword | Account identification information
apiInstance.authResetPassword(resetPasswordInfo, (error, data, response) => {
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
 **resetPasswordInfo** | [**AuthResetPassword**](AuthResetPassword.md)| Account identification information | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## authRevokeToken

> authRevokeToken()

Revoke a token

Invalidate the authentication used for the request. The access token and the refresh token will be invalid after this request. This request is typically called to implement logout. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.AuthenticationApi();
apiInstance.authRevokeToken((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

