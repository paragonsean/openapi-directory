# TwilioPricing.PricingV2NumberApi

All URIs are relative to *https://pricing.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchTrunkingNumber**](PricingV2NumberApi.md#fetchTrunkingNumber) | **GET** /v2/Trunking/Numbers/{DestinationNumber} | 
[**fetchVoiceNumber**](PricingV2NumberApi.md#fetchVoiceNumber) | **GET** /v2/Voice/Numbers/{DestinationNumber} | 



## fetchTrunkingNumber

> PricingV2TrunkingNumber fetchTrunkingNumber(destinationNumber, opts)



Fetch pricing information for a specific destination and, optionally, origination phone number.

### Example

```javascript
import TwilioPricing from 'twilio_pricing';
let defaultClient = TwilioPricing.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPricing.PricingV2NumberApi();
let destinationNumber = "destinationNumber_example"; // String | The destination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
let opts = {
  'originationNumber': "originationNumber_example" // String | The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
};
apiInstance.fetchTrunkingNumber(destinationNumber, opts, (error, data, response) => {
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
 **destinationNumber** | **String**| The destination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number. | 
 **originationNumber** | **String**| The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number. | [optional] 

### Return type

[**PricingV2TrunkingNumber**](PricingV2TrunkingNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchVoiceNumber

> PricingV2VoiceVoiceNumber fetchVoiceNumber(destinationNumber, opts)



Fetch pricing information for a specific destination and, optionally, origination phone number.

### Example

```javascript
import TwilioPricing from 'twilio_pricing';
let defaultClient = TwilioPricing.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPricing.PricingV2NumberApi();
let destinationNumber = "destinationNumber_example"; // String | The destination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
let opts = {
  'originationNumber': "originationNumber_example" // String | The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
};
apiInstance.fetchVoiceNumber(destinationNumber, opts, (error, data, response) => {
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
 **destinationNumber** | **String**| The destination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number. | 
 **originationNumber** | **String**| The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number. | [optional] 

### Return type

[**PricingV2VoiceVoiceNumber**](PricingV2VoiceVoiceNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

