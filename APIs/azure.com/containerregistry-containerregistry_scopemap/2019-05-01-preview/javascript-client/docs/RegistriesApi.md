# ContainerRegistryManagementClient.RegistriesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registriesGenerateCredentials**](RegistriesApi.md#registriesGenerateCredentials) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/generateCredentials | 



## registriesGenerateCredentials

> GenerateCredentialsResult registriesGenerateCredentials(apiVersion, subscriptionId, resourceGroupName, registryName, generateCredentialsParameters)



Generate keys for a token of a specified container registry.

### Example

```javascript
import ContainerRegistryManagementClient from 'container_registry_management_client';
let defaultClient = ContainerRegistryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerRegistryManagementClient.RegistriesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let registryName = "registryName_example"; // String | The name of the container registry.
let generateCredentialsParameters = new ContainerRegistryManagementClient.GenerateCredentialsParameters(); // GenerateCredentialsParameters | The parameters for generating credentials.
apiInstance.registriesGenerateCredentials(apiVersion, subscriptionId, resourceGroupName, registryName, generateCredentialsParameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **registryName** | **String**| The name of the container registry. | 
 **generateCredentialsParameters** | [**GenerateCredentialsParameters**](GenerateCredentialsParameters.md)| The parameters for generating credentials. | 

### Return type

[**GenerateCredentialsResult**](GenerateCredentialsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

