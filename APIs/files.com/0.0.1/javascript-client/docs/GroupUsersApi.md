# FilesComApi.GroupUsersApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteGroupUsersId**](GroupUsersApi.md#deleteGroupUsersId) | **DELETE** /group_users/{id} | Delete Group User
[**getGroupUsers**](GroupUsersApi.md#getGroupUsers) | **GET** /group_users | List Group Users
[**patchGroupUsersId**](GroupUsersApi.md#patchGroupUsersId) | **PATCH** /group_users/{id} | Update Group User
[**postGroupUsers**](GroupUsersApi.md#postGroupUsers) | **POST** /group_users | Create Group User



## deleteGroupUsersId

> deleteGroupUsersId(id, groupId, userId)

Delete Group User

Delete Group User

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupUsersApi();
let id = 56; // Number | Group User ID.
let groupId = 56; // Number | Group ID from which to remove user.
let userId = 56; // Number | User ID to remove from group.
apiInstance.deleteGroupUsersId(id, groupId, userId, (error, data, response) => {
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
 **id** | **Number**| Group User ID. | 
 **groupId** | **Number**| Group ID from which to remove user. | 
 **userId** | **Number**| User ID to remove from group. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGroupUsers

> [GroupUserEntity] getGroupUsers(opts)

List Group Users

List Group Users

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupUsersApi();
let opts = {
  'userId': 56, // Number | User ID.  If provided, will return group_users of this user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'groupId': 56 // Number | Group ID.  If provided, will return group_users of this group.
};
apiInstance.getGroupUsers(opts, (error, data, response) => {
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
 **userId** | **Number**| User ID.  If provided, will return group_users of this user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **groupId** | **Number**| Group ID.  If provided, will return group_users of this group. | [optional] 

### Return type

[**[GroupUserEntity]**](GroupUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchGroupUsersId

> GroupUserEntity patchGroupUsersId(id, groupId, userId, opts)

Update Group User

Update Group User

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupUsersApi();
let id = 56; // Number | Group User ID.
let groupId = 56; // Number | Group ID to add user to.
let userId = 56; // Number | User ID to add to group.
let opts = {
  'admin': true // Boolean | Is the user a group administrator?
};
apiInstance.patchGroupUsersId(id, groupId, userId, opts, (error, data, response) => {
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
 **id** | **Number**| Group User ID. | 
 **groupId** | **Number**| Group ID to add user to. | 
 **userId** | **Number**| User ID to add to group. | 
 **admin** | **Boolean**| Is the user a group administrator? | [optional] 

### Return type

[**GroupUserEntity**](GroupUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postGroupUsers

> GroupUserEntity postGroupUsers(groupId, userId, opts)

Create Group User

Create Group User

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupUsersApi();
let groupId = 56; // Number | Group ID to add user to.
let userId = 56; // Number | User ID to add to group.
let opts = {
  'admin': true // Boolean | Is the user a group administrator?
};
apiInstance.postGroupUsers(groupId, userId, opts, (error, data, response) => {
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
 **groupId** | **Number**| Group ID to add user to. | 
 **userId** | **Number**| User ID to add to group. | 
 **admin** | **Boolean**| Is the user a group administrator? | [optional] 

### Return type

[**GroupUserEntity**](GroupUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

