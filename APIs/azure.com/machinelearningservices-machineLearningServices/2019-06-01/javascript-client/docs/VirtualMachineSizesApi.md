# AzureMachineLearningWorkspaces.VirtualMachineSizesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachineSizesList**](VirtualMachineSizesApi.md#virtualMachineSizesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/locations/{location}/vmSizes | 



## virtualMachineSizesList

> VirtualMachineSizeListResult virtualMachineSizesList(location, apiVersion, subscriptionId)



Returns supported VM Sizes in a location

### Example

```javascript
import AzureMachineLearningWorkspaces from 'azure_machine_learning_workspaces';
let defaultClient = AzureMachineLearningWorkspaces.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningWorkspaces.VirtualMachineSizesApi();
let location = "location_example"; // String | The location upon which virtual-machine-sizes is queried.
let apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
apiInstance.virtualMachineSizesList(location, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| The location upon which virtual-machine-sizes is queried. | 
 **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | 
 **subscriptionId** | **String**| Azure subscription identifier. | 

### Return type

[**VirtualMachineSizeListResult**](VirtualMachineSizeListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

