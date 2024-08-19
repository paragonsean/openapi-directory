# VictorOps.UsersApi

All URIs are relative to *https://api.victorops.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPublicV1UserGet**](UsersApi.md#apiPublicV1UserGet) | **GET** /api-public/v1/user | List users
[**apiPublicV1UserPost**](UsersApi.md#apiPublicV1UserPost) | **POST** /api-public/v1/user | Add a user
[**apiPublicV1UserUserDelete**](UsersApi.md#apiPublicV1UserUserDelete) | **DELETE** /api-public/v1/user/{user} | Remove a user
[**apiPublicV1UserUserGet**](UsersApi.md#apiPublicV1UserUserGet) | **GET** /api-public/v1/user/{user} | Retrieve information for a user
[**apiPublicV1UserUserPut**](UsersApi.md#apiPublicV1UserUserPut) | **PUT** /api-public/v1/user/{user} | Update a user
[**apiPublicV1UserUserTeamsGet**](UsersApi.md#apiPublicV1UserUserTeamsGet) | **GET** /api-public/v1/user/{user}/teams | Retrieve the user&#39;s team membership



## apiPublicV1UserGet

> ListUserResponse apiPublicV1UserGet(xVOApiId, xVOApiKey)

List users

Get a list of users for your organization  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UsersApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1UserGet(xVOApiId, xVOApiKey, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**ListUserResponse**](ListUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserPost

> V1User apiPublicV1UserPost(xVOApiId, xVOApiKey, body)

Add a user

Add a user to your organization  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UsersApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.AddUserPayload(); // AddUserPayload | 
apiInstance.apiPublicV1UserPost(xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**AddUserPayload**](AddUserPayload.md)|  | 

### Return type

[**V1User**](V1User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserDelete

> apiPublicV1UserUserDelete(xVOApiId, xVOApiKey, user, body)

Remove a user

Remove a user from your organization. If no replacement is specified, an empty JSON payload (\&quot;{}\&quot;) is still required.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UsersApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user to be deleted
let body = new VictorOps.DeleteUserPayload(); // DeleteUserPayload | 
apiInstance.apiPublicV1UserUserDelete(xVOApiId, xVOApiKey, user, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user to be deleted | 
 **body** | [**DeleteUserPayload**](DeleteUserPayload.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiPublicV1UserUserGet

> V1User apiPublicV1UserUserGet(xVOApiId, xVOApiKey, user)

Retrieve information for a user

Get the information for the specified user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UsersApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user to fetch
apiInstance.apiPublicV1UserUserGet(xVOApiId, xVOApiKey, user, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user to fetch | 

### Return type

[**V1User**](V1User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserPut

> V1User apiPublicV1UserUserPut(xVOApiId, xVOApiKey, user, body)

Update a user

Update the designated user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UsersApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user to be updated
let body = new VictorOps.AddUserPayload(); // AddUserPayload | 
apiInstance.apiPublicV1UserUserPut(xVOApiId, xVOApiKey, user, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user to be updated | 
 **body** | [**AddUserPayload**](AddUserPayload.md)|  | 

### Return type

[**V1User**](V1User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserTeamsGet

> UserTeamsResponse apiPublicV1UserUserTeamsGet(xVOApiId, xVOApiKey, user)

Retrieve the user&#39;s team membership

This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UsersApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user
apiInstance.apiPublicV1UserUserTeamsGet(xVOApiId, xVOApiKey, user, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user | 

### Return type

[**UserTeamsResponse**](UserTeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

