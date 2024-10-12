# ContainerRegistryManagementClient.BuildTasksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buildTasksCreate**](BuildTasksApi.md#buildTasksCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName} | 
[**buildTasksDelete**](BuildTasksApi.md#buildTasksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName} | 
[**buildTasksGet**](BuildTasksApi.md#buildTasksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName} | 
[**buildTasksList**](BuildTasksApi.md#buildTasksList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks | 
[**buildTasksListSourceRepositoryProperties**](BuildTasksApi.md#buildTasksListSourceRepositoryProperties) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName}/listSourceRepositoryProperties | 
[**buildTasksUpdate**](BuildTasksApi.md#buildTasksUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName} | 



## buildTasksCreate

> BuildTask buildTasksCreate(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, buildTaskCreateParameters)



Creates a build task for a container registry with the specified parameters.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildTasksApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
let buildTaskCreateParameters = new ContainerRegistryManagementClient.BuildTask(); // BuildTask | The parameters for creating a build task.
apiInstance.buildTasksCreate(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, buildTaskCreateParameters, (error, data, response) => {
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
 **buildTaskName** | **String**| The name of the container registry build task. | 
 **buildTaskCreateParameters** | [**BuildTask**](BuildTask.md)| The parameters for creating a build task. | 

### Return type

[**BuildTask**](BuildTask.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## buildTasksDelete

> buildTasksDelete(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName)



Deletes a specified build task.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildTasksApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
apiInstance.buildTasksDelete(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, (error, data, response) => {
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
 **buildTaskName** | **String**| The name of the container registry build task. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## buildTasksGet

> BuildTask buildTasksGet(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName)



Get the properties of a specified build task.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildTasksApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
apiInstance.buildTasksGet(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, (error, data, response) => {
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
 **buildTaskName** | **String**| The name of the container registry build task. | 

### Return type

[**BuildTask**](BuildTask.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildTasksList

> BuildTaskListResult buildTasksList(subscriptionId, resourceGroupName, registryName, apiVersion, opts)



Lists all the build tasks for a specified container registry.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildTasksApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let opts = {
  'filter': "filter_example", // String | The build task filter to apply on the operation.
  'skipToken': "skipToken_example" // String | $skipToken is supported on get list of build tasks, which provides the next page in the list of tasks.
};
apiInstance.buildTasksList(subscriptionId, resourceGroupName, registryName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The build task filter to apply on the operation. | [optional] 
 **skipToken** | **String**| $skipToken is supported on get list of build tasks, which provides the next page in the list of tasks. | [optional] 

### Return type

[**BuildTaskListResult**](BuildTaskListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildTasksListSourceRepositoryProperties

> SourceRepositoryProperties buildTasksListSourceRepositoryProperties(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName)



Get the source control properties for a build task.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildTasksApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
apiInstance.buildTasksListSourceRepositoryProperties(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, (error, data, response) => {
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
 **buildTaskName** | **String**| The name of the container registry build task. | 

### Return type

[**SourceRepositoryProperties**](SourceRepositoryProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildTasksUpdate

> BuildTask buildTasksUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, buildTaskUpdateParameters)



Updates a build task with the specified parameters.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildTasksApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
let buildTaskUpdateParameters = new ContainerRegistryManagementClient.BuildTaskUpdateParameters(); // BuildTaskUpdateParameters | The parameters for updating a build task.
apiInstance.buildTasksUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, buildTaskUpdateParameters, (error, data, response) => {
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
 **buildTaskName** | **String**| The name of the container registry build task. | 
 **buildTaskUpdateParameters** | [**BuildTaskUpdateParameters**](BuildTaskUpdateParameters.md)| The parameters for updating a build task. | 

### Return type

[**BuildTask**](BuildTask.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

