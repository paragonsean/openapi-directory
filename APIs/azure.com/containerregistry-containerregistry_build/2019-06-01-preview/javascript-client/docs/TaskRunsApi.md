# ContainerRegistryManagementClient.TaskRunsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taskRunsCreate**](TaskRunsApi.md#taskRunsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/taskRuns/{taskRunName} | 
[**taskRunsDelete**](TaskRunsApi.md#taskRunsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/taskRuns/{taskRunName} | 
[**taskRunsGet**](TaskRunsApi.md#taskRunsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/taskRuns/{taskRunName} | 
[**taskRunsList**](TaskRunsApi.md#taskRunsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/taskRuns | 
[**taskRunsUpdate**](TaskRunsApi.md#taskRunsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/taskRuns/{taskRunName} | 



## taskRunsCreate

> TaskRun taskRunsCreate(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName, taskRun)



Creates a task run for a container registry with the specified parameters.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.TaskRunsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let taskRunName = "taskRunName_example"; // String | The name of task run.
let taskRun = new ContainerRegistryManagementClient.TaskRun(); // TaskRun | The parameters of a run that needs to scheduled.
apiInstance.taskRunsCreate(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName, taskRun, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **registryName** | **String**| The name of the container registry. | 
 **apiVersion** | **String**| The client API version. | 
 **taskRunName** | **String**| The name of task run. | 
 **taskRun** | [**TaskRun**](TaskRun.md)| The parameters of a run that needs to scheduled. | 

### Return type

[**TaskRun**](TaskRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## taskRunsDelete

> taskRunsDelete(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName)



Deletes a specified task run resource.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.TaskRunsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let taskRunName = "taskRunName_example"; // String | The task run name.
apiInstance.taskRunsDelete(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **registryName** | **String**| The name of the container registry. | 
 **apiVersion** | **String**| The client API version. | 
 **taskRunName** | **String**| The task run name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskRunsGet

> TaskRun taskRunsGet(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName)



Gets the detailed information for a given task run.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.TaskRunsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let taskRunName = "taskRunName_example"; // String | The run request name.
apiInstance.taskRunsGet(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **registryName** | **String**| The name of the container registry. | 
 **apiVersion** | **String**| The client API version. | 
 **taskRunName** | **String**| The run request name. | 

### Return type

[**TaskRun**](TaskRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskRunsList

> TaskRunListResult taskRunsList(subscriptionId, resourceGroupName, registryName, apiVersion)



Lists all the task runs for a specified container registry.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.TaskRunsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.taskRunsList(subscriptionId, resourceGroupName, registryName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **registryName** | **String**| The name of the container registry. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**TaskRunListResult**](TaskRunListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskRunsUpdate

> TaskRun taskRunsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName, updateParameters)



Updates a task run with the specified parameters.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.TaskRunsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let taskRunName = "taskRunName_example"; // String | The task run name.
let updateParameters = new ContainerRegistryManagementClient.TaskRunUpdateParameters(); // TaskRunUpdateParameters | The parameters for updating a task run.
apiInstance.taskRunsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName, updateParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **registryName** | **String**| The name of the container registry. | 
 **apiVersion** | **String**| The client API version. | 
 **taskRunName** | **String**| The task run name. | 
 **updateParameters** | [**TaskRunUpdateParameters**](TaskRunUpdateParameters.md)| The parameters for updating a task run. | 

### Return type

[**TaskRun**](TaskRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

