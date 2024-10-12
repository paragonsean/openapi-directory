# MerakiDashboardApi.MGLANSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceCellularGatewaySettings**](MGLANSettingsApi.md#getDeviceCellularGatewaySettings) | **GET** /devices/{serial}/cellularGateway/settings | Show the LAN Settings of a MG
[**updateDeviceCellularGatewaySettings**](MGLANSettingsApi.md#updateDeviceCellularGatewaySettings) | **PUT** /devices/{serial}/cellularGateway/settings | Update the LAN Settings for a single MG.



## getDeviceCellularGatewaySettings

> Object getDeviceCellularGatewaySettings(serial)

Show the LAN Settings of a MG

Show the LAN Settings of a MG

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MGLANSettingsApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCellularGatewaySettings(serial, (error, data, response) => {
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


## updateDeviceCellularGatewaySettings

> Object updateDeviceCellularGatewaySettings(serial, opts)

Update the LAN Settings for a single MG.

Update the LAN Settings for a single MG.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MGLANSettingsApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCellularGatewaySettingsRequest': new MerakiDashboardApi.UpdateDeviceCellularGatewaySettingsRequest() // UpdateDeviceCellularGatewaySettingsRequest | 
};
apiInstance.updateDeviceCellularGatewaySettings(serial, opts, (error, data, response) => {
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
 **updateDeviceCellularGatewaySettingsRequest** | [**UpdateDeviceCellularGatewaySettingsRequest**](UpdateDeviceCellularGatewaySettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

