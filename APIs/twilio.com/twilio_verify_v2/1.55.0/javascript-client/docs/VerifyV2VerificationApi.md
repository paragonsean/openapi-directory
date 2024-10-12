# TwilioVerify.VerifyV2VerificationApi

All URIs are relative to *https://verify.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createVerification**](VerifyV2VerificationApi.md#createVerification) | **POST** /v2/Services/{ServiceSid}/Verifications | 
[**fetchVerification**](VerifyV2VerificationApi.md#fetchVerification) | **GET** /v2/Services/{ServiceSid}/Verifications/{Sid} | 
[**updateVerification**](VerifyV2VerificationApi.md#updateVerification) | **POST** /v2/Services/{ServiceSid}/Verifications/{Sid} | 



## createVerification

> VerifyV2ServiceVerification createVerification(serviceSid, channel, to, opts)



Create a new Verification using a Service

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2VerificationApi();
let serviceSid = "serviceSid_example"; // String | The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to create the resource under.
let channel = "channel_example"; // String | The verification method to use. One of: [`email`](https://www.twilio.com/docs/verify/email), `sms`, `whatsapp`, `call`, `sna` or `auto`.
let to = "to_example"; // String | The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
let opts = {
  'amount': "amount_example", // String | The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
  'appHash': "appHash_example", // String | Your [App Hash](https://developers.google.com/identity/sms-retriever/verify#computing_your_apps_hash_string) to be appended at the end of your verification SMS body. Applies only to SMS. Example SMS body: `<#> Your AppName verification code is: 1234 He42w354ol9`.
  'channelConfiguration': null, // Object | [`email`](https://www.twilio.com/docs/verify/email) channel configuration in json format. The fields 'from' and 'from_name' are optional but if included the 'from' field must have a valid email address.
  'customCode': "customCode_example", // String | A pre-generated code to use for verification. The code can be between 4 and 10 characters, inclusive.
  'customFriendlyName': "customFriendlyName_example", // String | A custom user defined friendly name that overwrites the existing one in the verification message
  'customMessage': "customMessage_example", // String | The text of a custom message to use for the verification.
  'deviceIp': "deviceIp_example", // String | Strongly encouraged if using the auto channel. The IP address of the client's device. If provided, it has to be a valid IPv4 or IPv6 address.
  'locale': "locale_example", // String | Locale will automatically resolve based on phone number country code for SMS, WhatsApp, and call channel verifications. It will fallback to English or the template’s default translation if the selected translation is not available. This parameter will override the automatic locale resolution. [See supported languages and more information here](https://www.twilio.com/docs/verify/supported-languages).
  'payee': "payee_example", // String | The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
  'rateLimits': null, // Object | The custom key-value pairs of Programmable Rate Limits. Keys correspond to `unique_name` fields defined when [creating your Rate Limit](https://www.twilio.com/docs/verify/api/service-rate-limits). Associated value pairs represent values in the request that you are rate limiting on. You may include multiple Rate Limit values in each request.
  'riskCheck': "riskCheck_example", // VerificationEnumRiskCheck | 
  'sendDigits': "sendDigits_example", // String | The digits to send after a phone call is answered, for example, to dial an extension. For more information, see the Programmable Voice documentation of [sendDigits](https://www.twilio.com/docs/voice/twiml/number#attributes-sendDigits).
  'tags': "tags_example", // String | A string containing a JSON map of key value pairs of tags to be recorded as metadata for the message. The object may contain up to 10 tags. Keys and values can each be up to 128 characters in length.
  'templateCustomSubstitutions': "templateCustomSubstitutions_example", // String | A stringified JSON object in which the keys are the template's special variables and the values are the variables substitutions.
  'templateSid': "templateSid_example" // String | The message [template](https://www.twilio.com/docs/verify/api/templates). If provided, will override the default template for the Service. SMS and Voice channels only.
};
apiInstance.createVerification(serviceSid, channel, to, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to create the resource under. | 
 **channel** | **String**| The verification method to use. One of: [&#x60;email&#x60;](https://www.twilio.com/docs/verify/email), &#x60;sms&#x60;, &#x60;whatsapp&#x60;, &#x60;call&#x60;, &#x60;sna&#x60; or &#x60;auto&#x60;. | 
 **to** | **String**| The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164). | 
 **amount** | **String**| The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled. | [optional] 
 **appHash** | **String**| Your [App Hash](https://developers.google.com/identity/sms-retriever/verify#computing_your_apps_hash_string) to be appended at the end of your verification SMS body. Applies only to SMS. Example SMS body: &#x60;&lt;#&gt; Your AppName verification code is: 1234 He42w354ol9&#x60;. | [optional] 
 **channelConfiguration** | [**Object**](Object.md)| [&#x60;email&#x60;](https://www.twilio.com/docs/verify/email) channel configuration in json format. The fields &#39;from&#39; and &#39;from_name&#39; are optional but if included the &#39;from&#39; field must have a valid email address. | [optional] 
 **customCode** | **String**| A pre-generated code to use for verification. The code can be between 4 and 10 characters, inclusive. | [optional] 
 **customFriendlyName** | **String**| A custom user defined friendly name that overwrites the existing one in the verification message | [optional] 
 **customMessage** | **String**| The text of a custom message to use for the verification. | [optional] 
 **deviceIp** | **String**| Strongly encouraged if using the auto channel. The IP address of the client&#39;s device. If provided, it has to be a valid IPv4 or IPv6 address. | [optional] 
 **locale** | **String**| Locale will automatically resolve based on phone number country code for SMS, WhatsApp, and call channel verifications. It will fallback to English or the template’s default translation if the selected translation is not available. This parameter will override the automatic locale resolution. [See supported languages and more information here](https://www.twilio.com/docs/verify/supported-languages). | [optional] 
 **payee** | **String**| The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled. | [optional] 
 **rateLimits** | [**Object**](Object.md)| The custom key-value pairs of Programmable Rate Limits. Keys correspond to &#x60;unique_name&#x60; fields defined when [creating your Rate Limit](https://www.twilio.com/docs/verify/api/service-rate-limits). Associated value pairs represent values in the request that you are rate limiting on. You may include multiple Rate Limit values in each request. | [optional] 
 **riskCheck** | **VerificationEnumRiskCheck**|  | [optional] 
 **sendDigits** | **String**| The digits to send after a phone call is answered, for example, to dial an extension. For more information, see the Programmable Voice documentation of [sendDigits](https://www.twilio.com/docs/voice/twiml/number#attributes-sendDigits). | [optional] 
 **tags** | **String**| A string containing a JSON map of key value pairs of tags to be recorded as metadata for the message. The object may contain up to 10 tags. Keys and values can each be up to 128 characters in length. | [optional] 
 **templateCustomSubstitutions** | **String**| A stringified JSON object in which the keys are the template&#39;s special variables and the values are the variables substitutions. | [optional] 
 **templateSid** | **String**| The message [template](https://www.twilio.com/docs/verify/api/templates). If provided, will override the default template for the Service. SMS and Voice channels only. | [optional] 

### Return type

[**VerifyV2ServiceVerification**](VerifyV2ServiceVerification.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchVerification

> VerifyV2ServiceVerification fetchVerification(serviceSid, sid)



Fetch a specific Verification

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2VerificationApi();
let serviceSid = "serviceSid_example"; // String | The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to fetch the resource from.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Verification resource to fetch.
apiInstance.fetchVerification(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to fetch the resource from. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Verification resource to fetch. | 

### Return type

[**VerifyV2ServiceVerification**](VerifyV2ServiceVerification.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateVerification

> VerifyV2ServiceVerification updateVerification(serviceSid, sid, status)



Update a Verification status

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2VerificationApi();
let serviceSid = "serviceSid_example"; // String | The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to update the resource from.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Verification resource to update.
let status = "status_example"; // VerificationEnumStatus | 
apiInstance.updateVerification(serviceSid, sid, status, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to update the resource from. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Verification resource to update. | 
 **status** | **VerificationEnumStatus**|  | 

### Return type

[**VerifyV2ServiceVerification**](VerifyV2ServiceVerification.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

