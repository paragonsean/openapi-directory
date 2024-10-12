# ResourceManagementClient.DeploymentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploymentsCalculateTemplateHash**](DeploymentsApi.md#deploymentsCalculateTemplateHash) | **POST** /providers/Microsoft.Resources/calculateTemplateHash | 
[**deploymentsCancel**](DeploymentsApi.md#deploymentsCancel) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}/cancel | Cancels a currently running template deployment.
[**deploymentsCancelAtManagementGroupScope**](DeploymentsApi.md#deploymentsCancelAtManagementGroupScope) | **POST** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/cancel | Cancels a currently running template deployment.
[**deploymentsCancelAtScope**](DeploymentsApi.md#deploymentsCancelAtScope) | **POST** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName}/cancel | Cancels a currently running template deployment.
[**deploymentsCancelAtSubscriptionScope**](DeploymentsApi.md#deploymentsCancelAtSubscriptionScope) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/cancel | Cancels a currently running template deployment.
[**deploymentsCancelAtTenantScope**](DeploymentsApi.md#deploymentsCancelAtTenantScope) | **POST** /providers/Microsoft.Resources/deployments/{deploymentName}/cancel | Cancels a currently running template deployment.
[**deploymentsCheckExistence**](DeploymentsApi.md#deploymentsCheckExistence) | **HEAD** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsCheckExistenceAtManagementGroupScope**](DeploymentsApi.md#deploymentsCheckExistenceAtManagementGroupScope) | **HEAD** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsCheckExistenceAtScope**](DeploymentsApi.md#deploymentsCheckExistenceAtScope) | **HEAD** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsCheckExistenceAtSubscriptionScope**](DeploymentsApi.md#deploymentsCheckExistenceAtSubscriptionScope) | **HEAD** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsCheckExistenceAtTenantScope**](DeploymentsApi.md#deploymentsCheckExistenceAtTenantScope) | **HEAD** /providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsCreateOrUpdate**](DeploymentsApi.md#deploymentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} | Deploys resources to a resource group.
[**deploymentsCreateOrUpdateAtManagementGroupScope**](DeploymentsApi.md#deploymentsCreateOrUpdateAtManagementGroupScope) | **PUT** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName} | Deploys resources at management group scope.
[**deploymentsCreateOrUpdateAtScope**](DeploymentsApi.md#deploymentsCreateOrUpdateAtScope) | **PUT** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName} | Deploys resources at a given scope.
[**deploymentsCreateOrUpdateAtSubscriptionScope**](DeploymentsApi.md#deploymentsCreateOrUpdateAtSubscriptionScope) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName} | Deploys resources at subscription scope.
[**deploymentsCreateOrUpdateAtTenantScope**](DeploymentsApi.md#deploymentsCreateOrUpdateAtTenantScope) | **PUT** /providers/Microsoft.Resources/deployments/{deploymentName} | Deploys resources at tenant scope.
[**deploymentsDelete**](DeploymentsApi.md#deploymentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} | Deletes a deployment from the deployment history.
[**deploymentsDeleteAtManagementGroupScope**](DeploymentsApi.md#deploymentsDeleteAtManagementGroupScope) | **DELETE** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName} | Deletes a deployment from the deployment history.
[**deploymentsDeleteAtScope**](DeploymentsApi.md#deploymentsDeleteAtScope) | **DELETE** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName} | Deletes a deployment from the deployment history.
[**deploymentsDeleteAtSubscriptionScope**](DeploymentsApi.md#deploymentsDeleteAtSubscriptionScope) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName} | Deletes a deployment from the deployment history.
[**deploymentsDeleteAtTenantScope**](DeploymentsApi.md#deploymentsDeleteAtTenantScope) | **DELETE** /providers/Microsoft.Resources/deployments/{deploymentName} | Deletes a deployment from the deployment history.
[**deploymentsExportTemplate**](DeploymentsApi.md#deploymentsExportTemplate) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}/exportTemplate | 
[**deploymentsExportTemplateAtManagementGroupScope**](DeploymentsApi.md#deploymentsExportTemplateAtManagementGroupScope) | **POST** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/exportTemplate | 
[**deploymentsExportTemplateAtScope**](DeploymentsApi.md#deploymentsExportTemplateAtScope) | **POST** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName}/exportTemplate | 
[**deploymentsExportTemplateAtSubscriptionScope**](DeploymentsApi.md#deploymentsExportTemplateAtSubscriptionScope) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/exportTemplate | 
[**deploymentsExportTemplateAtTenantScope**](DeploymentsApi.md#deploymentsExportTemplateAtTenantScope) | **POST** /providers/Microsoft.Resources/deployments/{deploymentName}/exportTemplate | 
[**deploymentsGet**](DeploymentsApi.md#deploymentsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsGetAtManagementGroupScope**](DeploymentsApi.md#deploymentsGetAtManagementGroupScope) | **GET** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsGetAtScope**](DeploymentsApi.md#deploymentsGetAtScope) | **GET** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsGetAtSubscriptionScope**](DeploymentsApi.md#deploymentsGetAtSubscriptionScope) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsGetAtTenantScope**](DeploymentsApi.md#deploymentsGetAtTenantScope) | **GET** /providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsListAtManagementGroupScope**](DeploymentsApi.md#deploymentsListAtManagementGroupScope) | **GET** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/ | 
[**deploymentsListAtScope**](DeploymentsApi.md#deploymentsListAtScope) | **GET** /{scope}/providers/Microsoft.Resources/deployments/ | 
[**deploymentsListAtSubscriptionScope**](DeploymentsApi.md#deploymentsListAtSubscriptionScope) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/ | 
[**deploymentsListAtTenantScope**](DeploymentsApi.md#deploymentsListAtTenantScope) | **GET** /providers/Microsoft.Resources/deployments/ | 
[**deploymentsListByResourceGroup**](DeploymentsApi.md#deploymentsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/ | 
[**deploymentsValidate**](DeploymentsApi.md#deploymentsValidate) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}/validate | 
[**deploymentsValidateAtManagementGroupScope**](DeploymentsApi.md#deploymentsValidateAtManagementGroupScope) | **POST** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/validate | 
[**deploymentsValidateAtScope**](DeploymentsApi.md#deploymentsValidateAtScope) | **POST** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName}/validate | 
[**deploymentsValidateAtSubscriptionScope**](DeploymentsApi.md#deploymentsValidateAtSubscriptionScope) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/validate | 
[**deploymentsValidateAtTenantScope**](DeploymentsApi.md#deploymentsValidateAtTenantScope) | **POST** /providers/Microsoft.Resources/deployments/{deploymentName}/validate | 
[**deploymentsWhatIf**](DeploymentsApi.md#deploymentsWhatIf) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}/whatIf | 
[**deploymentsWhatIfAtSubscriptionScope**](DeploymentsApi.md#deploymentsWhatIfAtSubscriptionScope) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/whatIf | 



## deploymentsCalculateTemplateHash

> TemplateHashResult deploymentsCalculateTemplateHash(apiVersion, template)



Calculate the hash of the given template.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let template = {key: null}; // Object | The template provided to calculate hash.
apiInstance.deploymentsCalculateTemplateHash(apiVersion, template, (error, data, response) => {
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
 **template** | **Object**| The template provided to calculate hash. | 

### Return type

[**TemplateHashResult**](TemplateHashResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentsCancel

> deploymentsCancel(resourceGroupName, deploymentName, apiVersion, subscriptionId)

Cancels a currently running template deployment.

You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resource group partially deployed.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.deploymentsCancel(resourceGroupName, deploymentName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsCancelAtManagementGroupScope

> deploymentsCancelAtManagementGroupScope(groupId, deploymentName, apiVersion)

Cancels a currently running template deployment.

You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let groupId = "groupId_example"; // String | The management group ID.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsCancelAtManagementGroupScope(groupId, deploymentName, apiVersion, (error, data, response) => {
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
 **groupId** | **String**| The management group ID. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsCancelAtScope

> deploymentsCancelAtScope(scope, deploymentName, apiVersion)

Cancels a currently running template deployment.

You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let scope = "scope_example"; // String | The resource scope.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsCancelAtScope(scope, deploymentName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The resource scope. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsCancelAtSubscriptionScope

> deploymentsCancelAtSubscriptionScope(deploymentName, apiVersion, subscriptionId)

Cancels a currently running template deployment.

You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.deploymentsCancelAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, (error, data, response) => {
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
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsCancelAtTenantScope

> deploymentsCancelAtTenantScope(deploymentName, apiVersion)

Cancels a currently running template deployment.

You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsCancelAtTenantScope(deploymentName, apiVersion, (error, data, response) => {
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
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsCheckExistence

> deploymentsCheckExistence(resourceGroupName, deploymentName, apiVersion, subscriptionId)



Checks whether the deployment exists.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group with the deployment to check. The name is case insensitive.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.deploymentsCheckExistence(resourceGroupName, deploymentName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group with the deployment to check. The name is case insensitive. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsCheckExistenceAtManagementGroupScope

> deploymentsCheckExistenceAtManagementGroupScope(groupId, deploymentName, apiVersion)



Checks whether the deployment exists.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let groupId = "groupId_example"; // String | The management group ID.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsCheckExistenceAtManagementGroupScope(groupId, deploymentName, apiVersion, (error, data, response) => {
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
 **groupId** | **String**| The management group ID. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsCheckExistenceAtScope

> deploymentsCheckExistenceAtScope(scope, deploymentName, apiVersion)



Checks whether the deployment exists.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let scope = "scope_example"; // String | The resource scope.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsCheckExistenceAtScope(scope, deploymentName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The resource scope. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsCheckExistenceAtSubscriptionScope

> deploymentsCheckExistenceAtSubscriptionScope(deploymentName, apiVersion, subscriptionId)



Checks whether the deployment exists.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.deploymentsCheckExistenceAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, (error, data, response) => {
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
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsCheckExistenceAtTenantScope

> deploymentsCheckExistenceAtTenantScope(deploymentName, apiVersion)



Checks whether the deployment exists.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsCheckExistenceAtTenantScope(deploymentName, apiVersion, (error, data, response) => {
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
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsCreateOrUpdate

> DeploymentExtended deploymentsCreateOrUpdate(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters)

Deploys resources to a resource group.

You can provide the template and parameters directly in the request or link to JSON files.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to deploy the resources to. The name is case insensitive. The resource group must already exist.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ResourceManagementClient.Deployment(); // Deployment | Additional parameters supplied to the operation.
apiInstance.deploymentsCreateOrUpdate(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to deploy the resources to. The name is case insensitive. The resource group must already exist. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**Deployment**](Deployment.md)| Additional parameters supplied to the operation. | 

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentsCreateOrUpdateAtManagementGroupScope

> DeploymentExtended deploymentsCreateOrUpdateAtManagementGroupScope(groupId, deploymentName, apiVersion, parameters)

Deploys resources at management group scope.

You can provide the template and parameters directly in the request or link to JSON files.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let groupId = "groupId_example"; // String | The management group ID.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let parameters = new ResourceManagementClient.ScopedDeployment(); // ScopedDeployment | Additional parameters supplied to the operation.
apiInstance.deploymentsCreateOrUpdateAtManagementGroupScope(groupId, deploymentName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**ScopedDeployment**](ScopedDeployment.md)| Additional parameters supplied to the operation. | 

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentsCreateOrUpdateAtScope

> DeploymentExtended deploymentsCreateOrUpdateAtScope(scope, deploymentName, apiVersion, parameters)

Deploys resources at a given scope.

You can provide the template and parameters directly in the request or link to JSON files.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let scope = "scope_example"; // String | The resource scope.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let parameters = new ResourceManagementClient.Deployment(); // Deployment | Additional parameters supplied to the operation.
apiInstance.deploymentsCreateOrUpdateAtScope(scope, deploymentName, apiVersion, parameters, (error, data, response) => {
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
 **scope** | **String**| The resource scope. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **parameters** | [**Deployment**](Deployment.md)| Additional parameters supplied to the operation. | 

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentsCreateOrUpdateAtSubscriptionScope

> DeploymentExtended deploymentsCreateOrUpdateAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, parameters)

Deploys resources at subscription scope.

You can provide the template and parameters directly in the request or link to JSON files.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ResourceManagementClient.Deployment(); // Deployment | Additional parameters supplied to the operation.
apiInstance.deploymentsCreateOrUpdateAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **parameters** | [**Deployment**](Deployment.md)| Additional parameters supplied to the operation. | 

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentsCreateOrUpdateAtTenantScope

> DeploymentExtended deploymentsCreateOrUpdateAtTenantScope(deploymentName, apiVersion, parameters)

Deploys resources at tenant scope.

You can provide the template and parameters directly in the request or link to JSON files.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let parameters = new ResourceManagementClient.ScopedDeployment(); // ScopedDeployment | Additional parameters supplied to the operation.
apiInstance.deploymentsCreateOrUpdateAtTenantScope(deploymentName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**ScopedDeployment**](ScopedDeployment.md)| Additional parameters supplied to the operation. | 

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentsDelete

> deploymentsDelete(resourceGroupName, deploymentName, apiVersion, subscriptionId)

Deletes a deployment from the deployment history.

A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. Deleting a template deployment does not affect the state of the resource group. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group with the deployment to delete. The name is case insensitive.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.deploymentsDelete(resourceGroupName, deploymentName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group with the deployment to delete. The name is case insensitive. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsDeleteAtManagementGroupScope

> deploymentsDeleteAtManagementGroupScope(groupId, deploymentName, apiVersion)

Deletes a deployment from the deployment history.

A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let groupId = "groupId_example"; // String | The management group ID.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsDeleteAtManagementGroupScope(groupId, deploymentName, apiVersion, (error, data, response) => {
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
 **groupId** | **String**| The management group ID. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsDeleteAtScope

> deploymentsDeleteAtScope(scope, deploymentName, apiVersion)

Deletes a deployment from the deployment history.

A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let scope = "scope_example"; // String | The resource scope.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsDeleteAtScope(scope, deploymentName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The resource scope. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsDeleteAtSubscriptionScope

> deploymentsDeleteAtSubscriptionScope(deploymentName, apiVersion, subscriptionId)

Deletes a deployment from the deployment history.

A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.deploymentsDeleteAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, (error, data, response) => {
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
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsDeleteAtTenantScope

> deploymentsDeleteAtTenantScope(deploymentName, apiVersion)

Deletes a deployment from the deployment history.

A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsDeleteAtTenantScope(deploymentName, apiVersion, (error, data, response) => {
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
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsExportTemplate

> DeploymentExportResult deploymentsExportTemplate(resourceGroupName, deploymentName, apiVersion, subscriptionId)



Exports the template used for specified deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.deploymentsExportTemplate(resourceGroupName, deploymentName, apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**DeploymentExportResult**](DeploymentExportResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsExportTemplateAtManagementGroupScope

> DeploymentExportResult deploymentsExportTemplateAtManagementGroupScope(groupId, deploymentName, apiVersion)



Exports the template used for specified deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let groupId = "groupId_example"; // String | The management group ID.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsExportTemplateAtManagementGroupScope(groupId, deploymentName, apiVersion, (error, data, response) => {
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

### Return type

[**DeploymentExportResult**](DeploymentExportResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsExportTemplateAtScope

> DeploymentExportResult deploymentsExportTemplateAtScope(scope, deploymentName, apiVersion)



Exports the template used for specified deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let scope = "scope_example"; // String | The resource scope.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsExportTemplateAtScope(scope, deploymentName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The resource scope. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**DeploymentExportResult**](DeploymentExportResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsExportTemplateAtSubscriptionScope

> DeploymentExportResult deploymentsExportTemplateAtSubscriptionScope(deploymentName, apiVersion, subscriptionId)



Exports the template used for specified deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.deploymentsExportTemplateAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**DeploymentExportResult**](DeploymentExportResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsExportTemplateAtTenantScope

> DeploymentExportResult deploymentsExportTemplateAtTenantScope(deploymentName, apiVersion)



Exports the template used for specified deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsExportTemplateAtTenantScope(deploymentName, apiVersion, (error, data, response) => {
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

### Return type

[**DeploymentExportResult**](DeploymentExportResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsGet

> DeploymentExtended deploymentsGet(resourceGroupName, deploymentName, apiVersion, subscriptionId)



Gets a deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.deploymentsGet(resourceGroupName, deploymentName, apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsGetAtManagementGroupScope

> DeploymentExtended deploymentsGetAtManagementGroupScope(groupId, deploymentName, apiVersion)



Gets a deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let groupId = "groupId_example"; // String | The management group ID.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsGetAtManagementGroupScope(groupId, deploymentName, apiVersion, (error, data, response) => {
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

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsGetAtScope

> DeploymentExtended deploymentsGetAtScope(scope, deploymentName, apiVersion)



Gets a deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let scope = "scope_example"; // String | The resource scope.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsGetAtScope(scope, deploymentName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The resource scope. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsGetAtSubscriptionScope

> DeploymentExtended deploymentsGetAtSubscriptionScope(deploymentName, apiVersion, subscriptionId)



Gets a deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.deploymentsGetAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsGetAtTenantScope

> DeploymentExtended deploymentsGetAtTenantScope(deploymentName, apiVersion)



Gets a deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.deploymentsGetAtTenantScope(deploymentName, apiVersion, (error, data, response) => {
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

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsListAtManagementGroupScope

> DeploymentListResult deploymentsListAtManagementGroupScope(groupId, apiVersion, opts)



Get all the deployments for a management group.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let groupId = "groupId_example"; // String | The management group ID.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation. For example, you can use $filter=provisioningState eq '{state}'.
  'top': 56 // Number | The number of results to get. If null is passed, returns all deployments.
};
apiInstance.deploymentsListAtManagementGroupScope(groupId, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **filter** | **String**| The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;. | [optional] 
 **top** | **Number**| The number of results to get. If null is passed, returns all deployments. | [optional] 

### Return type

[**DeploymentListResult**](DeploymentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsListAtScope

> DeploymentListResult deploymentsListAtScope(scope, apiVersion, opts)



Get all the deployments at the given scope.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let scope = "scope_example"; // String | The resource scope.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation. For example, you can use $filter=provisioningState eq '{state}'.
  'top': 56 // Number | The number of results to get. If null is passed, returns all deployments.
};
apiInstance.deploymentsListAtScope(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| The resource scope. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **filter** | **String**| The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;. | [optional] 
 **top** | **Number**| The number of results to get. If null is passed, returns all deployments. | [optional] 

### Return type

[**DeploymentListResult**](DeploymentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsListAtSubscriptionScope

> DeploymentListResult deploymentsListAtSubscriptionScope(apiVersion, subscriptionId, opts)



Get all the deployments for a subscription.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation. For example, you can use $filter=provisioningState eq '{state}'.
  'top': 56 // Number | The number of results to get. If null is passed, returns all deployments.
};
apiInstance.deploymentsListAtSubscriptionScope(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **filter** | **String**| The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;. | [optional] 
 **top** | **Number**| The number of results to get. If null is passed, returns all deployments. | [optional] 

### Return type

[**DeploymentListResult**](DeploymentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsListAtTenantScope

> DeploymentListResult deploymentsListAtTenantScope(apiVersion, opts)



Get all the deployments at the tenant scope.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation. For example, you can use $filter=provisioningState eq '{state}'.
  'top': 56 // Number | The number of results to get. If null is passed, returns all deployments.
};
apiInstance.deploymentsListAtTenantScope(apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;. | [optional] 
 **top** | **Number**| The number of results to get. If null is passed, returns all deployments. | [optional] 

### Return type

[**DeploymentListResult**](DeploymentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsListByResourceGroup

> DeploymentListResult deploymentsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts)



Get all the deployments for a resource group.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group with the deployments to get. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation. For example, you can use $filter=provisioningState eq '{state}'.
  'top': 56 // Number | The number of results to get. If null is passed, returns all deployments.
};
apiInstance.deploymentsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group with the deployments to get. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **filter** | **String**| The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;. | [optional] 
 **top** | **Number**| The number of results to get. If null is passed, returns all deployments. | [optional] 

### Return type

[**DeploymentListResult**](DeploymentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsValidate

> DeploymentValidateResult deploymentsValidate(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters)



Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group the template will be deployed to. The name is case insensitive.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ResourceManagementClient.Deployment(); // Deployment | Parameters to validate.
apiInstance.deploymentsValidate(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group the template will be deployed to. The name is case insensitive. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**Deployment**](Deployment.md)| Parameters to validate. | 

### Return type

[**DeploymentValidateResult**](DeploymentValidateResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentsValidateAtManagementGroupScope

> DeploymentValidateResult deploymentsValidateAtManagementGroupScope(groupId, deploymentName, apiVersion, parameters)



Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let groupId = "groupId_example"; // String | The management group ID.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let parameters = new ResourceManagementClient.ScopedDeployment(); // ScopedDeployment | Parameters to validate.
apiInstance.deploymentsValidateAtManagementGroupScope(groupId, deploymentName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**ScopedDeployment**](ScopedDeployment.md)| Parameters to validate. | 

### Return type

[**DeploymentValidateResult**](DeploymentValidateResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentsValidateAtScope

> DeploymentValidateResult deploymentsValidateAtScope(scope, deploymentName, apiVersion, parameters)



Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let scope = "scope_example"; // String | The resource scope.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let parameters = new ResourceManagementClient.Deployment(); // Deployment | Parameters to validate.
apiInstance.deploymentsValidateAtScope(scope, deploymentName, apiVersion, parameters, (error, data, response) => {
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
 **scope** | **String**| The resource scope. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **parameters** | [**Deployment**](Deployment.md)| Parameters to validate. | 

### Return type

[**DeploymentValidateResult**](DeploymentValidateResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentsValidateAtSubscriptionScope

> DeploymentValidateResult deploymentsValidateAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, parameters)



Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ResourceManagementClient.Deployment(); // Deployment | Parameters to validate.
apiInstance.deploymentsValidateAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **parameters** | [**Deployment**](Deployment.md)| Parameters to validate. | 

### Return type

[**DeploymentValidateResult**](DeploymentValidateResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentsValidateAtTenantScope

> DeploymentValidateResult deploymentsValidateAtTenantScope(deploymentName, apiVersion, parameters)



Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let parameters = new ResourceManagementClient.ScopedDeployment(); // ScopedDeployment | Parameters to validate.
apiInstance.deploymentsValidateAtTenantScope(deploymentName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**ScopedDeployment**](ScopedDeployment.md)| Parameters to validate. | 

### Return type

[**DeploymentValidateResult**](DeploymentValidateResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentsWhatIf

> WhatIfOperationResult deploymentsWhatIf(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters)



Returns changes that will be made by the deployment if executed at the scope of the resource group.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group the template will be deployed to. The name is case insensitive.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ResourceManagementClient.DeploymentWhatIf(); // DeploymentWhatIf | Parameters to validate.
apiInstance.deploymentsWhatIf(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group the template will be deployed to. The name is case insensitive. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**DeploymentWhatIf**](DeploymentWhatIf.md)| Parameters to validate. | 

### Return type

[**WhatIfOperationResult**](WhatIfOperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentsWhatIfAtSubscriptionScope

> WhatIfOperationResult deploymentsWhatIfAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, parameters)



Returns changes that will be made by the deployment if executed at the scope of the subscription.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ResourceManagementClient.DeploymentWhatIf(); // DeploymentWhatIf | Parameters to What If.
apiInstance.deploymentsWhatIfAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **parameters** | [**DeploymentWhatIf**](DeploymentWhatIf.md)| Parameters to What If. | 

### Return type

[**WhatIfOperationResult**](WhatIfOperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

