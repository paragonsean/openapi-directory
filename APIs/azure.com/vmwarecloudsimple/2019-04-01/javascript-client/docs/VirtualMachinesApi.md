# VMwareCloudSimple.VirtualMachinesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachinesCreateOrUpdate**](VirtualMachinesApi.md#virtualMachinesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtualMachineName} | Implements virtual machine PUT method
[**virtualMachinesDelete**](VirtualMachinesApi.md#virtualMachinesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtualMachineName} | Implements virtual machine DELETE method
[**virtualMachinesGet**](VirtualMachinesApi.md#virtualMachinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtualMachineName} | Implements virtual machine GET method
[**virtualMachinesListByResourceGroup**](VirtualMachinesApi.md#virtualMachinesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines | Implements list virtual machine within RG method
[**virtualMachinesListBySubscription**](VirtualMachinesApi.md#virtualMachinesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/virtualMachines | Implements list virtual machine within subscription method
[**virtualMachinesStart**](VirtualMachinesApi.md#virtualMachinesStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtualMachineName}/start | Implements a start method for a virtual machine
[**virtualMachinesStop**](VirtualMachinesApi.md#virtualMachinesStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtualMachineName}/stop | Implements shutdown, poweroff, and suspend method for a virtual machine
[**virtualMachinesUpdate**](VirtualMachinesApi.md#virtualMachinesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtualMachineName} | Implements virtual machine PATCH method



## virtualMachinesCreateOrUpdate

> VirtualMachine virtualMachinesCreateOrUpdate(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion, virtualMachineRequest)

Implements virtual machine PUT method

Create Or Update Virtual Machine

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.VirtualMachinesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let referer = "referer_example"; // String | referer url
let virtualMachineName = "virtualMachineName_example"; // String | virtual machine name
let apiVersion = "apiVersion_example"; // String | Client API version.
let virtualMachineRequest = new VMwareCloudSimple.VirtualMachine(); // VirtualMachine | Create or Update Virtual Machine request
apiInstance.virtualMachinesCreateOrUpdate(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion, virtualMachineRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group | 
 **referer** | **String**| referer url | 
 **virtualMachineName** | **String**| virtual machine name | 
 **apiVersion** | **String**| Client API version. | 
 **virtualMachineRequest** | [**VirtualMachine**](VirtualMachine.md)| Create or Update Virtual Machine request | 

### Return type

[**VirtualMachine**](VirtualMachine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualMachinesDelete

> virtualMachinesDelete(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion)

Implements virtual machine DELETE method

Delete virtual machine

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.VirtualMachinesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let referer = "referer_example"; // String | referer url
let virtualMachineName = "virtualMachineName_example"; // String | virtual machine name
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.virtualMachinesDelete(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group | 
 **referer** | **String**| referer url | 
 **virtualMachineName** | **String**| virtual machine name | 
 **apiVersion** | **String**| Client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachinesGet

> VirtualMachine virtualMachinesGet(subscriptionId, resourceGroupName, virtualMachineName, apiVersion)

Implements virtual machine GET method

Get virtual machine

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.VirtualMachinesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let virtualMachineName = "virtualMachineName_example"; // String | virtual machine name
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.virtualMachinesGet(subscriptionId, resourceGroupName, virtualMachineName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group | 
 **virtualMachineName** | **String**| virtual machine name | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**VirtualMachine**](VirtualMachine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachinesListByResourceGroup

> VirtualMachineListResponse virtualMachinesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)

Implements list virtual machine within RG method

Returns list of virtual machine within resource group

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.VirtualMachinesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the list operation
  'top': 56, // Number | The maximum number of record sets to return
  'skipToken': "skipToken_example" // String | to be used by nextLink implementation
};
apiInstance.virtualMachinesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group | 
 **apiVersion** | **String**| Client API version. | 
 **filter** | **String**| The filter to apply on the list operation | [optional] 
 **top** | **Number**| The maximum number of record sets to return | [optional] 
 **skipToken** | **String**| to be used by nextLink implementation | [optional] 

### Return type

[**VirtualMachineListResponse**](VirtualMachineListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachinesListBySubscription

> VirtualMachineListResponse virtualMachinesListBySubscription(subscriptionId, apiVersion, opts)

Implements list virtual machine within subscription method

Returns list virtual machine within subscription

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.VirtualMachinesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the list operation
  'top': 56, // Number | The maximum number of record sets to return
  'skipToken': "skipToken_example" // String | to be used by nextLink implementation
};
apiInstance.virtualMachinesListBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **apiVersion** | **String**| Client API version. | 
 **filter** | **String**| The filter to apply on the list operation | [optional] 
 **top** | **Number**| The maximum number of record sets to return | [optional] 
 **skipToken** | **String**| to be used by nextLink implementation | [optional] 

### Return type

[**VirtualMachineListResponse**](VirtualMachineListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachinesStart

> virtualMachinesStart(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion)

Implements a start method for a virtual machine

Power on virtual machine

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.VirtualMachinesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let referer = "referer_example"; // String | referer url
let virtualMachineName = "virtualMachineName_example"; // String | virtual machine name
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.virtualMachinesStart(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group | 
 **referer** | **String**| referer url | 
 **virtualMachineName** | **String**| virtual machine name | 
 **apiVersion** | **String**| Client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachinesStop

> virtualMachinesStop(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion, opts)

Implements shutdown, poweroff, and suspend method for a virtual machine

Power off virtual machine, options: shutdown, poweroff, and suspend

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.VirtualMachinesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let referer = "referer_example"; // String | referer url
let virtualMachineName = "virtualMachineName_example"; // String | virtual machine name
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'mode': "mode_example", // String | query stop mode parameter (reboot, shutdown, etc...)
  'm': new VMwareCloudSimple.VirtualMachineStopMode() // VirtualMachineStopMode | body stop mode parameter (reboot, shutdown, etc...)
};
apiInstance.virtualMachinesStop(subscriptionId, resourceGroupName, referer, virtualMachineName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group | 
 **referer** | **String**| referer url | 
 **virtualMachineName** | **String**| virtual machine name | 
 **apiVersion** | **String**| Client API version. | 
 **mode** | **String**| query stop mode parameter (reboot, shutdown, etc...) | [optional] 
 **m** | [**VirtualMachineStopMode**](VirtualMachineStopMode.md)| body stop mode parameter (reboot, shutdown, etc...) | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualMachinesUpdate

> VirtualMachine virtualMachinesUpdate(subscriptionId, resourceGroupName, virtualMachineName, apiVersion, virtualMachineRequest)

Implements virtual machine PATCH method

Patch virtual machine properties

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.VirtualMachinesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
let virtualMachineName = "virtualMachineName_example"; // String | virtual machine name
let apiVersion = "apiVersion_example"; // String | Client API version.
let virtualMachineRequest = new VMwareCloudSimple.PatchPayload(); // PatchPayload | Patch virtual machine request
apiInstance.virtualMachinesUpdate(subscriptionId, resourceGroupName, virtualMachineName, apiVersion, virtualMachineRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group | 
 **virtualMachineName** | **String**| virtual machine name | 
 **apiVersion** | **String**| Client API version. | 
 **virtualMachineRequest** | [**PatchPayload**](PatchPayload.md)| Patch virtual machine request | 

### Return type

[**VirtualMachine**](VirtualMachine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

