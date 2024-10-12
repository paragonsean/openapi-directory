# MerakiDashboardApi.RadioApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceWirelessRadioSettings_1**](RadioApi.md#getDeviceWirelessRadioSettings_1) | **GET** /devices/{serial}/wireless/radio/settings | Return the radio settings of a device
[**updateDeviceWirelessRadioSettings_1**](RadioApi.md#updateDeviceWirelessRadioSettings_1) | **PUT** /devices/{serial}/wireless/radio/settings | Update the radio settings of a device



## getDeviceWirelessRadioSettings_1

> Object getDeviceWirelessRadioSettings_1(serial)

Return the radio settings of a device

Return the radio settings of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.RadioApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceWirelessRadioSettings_1(serial, (error, data, response) => {
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


## updateDeviceWirelessRadioSettings_1

> Object updateDeviceWirelessRadioSettings_1(serial, opts)

Update the radio settings of a device

Update the radio settings of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.RadioApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceWirelessRadioSettingsRequest': new MerakiDashboardApi.UpdateDeviceWirelessRadioSettingsRequest() // UpdateDeviceWirelessRadioSettingsRequest | 
};
apiInstance.updateDeviceWirelessRadioSettings_1(serial, opts, (error, data, response) => {
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
 **updateDeviceWirelessRadioSettingsRequest** | [**UpdateDeviceWirelessRadioSettingsRequest**](UpdateDeviceWirelessRadioSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

