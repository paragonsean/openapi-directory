# AuthorizationManagementClient.DenyAssignmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**denyAssignmentsGet**](DenyAssignmentsApi.md#denyAssignmentsGet) | **GET** /{scope}/providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId} | 
[**denyAssignmentsGetById**](DenyAssignmentsApi.md#denyAssignmentsGetById) | **GET** /{denyAssignmentId} | 
[**denyAssignmentsList**](DenyAssignmentsApi.md#denyAssignmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/denyAssignments | 
[**denyAssignmentsListForResource**](DenyAssignmentsApi.md#denyAssignmentsListForResource) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/denyAssignments | 
[**denyAssignmentsListForResourceGroup**](DenyAssignmentsApi.md#denyAssignmentsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/denyAssignments | 
[**denyAssignmentsListForScope**](DenyAssignmentsApi.md#denyAssignmentsListForScope) | **GET** /{scope}/providers/Microsoft.Authorization/denyAssignments | 



## denyAssignmentsGet

> DenyAssignment denyAssignmentsGet(scope, denyAssignmentId, apiVersion)



Get the specified deny assignment.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.DenyAssignmentsApi();
let scope = "scope_example"; // String | The scope of the deny assignment.
let denyAssignmentId = "denyAssignmentId_example"; // String | The ID of the deny assignment to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.denyAssignmentsGet(scope, denyAssignmentId, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the deny assignment. | 
 **denyAssignmentId** | **String**| The ID of the deny assignment to get. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**DenyAssignment**](DenyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## denyAssignmentsGetById

> DenyAssignment denyAssignmentsGetById(denyAssignmentId, apiVersion)



Gets a deny assignment by ID.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.DenyAssignmentsApi();
let denyAssignmentId = "denyAssignmentId_example"; // String | The fully qualified deny assignment ID. For example, use the format, /subscriptions/{guid}/providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId} for subscription level deny assignments, or /providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId} for tenant level deny assignments.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.denyAssignmentsGetById(denyAssignmentId, apiVersion, (error, data, response) => {
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
 **denyAssignmentId** | **String**| The fully qualified deny assignment ID. For example, use the format, /subscriptions/{guid}/providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId} for subscription level deny assignments, or /providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId} for tenant level deny assignments. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**DenyAssignment**](DenyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## denyAssignmentsList

> DenyAssignmentListResult denyAssignmentsList(subscriptionId, apiVersion, opts)



Gets all deny assignments for the subscription.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.DenyAssignmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. Use $filter=atScope() to return all deny assignments at or above the scope. Use $filter=denyAssignmentName eq '{name}' to search deny assignments by name at specified scope. Use $filter=principalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. Use $filter=gdprExportPrincipalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned.
};
apiInstance.denyAssignmentsList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all deny assignments at or above the scope. Use $filter&#x3D;denyAssignmentName eq &#39;{name}&#39; to search deny assignments by name at specified scope. Use $filter&#x3D;principalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. Use $filter&#x3D;gdprExportPrincipalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned. | [optional] 

### Return type

[**DenyAssignmentListResult**](DenyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## denyAssignmentsListForResource

> DenyAssignmentListResult denyAssignmentsListForResource(subscriptionId, resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, opts)



Gets deny assignments for a resource.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.DenyAssignmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
let parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
let resourceType = "resourceType_example"; // String | The resource type of the resource.
let resourceName = "resourceName_example"; // String | The name of the resource to get deny assignments for.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. Use $filter=atScope() to return all deny assignments at or above the scope. Use $filter=denyAssignmentName eq '{name}' to search deny assignments by name at specified scope. Use $filter=principalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. Use $filter=gdprExportPrincipalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned.
};
apiInstance.denyAssignmentsListForResource(subscriptionId, resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **parentResourcePath** | **String**| The parent resource identity. | 
 **resourceType** | **String**| The resource type of the resource. | 
 **resourceName** | **String**| The name of the resource to get deny assignments for. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all deny assignments at or above the scope. Use $filter&#x3D;denyAssignmentName eq &#39;{name}&#39; to search deny assignments by name at specified scope. Use $filter&#x3D;principalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. Use $filter&#x3D;gdprExportPrincipalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned. | [optional] 

### Return type

[**DenyAssignmentListResult**](DenyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## denyAssignmentsListForResourceGroup

> DenyAssignmentListResult denyAssignmentsListForResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)



Gets deny assignments for a resource group.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.DenyAssignmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. Use $filter=atScope() to return all deny assignments at or above the scope. Use $filter=denyAssignmentName eq '{name}' to search deny assignments by name at specified scope. Use $filter=principalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. Use $filter=gdprExportPrincipalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned.
};
apiInstance.denyAssignmentsListForResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all deny assignments at or above the scope. Use $filter&#x3D;denyAssignmentName eq &#39;{name}&#39; to search deny assignments by name at specified scope. Use $filter&#x3D;principalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. Use $filter&#x3D;gdprExportPrincipalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned. | [optional] 

### Return type

[**DenyAssignmentListResult**](DenyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## denyAssignmentsListForScope

> DenyAssignmentListResult denyAssignmentsListForScope(scope, apiVersion, opts)



Gets deny assignments for a scope.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.DenyAssignmentsApi();
let scope = "scope_example"; // String | The scope of the deny assignments.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. Use $filter=atScope() to return all deny assignments at or above the scope. Use $filter=denyAssignmentName eq '{name}' to search deny assignments by name at specified scope. Use $filter=principalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. Use $filter=gdprExportPrincipalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned.
};
apiInstance.denyAssignmentsListForScope(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| The scope of the deny assignments. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all deny assignments at or above the scope. Use $filter&#x3D;denyAssignmentName eq &#39;{name}&#39; to search deny assignments by name at specified scope. Use $filter&#x3D;principalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. Use $filter&#x3D;gdprExportPrincipalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned. | [optional] 

### Return type

[**DenyAssignmentListResult**](DenyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

