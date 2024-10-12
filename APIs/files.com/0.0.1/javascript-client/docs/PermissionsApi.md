# FilesComApi.PermissionsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePermissionsId**](PermissionsApi.md#deletePermissionsId) | **DELETE** /permissions/{id} | Delete Permission
[**getPermissions**](PermissionsApi.md#getPermissions) | **GET** /permissions | List Permissions
[**postPermissions**](PermissionsApi.md#postPermissions) | **POST** /permissions | Create Permission



## deletePermissionsId

> deletePermissionsId(id)

Delete Permission

Delete Permission

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.PermissionsApi();
let id = 56; // Number | Permission ID.
apiInstance.deletePermissionsId(id, (error, data, response) => {
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
 **id** | **Number**| Permission ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPermissions

> [PermissionEntity] getPermissions(opts)

List Permissions

List Permissions

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.PermissionsApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[group_id]=desc`). Valid fields are `group_id`, `path`, `user_id` or `permission`.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `group_id`, `user_id` or `path`. Valid field combinations are `[ group_id, path ]` and `[ user_id, path ]`.
  'filterPrefix': {key: null}, // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `path`.
  'path': "path_example", // String | DEPRECATED: Permission path.  If provided, will scope permissions to this path. Use `filter[path]` instead.
  'groupId': "groupId_example", // String | DEPRECATED: Group ID.  If provided, will scope permissions to this group. Use `filter[group_id]` instead.`
  'userId': "userId_example", // String | DEPRECATED: User ID.  If provided, will scope permissions to this user. Use `filter[user_id]` instead.`
  'includeGroups': true // Boolean | If searching by user or group, also include user's permissions that are inherited from its groups?
};
apiInstance.getPermissions(opts, (error, data, response) => {
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
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[group_id]&#x3D;desc&#x60;). Valid fields are &#x60;group_id&#x60;, &#x60;path&#x60;, &#x60;user_id&#x60; or &#x60;permission&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;group_id&#x60;, &#x60;user_id&#x60; or &#x60;path&#x60;. Valid field combinations are &#x60;[ group_id, path ]&#x60; and &#x60;[ user_id, path ]&#x60;. | [optional] 
 **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;path&#x60;. | [optional] 
 **path** | **String**| DEPRECATED: Permission path.  If provided, will scope permissions to this path. Use &#x60;filter[path]&#x60; instead. | [optional] 
 **groupId** | **String**| DEPRECATED: Group ID.  If provided, will scope permissions to this group. Use &#x60;filter[group_id]&#x60; instead.&#x60; | [optional] 
 **userId** | **String**| DEPRECATED: User ID.  If provided, will scope permissions to this user. Use &#x60;filter[user_id]&#x60; instead.&#x60; | [optional] 
 **includeGroups** | **Boolean**| If searching by user or group, also include user&#39;s permissions that are inherited from its groups? | [optional] 

### Return type

[**[PermissionEntity]**](PermissionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postPermissions

> PermissionEntity postPermissions(opts)

Create Permission

Create Permission

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.PermissionsApi();
let opts = {
  'groupId': 56, // Number | Group ID
  'path': "path_example", // String | Folder path
  'permission': "permission_example", // String |  Permission type.  Can be `admin`, `full`, `readonly`, `writeonly`, `list`, or `history`
  'recursive': true, // Boolean | Apply to subfolders recursively?
  'userId': 56, // Number | User ID.  Provide `username` or `user_id`
  'username': "username_example" // String | User username.  Provide `username` or `user_id`
};
apiInstance.postPermissions(opts, (error, data, response) => {
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
 **groupId** | **Number**| Group ID | [optional] 
 **path** | **String**| Folder path | [optional] 
 **permission** | **String**|  Permission type.  Can be &#x60;admin&#x60;, &#x60;full&#x60;, &#x60;readonly&#x60;, &#x60;writeonly&#x60;, &#x60;list&#x60;, or &#x60;history&#x60; | [optional] 
 **recursive** | **Boolean**| Apply to subfolders recursively? | [optional] 
 **userId** | **Number**| User ID.  Provide &#x60;username&#x60; or &#x60;user_id&#x60; | [optional] 
 **username** | **String**| User username.  Provide &#x60;username&#x60; or &#x60;user_id&#x60; | [optional] 

### Return type

[**PermissionEntity**](PermissionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

