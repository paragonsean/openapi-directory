# FilesComApi.StylesApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteStylesPath**](StylesApi.md#deleteStylesPath) | **DELETE** /styles/{path} | Delete Style
[**getStylesPath**](StylesApi.md#getStylesPath) | **GET** /styles/{path} | Show Style
[**patchStylesPath**](StylesApi.md#patchStylesPath) | **PATCH** /styles/{path} | Update Style



## deleteStylesPath

> deleteStylesPath(path)

Delete Style

Delete Style

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.StylesApi();
let path = "path_example"; // String | Style path.
apiInstance.deleteStylesPath(path, (error, data, response) => {
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
 **path** | **String**| Style path. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getStylesPath

> StyleEntity getStylesPath(path)

Show Style

Show Style

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.StylesApi();
let path = "path_example"; // String | Style path.
apiInstance.getStylesPath(path, (error, data, response) => {
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
 **path** | **String**| Style path. | 

### Return type

[**StyleEntity**](StyleEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchStylesPath

> StyleEntity patchStylesPath(path, file)

Update Style

Update Style

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.StylesApi();
let path = "path_example"; // String | Style path.
let file = "/path/to/file"; // File | Logo for custom branding.
apiInstance.patchStylesPath(path, file, (error, data, response) => {
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
 **path** | **String**| Style path. | 
 **file** | **File**| Logo for custom branding. | 

### Return type

[**StyleEntity**](StyleEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

