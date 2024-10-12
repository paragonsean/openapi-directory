# DeviceServices.CheckDeviceServiceNameAvailabilityApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicesCheckDeviceServiceNameAvailability**](CheckDeviceServiceNameAvailabilityApi.md#servicesCheckDeviceServiceNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.WindowsIoT/checkDeviceServiceNameAvailability | 



## servicesCheckDeviceServiceNameAvailability

> DeviceServiceNameAvailabilityInfo servicesCheckDeviceServiceNameAvailability(apiVersion, subscriptionId, deviceServiceCheckNameAvailabilityParameters)



Check if a Windows IoT Device Service name is available.

### Example

```javascript
import DeviceServices from 'device_services';
let defaultClient = DeviceServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeviceServices.CheckDeviceServiceNameAvailabilityApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let deviceServiceCheckNameAvailabilityParameters = new DeviceServices.DeviceServiceCheckNameAvailabilityParameters(); // DeviceServiceCheckNameAvailabilityParameters | Set the name parameter in the DeviceServiceCheckNameAvailabilityParameters structure to the name of the Windows IoT Device Service to check.
apiInstance.servicesCheckDeviceServiceNameAvailability(apiVersion, subscriptionId, deviceServiceCheckNameAvailabilityParameters, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **deviceServiceCheckNameAvailabilityParameters** | [**DeviceServiceCheckNameAvailabilityParameters**](DeviceServiceCheckNameAvailabilityParameters.md)| Set the name parameter in the DeviceServiceCheckNameAvailabilityParameters structure to the name of the Windows IoT Device Service to check. | 

### Return type

[**DeviceServiceNameAvailabilityInfo**](DeviceServiceNameAvailabilityInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

