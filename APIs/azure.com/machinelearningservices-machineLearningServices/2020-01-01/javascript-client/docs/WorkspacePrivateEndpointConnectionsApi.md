# AzureMachineLearningWorkspaces.WorkspacePrivateEndpointConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateEndpointConnectionsDelete**](WorkspacePrivateEndpointConnectionsApi.md#privateEndpointConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/privateEndpointConnections/{privateEndpointConnectionName} | 
[**privateEndpointConnectionsGet**](WorkspacePrivateEndpointConnectionsApi.md#privateEndpointConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/privateEndpointConnections/{privateEndpointConnectionName} | 
[**privateEndpointConnectionsPut**](WorkspacePrivateEndpointConnectionsApi.md#privateEndpointConnectionsPut) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/privateEndpointConnections/{privateEndpointConnectionName} | 



## privateEndpointConnectionsDelete

> privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, workspaceName, privateEndpointConnectionName, apiVersion)



Deletes the specified private endpoint connection associated with the workspace.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.WorkspacePrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection associated with the workspace
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
apiInstance.privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, workspaceName, privateEndpointConnectionName, apiVersion, (error, data, response) => {
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
 **privateEndpointConnectionName** | **String**| The name of the private endpoint connection associated with the workspace | 
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateEndpointConnectionsGet

> PrivateEndpointConnection privateEndpointConnectionsGet(subscriptionId, resourceGroupName, workspaceName, privateEndpointConnectionName, apiVersion)



Gets the specified private endpoint connection associated with the workspace.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.WorkspacePrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection associated with the workspace
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
apiInstance.privateEndpointConnectionsGet(subscriptionId, resourceGroupName, workspaceName, privateEndpointConnectionName, apiVersion, (error, data, response) => {
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
 **privateEndpointConnectionName** | **String**| The name of the private endpoint connection associated with the workspace | 
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateEndpointConnectionsPut

> PrivateEndpointConnection privateEndpointConnectionsPut(subscriptionId, resourceGroupName, workspaceName, privateEndpointConnectionName, apiVersion, properties)



Update the state of specified private endpoint connection associated with the workspace.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.WorkspacePrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection associated with the workspace
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let properties = new AzureMachineLearningWorkspaces.PrivateEndpointConnection(); // PrivateEndpointConnection | The private endpoint connection properties.
apiInstance.privateEndpointConnectionsPut(subscriptionId, resourceGroupName, workspaceName, privateEndpointConnectionName, apiVersion, properties, (error, data, response) => {
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
 **privateEndpointConnectionName** | **String**| The name of the private endpoint connection associated with the workspace | 
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 
 **properties** | [**PrivateEndpointConnection**](PrivateEndpointConnection.md)| The private endpoint connection properties. | 

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

