# MerakiDashboardApi.PingDeviceApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDeviceLiveToolsPingDevice_1**](PingDeviceApi.md#createDeviceLiveToolsPingDevice_1) | **POST** /devices/{serial}/liveTools/pingDevice | Enqueue a job to check connectivity status to the device
[**getDeviceLiveToolsPingDevice_1**](PingDeviceApi.md#getDeviceLiveToolsPingDevice_1) | **GET** /devices/{serial}/liveTools/pingDevice/{id} | Return a ping device job



## createDeviceLiveToolsPingDevice_1

> CreateDeviceLiveToolsPing201Response createDeviceLiveToolsPingDevice_1(serial, opts)

Enqueue a job to check connectivity status to the device

Enqueue a job to check connectivity status to the device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PingDeviceApi();
let serial = "serial_example"; // String | 
let opts = {
  'createDeviceLiveToolsPingDeviceRequest': new MerakiDashboardApi.CreateDeviceLiveToolsPingDeviceRequest() // CreateDeviceLiveToolsPingDeviceRequest | 
};
apiInstance.createDeviceLiveToolsPingDevice_1(serial, opts, (error, data, response) => {
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
 **createDeviceLiveToolsPingDeviceRequest** | [**CreateDeviceLiveToolsPingDeviceRequest**](CreateDeviceLiveToolsPingDeviceRequest.md)|  | [optional] 

### Return type

[**CreateDeviceLiveToolsPing201Response**](CreateDeviceLiveToolsPing201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDeviceLiveToolsPingDevice_1

> GetDeviceLiveToolsPing200Response getDeviceLiveToolsPingDevice_1(serial, id)

Return a ping device job

Return a ping device job. Latency unit in response is in milliseconds. Size is in bytes.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PingDeviceApi();
let serial = "serial_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getDeviceLiveToolsPingDevice_1(serial, id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**GetDeviceLiveToolsPing200Response**](GetDeviceLiveToolsPing200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

