# MerakiDashboardApi.MGPortForwardingRulesApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceCellularGatewaySettingsPortForwardingRules**](MGPortForwardingRulesApi.md#getDeviceCellularGatewaySettingsPortForwardingRules) | **GET** /devices/{serial}/cellularGateway/settings/portForwardingRules | Returns the port forwarding rules for a single MG.
[**updateDeviceCellularGatewaySettingsPortForwardingRules**](MGPortForwardingRulesApi.md#updateDeviceCellularGatewaySettingsPortForwardingRules) | **PUT** /devices/{serial}/cellularGateway/settings/portForwardingRules | Updates the port forwarding rules for a single MG.



## getDeviceCellularGatewaySettingsPortForwardingRules

> Object getDeviceCellularGatewaySettingsPortForwardingRules(serial)

Returns the port forwarding rules for a single MG.

Returns the port forwarding rules for a single MG.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MGPortForwardingRulesApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCellularGatewaySettingsPortForwardingRules(serial, (error, data, response) => {
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


## updateDeviceCellularGatewaySettingsPortForwardingRules

> Object updateDeviceCellularGatewaySettingsPortForwardingRules(serial, opts)

Updates the port forwarding rules for a single MG.

Updates the port forwarding rules for a single MG.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MGPortForwardingRulesApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCellularGatewaySettingsPortForwardingRulesRequest': new MerakiDashboardApi.UpdateDeviceCellularGatewaySettingsPortForwardingRulesRequest() // UpdateDeviceCellularGatewaySettingsPortForwardingRulesRequest | 
};
apiInstance.updateDeviceCellularGatewaySettingsPortForwardingRules(serial, opts, (error, data, response) => {
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
 **updateDeviceCellularGatewaySettingsPortForwardingRulesRequest** | [**UpdateDeviceCellularGatewaySettingsPortForwardingRulesRequest**](UpdateDeviceCellularGatewaySettingsPortForwardingRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

