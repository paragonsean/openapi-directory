# AzureMachineLearningWorkspaces.WorkspacesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspacesCreateOrUpdate**](WorkspacesApi.md#workspacesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName} | 
[**workspacesDelete**](WorkspacesApi.md#workspacesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName} | 
[**workspacesGet**](WorkspacesApi.md#workspacesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName} | 
[**workspacesListByResourceGroup**](WorkspacesApi.md#workspacesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces | 
[**workspacesListBySubscription**](WorkspacesApi.md#workspacesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/workspaces | 
[**workspacesListKeys**](WorkspacesApi.md#workspacesListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/listKeys | 
[**workspacesResyncKeys**](WorkspacesApi.md#workspacesResyncKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/resyncKeys | 
[**workspacesUpdate**](WorkspacesApi.md#workspacesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName} | 



## workspacesCreateOrUpdate

> Workspace workspacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, workspaceName, parameters)



Creates or updates a workspace with the specified parameters.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let parameters = new AzureMachineLearningWorkspaces.Workspace(); // Workspace | The parameters for creating or updating a machine learning workspace.
apiInstance.workspacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, workspaceName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **workspaceName** | **String**| Name of Azure Machine Learning workspace. | 
 **parameters** | [**Workspace**](Workspace.md)| The parameters for creating or updating a machine learning workspace. | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspacesDelete

> workspacesDelete(apiVersion, subscriptionId, resourceGroupName, workspaceName)



Deletes a machine learning workspace.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
apiInstance.workspacesDelete(apiVersion, subscriptionId, resourceGroupName, workspaceName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **workspaceName** | **String**| Name of Azure Machine Learning workspace. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesGet

> Workspace workspacesGet(apiVersion, subscriptionId, resourceGroupName, workspaceName)



Gets the properties of the specified machine learning workspace.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
apiInstance.workspacesGet(apiVersion, subscriptionId, resourceGroupName, workspaceName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **workspaceName** | **String**| Name of Azure Machine Learning workspace. | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesListByResourceGroup

> WorkspaceListResult workspacesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, opts)



Lists all the available machine learning workspaces under the specified resource group.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let opts = {
  'skiptoken': "skiptoken_example" // String | Continuation token for pagination.
};
apiInstance.workspacesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **skiptoken** | **String**| Continuation token for pagination. | [optional] 

### Return type

[**WorkspaceListResult**](WorkspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesListBySubscription

> WorkspaceListResult workspacesListBySubscription(apiVersion, subscriptionId, opts)



Lists all the available machine learning workspaces under the specified subscription.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let opts = {
  'skiptoken': "skiptoken_example" // String | Continuation token for pagination.
};
apiInstance.workspacesListBySubscription(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **skiptoken** | **String**| Continuation token for pagination. | [optional] 

### Return type

[**WorkspaceListResult**](WorkspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesListKeys

> ListWorkspaceKeysResult workspacesListKeys(apiVersion, subscriptionId, resourceGroupName, workspaceName)



Lists all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
apiInstance.workspacesListKeys(apiVersion, subscriptionId, resourceGroupName, workspaceName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **workspaceName** | **String**| Name of Azure Machine Learning workspace. | 

### Return type

[**ListWorkspaceKeysResult**](ListWorkspaceKeysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesResyncKeys

> workspacesResyncKeys(apiVersion, subscriptionId, resourceGroupName, workspaceName)



Resync all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
apiInstance.workspacesResyncKeys(apiVersion, subscriptionId, resourceGroupName, workspaceName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **workspaceName** | **String**| Name of Azure Machine Learning workspace. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesUpdate

> Workspace workspacesUpdate(apiVersion, subscriptionId, resourceGroupName, workspaceName, parameters)



Updates a machine learning workspace with the specified parameters.

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
let workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
let parameters = new AzureMachineLearningWorkspaces.WorkspaceUpdateParameters(); // WorkspaceUpdateParameters | The parameters for updating a machine learning workspace.
apiInstance.workspacesUpdate(apiVersion, subscriptionId, resourceGroupName, workspaceName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 
 **subscriptionId** | **String**| Azure subscription identifier. | 
 **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | 
 **workspaceName** | **String**| Name of Azure Machine Learning workspace. | 
 **parameters** | [**WorkspaceUpdateParameters**](WorkspaceUpdateParameters.md)| The parameters for updating a machine learning workspace. | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

