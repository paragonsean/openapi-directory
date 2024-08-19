# AuthorizationManagementClient.RoleDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roleDefinitionsCreateOrUpdate**](RoleDefinitionsApi.md#roleDefinitionsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId} | 
[**roleDefinitionsDelete**](RoleDefinitionsApi.md#roleDefinitionsDelete) | **DELETE** /{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId} | 
[**roleDefinitionsGet**](RoleDefinitionsApi.md#roleDefinitionsGet) | **GET** /{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId} | 
[**roleDefinitionsList**](RoleDefinitionsApi.md#roleDefinitionsList) | **GET** /{scope}/providers/Microsoft.Authorization/roleDefinitions | 



## roleDefinitionsCreateOrUpdate

> RoleDefinition roleDefinitionsCreateOrUpdate(scope, roleDefinitionId, apiVersion, roleDefinition)



Creates or updates a role definition.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleDefinitionsApi();
let scope = "scope_example"; // String | The scope of the role definition.
let roleDefinitionId = "roleDefinitionId_example"; // String | The ID of the role definition.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let roleDefinition = new AuthorizationManagementClient.RoleDefinition(); // RoleDefinition | The values for the role definition.
apiInstance.roleDefinitionsCreateOrUpdate(scope, roleDefinitionId, apiVersion, roleDefinition, (error, data, response) => {
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
 **scope** | **String**| The scope of the role definition. | 
 **roleDefinitionId** | **String**| The ID of the role definition. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **roleDefinition** | [**RoleDefinition**](RoleDefinition.md)| The values for the role definition. | 

### Return type

[**RoleDefinition**](RoleDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## roleDefinitionsDelete

> RoleDefinition roleDefinitionsDelete(scope, roleDefinitionId, apiVersion)



Deletes a role definition.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleDefinitionsApi();
let scope = "scope_example"; // String | The scope of the role definition.
let roleDefinitionId = "roleDefinitionId_example"; // String | The ID of the role definition to delete.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.roleDefinitionsDelete(scope, roleDefinitionId, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the role definition. | 
 **roleDefinitionId** | **String**| The ID of the role definition to delete. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**RoleDefinition**](RoleDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roleDefinitionsGet

> RoleDefinition roleDefinitionsGet(scope, roleDefinitionId, apiVersion)



Get role definition by name (GUID).

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleDefinitionsApi();
let scope = "scope_example"; // String | The scope of the role definition.
let roleDefinitionId = "roleDefinitionId_example"; // String | The ID of the role definition.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.roleDefinitionsGet(scope, roleDefinitionId, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the role definition. | 
 **roleDefinitionId** | **String**| The ID of the role definition. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**RoleDefinition**](RoleDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roleDefinitionsList

> RoleDefinitionListResult roleDefinitionsList(scope, apiVersion, opts)



Get all role definitions that are applicable at scope and above.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleDefinitionsApi();
let scope = "scope_example"; // String | The scope of the role definition.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. Use atScopeAndBelow filter to search below the given scope as well.
};
apiInstance.roleDefinitionsList(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| The scope of the role definition. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **filter** | **String**| The filter to apply on the operation. Use atScopeAndBelow filter to search below the given scope as well. | [optional] 

### Return type

[**RoleDefinitionListResult**](RoleDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

