# ContainerRegistryManagementClient.BuildStepsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buildStepsCreate**](BuildStepsApi.md#buildStepsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName}/steps/{stepName} | 
[**buildStepsDelete**](BuildStepsApi.md#buildStepsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName}/steps/{stepName} | 
[**buildStepsGet**](BuildStepsApi.md#buildStepsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName}/steps/{stepName} | 
[**buildStepsList**](BuildStepsApi.md#buildStepsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName}/steps | 
[**buildStepsListBuildArguments**](BuildStepsApi.md#buildStepsListBuildArguments) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName}/steps/{stepName}/listBuildArguments | 
[**buildStepsUpdate**](BuildStepsApi.md#buildStepsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName}/steps/{stepName} | 



## buildStepsCreate

> BuildStep buildStepsCreate(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName, buildStepCreateParameters)



Creates a build step for a build task.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildStepsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
let stepName = "stepName_example"; // String | The name of a build step for a container registry build task.
let buildStepCreateParameters = new ContainerRegistryManagementClient.BuildStep(); // BuildStep | The parameters for creating a build step.
apiInstance.buildStepsCreate(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName, buildStepCreateParameters, (error, data, response) => {
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
 **stepName** | **String**| The name of a build step for a container registry build task. | 
 **buildStepCreateParameters** | [**BuildStep**](BuildStep.md)| The parameters for creating a build step. | 

### Return type

[**BuildStep**](BuildStep.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## buildStepsDelete

> buildStepsDelete(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName)



Deletes a build step from the build task.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildStepsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
let stepName = "stepName_example"; // String | The name of a build step for a container registry build task.
apiInstance.buildStepsDelete(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName, (error, data, response) => {
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
 **stepName** | **String**| The name of a build step for a container registry build task. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## buildStepsGet

> BuildStep buildStepsGet(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName)



Gets the build step for a build task.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildStepsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
let stepName = "stepName_example"; // String | The name of a build step for a container registry build task.
apiInstance.buildStepsGet(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName, (error, data, response) => {
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
 **stepName** | **String**| The name of a build step for a container registry build task. | 

### Return type

[**BuildStep**](BuildStep.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildStepsList

> BuildStepList buildStepsList(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName)



List all the build steps for a given build task.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildStepsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
apiInstance.buildStepsList(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, (error, data, response) => {
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

[**BuildStepList**](BuildStepList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildStepsListBuildArguments

> BuildArgumentList buildStepsListBuildArguments(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName)



List the build arguments for a step including the secret arguments.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildStepsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
let stepName = "stepName_example"; // String | The name of a build step for a container registry build task.
apiInstance.buildStepsListBuildArguments(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName, (error, data, response) => {
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
 **stepName** | **String**| The name of a build step for a container registry build task. | 

### Return type

[**BuildArgumentList**](BuildArgumentList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildStepsUpdate

> BuildStep buildStepsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName, buildStepUpdateParameters)



Updates a build step in a build task.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildStepsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
let stepName = "stepName_example"; // String | The name of a build step for a container registry build task.
let buildStepUpdateParameters = new ContainerRegistryManagementClient.BuildStepUpdateParameters(); // BuildStepUpdateParameters | The parameters for updating a build step.
apiInstance.buildStepsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName, buildStepUpdateParameters, (error, data, response) => {
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
 **stepName** | **String**| The name of a build step for a container registry build task. | 
 **buildStepUpdateParameters** | [**BuildStepUpdateParameters**](BuildStepUpdateParameters.md)| The parameters for updating a build step. | 

### Return type

[**BuildStep**](BuildStep.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

