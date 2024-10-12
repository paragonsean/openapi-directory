# Vimeo.APIInformationApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEndpoints**](APIInformationApi.md#getEndpoints) | **GET** / | Get an API specification



## getEndpoints

> Endpoint getEndpoints(opts)

Get an API specification

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.APIInformationApi();
let opts = {
  'openapi': true // Boolean | Return an OpenAPI specification.
};
apiInstance.getEndpoints(opts, (error, data, response) => {
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
 **openapi** | **Boolean**| Return an OpenAPI specification. | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.endpoint+json

