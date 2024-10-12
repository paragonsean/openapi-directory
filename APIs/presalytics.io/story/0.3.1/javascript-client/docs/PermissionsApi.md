# Story.PermissionsApi

All URIs are relative to */story*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storyIdCollaboratorsUseridPermissiontypeGet**](PermissionsApi.md#storyIdCollaboratorsUseridPermissiontypeGet) | **GET** /{id}/collaborators/authorize/{story_collaborator_userid}/{permissiontype} | Permissions: Story Authorization for a User
[**storyPermissionTypesGet**](PermissionsApi.md#storyPermissionTypesGet) | **GET** /permission_types | Permissions: List Permission Types



## storyIdCollaboratorsUseridPermissiontypeGet

> storyIdCollaboratorsUseridPermissiontypeGet(id, storyCollaboratorUserid, permissiontype)

Permissions: Story Authorization for a User

Check whether user have certain types of permissions.  Use http status codes to understand if permission is granted - 204 &#x3D; Granted, 403 &#x3D; Forbidden

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.PermissionsApi();
let id = "id_example"; // String | the id from the story object
let storyCollaboratorUserid = "storyCollaboratorUserid_example"; // String | The presalytics userid (NOT the Id of the story_collaborator object)
let permissiontype = "permissiontype_example"; // String | the type of permission requested.  can be a permission_type object name (e.g., owner, editor, create, viewer, admin) or a permission type field (e.g., can_edit, can_view, can_add_collaborators, can_delete)
apiInstance.storyIdCollaboratorsUseridPermissiontypeGet(id, storyCollaboratorUserid, permissiontype, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **storyCollaboratorUserid** | **String**| The presalytics userid (NOT the Id of the story_collaborator object) | 
 **permissiontype** | **String**| the type of permission requested.  can be a permission_type object name (e.g., owner, editor, create, viewer, admin) or a permission type field (e.g., can_edit, can_view, can_add_collaborators, can_delete) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyPermissionTypesGet

> [PermissionType] storyPermissionTypesGet()

Permissions: List Permission Types

Returns a list of possible user permission types

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.PermissionsApi();
apiInstance.storyPermissionTypesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[PermissionType]**](PermissionType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

