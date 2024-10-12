# FilesComApi.FileCommentsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteFileCommentsId**](FileCommentsApi.md#deleteFileCommentsId) | **DELETE** /file_comments/{id} | Delete File Comment
[**fileCommentListForPath**](FileCommentsApi.md#fileCommentListForPath) | **GET** /file_comments/files/{path} | List File Comments by path
[**patchFileCommentsId**](FileCommentsApi.md#patchFileCommentsId) | **PATCH** /file_comments/{id} | Update File Comment
[**postFileComments**](FileCommentsApi.md#postFileComments) | **POST** /file_comments | Create File Comment



## deleteFileCommentsId

> deleteFileCommentsId(id)

Delete File Comment

Delete File Comment

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FileCommentsApi();
let id = 56; // Number | File Comment ID.
apiInstance.deleteFileCommentsId(id, (error, data, response) => {
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
 **id** | **Number**| File Comment ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fileCommentListForPath

> [FileCommentEntity] fileCommentListForPath(path, opts)

List File Comments by path

List File Comments by path

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FileCommentsApi();
let path = "path_example"; // String | Path to operate on.
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.fileCommentListForPath(path, opts, (error, data, response) => {
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
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[FileCommentEntity]**](FileCommentEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchFileCommentsId

> FileCommentEntity patchFileCommentsId(id, body)

Update File Comment

Update File Comment

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FileCommentsApi();
let id = 56; // Number | File Comment ID.
let body = "body_example"; // String | Comment body.
apiInstance.patchFileCommentsId(id, body, (error, data, response) => {
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
 **id** | **Number**| File Comment ID. | 
 **body** | **String**| Comment body. | 

### Return type

[**FileCommentEntity**](FileCommentEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postFileComments

> FileCommentEntity postFileComments(body, path)

Create File Comment

Create File Comment

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FileCommentsApi();
let body = "body_example"; // String | Comment body.
let path = "path_example"; // String | File path.
apiInstance.postFileComments(body, path, (error, data, response) => {
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
 **body** | **String**| Comment body. | 
 **path** | **String**| File path. | 

### Return type

[**FileCommentEntity**](FileCommentEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

