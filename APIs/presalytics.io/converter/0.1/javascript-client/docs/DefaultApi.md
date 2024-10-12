# DocConverter.DefaultApi

All URIs are relative to *https://api.presalytics.io/doc-converter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**svgconvert**](DefaultApi.md#svgconvert) | **POST** /svgconvert | converts pptx file to svg image



## svgconvert

> FileUrl svgconvert(opts)

converts pptx file to svg image

### Example

```javascript
import DocConverter from 'doc_converter';

let apiInstance = new DocConverter.DefaultApi();
let opts = {
  'file': "/path/to/file" // File | 
};
apiInstance.svgconvert(opts, (error, data, response) => {
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
 **file** | **File**|  | [optional] 

### Return type

[**FileUrl**](FileUrl.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

