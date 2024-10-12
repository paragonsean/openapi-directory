# ResourceManagementClient.DeploymentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploymentsCalculateTemplateHash**](DeploymentsApi.md#deploymentsCalculateTemplateHash) | **POST** /providers/Microsoft.Resources/calculateTemplateHash | 
[**deploymentsCancel**](DeploymentsApi.md#deploymentsCancel) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}/cancel | 
[**deploymentsCheckExistence**](DeploymentsApi.md#deploymentsCheckExistence) | **HEAD** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsCreateOrUpdate**](DeploymentsApi.md#deploymentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsDelete**](DeploymentsApi.md#deploymentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsGet**](DeploymentsApi.md#deploymentsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} | 
[**deploymentsList**](DeploymentsApi.md#deploymentsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/ | 
[**deploymentsValidate**](DeploymentsApi.md#deploymentsValidate) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}/validate | 



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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **apiVersion** | **String**| Client Api Version. | 
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



Cancel a currently running template deployment.

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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deploymentsCheckExistence

> deploymentsCheckExistence(resourceGroupName, deploymentName, apiVersion, subscriptionId)



Checks whether deployment exists.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to check. The name is case insensitive.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **resourceGroupName** | **String**| The name of the resource group to check. The name is case insensitive. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deploymentsCreateOrUpdate

> DeploymentExtended deploymentsCreateOrUpdate(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters)



Create a named template deployment using a template.

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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**Deployment**](Deployment.md)| Additional parameters supplied to the operation. | 

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentsDelete

> deploymentsDelete(resourceGroupName, deploymentName, apiVersion, subscriptionId)



Begin deleting deployment.To determine whether the operation has finished processing the request, call GetLongRunningOperationStatus.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let deploymentName = "deploymentName_example"; // String | The name of the deployment to be deleted.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **deploymentName** | **String**| The name of the deployment to be deleted. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deploymentsGet

> DeploymentExtended deploymentsGet(resourceGroupName, deploymentName, apiVersion, subscriptionId)



Get a deployment.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let deploymentName = "deploymentName_example"; // String | The name of the deployment.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsList

> DeploymentListResult deploymentsList(resourceGroupName, apiVersion, subscriptionId, opts)



Get a list of deployments.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.DeploymentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to filter by. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56 // Number | Query parameters. If null is passed returns all deployments.
};
apiInstance.deploymentsList(resourceGroupName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to filter by. The name is case insensitive. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**| Query parameters. If null is passed returns all deployments. | [optional] 

### Return type

[**DeploymentListResult**](DeploymentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentsValidate

> DeploymentValidateResult deploymentsValidate(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters)



Validate a deployment template.

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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ResourceManagementClient.Deployment(); // Deployment | Deployment to validate.
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **deploymentName** | **String**| The name of the deployment. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**Deployment**](Deployment.md)| Deployment to validate. | 

### Return type

[**DeploymentValidateResult**](DeploymentValidateResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

