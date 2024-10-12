# PocketSmith.UsersApi

All URIs are relative to *https://api.pocketsmith.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meGet**](UsersApi.md#meGet) | **GET** /me | Get the authorised user
[**usersIdGet**](UsersApi.md#usersIdGet) | **GET** /users/{id} | Get user
[**usersIdPut**](UsersApi.md#usersIdPut) | **PUT** /users/{id} | Update user



## meGet

> User meGet()

Get the authorised user

Gets the user that corresponds to the access token used in the request.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.UsersApi();
apiInstance.meGet((error, data, response) => {
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

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdGet

> User usersIdGet(id)

Get user

Gets a user by ID. You must be authorised as the target user in order to make this request.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.UsersApi();
let id = 42; // Number | The unique identifier of the user.
apiInstance.usersIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the user. | 

### Return type

[**User**](User.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdPut

> User usersIdPut(id, opts)

Update user

Updates the user by their ID. You must be authorised as the target user in order to make this request.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.UsersApi();
let id = 42; // Number | The unique identifier of the user.
let opts = {
  'usersIdPutRequest': new PocketSmith.UsersIdPutRequest() // UsersIdPutRequest | 
};
apiInstance.usersIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the user. | 
 **usersIdPutRequest** | [**UsersIdPutRequest**](UsersIdPutRequest.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

