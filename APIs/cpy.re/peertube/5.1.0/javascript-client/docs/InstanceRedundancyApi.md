# PeerTube.InstanceRedundancyApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1ServerRedundancyHostPut**](InstanceRedundancyApi.md#apiV1ServerRedundancyHostPut) | **PUT** /api/v1/server/redundancy/{host} | Update a server redundancy policy



## apiV1ServerRedundancyHostPut

> apiV1ServerRedundancyHostPut(host, opts)

Update a server redundancy policy

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.InstanceRedundancyApi();
let host = "host_example"; // String | server domain to mirror
let opts = {
  'apiV1ServerRedundancyHostPutRequest': new PeerTube.ApiV1ServerRedundancyHostPutRequest() // ApiV1ServerRedundancyHostPutRequest | 
};
apiInstance.apiV1ServerRedundancyHostPut(host, opts, (error, data, response) => {
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
 **host** | **String**| server domain to mirror | 
 **apiV1ServerRedundancyHostPutRequest** | [**ApiV1ServerRedundancyHostPutRequest**](ApiV1ServerRedundancyHostPutRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

