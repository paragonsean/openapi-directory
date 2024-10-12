# FilesComApi.FileActionsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileActionBeginUpload**](FileActionsApi.md#fileActionBeginUpload) | **POST** /file_actions/begin_upload/{path} | Begin file upload
[**fileActionCopy**](FileActionsApi.md#fileActionCopy) | **POST** /file_actions/copy/{path} | Copy file/folder
[**fileActionFind**](FileActionsApi.md#fileActionFind) | **GET** /file_actions/metadata/{path} | Find file/folder by path
[**fileActionMove**](FileActionsApi.md#fileActionMove) | **POST** /file_actions/move/{path} | Move file/folder



## fileActionBeginUpload

> [FileUploadPartEntity] fileActionBeginUpload(path, opts)

Begin file upload

Begin file upload

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FileActionsApi();
let path = "path_example"; // String | Path to operate on.
let opts = {
  'mkdirParents': true, // Boolean | Create parent directories if they do not exist?
  'part': 56, // Number | Part if uploading a part.
  'parts': 56, // Number | How many parts to fetch?
  'ref': "ref_example", // String | 
  'restart': 56, // Number | File byte offset to restart from.
  'size': 56, // Number | Total bytes of file being uploaded (include bytes being retained if appending/restarting).
  'withRename': true // Boolean | Allow file rename instead of overwrite?
};
apiInstance.fileActionBeginUpload(path, opts, (error, data, response) => {
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
 **path** | **String**| Path to operate on. | 
 **mkdirParents** | **Boolean**| Create parent directories if they do not exist? | [optional] 
 **part** | **Number**| Part if uploading a part. | [optional] 
 **parts** | **Number**| How many parts to fetch? | [optional] 
 **ref** | **String**|  | [optional] 
 **restart** | **Number**| File byte offset to restart from. | [optional] 
 **size** | **Number**| Total bytes of file being uploaded (include bytes being retained if appending/restarting). | [optional] 
 **withRename** | **Boolean**| Allow file rename instead of overwrite? | [optional] 

### Return type

[**[FileUploadPartEntity]**](FileUploadPartEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## fileActionCopy

> FileActionEntity fileActionCopy(path, destination, opts)

Copy file/folder

Copy file/folder

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FileActionsApi();
let path = "path_example"; // String | Path to operate on.
let destination = "destination_example"; // String | Copy destination path.
let opts = {
  'structure': true // Boolean | Copy structure only?
};
apiInstance.fileActionCopy(path, destination, opts, (error, data, response) => {
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
 **path** | **String**| Path to operate on. | 
 **destination** | **String**| Copy destination path. | 
 **structure** | **Boolean**| Copy structure only? | [optional] 

### Return type

[**FileActionEntity**](FileActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## fileActionFind

> FileEntity fileActionFind(path, opts)

Find file/folder by path

Find file/folder by path

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FileActionsApi();
let path = "path_example"; // String | Path to operate on.
let opts = {
  'previewSize': "previewSize_example", // String | Request a preview size.  Can be `small` (default), `large`, `xlarge`, or `pdf`.
  'withPreviews': true, // Boolean | Include file preview information?
  'withPriorityColor': true // Boolean | Include file priority color information?
};
apiInstance.fileActionFind(path, opts, (error, data, response) => {
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
 **path** | **String**| Path to operate on. | 
 **previewSize** | **String**| Request a preview size.  Can be &#x60;small&#x60; (default), &#x60;large&#x60;, &#x60;xlarge&#x60;, or &#x60;pdf&#x60;. | [optional] 
 **withPreviews** | **Boolean**| Include file preview information? | [optional] 
 **withPriorityColor** | **Boolean**| Include file priority color information? | [optional] 

### Return type

[**FileEntity**](FileEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileActionMove

> FileActionEntity fileActionMove(path, destination)

Move file/folder

Move file/folder

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FileActionsApi();
let path = "path_example"; // String | Path to operate on.
let destination = "destination_example"; // String | Move destination path.
apiInstance.fileActionMove(path, destination, (error, data, response) => {
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
 **path** | **String**| Path to operate on. | 
 **destination** | **String**| Move destination path. | 

### Return type

[**FileActionEntity**](FileActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

