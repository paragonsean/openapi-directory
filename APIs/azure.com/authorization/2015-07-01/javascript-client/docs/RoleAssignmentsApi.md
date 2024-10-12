# AuthorizationManagementClient.RoleAssignmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roleAssignmentsCreate**](RoleAssignmentsApi.md#roleAssignmentsCreate) | **PUT** /{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName} | 
[**roleAssignmentsCreateById**](RoleAssignmentsApi.md#roleAssignmentsCreateById) | **PUT** /{roleAssignmentId} | 
[**roleAssignmentsDelete**](RoleAssignmentsApi.md#roleAssignmentsDelete) | **DELETE** /{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName} | 
[**roleAssignmentsDeleteById**](RoleAssignmentsApi.md#roleAssignmentsDeleteById) | **DELETE** /{roleAssignmentId} | 
[**roleAssignmentsGet**](RoleAssignmentsApi.md#roleAssignmentsGet) | **GET** /{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName} | 
[**roleAssignmentsGetById**](RoleAssignmentsApi.md#roleAssignmentsGetById) | **GET** /{roleAssignmentId} | 
[**roleAssignmentsList**](RoleAssignmentsApi.md#roleAssignmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/roleAssignments | 
[**roleAssignmentsListForResource**](RoleAssignmentsApi.md#roleAssignmentsListForResource) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/roleAssignments | 
[**roleAssignmentsListForResourceGroup**](RoleAssignmentsApi.md#roleAssignmentsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/roleAssignments | 
[**roleAssignmentsListForScope**](RoleAssignmentsApi.md#roleAssignmentsListForScope) | **GET** /{scope}/providers/Microsoft.Authorization/roleAssignments | 



## roleAssignmentsCreate

> RoleAssignment roleAssignmentsCreate(scope, roleAssignmentName, apiVersion, parameters)



Creates a role assignment.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleAssignmentsApi();
let scope = "scope_example"; // String | The scope of the role assignment to create. The scope can be any REST resource instance. For example, use '/subscriptions/{subscription-id}/' for a subscription, '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for a resource group, and '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}' for a resource.
let roleAssignmentName = "roleAssignmentName_example"; // String | The name of the role assignment to create. It can be any valid GUID.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let parameters = new AuthorizationManagementClient.RoleAssignmentCreateParameters(); // RoleAssignmentCreateParameters | Parameters for the role assignment.
apiInstance.roleAssignmentsCreate(scope, roleAssignmentName, apiVersion, parameters, (error, data, response) => {
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
 **scope** | **String**| The scope of the role assignment to create. The scope can be any REST resource instance. For example, use &#39;/subscriptions/{subscription-id}/&#39; for a subscription, &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}&#39; for a resource group, and &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}&#39; for a resource. | 
 **roleAssignmentName** | **String**| The name of the role assignment to create. It can be any valid GUID. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **parameters** | [**RoleAssignmentCreateParameters**](RoleAssignmentCreateParameters.md)| Parameters for the role assignment. | 

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## roleAssignmentsCreateById

> RoleAssignment roleAssignmentsCreateById(roleAssignmentId, apiVersion, parameters)



Creates a role assignment by ID.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleAssignmentsApi();
let roleAssignmentId = "roleAssignmentId_example"; // String | The fully qualified ID of the role assignment, including the scope, resource name and resource type. Use the format, /{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}. Example: /subscriptions/{subId}/resourcegroups/{rgname}//providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let parameters = new AuthorizationManagementClient.RoleAssignmentCreateParameters(); // RoleAssignmentCreateParameters | Parameters for the role assignment.
apiInstance.roleAssignmentsCreateById(roleAssignmentId, apiVersion, parameters, (error, data, response) => {
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
 **roleAssignmentId** | **String**| The fully qualified ID of the role assignment, including the scope, resource name and resource type. Use the format, /{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}. Example: /subscriptions/{subId}/resourcegroups/{rgname}//providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **parameters** | [**RoleAssignmentCreateParameters**](RoleAssignmentCreateParameters.md)| Parameters for the role assignment. | 

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## roleAssignmentsDelete

> RoleAssignment roleAssignmentsDelete(scope, roleAssignmentName, apiVersion)



Deletes a role assignment.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleAssignmentsApi();
let scope = "scope_example"; // String | The scope of the role assignment to delete.
let roleAssignmentName = "roleAssignmentName_example"; // String | The name of the role assignment to delete.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.roleAssignmentsDelete(scope, roleAssignmentName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the role assignment to delete. | 
 **roleAssignmentName** | **String**| The name of the role assignment to delete. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roleAssignmentsDeleteById

> RoleAssignment roleAssignmentsDeleteById(roleAssignmentId, apiVersion)



Deletes a role assignment.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleAssignmentsApi();
let roleAssignmentId = "roleAssignmentId_example"; // String | The fully qualified ID of the role assignment, including the scope, resource name and resource type. Use the format, /{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}. Example: /subscriptions/{subId}/resourcegroups/{rgname}//providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.roleAssignmentsDeleteById(roleAssignmentId, apiVersion, (error, data, response) => {
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
 **roleAssignmentId** | **String**| The fully qualified ID of the role assignment, including the scope, resource name and resource type. Use the format, /{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}. Example: /subscriptions/{subId}/resourcegroups/{rgname}//providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roleAssignmentsGet

> RoleAssignment roleAssignmentsGet(scope, roleAssignmentName, apiVersion)



Get the specified role assignment.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleAssignmentsApi();
let scope = "scope_example"; // String | The scope of the role assignment.
let roleAssignmentName = "roleAssignmentName_example"; // String | The name of the role assignment to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.roleAssignmentsGet(scope, roleAssignmentName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the role assignment. | 
 **roleAssignmentName** | **String**| The name of the role assignment to get. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roleAssignmentsGetById

> RoleAssignment roleAssignmentsGetById(roleAssignmentId, apiVersion)



Gets a role assignment by ID.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleAssignmentsApi();
let roleAssignmentId = "roleAssignmentId_example"; // String | The fully qualified ID of the role assignment, including the scope, resource name and resource type. Use the format, /{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}. Example: /subscriptions/{subId}/resourcegroups/{rgname}//providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.roleAssignmentsGetById(roleAssignmentId, apiVersion, (error, data, response) => {
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
 **roleAssignmentId** | **String**| The fully qualified ID of the role assignment, including the scope, resource name and resource type. Use the format, /{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}. Example: /subscriptions/{subId}/resourcegroups/{rgname}//providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roleAssignmentsList

> RoleAssignmentListResult roleAssignmentsList(apiVersion, subscriptionId, opts)



Gets all role assignments for the subscription.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. Use $filter=atScope() to return all role assignments at or above the scope. Use $filter=principalId eq {id} to return all role assignments at, above or below the scope for the specified principal.
};
apiInstance.roleAssignmentsList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all role assignments at or above the scope. Use $filter&#x3D;principalId eq {id} to return all role assignments at, above or below the scope for the specified principal. | [optional] 

### Return type

[**RoleAssignmentListResult**](RoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roleAssignmentsListForResource

> RoleAssignmentListResult roleAssignmentsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, opts)



Gets role assignments for a resource.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleAssignmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
let parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
let resourceType = "resourceType_example"; // String | The resource type of the resource.
let resourceName = "resourceName_example"; // String | The name of the resource to get role assignments for.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. Use $filter=atScope() to return all role assignments at or above the scope. Use $filter=principalId eq {id} to return all role assignments at, above or below the scope for the specified principal.
};
apiInstance.roleAssignmentsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **parentResourcePath** | **String**| The parent resource identity. | 
 **resourceType** | **String**| The resource type of the resource. | 
 **resourceName** | **String**| The name of the resource to get role assignments for. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all role assignments at or above the scope. Use $filter&#x3D;principalId eq {id} to return all role assignments at, above or below the scope for the specified principal. | [optional] 

### Return type

[**RoleAssignmentListResult**](RoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roleAssignmentsListForResourceGroup

> RoleAssignmentListResult roleAssignmentsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts)



Gets role assignments for a resource group.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleAssignmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. Use $filter=atScope() to return all role assignments at or above the scope. Use $filter=principalId eq {id} to return all role assignments at, above or below the scope for the specified principal.
};
apiInstance.roleAssignmentsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all role assignments at or above the scope. Use $filter&#x3D;principalId eq {id} to return all role assignments at, above or below the scope for the specified principal. | [optional] 

### Return type

[**RoleAssignmentListResult**](RoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roleAssignmentsListForScope

> RoleAssignmentListResult roleAssignmentsListForScope(scope, apiVersion, opts)



Gets role assignments for a scope.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.RoleAssignmentsApi();
let scope = "scope_example"; // String | The scope of the role assignments.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. Use $filter=atScope() to return all role assignments at or above the scope. Use $filter=principalId eq {id} to return all role assignments at, above or below the scope for the specified principal.
};
apiInstance.roleAssignmentsListForScope(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| The scope of the role assignments. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all role assignments at or above the scope. Use $filter&#x3D;principalId eq {id} to return all role assignments at, above or below the scope for the specified principal. | [optional] 

### Return type

[**RoleAssignmentListResult**](RoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

