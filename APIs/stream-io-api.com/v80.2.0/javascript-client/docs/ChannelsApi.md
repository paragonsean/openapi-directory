# StreamChatApi.ChannelsApi

All URIs are relative to *https://chat.stream-io-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteChannel**](ChannelsApi.md#deleteChannel) | **DELETE** /channels/{type}/{id} | Delete channel
[**deleteChannels**](ChannelsApi.md#deleteChannels) | **POST** /channels/delete | Deletes channels asynchronously
[**exportChannels**](ChannelsApi.md#exportChannels) | **POST** /export_channels | Export channels
[**getExportChannelsStatus**](ChannelsApi.md#getExportChannelsStatus) | **GET** /export_channels/{id} | Export channels status
[**getOrCreateChannelType1**](ChannelsApi.md#getOrCreateChannelType1) | **POST** /channels/{type}/query | Get or create channel (type)
[**getOrCreateChannelTypeId0**](ChannelsApi.md#getOrCreateChannelTypeId0) | **POST** /channels/{type}/{id}/query | Get or create channel (type, id)
[**hideChannel**](ChannelsApi.md#hideChannel) | **POST** /channels/{type}/{id}/hide | Hide channel
[**markChannelsRead**](ChannelsApi.md#markChannelsRead) | **POST** /channels/read | Mark channels as read
[**markRead**](ChannelsApi.md#markRead) | **POST** /channels/{type}/{id}/read | Mark read
[**markUnread**](ChannelsApi.md#markUnread) | **POST** /channels/{type}/{id}/unread | Mark unread
[**muteChannel**](ChannelsApi.md#muteChannel) | **POST** /moderation/mute/channel | Mute channel
[**queryChannels**](ChannelsApi.md#queryChannels) | **POST** /channels | Query channels
[**queryMembers**](ChannelsApi.md#queryMembers) | **GET** /members | Query members
[**search**](ChannelsApi.md#search) | **GET** /search | Search messages
[**showChannel**](ChannelsApi.md#showChannel) | **POST** /channels/{type}/{id}/show | Show channel
[**stopWatchingChannel**](ChannelsApi.md#stopWatchingChannel) | **POST** /channels/{type}/{id}/stop-watching | Stop watching channel
[**sync**](ChannelsApi.md#sync) | **POST** /sync | Sync
[**truncateChannel**](ChannelsApi.md#truncateChannel) | **POST** /channels/{type}/{id}/truncate | Truncate channel
[**unmuteChannel**](ChannelsApi.md#unmuteChannel) | **POST** /moderation/unmute/channel | Unmute channel
[**updateChannel**](ChannelsApi.md#updateChannel) | **POST** /channels/{type}/{id} | Update channel
[**updateChannelPartial**](ChannelsApi.md#updateChannelPartial) | **PATCH** /channels/{type}/{id} | Partially update channel



## deleteChannel

> DeleteChannelResponse deleteChannel(type, id, opts)

Delete channel

Deletes channel  Sends events: - channel.deleted  Required permissions: - DeleteChannel 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let type = "type_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'hardDelete': true // Boolean | 
};
apiInstance.deleteChannel(type, id, opts, (error, data, response) => {
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
 **type** | **String**|  | 
 **id** | **String**|  | 
 **hardDelete** | **Boolean**|  | [optional] 

### Return type

[**DeleteChannelResponse**](DeleteChannelResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChannels

> DeleteChannelsResponse deleteChannels(deleteChannelsRequest)

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

let apiInstance = new StreamChatApi.ChannelsApi();
let deleteChannelsRequest = new StreamChatApi.DeleteChannelsRequest(); // DeleteChannelsRequest | 
apiInstance.deleteChannels(deleteChannelsRequest, (error, data, response) => {
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


## exportChannels

> ExportChannelsResponse exportChannels(exportChannelsRequest)

Export channels

Exports channel data to JSON file 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let exportChannelsRequest = new StreamChatApi.ExportChannelsRequest(); // ExportChannelsRequest | 
apiInstance.exportChannels(exportChannelsRequest, (error, data, response) => {
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
 **exportChannelsRequest** | [**ExportChannelsRequest**](ExportChannelsRequest.md)|  | 

### Return type

[**ExportChannelsResponse**](ExportChannelsResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getExportChannelsStatus

> GetExportChannelsStatusResponse getExportChannelsStatus(id)

Export channels status

 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let id = "id_example"; // String | 
apiInstance.getExportChannelsStatus(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**GetExportChannelsStatusResponse**](GetExportChannelsStatusResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrCreateChannelType1

> ChannelStateResponse getOrCreateChannelType1(type, channelGetOrCreateRequest, opts)

Get or create channel (type)

This method creates a channel or returns an existing one with matching attributes  Sends events: - channel.created - member.added - member.removed - member.updated - user.watching.start 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let type = "type_example"; // String | 
let channelGetOrCreateRequest = new StreamChatApi.ChannelGetOrCreateRequest(); // ChannelGetOrCreateRequest | 
let opts = {
  'clientId': "clientId_example", // String | 
  'connectionId': "connectionId_example" // String | 
};
apiInstance.getOrCreateChannelType1(type, channelGetOrCreateRequest, opts, (error, data, response) => {
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
 **type** | **String**|  | 
 **channelGetOrCreateRequest** | [**ChannelGetOrCreateRequest**](ChannelGetOrCreateRequest.md)|  | 
 **clientId** | **String**|  | [optional] 
 **connectionId** | **String**|  | [optional] 

### Return type

[**ChannelStateResponse**](ChannelStateResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOrCreateChannelTypeId0

> ChannelStateResponse getOrCreateChannelTypeId0(type, id, channelGetOrCreateRequest, opts)

Get or create channel (type, id)

This method creates a channel or returns an existing one with matching attributes  Sends events: - channel.created - member.added - member.removed - member.updated - user.watching.start 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let type = "type_example"; // String | 
let id = "id_example"; // String | 
let channelGetOrCreateRequest = new StreamChatApi.ChannelGetOrCreateRequest(); // ChannelGetOrCreateRequest | 
let opts = {
  'clientId': "clientId_example", // String | 
  'connectionId': "connectionId_example" // String | 
};
apiInstance.getOrCreateChannelTypeId0(type, id, channelGetOrCreateRequest, opts, (error, data, response) => {
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
 **type** | **String**|  | 
 **id** | **String**|  | 
 **channelGetOrCreateRequest** | [**ChannelGetOrCreateRequest**](ChannelGetOrCreateRequest.md)|  | 
 **clientId** | **String**|  | [optional] 
 **connectionId** | **String**|  | [optional] 

### Return type

[**ChannelStateResponse**](ChannelStateResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## hideChannel

> HideChannelResponse hideChannel(type, id, hideChannelRequest)

Hide channel

Marks channel as hidden for current user  Sends events: - channel.hidden  Required permissions: - ReadChannel 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let type = "type_example"; // String | 
let id = "id_example"; // String | 
let hideChannelRequest = new StreamChatApi.HideChannelRequest(); // HideChannelRequest | 
apiInstance.hideChannel(type, id, hideChannelRequest, (error, data, response) => {
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
 **type** | **String**|  | 
 **id** | **String**|  | 
 **hideChannelRequest** | [**HideChannelRequest**](HideChannelRequest.md)|  | 

### Return type

[**HideChannelResponse**](HideChannelResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## markChannelsRead

> MarkReadResponse markChannelsRead(markChannelsReadRequest)

Mark channels as read

Marks channels as read up to the specific message. If no channels is given, mark all channel as read  Sends events: - message.read  Required permissions: - ReadChannel 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let markChannelsReadRequest = new StreamChatApi.MarkChannelsReadRequest(); // MarkChannelsReadRequest | 
apiInstance.markChannelsRead(markChannelsReadRequest, (error, data, response) => {
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
 **markChannelsReadRequest** | [**MarkChannelsReadRequest**](MarkChannelsReadRequest.md)|  | 

### Return type

[**MarkReadResponse**](MarkReadResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## markRead

> MarkReadResponse markRead(type, id, markReadRequest)

Mark read

Marks channel as read up to the specific message  Sends events: - message.read  Required permissions: - ReadChannel 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let type = "type_example"; // String | 
let id = "id_example"; // String | 
let markReadRequest = new StreamChatApi.MarkReadRequest(); // MarkReadRequest | 
apiInstance.markRead(type, id, markReadRequest, (error, data, response) => {
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
 **type** | **String**|  | 
 **id** | **String**|  | 
 **markReadRequest** | [**MarkReadRequest**](MarkReadRequest.md)|  | 

### Return type

[**MarkReadResponse**](MarkReadResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## markUnread

> Response markUnread(type, id, markUnreadRequest)

Mark unread

Marks channel as unread from a specific message  Required permissions: - ReadChannel 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let type = "type_example"; // String | 
let id = "id_example"; // String | 
let markUnreadRequest = new StreamChatApi.MarkUnreadRequest(); // MarkUnreadRequest | 
apiInstance.markUnread(type, id, markUnreadRequest, (error, data, response) => {
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
 **type** | **String**|  | 
 **id** | **String**|  | 
 **markUnreadRequest** | [**MarkUnreadRequest**](MarkUnreadRequest.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## muteChannel

> MuteChannelResponse muteChannel(muteChannelRequest)

Mute channel

Mutes channel for user  Sends events: - channel.muted  Required permissions: - MuteChannel 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let muteChannelRequest = new StreamChatApi.MuteChannelRequest(); // MuteChannelRequest | 
apiInstance.muteChannel(muteChannelRequest, (error, data, response) => {
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
 **muteChannelRequest** | [**MuteChannelRequest**](MuteChannelRequest.md)|  | 

### Return type

[**MuteChannelResponse**](MuteChannelResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryChannels

> ChannelsResponse queryChannels(queryChannelsRequest, opts)

Query channels

Query channels with filter query  Required permissions: - ReadChannel 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let queryChannelsRequest = new StreamChatApi.QueryChannelsRequest(); // QueryChannelsRequest | Query Channels Request
let opts = {
  'clientId': "clientId_example", // String | 
  'connectionId': "connectionId_example" // String | 
};
apiInstance.queryChannels(queryChannelsRequest, opts, (error, data, response) => {
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
 **queryChannelsRequest** | [**QueryChannelsRequest**](QueryChannelsRequest.md)| Query Channels Request | 
 **clientId** | **String**|  | [optional] 
 **connectionId** | **String**|  | [optional] 

### Return type

[**ChannelsResponse**](ChannelsResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryMembers

> MembersResponse queryMembers(opts)

Query members

Find and filter channel members  Required permissions: - ReadChannel 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let opts = {
  'payload': new StreamChatApi.QueryMembersRequest() // QueryMembersRequest | 
};
apiInstance.queryMembers(opts, (error, data, response) => {
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
 **payload** | [**QueryMembersRequest**](.md)|  | [optional] 

### Return type

[**MembersResponse**](MembersResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## search

> SearchResponse search(opts)

Search messages

Search messages across channels  Required permissions: - ReadChannel 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let opts = {
  'payload': new StreamChatApi.SearchRequest() // SearchRequest | 
};
apiInstance.search(opts, (error, data, response) => {
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
 **payload** | [**SearchRequest**](.md)|  | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showChannel

> ShowChannelResponse showChannel(type, id, showChannelRequest)

Show channel

Shows previously hidden channel  Sends events: - channel.visible 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let type = "type_example"; // String | 
let id = "id_example"; // String | 
let showChannelRequest = new StreamChatApi.ShowChannelRequest(); // ShowChannelRequest | 
apiInstance.showChannel(type, id, showChannelRequest, (error, data, response) => {
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
 **type** | **String**|  | 
 **id** | **String**|  | 
 **showChannelRequest** | [**ShowChannelRequest**](ShowChannelRequest.md)|  | 

### Return type

[**ShowChannelResponse**](ShowChannelResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopWatchingChannel

> StopWatchingResponse stopWatchingChannel(type, id, channelStopWatchingRequest, opts)

Stop watching channel

Call this method to stop receiving channel events  Sends events: - user.watching.stop 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let type = "type_example"; // String | 
let id = "id_example"; // String | 
let channelStopWatchingRequest = new StreamChatApi.ChannelStopWatchingRequest(); // ChannelStopWatchingRequest | 
let opts = {
  'clientId': "clientId_example", // String | 
  'connectionId': "connectionId_example" // String | 
};
apiInstance.stopWatchingChannel(type, id, channelStopWatchingRequest, opts, (error, data, response) => {
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
 **type** | **String**|  | 
 **id** | **String**|  | 
 **channelStopWatchingRequest** | [**ChannelStopWatchingRequest**](ChannelStopWatchingRequest.md)|  | 
 **clientId** | **String**|  | [optional] 
 **connectionId** | **String**|  | [optional] 

### Return type

[**StopWatchingResponse**](StopWatchingResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sync

> SyncResponse sync(syncRequest, opts)

Sync

Returns all events happened since client disconnect in specified channels  Required permissions: - ReadChannel 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let syncRequest = new StreamChatApi.SyncRequest(); // SyncRequest | 
let opts = {
  'withInaccessibleCids': true, // Boolean | 
  'watch': true, // Boolean | 
  'clientId': "clientId_example", // String | 
  'connectionId': "connectionId_example" // String | 
};
apiInstance.sync(syncRequest, opts, (error, data, response) => {
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
 **syncRequest** | [**SyncRequest**](SyncRequest.md)|  | 
 **withInaccessibleCids** | **Boolean**|  | [optional] 
 **watch** | **Boolean**|  | [optional] 
 **clientId** | **String**|  | [optional] 
 **connectionId** | **String**|  | [optional] 

### Return type

[**SyncResponse**](SyncResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## truncateChannel

> TruncateChannelResponse truncateChannel(type, id, truncateChannelRequest)

Truncate channel

Truncates channel  Sends events: - channel.truncated  Required permissions: - DeleteChannel - TruncateChannel 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let type = "type_example"; // String | 
let id = "id_example"; // String | 
let truncateChannelRequest = new StreamChatApi.TruncateChannelRequest(); // TruncateChannelRequest | 
apiInstance.truncateChannel(type, id, truncateChannelRequest, (error, data, response) => {
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
 **type** | **String**|  | 
 **id** | **String**|  | 
 **truncateChannelRequest** | [**TruncateChannelRequest**](TruncateChannelRequest.md)|  | 

### Return type

[**TruncateChannelResponse**](TruncateChannelResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## unmuteChannel

> UnmuteResponse unmuteChannel(unmuteChannelRequest)

Unmute channel

Unmutes channel for user  Sends events: - channel.unmuted  Required permissions: - MuteChannel 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let unmuteChannelRequest = new StreamChatApi.UnmuteChannelRequest(); // UnmuteChannelRequest | 
apiInstance.unmuteChannel(unmuteChannelRequest, (error, data, response) => {
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
 **unmuteChannelRequest** | [**UnmuteChannelRequest**](UnmuteChannelRequest.md)|  | 

### Return type

[**UnmuteResponse**](UnmuteResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannel

> UpdateChannelResponse updateChannel(type, id, updateChannelRequest)

Update channel

Change channel data  Sends events: - channel.updated - member.added - member.removed - member.updated - message.new  Required permissions: - AddOwnChannelMembership - RemoveOwnChannelMembership - UpdateChannel - UpdateChannelCooldown - UpdateChannelFrozen - UpdateChannelMembers 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let type = "type_example"; // String | 
let id = "id_example"; // String | 
let updateChannelRequest = new StreamChatApi.UpdateChannelRequest(); // UpdateChannelRequest | Channel update request
apiInstance.updateChannel(type, id, updateChannelRequest, (error, data, response) => {
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
 **type** | **String**|  | 
 **id** | **String**|  | 
 **updateChannelRequest** | [**UpdateChannelRequest**](UpdateChannelRequest.md)| Channel update request | 

### Return type

[**UpdateChannelResponse**](UpdateChannelResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannelPartial

> UpdateChannelPartialResponse updateChannelPartial(type, id, updateChannelPartialRequest)

Partially update channel

Updates certain fields of the channel  Sends events: - channel.updated  Required permissions: - UpdateChannel - UpdateChannelCooldown - UpdateChannelFrozen 

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

let apiInstance = new StreamChatApi.ChannelsApi();
let type = "type_example"; // String | 
let id = "id_example"; // String | 
let updateChannelPartialRequest = new StreamChatApi.UpdateChannelPartialRequest(); // UpdateChannelPartialRequest | 
apiInstance.updateChannelPartial(type, id, updateChannelPartialRequest, (error, data, response) => {
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
 **type** | **String**|  | 
 **id** | **String**|  | 
 **updateChannelPartialRequest** | [**UpdateChannelPartialRequest**](UpdateChannelPartialRequest.md)|  | 

### Return type

[**UpdateChannelPartialResponse**](UpdateChannelPartialResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

