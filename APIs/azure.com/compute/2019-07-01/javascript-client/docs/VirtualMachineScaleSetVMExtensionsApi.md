# ComputeManagementClient.VirtualMachineScaleSetVMExtensionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachineScaleSetVMExtensionsCreateOrUpdate**](VirtualMachineScaleSetVMExtensionsApi.md#virtualMachineScaleSetVMExtensionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName} | 
[**virtualMachineScaleSetVMExtensionsDelete**](VirtualMachineScaleSetVMExtensionsApi.md#virtualMachineScaleSetVMExtensionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName} | 
[**virtualMachineScaleSetVMExtensionsGet**](VirtualMachineScaleSetVMExtensionsApi.md#virtualMachineScaleSetVMExtensionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName} | 
[**virtualMachineScaleSetVMExtensionsList**](VirtualMachineScaleSetVMExtensionsApi.md#virtualMachineScaleSetVMExtensionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions | 
[**virtualMachineScaleSetVMExtensionsUpdate**](VirtualMachineScaleSetVMExtensionsApi.md#virtualMachineScaleSetVMExtensionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName} | 



## virtualMachineScaleSetVMExtensionsCreateOrUpdate

> VirtualMachineExtension virtualMachineScaleSetVMExtensionsCreateOrUpdate(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId, extensionParameters)



The operation to create or update the VMSS VM extension.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetVMExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
let vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let extensionParameters = new ComputeManagementClient.VirtualMachineExtension(); // VirtualMachineExtension | Parameters supplied to the Create Virtual Machine Extension operation.
apiInstance.virtualMachineScaleSetVMExtensionsCreateOrUpdate(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId, extensionParameters, (error, data, response) => {
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
 **vmScaleSetName** | **String**| The name of the VM scale set. | 
 **instanceId** | **String**| The instance ID of the virtual machine. | 
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


## virtualMachineScaleSetVMExtensionsDelete

> virtualMachineScaleSetVMExtensionsDelete(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId)



The operation to delete the VMSS VM extension.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetVMExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
let vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetVMExtensionsDelete(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **vmScaleSetName** | **String**| The name of the VM scale set. | 
 **instanceId** | **String**| The instance ID of the virtual machine. | 
 **vmExtensionName** | **String**| The name of the virtual machine extension. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineScaleSetVMExtensionsGet

> VirtualMachineExtension virtualMachineScaleSetVMExtensionsGet(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId, opts)



The operation to get the VMSS VM extension.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetVMExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
let vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | The expand expression to apply on the operation.
};
apiInstance.virtualMachineScaleSetVMExtensionsGet(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **vmScaleSetName** | **String**| The name of the VM scale set. | 
 **instanceId** | **String**| The instance ID of the virtual machine. | 
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


## virtualMachineScaleSetVMExtensionsList

> VirtualMachineExtensionsListResult virtualMachineScaleSetVMExtensionsList(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId, opts)



The operation to get all extensions of an instance in Virtual Machine Scaleset.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetVMExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | The expand expression to apply on the operation.
};
apiInstance.virtualMachineScaleSetVMExtensionsList(resourceGroupName, vmScaleSetName, instanceId, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **vmScaleSetName** | **String**| The name of the VM scale set. | 
 **instanceId** | **String**| The instance ID of the virtual machine. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| The expand expression to apply on the operation. | [optional] 

### Return type

[**VirtualMachineExtensionsListResult**](VirtualMachineExtensionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineScaleSetVMExtensionsUpdate

> VirtualMachineExtension virtualMachineScaleSetVMExtensionsUpdate(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId, extensionParameters)



The operation to update the VMSS VM extension.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetVMExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let instanceId = "instanceId_example"; // String | The instance ID of the virtual machine.
let vmExtensionName = "vmExtensionName_example"; // String | The name of the virtual machine extension.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let extensionParameters = new ComputeManagementClient.VirtualMachineExtensionUpdate(); // VirtualMachineExtensionUpdate | Parameters supplied to the Update Virtual Machine Extension operation.
apiInstance.virtualMachineScaleSetVMExtensionsUpdate(resourceGroupName, vmScaleSetName, instanceId, vmExtensionName, apiVersion, subscriptionId, extensionParameters, (error, data, response) => {
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
 **vmScaleSetName** | **String**| The name of the VM scale set. | 
 **instanceId** | **String**| The instance ID of the virtual machine. | 
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

