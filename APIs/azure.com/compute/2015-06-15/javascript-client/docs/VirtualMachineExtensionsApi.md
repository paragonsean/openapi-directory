# ComputeManagementClient.VirtualMachineExtensionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachineExtensionsCreateOrUpdate**](VirtualMachineExtensionsApi.md#virtualMachineExtensionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{vmExtensionName} | 
[**virtualMachineExtensionsDelete**](VirtualMachineExtensionsApi.md#virtualMachineExtensionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{vmExtensionName} | 
[**virtualMachineExtensionsGet**](VirtualMachineExtensionsApi.md#virtualMachineExtensionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{vmExtensionName} | 
[**virtualMachineExtensionsUpdate**](VirtualMachineExtensionsApi.md#virtualMachineExtensionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{vmExtensionName} | 



## virtualMachineExtensionsCreateOrUpdate

> VirtualMachineExtension virtualMachineExtensionsCreateOrUpdate(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId, extensionParameters)



The operation to create or update the extension.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmName = "vmName_example"; // String | The name of the virtual machine where the extension should be created or updated.
let vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let extensionParameters = new ComputeManagementClient.VirtualMachineExtension(); // VirtualMachineExtension | Parameters supplied to the Create Virtual Machine Extension operation.
apiInstance.virtualMachineExtensionsCreateOrUpdate(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId, extensionParameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **vmName** | **String**| The name of the virtual machine where the extension should be created or updated. | 
 **vmExtensionName** | **String**| The name of the virtual machine extension. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **extensionParameters** | [**VirtualMachineExtension**](VirtualMachineExtension.md)| Parameters supplied to the Create Virtual Machine Extension operation. | 

### Return type

[**VirtualMachineExtension**](VirtualMachineExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualMachineExtensionsDelete

> OperationStatusResponse virtualMachineExtensionsDelete(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId)



The operation to delete the extension.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmName = "vmName_example"; // String | The name of the virtual machine where the extension should be deleted.
let vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineExtensionsDelete(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **vmName** | **String**| The name of the virtual machine where the extension should be deleted. | 
 **vmExtensionName** | **String**| The name of the virtual machine extension. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineExtensionsGet

> VirtualMachineExtension virtualMachineExtensionsGet(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId, opts)



The operation to get the extension.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmName = "vmName_example"; // String | The name of the virtual machine containing the extension.
let vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | The expand expression to apply on the operation.
};
apiInstance.virtualMachineExtensionsGet(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **vmName** | **String**| The name of the virtual machine containing the extension. | 
 **vmExtensionName** | **String**| The name of the virtual machine extension. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| The expand expression to apply on the operation. | [optional] 

### Return type

[**VirtualMachineExtension**](VirtualMachineExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineExtensionsUpdate

> VirtualMachineExtension virtualMachineExtensionsUpdate(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId, extensionParameters)



The operation to update the extension.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmName = "vmName_example"; // String | The name of the virtual machine where the extension should be updated.
let vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let extensionParameters = new ComputeManagementClient.VirtualMachineExtensionUpdate(); // VirtualMachineExtensionUpdate | Parameters supplied to the Update Virtual Machine Extension operation.
apiInstance.virtualMachineExtensionsUpdate(resourceGroupName, vmName, vmExtensionName, apiVersion, subscriptionId, extensionParameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **vmName** | **String**| The name of the virtual machine where the extension should be updated. | 
 **vmExtensionName** | **String**| The name of the virtual machine extension. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **extensionParameters** | [**VirtualMachineExtensionUpdate**](VirtualMachineExtensionUpdate.md)| Parameters supplied to the Update Virtual Machine Extension operation. | 

### Return type

[**VirtualMachineExtension**](VirtualMachineExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

