# TwilioNumbers.NumbersV1PortingPortabilityApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchPortingPortability**](NumbersV1PortingPortabilityApi.md#fetchPortingPortability) | **GET** /v1/Porting/Portability/PhoneNumber/{PhoneNumber} | 



## fetchPortingPortability

> NumbersV1PortingPortability fetchPortingPortability(phoneNumber, opts)



Allows to check if a single phone number can be ported to Twilio or not.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV1PortingPortabilityApi();
let phoneNumber = "phoneNumber_example"; // String | The phone number which portability is to be checked. Phone numbers are in E.164 format (e.g. +16175551212).
let opts = {
  'targetAccountSid': "targetAccountSid_example" // String | The SID of the account where the phone number(s) will be ported.
};
apiInstance.fetchPortingPortability(phoneNumber, opts, (error, data, response) => {
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
 **phoneNumber** | **String**| The phone number which portability is to be checked. Phone numbers are in E.164 format (e.g. +16175551212). | 
 **targetAccountSid** | **String**| The SID of the account where the phone number(s) will be ported. | [optional] 

### Return type

[**NumbersV1PortingPortability**](NumbersV1PortingPortability.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

