# TwilioVerify.VerifyV2VerificationCheckApi

All URIs are relative to *https://verify.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createVerificationCheck**](VerifyV2VerificationCheckApi.md#createVerificationCheck) | **POST** /v2/Services/{ServiceSid}/VerificationCheck | 



## createVerificationCheck

> VerifyV2ServiceVerificationCheck createVerificationCheck(serviceSid, opts)



challenge a specific Verification Check.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2VerificationCheckApi();
let serviceSid = "serviceSid_example"; // String | The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to create the resource under.
let opts = {
  'amount': "amount_example", // String | The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
  'code': "code_example", // String | The 4-10 character string being verified.
  'payee': "payee_example", // String | The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
  'to': "to_example", // String | The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Either this parameter or the `verification_sid` must be specified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
  'verificationSid': "verificationSid_example" // String | A SID that uniquely identifies the Verification Check. Either this parameter or the `to` phone number/[email](https://www.twilio.com/docs/verify/email) must be specified.
};
apiInstance.createVerificationCheck(serviceSid, opts, (error, data, response) => {
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
 **amount** | **String**| The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled. | [optional] 
 **code** | **String**| The 4-10 character string being verified. | [optional] 
 **payee** | **String**| The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled. | [optional] 
 **to** | **String**| The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Either this parameter or the &#x60;verification_sid&#x60; must be specified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164). | [optional] 
 **verificationSid** | **String**| A SID that uniquely identifies the Verification Check. Either this parameter or the &#x60;to&#x60; phone number/[email](https://www.twilio.com/docs/verify/email) must be specified. | [optional] 

### Return type

[**VerifyV2ServiceVerificationCheck**](VerifyV2ServiceVerificationCheck.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

