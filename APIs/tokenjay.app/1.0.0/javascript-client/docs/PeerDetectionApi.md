# TokenJayApiServices.PeerDetectionApi

All URIs are relative to *https://api.tokenjay.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPeersList**](PeerDetectionApi.md#getPeersList) | **GET** /peers/list | Lists known peers sorted by block height



## getPeersList

> [NodePeer] getPeersList(opts)

Lists known peers sorted by block height

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.PeerDetectionApi();
let opts = {
  'unreachable': false, // Boolean | Set to true to show unreachable peers in the list
  'closedApi': false, // Boolean | Set to true to show peers not open to be connected
  'limit': 50 // Number | 
};
apiInstance.getPeersList(opts, (error, data, response) => {
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
 **unreachable** | **Boolean**| Set to true to show unreachable peers in the list | [optional] [default to false]
 **closedApi** | **Boolean**| Set to true to show peers not open to be connected | [optional] [default to false]
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

[**[NodePeer]**](NodePeer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

