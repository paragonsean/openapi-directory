# ResourceManagementClient.PolicyAssignmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policyAssignmentsCreate**](PolicyAssignmentsApi.md#policyAssignmentsCreate) | **PUT** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} | 
[**policyAssignmentsCreateById**](PolicyAssignmentsApi.md#policyAssignmentsCreateById) | **PUT** /{policyAssignmentId} | 
[**policyAssignmentsDelete**](PolicyAssignmentsApi.md#policyAssignmentsDelete) | **DELETE** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} | 
[**policyAssignmentsDeleteById**](PolicyAssignmentsApi.md#policyAssignmentsDeleteById) | **DELETE** /{policyAssignmentId} | 
[**policyAssignmentsGet**](PolicyAssignmentsApi.md#policyAssignmentsGet) | **GET** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} | 
[**policyAssignmentsGetById**](PolicyAssignmentsApi.md#policyAssignmentsGetById) | **GET** /{policyAssignmentId} | 
[**policyAssignmentsList**](PolicyAssignmentsApi.md#policyAssignmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyAssignments | 
[**policyAssignmentsListForResource**](PolicyAssignmentsApi.md#policyAssignmentsListForResource) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}providers/Microsoft.Authorization/policyAssignments | 
[**policyAssignmentsListForResourceGroup**](PolicyAssignmentsApi.md#policyAssignmentsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/policyAssignments | 
[**policyAssignmentsListForScope**](PolicyAssignmentsApi.md#policyAssignmentsListForScope) | **GET** /{scope}/providers/Microsoft.Authorization/policyAssignments | 



## policyAssignmentsCreate

> PolicyAssignment policyAssignmentsCreate(scope, policyAssignmentName, apiVersion, parameters)



Create policy assignment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.PolicyAssignmentsApi();
let scope = "scope_example"; // String | Scope.
let policyAssignmentName = "policyAssignmentName_example"; // String | Policy assignment name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new ResourceManagementClient.PolicyAssignment(); // PolicyAssignment | Policy assignment.
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
 **scope** | **String**| Scope. | 
 **policyAssignmentName** | **String**| Policy assignment name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**PolicyAssignment**](PolicyAssignment.md)| Policy assignment. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## policyAssignmentsCreateById

> PolicyAssignment policyAssignmentsCreateById(policyAssignmentId, apiVersion, parameters)



Create policy assignment by Id.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.PolicyAssignmentsApi();
let policyAssignmentId = "policyAssignmentId_example"; // String | Policy assignment Id
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new ResourceManagementClient.PolicyAssignment(); // PolicyAssignment | Policy assignment.
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
 **policyAssignmentId** | **String**| Policy assignment Id | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**PolicyAssignment**](PolicyAssignment.md)| Policy assignment. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## policyAssignmentsDelete

> PolicyAssignment policyAssignmentsDelete(scope, policyAssignmentName)



Delete policy assignment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.PolicyAssignmentsApi();
let scope = "scope_example"; // String | Scope.
let policyAssignmentName = "policyAssignmentName_example"; // String | Policy assignment name.
apiInstance.policyAssignmentsDelete(scope, policyAssignmentName, (error, data, response) => {
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
 **scope** | **String**| Scope. | 
 **policyAssignmentName** | **String**| Policy assignment name. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyAssignmentsDeleteById

> PolicyAssignment policyAssignmentsDeleteById(policyAssignmentId, apiVersion)



Delete policy assignment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.PolicyAssignmentsApi();
let policyAssignmentId = "policyAssignmentId_example"; // String | Policy assignment Id
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **policyAssignmentId** | **String**| Policy assignment Id | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyAssignmentsGet

> PolicyAssignment policyAssignmentsGet(scope, policyAssignmentName, apiVersion)



Get single policy assignment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.PolicyAssignmentsApi();
let scope = "scope_example"; // String | Scope.
let policyAssignmentName = "policyAssignmentName_example"; // String | Policy assignment name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **scope** | **String**| Scope. | 
 **policyAssignmentName** | **String**| Policy assignment name. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyAssignmentsGetById

> PolicyAssignment policyAssignmentsGetById(policyAssignmentId, apiVersion)



Get single policy assignment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.PolicyAssignmentsApi();
let policyAssignmentId = "policyAssignmentId_example"; // String | Policy assignment Id
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **policyAssignmentId** | **String**| Policy assignment Id | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyAssignmentsList

> PolicyAssignmentListResult policyAssignmentsList(apiVersion, subscriptionId, opts)



Gets policy assignments of the subscription.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.PolicyAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyAssignmentsListForResource

> PolicyAssignmentListResult policyAssignmentsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, opts)



Gets policy assignments of the resource.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.PolicyAssignmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The name of the resource provider.
let parentResourcePath = "parentResourcePath_example"; // String | The parent resource path.
let resourceType = "resourceType_example"; // String | The resource type.
let resourceName = "resourceName_example"; // String | The resource name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceProviderNamespace** | **String**| The name of the resource provider. | 
 **parentResourcePath** | **String**| The parent resource path. | 
 **resourceType** | **String**| The resource type. | 
 **resourceName** | **String**| The resource name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyAssignmentsListForResourceGroup

> PolicyAssignmentListResult policyAssignmentsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts)



Gets policy assignments of the resource group.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.PolicyAssignmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **resourceGroupName** | **String**| Resource group name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyAssignmentsListForScope

> PolicyAssignmentListResult policyAssignmentsListForScope(scope, apiVersion, opts)



Gets policy assignments of the scope.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.PolicyAssignmentsApi();
let scope = "scope_example"; // String | Scope.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.policyAssignmentsListForScope(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| Scope. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

