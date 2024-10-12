# TwilioMicrovisor.MicrovisorV1DeviceApi

All URIs are relative to *https://microvisor.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchDevice**](MicrovisorV1DeviceApi.md#fetchDevice) | **GET** /v1/Devices/{Sid} | 
[**listDevice**](MicrovisorV1DeviceApi.md#listDevice) | **GET** /v1/Devices | 
[**updateDevice**](MicrovisorV1DeviceApi.md#updateDevice) | **POST** /v1/Devices/{Sid} | 



## fetchDevice

> MicrovisorV1Device fetchDevice(sid)



Fetch a specific Device.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1DeviceApi();
let sid = "sid_example"; // String | A 34-character string that uniquely identifies this Device.
apiInstance.fetchDevice(sid, (error, data, response) => {
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
 **sid** | **String**| A 34-character string that uniquely identifies this Device. | 

### Return type

[**MicrovisorV1Device**](MicrovisorV1Device.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDevice

> ListDeviceResponse listDevice(opts)



Retrieve a list of all Devices registered with the Account.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1DeviceApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDevice(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListDeviceResponse**](ListDeviceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDevice

> MicrovisorV1Device updateDevice(sid, opts)



Update a specific Device.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1DeviceApi();
let sid = "sid_example"; // String | A 34-character string that uniquely identifies this Device.
let opts = {
  'loggingEnabled': true, // Boolean | A Boolean flag specifying whether to enable application logging. Logs will be enabled or extended for 24 hours.
  'restartApp': true, // Boolean | Set to true to restart the App running on the Device.
  'targetApp': "targetApp_example", // String | The SID or unique name of the App to be targeted to the Device.
  'uniqueName': "uniqueName_example" // String | A unique and addressable name to be assigned to this Device by the developer. It may be used in place of the Device SID.
};
apiInstance.updateDevice(sid, opts, (error, data, response) => {
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
 **sid** | **String**| A 34-character string that uniquely identifies this Device. | 
 **loggingEnabled** | **Boolean**| A Boolean flag specifying whether to enable application logging. Logs will be enabled or extended for 24 hours. | [optional] 
 **restartApp** | **Boolean**| Set to true to restart the App running on the Device. | [optional] 
 **targetApp** | **String**| The SID or unique name of the App to be targeted to the Device. | [optional] 
 **uniqueName** | **String**| A unique and addressable name to be assigned to this Device by the developer. It may be used in place of the Device SID. | [optional] 

### Return type

[**MicrovisorV1Device**](MicrovisorV1Device.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

