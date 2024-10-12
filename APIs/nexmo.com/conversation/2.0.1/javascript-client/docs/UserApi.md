# ConversationApi.UserApi

All URIs are relative to *https://api.nexmo.com/v0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUser**](UserApi.md#createUser) | **POST** /users | Create a user
[**deleteUser**](UserApi.md#deleteUser) | **DELETE** /users/{user_id} | Delete a user
[**getUser**](UserApi.md#getUser) | **GET** /users/{user_id} | Retrieve a user
[**getUsers**](UserApi.md#getUsers) | **GET** /users | List users
[**getuserConversations**](UserApi.md#getuserConversations) | **GET** /users/{user_id}/conversations | List user conversations
[**updateUser**](UserApi.md#updateUser) | **PUT** /users/{user_id} | Update a user



## createUser

> CreateUser200Response createUser(opts)

Create a user

Note: Users must be created with an admin JWT.

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.UserApi();
let opts = {
  'createUserRequest': new ConversationApi.CreateUserRequest() // CreateUserRequest | 
};
apiInstance.createUser(opts, (error, data, response) => {
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
 **createUserRequest** | [**CreateUserRequest**](CreateUserRequest.md)|  | [optional] 

### Return type

[**CreateUser200Response**](CreateUser200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteUser

> Object deleteUser(userId)

Delete a user

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.UserApi();
let userId = "userId_example"; // String | User ID
apiInstance.deleteUser(userId, (error, data, response) => {
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
 **userId** | **String**| User ID | 

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUser

> GetUser200Response getUser(userId)

Retrieve a user

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.UserApi();
let userId = "userId_example"; // String | User ID
apiInstance.getUser(userId, (error, data, response) => {
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
 **userId** | **String**| User ID | 

### Return type

[**GetUser200Response**](GetUser200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsers

> [GetUsers200ResponseInner] getUsers()

List users

This endpoint is **DEPRECATED**. Please use [/v0.2/users](/api/conversation.v2#get-users).

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.UserApi();
apiInstance.getUsers((error, data, response) => {
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

[**[GetUsers200ResponseInner]**](GetUsers200ResponseInner.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getuserConversations

> [GetuserConversations200ResponseInner] getuserConversations(userId)

List user conversations

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.UserApi();
let userId = "userId_example"; // String | User ID
apiInstance.getuserConversations(userId, (error, data, response) => {
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
 **userId** | **String**| User ID | 

### Return type

[**[GetuserConversations200ResponseInner]**](GetuserConversations200ResponseInner.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateUser

> UpdateUser200Response updateUser(userId, opts)

Update a user

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.UserApi();
let userId = "userId_example"; // String | User ID
let opts = {
  'updateUserRequest': new ConversationApi.UpdateUserRequest() // UpdateUserRequest | 
};
apiInstance.updateUser(userId, opts, (error, data, response) => {
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
 **userId** | **String**| User ID | 
 **updateUserRequest** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | [optional] 

### Return type

[**UpdateUser200Response**](UpdateUser200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

