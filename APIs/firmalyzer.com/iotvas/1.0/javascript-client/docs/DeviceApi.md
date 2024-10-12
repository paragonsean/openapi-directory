# IoTvasApi.DeviceApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detectDevice**](DeviceApi.md#detectDevice) | **POST** /device/detect | Detect iot device by service banners and mac address



## detectDevice

> DeviceInfo detectDevice(deviceFeatures)

Detect iot device by service banners and mac address

Use device service banners and mac address captured by your network port scanner, vulnerability assessment or asset discovery tools to detect device maker, model and firmware information

### Example

```javascript
import IoTvasApi from 'io_tvas_api';
let defaultClient = IoTvasApi.ApiClient.instance;
// Configure API key authorization: api-key-header
let api-key-header = defaultClient.authentications['api-key-header'];
api-key-header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key-header.apiKeyPrefix = 'Token';

let apiInstance = new IoTvasApi.DeviceApi();
let deviceFeatures = new IoTvasApi.DeviceFeatures(); // DeviceFeatures | 
apiInstance.detectDevice(deviceFeatures, (error, data, response) => {
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
 **deviceFeatures** | [**DeviceFeatures**](DeviceFeatures.md)|  | 

### Return type

[**DeviceInfo**](DeviceInfo.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

