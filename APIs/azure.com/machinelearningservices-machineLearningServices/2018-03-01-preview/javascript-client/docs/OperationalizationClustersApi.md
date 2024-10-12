# AzureMachineLearningWorkspaces.OperationalizationClustersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**machineLearningComputeCreateOrUpdate**](OperationalizationClustersApi.md#machineLearningComputeCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName} | 
[**machineLearningComputeDelete**](OperationalizationClustersApi.md#machineLearningComputeDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName} | 
[**machineLearningComputeGet**](OperationalizationClustersApi.md#machineLearningComputeGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName} | 
[**machineLearningComputeListByWorkspace**](OperationalizationClustersApi.md#machineLearningComputeListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes | 
[**machineLearningComputeListKeys**](OperationalizationClustersApi.md#machineLearningComputeListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName}/listKeys | 
[**machineLearningComputeSystemUpdate**](OperationalizationClustersApi.md#machineLearningComputeSystemUpdate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName} | 



## machineLearningComputeCreateOrUpdate

> ComputeResource machineLearningComputeCreateOrUpdate(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, parameters)



Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.OperationalizationClustersApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let parameters = new AzureMachineLearningWorkspaces.ComputeResource(); // ComputeResource | Payload with Machine Learning compute definition.
apiInstance.machineLearningComputeCreateOrUpdate(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **workspaceName** | **String**| Name of Azure Machine Learning workspace. | 
 **computeName** | **String**| Name of the Azure Machine Learning compute. | 
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 
 **parameters** | [**ComputeResource**](ComputeResource.md)| Payload with Machine Learning compute definition. | 

### Return type

[**ComputeResource**](ComputeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## machineLearningComputeDelete

> machineLearningComputeDelete(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion)



Deletes specified Machine Learning compute.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.OperationalizationClustersApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
apiInstance.machineLearningComputeDelete(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **workspaceName** | **String**| Name of Azure Machine Learning workspace. | 
 **computeName** | **String**| Name of the Azure Machine Learning compute. | 
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## machineLearningComputeGet

> ComputeResource machineLearningComputeGet(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion)



Gets compute definition by its name. Any secrets (storage keys, service credentials, etc) are not returned - use &#39;keys&#39; nested resource to get them.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.OperationalizationClustersApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
apiInstance.machineLearningComputeGet(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **workspaceName** | **String**| Name of Azure Machine Learning workspace. | 
 **computeName** | **String**| Name of the Azure Machine Learning compute. | 
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 

### Return type

[**ComputeResource**](ComputeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## machineLearningComputeListByWorkspace

> PaginatedComputeResourcesList machineLearningComputeListByWorkspace(subscriptionId, resourceGroupName, workspaceName, apiVersion, opts)



Gets computes in specified workspace.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.OperationalizationClustersApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let opts = {
  'skiptoken': "skiptoken_example" // String | Continuation token for pagination.
};
apiInstance.machineLearningComputeListByWorkspace(subscriptionId, resourceGroupName, workspaceName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **workspaceName** | **String**| Name of Azure Machine Learning workspace. | 
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 
 **skiptoken** | **String**| Continuation token for pagination. | [optional] 

### Return type

[**PaginatedComputeResourcesList**](PaginatedComputeResourcesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## machineLearningComputeListKeys

> ComputeSecrets machineLearningComputeListKeys(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion)



Gets secrets related to Machine Learning compute (storage keys, service credentials, etc).

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.OperationalizationClustersApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
apiInstance.machineLearningComputeListKeys(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **workspaceName** | **String**| Name of Azure Machine Learning workspace. | 
 **computeName** | **String**| Name of the Azure Machine Learning compute. | 
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 

### Return type

[**ComputeSecrets**](ComputeSecrets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## machineLearningComputeSystemUpdate

> machineLearningComputeSystemUpdate(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion)



System Update On Machine Learning compute.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.OperationalizationClustersApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
apiInstance.machineLearningComputeSystemUpdate(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **workspaceName** | **String**| Name of Azure Machine Learning workspace. | 
 **computeName** | **String**| Name of the Azure Machine Learning compute. | 
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

