# FilesComApi.HistoryApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**historyList**](HistoryApi.md#historyList) | **GET** /history | List site full action history.
[**historyListForFile**](HistoryApi.md#historyListForFile) | **GET** /history/files/{path} | List history for specific file.
[**historyListForFolder**](HistoryApi.md#historyListForFolder) | **GET** /history/folders/{path} | List history for specific folder.
[**historyListForUser**](HistoryApi.md#historyListForUser) | **GET** /history/users/{user_id} | List history for specific user.
[**historyListLogins**](HistoryApi.md#historyListLogins) | **GET** /history/login | List site login history.



## historyList

> [ActionEntity] historyList(opts)

List site full action history.

List site full action history.

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.HistoryApi();
let opts = {
  'startAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Leave blank or set to a date/time to filter earlier entries.
  'endAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Leave blank or set to a date/time to filter later entries.
  'display': "display_example", // String | Display format. Leave blank or set to `full` or `parent`.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[path]=desc`). Valid fields are `path`, `folder`, `user_id` or `created_at`.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `user_id`, `folder` or `path`.
  'filterPrefix': {key: null} // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `path`.
};
apiInstance.historyList(opts, (error, data, response) => {
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
 **startAt** | **Date**| Leave blank or set to a date/time to filter earlier entries. | [optional] 
 **endAt** | **Date**| Leave blank or set to a date/time to filter later entries. | [optional] 
 **display** | **String**| Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[path]&#x3D;desc&#x60;). Valid fields are &#x60;path&#x60;, &#x60;folder&#x60;, &#x60;user_id&#x60; or &#x60;created_at&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;user_id&#x60;, &#x60;folder&#x60; or &#x60;path&#x60;. | [optional] 
 **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;path&#x60;. | [optional] 

### Return type

[**[ActionEntity]**](ActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## historyListForFile

> [ActionEntity] historyListForFile(path, opts)

List history for specific file.

List history for specific file.

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.HistoryApi();
let path = "path_example"; // String | Path to operate on.
let opts = {
  'startAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Leave blank or set to a date/time to filter earlier entries.
  'endAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Leave blank or set to a date/time to filter later entries.
  'display': "display_example", // String | Display format. Leave blank or set to `full` or `parent`.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null} // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[user_id]=desc`). Valid fields are `user_id` and `created_at`.
};
apiInstance.historyListForFile(path, opts, (error, data, response) => {
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
 **startAt** | **Date**| Leave blank or set to a date/time to filter earlier entries. | [optional] 
 **endAt** | **Date**| Leave blank or set to a date/time to filter later entries. | [optional] 
 **display** | **String**| Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[user_id]&#x3D;desc&#x60;). Valid fields are &#x60;user_id&#x60; and &#x60;created_at&#x60;. | [optional] 

### Return type

[**[ActionEntity]**](ActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## historyListForFolder

> [ActionEntity] historyListForFolder(path, opts)

List history for specific folder.

List history for specific folder.

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.HistoryApi();
let path = "path_example"; // String | Path to operate on.
let opts = {
  'startAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Leave blank or set to a date/time to filter earlier entries.
  'endAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Leave blank or set to a date/time to filter later entries.
  'display': "display_example", // String | Display format. Leave blank or set to `full` or `parent`.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null} // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[user_id]=desc`). Valid fields are `user_id` and `created_at`.
};
apiInstance.historyListForFolder(path, opts, (error, data, response) => {
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
 **startAt** | **Date**| Leave blank or set to a date/time to filter earlier entries. | [optional] 
 **endAt** | **Date**| Leave blank or set to a date/time to filter later entries. | [optional] 
 **display** | **String**| Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[user_id]&#x3D;desc&#x60;). Valid fields are &#x60;user_id&#x60; and &#x60;created_at&#x60;. | [optional] 

### Return type

[**[ActionEntity]**](ActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## historyListForUser

> [ActionEntity] historyListForUser(userId, opts)

List history for specific user.

List history for specific user.

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.HistoryApi();
let userId = 56; // Number | User ID.
let opts = {
  'startAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Leave blank or set to a date/time to filter earlier entries.
  'endAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Leave blank or set to a date/time to filter later entries.
  'display': "display_example", // String | Display format. Leave blank or set to `full` or `parent`.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null} // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[user_id]=desc`). Valid fields are `user_id` and `created_at`.
};
apiInstance.historyListForUser(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| User ID. | 
 **startAt** | **Date**| Leave blank or set to a date/time to filter earlier entries. | [optional] 
 **endAt** | **Date**| Leave blank or set to a date/time to filter later entries. | [optional] 
 **display** | **String**| Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[user_id]&#x3D;desc&#x60;). Valid fields are &#x60;user_id&#x60; and &#x60;created_at&#x60;. | [optional] 

### Return type

[**[ActionEntity]**](ActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## historyListLogins

> [ActionEntity] historyListLogins(opts)

List site login history.

List site login history.

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.HistoryApi();
let opts = {
  'startAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Leave blank or set to a date/time to filter earlier entries.
  'endAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Leave blank or set to a date/time to filter later entries.
  'display': "display_example", // String | Display format. Leave blank or set to `full` or `parent`.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null} // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[user_id]=desc`). Valid fields are `user_id` and `created_at`.
};
apiInstance.historyListLogins(opts, (error, data, response) => {
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
 **startAt** | **Date**| Leave blank or set to a date/time to filter earlier entries. | [optional] 
 **endAt** | **Date**| Leave blank or set to a date/time to filter later entries. | [optional] 
 **display** | **String**| Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[user_id]&#x3D;desc&#x60;). Valid fields are &#x60;user_id&#x60; and &#x60;created_at&#x60;. | [optional] 

### Return type

[**[ActionEntity]**](ActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

