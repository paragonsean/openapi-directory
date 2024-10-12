# AgcoApi.UserPermissionsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2RolesIdUsersPut**](UserPermissionsApi.md#apiV2RolesIdUsersPut) | **PUT** /api/v2/Roles/{id}/Users | Update a Role&#39;s users
[**apiV2UsersCurrentPermissionsGet**](UserPermissionsApi.md#apiV2UsersCurrentPermissionsGet) | **GET** /api/v2/Users/Current/Permissions | Get a user&#39;s permissions
[**userPermissionsGetCurrentUserRoles**](UserPermissionsApi.md#userPermissionsGetCurrentUserRoles) | **GET** /api/v2/Users/Current/Roles | Gets the current user&#39;s roles
[**userPermissionsGetPermissions**](UserPermissionsApi.md#userPermissionsGetPermissions) | **GET** /api/v2/Users/{id}/Permissions | Get a user&#39;s permissions
[**userPermissionsGetRoles**](UserPermissionsApi.md#userPermissionsGetRoles) | **GET** /api/v2/Users/{id}/Roles | Get a user&#39;s roles
[**userPermissionsGetUsers**](UserPermissionsApi.md#userPermissionsGetUsers) | **GET** /api/v2/Roles/{id}/Users | Get all user&#39;s in a role
[**userPermissionsPut**](UserPermissionsApi.md#userPermissionsPut) | **PUT** /api/v2/Users/{id}/Roles | Update a user&#39;s roles



## apiV2RolesIdUsersPut

> apiV2RolesIdUsersPut(id, aPIModelsRoleUserChange)

Update a Role&#39;s users

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UserPermissionsApi();
let id = 56; // Number | The Role's ID
let aPIModelsRoleUserChange = [new AgcoApi.APIModelsRoleUserChange()]; // [APIModelsRoleUserChange] | A list of changes to the Role's Users
apiInstance.apiV2RolesIdUsersPut(id, aPIModelsRoleUserChange, (error, data, response) => {
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
 **id** | **Number**| The Role&#39;s ID | 
 **aPIModelsRoleUserChange** | [**[APIModelsRoleUserChange]**](APIModelsRoleUserChange.md)| A list of changes to the Role&#39;s Users | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## apiV2UsersCurrentPermissionsGet

> APIPagedResponseAPIModelsUserEffectivePermission apiV2UsersCurrentPermissionsGet(opts)

Get a user&#39;s permissions

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UserPermissionsApi();
let opts = {
  'permission': "permission_example", // String | Filter by permission name. Supports ending wildcard (*). Optional.
  'limit': 56, // Number | The page limit. The default page limit is 10.
  'offset': 56 // Number | The page offset. The default page offset is 0.
};
apiInstance.apiV2UsersCurrentPermissionsGet(opts, (error, data, response) => {
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
 **permission** | **String**| Filter by permission name. Supports ending wildcard (*). Optional. | [optional] 
 **limit** | **Number**| The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseAPIModelsUserEffectivePermission**](APIPagedResponseAPIModelsUserEffectivePermission.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## userPermissionsGetCurrentUserRoles

> APIPagedResponseAPIModelsRole userPermissionsGetCurrentUserRoles(opts)

Gets the current user&#39;s roles

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UserPermissionsApi();
let opts = {
  'role': "role_example", // String | Filter by role name. Supports ending wildcard (*). Optional.
  'limit': 56, // Number | The page limit. The default page limit is 10.
  'offset': 56 // Number | The page offset. The default page offset is 0.
};
apiInstance.userPermissionsGetCurrentUserRoles(opts, (error, data, response) => {
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
 **role** | **String**| Filter by role name. Supports ending wildcard (*). Optional. | [optional] 
 **limit** | **Number**| The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseAPIModelsRole**](APIPagedResponseAPIModelsRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## userPermissionsGetPermissions

> APIPagedResponseAPIModelsUserEffectivePermission userPermissionsGetPermissions(id, opts)

Get a user&#39;s permissions

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UserPermissionsApi();
let id = 56; // Number | The User's ID
let opts = {
  'permission': "permission_example", // String | Filter by permission name. Supports ending wildcard (*). Optional.
  'limit': 56, // Number | The page limit. The default page limit is 10.
  'offset': 56 // Number | The page offset. The default page offset is 0.
};
apiInstance.userPermissionsGetPermissions(id, opts, (error, data, response) => {
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
 **id** | **Number**| The User&#39;s ID | 
 **permission** | **String**| Filter by permission name. Supports ending wildcard (*). Optional. | [optional] 
 **limit** | **Number**| The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseAPIModelsUserEffectivePermission**](APIPagedResponseAPIModelsUserEffectivePermission.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## userPermissionsGetRoles

> APIPagedResponseAPIModelsRole userPermissionsGetRoles(id, opts)

Get a user&#39;s roles

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UserPermissionsApi();
let id = 56; // Number | The User's ID
let opts = {
  'role': "role_example", // String | Filter by role name. Supports ending wildcard (*). Optional.
  'limit': 56, // Number | The page limit. The default page limit is 10.
  'offset': 56 // Number | The page offset. The default page offset is 0.
};
apiInstance.userPermissionsGetRoles(id, opts, (error, data, response) => {
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
 **id** | **Number**| The User&#39;s ID | 
 **role** | **String**| Filter by role name. Supports ending wildcard (*). Optional. | [optional] 
 **limit** | **Number**| The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseAPIModelsRole**](APIPagedResponseAPIModelsRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## userPermissionsGetUsers

> APIPagedResponseAPIModelsUser userPermissionsGetUsers(id, opts)

Get all user&#39;s in a role

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UserPermissionsApi();
let id = 56; // Number | The Role's ID
let opts = {
  'limit': 56, // Number | The page limit. The default page limit is 10.
  'offset': 56 // Number | The page offset. The default page offset is 0.
};
apiInstance.userPermissionsGetUsers(id, opts, (error, data, response) => {
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
 **id** | **Number**| The Role&#39;s ID | 
 **limit** | **Number**| The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseAPIModelsUser**](APIPagedResponseAPIModelsUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## userPermissionsPut

> userPermissionsPut(id, aPIModelsUserRoleChange)

Update a user&#39;s roles

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UserPermissionsApi();
let id = 56; // Number | The User's ID
let aPIModelsUserRoleChange = [new AgcoApi.APIModelsUserRoleChange()]; // [APIModelsUserRoleChange] | A list of changes to the User's Roles
apiInstance.userPermissionsPut(id, aPIModelsUserRoleChange, (error, data, response) => {
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
 **id** | **Number**| The User&#39;s ID | 
 **aPIModelsUserRoleChange** | [**[APIModelsUserRoleChange]**](APIModelsUserRoleChange.md)| A list of changes to the User&#39;s Roles | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

