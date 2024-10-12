# RunCommandsClient.VirtualMachineRunCommandsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachineRunCommandsGet**](VirtualMachineRunCommandsApi.md#virtualMachineRunCommandsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/runCommands/{commandId} | 
[**virtualMachineRunCommandsList**](VirtualMachineRunCommandsApi.md#virtualMachineRunCommandsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/runCommands | 



## virtualMachineRunCommandsGet

> RunCommandDocument virtualMachineRunCommandsGet(location, commandId, apiVersion, subscriptionId)



Gets specific run command for a subscription in a location.

### Example

```javascript
import RunCommandsClient from 'run_commands_client';
let defaultClient = RunCommandsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunCommandsClient.VirtualMachineRunCommandsApi();
let location = "location_example"; // String | The location upon which run commands is queried.
let commandId = "commandId_example"; // String | The command id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineRunCommandsGet(location, commandId, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| The location upon which run commands is queried. | 
 **commandId** | **String**| The command id. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RunCommandDocument**](RunCommandDocument.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## virtualMachineRunCommandsList

> RunCommandListResult virtualMachineRunCommandsList(location, apiVersion, subscriptionId)



Lists all available run commands for a subscription in a location.

### Example

```javascript
import RunCommandsClient from 'run_commands_client';
let defaultClient = RunCommandsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunCommandsClient.VirtualMachineRunCommandsApi();
let location = "location_example"; // String | The location upon which run commands is queried.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualMachineRunCommandsList(location, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| The location upon which run commands is queried. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RunCommandListResult**](RunCommandListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

