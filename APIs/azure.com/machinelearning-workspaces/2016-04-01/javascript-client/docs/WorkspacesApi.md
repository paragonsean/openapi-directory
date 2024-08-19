# MachineLearningWorkspacesManagementClient.WorkspacesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspacesCreateOrUpdate**](WorkspacesApi.md#workspacesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/workspaces/{workspaceName} | 
[**workspacesDelete**](WorkspacesApi.md#workspacesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/workspaces/{workspaceName} | 
[**workspacesGet**](WorkspacesApi.md#workspacesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/workspaces/{workspaceName} | 
[**workspacesList**](WorkspacesApi.md#workspacesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearning/workspaces | 
[**workspacesListByResourceGroup**](WorkspacesApi.md#workspacesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/workspaces | 
[**workspacesListWorkspaceKeys**](WorkspacesApi.md#workspacesListWorkspaceKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/workspaces/{workspaceName}/listWorkspaceKeys | 
[**workspacesResyncStorageKeys**](WorkspacesApi.md#workspacesResyncStorageKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/workspaces/{workspaceName}/resyncStorageKeys | 
[**workspacesUpdate**](WorkspacesApi.md#workspacesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/workspaces/{workspaceName} | 



## workspacesCreateOrUpdate

> Workspace workspacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, workspaceName, parameters)



Creates or updates a workspace with the specified parameters.

### Example

```javascript
import MachineLearningWorkspacesManagementClient from 'machine_learning_workspaces_management_client';
let defaultClient = MachineLearningWorkspacesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MachineLearningWorkspacesManagementClient.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning workspace belongs.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning workspace.
let parameters = new MachineLearningWorkspacesManagementClient.Workspace(); // Workspace | The parameters for creating or updating a machine learning workspace.
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning workspace belongs. | 
 **workspaceName** | **String**| The name of the machine learning workspace. | 
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
import MachineLearningWorkspacesManagementClient from 'machine_learning_workspaces_management_client';
let defaultClient = MachineLearningWorkspacesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MachineLearningWorkspacesManagementClient.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning workspace belongs.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning workspace.
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning workspace belongs. | 
 **workspaceName** | **String**| The name of the machine learning workspace. | 

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
import MachineLearningWorkspacesManagementClient from 'machine_learning_workspaces_management_client';
let defaultClient = MachineLearningWorkspacesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MachineLearningWorkspacesManagementClient.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning workspace belongs.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning workspace.
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning workspace belongs. | 
 **workspaceName** | **String**| The name of the machine learning workspace. | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesList

> WorkspaceListResult workspacesList(apiVersion, subscriptionId)



Lists all the available machine learning workspaces under the specified subscription.

### Example

```javascript
import MachineLearningWorkspacesManagementClient from 'machine_learning_workspaces_management_client';
let defaultClient = MachineLearningWorkspacesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MachineLearningWorkspacesManagementClient.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
apiInstance.workspacesList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 

### Return type

[**WorkspaceListResult**](WorkspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesListByResourceGroup

> WorkspaceListResult workspacesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Lists all the available machine learning workspaces under the specified resource group.

### Example

```javascript
import MachineLearningWorkspacesManagementClient from 'machine_learning_workspaces_management_client';
let defaultClient = MachineLearningWorkspacesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MachineLearningWorkspacesManagementClient.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning workspace belongs.
apiInstance.workspacesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning workspace belongs. | 

### Return type

[**WorkspaceListResult**](WorkspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesListWorkspaceKeys

> WorkspaceKeysResponse workspacesListWorkspaceKeys(apiVersion, subscriptionId, workspaceName, resourceGroupName)



List the authorization keys associated with this workspace.

### Example

```javascript
import MachineLearningWorkspacesManagementClient from 'machine_learning_workspaces_management_client';
let defaultClient = MachineLearningWorkspacesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MachineLearningWorkspacesManagementClient.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning workspace.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning workspace belongs.
apiInstance.workspacesListWorkspaceKeys(apiVersion, subscriptionId, workspaceName, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **workspaceName** | **String**| The name of the machine learning workspace. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning workspace belongs. | 

### Return type

[**WorkspaceKeysResponse**](WorkspaceKeysResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesResyncStorageKeys

> workspacesResyncStorageKeys(apiVersion, subscriptionId, workspaceName, resourceGroupName)



Resync storage keys associated with this workspace.

### Example

```javascript
import MachineLearningWorkspacesManagementClient from 'machine_learning_workspaces_management_client';
let defaultClient = MachineLearningWorkspacesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MachineLearningWorkspacesManagementClient.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning workspace.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning workspace belongs.
apiInstance.workspacesResyncStorageKeys(apiVersion, subscriptionId, workspaceName, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **workspaceName** | **String**| The name of the machine learning workspace. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning workspace belongs. | 

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
import MachineLearningWorkspacesManagementClient from 'machine_learning_workspaces_management_client';
let defaultClient = MachineLearningWorkspacesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MachineLearningWorkspacesManagementClient.WorkspacesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning workspace belongs.
let workspaceName = "workspaceName_example"; // String | The name of the machine learning workspace.
let parameters = new MachineLearningWorkspacesManagementClient.WorkspaceUpdateParameters(); // WorkspaceUpdateParameters | The parameters for updating a machine learning workspace.
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning workspace belongs. | 
 **workspaceName** | **String**| The name of the machine learning workspace. | 
 **parameters** | [**WorkspaceUpdateParameters**](WorkspaceUpdateParameters.md)| The parameters for updating a machine learning workspace. | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

