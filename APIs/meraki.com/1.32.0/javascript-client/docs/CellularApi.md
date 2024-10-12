# MerakiDashboardApi.CellularApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceCellularSims_1**](CellularApi.md#getDeviceCellularSims_1) | **GET** /devices/{serial}/cellular/sims | Return the SIM and APN configurations for a cellular device.
[**updateDeviceCellularSims_1**](CellularApi.md#updateDeviceCellularSims_1) | **PUT** /devices/{serial}/cellular/sims | Updates the SIM and APN configurations for a cellular device.



## getDeviceCellularSims_1

> Object getDeviceCellularSims_1(serial)

Return the SIM and APN configurations for a cellular device.

Return the SIM and APN configurations for a cellular device.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CellularApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCellularSims_1(serial, (error, data, response) => {
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


## updateDeviceCellularSims_1

> Object updateDeviceCellularSims_1(serial, opts)

Updates the SIM and APN configurations for a cellular device.

Updates the SIM and APN configurations for a cellular device.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CellularApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCellularSimsRequest': new MerakiDashboardApi.UpdateDeviceCellularSimsRequest() // UpdateDeviceCellularSimsRequest | 
};
apiInstance.updateDeviceCellularSims_1(serial, opts, (error, data, response) => {
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
 **updateDeviceCellularSimsRequest** | [**UpdateDeviceCellularSimsRequest**](UpdateDeviceCellularSimsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

