# TwilioMicrovisor.MicrovisorV1DeviceConfigApi

All URIs are relative to *https://microvisor.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDeviceConfig**](MicrovisorV1DeviceConfigApi.md#createDeviceConfig) | **POST** /v1/Devices/{DeviceSid}/Configs | 
[**deleteDeviceConfig**](MicrovisorV1DeviceConfigApi.md#deleteDeviceConfig) | **DELETE** /v1/Devices/{DeviceSid}/Configs/{Key} | 
[**fetchDeviceConfig**](MicrovisorV1DeviceConfigApi.md#fetchDeviceConfig) | **GET** /v1/Devices/{DeviceSid}/Configs/{Key} | 
[**listDeviceConfig**](MicrovisorV1DeviceConfigApi.md#listDeviceConfig) | **GET** /v1/Devices/{DeviceSid}/Configs | 
[**updateDeviceConfig**](MicrovisorV1DeviceConfigApi.md#updateDeviceConfig) | **POST** /v1/Devices/{DeviceSid}/Configs/{Key} | 



## createDeviceConfig

> MicrovisorV1DeviceDeviceConfig createDeviceConfig(deviceSid, key, value)



Create a config for a Microvisor Device.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1DeviceConfigApi();
let deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
let key = "key_example"; // String | The config key; up to 100 characters.
let value = "value_example"; // String | The config value; up to 4096 characters.
apiInstance.createDeviceConfig(deviceSid, key, value, (error, data, response) => {
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
 **deviceSid** | **String**| A 34-character string that uniquely identifies the Device. | 
 **key** | **String**| The config key; up to 100 characters. | 
 **value** | **String**| The config value; up to 4096 characters. | 

### Return type

[**MicrovisorV1DeviceDeviceConfig**](MicrovisorV1DeviceDeviceConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteDeviceConfig

> deleteDeviceConfig(deviceSid, key)



Delete a config for a Microvisor Device.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1DeviceConfigApi();
let deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
let key = "key_example"; // String | The config key; up to 100 characters.
apiInstance.deleteDeviceConfig(deviceSid, key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceSid** | **String**| A 34-character string that uniquely identifies the Device. | 
 **key** | **String**| The config key; up to 100 characters. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchDeviceConfig

> MicrovisorV1DeviceDeviceConfig fetchDeviceConfig(deviceSid, key)



Retrieve a Config for a Device.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1DeviceConfigApi();
let deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
let key = "key_example"; // String | The config key; up to 100 characters.
apiInstance.fetchDeviceConfig(deviceSid, key, (error, data, response) => {
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
 **deviceSid** | **String**| A 34-character string that uniquely identifies the Device. | 
 **key** | **String**| The config key; up to 100 characters. | 

### Return type

[**MicrovisorV1DeviceDeviceConfig**](MicrovisorV1DeviceDeviceConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeviceConfig

> ListDeviceConfigResponse listDeviceConfig(deviceSid, opts)



Retrieve a list of all Configs for a Device.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1DeviceConfigApi();
let deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDeviceConfig(deviceSid, opts, (error, data, response) => {
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
 **deviceSid** | **String**| A 34-character string that uniquely identifies the Device. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListDeviceConfigResponse**](ListDeviceConfigResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeviceConfig

> MicrovisorV1DeviceDeviceConfig updateDeviceConfig(deviceSid, key, value)



Update a config for a Microvisor Device.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1DeviceConfigApi();
let deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
let key = "key_example"; // String | The config key; up to 100 characters.
let value = "value_example"; // String | The config value; up to 4096 characters.
apiInstance.updateDeviceConfig(deviceSid, key, value, (error, data, response) => {
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
 **deviceSid** | **String**| A 34-character string that uniquely identifies the Device. | 
 **key** | **String**| The config key; up to 100 characters. | 
 **value** | **String**| The config value; up to 4096 characters. | 

### Return type

[**MicrovisorV1DeviceDeviceConfig**](MicrovisorV1DeviceDeviceConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

