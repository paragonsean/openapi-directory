# FilesComApi.FilesApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteFilesPath**](FilesApi.md#deleteFilesPath) | **DELETE** /files/{path} | Delete file/folder
[**fileDownload**](FilesApi.md#fileDownload) | **GET** /files/{path} | Download file
[**patchFilesPath**](FilesApi.md#patchFilesPath) | **PATCH** /files/{path} | Update file/folder metadata
[**postFilesPath**](FilesApi.md#postFilesPath) | **POST** /files/{path} | Upload file



## deleteFilesPath

> deleteFilesPath(path, opts)

Delete file/folder

Delete file/folder

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FilesApi();
let path = "path_example"; // String | Path to operate on.
let opts = {
  'recursive': true // Boolean | If true, will recursively delete folers.  Otherwise, will error on non-empty folders.
};
apiInstance.deleteFilesPath(path, opts, (error, data, response) => {
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
 **path** | **String**| Path to operate on. | 
 **recursive** | **Boolean**| If true, will recursively delete folers.  Otherwise, will error on non-empty folders. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fileDownload

> FileEntity fileDownload(path, opts)

Download file

Download file

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FilesApi();
let path = "path_example"; // String | Path to operate on.
let opts = {
  'action': "action_example", // String | Can be blank, `redirect` or `stat`.  If set to `stat`, we will return file information but without a download URL, and without logging a download.  If set to `redirect` we will serve a 302 redirect directly to the file.  This is used for integrations with Zapier, and is not recommended for most integrations.
  'previewSize': "previewSize_example", // String | Request a preview size.  Can be `small` (default), `large`, `xlarge`, or `pdf`.
  'withPreviews': true, // Boolean | Include file preview information?
  'withPriorityColor': true // Boolean | Include file priority color information?
};
apiInstance.fileDownload(path, opts, (error, data, response) => {
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
 **action** | **String**| Can be blank, &#x60;redirect&#x60; or &#x60;stat&#x60;.  If set to &#x60;stat&#x60;, we will return file information but without a download URL, and without logging a download.  If set to &#x60;redirect&#x60; we will serve a 302 redirect directly to the file.  This is used for integrations with Zapier, and is not recommended for most integrations. | [optional] 
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


## patchFilesPath

> FileEntity patchFilesPath(path, opts)

Update file/folder metadata

Update file/folder metadata

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FilesApi();
let path = "path_example"; // String | Path to operate on.
let opts = {
  'priorityColor': "priorityColor_example", // String | Priority/Bookmark color of file.
  'providedMtime': new Date("2013-10-20T19:20:30+01:00") // Date | Modified time of file.
};
apiInstance.patchFilesPath(path, opts, (error, data, response) => {
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
 **priorityColor** | **String**| Priority/Bookmark color of file. | [optional] 
 **providedMtime** | **Date**| Modified time of file. | [optional] 

### Return type

[**FileEntity**](FileEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postFilesPath

> FileEntity postFilesPath(path, etagsEtag, etagsPart, opts)

Upload file

Upload file

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FilesApi();
let path = "path_example"; // String | Path to operate on.
let etagsEtag = ["null"]; // [String] | etag identifier.
let etagsPart = [null]; // [Number] | Part number.
let opts = {
  'action': "action_example", // String | The action to perform.  Can be `append`, `attachment`, `end`, `upload`, `put`, or may not exist
  'length': 56, // Number | Length of file.
  'mkdirParents': true, // Boolean | Create parent directories if they do not exist?
  'part': 56, // Number | Part if uploading a part.
  'parts': 56, // Number | How many parts to fetch?
  'providedMtime': new Date("2013-10-20T19:20:30+01:00"), // Date | User provided modification time.
  'ref': "ref_example", // String | 
  'restart': 56, // Number | File byte offset to restart from.
  'size': 56, // Number | Size of file.
  'structure': "structure_example", // String | If copying folder, copy just the structure?
  'withRename': true // Boolean | Allow file rename instead of overwrite?
};
apiInstance.postFilesPath(path, etagsEtag, etagsPart, opts, (error, data, response) => {
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
 **etagsEtag** | [**[String]**](String.md)| etag identifier. | 
 **etagsPart** | [**[Number]**](Number.md)| Part number. | 
 **action** | **String**| The action to perform.  Can be &#x60;append&#x60;, &#x60;attachment&#x60;, &#x60;end&#x60;, &#x60;upload&#x60;, &#x60;put&#x60;, or may not exist | [optional] 
 **length** | **Number**| Length of file. | [optional] 
 **mkdirParents** | **Boolean**| Create parent directories if they do not exist? | [optional] 
 **part** | **Number**| Part if uploading a part. | [optional] 
 **parts** | **Number**| How many parts to fetch? | [optional] 
 **providedMtime** | **Date**| User provided modification time. | [optional] 
 **ref** | **String**|  | [optional] 
 **restart** | **Number**| File byte offset to restart from. | [optional] 
 **size** | **Number**| Size of file. | [optional] 
 **structure** | **String**| If copying folder, copy just the structure? | [optional] 
 **withRename** | **Boolean**| Allow file rename instead of overwrite? | [optional] 

### Return type

[**FileEntity**](FileEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

