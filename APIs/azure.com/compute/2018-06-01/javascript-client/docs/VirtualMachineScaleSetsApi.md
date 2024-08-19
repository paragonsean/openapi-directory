# ComputeManagementClient.VirtualMachineScaleSetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachineScaleSetsCreateOrUpdate**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName} | 
[**virtualMachineScaleSetsDeallocate**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsDeallocate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/deallocate | 
[**virtualMachineScaleSetsDelete**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName} | 
[**virtualMachineScaleSetsDeleteInstances**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsDeleteInstances) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/delete | 
[**virtualMachineScaleSetsForceRecoveryServiceFabricPlatformUpdateDomainWalk**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsForceRecoveryServiceFabricPlatformUpdateDomainWalk) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/forceRecoveryServiceFabricPlatformUpdateDomainWalk | 
[**virtualMachineScaleSetsGet**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName} | 
[**virtualMachineScaleSetsGetInstanceView**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsGetInstanceView) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/instanceView | 
[**virtualMachineScaleSetsGetOSUpgradeHistory**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsGetOSUpgradeHistory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/osUpgradeHistory | 
[**virtualMachineScaleSetsList**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets | 
[**virtualMachineScaleSetsListAll**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/virtualMachineScaleSets | 
[**virtualMachineScaleSetsListSkus**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsListSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/skus | 
[**virtualMachineScaleSetsPerformMaintenance**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsPerformMaintenance) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/performMaintenance | 
[**virtualMachineScaleSetsPowerOff**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsPowerOff) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/poweroff | 
[**virtualMachineScaleSetsRedeploy**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsRedeploy) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/redeploy | 
[**virtualMachineScaleSetsReimage**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsReimage) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/reimage | 
[**virtualMachineScaleSetsReimageAll**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsReimageAll) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/reimageall | 
[**virtualMachineScaleSetsRestart**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsRestart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/restart | 
[**virtualMachineScaleSetsStart**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/start | 
[**virtualMachineScaleSetsUpdate**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName} | 
[**virtualMachineScaleSetsUpdateInstances**](VirtualMachineScaleSetsApi.md#virtualMachineScaleSetsUpdateInstances) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/manualupgrade | 



## virtualMachineScaleSetsCreateOrUpdate

> VirtualMachineScaleSet virtualMachineScaleSetsCreateOrUpdate(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, parameters)



Create or update a VM scale set.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set to create or update.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ComputeManagementClient.VirtualMachineScaleSet(); // VirtualMachineScaleSet | The scale set object.
apiInstance.virtualMachineScaleSetsCreateOrUpdate(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **vmScaleSetName** | **String**| The name of the VM scale set to create or update. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VirtualMachineScaleSet**](VirtualMachineScaleSet.md)| The scale set object. | 

### Return type

[**VirtualMachineScaleSet**](VirtualMachineScaleSet.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualMachineScaleSetsDeallocate

> virtualMachineScaleSetsDeallocate(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts)



Deallocates specific virtual machines in a VM scale set. Shuts down the virtual machines and releases the compute resources. You are not billed for the compute resources that this virtual machine scale set deallocates.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'vmInstanceIDs': new ComputeManagementClient.VirtualMachineScaleSetVMInstanceIDs() // VirtualMachineScaleSetVMInstanceIDs | A list of virtual machine instance IDs from the VM scale set.
};
apiInstance.virtualMachineScaleSetsDeallocate(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceIDs**](VirtualMachineScaleSetVMInstanceIDs.md)| A list of virtual machine instance IDs from the VM scale set. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## virtualMachineScaleSetsDelete

> virtualMachineScaleSetsDelete(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Deletes a VM scale set.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetsDelete(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, (error, data, response) => {
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


## virtualMachineScaleSetsDeleteInstances

> virtualMachineScaleSetsDeleteInstances(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs)



Deletes virtual machines in a VM scale set.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let vmInstanceIDs = new ComputeManagementClient.VirtualMachineScaleSetVMInstanceRequiredIDs(); // VirtualMachineScaleSetVMInstanceRequiredIDs | A list of virtual machine instance IDs from the VM scale set.
apiInstance.virtualMachineScaleSetsDeleteInstances(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs, (error, data, response) => {
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
 **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceRequiredIDs**](VirtualMachineScaleSetVMInstanceRequiredIDs.md)| A list of virtual machine instance IDs from the VM scale set. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## virtualMachineScaleSetsForceRecoveryServiceFabricPlatformUpdateDomainWalk

> RecoveryWalkResponse virtualMachineScaleSetsForceRecoveryServiceFabricPlatformUpdateDomainWalk(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, platformUpdateDomain)



Manual platform update domain walk to update virtual machines in a service fabric virtual machine scale set.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let platformUpdateDomain = 56; // Number | The platform update domain for which a manual recovery walk is requested
apiInstance.virtualMachineScaleSetsForceRecoveryServiceFabricPlatformUpdateDomainWalk(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, platformUpdateDomain, (error, data, response) => {
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
 **platformUpdateDomain** | **Number**| The platform update domain for which a manual recovery walk is requested | 

### Return type

[**RecoveryWalkResponse**](RecoveryWalkResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineScaleSetsGet

> VirtualMachineScaleSet virtualMachineScaleSetsGet(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Display information about a virtual machine scale set.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetsGet(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, (error, data, response) => {
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

[**VirtualMachineScaleSet**](VirtualMachineScaleSet.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineScaleSetsGetInstanceView

> VirtualMachineScaleSetInstanceView virtualMachineScaleSetsGetInstanceView(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Gets the status of a VM scale set instance.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetsGetInstanceView(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, (error, data, response) => {
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

[**VirtualMachineScaleSetInstanceView**](VirtualMachineScaleSetInstanceView.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineScaleSetsGetOSUpgradeHistory

> VirtualMachineScaleSetListOSUpgradeHistory virtualMachineScaleSetsGetOSUpgradeHistory(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Gets list of OS upgrades on a VM scale set instance.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetsGetOSUpgradeHistory(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, (error, data, response) => {
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

[**VirtualMachineScaleSetListOSUpgradeHistory**](VirtualMachineScaleSetListOSUpgradeHistory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineScaleSetsList

> VirtualMachineScaleSetListResult virtualMachineScaleSetsList(resourceGroupName, apiVersion, subscriptionId)



Gets a list of all VM scale sets under a resource group.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetsList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualMachineScaleSetListResult**](VirtualMachineScaleSetListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineScaleSetsListAll

> VirtualMachineScaleSetListWithLinkResult virtualMachineScaleSetsListAll(apiVersion, subscriptionId)



Gets a list of all VM Scale Sets in the subscription, regardless of the associated resource group. Use nextLink property in the response to get the next page of VM Scale Sets. Do this till nextLink is null to fetch all the VM Scale Sets.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetsListAll(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualMachineScaleSetListWithLinkResult**](VirtualMachineScaleSetListWithLinkResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineScaleSetsListSkus

> VirtualMachineScaleSetListSkusResult virtualMachineScaleSetsListSkus(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId)



Gets a list of SKUs available for your VM scale set, including the minimum and maximum VM instances allowed for each SKU.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineScaleSetsListSkus(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, (error, data, response) => {
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

[**VirtualMachineScaleSetListSkusResult**](VirtualMachineScaleSetListSkusResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineScaleSetsPerformMaintenance

> virtualMachineScaleSetsPerformMaintenance(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts)



Perform maintenance on one or more virtual machines in a VM scale set. Operation on instances which are not eligible for perform maintenance will be failed. Please refer to best practices for more details: https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-maintenance-notifications

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'vmInstanceIDs': new ComputeManagementClient.VirtualMachineScaleSetVMInstanceIDs() // VirtualMachineScaleSetVMInstanceIDs | A list of virtual machine instance IDs from the VM scale set.
};
apiInstance.virtualMachineScaleSetsPerformMaintenance(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceIDs**](VirtualMachineScaleSetVMInstanceIDs.md)| A list of virtual machine instance IDs from the VM scale set. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## virtualMachineScaleSetsPowerOff

> virtualMachineScaleSetsPowerOff(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts)



Power off (stop) one or more virtual machines in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'vmInstanceIDs': new ComputeManagementClient.VirtualMachineScaleSetVMInstanceIDs() // VirtualMachineScaleSetVMInstanceIDs | A list of virtual machine instance IDs from the VM scale set.
};
apiInstance.virtualMachineScaleSetsPowerOff(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceIDs**](VirtualMachineScaleSetVMInstanceIDs.md)| A list of virtual machine instance IDs from the VM scale set. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## virtualMachineScaleSetsRedeploy

> virtualMachineScaleSetsRedeploy(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts)



Shuts down all the virtual machines in the virtual machine scale set, moves them to a new node, and powers them back on.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'vmInstanceIDs': new ComputeManagementClient.VirtualMachineScaleSetVMInstanceIDs() // VirtualMachineScaleSetVMInstanceIDs | A list of virtual machine instance IDs from the VM scale set.
};
apiInstance.virtualMachineScaleSetsRedeploy(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceIDs**](VirtualMachineScaleSetVMInstanceIDs.md)| A list of virtual machine instance IDs from the VM scale set. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## virtualMachineScaleSetsReimage

> virtualMachineScaleSetsReimage(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts)



Reimages (upgrade the operating system) one or more virtual machines in a VM scale set which don&#39;t have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'vmScaleSetReimageInput': new ComputeManagementClient.VirtualMachineScaleSetReimageParameters() // VirtualMachineScaleSetReimageParameters | Parameters for Reimaging VM ScaleSet.
};
apiInstance.virtualMachineScaleSetsReimage(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **vmScaleSetReimageInput** | [**VirtualMachineScaleSetReimageParameters**](VirtualMachineScaleSetReimageParameters.md)| Parameters for Reimaging VM ScaleSet. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## virtualMachineScaleSetsReimageAll

> virtualMachineScaleSetsReimageAll(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts)



Reimages all the disks ( including data disks ) in the virtual machines in a VM scale set. This operation is only supported for managed disks.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'vmInstanceIDs': new ComputeManagementClient.VirtualMachineScaleSetVMInstanceIDs() // VirtualMachineScaleSetVMInstanceIDs | A list of virtual machine instance IDs from the VM scale set.
};
apiInstance.virtualMachineScaleSetsReimageAll(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceIDs**](VirtualMachineScaleSetVMInstanceIDs.md)| A list of virtual machine instance IDs from the VM scale set. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## virtualMachineScaleSetsRestart

> virtualMachineScaleSetsRestart(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts)



Restarts one or more virtual machines in a VM scale set.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'vmInstanceIDs': new ComputeManagementClient.VirtualMachineScaleSetVMInstanceIDs() // VirtualMachineScaleSetVMInstanceIDs | A list of virtual machine instance IDs from the VM scale set.
};
apiInstance.virtualMachineScaleSetsRestart(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceIDs**](VirtualMachineScaleSetVMInstanceIDs.md)| A list of virtual machine instance IDs from the VM scale set. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## virtualMachineScaleSetsStart

> virtualMachineScaleSetsStart(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts)



Starts one or more virtual machines in a VM scale set.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'vmInstanceIDs': new ComputeManagementClient.VirtualMachineScaleSetVMInstanceIDs() // VirtualMachineScaleSetVMInstanceIDs | A list of virtual machine instance IDs from the VM scale set.
};
apiInstance.virtualMachineScaleSetsStart(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceIDs**](VirtualMachineScaleSetVMInstanceIDs.md)| A list of virtual machine instance IDs from the VM scale set. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## virtualMachineScaleSetsUpdate

> VirtualMachineScaleSet virtualMachineScaleSetsUpdate(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, parameters)



Update a VM scale set.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set to create or update.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ComputeManagementClient.VirtualMachineScaleSetUpdate(); // VirtualMachineScaleSetUpdate | The scale set object.
apiInstance.virtualMachineScaleSetsUpdate(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **vmScaleSetName** | **String**| The name of the VM scale set to create or update. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VirtualMachineScaleSetUpdate**](VirtualMachineScaleSetUpdate.md)| The scale set object. | 

### Return type

[**VirtualMachineScaleSet**](VirtualMachineScaleSet.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualMachineScaleSetsUpdateInstances

> virtualMachineScaleSetsUpdateInstances(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs)



Upgrades one or more virtual machines to the latest SKU set in the VM scale set model.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.VirtualMachineScaleSetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmScaleSetName = "vmScaleSetName_example"; // String | The name of the VM scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let vmInstanceIDs = new ComputeManagementClient.VirtualMachineScaleSetVMInstanceRequiredIDs(); // VirtualMachineScaleSetVMInstanceRequiredIDs | A list of virtual machine instance IDs from the VM scale set.
apiInstance.virtualMachineScaleSetsUpdateInstances(resourceGroupName, vmScaleSetName, apiVersion, subscriptionId, vmInstanceIDs, (error, data, response) => {
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
 **vmInstanceIDs** | [**VirtualMachineScaleSetVMInstanceRequiredIDs**](VirtualMachineScaleSetVMInstanceRequiredIDs.md)| A list of virtual machine instance IDs from the VM scale set. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

