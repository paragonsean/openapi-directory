# PlatformApi.HistoryApi

All URIs are relative to *https://rest.ably.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMessagesByChannel**](HistoryApi.md#getMessagesByChannel) | **GET** /channels/{channel_id}/messages | Get message history for a channel
[**getPresenceHistoryOfChannel**](HistoryApi.md#getPresenceHistoryOfChannel) | **GET** /channels/{channel_id}/presence/history | Get presence history of a channel



## getMessagesByChannel

> [Message] getMessagesByChannel(channelId, opts)

Get message history for a channel

Get message history for a channel

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.HistoryApi();
let channelId = "channelId_example"; // String | The [Channel's ID](https://www.ably.io/documentation/rest/channels).
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'start': "start_example", // String | 
  'limit': 56, // Number | 
  'end': "'now'", // String | 
  'direction': "'backwards'" // String | 
};
apiInstance.getMessagesByChannel(channelId, opts, (error, data, response) => {
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
 **channelId** | **String**| The [Channel&#39;s ID](https://www.ably.io/documentation/rest/channels). | 
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 
 **start** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **end** | **String**|  | [optional] [default to &#39;now&#39;]
 **direction** | **String**|  | [optional] [default to &#39;backwards&#39;]

### Return type

[**[Message]**](Message.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html


## getPresenceHistoryOfChannel

> [PresenceMessage] getPresenceHistoryOfChannel(channelId, opts)

Get presence history of a channel

Get presence on a channel

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.HistoryApi();
let channelId = "channelId_example"; // String | The [Channel's ID](https://www.ably.io/documentation/rest/channels).
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'start': "start_example", // String | 
  'limit': 56, // Number | 
  'end': "'now'", // String | 
  'direction': "'backwards'" // String | 
};
apiInstance.getPresenceHistoryOfChannel(channelId, opts, (error, data, response) => {
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
 **channelId** | **String**| The [Channel&#39;s ID](https://www.ably.io/documentation/rest/channels). | 
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 
 **start** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **end** | **String**|  | [optional] [default to &#39;now&#39;]
 **direction** | **String**|  | [optional] [default to &#39;backwards&#39;]

### Return type

[**[PresenceMessage]**](PresenceMessage.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html

