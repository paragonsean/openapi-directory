# PolicyClient.PolicyAssignmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policyAssignmentsCreate**](PolicyAssignmentsApi.md#policyAssignmentsCreate) | **PUT** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} | Creates or updates a policy assignment.
[**policyAssignmentsCreateById**](PolicyAssignmentsApi.md#policyAssignmentsCreateById) | **PUT** /{policyAssignmentId} | Creates or updates a policy assignment.
[**policyAssignmentsDelete**](PolicyAssignmentsApi.md#policyAssignmentsDelete) | **DELETE** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} | Deletes a policy assignment.
[**policyAssignmentsDeleteById**](PolicyAssignmentsApi.md#policyAssignmentsDeleteById) | **DELETE** /{policyAssignmentId} | Deletes a policy assignment.
[**policyAssignmentsGet**](PolicyAssignmentsApi.md#policyAssignmentsGet) | **GET** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} | Retrieves a policy assignment.
[**policyAssignmentsGetById**](PolicyAssignmentsApi.md#policyAssignmentsGetById) | **GET** /{policyAssignmentId} | Retrieves the policy assignment with the given ID.
[**policyAssignmentsList**](PolicyAssignmentsApi.md#policyAssignmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyAssignments | Retrieves all policy assignments that apply to a subscription.
[**policyAssignmentsListForResource**](PolicyAssignmentsApi.md#policyAssignmentsListForResource) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/policyAssignments | Retrieves all policy assignments that apply to a resource.
[**policyAssignmentsListForResourceGroup**](PolicyAssignmentsApi.md#policyAssignmentsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/policyAssignments | Retrieves all policy assignments that apply to a resource group.



## policyAssignmentsCreate

> PolicyAssignment policyAssignmentsCreate(scope, policyAssignmentName, apiVersion, parameters)

Creates or updates a policy assignment.

 This operation creates or updates a policy assignment with the given scope and name. Policy assignments apply to all resources contained within their scope. For example, when you assign a policy at resource group scope, that policy applies to all resources in the group.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let scope = "scope_example"; // String | The scope of the policy assignment. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
let policyAssignmentName = "policyAssignmentName_example"; // String | The name of the policy assignment.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let parameters = new PolicyClient.PolicyAssignment(); // PolicyAssignment | Parameters for the policy assignment.
apiInstance.policyAssignmentsCreate(scope, policyAssignmentName, apiVersion, parameters, (error, data, response) => {
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
 **scope** | **String**| The scope of the policy assignment. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39; | 
 **policyAssignmentName** | **String**| The name of the policy assignment. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **parameters** | [**PolicyAssignment**](PolicyAssignment.md)| Parameters for the policy assignment. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## policyAssignmentsCreateById

> PolicyAssignment policyAssignmentsCreateById(policyAssignmentId, apiVersion, parameters)

Creates or updates a policy assignment.

This operation creates or updates the policy assignment with the given ID. Policy assignments made on a scope apply to all resources contained in that scope. For example, when you assign a policy to a resource group that policy applies to all resources in the group. Policy assignment IDs have this format: &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39;.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let policyAssignmentId = "policyAssignmentId_example"; // String | The ID of the policy assignment to create. Use the format '{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let parameters = new PolicyClient.PolicyAssignment(); // PolicyAssignment | Parameters for policy assignment.
apiInstance.policyAssignmentsCreateById(policyAssignmentId, apiVersion, parameters, (error, data, response) => {
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
 **policyAssignmentId** | **String**| The ID of the policy assignment to create. Use the format &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **parameters** | [**PolicyAssignment**](PolicyAssignment.md)| Parameters for policy assignment. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## policyAssignmentsDelete

> PolicyAssignment policyAssignmentsDelete(scope, policyAssignmentName, apiVersion)

Deletes a policy assignment.

This operation deletes a policy assignment, given its name and the scope it was created in. The scope of a policy assignment is the part of its ID preceding &#39;/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let scope = "scope_example"; // String | The scope of the policy assignment. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
let policyAssignmentName = "policyAssignmentName_example"; // String | The name of the policy assignment to delete.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.policyAssignmentsDelete(scope, policyAssignmentName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the policy assignment. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39; | 
 **policyAssignmentName** | **String**| The name of the policy assignment to delete. | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyAssignmentsDeleteById

> PolicyAssignment policyAssignmentsDeleteById(policyAssignmentId, apiVersion)

Deletes a policy assignment.

This operation deletes the policy with the given ID. Policy assignment IDs have this format: &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. Valid formats for {scope} are: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39; (management group), &#39;/subscriptions/{subscriptionId}&#39; (subscription), &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; (resource group), or &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39; (resource).

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let policyAssignmentId = "policyAssignmentId_example"; // String | The ID of the policy assignment to delete. Use the format '{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.policyAssignmentsDeleteById(policyAssignmentId, apiVersion, (error, data, response) => {
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
 **policyAssignmentId** | **String**| The ID of the policy assignment to delete. Use the format &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyAssignmentsGet

> PolicyAssignment policyAssignmentsGet(scope, policyAssignmentName, apiVersion)

Retrieves a policy assignment.

This operation retrieves a single policy assignment, given its name and the scope it was created at.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let scope = "scope_example"; // String | The scope of the policy assignment. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
let policyAssignmentName = "policyAssignmentName_example"; // String | The name of the policy assignment to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.policyAssignmentsGet(scope, policyAssignmentName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the policy assignment. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39; | 
 **policyAssignmentName** | **String**| The name of the policy assignment to get. | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyAssignmentsGetById

> PolicyAssignment policyAssignmentsGetById(policyAssignmentId, apiVersion)

Retrieves the policy assignment with the given ID.

The operation retrieves the policy assignment with the given ID. Policy assignment IDs have this format: &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39;.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let policyAssignmentId = "policyAssignmentId_example"; // String | The ID of the policy assignment to get. Use the format '{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.policyAssignmentsGetById(policyAssignmentId, apiVersion, (error, data, response) => {
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
 **policyAssignmentId** | **String**| The ID of the policy assignment to get. Use the format &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyAssignmentsList

> PolicyAssignmentListResult policyAssignmentsList(apiVersion, subscriptionId, opts)

Retrieves all policy assignments that apply to a subscription.

This operation retrieves the list of all policy assignments associated with the given subscription that match the optional given $filter. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, the unfiltered list includes all policy assignments associated with the subscription, including those that apply directly or from management groups that contain the given subscription, as well as any applied to objects contained within the subscription. If $filter&#x3D;atScope() is provided, the returned list includes all policy assignments that apply to the subscription, which is everything in the unfiltered list except those applied to objects contained within the subscription. If $filter&#x3D;policyDefinitionId eq &#39;{value}&#39; is provided, the returned list includes all policy assignments of the policy definition whose id is {value}.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. Valid values for $filter are: 'atScope()' or 'policyDefinitionId eq '{value}''. If $filter is not provided, no filtering is performed.
};
apiInstance.policyAssignmentsList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **filter** | **String**| The filter to apply on the operation. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, no filtering is performed. | [optional] 

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyAssignmentsListForResource

> PolicyAssignmentListResult policyAssignmentsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, opts)

Retrieves all policy assignments that apply to a resource.

This operation retrieves the list of all policy assignments associated with the specified resource in the given resource group and subscription that match the optional given $filter. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, the unfiltered list includes all policy assignments associated with the resource, including those that apply directly or from all containing scopes, as well as any applied to resources contained within the resource. If $filter&#x3D;atScope() is provided, the returned list includes all policy assignments that apply to the resource, which is everything in the unfiltered list except those applied to resources contained within the resource. If $filter&#x3D;policyDefinitionId eq &#39;{value}&#39; is provided, the returned list includes all policy assignments of the policy definition whose id is {value} that apply to the resource. Three parameters plus the resource name are used to identify a specific resource. If the resource is not part of a parent resource (the more common case), the parent resource path should not be provided (or provided as &#39;&#39;). For example a web app could be specified as ({resourceProviderNamespace} &#x3D;&#x3D; &#39;Microsoft.Web&#39;, {parentResourcePath} &#x3D;&#x3D; &#39;&#39;, {resourceType} &#x3D;&#x3D; &#39;sites&#39;, {resourceName} &#x3D;&#x3D; &#39;MyWebApp&#39;). If the resource is part of a parent resource, then all parameters should be provided. For example a virtual machine DNS name could be specified as ({resourceProviderNamespace} &#x3D;&#x3D; &#39;Microsoft.Compute&#39;, {parentResourcePath} &#x3D;&#x3D; &#39;virtualMachines/MyVirtualMachine&#39;, {resourceType} &#x3D;&#x3D; &#39;domainNames&#39;, {resourceName} &#x3D;&#x3D; &#39;MyComputerName&#39;). A convenient alternative to providing the namespace and type name separately is to provide both in the {resourceType} parameter, format: ({resourceProviderNamespace} &#x3D;&#x3D; &#39;&#39;, {parentResourcePath} &#x3D;&#x3D; &#39;&#39;, {resourceType} &#x3D;&#x3D; &#39;Microsoft.Web/sites&#39;, {resourceName} &#x3D;&#x3D; &#39;MyWebApp&#39;).

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider. For example, the namespace of a virtual machine is Microsoft.Compute (from Microsoft.Compute/virtualMachines)
let parentResourcePath = "parentResourcePath_example"; // String | The parent resource path. Use empty string if there is none.
let resourceType = "resourceType_example"; // String | The resource type name. For example the type name of a web app is 'sites' (from Microsoft.Web/sites).
let resourceName = "resourceName_example"; // String | The name of the resource.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. Valid values for $filter are: 'atScope()' or 'policyDefinitionId eq '{value}''. If $filter is not provided, no filtering is performed.
};
apiInstance.policyAssignmentsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the resource. | 
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. For example, the namespace of a virtual machine is Microsoft.Compute (from Microsoft.Compute/virtualMachines) | 
 **parentResourcePath** | **String**| The parent resource path. Use empty string if there is none. | 
 **resourceType** | **String**| The resource type name. For example the type name of a web app is &#39;sites&#39; (from Microsoft.Web/sites). | 
 **resourceName** | **String**| The name of the resource. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **filter** | **String**| The filter to apply on the operation. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, no filtering is performed. | [optional] 

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyAssignmentsListForResourceGroup

> PolicyAssignmentListResult policyAssignmentsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts)

Retrieves all policy assignments that apply to a resource group.

This operation retrieves the list of all policy assignments associated with the given resource group in the given subscription that match the optional given $filter. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, the unfiltered list includes all policy assignments associated with the resource group, including those that apply directly or apply from containing scopes, as well as any applied to resources contained within the resource group. If $filter&#x3D;atScope() is provided, the returned list includes all policy assignments that apply to the resource group, which is everything in the unfiltered list except those applied to resources contained within the resource group. If $filter&#x3D;policyDefinitionId eq &#39;{value}&#39; is provided, the returned list includes all policy assignments of the policy definition whose id is {value} that apply to the resource group.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains policy assignments.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. Valid values for $filter are: 'atScope()' or 'policyDefinitionId eq '{value}''. If $filter is not provided, no filtering is performed.
};
apiInstance.policyAssignmentsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains policy assignments. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **filter** | **String**| The filter to apply on the operation. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, no filtering is performed. | [optional] 

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

