# ElmahIoApi.SourceMapsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sourceMapsCreateOrUpdate**](SourceMapsApi.md#sourceMapsCreateOrUpdate) | **POST** /v3/sourcemaps/{logId} | Create or update a translation between a minified JavaScript path to the minified JavaScript and source map files.



## sourceMapsCreateOrUpdate

> sourceMapsCreateOrUpdate(logId, minifiedJavaScript, path, sourceMap)

Create or update a translation between a minified JavaScript path to the minified JavaScript and source map files.

Required permission: &#x60;sourcemaps_write&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.SourceMapsApi();
let logId = "logId_example"; // String | The ID of the log which should contain the minified JavaScript and source map.
let minifiedJavaScript = "/path/to/file"; // File | The minified JavaScript file. Only files with an extension of .js and content type of text/javascript will be accepted.
let path = "path_example"; // String | An URL to the online minified JavaScript file. The URL can be absolute or relative but will always be converted to a relative path (no protocol, domain, and query parameters).  elmah.io uses this path to lookup any lines in a JS stack trace that will need de-minification.
let sourceMap = "/path/to/file"; // File | The source map file. Only files with an extension of .map and content type of application/json will be accepted.
apiInstance.sourceMapsCreateOrUpdate(logId, minifiedJavaScript, path, sourceMap, (error, data, response) => {
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
 **logId** | **String**| The ID of the log which should contain the minified JavaScript and source map. | 
 **minifiedJavaScript** | **File**| The minified JavaScript file. Only files with an extension of .js and content type of text/javascript will be accepted. | 
 **path** | **String**| An URL to the online minified JavaScript file. The URL can be absolute or relative but will always be converted to a relative path (no protocol, domain, and query parameters).  elmah.io uses this path to lookup any lines in a JS stack trace that will need de-minification. | 
 **sourceMap** | **File**| The source map file. Only files with an extension of .map and content type of application/json will be accepted. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

