# TwilioVoice.VoiceV1SettingsApi

All URIs are relative to *https://voice.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchDialingPermissionsSettings**](VoiceV1SettingsApi.md#fetchDialingPermissionsSettings) | **GET** /v1/Settings | 
[**updateDialingPermissionsSettings**](VoiceV1SettingsApi.md#updateDialingPermissionsSettings) | **POST** /v1/Settings | 



## fetchDialingPermissionsSettings

> VoiceV1DialingPermissionsDialingPermissionsSettings fetchDialingPermissionsSettings()



Retrieve voice dialing permissions inheritance for the sub-account

### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1SettingsApi();
apiInstance.fetchDialingPermissionsSettings((error, data, response) => {
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

[**VoiceV1DialingPermissionsDialingPermissionsSettings**](VoiceV1DialingPermissionsDialingPermissionsSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDialingPermissionsSettings

> VoiceV1DialingPermissionsDialingPermissionsSettings updateDialingPermissionsSettings(opts)



Update voice dialing permissions inheritance for the sub-account

### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1SettingsApi();
let opts = {
  'dialingPermissionsInheritance': true // Boolean | `true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.
};
apiInstance.updateDialingPermissionsSettings(opts, (error, data, response) => {
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
 **dialingPermissionsInheritance** | **Boolean**| &#x60;true&#x60; for the sub-account to inherit voice dialing permissions from the Master Project; otherwise &#x60;false&#x60;. | [optional] 

### Return type

[**VoiceV1DialingPermissionsDialingPermissionsSettings**](VoiceV1DialingPermissionsDialingPermissionsSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

