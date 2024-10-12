# AgcoApi.PermissionsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissionsDeletePermission**](PermissionsApi.md#permissionsDeletePermission) | **DELETE** /api/v2/Permissions/{id} | Deletes a Permission
[**permissionsGetPermission**](PermissionsApi.md#permissionsGetPermission) | **GET** /api/v2/Permissions/{id} | Gets a Permission
[**permissionsGetPermissions**](PermissionsApi.md#permissionsGetPermissions) | **GET** /api/v2/Permissions | List Permissions
[**permissionsPostPermission**](PermissionsApi.md#permissionsPostPermission) | **POST** /api/v2/Permissions | Adds a Permission
[**permissionsPutPermission**](PermissionsApi.md#permissionsPutPermission) | **PUT** /api/v2/Permissions/{id} | Updates a Permission



## permissionsDeletePermission

> permissionsDeletePermission(id)

Deletes a Permission

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PermissionsApi();
let id = 56; // Number | Id of Permission
apiInstance.permissionsDeletePermission(id, (error, data, response) => {
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
 **id** | **Number**| Id of Permission | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## permissionsGetPermission

> APIModelsPermission permissionsGetPermission(id)

Gets a Permission

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PermissionsApi();
let id = 56; // Number | Id of Permission
apiInstance.permissionsGetPermission(id, (error, data, response) => {
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
 **id** | **Number**| Id of Permission | 

### Return type

[**APIModelsPermission**](APIModelsPermission.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## permissionsGetPermissions

> APIPagedResponseAPIModelsPermission permissionsGetPermissions(opts)

List Permissions

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PermissionsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56, // Number | Optional. The page offset. The default page offset is 0.
  'name': "name_example" // String | Filter by permission name. Supports ending wildcard (*). Optional.
};
apiInstance.permissionsGetPermissions(opts, (error, data, response) => {
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
 **name** | **String**| Filter by permission name. Supports ending wildcard (*). Optional. | [optional] 

### Return type

[**APIPagedResponseAPIModelsPermission**](APIPagedResponseAPIModelsPermission.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## permissionsPostPermission

> Number permissionsPostPermission(aPIModelsPermission)

Adds a Permission

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PermissionsApi();
let aPIModelsPermission = new AgcoApi.APIModelsPermission(); // APIModelsPermission | Permission to add
apiInstance.permissionsPostPermission(aPIModelsPermission, (error, data, response) => {
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
 **aPIModelsPermission** | [**APIModelsPermission**](APIModelsPermission.md)| Permission to add | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## permissionsPutPermission

> permissionsPutPermission(id, aPIModelsPermission)

Updates a Permission

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PermissionsApi();
let id = 56; // Number | Id of Permission
let aPIModelsPermission = new AgcoApi.APIModelsPermission(); // APIModelsPermission | The Updated Permission
apiInstance.permissionsPutPermission(id, aPIModelsPermission, (error, data, response) => {
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
 **id** | **Number**| Id of Permission | 
 **aPIModelsPermission** | [**APIModelsPermission**](APIModelsPermission.md)| The Updated Permission | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined

