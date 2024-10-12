# PlatformApi.StatusApi

All URIs are relative to *https://rest.ably.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMetadataOfAllChannels**](StatusApi.md#getMetadataOfAllChannels) | **GET** /channels | Enumerate all active channels of the application
[**getMetadataOfChannel**](StatusApi.md#getMetadataOfChannel) | **GET** /channels/{channel_id} | Get metadata of a channel
[**getPresenceOfChannel**](StatusApi.md#getPresenceOfChannel) | **GET** /channels/{channel_id}/presence | Get presence of a channel



## getMetadataOfAllChannels

> GetMetadataOfAllChannels2XXResponse getMetadataOfAllChannels(opts)

Enumerate all active channels of the application

Enumerate all active channels of the application

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

let apiInstance = new PlatformApi.StatusApi();
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'limit': 100, // Number | 
  'prefix': "prefix_example", // String | Optionally limits the query to only those channels whose name starts with the given prefix
  'by': "by_example" // String | optionally specifies whether to return just channel names (by=id) or ChannelDetails (by=value)
};
apiInstance.getMetadataOfAllChannels(opts, (error, data, response) => {
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
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 
 **limit** | **Number**|  | [optional] [default to 100]
 **prefix** | **String**| Optionally limits the query to only those channels whose name starts with the given prefix | [optional] 
 **by** | **String**| optionally specifies whether to return just channel names (by&#x3D;id) or ChannelDetails (by&#x3D;value) | [optional] 

### Return type

[**GetMetadataOfAllChannels2XXResponse**](GetMetadataOfAllChannels2XXResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html


## getMetadataOfChannel

> ChannelDetails getMetadataOfChannel(channelId, opts)

Get metadata of a channel

Get metadata of a channel

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

let apiInstance = new PlatformApi.StatusApi();
let channelId = "channelId_example"; // String | The [Channel's ID](https://www.ably.io/documentation/rest/channels).
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example" // String | The response format you would like
};
apiInstance.getMetadataOfChannel(channelId, opts, (error, data, response) => {
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

### Return type

[**ChannelDetails**](ChannelDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html


## getPresenceOfChannel

> [PresenceMessage] getPresenceOfChannel(channelId, opts)

Get presence of a channel

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

let apiInstance = new PlatformApi.StatusApi();
let channelId = "channelId_example"; // String | The [Channel's ID](https://www.ably.io/documentation/rest/channels).
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'clientId': "clientId_example", // String | 
  'connectionId': "connectionId_example", // String | 
  'limit': 100 // Number | 
};
apiInstance.getPresenceOfChannel(channelId, opts, (error, data, response) => {
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
 **clientId** | **String**|  | [optional] 
 **connectionId** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 100]

### Return type

[**[PresenceMessage]**](PresenceMessage.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html

