# FraudLabsProSmsVerification.DefaultApi

All URIs are relative to *https://api.fraudlabspro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1VerificationResultGet**](DefaultApi.md#v1VerificationResultGet) | **GET** /v1/verification/result | 
[**v1VerificationSendPost**](DefaultApi.md#v1VerificationSendPost) | **POST** /v1/verification/send | 



## v1VerificationResultGet

> String v1VerificationResultGet(tranId, key, otp, opts)



Verify that an OTP sent by the Send SMS Verification API is valid.

### Example

```javascript
import FraudLabsProSmsVerification from 'fraud_labs_pro_sms_verification';

let apiInstance = new FraudLabsProSmsVerification.DefaultApi();
let tranId = "tranId_example"; // String | The unique ID that was returned by the Send Verification SMS API that triggered the OTP sms.
let key = "key_example"; // String | FraudLabs Pro API key.
let otp = "otp_example"; // String | The OTP that was sent to the recipient’s phone.
let opts = {
  'format': "format_example" // String | Returns the API response in json (default) or xml format.
};
apiInstance.v1VerificationResultGet(tranId, key, otp, opts, (error, data, response) => {
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
 **tranId** | **String**| The unique ID that was returned by the Send Verification SMS API that triggered the OTP sms. | 
 **key** | **String**| FraudLabs Pro API key. | 
 **otp** | **String**| The OTP that was sent to the recipient’s phone. | 
 **format** | **String**| Returns the API response in json (default) or xml format. | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## v1VerificationSendPost

> String v1VerificationSendPost(tel, key, opts)



Send an SMS with verification code and a custom message for authentication purpose.

### Example

```javascript
import FraudLabsProSmsVerification from 'fraud_labs_pro_sms_verification';

let apiInstance = new FraudLabsProSmsVerification.DefaultApi();
let tel = "tel_example"; // String | The recipient mobile phone number in E164 format which is a plus followed by just numbers with no spaces or parentheses.
let key = "key_example"; // String | FraudLabs Pro API key.
let opts = {
  'countryCode': "countryCode_example", // String | ISO 3166 country code for the recipient mobile phone number. If parameter is supplied, then some basic telephone number validation is done.
  'format': "format_example", // String | Returns the API response in json (default) or xml format.
  'mesg': "mesg_example" // String | The message template for the SMS. Add <otp> as placeholder for the actual OTP to be generated. Max length is 140 characters.
};
apiInstance.v1VerificationSendPost(tel, key, opts, (error, data, response) => {
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
 **tel** | **String**| The recipient mobile phone number in E164 format which is a plus followed by just numbers with no spaces or parentheses. | 
 **key** | **String**| FraudLabs Pro API key. | 
 **countryCode** | **String**| ISO 3166 country code for the recipient mobile phone number. If parameter is supplied, then some basic telephone number validation is done. | [optional] 
 **format** | **String**| Returns the API response in json (default) or xml format. | [optional] 
 **mesg** | **String**| The message template for the SMS. Add &lt;otp&gt; as placeholder for the actual OTP to be generated. Max length is 140 characters. | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

