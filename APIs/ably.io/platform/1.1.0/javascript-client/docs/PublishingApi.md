# PlatformApi.PublishingApi

All URIs are relative to *https://rest.ably.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publishMessagesToChannel**](PublishingApi.md#publishMessagesToChannel) | **POST** /channels/{channel_id}/messages | Publish a message to a channel



## publishMessagesToChannel

> PublishMessagesToChannel2XXResponse publishMessagesToChannel(channelId, opts)

Publish a message to a channel

Publish a message to the specified channel

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

let apiInstance = new PlatformApi.PublishingApi();
let channelId = "channelId_example"; // String | The [Channel's ID](https://www.ably.io/documentation/rest/channels).
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'message': new PlatformApi.Message() // Message | 
};
apiInstance.publishMessagesToChannel(channelId, opts, (error, data, response) => {
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
 **message** | [**Message**](Message.md)|  | [optional] 

### Return type

[**PublishMessagesToChannel2XXResponse**](PublishMessagesToChannel2XXResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-msgpack, application/x-www-form-urlencoded
- **Accept**: application/json, application/x-msgpack, text/html

