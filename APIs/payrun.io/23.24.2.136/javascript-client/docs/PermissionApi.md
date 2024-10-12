# PayRunIo.PermissionApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePermission**](PermissionApi.md#deletePermission) | **DELETE** /Permission/{PermissionId} | Deletes the permission object
[**deletePermissionTag_0**](PermissionApi.md#deletePermissionTag_0) | **DELETE** /Permission/{PermissionId}/Tag/{TagId} | Delete Permission tag
[**getAllPermissionTags_0**](PermissionApi.md#getAllPermissionTags_0) | **GET** /Permissions/Tags | Get all Permission tags
[**getAllPermissionsWithTag_0**](PermissionApi.md#getAllPermissionsWithTag_0) | **GET** /Permissions/Tag/{TagId} | Get links to tagged Permissions
[**getPermission**](PermissionApi.md#getPermission) | **GET** /Permission/{PermissionId} | Gets the permission object
[**getPermissions**](PermissionApi.md#getPermissions) | **GET** /Permissions | Gets all permission objects
[**getTagFromPermission_0**](PermissionApi.md#getTagFromPermission_0) | **GET** /Permission/{PermissionId}/Tag/{TagId} | Get Permission tag
[**getTagsFromPermission_0**](PermissionApi.md#getTagsFromPermission_0) | **GET** /Permission/{PermissionId}/Tags | Get tags from Permission
[**getUserPermissions**](PermissionApi.md#getUserPermissions) | **GET** /User/{UserId}/Permissions | Gets the user permissions
[**getUsersFromPermission**](PermissionApi.md#getUsersFromPermission) | **GET** /Permission/{PermissionId}/Users | Gets the users with the specified permission
[**patchPermission**](PermissionApi.md#patchPermission) | **PATCH** /Permission/{PermissionId} | Patch permission object
[**postPermission**](PermissionApi.md#postPermission) | **POST** /Permissions | Post permisson object
[**putPermission**](PermissionApi.md#putPermission) | **PUT** /Permission/{PermissionId} | Puts permisson object
[**putPermissionTag_0**](PermissionApi.md#putPermissionTag_0) | **PUT** /Permission/{PermissionId}/Tag/{TagId} | Insert Permission tag



## deletePermission

> deletePermission(permissionId, authorization, apiVersion)

Deletes the permission object

Deletes the permission object from the application

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let permissionId = "permissionId_example"; // String | The permission unique identifier. E.g PERM001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePermission(permissionId, authorization, apiVersion, (error, data, response) => {
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
 **permissionId** | **String**| The permission unique identifier. E.g PERM001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePermissionTag_0

> deletePermissionTag_0(permissionId, tagId, authorization, apiVersion)

Delete Permission tag

Deletes a tag from the Permission

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let permissionId = "permissionId_example"; // String | The permission unique identifier. E.g PERM001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePermissionTag_0(permissionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **permissionId** | **String**| The permission unique identifier. E.g PERM001 | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllPermissionTags_0

> LinkCollection getAllPermissionTags_0(authorization, apiVersion)

Get all Permission tags

Get all tags from all Permissions

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllPermissionTags_0(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllPermissionsWithTag_0

> LinkCollection getAllPermissionsWithTag_0(tagId, authorization, apiVersion)

Get links to tagged Permissions

Gets the Permissions with the specified tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllPermissionsWithTag_0(tagId, authorization, apiVersion, (error, data, response) => {
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
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPermission

> Permission getPermission(permissionId, authorization, apiVersion)

Gets the permission object

Gets the permission object for application

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let permissionId = "permissionId_example"; // String | The permission unique identifier. E.g PERM001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPermission(permissionId, authorization, apiVersion, (error, data, response) => {
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
 **permissionId** | **String**| The permission unique identifier. E.g PERM001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Permission**](Permission.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPermissions

> LinkCollection getPermissions(authorization, apiVersion)

Gets all permission objects

Gets all permission objects for application

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPermissions(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagFromPermission_0

> Tag getTagFromPermission_0(permissionId, tagId, authorization, apiVersion)

Get Permission tag

Gets a tag from the Permission

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let permissionId = "permissionId_example"; // String | The permission unique identifier. E.g PERM001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromPermission_0(permissionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **permissionId** | **String**| The permission unique identifier. E.g PERM001 | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromPermission_0

> LinkCollection getTagsFromPermission_0(permissionId, authorization, apiVersion)

Get tags from Permission

Gets all tags from the Permission

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let permissionId = "permissionId_example"; // String | The permission unique identifier. E.g PERM001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromPermission_0(permissionId, authorization, apiVersion, (error, data, response) => {
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
 **permissionId** | **String**| The permission unique identifier. E.g PERM001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserPermissions

> LinkCollection getUserPermissions(userId, authorization, apiVersion)

Gets the user permissions

Gets the user permission instances

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let userId = "userId_example"; // String | The user unique identifier. E.g USER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getUserPermissions(userId, authorization, apiVersion, (error, data, response) => {
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
 **userId** | **String**| The user unique identifier. E.g USER001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersFromPermission

> LinkCollection getUsersFromPermission(permissionId, authorization, apiVersion)

Gets the users with the specified permission

Gets the users with the specified permission

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let permissionId = "permissionId_example"; // String | The permission unique identifier. E.g PERM001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getUsersFromPermission(permissionId, authorization, apiVersion, (error, data, response) => {
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
 **permissionId** | **String**| The permission unique identifier. E.g PERM001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchPermission

> Permission patchPermission(permissionId, authorization, apiVersion)

Patch permission object

Patch the permission object at the specified resource location

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let permissionId = "permissionId_example"; // String | The permission unique identifier. E.g PERM001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.patchPermission(permissionId, authorization, apiVersion, (error, data, response) => {
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
 **permissionId** | **String**| The permission unique identifier. E.g PERM001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Permission**](Permission.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postPermission

> Link postPermission(authorization, apiVersion)

Post permisson object

Post the new permission object into the application

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.postPermission(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putPermission

> Permission putPermission(permissionId, authorization, apiVersion)

Puts permisson object

Puts the permission object into the specified resource location

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let permissionId = "permissionId_example"; // String | The permission unique identifier. E.g PERM001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putPermission(permissionId, authorization, apiVersion, (error, data, response) => {
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
 **permissionId** | **String**| The permission unique identifier. E.g PERM001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Permission**](Permission.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putPermissionTag_0

> Tag putPermissionTag_0(permissionId, tagId, authorization, apiVersion)

Insert Permission tag

Inserts a tag on the Permission

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PermissionApi();
let permissionId = "permissionId_example"; // String | The permission unique identifier. E.g PERM001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putPermissionTag_0(permissionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **permissionId** | **String**| The permission unique identifier. E.g PERM001 | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

