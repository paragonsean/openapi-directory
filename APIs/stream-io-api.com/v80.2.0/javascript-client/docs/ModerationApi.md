# StreamChatApi.ModerationApi

All URIs are relative to *https://chat.stream-io-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ban_0**](ModerationApi.md#ban_0) | **POST** /moderation/ban | Ban user
[**createBlockList_0**](ModerationApi.md#createBlockList_0) | **POST** /blocklists | Create block list
[**deactivateUser_1**](ModerationApi.md#deactivateUser_1) | **POST** /users/{user_id}/deactivate | Deactivate user
[**deactivateUsers_1**](ModerationApi.md#deactivateUsers_1) | **POST** /users/deactivate | Deactivate users
[**deleteBlockList_0**](ModerationApi.md#deleteBlockList_0) | **DELETE** /blocklists/{name} | Delete block list
[**deleteUser_1**](ModerationApi.md#deleteUser_1) | **DELETE** /users/{user_id} | Delete user
[**deleteUsers_1**](ModerationApi.md#deleteUsers_1) | **POST** /users/delete | Delete Users
[**flag**](ModerationApi.md#flag) | **POST** /moderation/flag | Flag
[**getBlockList_0**](ModerationApi.md#getBlockList_0) | **GET** /blocklists/{name} | Get block list
[**listBlockLists_0**](ModerationApi.md#listBlockLists_0) | **GET** /blocklists | List block lists
[**muteUser_0**](ModerationApi.md#muteUser_0) | **POST** /moderation/mute | Mute user
[**queryBannedUsers_0**](ModerationApi.md#queryBannedUsers_0) | **GET** /query_banned_users | Query Banned Users
[**queryMessageFlags_0**](ModerationApi.md#queryMessageFlags_0) | **GET** /moderation/flags/message | Query Message Flags
[**reactivateUser_1**](ModerationApi.md#reactivateUser_1) | **POST** /users/{user_id}/reactivate | Reactivate user
[**reactivateUsers_1**](ModerationApi.md#reactivateUsers_1) | **POST** /users/reactivate | Reactivate users
[**unban_0**](ModerationApi.md#unban_0) | **DELETE** /moderation/ban | Unban user
[**unflag**](ModerationApi.md#unflag) | **POST** /moderation/unflag | Unflag
[**unmuteUser_0**](ModerationApi.md#unmuteUser_0) | **POST** /moderation/unmute | Unmute user
[**updateBlockList_0**](ModerationApi.md#updateBlockList_0) | **PUT** /blocklists/{name} | Update block list



## ban_0

> Response ban_0(banRequest)

Ban user

Restricts user activity either in specific channel or globally  Sends events: - user.banned  Required permissions: - BanChannelMember - BanUser 

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

let apiInstance = new StreamChatApi.ModerationApi();
let banRequest = new StreamChatApi.BanRequest(); // BanRequest | 
apiInstance.ban_0(banRequest, (error, data, response) => {
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
 **banRequest** | [**BanRequest**](BanRequest.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBlockList_0

> Response createBlockList_0(createBlockListRequest)

Create block list

Creates a new application blocklist, once created the blocklist can be used by any channel type 

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

let apiInstance = new StreamChatApi.ModerationApi();
let createBlockListRequest = new StreamChatApi.CreateBlockListRequest(); // CreateBlockListRequest | Block list
apiInstance.createBlockList_0(createBlockListRequest, (error, data, response) => {
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
 **createBlockListRequest** | [**CreateBlockListRequest**](CreateBlockListRequest.md)| Block list | 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deactivateUser_1

> DeactivateUserResponse deactivateUser_1(userId, deactivateUserRequest)

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

let apiInstance = new StreamChatApi.ModerationApi();
let userId = "userId_example"; // String | 
let deactivateUserRequest = new StreamChatApi.DeactivateUserRequest(); // DeactivateUserRequest | 
apiInstance.deactivateUser_1(userId, deactivateUserRequest, (error, data, response) => {
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


## deactivateUsers_1

> DeactivateUsersResponse deactivateUsers_1(deactivateUsersRequest)

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

let apiInstance = new StreamChatApi.ModerationApi();
let deactivateUsersRequest = new StreamChatApi.DeactivateUsersRequest(); // DeactivateUsersRequest | 
apiInstance.deactivateUsers_1(deactivateUsersRequest, (error, data, response) => {
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


## deleteBlockList_0

> Response deleteBlockList_0(name)

Delete block list

Deletes previously created application blocklist 

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

let apiInstance = new StreamChatApi.ModerationApi();
let name = "name_example"; // String | 
apiInstance.deleteBlockList_0(name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteUser_1

> DeleteUserResponse deleteUser_1(userId, opts)

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

let apiInstance = new StreamChatApi.ModerationApi();
let userId = "userId_example"; // String | 
let opts = {
  'markMessagesDeleted': true, // Boolean | 
  'hardDelete': true, // Boolean | 
  'deleteConversationChannels': true // Boolean | 
};
apiInstance.deleteUser_1(userId, opts, (error, data, response) => {
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


## deleteUsers_1

> DeleteUsersResponse deleteUsers_1(deleteUsersRequest)

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

let apiInstance = new StreamChatApi.ModerationApi();
let deleteUsersRequest = new StreamChatApi.DeleteUsersRequest(); // DeleteUsersRequest | 
apiInstance.deleteUsers_1(deleteUsersRequest, (error, data, response) => {
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


## flag

> FlagResponse flag(flagRequest)

Flag

Reports message or user for review by moderators  Sends events: - message.flagged - user.flagged  Required permissions: - FlagMessage - FlagUser 

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

let apiInstance = new StreamChatApi.ModerationApi();
let flagRequest = new StreamChatApi.FlagRequest(); // FlagRequest | 
apiInstance.flag(flagRequest, (error, data, response) => {
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
 **flagRequest** | [**FlagRequest**](FlagRequest.md)|  | 

### Return type

[**FlagResponse**](FlagResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getBlockList_0

> GetBlockListResponse getBlockList_0(name)

Get block list

Returns block list by given name 

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

let apiInstance = new StreamChatApi.ModerationApi();
let name = "name_example"; // String | 
apiInstance.getBlockList_0(name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

[**GetBlockListResponse**](GetBlockListResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBlockLists_0

> ListBlockListResponse listBlockLists_0()

List block lists

Returns all available block lists 

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

let apiInstance = new StreamChatApi.ModerationApi();
apiInstance.listBlockLists_0((error, data, response) => {
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

[**ListBlockListResponse**](ListBlockListResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## muteUser_0

> MuteUserResponse muteUser_0(muteUserRequest)

Mute user

Mutes one or several users  Sends events: - user.muted  Required permissions: - MuteUser 

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

let apiInstance = new StreamChatApi.ModerationApi();
let muteUserRequest = new StreamChatApi.MuteUserRequest(); // MuteUserRequest | 
apiInstance.muteUser_0(muteUserRequest, (error, data, response) => {
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
 **muteUserRequest** | [**MuteUserRequest**](MuteUserRequest.md)|  | 

### Return type

[**MuteUserResponse**](MuteUserResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryBannedUsers_0

> QueryBannedUsersResponse queryBannedUsers_0(opts)

Query Banned Users

Find and filter channel scoped or global user bans  Required permissions: - ReadChannel 

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

let apiInstance = new StreamChatApi.ModerationApi();
let opts = {
  'payload': new StreamChatApi.QueryBannedUsersRequest() // QueryBannedUsersRequest | 
};
apiInstance.queryBannedUsers_0(opts, (error, data, response) => {
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
 **payload** | [**QueryBannedUsersRequest**](.md)|  | [optional] 

### Return type

[**QueryBannedUsersResponse**](QueryBannedUsersResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryMessageFlags_0

> QueryMessageFlagsResponse queryMessageFlags_0(opts)

Query Message Flags

Find and filter message flags  Required permissions: - ReadMessageFlags 

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

let apiInstance = new StreamChatApi.ModerationApi();
let opts = {
  'payload': new StreamChatApi.QueryMessageFlagsRequest() // QueryMessageFlagsRequest | 
};
apiInstance.queryMessageFlags_0(opts, (error, data, response) => {
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
 **payload** | [**QueryMessageFlagsRequest**](.md)|  | [optional] 

### Return type

[**QueryMessageFlagsResponse**](QueryMessageFlagsResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reactivateUser_1

> ReactivateUserResponse reactivateUser_1(userId, reactivateUserRequest)

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

let apiInstance = new StreamChatApi.ModerationApi();
let userId = "userId_example"; // String | 
let reactivateUserRequest = new StreamChatApi.ReactivateUserRequest(); // ReactivateUserRequest | 
apiInstance.reactivateUser_1(userId, reactivateUserRequest, (error, data, response) => {
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


## reactivateUsers_1

> ReactivateUsersResponse reactivateUsers_1(reactivateUsersRequest)

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

let apiInstance = new StreamChatApi.ModerationApi();
let reactivateUsersRequest = new StreamChatApi.ReactivateUsersRequest(); // ReactivateUsersRequest | 
apiInstance.reactivateUsers_1(reactivateUsersRequest, (error, data, response) => {
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


## unban_0

> Response unban_0(opts)

Unban user

Removes previously applied ban  Sends events: - user.unbanned  Required permissions: - BanChannelMember - BanUser 

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

let apiInstance = new StreamChatApi.ModerationApi();
let opts = {
  'targetUserId': "targetUserId_example", // String | 
  'type': "type_example", // String | 
  'id': "id_example" // String | 
};
apiInstance.unban_0(opts, (error, data, response) => {
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
 **targetUserId** | **String**|  | [optional] 
 **type** | **String**|  | [optional] 
 **id** | **String**|  | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unflag

> FlagResponse unflag(flagRequest)

Unflag

Removes previously created user or message flag  Required permissions: - FlagMessage - FlagUser 

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

let apiInstance = new StreamChatApi.ModerationApi();
let flagRequest = new StreamChatApi.FlagRequest(); // FlagRequest | 
apiInstance.unflag(flagRequest, (error, data, response) => {
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
 **flagRequest** | [**FlagRequest**](FlagRequest.md)|  | 

### Return type

[**FlagResponse**](FlagResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## unmuteUser_0

> UnmuteResponse unmuteUser_0(unmuteUserRequest)

Unmute user

Unmutes previously muted user  Sends events: - user.unmuted  Required permissions: - MuteUser 

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

let apiInstance = new StreamChatApi.ModerationApi();
let unmuteUserRequest = new StreamChatApi.UnmuteUserRequest(); // UnmuteUserRequest | 
apiInstance.unmuteUser_0(unmuteUserRequest, (error, data, response) => {
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
 **unmuteUserRequest** | [**UnmuteUserRequest**](UnmuteUserRequest.md)|  | 

### Return type

[**UnmuteResponse**](UnmuteResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBlockList_0

> Response updateBlockList_0(name, updateBlockListRequest)

Update block list

Updates contents of the block list 

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

let apiInstance = new StreamChatApi.ModerationApi();
let name = "name_example"; // String | 
let updateBlockListRequest = new StreamChatApi.UpdateBlockListRequest(); // UpdateBlockListRequest | 
apiInstance.updateBlockList_0(name, updateBlockListRequest, (error, data, response) => {
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
 **name** | **String**|  | 
 **updateBlockListRequest** | [**UpdateBlockListRequest**](UpdateBlockListRequest.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

