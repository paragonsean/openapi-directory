# TwilioMicrovisor.MicrovisorV1DeviceSecretApi

All URIs are relative to *https://microvisor.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDeviceSecret**](MicrovisorV1DeviceSecretApi.md#createDeviceSecret) | **POST** /v1/Devices/{DeviceSid}/Secrets | 
[**deleteDeviceSecret**](MicrovisorV1DeviceSecretApi.md#deleteDeviceSecret) | **DELETE** /v1/Devices/{DeviceSid}/Secrets/{Key} | 
[**fetchDeviceSecret**](MicrovisorV1DeviceSecretApi.md#fetchDeviceSecret) | **GET** /v1/Devices/{DeviceSid}/Secrets/{Key} | 
[**listDeviceSecret**](MicrovisorV1DeviceSecretApi.md#listDeviceSecret) | **GET** /v1/Devices/{DeviceSid}/Secrets | 
[**updateDeviceSecret**](MicrovisorV1DeviceSecretApi.md#updateDeviceSecret) | **POST** /v1/Devices/{DeviceSid}/Secrets/{Key} | 



## createDeviceSecret

> MicrovisorV1DeviceDeviceSecret createDeviceSecret(deviceSid, key, value)



Create a secret for a Microvisor Device.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1DeviceSecretApi();
let deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
let key = "key_example"; // String | The secret key; up to 100 characters.
let value = "value_example"; // String | The secret value; up to 4096 characters.
apiInstance.createDeviceSecret(deviceSid, key, value, (error, data, response) => {
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
 **key** | **String**| The secret key; up to 100 characters. | 
 **value** | **String**| The secret value; up to 4096 characters. | 

### Return type

[**MicrovisorV1DeviceDeviceSecret**](MicrovisorV1DeviceDeviceSecret.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteDeviceSecret

> deleteDeviceSecret(deviceSid, key)



Delete a secret for a Microvisor Device.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1DeviceSecretApi();
let deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
let key = "key_example"; // String | The secret key; up to 100 characters.
apiInstance.deleteDeviceSecret(deviceSid, key, (error, data, response) => {
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
 **key** | **String**| The secret key; up to 100 characters. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchDeviceSecret

> MicrovisorV1DeviceDeviceSecret fetchDeviceSecret(deviceSid, key)



Retrieve a Secret for a Device.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1DeviceSecretApi();
let deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
let key = "key_example"; // String | The secret key; up to 100 characters.
apiInstance.fetchDeviceSecret(deviceSid, key, (error, data, response) => {
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
 **key** | **String**| The secret key; up to 100 characters. | 

### Return type

[**MicrovisorV1DeviceDeviceSecret**](MicrovisorV1DeviceDeviceSecret.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeviceSecret

> ListDeviceSecretResponse listDeviceSecret(deviceSid, opts)



Retrieve a list of all Secrets for a Device.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1DeviceSecretApi();
let deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDeviceSecret(deviceSid, opts, (error, data, response) => {
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

[**ListDeviceSecretResponse**](ListDeviceSecretResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeviceSecret

> MicrovisorV1DeviceDeviceSecret updateDeviceSecret(deviceSid, key, value)



Update a secret for a Microvisor Device.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1DeviceSecretApi();
let deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
let key = "key_example"; // String | The secret key; up to 100 characters.
let value = "value_example"; // String | The secret value; up to 4096 characters.
apiInstance.updateDeviceSecret(deviceSid, key, value, (error, data, response) => {
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
 **key** | **String**| The secret key; up to 100 characters. | 
 **value** | **String**| The secret value; up to 4096 characters. | 

### Return type

[**MicrovisorV1DeviceDeviceSecret**](MicrovisorV1DeviceDeviceSecret.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

