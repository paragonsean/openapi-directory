# MerakiDashboardApi.ManagementInterfaceApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceManagementInterface_1**](ManagementInterfaceApi.md#getDeviceManagementInterface_1) | **GET** /devices/{serial}/managementInterface | Return the management interface settings for a device
[**updateDeviceManagementInterface_1**](ManagementInterfaceApi.md#updateDeviceManagementInterface_1) | **PUT** /devices/{serial}/managementInterface | Update the management interface settings for a device



## getDeviceManagementInterface_1

> Object getDeviceManagementInterface_1(serial)

Return the management interface settings for a device

Return the management interface settings for a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ManagementInterfaceApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceManagementInterface_1(serial, (error, data, response) => {
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
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeviceManagementInterface_1

> Object updateDeviceManagementInterface_1(serial, opts)

Update the management interface settings for a device

Update the management interface settings for a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ManagementInterfaceApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceManagementInterfaceRequest': new MerakiDashboardApi.UpdateDeviceManagementInterfaceRequest() // UpdateDeviceManagementInterfaceRequest | 
};
apiInstance.updateDeviceManagementInterface_1(serial, opts, (error, data, response) => {
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
 **serial** | **String**|  | 
 **updateDeviceManagementInterfaceRequest** | [**UpdateDeviceManagementInterfaceRequest**](UpdateDeviceManagementInterfaceRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

