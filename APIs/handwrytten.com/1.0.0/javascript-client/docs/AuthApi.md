# HandwryttenApi.AuthApi

All URIs are relative to *https://api.handwrytten.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changePassword**](AuthApi.md#changePassword) | **POST** /auth/changePassword | changes a user&#39;s password
[**login**](AuthApi.md#login) | **POST** /auth/authorization | Logs in to an existing account
[**logout**](AuthApi.md#logout) | **POST** /auth/logout | logs out a session uid
[**register**](AuthApi.md#register) | **POST** /auth/register | Registers a new account
[**resetPasswordRequest**](AuthApi.md#resetPasswordRequest) | **POST** /auth/resetPasswordRequest | resets a user&#39;s password



## changePassword

> ChangePassword200Response changePassword(body)

changes a user&#39;s password

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.AuthApi();
let body = new HandwryttenApi.ChangePasswordRequest(); // ChangePasswordRequest | Change password
apiInstance.changePassword(body, (error, data, response) => {
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
 **body** | [**ChangePasswordRequest**](ChangePasswordRequest.md)| Change password | 

### Return type

[**ChangePassword200Response**](ChangePassword200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## login

> Login200Response login(body)

Logs in to an existing account

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.AuthApi();
let body = new HandwryttenApi.Login(); // Login | Login to account
apiInstance.login(body, (error, data, response) => {
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
 **body** | [**Login**](Login.md)| Login to account | 

### Return type

[**Login200Response**](Login200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## logout

> ChangePassword200Response logout(body)

logs out a session uid

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.AuthApi();
let body = new HandwryttenApi.LogoutRequest(); // LogoutRequest | logout session
apiInstance.logout(body, (error, data, response) => {
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
 **body** | [**LogoutRequest**](LogoutRequest.md)| logout session | 

### Return type

[**ChangePassword200Response**](ChangePassword200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## register

> Register200Response register(body)

Registers a new account

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.AuthApi();
let body = new HandwryttenApi.Registration(); // Registration | New user account information
apiInstance.register(body, (error, data, response) => {
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
 **body** | [**Registration**](Registration.md)| New user account information | 

### Return type

[**Register200Response**](Register200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resetPasswordRequest

> ChangePassword200Response resetPasswordRequest(body)

resets a user&#39;s password

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.AuthApi();
let body = new HandwryttenApi.ResetPasswordRequestRequest(); // ResetPasswordRequestRequest | Reset password
apiInstance.resetPasswordRequest(body, (error, data, response) => {
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
 **body** | [**ResetPasswordRequestRequest**](ResetPasswordRequestRequest.md)| Reset password | 

### Return type

[**ChangePassword200Response**](ChangePassword200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

