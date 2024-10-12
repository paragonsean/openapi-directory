# NetworkManagementClient.NetworkInterfacesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networkInterfacesCreateOrUpdate**](NetworkInterfacesApi.md#networkInterfacesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkInterfaces/{networkInterfaceName} | 
[**networkInterfacesDelete**](NetworkInterfacesApi.md#networkInterfacesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkInterfaces/{networkInterfaceName} | 
[**networkInterfacesGet**](NetworkInterfacesApi.md#networkInterfacesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkInterfaces/{networkInterfaceName} | 
[**networkInterfacesGetEffectiveRouteTable**](NetworkInterfacesApi.md#networkInterfacesGetEffectiveRouteTable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkInterfaces/{networkInterfaceName}/effectiveRouteTable | 
[**networkInterfacesGetVirtualMachineScaleSetNetworkInterface**](NetworkInterfacesApi.md#networkInterfacesGetVirtualMachineScaleSetNetworkInterface) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces/{networkInterfaceName} | 
[**networkInterfacesList**](NetworkInterfacesApi.md#networkInterfacesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkInterfaces | 
[**networkInterfacesListAll**](NetworkInterfacesApi.md#networkInterfacesListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/networkInterfaces | 
[**networkInterfacesListEffectiveNetworkSecurityGroups**](NetworkInterfacesApi.md#networkInterfacesListEffectiveNetworkSecurityGroups) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkInterfaces/{networkInterfaceName}/effectiveNetworkSecurityGroups | 
[**networkInterfacesListVirtualMachineScaleSetNetworkInterfaces**](NetworkInterfacesApi.md#networkInterfacesListVirtualMachineScaleSetNetworkInterfaces) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/networkInterfaces | 
[**networkInterfacesListVirtualMachineScaleSetVMNetworkInterfaces**](NetworkInterfacesApi.md#networkInterfacesListVirtualMachineScaleSetVMNetworkInterfaces) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces | 



## networkInterfacesCreateOrUpdate

> NetworkInterface networkInterfacesCreateOrUpdate(resourceGroupName, networkInterfaceName, apiVersion, subscriptionId, parameters)



The Put NetworkInterface operation creates/updates a networkInterface

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkInterfacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkInterfaceName = "networkInterfaceName_example"; // String | The name of the network interface.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.NetworkInterface(); // NetworkInterface | Parameters supplied to the create/update NetworkInterface operation
apiInstance.networkInterfacesCreateOrUpdate(resourceGroupName, networkInterfaceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **networkInterfaceName** | **String**| The name of the network interface. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**NetworkInterface**](NetworkInterface.md)| Parameters supplied to the create/update NetworkInterface operation | 

### Return type

[**NetworkInterface**](NetworkInterface.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## networkInterfacesDelete

> networkInterfacesDelete(resourceGroupName, networkInterfaceName, apiVersion, subscriptionId)



The delete networkInterface operation deletes the specified networkInterface.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkInterfacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkInterfaceName = "networkInterfaceName_example"; // String | The name of the network interface.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.networkInterfacesDelete(resourceGroupName, networkInterfaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **networkInterfaceName** | **String**| The name of the network interface. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## networkInterfacesGet

> NetworkInterface networkInterfacesGet(resourceGroupName, networkInterfaceName, apiVersion, subscriptionId, opts)



The Get network interface operation retrieves information about the specified network interface.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkInterfacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkInterfaceName = "networkInterfaceName_example"; // String | The name of the network interface.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | expand references resources.
};
apiInstance.networkInterfacesGet(resourceGroupName, networkInterfaceName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **networkInterfaceName** | **String**| The name of the network interface. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| expand references resources. | [optional] 

### Return type

[**NetworkInterface**](NetworkInterface.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## networkInterfacesGetEffectiveRouteTable

> EffectiveRouteListResult networkInterfacesGetEffectiveRouteTable(resourceGroupName, networkInterfaceName, apiVersion, subscriptionId)



Retrieves all the route tables applied on a networkInterface.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkInterfacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkInterfaceName = "networkInterfaceName_example"; // String | The name of the network interface.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.networkInterfacesGetEffectiveRouteTable(resourceGroupName, networkInterfaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **networkInterfaceName** | **String**| The name of the network interface. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**EffectiveRouteListResult**](EffectiveRouteListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## networkInterfacesGetVirtualMachineScaleSetNetworkInterface

> NetworkInterface networkInterfacesGetVirtualMachineScaleSetNetworkInterface(resourceGroupName, virtualMachineScaleSetName, virtualmachineIndex, networkInterfaceName, apiVersion, subscriptionId, opts)



The Get network interface operation retrieves information about the specified network interface in a virtual machine scale set.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkInterfacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualMachineScaleSetName = "virtualMachineScaleSetName_example"; // String | The name of the virtual machine scale set.
let virtualmachineIndex = "virtualmachineIndex_example"; // String | The virtual machine index.
let networkInterfaceName = "networkInterfaceName_example"; // String | The name of the network interface.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | expand references resources.
};
apiInstance.networkInterfacesGetVirtualMachineScaleSetNetworkInterface(resourceGroupName, virtualMachineScaleSetName, virtualmachineIndex, networkInterfaceName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| expand references resources. | [optional] 

### Return type

[**NetworkInterface**](NetworkInterface.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## networkInterfacesList

> NetworkInterfaceListResult networkInterfacesList(resourceGroupName, apiVersion, subscriptionId)



The List networkInterfaces operation retrieves all the networkInterfaces in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkInterfacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.networkInterfacesList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**NetworkInterfaceListResult**](NetworkInterfaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## networkInterfacesListAll

> NetworkInterfaceListResult networkInterfacesListAll(apiVersion, subscriptionId)



The List networkInterfaces operation retrieves all the networkInterfaces in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkInterfacesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.networkInterfacesListAll(apiVersion, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**NetworkInterfaceListResult**](NetworkInterfaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## networkInterfacesListEffectiveNetworkSecurityGroups

> EffectiveNetworkSecurityGroupListResult networkInterfacesListEffectiveNetworkSecurityGroups(resourceGroupName, networkInterfaceName, apiVersion, subscriptionId)



The list effective network security group operation retrieves all the network security groups applied on a networkInterface.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkInterfacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkInterfaceName = "networkInterfaceName_example"; // String | The name of the network interface.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.networkInterfacesListEffectiveNetworkSecurityGroups(resourceGroupName, networkInterfaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **networkInterfaceName** | **String**| The name of the network interface. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**EffectiveNetworkSecurityGroupListResult**](EffectiveNetworkSecurityGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## networkInterfacesListVirtualMachineScaleSetNetworkInterfaces

> NetworkInterfaceListResult networkInterfacesListVirtualMachineScaleSetNetworkInterfaces(resourceGroupName, virtualMachineScaleSetName, apiVersion, subscriptionId)



The list network interface operation retrieves information about all network interfaces in a virtual machine scale set.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkInterfacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualMachineScaleSetName = "virtualMachineScaleSetName_example"; // String | The name of the virtual machine scale set.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.networkInterfacesListVirtualMachineScaleSetNetworkInterfaces(resourceGroupName, virtualMachineScaleSetName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**NetworkInterfaceListResult**](NetworkInterfaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## networkInterfacesListVirtualMachineScaleSetVMNetworkInterfaces

> NetworkInterfaceListResult networkInterfacesListVirtualMachineScaleSetVMNetworkInterfaces(resourceGroupName, virtualMachineScaleSetName, virtualmachineIndex, apiVersion, subscriptionId)



The list network interface operation retrieves information about all network interfaces in a virtual machine from a virtual machine scale set.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkInterfacesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualMachineScaleSetName = "virtualMachineScaleSetName_example"; // String | The name of the virtual machine scale set.
let virtualmachineIndex = "virtualmachineIndex_example"; // String | The virtual machine index.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.networkInterfacesListVirtualMachineScaleSetVMNetworkInterfaces(resourceGroupName, virtualMachineScaleSetName, virtualmachineIndex, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**NetworkInterfaceListResult**](NetworkInterfaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

