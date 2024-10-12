# FilesComApi.RequestsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteRequestsId**](RequestsApi.md#deleteRequestsId) | **DELETE** /requests/{id} | Delete Request
[**getRequests**](RequestsApi.md#getRequests) | **GET** /requests | List Requests
[**getRequestsFoldersPath**](RequestsApi.md#getRequestsFoldersPath) | **GET** /requests/folders/{path} | List Requests
[**postRequests**](RequestsApi.md#postRequests) | **POST** /requests | Create Request



## deleteRequestsId

> deleteRequestsId(id)

Delete Request

Delete Request

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.RequestsApi();
let id = 56; // Number | Request ID.
apiInstance.deleteRequestsId(id, (error, data, response) => {
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
 **id** | **Number**| Request ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRequests

> [RequestEntity] getRequests(opts)

List Requests

List Requests

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.RequestsApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[destination]=desc`). Valid fields are `destination`.
  'mine': true, // Boolean | Only show requests of the current user?  (Defaults to true if current user is not a site admin.)
  'path': "path_example" // String | Path to show requests for.  If omitted, shows all paths. Send `/` to represent the root directory.
};
apiInstance.getRequests(opts, (error, data, response) => {
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
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[destination]&#x3D;desc&#x60;). Valid fields are &#x60;destination&#x60;. | [optional] 
 **mine** | **Boolean**| Only show requests of the current user?  (Defaults to true if current user is not a site admin.) | [optional] 
 **path** | **String**| Path to show requests for.  If omitted, shows all paths. Send &#x60;/&#x60; to represent the root directory. | [optional] 

### Return type

[**[RequestEntity]**](RequestEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRequestsFoldersPath

> [RequestEntity] getRequestsFoldersPath(path, opts)

List Requests

List Requests

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.RequestsApi();
let path = "path_example"; // String | Path to show requests for.  If omitted, shows all paths. Send `/` to represent the root directory.
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[destination]=desc`). Valid fields are `destination`.
  'mine': true // Boolean | Only show requests of the current user?  (Defaults to true if current user is not a site admin.)
};
apiInstance.getRequestsFoldersPath(path, opts, (error, data, response) => {
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
 **path** | **String**| Path to show requests for.  If omitted, shows all paths. Send &#x60;/&#x60; to represent the root directory. | 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[destination]&#x3D;desc&#x60;). Valid fields are &#x60;destination&#x60;. | [optional] 
 **mine** | **Boolean**| Only show requests of the current user?  (Defaults to true if current user is not a site admin.) | [optional] 

### Return type

[**[RequestEntity]**](RequestEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postRequests

> RequestEntity postRequests(destination, path, opts)

Create Request

Create Request

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.RequestsApi();
let destination = "destination_example"; // String | Destination filename (without extension) to request.
let path = "path_example"; // String | Folder path on which to request the file.
let opts = {
  'groupIds': "groupIds_example", // String | A list of group IDs to request the file from. If sent as a string, it should be comma-delimited.
  'userIds': "userIds_example" // String | A list of user IDs to request the file from. If sent as a string, it should be comma-delimited.
};
apiInstance.postRequests(destination, path, opts, (error, data, response) => {
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
 **destination** | **String**| Destination filename (without extension) to request. | 
 **path** | **String**| Folder path on which to request the file. | 
 **groupIds** | **String**| A list of group IDs to request the file from. If sent as a string, it should be comma-delimited. | [optional] 
 **userIds** | **String**| A list of user IDs to request the file from. If sent as a string, it should be comma-delimited. | [optional] 

### Return type

[**RequestEntity**](RequestEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

