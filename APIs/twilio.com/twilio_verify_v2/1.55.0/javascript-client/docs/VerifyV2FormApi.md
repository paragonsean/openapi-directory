# TwilioVerify.VerifyV2FormApi

All URIs are relative to *https://verify.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchForm**](VerifyV2FormApi.md#fetchForm) | **GET** /v2/Forms/{FormType} | 



## fetchForm

> VerifyV2Form fetchForm(formType)



Fetch the forms for a specific Form Type.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2FormApi();
let formType = "formType_example"; // FormEnumFormTypes | The Type of this Form. Currently only `form-push` is supported.
apiInstance.fetchForm(formType, (error, data, response) => {
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
 **formType** | **FormEnumFormTypes**| The Type of this Form. Currently only &#x60;form-push&#x60; is supported. | 

### Return type

[**VerifyV2Form**](VerifyV2Form.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

