# MuxApi.ExportsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listExports**](ExportsApi.md#listExports) | **GET** /data/v1/exports | List property video view export links
[**listExportsViews**](ExportsApi.md#listExportsViews) | **GET** /data/v1/exports/views | List available property view exports



## listExports

> ListExportsResponse listExports()

List property video view export links

The API has been replaced by the list-exports-views API call.  Lists the available video view exports along with URLs to retrieve them. 

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.ExportsApi();
apiInstance.listExports((error, data, response) => {
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

[**ListExportsResponse**](ListExportsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listExportsViews

> ListVideoViewExportsResponse listExportsViews()

List available property view exports

Lists the available video view exports along with URLs to retrieve them.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.ExportsApi();
apiInstance.listExportsViews((error, data, response) => {
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

[**ListVideoViewExportsResponse**](ListVideoViewExportsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

