# ShipEngineApi.DownloadsApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadFile**](DownloadsApi.md#downloadFile) | **GET** /v1/downloads/{dir}/{subdir}/{filename} | Download File



## downloadFile

> File downloadFile(subdir, filename, dir, opts)

Download File

Get File

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.DownloadsApi();
let subdir = "subdir_example"; // String | 
let filename = "filename_example"; // String | 
let dir = "dir_example"; // String | 
let opts = {
  'download': "download_example", // String | 
  'rotation': 56 // Number | 
};
apiInstance.downloadFile(subdir, filename, dir, opts, (error, data, response) => {
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
 **subdir** | **String**|  | 
 **filename** | **String**|  | 
 **dir** | **String**|  | 
 **download** | **String**|  | [optional] 
 **rotation** | **Number**|  | [optional] 

### Return type

**File**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf, application/zpl, image/png, application/json

