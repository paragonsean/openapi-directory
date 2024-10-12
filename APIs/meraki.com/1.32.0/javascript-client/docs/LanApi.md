# MerakiDashboardApi.LanApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceCellularGatewayLan_1**](LanApi.md#getDeviceCellularGatewayLan_1) | **GET** /devices/{serial}/cellularGateway/lan | Show the LAN Settings of a MG
[**updateDeviceCellularGatewayLan_1**](LanApi.md#updateDeviceCellularGatewayLan_1) | **PUT** /devices/{serial}/cellularGateway/lan | Update the LAN Settings for a single MG.



## getDeviceCellularGatewayLan_1

> Object getDeviceCellularGatewayLan_1(serial)

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

let apiInstance = new MerakiDashboardApi.LanApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCellularGatewayLan_1(serial, (error, data, response) => {
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


## updateDeviceCellularGatewayLan_1

> Object updateDeviceCellularGatewayLan_1(serial, opts)

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

let apiInstance = new MerakiDashboardApi.LanApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCellularGatewayLanRequest': new MerakiDashboardApi.UpdateDeviceCellularGatewayLanRequest() // UpdateDeviceCellularGatewayLanRequest | 
};
apiInstance.updateDeviceCellularGatewayLan_1(serial, opts, (error, data, response) => {
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
 **updateDeviceCellularGatewayLanRequest** | [**UpdateDeviceCellularGatewayLanRequest**](UpdateDeviceCellularGatewayLanRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

