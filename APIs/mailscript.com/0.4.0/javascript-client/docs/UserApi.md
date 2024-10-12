# Mailscript.UserApi

All URIs are relative to *https://api.mailscript.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAuthenticatedUser**](UserApi.md#getAuthenticatedUser) | **GET** /user | Get the authenticated user
[**updateUser**](UserApi.md#updateUser) | **PUT** /user | Update a user



## getAuthenticatedUser

> User getAuthenticatedUser()

Get the authenticated user

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.UserApi();
apiInstance.getAuthenticatedUser((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateUser

> updateUser(updateUserRequest)

Update a user

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.UserApi();
let updateUserRequest = new Mailscript.UpdateUserRequest(); // UpdateUserRequest | User body
apiInstance.updateUser(updateUserRequest, (error, data, response) => {
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
 **updateUserRequest** | [**UpdateUserRequest**](UpdateUserRequest.md)| User body | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

