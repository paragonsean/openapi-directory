# BeezUpMerchantApi.ChannelsChannelsGlobalApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAvailableChannels**](ChannelsChannelsGlobalApi.md#getAvailableChannels) | **GET** /v2/user/channels/ | List all available channel for this store
[**getChannelCategories**](ChannelsChannelsGlobalApi.md#getChannelCategories) | **GET** /v2/user/channels/{channelId}/categories | Get channel categories
[**getChannelColumns**](ChannelsChannelsGlobalApi.md#getChannelColumns) | **POST** /v2/user/channels/{channelId}/columns | Get channel columns
[**getChannelInfo**](ChannelsChannelsGlobalApi.md#getChannelInfo) | **GET** /v2/user/channels/{channelId} | Get channel information



## getAvailableChannels

> [ChannelHeader] getAvailableChannels(storeId)

List all available channel for this store

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelsChannelsGlobalApi();
let storeId = "04730364-9826-4ff3-92e4-51fccd02bf10"; // String | The store identifier
apiInstance.getAvailableChannels(storeId, (error, data, response) => {
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
 **storeId** | **String**| The store identifier | 

### Return type

[**[ChannelHeader]**](ChannelHeader.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelCategories

> ChannelRootCategory getChannelCategories(channelId, acceptEncoding)

Get channel categories

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelsChannelsGlobalApi();
let channelId = "2dc136a7-0d3d-4cc9-a825-a28a42c53e28"; // String | The channel identifier
let acceptEncoding = ["null"]; // [String] | Indicates that the client accepts that the response will be compressed to reduce traffic size.
apiInstance.getChannelCategories(channelId, acceptEncoding, (error, data, response) => {
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
 **channelId** | **String**| The channel identifier | 
 **acceptEncoding** | [**[String]**](String.md)| Indicates that the client accepts that the response will be compressed to reduce traffic size. | 

### Return type

[**ChannelRootCategory**](ChannelRootCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelColumns

> [ChannelColumn] getChannelColumns(channelId, acceptEncoding, opts)

Get channel columns

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelsChannelsGlobalApi();
let channelId = "2dc136a7-0d3d-4cc9-a825-a28a42c53e28"; // String | The channel identifier
let acceptEncoding = ["null"]; // [String] | Indicates that the client accepts that the response will be compressed to reduce traffic size.
let opts = {
  'requestBody': ["8a76f06a-fefc-4c0d-bcfe-b210f1482977"] // [String] | Allow you to filter the channel column identifier list your want to get
};
apiInstance.getChannelColumns(channelId, acceptEncoding, opts, (error, data, response) => {
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
 **channelId** | **String**| The channel identifier | 
 **acceptEncoding** | [**[String]**](String.md)| Indicates that the client accepts that the response will be compressed to reduce traffic size. | 
 **requestBody** | [**[String]**](String.md)| Allow you to filter the channel column identifier list your want to get | [optional] 

### Return type

[**[ChannelColumn]**](ChannelColumn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getChannelInfo

> ChannelInfo getChannelInfo(channelId)

Get channel information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelsChannelsGlobalApi();
let channelId = "2dc136a7-0d3d-4cc9-a825-a28a42c53e28"; // String | The channel identifier
apiInstance.getChannelInfo(channelId, (error, data, response) => {
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
 **channelId** | **String**| The channel identifier | 

### Return type

[**ChannelInfo**](ChannelInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

