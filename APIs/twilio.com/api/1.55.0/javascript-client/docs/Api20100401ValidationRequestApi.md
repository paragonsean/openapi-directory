# TwilioApi.Api20100401ValidationRequestApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createValidationRequest**](Api20100401ValidationRequestApi.md#createValidationRequest) | **POST** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds.json | 



## createValidationRequest

> ApiV2010AccountValidationRequest createValidationRequest(accountSid, phoneNumber, opts)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401ValidationRequestApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for the new caller ID resource.
let phoneNumber = "phoneNumber_example"; // String | The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
let opts = {
  'callDelay': 56, // Number | The number of seconds to delay before initiating the verification call. Can be an integer between `0` and `60`, inclusive. The default is `0`.
  'extension': "extension_example", // String | The digits to dial after connecting the verification call.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the new caller ID resource. It can be up to 64 characters long. The default value is a formatted version of the phone number.
  'statusCallback': "statusCallback_example", // String | The URL we should call using the `status_callback_method` to send status information about the verification process to your application.
  'statusCallbackMethod': "statusCallbackMethod_example" // String | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`, and the default is `POST`.
};
apiInstance.createValidationRequest(accountSid, phoneNumber, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for the new caller ID resource. | 
 **phoneNumber** | **String**| The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number. | 
 **callDelay** | **Number**| The number of seconds to delay before initiating the verification call. Can be an integer between &#x60;0&#x60; and &#x60;60&#x60;, inclusive. The default is &#x60;0&#x60;. | [optional] 
 **extension** | **String**| The digits to dial after connecting the verification call. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the new caller ID resource. It can be up to 64 characters long. The default value is a formatted version of the phone number. | [optional] 
 **statusCallback** | **String**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information about the verification process to your application. | [optional] 
 **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;, and the default is &#x60;POST&#x60;. | [optional] 

### Return type

[**ApiV2010AccountValidationRequest**](ApiV2010AccountValidationRequest.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

