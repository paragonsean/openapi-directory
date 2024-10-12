# FilesComApi.ApiKeysApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteApiKeysId**](ApiKeysApi.md#deleteApiKeysId) | **DELETE** /api_keys/{id} | Delete Api Key
[**getApiKeys**](ApiKeysApi.md#getApiKeys) | **GET** /api_keys | List Api Keys
[**getApiKeysId**](ApiKeysApi.md#getApiKeysId) | **GET** /api_keys/{id} | Show Api Key
[**patchApiKeysId**](ApiKeysApi.md#patchApiKeysId) | **PATCH** /api_keys/{id} | Update Api Key
[**postApiKeys**](ApiKeysApi.md#postApiKeys) | **POST** /api_keys | Create Api Key



## deleteApiKeysId

> deleteApiKeysId(id)

Delete Api Key

Delete Api Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ApiKeysApi();
let id = 56; // Number | Api Key ID.
apiInstance.deleteApiKeysId(id, (error, data, response) => {
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
 **id** | **Number**| Api Key ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getApiKeys

> [ApiKeyEntity] getApiKeys(opts)

List Api Keys

List Api Keys

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ApiKeysApi();
let opts = {
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[expires_at]=desc`). Valid fields are `expires_at`.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `expires_at`.
  'filterGt': {key: null}, // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `expires_at`.
  'filterGteq': {key: null}, // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `expires_at`.
  'filterLt': {key: null}, // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `expires_at`.
  'filterLteq': {key: null} // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `expires_at`.
};
apiInstance.getApiKeys(opts, (error, data, response) => {
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
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[expires_at]&#x3D;desc&#x60;). Valid fields are &#x60;expires_at&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] 
 **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] 
 **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] 
 **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] 
 **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] 

### Return type

[**[ApiKeyEntity]**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApiKeysId

> ApiKeyEntity getApiKeysId(id)

Show Api Key

Show Api Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ApiKeysApi();
let id = 56; // Number | Api Key ID.
apiInstance.getApiKeysId(id, (error, data, response) => {
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
 **id** | **Number**| Api Key ID. | 

### Return type

[**ApiKeyEntity**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchApiKeysId

> ApiKeyEntity patchApiKeysId(id, opts)

Update Api Key

Update Api Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ApiKeysApi();
let id = 56; // Number | Api Key ID.
let opts = {
  'description': "description_example", // String | User-supplied description of API key.
  'expiresAt': new Date("2013-10-20T19:20:30+01:00"), // Date | API Key expiration date
  'name': "name_example", // String | Internal name for the API Key.  For your use.
  'permissionSet': "permissionSet_example" // String | Permissions for this API Key.  Keys with the `desktop_app` permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
};
apiInstance.patchApiKeysId(id, opts, (error, data, response) => {
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
 **id** | **Number**| Api Key ID. | 
 **description** | **String**| User-supplied description of API key. | [optional] 
 **expiresAt** | **Date**| API Key expiration date | [optional] 
 **name** | **String**| Internal name for the API Key.  For your use. | [optional] 
 **permissionSet** | **String**| Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know. | [optional] 

### Return type

[**ApiKeyEntity**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postApiKeys

> ApiKeyEntity postApiKeys(opts)

Create Api Key

Create Api Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ApiKeysApi();
let opts = {
  'description': "description_example", // String | User-supplied description of API key.
  'expiresAt': new Date("2013-10-20T19:20:30+01:00"), // Date | API Key expiration date
  'name': "name_example", // String | Internal name for the API Key.  For your use.
  'path': "path_example", // String | Folder path restriction for this api key.
  'permissionSet': "'full'", // String | Permissions for this API Key.  Keys with the `desktop_app` permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
  'userId': 56 // Number | User ID.  Provide a value of `0` to operate the current session's user.
};
apiInstance.postApiKeys(opts, (error, data, response) => {
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
 **description** | **String**| User-supplied description of API key. | [optional] 
 **expiresAt** | **Date**| API Key expiration date | [optional] 
 **name** | **String**| Internal name for the API Key.  For your use. | [optional] 
 **path** | **String**| Folder path restriction for this api key. | [optional] 
 **permissionSet** | **String**| Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know. | [optional] [default to &#39;full&#39;]
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 

### Return type

[**ApiKeyEntity**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

