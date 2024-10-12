# TwilioVerify.VerifyV2ServiceApi

All URIs are relative to *https://verify.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createService**](VerifyV2ServiceApi.md#createService) | **POST** /v2/Services | 
[**deleteService**](VerifyV2ServiceApi.md#deleteService) | **DELETE** /v2/Services/{Sid} | 
[**fetchService**](VerifyV2ServiceApi.md#fetchService) | **GET** /v2/Services/{Sid} | 
[**listService**](VerifyV2ServiceApi.md#listService) | **GET** /v2/Services | 
[**updateService**](VerifyV2ServiceApi.md#updateService) | **POST** /v2/Services/{Sid} | 



## createService

> VerifyV2Service createService(friendlyName, opts)



Create a new Verification Service.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2ServiceApi();
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the verification service. It can be up to 32 characters long. **This value should not contain PII.**
let opts = {
  'codeLength': 56, // Number | The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive.
  'customCodeEnabled': true, // Boolean | Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers.
  'defaultTemplateSid': "defaultTemplateSid_example", // String | The default message [template](https://www.twilio.com/docs/verify/api/templates). Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
  'doNotShareWarningEnabled': true, // Boolean | Whether to add a security warning at the end of an SMS verification body. Disabled by default and applies only to SMS. Example SMS body: `Your AppName verification code is: 1234. Don’t share this code with anyone; our employees will never ask for the code`
  'dtmfInputRequired': true, // Boolean | Whether to ask the user to press a number before delivering the verify code in a phone call.
  'lookupEnabled': true, // Boolean | Whether to perform a lookup with each verification started and return info about the phone number.
  'psd2Enabled': true, // Boolean | Whether to pass PSD2 transaction parameters when starting a verification.
  'pushApnCredentialSid': "pushApnCredentialSid_example", // String | Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
  'pushFcmCredentialSid': "pushFcmCredentialSid_example", // String | Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
  'pushIncludeDate': true, // Boolean | Optional configuration for the Push factors. If true, include the date in the Challenge's response. Otherwise, the date is omitted from the response. See [Challenge](https://www.twilio.com/docs/verify/api/challenge) resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter. This timestamp value is the same one as the one found in `date_created`, please use that one instead.
  'skipSmsToLandlines': true, // Boolean | Whether to skip sending SMS verifications to landlines. Requires `lookup_enabled`.
  'totpCodeLength': 56, // Number | Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6
  'totpIssuer': "totpIssuer_example", // String | Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI. Defaults to the service friendly name if not provided.
  'totpSkew': 56, // Number | Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
  'totpTimeStep': 56, // Number | Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds
  'ttsName': "ttsName_example", // String | The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages.
  'verifyEventSubscriptionEnabled': true // Boolean | Whether to allow verifications from the service to reach the stream-events sinks if configured
};
apiInstance.createService(friendlyName, opts, (error, data, response) => {
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
 **friendlyName** | **String**| A descriptive string that you create to describe the verification service. It can be up to 32 characters long. **This value should not contain PII.** | 
 **codeLength** | **Number**| The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive. | [optional] 
 **customCodeEnabled** | **Boolean**| Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers. | [optional] 
 **defaultTemplateSid** | **String**| The default message [template](https://www.twilio.com/docs/verify/api/templates). Will be used for all SMS verifications unless explicitly overriden. SMS channel only. | [optional] 
 **doNotShareWarningEnabled** | **Boolean**| Whether to add a security warning at the end of an SMS verification body. Disabled by default and applies only to SMS. Example SMS body: &#x60;Your AppName verification code is: 1234. Don’t share this code with anyone; our employees will never ask for the code&#x60; | [optional] 
 **dtmfInputRequired** | **Boolean**| Whether to ask the user to press a number before delivering the verify code in a phone call. | [optional] 
 **lookupEnabled** | **Boolean**| Whether to perform a lookup with each verification started and return info about the phone number. | [optional] 
 **psd2Enabled** | **Boolean**| Whether to pass PSD2 transaction parameters when starting a verification. | [optional] 
 **pushApnCredentialSid** | **String**| Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource) | [optional] 
 **pushFcmCredentialSid** | **String**| Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource) | [optional] 
 **pushIncludeDate** | **Boolean**| Optional configuration for the Push factors. If true, include the date in the Challenge&#39;s response. Otherwise, the date is omitted from the response. See [Challenge](https://www.twilio.com/docs/verify/api/challenge) resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter. This timestamp value is the same one as the one found in &#x60;date_created&#x60;, please use that one instead. | [optional] 
 **skipSmsToLandlines** | **Boolean**| Whether to skip sending SMS verifications to landlines. Requires &#x60;lookup_enabled&#x60;. | [optional] 
 **totpCodeLength** | **Number**| Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6 | [optional] 
 **totpIssuer** | **String**| Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI. Defaults to the service friendly name if not provided. | [optional] 
 **totpSkew** | **Number**| Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1 | [optional] 
 **totpTimeStep** | **Number**| Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds | [optional] 
 **ttsName** | **String**| The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages. | [optional] 
 **verifyEventSubscriptionEnabled** | **Boolean**| Whether to allow verifications from the service to reach the stream-events sinks if configured | [optional] 

### Return type

[**VerifyV2Service**](VerifyV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteService

> deleteService(sid)



Delete a specific Verification Service Instance.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2ServiceApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Verification Service resource to delete.
apiInstance.deleteService(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Verification Service resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchService

> VerifyV2Service fetchService(sid)



Fetch specific Verification Service Instance.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2ServiceApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Verification Service resource to fetch.
apiInstance.fetchService(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Verification Service resource to fetch. | 

### Return type

[**VerifyV2Service**](VerifyV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listService

> ListServiceResponse listService(opts)



Retrieve a list of all Verification Services for an account.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2ServiceApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listService(opts, (error, data, response) => {
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

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateService

> VerifyV2Service updateService(sid, opts)



Update a specific Verification Service.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2ServiceApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to update.
let opts = {
  'codeLength': 56, // Number | The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive.
  'customCodeEnabled': true, // Boolean | Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers.
  'defaultTemplateSid': "defaultTemplateSid_example", // String | The default message [template](https://www.twilio.com/docs/verify/api/templates). Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
  'doNotShareWarningEnabled': true, // Boolean | Whether to add a privacy warning at the end of an SMS. **Disabled by default and applies only for SMS.**
  'dtmfInputRequired': true, // Boolean | Whether to ask the user to press a number before delivering the verify code in a phone call.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the verification service. It can be up to 32 characters long. **This value should not contain PII.**
  'lookupEnabled': true, // Boolean | Whether to perform a lookup with each verification started and return info about the phone number.
  'psd2Enabled': true, // Boolean | Whether to pass PSD2 transaction parameters when starting a verification.
  'pushApnCredentialSid': "pushApnCredentialSid_example", // String | Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
  'pushFcmCredentialSid': "pushFcmCredentialSid_example", // String | Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
  'pushIncludeDate': true, // Boolean | Optional configuration for the Push factors. If true, include the date in the Challenge's response. Otherwise, the date is omitted from the response. See [Challenge](https://www.twilio.com/docs/verify/api/challenge) resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter.
  'skipSmsToLandlines': true, // Boolean | Whether to skip sending SMS verifications to landlines. Requires `lookup_enabled`.
  'totpCodeLength': 56, // Number | Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6
  'totpIssuer': "totpIssuer_example", // String | Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI.
  'totpSkew': 56, // Number | Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
  'totpTimeStep': 56, // Number | Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds
  'ttsName': "ttsName_example", // String | The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages.
  'verifyEventSubscriptionEnabled': true // Boolean | Whether to allow verifications from the service to reach the stream-events sinks if configured
};
apiInstance.updateService(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to update. | 
 **codeLength** | **Number**| The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive. | [optional] 
 **customCodeEnabled** | **Boolean**| Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers. | [optional] 
 **defaultTemplateSid** | **String**| The default message [template](https://www.twilio.com/docs/verify/api/templates). Will be used for all SMS verifications unless explicitly overriden. SMS channel only. | [optional] 
 **doNotShareWarningEnabled** | **Boolean**| Whether to add a privacy warning at the end of an SMS. **Disabled by default and applies only for SMS.** | [optional] 
 **dtmfInputRequired** | **Boolean**| Whether to ask the user to press a number before delivering the verify code in a phone call. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the verification service. It can be up to 32 characters long. **This value should not contain PII.** | [optional] 
 **lookupEnabled** | **Boolean**| Whether to perform a lookup with each verification started and return info about the phone number. | [optional] 
 **psd2Enabled** | **Boolean**| Whether to pass PSD2 transaction parameters when starting a verification. | [optional] 
 **pushApnCredentialSid** | **String**| Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource) | [optional] 
 **pushFcmCredentialSid** | **String**| Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource) | [optional] 
 **pushIncludeDate** | **Boolean**| Optional configuration for the Push factors. If true, include the date in the Challenge&#39;s response. Otherwise, the date is omitted from the response. See [Challenge](https://www.twilio.com/docs/verify/api/challenge) resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter. | [optional] 
 **skipSmsToLandlines** | **Boolean**| Whether to skip sending SMS verifications to landlines. Requires &#x60;lookup_enabled&#x60;. | [optional] 
 **totpCodeLength** | **Number**| Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6 | [optional] 
 **totpIssuer** | **String**| Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI. | [optional] 
 **totpSkew** | **Number**| Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1 | [optional] 
 **totpTimeStep** | **Number**| Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds | [optional] 
 **ttsName** | **String**| The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages. | [optional] 
 **verifyEventSubscriptionEnabled** | **Boolean**| Whether to allow verifications from the service to reach the stream-events sinks if configured | [optional] 

### Return type

[**VerifyV2Service**](VerifyV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

