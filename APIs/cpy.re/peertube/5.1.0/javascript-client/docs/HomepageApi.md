# PeerTube.HomepageApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1CustomPagesHomepageInstanceGet**](HomepageApi.md#apiV1CustomPagesHomepageInstanceGet) | **GET** /api/v1/custom-pages/homepage/instance | Get instance custom homepage
[**apiV1CustomPagesHomepageInstancePut**](HomepageApi.md#apiV1CustomPagesHomepageInstancePut) | **PUT** /api/v1/custom-pages/homepage/instance | Set instance custom homepage



## apiV1CustomPagesHomepageInstanceGet

> CustomHomepage apiV1CustomPagesHomepageInstanceGet()

Get instance custom homepage

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.HomepageApi();
apiInstance.apiV1CustomPagesHomepageInstanceGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CustomHomepage**](CustomHomepage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1CustomPagesHomepageInstancePut

> apiV1CustomPagesHomepageInstancePut(opts)

Set instance custom homepage

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.HomepageApi();
let opts = {
  'apiV1CustomPagesHomepageInstancePutRequest': new PeerTube.ApiV1CustomPagesHomepageInstancePutRequest() // ApiV1CustomPagesHomepageInstancePutRequest | 
};
apiInstance.apiV1CustomPagesHomepageInstancePut(opts, (error, data, response) => {
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
 **apiV1CustomPagesHomepageInstancePutRequest** | [**ApiV1CustomPagesHomepageInstancePutRequest**](ApiV1CustomPagesHomepageInstancePutRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

