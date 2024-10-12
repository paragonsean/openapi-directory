# FilesComApi.SettingsChangesApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSettingsChanges**](SettingsChangesApi.md#getSettingsChanges) | **GET** /settings_changes | List Settings Changes



## getSettingsChanges

> [SettingsChangeEntity] getSettingsChanges(opts)

List Settings Changes

List Settings Changes

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SettingsChangesApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[api_key_id]=desc`). Valid fields are `api_key_id`, `created_at` or `user_id`.
  'apiKeyId': "apiKeyId_example", // String | If set, return records where the specified field is equal to the supplied value.
  'userId': "userId_example", // String | If set, return records where the specified field is equal to the supplied value.
  'filter': {key: null} // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `api_key_id` and `user_id`.
};
apiInstance.getSettingsChanges(opts, (error, data, response) => {
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
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[api_key_id]&#x3D;desc&#x60;). Valid fields are &#x60;api_key_id&#x60;, &#x60;created_at&#x60; or &#x60;user_id&#x60;. | [optional] 
 **apiKeyId** | **String**| If set, return records where the specified field is equal to the supplied value. | [optional] 
 **userId** | **String**| If set, return records where the specified field is equal to the supplied value. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;api_key_id&#x60; and &#x60;user_id&#x60;. | [optional] 

### Return type

[**[SettingsChangeEntity]**](SettingsChangeEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

