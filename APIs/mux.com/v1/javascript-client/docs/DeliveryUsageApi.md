# MuxApi.DeliveryUsageApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listDeliveryUsage**](DeliveryUsageApi.md#listDeliveryUsage) | **GET** /video/v1/delivery-usage | List Usage



## listDeliveryUsage

> ListDeliveryUsageResponse listDeliveryUsage(opts)

List Usage

Returns a list of delivery usage records and their associated Asset IDs or Live Stream IDs.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.DeliveryUsageApi();
let opts = {
  'page': 1, // Number | Offset by this many pages, of the size of `limit`
  'limit': 100, // Number | Number of items to include in the response
  'assetId': "assetId_example", // String | Filter response to return delivery usage for this asset only. You cannot specify both the `asset_id` and `live_stream_id` parameters together.
  'liveStreamId': "liveStreamId_example", // String | Filter response to return delivery usage for assets for this live stream. You cannot specify both the `asset_id` and `live_stream_id` parameters together.
  'timeframe': ["null"] // [String] | Time window to get delivery usage information. timeframe[0] indicates the start time, timeframe[1] indicates the end time in seconds since the Unix epoch. Default time window is 1 hour representing usage from 13th to 12th hour from when the request is made.
};
apiInstance.listDeliveryUsage(opts, (error, data, response) => {
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
 **page** | **Number**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **limit** | **Number**| Number of items to include in the response | [optional] [default to 100]
 **assetId** | **String**| Filter response to return delivery usage for this asset only. You cannot specify both the &#x60;asset_id&#x60; and &#x60;live_stream_id&#x60; parameters together. | [optional] 
 **liveStreamId** | **String**| Filter response to return delivery usage for assets for this live stream. You cannot specify both the &#x60;asset_id&#x60; and &#x60;live_stream_id&#x60; parameters together. | [optional] 
 **timeframe** | [**[String]**](String.md)| Time window to get delivery usage information. timeframe[0] indicates the start time, timeframe[1] indicates the end time in seconds since the Unix epoch. Default time window is 1 hour representing usage from 13th to 12th hour from when the request is made. | [optional] 

### Return type

[**ListDeliveryUsageResponse**](ListDeliveryUsageResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

