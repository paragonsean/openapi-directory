# ComputeManagementClient.VirtualMachineScaleSetExtensionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachineScaleSetExtensionsCreateOrUpdate**](VirtualMachineScaleSetExtensionsApi.md#virtualMachineScaleSetExtensionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName} | 
[**virtualMachineScaleSetExtensionsDelete**](VirtualMachineScaleSetExtensionsApi.md#virtualMachineScaleSetExtensionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName} | 
[**virtualMachineScaleSetExtensionsGet**](VirtualMachineScaleSetExtensionsApi.md#virtualMachineScaleSetExtensionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName} | 
[**virtualMachineScaleSetExtensionsList**](VirtualMachineScaleSetExtensionsApi.md#virtualMachineScaleSetExtensionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions | 



## virtualMachineScaleSetExtensionsCreateOrUpdate

> VirtualMachineScaleSetExtension virtualMachineScaleSetExtensionsCreateOrUpdate(resourceGroupName, vmScaleSetName, vmssExtensionName, apiVersion, subscriptionId, extensionParameters)



The operation to create or update an extension.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set where the extension should be create or updated.
let vmssExtensionName = "vmssExtensionName_example"; // String | The name of the VM scale set extension.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let extensionParameters = new ComputeManagementClient.VirtualMachineScaleSetExtension(); // VirtualMachineScaleSetExtension | Parameters supplied to the Create VM scale set Extension operation.
apiInstance.virtualMachineScaleSetExtensionsCreateOrUpdate(resourceGroupName, vmScaleSetName, vmssExtensionName, apiVersion, subscriptionId, extensionParameters, (error, data, response) => {
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
 **vmScaleSetName** | **String**| The name of the VM scale set where the extension should be create or updated. | 
 **vmssExtensionName** | **String**| The name of the VM scale set extension. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **extensionParameters** | [**VirtualMachineScaleSetExtension**](VirtualMachineScaleSetExtension.md)| Parameters supplied to the Create VM scale set Extension operation. | 

### Return type

[**VirtualMachineScaleSetExtension**](VirtualMachineScaleSetExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualMachineScaleSetExtensionsDelete

> virtualMachineScaleSetExtensionsDelete(resourceGroupName, vmScaleSetName, vmssExtensionName, apiVersion, subscriptionId)



The operation to delete the extension.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set where the extension should be deleted.
let vmssExtensionName = "vmssExtensionName_example"; // String | The name of the VM scale set extension.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetExtensionsDelete(resourceGroupName, vmScaleSetName, vmssExtensionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **vmScaleSetName** | **String**| The name of the VM scale set where the extension should be deleted. | 
 **vmssExtensionName** | **String**| The name of the VM scale set extension. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualMachineScaleSetExtensionsGet

> VirtualMachineScaleSetExtension virtualMachineScaleSetExtensionsGet(resourceGroupName, vmScaleSetName, vmssExtensionName, apiVersion, subscriptionId, opts)



The operation to get the extension.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set containing the extension.
let vmssExtensionName = "vmssExtensionName_example"; // String | The name of the VM scale set extension.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | The expand expression to apply on the operation.
};
apiInstance.virtualMachineScaleSetExtensionsGet(resourceGroupName, vmScaleSetName, vmssExtensionName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **vmScaleSetName** | **String**| The name of the VM scale set containing the extension. | 
 **vmssExtensionName** | **String**| The name of the VM scale set extension. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| The expand expression to apply on the operation. | [optional] 

### Return type

[**VirtualMachineScaleSetExtension**](VirtualMachineScaleSetExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineScaleSetExtensionsList

> VirtualMachineScaleSetExtensionListResult virtualMachineScaleSetExtensionsList(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Gets a list of all extensions in a VM scale set.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set containing the extension.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetExtensionsList(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, (error, data, response) => {
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
 **vmScaleSetName** | **String**| The name of the VM scale set containing the extension. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualMachineScaleSetExtensionListResult**](VirtualMachineScaleSetExtensionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

