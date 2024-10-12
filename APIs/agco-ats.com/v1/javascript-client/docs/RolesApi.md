# AgcoApi.RolesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rolesDeleteRole**](RolesApi.md#rolesDeleteRole) | **DELETE** /api/v2/Roles/{id} | Deletes a User Role
[**rolesGetRole**](RolesApi.md#rolesGetRole) | **GET** /api/v2/Roles/{id} | Gets a User Role
[**rolesGetRolePermissions**](RolesApi.md#rolesGetRolePermissions) | **GET** /api/v2/Roles/{id}/Permissions | Get the Permissions for a Role
[**rolesGetRoles**](RolesApi.md#rolesGetRoles) | **GET** /api/v2/Roles | List Roles
[**rolesPostRole**](RolesApi.md#rolesPostRole) | **POST** /api/v2/Roles | Adds a User Role
[**rolesPutRole**](RolesApi.md#rolesPutRole) | **PUT** /api/v2/Roles/{id} | Updates a User Role
[**rolesPutRolePermissions**](RolesApi.md#rolesPutRolePermissions) | **PUT** /api/v2/Roles/{id}/Permissions | Manage the Permissions for a Role



## rolesDeleteRole

> rolesDeleteRole(id)

Deletes a User Role

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.RolesApi();
let id = 56; // Number | The role's id
apiInstance.rolesDeleteRole(id, (error, data, response) => {
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
 **id** | **Number**| The role&#39;s id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## rolesGetRole

> APIModelsRole rolesGetRole(id)

Gets a User Role

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.RolesApi();
let id = 56; // Number | The role's id
apiInstance.rolesGetRole(id, (error, data, response) => {
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
 **id** | **Number**| The role&#39;s id | 

### Return type

[**APIModelsRole**](APIModelsRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## rolesGetRolePermissions

> APIPagedResponseAPIModelsPermission rolesGetRolePermissions(id, opts)

Get the Permissions for a Role

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.RolesApi();
let id = 56; // Number | The id of the Role
let opts = {
  'name': "name_example", // String | Filter by permission name. Optional.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.rolesGetRolePermissions(id, opts, (error, data, response) => {
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
 **id** | **Number**| The id of the Role | 
 **name** | **String**| Filter by permission name. Optional. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseAPIModelsPermission**](APIPagedResponseAPIModelsPermission.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## rolesGetRoles

> APIPagedResponseAPIModelsRole rolesGetRoles(opts)

List Roles

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.RolesApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56, // Number | Optional. The page offset. The default page offset is 0.
  'name': "name_example", // String | Optional. Finds a role with the given name.
  'permissionID': 56, // Number | 
  'permissionName': "permissionName_example" // String | Optional. Filters roles by whether they contain the provided permission.
};
apiInstance.rolesGetRoles(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 
 **name** | **String**| Optional. Finds a role with the given name. | [optional] 
 **permissionID** | **Number**|  | [optional] 
 **permissionName** | **String**| Optional. Filters roles by whether they contain the provided permission. | [optional] 

### Return type

[**APIPagedResponseAPIModelsRole**](APIPagedResponseAPIModelsRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## rolesPostRole

> Number rolesPostRole(aPIModelsRole)

Adds a User Role

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.RolesApi();
let aPIModelsRole = new AgcoApi.APIModelsRole(); // APIModelsRole | Role to add
apiInstance.rolesPostRole(aPIModelsRole, (error, data, response) => {
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
 **aPIModelsRole** | [**APIModelsRole**](APIModelsRole.md)| Role to add | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## rolesPutRole

> rolesPutRole(id, aPIModelsRole)

Updates a User Role

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.RolesApi();
let id = 56; // Number | The role's id
let aPIModelsRole = new AgcoApi.APIModelsRole(); // APIModelsRole | The Updated Role
apiInstance.rolesPutRole(id, aPIModelsRole, (error, data, response) => {
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
 **id** | **Number**| The role&#39;s id | 
 **aPIModelsRole** | [**APIModelsRole**](APIModelsRole.md)| The Updated Role | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined


## rolesPutRolePermissions

> rolesPutRolePermissions(id, aPIModelsRolePermissionChange)

Manage the Permissions for a Role

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.RolesApi();
let id = 56; // Number | The id of the Role
let aPIModelsRolePermissionChange = [new AgcoApi.APIModelsRolePermissionChange()]; // [APIModelsRolePermissionChange] | Permissions Changes for the Role
apiInstance.rolesPutRolePermissions(id, aPIModelsRolePermissionChange, (error, data, response) => {
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
 **id** | **Number**| The id of the Role | 
 **aPIModelsRolePermissionChange** | [**[APIModelsRolePermissionChange]**](APIModelsRolePermissionChange.md)| Permissions Changes for the Role | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined

