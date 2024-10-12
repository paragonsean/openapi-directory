# MerakiDashboardApi.LiveToolsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blinkDeviceLeds_0**](LiveToolsApi.md#blinkDeviceLeds_0) | **POST** /devices/{serial}/blinkLeds | Blink the LEDs on a device
[**createDeviceLiveToolsPingDevice_0**](LiveToolsApi.md#createDeviceLiveToolsPingDevice_0) | **POST** /devices/{serial}/liveTools/pingDevice | Enqueue a job to check connectivity status to the device
[**createDeviceLiveToolsPing_0**](LiveToolsApi.md#createDeviceLiveToolsPing_0) | **POST** /devices/{serial}/liveTools/ping | Enqueue a job to ping a target host from the device
[**cycleDeviceSwitchPorts_0**](LiveToolsApi.md#cycleDeviceSwitchPorts_0) | **POST** /devices/{serial}/switch/ports/cycle | Cycle a set of switch ports
[**getDeviceLiveToolsPingDevice_0**](LiveToolsApi.md#getDeviceLiveToolsPingDevice_0) | **GET** /devices/{serial}/liveTools/pingDevice/{id} | Return a ping device job
[**getDeviceLiveToolsPing_0**](LiveToolsApi.md#getDeviceLiveToolsPing_0) | **GET** /devices/{serial}/liveTools/ping/{id} | Return a ping job
[**rebootDevice_0**](LiveToolsApi.md#rebootDevice_0) | **POST** /devices/{serial}/reboot | Reboot a device



## blinkDeviceLeds_0

> Object blinkDeviceLeds_0(serial, opts)

Blink the LEDs on a device

Blink the LEDs on a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LiveToolsApi();
let serial = "serial_example"; // String | 
let opts = {
  'blinkDeviceLedsRequest': new MerakiDashboardApi.BlinkDeviceLedsRequest() // BlinkDeviceLedsRequest | 
};
apiInstance.blinkDeviceLeds_0(serial, opts, (error, data, response) => {
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
 **blinkDeviceLedsRequest** | [**BlinkDeviceLedsRequest**](BlinkDeviceLedsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDeviceLiveToolsPingDevice_0

> CreateDeviceLiveToolsPing201Response createDeviceLiveToolsPingDevice_0(serial, opts)

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

let apiInstance = new MerakiDashboardApi.LiveToolsApi();
let serial = "serial_example"; // String | 
let opts = {
  'createDeviceLiveToolsPingDeviceRequest': new MerakiDashboardApi.CreateDeviceLiveToolsPingDeviceRequest() // CreateDeviceLiveToolsPingDeviceRequest | 
};
apiInstance.createDeviceLiveToolsPingDevice_0(serial, opts, (error, data, response) => {
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


## createDeviceLiveToolsPing_0

> CreateDeviceLiveToolsPing201Response createDeviceLiveToolsPing_0(serial, createDeviceLiveToolsPingRequest)

Enqueue a job to ping a target host from the device

Enqueue a job to ping a target host from the device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LiveToolsApi();
let serial = "serial_example"; // String | 
let createDeviceLiveToolsPingRequest = new MerakiDashboardApi.CreateDeviceLiveToolsPingRequest(); // CreateDeviceLiveToolsPingRequest | 
apiInstance.createDeviceLiveToolsPing_0(serial, createDeviceLiveToolsPingRequest, (error, data, response) => {
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
 **createDeviceLiveToolsPingRequest** | [**CreateDeviceLiveToolsPingRequest**](CreateDeviceLiveToolsPingRequest.md)|  | 

### Return type

[**CreateDeviceLiveToolsPing201Response**](CreateDeviceLiveToolsPing201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cycleDeviceSwitchPorts_0

> Object cycleDeviceSwitchPorts_0(serial, cycleDeviceSwitchPortsRequest)

Cycle a set of switch ports

Cycle a set of switch ports

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LiveToolsApi();
let serial = "serial_example"; // String | 
let cycleDeviceSwitchPortsRequest = new MerakiDashboardApi.CycleDeviceSwitchPortsRequest(); // CycleDeviceSwitchPortsRequest | 
apiInstance.cycleDeviceSwitchPorts_0(serial, cycleDeviceSwitchPortsRequest, (error, data, response) => {
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
 **cycleDeviceSwitchPortsRequest** | [**CycleDeviceSwitchPortsRequest**](CycleDeviceSwitchPortsRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDeviceLiveToolsPingDevice_0

> GetDeviceLiveToolsPing200Response getDeviceLiveToolsPingDevice_0(serial, id)

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

let apiInstance = new MerakiDashboardApi.LiveToolsApi();
let serial = "serial_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getDeviceLiveToolsPingDevice_0(serial, id, (error, data, response) => {
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


## getDeviceLiveToolsPing_0

> GetDeviceLiveToolsPing200Response getDeviceLiveToolsPing_0(serial, id)

Return a ping job

Return a ping job. Latency unit in response is in milliseconds. Size is in bytes.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LiveToolsApi();
let serial = "serial_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getDeviceLiveToolsPing_0(serial, id, (error, data, response) => {
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


## rebootDevice_0

> Object rebootDevice_0(serial)

Reboot a device

Reboot a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LiveToolsApi();
let serial = "serial_example"; // String | 
apiInstance.rebootDevice_0(serial, (error, data, response) => {
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

