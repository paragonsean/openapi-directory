# ResourceManagementClient.DeploymentOperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploymentOperationsGet**](DeploymentOperationsApi.md#deploymentOperationsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/deployments/{deploymentName}/operations/{operationId} | 
[**deploymentOperationsGetAtManagementGroupScope**](DeploymentOperationsApi.md#deploymentOperationsGetAtManagementGroupScope) | **GET** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations/{operationId} | 
[**deploymentOperationsGetAtSubscriptionScope**](DeploymentOperationsApi.md#deploymentOperationsGetAtSubscriptionScope) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations/{operationId} | 
[**deploymentOperationsList**](DeploymentOperationsApi.md#deploymentOperationsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/deployments/{deploymentName}/operations | 
[**deploymentOperationsListAtManagementGroupScope**](DeploymentOperationsApi.md#deploymentOperationsListAtManagementGroupScope) | **GET** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations | 
[**deploymentOperationsListAtSubscriptionScope**](DeploymentOperationsApi.md#deploymentOperationsListAtSubscriptionScope) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations | 



## deploymentOperationsGet

> DeploymentOperation deploymentOperationsGet(resourceGroupName, deploymentName, operationId, apiVersion, subscriptionId)



Gets a deployments operation.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentOperationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let operationId = "operationId_example"; // String | The ID of the operation to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.deploymentOperationsGet(resourceGroupName, deploymentName, operationId, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **operationId** | **String**| The ID of the operation to get. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**DeploymentOperation**](DeploymentOperation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentOperationsGetAtManagementGroupScope

> DeploymentOperation deploymentOperationsGetAtManagementGroupScope(groupId, deploymentName, operationId, apiVersion)



Gets a deployments operation.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentOperationsApi();
let groupId = "groupId_example"; // String | The management group ID.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let operationId = "operationId_example"; // String | The ID of the operation to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentOperationsGetAtManagementGroupScope(groupId, deploymentName, operationId, apiVersion, (error, data, response) => {
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
 **groupId** | **String**| The management group ID. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **operationId** | **String**| The ID of the operation to get. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**DeploymentOperation**](DeploymentOperation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentOperationsGetAtSubscriptionScope

> DeploymentOperation deploymentOperationsGetAtSubscriptionScope(deploymentName, operationId, apiVersion, subscriptionId)



Gets a deployments operation.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentOperationsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let operationId = "operationId_example"; // String | The ID of the operation to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.deploymentOperationsGetAtSubscriptionScope(deploymentName, operationId, apiVersion, subscriptionId, (error, data, response) => {
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
 **deploymentName** | **String**| The name of the deployment. | 
 **operationId** | **String**| The ID of the operation to get. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**DeploymentOperation**](DeploymentOperation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentOperationsList

> DeploymentOperationsListResult deploymentOperationsList(resourceGroupName, deploymentName, apiVersion, subscriptionId, opts)



Gets all deployments operations for a deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentOperationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'top': 56 // Number | The number of results to return.
};
apiInstance.deploymentOperationsList(resourceGroupName, deploymentName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **top** | **Number**| The number of results to return. | [optional] 

### Return type

[**DeploymentOperationsListResult**](DeploymentOperationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentOperationsListAtManagementGroupScope

> DeploymentOperationsListResult deploymentOperationsListAtManagementGroupScope(groupId, deploymentName, apiVersion, opts)



Gets all deployments operations for a deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentOperationsApi();
let groupId = "groupId_example"; // String | The management group ID.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'top': 56 // Number | The number of results to return.
};
apiInstance.deploymentOperationsListAtManagementGroupScope(groupId, deploymentName, apiVersion, opts, (error, data, response) => {
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
 **groupId** | **String**| The management group ID. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **top** | **Number**| The number of results to return. | [optional] 

### Return type

[**DeploymentOperationsListResult**](DeploymentOperationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentOperationsListAtSubscriptionScope

> DeploymentOperationsListResult deploymentOperationsListAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, opts)



Gets all deployments operations for a deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentOperationsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'top': 56 // Number | The number of results to return.
};
apiInstance.deploymentOperationsListAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **top** | **Number**| The number of results to return. | [optional] 

### Return type

[**DeploymentOperationsListResult**](DeploymentOperationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

