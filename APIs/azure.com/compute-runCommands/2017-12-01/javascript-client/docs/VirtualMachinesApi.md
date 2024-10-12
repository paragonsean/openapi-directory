# RunCommandsClient.VirtualMachinesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachinesRunCommand**](VirtualMachinesApi.md#virtualMachinesRunCommand) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/runCommand | 



## virtualMachinesRunCommand

> RunCommandResult virtualMachinesRunCommand(resourceGroupName, vmName, apiVersion, subscriptionId, parameters)



Run command on the VM.

### Example

```javascript
import RunCommandsClient from 'run_commands_client';
let defaultClient = RunCommandsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunCommandsClient.VirtualMachinesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let vmName = "vmName_example"; // String | The name of the virtual machine.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RunCommandsClient.RunCommandInput(); // RunCommandInput | Parameters supplied to the Run command operation.
apiInstance.virtualMachinesRunCommand(resourceGroupName, vmName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **vmName** | **String**| The name of the virtual machine. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RunCommandInput**](RunCommandInput.md)| Parameters supplied to the Run command operation. | 

### Return type

[**RunCommandResult**](RunCommandResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

