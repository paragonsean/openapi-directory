# ContainerRegistryManagementClient.RunsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**runsCancel**](RunsApi.md#runsCancel) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/runs/{runId}/cancel | 
[**runsGet**](RunsApi.md#runsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/runs/{runId} | 
[**runsGetLogSasUrl**](RunsApi.md#runsGetLogSasUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/runs/{runId}/listLogSasUrl | 
[**runsList**](RunsApi.md#runsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/runs | 
[**runsUpdate**](RunsApi.md#runsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/runs/{runId} | 



## runsCancel

> runsCancel(subscriptionId, resourceGroupName, registryName, apiVersion, runId)



Cancel an existing run.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.RunsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let runId = "runId_example"; // String | The run ID.
apiInstance.runsCancel(subscriptionId, resourceGroupName, registryName, apiVersion, runId, (error, data, response) => {
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
 **runId** | **String**| The run ID. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runsGet

> Run runsGet(subscriptionId, resourceGroupName, registryName, apiVersion, runId)



Gets the detailed information for a given run.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.RunsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let runId = "runId_example"; // String | The run ID.
apiInstance.runsGet(subscriptionId, resourceGroupName, registryName, apiVersion, runId, (error, data, response) => {
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
 **runId** | **String**| The run ID. | 

### Return type

[**Run**](Run.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runsGetLogSasUrl

> RunGetLogResult runsGetLogSasUrl(subscriptionId, resourceGroupName, registryName, apiVersion, runId)



Gets a link to download the run logs.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.RunsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let runId = "runId_example"; // String | The run ID.
apiInstance.runsGetLogSasUrl(subscriptionId, resourceGroupName, registryName, apiVersion, runId, (error, data, response) => {
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
 **runId** | **String**| The run ID. | 

### Return type

[**RunGetLogResult**](RunGetLogResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runsList

> RunListResult runsList(subscriptionId, resourceGroupName, registryName, apiVersion, opts)



Gets all the runs for a registry.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.RunsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let opts = {
  'filter': "filter_example", // String | The runs filter to apply on the operation. Arithmetic operators are not supported. The allowed string function is 'contains'. All logical operators except 'Not', 'Has', 'All' are allowed.
  'top': 56 // Number | $top is supported for get list of runs, which limits the maximum number of runs to return.
};
apiInstance.runsList(subscriptionId, resourceGroupName, registryName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The runs filter to apply on the operation. Arithmetic operators are not supported. The allowed string function is &#39;contains&#39;. All logical operators except &#39;Not&#39;, &#39;Has&#39;, &#39;All&#39; are allowed. | [optional] 
 **top** | **Number**| $top is supported for get list of runs, which limits the maximum number of runs to return. | [optional] 

### Return type

[**RunListResult**](RunListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runsUpdate

> Run runsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, runId, runUpdateParameters)



Patch the run properties.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.RunsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let runId = "runId_example"; // String | The run ID.
let runUpdateParameters = new ContainerRegistryManagementClient.RunUpdateParameters(); // RunUpdateParameters | The run update properties.
apiInstance.runsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, runId, runUpdateParameters, (error, data, response) => {
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
 **runId** | **String**| The run ID. | 
 **runUpdateParameters** | [**RunUpdateParameters**](RunUpdateParameters.md)| The run update properties. | 

### Return type

[**Run**](Run.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

