# StorSimple8000SeriesManagementClient.HardwareComponentGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hardwareComponentGroupsChangeControllerPowerState**](HardwareComponentGroupsApi.md#hardwareComponentGroupsChangeControllerPowerState) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/hardwareComponentGroups/{hardwareComponentGroupName}/changeControllerPowerState | 
[**hardwareComponentGroupsListByDevice**](HardwareComponentGroupsApi.md#hardwareComponentGroupsListByDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/hardwareComponentGroups | 



## hardwareComponentGroupsChangeControllerPowerState

> hardwareComponentGroupsChangeControllerPowerState(deviceName, hardwareComponentGroupName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters)



Changes the power state of the controller.

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.HardwareComponentGroupsApi();
let deviceName = "deviceName_example"; // String | The device name
let hardwareComponentGroupName = "hardwareComponentGroupName_example"; // String | The hardware component group name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let parameters = new StorSimple8000SeriesManagementClient.ControllerPowerStateChangeRequest(); // ControllerPowerStateChangeRequest | The controller power state change request.
apiInstance.hardwareComponentGroupsChangeControllerPowerState(deviceName, hardwareComponentGroupName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters, (error, data, response) => {
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
 **deviceName** | **String**| The device name | 
 **hardwareComponentGroupName** | **String**| The hardware component group name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **parameters** | [**ControllerPowerStateChangeRequest**](ControllerPowerStateChangeRequest.md)| The controller power state change request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## hardwareComponentGroupsListByDevice

> HardwareComponentGroupList hardwareComponentGroupsListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion)



Lists the hardware component groups at device-level.

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.HardwareComponentGroupsApi();
let deviceName = "deviceName_example"; // String | The device name
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.hardwareComponentGroupsListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**HardwareComponentGroupList**](HardwareComponentGroupList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

