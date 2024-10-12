# ComputeManagementClient.VirtualMachineScaleSetRollingUpgradesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachineScaleSetRollingUpgradesCancel**](VirtualMachineScaleSetRollingUpgradesApi.md#virtualMachineScaleSetRollingUpgradesCancel) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/rollingUpgrades/cancel | 
[**virtualMachineScaleSetRollingUpgradesGetLatest**](VirtualMachineScaleSetRollingUpgradesApi.md#virtualMachineScaleSetRollingUpgradesGetLatest) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/rollingUpgrades/latest | 
[**virtualMachineScaleSetRollingUpgradesStartExtensionUpgrade**](VirtualMachineScaleSetRollingUpgradesApi.md#virtualMachineScaleSetRollingUpgradesStartExtensionUpgrade) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensionRollingUpgrade | 
[**virtualMachineScaleSetRollingUpgradesStartOSUpgrade**](VirtualMachineScaleSetRollingUpgradesApi.md#virtualMachineScaleSetRollingUpgradesStartOSUpgrade) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/osRollingUpgrade | 



## virtualMachineScaleSetRollingUpgradesCancel

> virtualMachineScaleSetRollingUpgradesCancel(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Cancels the current virtual machine scale set rolling upgrade.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetRollingUpgradesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetRollingUpgradesCancel(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualMachineScaleSetRollingUpgradesGetLatest

> RollingUpgradeStatusInfo virtualMachineScaleSetRollingUpgradesGetLatest(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Gets the status of the latest virtual machine scale set rolling upgrade.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetRollingUpgradesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetRollingUpgradesGetLatest(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RollingUpgradeStatusInfo**](RollingUpgradeStatusInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineScaleSetRollingUpgradesStartExtensionUpgrade

> virtualMachineScaleSetRollingUpgradesStartExtensionUpgrade(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Starts a rolling upgrade to move all extensions for all virtual machine scale set instances to the latest available extension version. Instances which are already running the latest extension versions are not affected.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetRollingUpgradesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetRollingUpgradesStartExtensionUpgrade(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualMachineScaleSetRollingUpgradesStartOSUpgrade

> virtualMachineScaleSetRollingUpgradesStartOSUpgrade(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Starts a rolling upgrade to move all virtual machine scale set instances to the latest available Platform Image OS version. Instances which are already running the latest available OS version are not affected.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetRollingUpgradesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetRollingUpgradesStartOSUpgrade(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

