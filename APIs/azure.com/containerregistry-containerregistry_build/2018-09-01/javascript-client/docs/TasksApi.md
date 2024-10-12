# ContainerRegistryManagementClient.TasksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasksCreate**](TasksApi.md#tasksCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName} | 
[**tasksDelete**](TasksApi.md#tasksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName} | 
[**tasksGet**](TasksApi.md#tasksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName} | 
[**tasksGetDetails**](TasksApi.md#tasksGetDetails) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}/listDetails | 
[**tasksList**](TasksApi.md#tasksList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks | 
[**tasksUpdate**](TasksApi.md#tasksUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName} | 



## tasksCreate

> Task tasksCreate(subscriptionId, resourceGroupName, registryName, apiVersion, taskName, taskCreateParameters)



Creates a task for a container registry with the specified parameters.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.TasksApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let taskName = "taskName_example"; // String | The name of the container registry task.
let taskCreateParameters = new ContainerRegistryManagementClient.Task(); // Task | The parameters for creating a task.
apiInstance.tasksCreate(subscriptionId, resourceGroupName, registryName, apiVersion, taskName, taskCreateParameters, (error, data, response) => {
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
 **taskName** | **String**| The name of the container registry task. | 
 **taskCreateParameters** | [**Task**](Task.md)| The parameters for creating a task. | 

### Return type

[**Task**](Task.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tasksDelete

> tasksDelete(subscriptionId, resourceGroupName, registryName, apiVersion, taskName)



Deletes a specified task.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.TasksApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let taskName = "taskName_example"; // String | The name of the container registry task.
apiInstance.tasksDelete(subscriptionId, resourceGroupName, registryName, apiVersion, taskName, (error, data, response) => {
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
 **taskName** | **String**| The name of the container registry task. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## tasksGet

> Task tasksGet(subscriptionId, resourceGroupName, registryName, apiVersion, taskName)



Get the properties of a specified task.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.TasksApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let taskName = "taskName_example"; // String | The name of the container registry task.
apiInstance.tasksGet(subscriptionId, resourceGroupName, registryName, apiVersion, taskName, (error, data, response) => {
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
 **taskName** | **String**| The name of the container registry task. | 

### Return type

[**Task**](Task.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksGetDetails

> Task tasksGetDetails(subscriptionId, resourceGroupName, registryName, apiVersion, taskName)



Returns a task with extended information that includes all secrets.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.TasksApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let taskName = "taskName_example"; // String | The name of the container registry task.
apiInstance.tasksGetDetails(subscriptionId, resourceGroupName, registryName, apiVersion, taskName, (error, data, response) => {
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
 **taskName** | **String**| The name of the container registry task. | 

### Return type

[**Task**](Task.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksList

> TaskListResult tasksList(subscriptionId, resourceGroupName, registryName, apiVersion)



Lists all the tasks for a specified container registry.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.TasksApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.tasksList(subscriptionId, resourceGroupName, registryName, apiVersion, (error, data, response) => {
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

[**TaskListResult**](TaskListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksUpdate

> Task tasksUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, taskName, taskUpdateParameters)



Updates a task with the specified parameters.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.TasksApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let taskName = "taskName_example"; // String | The name of the container registry task.
let taskUpdateParameters = new ContainerRegistryManagementClient.TaskUpdateParameters(); // TaskUpdateParameters | The parameters for updating a task.
apiInstance.tasksUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, taskName, taskUpdateParameters, (error, data, response) => {
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
 **taskName** | **String**| The name of the container registry task. | 
 **taskUpdateParameters** | [**TaskUpdateParameters**](TaskUpdateParameters.md)| The parameters for updating a task. | 

### Return type

[**Task**](Task.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

