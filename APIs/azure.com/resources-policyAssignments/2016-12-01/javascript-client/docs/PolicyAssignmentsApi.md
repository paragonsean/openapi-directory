# PolicyClient.PolicyAssignmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policyAssignmentsCreate**](PolicyAssignmentsApi.md#policyAssignmentsCreate) | **PUT** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} | Creates a policy assignment.
[**policyAssignmentsCreateById**](PolicyAssignmentsApi.md#policyAssignmentsCreateById) | **PUT** /{policyAssignmentId} | Creates a policy assignment by ID.
[**policyAssignmentsDelete**](PolicyAssignmentsApi.md#policyAssignmentsDelete) | **DELETE** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} | 
[**policyAssignmentsDeleteById**](PolicyAssignmentsApi.md#policyAssignmentsDeleteById) | **DELETE** /{policyAssignmentId} | Deletes a policy assignment by ID.
[**policyAssignmentsGet**](PolicyAssignmentsApi.md#policyAssignmentsGet) | **GET** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} | 
[**policyAssignmentsGetById**](PolicyAssignmentsApi.md#policyAssignmentsGetById) | **GET** /{policyAssignmentId} | Gets a policy assignment by ID.
[**policyAssignmentsList**](PolicyAssignmentsApi.md#policyAssignmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyAssignments | 
[**policyAssignmentsListForResource**](PolicyAssignmentsApi.md#policyAssignmentsListForResource) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/policyAssignments | 
[**policyAssignmentsListForResourceGroup**](PolicyAssignmentsApi.md#policyAssignmentsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/policyAssignments | 



## policyAssignmentsCreate

> PolicyAssignment policyAssignmentsCreate(scope, policyAssignmentName, apiVersion, parameters)

Creates a policy assignment.

Policy assignments are inherited by child resources. For example, when you apply a policy to a resource group that policy is assigned to all resources in the group.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let scope = "scope_example"; // String | The scope of the policy assignment.
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
 **scope** | **String**| The scope of the policy assignment. | 
 **policyAssignmentName** | **String**| The name of the policy assignment. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **parameters** | [**PolicyAssignment**](PolicyAssignment.md)| Parameters for the policy assignment. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## policyAssignmentsCreateById

> PolicyAssignment policyAssignmentsCreateById(policyAssignmentId, apiVersion, parameters)

Creates a policy assignment by ID.

Policy assignments are inherited by child resources. For example, when you apply a policy to a resource group that policy is assigned to all resources in the group. When providing a scope for the assignment, use &#39;/subscriptions/{subscription-id}/&#39; for subscriptions, &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}&#39; for resource groups, and &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}&#39; for resources.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let policyAssignmentId = "policyAssignmentId_example"; // String | The ID of the policy assignment to create. Use the format '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}'.
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
 **policyAssignmentId** | **String**| The ID of the policy assignment to create. Use the format &#39;/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}&#39;. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **parameters** | [**PolicyAssignment**](PolicyAssignment.md)| Parameters for policy assignment. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## policyAssignmentsDelete

> PolicyAssignment policyAssignmentsDelete(scope, policyAssignmentName, apiVersion)



Deletes a policy assignment.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let scope = "scope_example"; // String | The scope of the policy assignment.
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
 **scope** | **String**| The scope of the policy assignment. | 
 **policyAssignmentName** | **String**| The name of the policy assignment to delete. | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policyAssignmentsDeleteById

> PolicyAssignment policyAssignmentsDeleteById(policyAssignmentId, apiVersion)

Deletes a policy assignment by ID.

When providing a scope for the assignment, use &#39;/subscriptions/{subscription-id}/&#39; for subscriptions, &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}&#39; for resource groups, and &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}&#39; for resources.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let policyAssignmentId = "policyAssignmentId_example"; // String | The ID of the policy assignment to delete. Use the format '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}'.
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
 **policyAssignmentId** | **String**| The ID of the policy assignment to delete. Use the format &#39;/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}&#39;. | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policyAssignmentsGet

> PolicyAssignment policyAssignmentsGet(scope, policyAssignmentName, apiVersion)



Gets a policy assignment.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let scope = "scope_example"; // String | The scope of the policy assignment.
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
 **scope** | **String**| The scope of the policy assignment. | 
 **policyAssignmentName** | **String**| The name of the policy assignment to get. | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policyAssignmentsGetById

> PolicyAssignment policyAssignmentsGetById(policyAssignmentId, apiVersion)

Gets a policy assignment by ID.

When providing a scope for the assignment, use &#39;/subscriptions/{subscription-id}/&#39; for subscriptions, &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}&#39; for resource groups, and &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}&#39; for resources.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let policyAssignmentId = "policyAssignmentId_example"; // String | The ID of the policy assignment to get. Use the format '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}'.
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
 **policyAssignmentId** | **String**| The ID of the policy assignment to get. Use the format &#39;/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}&#39;. | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policyAssignmentsList

> PolicyAssignmentListResult policyAssignmentsList(apiVersion, subscriptionId, opts)



Gets all the policy assignments for a subscription.

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
  'filter': "filter_example" // String | The filter to apply on the operation.
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
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policyAssignmentsListForResource

> PolicyAssignmentListResult policyAssignmentsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, opts)



Gets policy assignments for a resource.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyAssignmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource. The name is case insensitive.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
let parentResourcePath = "parentResourcePath_example"; // String | The parent resource path.
let resourceType = "resourceType_example"; // String | The resource type.
let resourceName = "resourceName_example"; // String | The name of the resource with policy assignments.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
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
 **resourceGroupName** | **String**| The name of the resource group containing the resource. The name is case insensitive. | 
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **parentResourcePath** | **String**| The parent resource path. | 
 **resourceType** | **String**| The resource type. | 
 **resourceName** | **String**| The name of the resource with policy assignments. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policyAssignmentsListForResourceGroup

> PolicyAssignmentListResult policyAssignmentsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts)



Gets policy assignments for the resource group.

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
  'filter': "filter_example" // String | The filter to apply on the operation.
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
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

