# TwilioMessaging.MessagingV1BrandRegistrationOtpApi

All URIs are relative to *https://messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBrandRegistrationOtp**](MessagingV1BrandRegistrationOtpApi.md#createBrandRegistrationOtp) | **POST** /v1/a2p/BrandRegistrations/{BrandRegistrationSid}/SmsOtp | 



## createBrandRegistrationOtp

> MessagingV1BrandRegistrationsBrandRegistrationOtp createBrandRegistrationOtp(brandRegistrationSid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1BrandRegistrationOtpApi();
let brandRegistrationSid = "brandRegistrationSid_example"; // String | Brand Registration Sid of Sole Proprietor Brand.
apiInstance.createBrandRegistrationOtp(brandRegistrationSid, (error, data, response) => {
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
 **brandRegistrationSid** | **String**| Brand Registration Sid of Sole Proprietor Brand. | 

### Return type

[**MessagingV1BrandRegistrationsBrandRegistrationOtp**](MessagingV1BrandRegistrationsBrandRegistrationOtp.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

