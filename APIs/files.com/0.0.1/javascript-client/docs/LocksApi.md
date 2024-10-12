# FilesComApi.LocksApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteLocksPath**](LocksApi.md#deleteLocksPath) | **DELETE** /locks/{path} | Delete Lock
[**lockListForPath**](LocksApi.md#lockListForPath) | **GET** /locks/{path} | List Locks by path
[**postLocksPath**](LocksApi.md#postLocksPath) | **POST** /locks/{path} | Create Lock



## deleteLocksPath

> deleteLocksPath(path, token)

Delete Lock

Delete Lock

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.LocksApi();
let path = "path_example"; // String | Path
let token = "token_example"; // String | Lock token
apiInstance.deleteLocksPath(path, token, (error, data, response) => {
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
 **path** | **String**| Path | 
 **token** | **String**| Lock token | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## lockListForPath

> [LockEntity] lockListForPath(path, opts)

List Locks by path

List Locks by path

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.LocksApi();
let path = "path_example"; // String | Path to operate on.
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'includeChildren': true // Boolean | Include locks from children objects?
};
apiInstance.lockListForPath(path, opts, (error, data, response) => {
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
 **includeChildren** | **Boolean**| Include locks from children objects? | [optional] 

### Return type

[**[LockEntity]**](LockEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postLocksPath

> LockEntity postLocksPath(path, opts)

Create Lock

Create Lock

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.LocksApi();
let path = "path_example"; // String | Path
let opts = {
  'allowAccessByAnyUser': true, // Boolean | Allow lock to be updated by any user?
  'exclusive': true, // Boolean | Is lock exclusive?
  'recursive': "recursive_example", // String | Does lock apply to subfolders?
  'timeout': 56 // Number | Lock timeout length
};
apiInstance.postLocksPath(path, opts, (error, data, response) => {
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
 **path** | **String**| Path | 
 **allowAccessByAnyUser** | **Boolean**| Allow lock to be updated by any user? | [optional] 
 **exclusive** | **Boolean**| Is lock exclusive? | [optional] 
 **recursive** | **String**| Does lock apply to subfolders? | [optional] 
 **timeout** | **Number**| Lock timeout length | [optional] 

### Return type

[**LockEntity**](LockEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

