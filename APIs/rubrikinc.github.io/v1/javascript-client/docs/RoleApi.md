# RubrikRestApi.RoleApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRole**](RoleApi.md#createRole) | **POST** /role | Create a new role
[**deleteRole**](RoleApi.md#deleteRole) | **DELETE** /role/{id} | Delete a role
[**getRole**](RoleApi.md#getRole) | **GET** /role/{id} | Get role information for the specified role
[**getRoles**](RoleApi.md#getRoles) | **GET** /role | Get all roles in an organization
[**updateRole**](RoleApi.md#updateRole) | **PATCH** /role/{id} | Update role information



## createRole

> RoleInfo createRole(roleInfoCreate)

Create a new role

Create a new role in the current organization.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.RoleApi();
let roleInfoCreate = new RubrikRestApi.RoleInfoCreate(); // RoleInfoCreate | Information about the role.
apiInstance.createRole(roleInfoCreate, (error, data, response) => {
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
 **roleInfoCreate** | [**RoleInfoCreate**](RoleInfoCreate.md)| Information about the role. | 

### Return type

[**RoleInfo**](RoleInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteRole

> deleteRole(id)

Delete a role

Delete the role with the specified ID.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.RoleApi();
let id = "id_example"; // String | ID of the role.
apiInstance.deleteRole(id, (error, data, response) => {
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
 **id** | **String**| ID of the role. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRole

> RoleInfo getRole(id)

Get role information for the specified role

Get role information for the role with the specified ID.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.RoleApi();
let id = "id_example"; // String | ID of the role.
apiInstance.getRole(id, (error, data, response) => {
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
 **id** | **String**| ID of the role. | 

### Return type

[**RoleInfo**](RoleInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRoles

> RoleInfoListResponse getRoles(opts)

Get all roles in an organization

Get a list of role information for all roles in the specified organization. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.RoleApi();
let opts = {
  'limit': 56, // Number | Maximum number of results to return.
  'offset': 56, // Number | Starting offset of the results to return.
  'sortBy': "'Name'", // String | Attribute used to sort the role list.
  'sortOrder': "'asc'", // String | Sort order used, ascending or descending.
  'organizationId': "organizationId_example", // String | The ID of the organization the roles are a part of. When empty, the Rubrik cluster infers the organization from the session. 
  'name': "name_example", // String | The name of the role.
  'roleTemplate': ["null"] // [String] | List of comma-separated role templates by which to filter the roles. 
};
apiInstance.getRoles(opts, (error, data, response) => {
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
 **limit** | **Number**| Maximum number of results to return. | [optional] 
 **offset** | **Number**| Starting offset of the results to return. | [optional] 
 **sortBy** | **String**| Attribute used to sort the role list. | [optional] [default to &#39;Name&#39;]
 **sortOrder** | **String**| Sort order used, ascending or descending. | [optional] [default to &#39;asc&#39;]
 **organizationId** | **String**| The ID of the organization the roles are a part of. When empty, the Rubrik cluster infers the organization from the session.  | [optional] 
 **name** | **String**| The name of the role. | [optional] 
 **roleTemplate** | [**[String]**](String.md)| List of comma-separated role templates by which to filter the roles.  | [optional] 

### Return type

[**RoleInfoListResponse**](RoleInfoListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRole

> RoleInfo updateRole(id, roleInfoUpdate)

Update role information

Update the role information for the specified role.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.RoleApi();
let id = "id_example"; // String | ID of the role.
let roleInfoUpdate = new RubrikRestApi.RoleInfoUpdate(); // RoleInfoUpdate | Information about the role.
apiInstance.updateRole(id, roleInfoUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the role. | 
 **roleInfoUpdate** | [**RoleInfoUpdate**](RoleInfoUpdate.md)| Information about the role. | 

### Return type

[**RoleInfo**](RoleInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

