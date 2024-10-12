# NetworkManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publicIPAddressesGetVirtualMachineScaleSetPublicIPAddress**](DefaultApi.md#publicIPAddressesGetVirtualMachineScaleSetPublicIPAddress) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces/{networkInterfaceName}/ipconfigurations/{ipConfigurationName}/publicipaddresses/{publicIpAddressName} | 
[**publicIPAddressesListVirtualMachineScaleSetPublicIPAddresses**](DefaultApi.md#publicIPAddressesListVirtualMachineScaleSetPublicIPAddresses) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/publicipaddresses | 
[**publicIPAddressesListVirtualMachineScaleSetVMPublicIPAddresses**](DefaultApi.md#publicIPAddressesListVirtualMachineScaleSetVMPublicIPAddresses) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces/{networkInterfaceName}/ipconfigurations/{ipConfigurationName}/publicipaddresses | 



## publicIPAddressesGetVirtualMachineScaleSetPublicIPAddress

> PublicIPAddressesGetVirtualMachineScaleSetPublicIPAddress200Response publicIPAddressesGetVirtualMachineScaleSetPublicIPAddress(resourceGroupName, virtualMachineScaleSetName, virtualmachineIndex, networkInterfaceName, ipConfigurationName, publicIpAddressName, apiVersion, subscriptionId, opts)



Get the specified public IP address in a virtual machine scale set.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualMachineScaleSetName = "virtualMachineScaleSetName_example"; // String | The name of the virtual machine scale set.
let virtualmachineIndex = "virtualmachineIndex_example"; // String | The virtual machine index.
let networkInterfaceName = "networkInterfaceName_example"; // String | The name of the network interface.
let ipConfigurationName = "ipConfigurationName_example"; // String | The name of the IP configuration.
let publicIpAddressName = "publicIpAddressName_example"; // String | The name of the public IP Address.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | Expands referenced resources.
};
apiInstance.publicIPAddressesGetVirtualMachineScaleSetPublicIPAddress(resourceGroupName, virtualMachineScaleSetName, virtualmachineIndex, networkInterfaceName, ipConfigurationName, publicIpAddressName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **virtualMachineScaleSetName** | **String**| The name of the virtual machine scale set. | 
 **virtualmachineIndex** | **String**| The virtual machine index. | 
 **networkInterfaceName** | **String**| The name of the network interface. | 
 **ipConfigurationName** | **String**| The name of the IP configuration. | 
 **publicIpAddressName** | **String**| The name of the public IP Address. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| Expands referenced resources. | [optional] 

### Return type

[**PublicIPAddressesGetVirtualMachineScaleSetPublicIPAddress200Response**](PublicIPAddressesGetVirtualMachineScaleSetPublicIPAddress200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publicIPAddressesListVirtualMachineScaleSetPublicIPAddresses

> PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response publicIPAddressesListVirtualMachineScaleSetPublicIPAddresses(resourceGroupName, virtualMachineScaleSetName, apiVersion, subscriptionId)



Gets information about all public IP addresses on a virtual machine scale set level.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualMachineScaleSetName = "virtualMachineScaleSetName_example"; // String | The name of the virtual machine scale set.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.publicIPAddressesListVirtualMachineScaleSetPublicIPAddresses(resourceGroupName, virtualMachineScaleSetName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualMachineScaleSetName** | **String**| The name of the virtual machine scale set. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response**](PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publicIPAddressesListVirtualMachineScaleSetVMPublicIPAddresses

> PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response publicIPAddressesListVirtualMachineScaleSetVMPublicIPAddresses(resourceGroupName, virtualMachineScaleSetName, virtualmachineIndex, networkInterfaceName, ipConfigurationName, apiVersion, subscriptionId)



Gets information about all public IP addresses in a virtual machine IP configuration in a virtual machine scale set.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualMachineScaleSetName = "virtualMachineScaleSetName_example"; // String | The name of the virtual machine scale set.
let virtualmachineIndex = "virtualmachineIndex_example"; // String | The virtual machine index.
let networkInterfaceName = "networkInterfaceName_example"; // String | The network interface name.
let ipConfigurationName = "ipConfigurationName_example"; // String | The IP configuration name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.publicIPAddressesListVirtualMachineScaleSetVMPublicIPAddresses(resourceGroupName, virtualMachineScaleSetName, virtualmachineIndex, networkInterfaceName, ipConfigurationName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualMachineScaleSetName** | **String**| The name of the virtual machine scale set. | 
 **virtualmachineIndex** | **String**| The virtual machine index. | 
 **networkInterfaceName** | **String**| The network interface name. | 
 **ipConfigurationName** | **String**| The IP configuration name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response**](PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

