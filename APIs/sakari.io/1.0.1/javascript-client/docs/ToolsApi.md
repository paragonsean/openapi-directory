# Sakari.ToolsApi

All URIs are relative to *https://api.sakari.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**toolsShareFile**](ToolsApi.md#toolsShareFile) | **POST** /v1/tools/sharefile | Share file - use to host a file and generate a short link to be used directly in a message or as a link to media for a MMS



## toolsShareFile

> ShareFileResponse toolsShareFile(body)

Share file - use to host a file and generate a short link to be used directly in a message or as a link to media for a MMS

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.ToolsApi();
let body = "/path/to/file"; // File | 
apiInstance.toolsShareFile(body, (error, data, response) => {
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
 **body** | **File**|  | 

### Return type

[**ShareFileResponse**](ShareFileResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: application/octet-stream, multipart/form-data
- **Accept**: application/json

