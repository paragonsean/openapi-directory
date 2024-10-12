# PacControlRestApi.DeviceApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**readDeviceDetails_0**](DeviceApi.md#readDeviceDetails_0) | **GET** /device | 



## readDeviceDetails_0

> ControllerResponse readDeviceDetails_0()



Returns controller&#39;s type; firmware version; both mac addresses; and uptime in seconds

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.DeviceApi();
apiInstance.readDeviceDetails_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ControllerResponse**](ControllerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

