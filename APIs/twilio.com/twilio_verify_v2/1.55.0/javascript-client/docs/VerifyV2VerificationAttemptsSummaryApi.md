# TwilioVerify.VerifyV2VerificationAttemptsSummaryApi

All URIs are relative to *https://verify.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchVerificationAttemptsSummary**](VerifyV2VerificationAttemptsSummaryApi.md#fetchVerificationAttemptsSummary) | **GET** /v2/Attempts/Summary | 



## fetchVerificationAttemptsSummary

> VerifyV2VerificationAttemptsSummary fetchVerificationAttemptsSummary(opts)



Get a summary of how many attempts were made and how many were converted.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2VerificationAttemptsSummaryApi();
let opts = {
  'verifyServiceSid': "verifyServiceSid_example", // String | Filter used to consider only Verification Attempts of the given verify service on the summary aggregation.
  'dateCreatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
  'dateCreatedBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
  'country': "country_example", // String | Filter used to consider only Verification Attempts sent to the specified destination country on the summary aggregation.
  'channel': "channel_example", // VerificationAttemptsSummaryEnumChannels | Filter Verification Attempts considered on the summary aggregation by communication channel. Valid values are `SMS`, `CALL` and `WHATSAPP`
  'destinationPrefix': "destinationPrefix_example" // String | Filter the Verification Attempts considered on the summary aggregation by Destination prefix. It is the prefix of a phone number in E.164 format.
};
apiInstance.fetchVerificationAttemptsSummary(opts, (error, data, response) => {
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
 **verifyServiceSid** | **String**| Filter used to consider only Verification Attempts of the given verify service on the summary aggregation. | [optional] 
 **dateCreatedAfter** | **Date**| Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z. | [optional] 
 **dateCreatedBefore** | **Date**| Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z. | [optional] 
 **country** | **String**| Filter used to consider only Verification Attempts sent to the specified destination country on the summary aggregation. | [optional] 
 **channel** | **VerificationAttemptsSummaryEnumChannels**| Filter Verification Attempts considered on the summary aggregation by communication channel. Valid values are &#x60;SMS&#x60;, &#x60;CALL&#x60; and &#x60;WHATSAPP&#x60; | [optional] 
 **destinationPrefix** | **String**| Filter the Verification Attempts considered on the summary aggregation by Destination prefix. It is the prefix of a phone number in E.164 format. | [optional] 

### Return type

[**VerifyV2VerificationAttemptsSummary**](VerifyV2VerificationAttemptsSummary.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

