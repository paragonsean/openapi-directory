# AzureMachineLearningWorkspaces.MachineLearningComputesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**machineLearningComputeCreateOrUpdate_0**](MachineLearningComputesApi.md#machineLearningComputeCreateOrUpdate_0) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName} | 
[**machineLearningComputeDelete_0**](MachineLearningComputesApi.md#machineLearningComputeDelete_0) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName} | 
[**machineLearningComputeGet_0**](MachineLearningComputesApi.md#machineLearningComputeGet_0) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName} | 
[**machineLearningComputeListByWorkspace_0**](MachineLearningComputesApi.md#machineLearningComputeListByWorkspace_0) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes | 
[**machineLearningComputeListKeys_0**](MachineLearningComputesApi.md#machineLearningComputeListKeys_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName}/listKeys | 
[**machineLearningComputeListNodes**](MachineLearningComputesApi.md#machineLearningComputeListNodes) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName}/listNodes | 
[**machineLearningComputeUpdate_0**](MachineLearningComputesApi.md#machineLearningComputeUpdate_0) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName} | 



## machineLearningComputeCreateOrUpdate_0

> ComputeResource machineLearningComputeCreateOrUpdate_0(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, parameters)



Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.MachineLearningComputesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let parameters = new AzureMachineLearningWorkspaces.ComputeResource(); // ComputeResource | Payload with Machine Learning compute definition.
apiInstance.machineLearningComputeCreateOrUpdate_0(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, parameters, (error, data, response) => {
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


## machineLearningComputeDelete_0

> machineLearningComputeDelete_0(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, underlyingResourceAction)



Deletes specified Machine Learning compute.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.MachineLearningComputesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let underlyingResourceAction = "underlyingResourceAction_example"; // String | Delete the underlying compute if 'Delete', or detach the underlying compute from workspace if 'Detach'.
apiInstance.machineLearningComputeDelete_0(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, underlyingResourceAction, (error, data, response) => {
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
 **underlyingResourceAction** | **String**| Delete the underlying compute if &#39;Delete&#39;, or detach the underlying compute from workspace if &#39;Detach&#39;. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## machineLearningComputeGet_0

> ComputeResource machineLearningComputeGet_0(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion)



Gets compute definition by its name. Any secrets (storage keys, service credentials, etc) are not returned - use &#39;keys&#39; nested resource to get them.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.MachineLearningComputesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
apiInstance.machineLearningComputeGet_0(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, (error, data, response) => {
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


## machineLearningComputeListByWorkspace_0

> PaginatedComputeResourcesList machineLearningComputeListByWorkspace_0(subscriptionId, resourceGroupName, workspaceName, apiVersion, opts)



Gets computes in specified workspace.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.MachineLearningComputesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let opts = {
  'skiptoken': "skiptoken_example" // String | Continuation token for pagination.
};
apiInstance.machineLearningComputeListByWorkspace_0(subscriptionId, resourceGroupName, workspaceName, apiVersion, opts, (error, data, response) => {
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


## machineLearningComputeListKeys_0

> ComputeSecrets machineLearningComputeListKeys_0(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion)



Gets secrets related to Machine Learning compute (storage keys, service credentials, etc).

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.MachineLearningComputesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
apiInstance.machineLearningComputeListKeys_0(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, (error, data, response) => {
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


## machineLearningComputeListNodes

> AmlComputeNodesInformation machineLearningComputeListNodes(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion)



Get the details (e.g IP address, port etc) of all the compute nodes in the compute.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.MachineLearningComputesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
apiInstance.machineLearningComputeListNodes(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, (error, data, response) => {
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

[**AmlComputeNodesInformation**](AmlComputeNodesInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## machineLearningComputeUpdate_0

> ComputeResource machineLearningComputeUpdate_0(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, parameters)



Updates properties of a compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.MachineLearningComputesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let parameters = new AzureMachineLearningWorkspaces.ClusterUpdateParameters(); // ClusterUpdateParameters | Additional parameters for cluster update.
apiInstance.machineLearningComputeUpdate_0(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**ClusterUpdateParameters**](ClusterUpdateParameters.md)| Additional parameters for cluster update. | 

### Return type

[**ComputeResource**](ComputeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

