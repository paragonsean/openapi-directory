# Apacta.UserCustomFieldValueApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersUserIdUserCustomFieldValueGet**](UserCustomFieldValueApi.md#usersUserIdUserCustomFieldValueGet) | **GET** /users/{user_id}/user_custom_field_value | Get a list of user custom field values
[**usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet**](UserCustomFieldValueApi.md#usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet) | **GET** /users/{user_id}/user_custom_field_value/{user_custom_field_value_id} | Get a single record of user custom field value
[**usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut**](UserCustomFieldValueApi.md#usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut) | **PUT** /users/{user_id}/user_custom_field_value/{user_custom_field_value_id} | Update a single record of user custom field value



## usersUserIdUserCustomFieldValueGet

> UsersUserIdUserCustomFieldValueGet200Response usersUserIdUserCustomFieldValueGet(userId)

Get a list of user custom field values

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UserCustomFieldValueApi();
let userId = "userId_example"; // String | Automatically added
apiInstance.usersUserIdUserCustomFieldValueGet(userId, (error, data, response) => {
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
 **userId** | **String**| Automatically added | 

### Return type

[**UsersUserIdUserCustomFieldValueGet200Response**](UsersUserIdUserCustomFieldValueGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet

> UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet(userId, userCustomFieldValueId)

Get a single record of user custom field value

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UserCustomFieldValueApi();
let userId = "userId_example"; // String | Automatically added
let userCustomFieldValueId = "userCustomFieldValueId_example"; // String | Automatically added
apiInstance.usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet(userId, userCustomFieldValueId, (error, data, response) => {
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
 **userId** | **String**| Automatically added | 
 **userCustomFieldValueId** | **String**| Automatically added | 

### Return type

[**UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response**](UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut

> UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut(userId, userCustomFieldValueId)

Update a single record of user custom field value

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.UserCustomFieldValueApi();
let userId = "userId_example"; // String | Automatically added
let userCustomFieldValueId = "userCustomFieldValueId_example"; // String | Automatically added
apiInstance.usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut(userId, userCustomFieldValueId, (error, data, response) => {
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
 **userId** | **String**| Automatically added | 
 **userCustomFieldValueId** | **String**| Automatically added | 

### Return type

[**UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response**](UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

