# PeerTube.UsersApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addUser**](UsersApi.md#addUser) | **POST** /api/v1/users | Create a user
[**confirmTwoFactorRequest**](UsersApi.md#confirmTwoFactorRequest) | **POST** /api/v1/users/{id}/two-factor/confirm-request | Confirm two factor auth
[**delUser**](UsersApi.md#delUser) | **DELETE** /api/v1/users/{id} | Delete a user
[**disableTwoFactor**](UsersApi.md#disableTwoFactor) | **POST** /api/v1/users/{id}/two-factor/disable | Disable two factor auth
[**getUser**](UsersApi.md#getUser) | **GET** /api/v1/users/{id} | Get a user
[**getUsers**](UsersApi.md#getUsers) | **GET** /api/v1/users | List users
[**putUser**](UsersApi.md#putUser) | **PUT** /api/v1/users/{id} | Update a user
[**requestTwoFactor**](UsersApi.md#requestTwoFactor) | **POST** /api/v1/users/{id}/two-factor/request | Request two factor auth
[**resendEmailToVerifyUser**](UsersApi.md#resendEmailToVerifyUser) | **POST** /api/v1/users/ask-send-verify-email | Resend user verification link
[**verifyUser**](UsersApi.md#verifyUser) | **POST** /api/v1/users/{id}/verify-email | Verify a user



## addUser

> AddUserResponse addUser(addUser)

Create a user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.UsersApi();
let addUser = new PeerTube.AddUser(); // AddUser | If the smtp server is configured, you can leave the password empty and an email will be sent asking the user to set it first. 
apiInstance.addUser(addUser, (error, data, response) => {
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
 **addUser** | [**AddUser**](AddUser.md)| If the smtp server is configured, you can leave the password empty and an email will be sent asking the user to set it first.  | 

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## confirmTwoFactorRequest

> confirmTwoFactorRequest(id, opts)

Confirm two factor auth

Confirm a two factor authentication request

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.UsersApi();
let id = 56; // Number | Entity id
let opts = {
  'confirmTwoFactorRequestRequest': new PeerTube.ConfirmTwoFactorRequestRequest() // ConfirmTwoFactorRequestRequest | 
};
apiInstance.confirmTwoFactorRequest(id, opts, (error, data, response) => {
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
 **id** | **Number**| Entity id | 
 **confirmTwoFactorRequestRequest** | [**ConfirmTwoFactorRequestRequest**](ConfirmTwoFactorRequestRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## delUser

> delUser(id)

Delete a user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.UsersApi();
let id = 56; // Number | Entity id
apiInstance.delUser(id, (error, data, response) => {
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
 **id** | **Number**| Entity id | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## disableTwoFactor

> disableTwoFactor(id, opts)

Disable two factor auth

Disable two factor authentication of a user

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.UsersApi();
let id = 56; // Number | Entity id
let opts = {
  'disableTwoFactorRequest': new PeerTube.DisableTwoFactorRequest() // DisableTwoFactorRequest | 
};
apiInstance.disableTwoFactor(id, opts, (error, data, response) => {
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
 **id** | **Number**| Entity id | 
 **disableTwoFactorRequest** | [**DisableTwoFactorRequest**](DisableTwoFactorRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getUser

> GetUser200Response getUser(id, opts)

Get a user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.UsersApi();
let id = 56; // Number | Entity id
let opts = {
  'withStats': true // Boolean | include statistics about the user (only available as a moderator/admin)
};
apiInstance.getUser(id, opts, (error, data, response) => {
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
 **id** | **Number**| Entity id | 
 **withStats** | **Boolean**| include statistics about the user (only available as a moderator/admin) | [optional] 

### Return type

[**GetUser200Response**](GetUser200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsers

> [User] getUsers(opts)

List users

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.UsersApi();
let opts = {
  'search': "search_example", // String | Plain text search that will match with user usernames or emails
  'blocked': true, // Boolean | Filter results down to (un)banned users
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "sort_example" // String | Sort users by criteria
};
apiInstance.getUsers(opts, (error, data, response) => {
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
 **search** | **String**| Plain text search that will match with user usernames or emails | [optional] 
 **blocked** | **Boolean**| Filter results down to (un)banned users | [optional] 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort users by criteria | [optional] 

### Return type

[**[User]**](User.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putUser

> putUser(id, updateUser)

Update a user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.UsersApi();
let id = 56; // Number | Entity id
let updateUser = new PeerTube.UpdateUser(); // UpdateUser | 
apiInstance.putUser(id, updateUser, (error, data, response) => {
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
 **id** | **Number**| Entity id | 
 **updateUser** | [**UpdateUser**](UpdateUser.md)|  | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## requestTwoFactor

> [RequestTwoFactorResponse] requestTwoFactor(id, opts)

Request two factor auth

Request two factor authentication for a user

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.UsersApi();
let id = 56; // Number | Entity id
let opts = {
  'disableTwoFactorRequest': new PeerTube.DisableTwoFactorRequest() // DisableTwoFactorRequest | 
};
apiInstance.requestTwoFactor(id, opts, (error, data, response) => {
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
 **id** | **Number**| Entity id | 
 **disableTwoFactorRequest** | [**DisableTwoFactorRequest**](DisableTwoFactorRequest.md)|  | [optional] 

### Return type

[**[RequestTwoFactorResponse]**](RequestTwoFactorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resendEmailToVerifyUser

> resendEmailToVerifyUser(opts)

Resend user verification link

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.UsersApi();
let opts = {
  'resendEmailToVerifyUserRequest': new PeerTube.ResendEmailToVerifyUserRequest() // ResendEmailToVerifyUserRequest | 
};
apiInstance.resendEmailToVerifyUser(opts, (error, data, response) => {
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
 **resendEmailToVerifyUserRequest** | [**ResendEmailToVerifyUserRequest**](ResendEmailToVerifyUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## verifyUser

> verifyUser(id, opts)

Verify a user

Following a user registration, the new user will receive an email asking to click a link containing a secret. This endpoint can also be used to verify a new email set in the user account. 

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.UsersApi();
let id = 56; // Number | Entity id
let opts = {
  'verifyUserRequest': new PeerTube.VerifyUserRequest() // VerifyUserRequest | 
};
apiInstance.verifyUser(id, opts, (error, data, response) => {
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
 **id** | **Number**| Entity id | 
 **verifyUserRequest** | [**VerifyUserRequest**](VerifyUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

