# ContainerRegistryManagementClient.BuildsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buildsCancel**](BuildsApi.md#buildsCancel) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/builds/{buildId}/cancel | 
[**buildsGet**](BuildsApi.md#buildsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/builds/{buildId} | 
[**buildsGetLogLink**](BuildsApi.md#buildsGetLogLink) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/builds/{buildId}/getLogLink | 
[**buildsList**](BuildsApi.md#buildsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/builds | 
[**buildsUpdate**](BuildsApi.md#buildsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/builds/{buildId} | 



## buildsCancel

> buildsCancel(subscriptionId, resourceGroupName, registryName, apiVersion, buildId)



Cancel an existing build.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildId = "buildId_example"; // String | The build ID.
apiInstance.buildsCancel(subscriptionId, resourceGroupName, registryName, apiVersion, buildId, (error, data, response) => {
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
 **buildId** | **String**| The build ID. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## buildsGet

> Build buildsGet(subscriptionId, resourceGroupName, registryName, apiVersion, buildId)



Gets the detailed information for a given build.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildId = "buildId_example"; // String | The build ID.
apiInstance.buildsGet(subscriptionId, resourceGroupName, registryName, apiVersion, buildId, (error, data, response) => {
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
 **buildId** | **String**| The build ID. | 

### Return type

[**Build**](Build.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsGetLogLink

> BuildGetLogResult buildsGetLogLink(subscriptionId, resourceGroupName, registryName, apiVersion, buildId)



Gets a link to download the build logs.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildId = "buildId_example"; // String | The build ID.
apiInstance.buildsGetLogLink(subscriptionId, resourceGroupName, registryName, apiVersion, buildId, (error, data, response) => {
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
 **buildId** | **String**| The build ID. | 

### Return type

[**BuildGetLogResult**](BuildGetLogResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsList

> BuildListResult buildsList(subscriptionId, resourceGroupName, registryName, apiVersion, opts)



Gets all the builds for a registry.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let opts = {
  'filter': "filter_example", // String | The builds filter to apply on the operation.
  'top': 56, // Number | $top is supported for get list of builds, which limits the maximum number of builds to return.
  'skipToken': "skipToken_example" // String | $skipToken is supported on get list of builds, which provides the next page in the list of builds.
};
apiInstance.buildsList(subscriptionId, resourceGroupName, registryName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The builds filter to apply on the operation. | [optional] 
 **top** | **Number**| $top is supported for get list of builds, which limits the maximum number of builds to return. | [optional] 
 **skipToken** | **String**| $skipToken is supported on get list of builds, which provides the next page in the list of builds. | [optional] 

### Return type

[**BuildListResult**](BuildListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsUpdate

> Build buildsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, buildId, buildUpdateParameters)



Patch the build properties.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.BuildsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let apiVersion = "apiVersion_example"; // String | The client API version.
let buildId = "buildId_example"; // String | The build ID.
let buildUpdateParameters = new ContainerRegistryManagementClient.BuildUpdateParameters(); // BuildUpdateParameters | The build update properties.
apiInstance.buildsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, buildId, buildUpdateParameters, (error, data, response) => {
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
 **buildId** | **String**| The build ID. | 
 **buildUpdateParameters** | [**BuildUpdateParameters**](BuildUpdateParameters.md)| The build update properties. | 

### Return type

[**Build**](Build.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

