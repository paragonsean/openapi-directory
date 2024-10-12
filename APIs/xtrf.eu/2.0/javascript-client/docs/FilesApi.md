# XtrfHomePortalApi.FilesApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uploadFile**](FilesApi.md#uploadFile) | **POST** /files | Uploads a temporary file (ie. for XML import). Returns token which can be used in other API calls.



## uploadFile

> uploadFile(opts)

Uploads a temporary file (ie. for XML import). Returns token which can be used in other API calls.

When a file is required by an operation (ie. task creation) it must be uploaded previously to the API. Uploading a file will result in a file token, which can be used to reference this file in other API calls.  Each file must be uploaded separately.  Keep in mind that file token has limited validity (ie. 10 minutes).  Therefore files must be uploaded just before issuing API call which reference them. 

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.FilesApi();
let opts = {
  'file': "/path/to/file" // File | 
};
apiInstance.uploadFile(opts, (error, data, response) => {
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
 **file** | **File**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

