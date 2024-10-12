# TraktApi.NetworksApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworks**](NetworksApi.md#getNetworks) | **GET** /networks | Get networks



## getNetworks

> getNetworks(opts)

Get networks

Get a list of all TV networks, including the name.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.NetworksApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getNetworks(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

