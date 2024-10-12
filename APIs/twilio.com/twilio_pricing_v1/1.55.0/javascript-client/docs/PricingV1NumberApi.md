# TwilioPricing.PricingV1NumberApi

All URIs are relative to *https://pricing.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchVoiceNumber**](PricingV1NumberApi.md#fetchVoiceNumber) | **GET** /v1/Voice/Numbers/{Number} | 



## fetchVoiceNumber

> PricingV1VoiceVoiceNumber fetchVoiceNumber(number)





### Example

```javascript
import TwilioPricing from 'twilio_pricing';
let defaultClient = TwilioPricing.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPricing.PricingV1NumberApi();
let number = "number_example"; // String | The phone number to fetch.
apiInstance.fetchVoiceNumber(number, (error, data, response) => {
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
 **number** | **String**| The phone number to fetch. | 

### Return type

[**PricingV1VoiceVoiceNumber**](PricingV1VoiceVoiceNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

