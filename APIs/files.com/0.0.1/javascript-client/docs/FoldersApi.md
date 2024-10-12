# FilesComApi.FoldersApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folderListForPath**](FoldersApi.md#folderListForPath) | **GET** /folders/{path} | List Folders by path
[**postFoldersPath**](FoldersApi.md#postFoldersPath) | **POST** /folders/{path} | Create folder



## folderListForPath

> [FileEntity] folderListForPath(path, opts)

List Folders by path

List Folders by path

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FoldersApi();
let path = "path_example"; // String | Path to operate on.
let opts = {
  'cursor': "cursor_example", // String | Send cursor to resume an existing list from the point at which you left off.  Get a cursor from an existing list via the X-Files-Cursor-Next header or the X-Files-Cursor-Prev header.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'filter': "filter_example", // String | If specified, will filter folders/files list by this string.  Wildcards of `*` and `?` are acceptable here.
  'previewSize': "previewSize_example", // String | Request a preview size.  Can be `small` (default), `large`, `xlarge`, or `pdf`.
  'sortBy': {key: null}, // Object | Search by field and direction. Valid fields are `path`, `size`, `modified_at_datetime`, `provided_modified_at`.  Valid directions are `asc` and `desc`.  Defaults to `{\"path\":\"asc\"}`.
  'search': "search_example", // String | If `search_all` is `true`, provide the search string here.  Otherwise, this parameter acts like an alias of `filter`.
  'searchAll': true, // Boolean | Search entire site?  If set, we will ignore the folder path provided and search the entire site.  This is the same API used by the search bar in the UI.  Search results are a best effort, not real time, and not guaranteed to match every file.  This field should only be used for ad-hoc (human) searching, and not as part of an automated process.
  'withPreviews': true, // Boolean | Include file previews?
  'withPriorityColor': true // Boolean | Include file priority color information?
};
apiInstance.folderListForPath(path, opts, (error, data, response) => {
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
 **cursor** | **String**| Send cursor to resume an existing list from the point at which you left off.  Get a cursor from an existing list via the X-Files-Cursor-Next header or the X-Files-Cursor-Prev header. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **filter** | **String**| If specified, will filter folders/files list by this string.  Wildcards of &#x60;*&#x60; and &#x60;?&#x60; are acceptable here. | [optional] 
 **previewSize** | **String**| Request a preview size.  Can be &#x60;small&#x60; (default), &#x60;large&#x60;, &#x60;xlarge&#x60;, or &#x60;pdf&#x60;. | [optional] 
 **sortBy** | [**Object**](.md)| Search by field and direction. Valid fields are &#x60;path&#x60;, &#x60;size&#x60;, &#x60;modified_at_datetime&#x60;, &#x60;provided_modified_at&#x60;.  Valid directions are &#x60;asc&#x60; and &#x60;desc&#x60;.  Defaults to &#x60;{\&quot;path\&quot;:\&quot;asc\&quot;}&#x60;. | [optional] 
 **search** | **String**| If &#x60;search_all&#x60; is &#x60;true&#x60;, provide the search string here.  Otherwise, this parameter acts like an alias of &#x60;filter&#x60;. | [optional] 
 **searchAll** | **Boolean**| Search entire site?  If set, we will ignore the folder path provided and search the entire site.  This is the same API used by the search bar in the UI.  Search results are a best effort, not real time, and not guaranteed to match every file.  This field should only be used for ad-hoc (human) searching, and not as part of an automated process. | [optional] 
 **withPreviews** | **Boolean**| Include file previews? | [optional] 
 **withPriorityColor** | **Boolean**| Include file priority color information? | [optional] 

### Return type

[**[FileEntity]**](FileEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postFoldersPath

> FileEntity postFoldersPath(path, opts)

Create folder

Create folder

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FoldersApi();
let path = "path_example"; // String | Path to operate on.
let opts = {
  'mkdirParents': true, // Boolean | Create parent directories if they do not exist?
  'providedMtime': new Date("2013-10-20T19:20:30+01:00") // Date | User provided modification time.
};
apiInstance.postFoldersPath(path, opts, (error, data, response) => {
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
 **providedMtime** | **Date**| User provided modification time. | [optional] 

### Return type

[**FileEntity**](FileEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

