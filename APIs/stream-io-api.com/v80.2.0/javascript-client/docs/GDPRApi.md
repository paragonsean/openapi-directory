# StreamChatApi.GDPRApi

All URIs are relative to *https://chat.stream-io-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deactivateUser_0**](GDPRApi.md#deactivateUser_0) | **POST** /users/{user_id}/deactivate | Deactivate user
[**deactivateUsers_0**](GDPRApi.md#deactivateUsers_0) | **POST** /users/deactivate | Deactivate users
[**deleteChannels_0**](GDPRApi.md#deleteChannels_0) | **POST** /channels/delete | Deletes channels asynchronously
[**deleteUser_0**](GDPRApi.md#deleteUser_0) | **DELETE** /users/{user_id} | Delete user
[**deleteUsers_0**](GDPRApi.md#deleteUsers_0) | **POST** /users/delete | Delete Users
[**reactivateUser_0**](GDPRApi.md#reactivateUser_0) | **POST** /users/{user_id}/reactivate | Reactivate user
[**reactivateUsers_0**](GDPRApi.md#reactivateUsers_0) | **POST** /users/reactivate | Reactivate users



## deactivateUser_0

> DeactivateUserResponse deactivateUser_0(userId, deactivateUserRequest)

Deactivate user

Deactivates user with possibility to activate it back  Sends events: - user.deactivated 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.GDPRApi();
let userId = "userId_example"; // String | 
let deactivateUserRequest = new StreamChatApi.DeactivateUserRequest(); // DeactivateUserRequest | 
apiInstance.deactivateUser_0(userId, deactivateUserRequest, (error, data, response) => {
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
 **userId** | **String**|  | 
 **deactivateUserRequest** | [**DeactivateUserRequest**](DeactivateUserRequest.md)|  | 

### Return type

[**DeactivateUserResponse**](DeactivateUserResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deactivateUsers_0

> DeactivateUsersResponse deactivateUsers_0(deactivateUsersRequest)

Deactivate users

Deactivate users in batches  Sends events: - user.deactivated 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.GDPRApi();
let deactivateUsersRequest = new StreamChatApi.DeactivateUsersRequest(); // DeactivateUsersRequest | 
apiInstance.deactivateUsers_0(deactivateUsersRequest, (error, data, response) => {
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
 **deactivateUsersRequest** | [**DeactivateUsersRequest**](DeactivateUsersRequest.md)|  | 

### Return type

[**DeactivateUsersResponse**](DeactivateUsersResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteChannels_0

> DeleteChannelsResponse deleteChannels_0(deleteChannelsRequest)

Deletes channels asynchronously

Allows to delete several channels at once asynchronously  Sends events: - channel.deleted  Required permissions: - DeleteChannel 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.GDPRApi();
let deleteChannelsRequest = new StreamChatApi.DeleteChannelsRequest(); // DeleteChannelsRequest | 
apiInstance.deleteChannels_0(deleteChannelsRequest, (error, data, response) => {
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
 **deleteChannelsRequest** | [**DeleteChannelsRequest**](DeleteChannelsRequest.md)|  | 

### Return type

[**DeleteChannelsResponse**](DeleteChannelsResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteUser_0

> DeleteUserResponse deleteUser_0(userId, opts)

Delete user

Deletes user and optionally all their belongings. The Endpoint is deprecated, please use &#39;Delete Users&#39; endpoint instead  Sends events: - channel.deleted - message.deleted - user.deleted 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.GDPRApi();
let userId = "userId_example"; // String | 
let opts = {
  'markMessagesDeleted': true, // Boolean | 
  'hardDelete': true, // Boolean | 
  'deleteConversationChannels': true // Boolean | 
};
apiInstance.deleteUser_0(userId, opts, (error, data, response) => {
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
 **userId** | **String**|  | 
 **markMessagesDeleted** | **Boolean**|  | [optional] 
 **hardDelete** | **Boolean**|  | [optional] 
 **deleteConversationChannels** | **Boolean**|  | [optional] 

### Return type

[**DeleteUserResponse**](DeleteUserResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteUsers_0

> DeleteUsersResponse deleteUsers_0(deleteUsersRequest)

Delete Users

Deletes users and optionally all their belongings asynchronously.  Sends events: - channel.deleted - user.deleted 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.GDPRApi();
let deleteUsersRequest = new StreamChatApi.DeleteUsersRequest(); // DeleteUsersRequest | 
apiInstance.deleteUsers_0(deleteUsersRequest, (error, data, response) => {
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
 **deleteUsersRequest** | [**DeleteUsersRequest**](DeleteUsersRequest.md)|  | 

### Return type

[**DeleteUsersResponse**](DeleteUsersResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reactivateUser_0

> ReactivateUserResponse reactivateUser_0(userId, reactivateUserRequest)

Reactivate user

Activates user who&#39;s been deactivated previously  Sends events: - user.reactivated 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.GDPRApi();
let userId = "userId_example"; // String | 
let reactivateUserRequest = new StreamChatApi.ReactivateUserRequest(); // ReactivateUserRequest | 
apiInstance.reactivateUser_0(userId, reactivateUserRequest, (error, data, response) => {
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
 **userId** | **String**|  | 
 **reactivateUserRequest** | [**ReactivateUserRequest**](ReactivateUserRequest.md)|  | 

### Return type

[**ReactivateUserResponse**](ReactivateUserResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reactivateUsers_0

> ReactivateUsersResponse reactivateUsers_0(reactivateUsersRequest)

Reactivate users

Reactivate users in batches  Sends events: - user.reactivated 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.GDPRApi();
let reactivateUsersRequest = new StreamChatApi.ReactivateUsersRequest(); // ReactivateUsersRequest | 
apiInstance.reactivateUsers_0(reactivateUsersRequest, (error, data, response) => {
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
 **reactivateUsersRequest** | [**ReactivateUsersRequest**](ReactivateUsersRequest.md)|  | 

### Return type

[**ReactivateUsersResponse**](ReactivateUsersResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

