# StreamChatApi.EventsApi

All URIs are relative to *https://chat.stream-io-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sendEvent**](EventsApi.md#sendEvent) | **POST** /channels/{type}/{id}/event | Send event
[**sendUserCustomEvent**](EventsApi.md#sendUserCustomEvent) | **POST** /users/{user_id}/event | Send user event
[**sync_0**](EventsApi.md#sync_0) | **POST** /sync | Sync



## sendEvent

> EventResponse sendEvent(type, id, sendEventRequest)

Send event

Sends event to the channel  Sends events: - any  Required permissions: - SendCustomEvent 

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

let apiInstance = new StreamChatApi.EventsApi();
let type = "type_example"; // String | 
let id = "id_example"; // String | 
let sendEventRequest = new StreamChatApi.SendEventRequest(); // SendEventRequest | 
apiInstance.sendEvent(type, id, sendEventRequest, (error, data, response) => {
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
 **sendEventRequest** | [**SendEventRequest**](SendEventRequest.md)|  | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendUserCustomEvent

> Response sendUserCustomEvent(userId, sendUserCustomEventRequest)

Send user event

Sends a custom event to a user  Sends events: - custom 

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

let apiInstance = new StreamChatApi.EventsApi();
let userId = "userId_example"; // String | 
let sendUserCustomEventRequest = new StreamChatApi.SendUserCustomEventRequest(); // SendUserCustomEventRequest | 
apiInstance.sendUserCustomEvent(userId, sendUserCustomEventRequest, (error, data, response) => {
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
 **sendUserCustomEventRequest** | [**SendUserCustomEventRequest**](SendUserCustomEventRequest.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sync_0

> SyncResponse sync_0(syncRequest, opts)

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

let apiInstance = new StreamChatApi.EventsApi();
let syncRequest = new StreamChatApi.SyncRequest(); // SyncRequest | 
let opts = {
  'withInaccessibleCids': true, // Boolean | 
  'watch': true, // Boolean | 
  'clientId': "clientId_example", // String | 
  'connectionId': "connectionId_example" // String | 
};
apiInstance.sync_0(syncRequest, opts, (error, data, response) => {
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

