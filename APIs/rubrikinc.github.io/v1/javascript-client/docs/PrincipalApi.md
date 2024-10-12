# RubrikRestApi.PrincipalApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignRolesToPrincipals**](PrincipalApi.md#assignRolesToPrincipals) | **POST** /principal/role | Assign roles to principals
[**getRolesForPrincipals**](PrincipalApi.md#getRolesForPrincipals) | **GET** /principal/role | Get roles assigned to principals
[**revokeRolesFromPrincipals**](PrincipalApi.md#revokeRolesFromPrincipals) | **POST** /principal/role/bulk_revoke | Revoke roles from principals
[**searchPrincipalsV1**](PrincipalApi.md#searchPrincipalsV1) | **GET** /principal | Search for principals



## assignRolesToPrincipals

> [RoleInfo] assignRolesToPrincipals(roleAssignmentRequest)

Assign roles to principals

Assign a set of roles to the specified principals.

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

let apiInstance = new RubrikRestApi.PrincipalApi();
let roleAssignmentRequest = new RubrikRestApi.RoleAssignmentRequest(); // RoleAssignmentRequest | A set of roles and a set of principals to which the roles should be granted. 
apiInstance.assignRolesToPrincipals(roleAssignmentRequest, (error, data, response) => {
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
 **roleAssignmentRequest** | [**RoleAssignmentRequest**](RoleAssignmentRequest.md)| A set of roles and a set of principals to which the roles should be granted.  | 

### Return type

[**[RoleInfo]**](RoleInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getRolesForPrincipals

> [PrincipalWithRoleInfo] getRolesForPrincipals(principals)

Get roles assigned to principals

Get a list of role information for all roles assigned to the principals. 

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

let apiInstance = new RubrikRestApi.PrincipalApi();
let principals = ["null"]; // [String] | IDs of the principals.
apiInstance.getRolesForPrincipals(principals, (error, data, response) => {
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
 **principals** | [**[String]**](String.md)| IDs of the principals. | 

### Return type

[**[PrincipalWithRoleInfo]**](PrincipalWithRoleInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## revokeRolesFromPrincipals

> revokeRolesFromPrincipals(roleAssignmentRequest)

Revoke roles from principals

Revoke a set of roles from the specified principals. 

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

let apiInstance = new RubrikRestApi.PrincipalApi();
let roleAssignmentRequest = new RubrikRestApi.RoleAssignmentRequest(); // RoleAssignmentRequest | A set of roles to revoke from a set of principals.
apiInstance.revokeRolesFromPrincipals(roleAssignmentRequest, (error, data, response) => {
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
 **roleAssignmentRequest** | [**RoleAssignmentRequest**](RoleAssignmentRequest.md)| A set of roles to revoke from a set of principals. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## searchPrincipalsV1

> PrincipalSummaryV1ListResponse searchPrincipalsV1(opts)

Search for principals

Search for principals based on the specified parameters.

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

let apiInstance = new RubrikRestApi.PrincipalApi();
let opts = {
  'limit': 56, // Number | Maximum number of results to return.
  'offset': 56, // Number | Starting offset of the results to return.
  'sortBy': "sortBy_example", // String | Attribute by which to sort. Default is \"name\".
  'sortOrder': "sortOrder_example", // String | Sort order. Default order is ascending.
  'authDomainId': "authDomainId_example", // String | ID of the authentication domain that contains the principal.
  'organizationId': "organizationId_example", // String | ID of the organization of which the principal is a member.
  'isAssignedRolesOrIsLocal': true, // Boolean | A Boolean that specifies whether the principal has any roles assigned or is a local user. When a principal is a local user, or when the principal has any roles assigned, this value is 'true'. 
  'roleId': "roleId_example", // String | ID of a role assigned to the principal.
  'name': "name_example", // String | The name of the principal.
  'principalType': "principalType_example", // String | The type of principal.
  'isTotpEnabled': true // Boolean | Indicates if the principal has TOTP authentication enabled. Returns the users with TOTP authentication enabled when the value is true. 
};
apiInstance.searchPrincipalsV1(opts, (error, data, response) => {
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
 **sortBy** | **String**| Attribute by which to sort. Default is \&quot;name\&quot;. | [optional] 
 **sortOrder** | **String**| Sort order. Default order is ascending. | [optional] 
 **authDomainId** | **String**| ID of the authentication domain that contains the principal. | [optional] 
 **organizationId** | **String**| ID of the organization of which the principal is a member. | [optional] 
 **isAssignedRolesOrIsLocal** | **Boolean**| A Boolean that specifies whether the principal has any roles assigned or is a local user. When a principal is a local user, or when the principal has any roles assigned, this value is &#39;true&#39;.  | [optional] 
 **roleId** | **String**| ID of a role assigned to the principal. | [optional] 
 **name** | **String**| The name of the principal. | [optional] 
 **principalType** | **String**| The type of principal. | [optional] 
 **isTotpEnabled** | **Boolean**| Indicates if the principal has TOTP authentication enabled. Returns the users with TOTP authentication enabled when the value is true.  | [optional] 

### Return type

[**PrincipalSummaryV1ListResponse**](PrincipalSummaryV1ListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

