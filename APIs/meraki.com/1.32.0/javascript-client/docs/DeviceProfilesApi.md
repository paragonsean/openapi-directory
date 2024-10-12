# MerakiDashboardApi.DeviceProfilesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkSmDeviceDeviceProfiles_2**](DeviceProfilesApi.md#getNetworkSmDeviceDeviceProfiles_2) | **GET** /networks/{networkId}/sm/devices/{deviceId}/deviceProfiles | Get the installed profiles associated with a device
[**getNetworkSmUserDeviceProfiles_2**](DeviceProfilesApi.md#getNetworkSmUserDeviceProfiles_2) | **GET** /networks/{networkId}/sm/users/{userId}/deviceProfiles | Get the profiles associated with a user



## getNetworkSmDeviceDeviceProfiles_2

> [GetNetworkSmDeviceDeviceProfiles200ResponseInner] getNetworkSmDeviceDeviceProfiles_2(networkId, deviceId)

Get the installed profiles associated with a device

Get the installed profiles associated with a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.DeviceProfilesApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmDeviceDeviceProfiles_2(networkId, deviceId, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **deviceId** | **String**|  | 

### Return type

[**[GetNetworkSmDeviceDeviceProfiles200ResponseInner]**](GetNetworkSmDeviceDeviceProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmUserDeviceProfiles_2

> [GetNetworkSmDeviceDeviceProfiles200ResponseInner] getNetworkSmUserDeviceProfiles_2(networkId, userId)

Get the profiles associated with a user

Get the profiles associated with a user

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.DeviceProfilesApi();
let networkId = "networkId_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.getNetworkSmUserDeviceProfiles_2(networkId, userId, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **userId** | **String**|  | 

### Return type

[**[GetNetworkSmDeviceDeviceProfiles200ResponseInner]**](GetNetworkSmDeviceDeviceProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

