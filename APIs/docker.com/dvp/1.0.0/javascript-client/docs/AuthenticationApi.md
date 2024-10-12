# DvpDataApi.AuthenticationApi

All URIs are relative to *https://hub.docker.com/api/publisher/analytics/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postUsers2FALogin**](AuthenticationApi.md#postUsers2FALogin) | **POST** /v2/users/2fa-login | Second factor authentication.
[**postUsersLogin**](AuthenticationApi.md#postUsersLogin) | **POST** /v2/users/login | Create an authentication token



## postUsers2FALogin

> PostUsersLoginSuccessResponse postUsers2FALogin(users2FALoginRequest)

Second factor authentication.

When a user has 2FA enabled, this is the second call to perform after &#x60;/v2/users/login&#x60; call.  Creates and returns a bearer token in JWT format that you can use to authenticate with Docker Hub APIs.  The returned token is used in the HTTP Authorization header like &#x60;Authorization: Bearer {TOKEN}&#x60;.  Most Docker Hub APIs require this token either to consume or to get detailed information. For example, to list images in a private repository. 

### Example

```javascript
import DvpDataApi from 'dvp_data_api';

let apiInstance = new DvpDataApi.AuthenticationApi();
let users2FALoginRequest = new DvpDataApi.Users2FALoginRequest(); // Users2FALoginRequest | Login details.
apiInstance.postUsers2FALogin(users2FALoginRequest, (error, data, response) => {
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
 **users2FALoginRequest** | [**Users2FALoginRequest**](Users2FALoginRequest.md)| Login details. | 

### Return type

[**PostUsersLoginSuccessResponse**](PostUsersLoginSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postUsersLogin

> PostUsersLoginSuccessResponse postUsersLogin(usersLoginRequest)

Create an authentication token

Creates and returns a bearer token in JWT format that you can use to authenticate with Docker Hub APIs.  The returned token is used in the HTTP Authorization header like &#x60;Authorization: Bearer {TOKEN}&#x60;.  Most Docker Hub APIs require this token either to consume or to get detailed information. For example, to list images in a private repository. 

### Example

```javascript
import DvpDataApi from 'dvp_data_api';

let apiInstance = new DvpDataApi.AuthenticationApi();
let usersLoginRequest = new DvpDataApi.UsersLoginRequest(); // UsersLoginRequest | Login details.
apiInstance.postUsersLogin(usersLoginRequest, (error, data, response) => {
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
 **usersLoginRequest** | [**UsersLoginRequest**](UsersLoginRequest.md)| Login details. | 

### Return type

[**PostUsersLoginSuccessResponse**](PostUsersLoginSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

