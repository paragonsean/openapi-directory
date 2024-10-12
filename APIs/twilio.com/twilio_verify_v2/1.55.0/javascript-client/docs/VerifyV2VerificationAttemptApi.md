# TwilioVerify.VerifyV2VerificationAttemptApi

All URIs are relative to *https://verify.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchVerificationAttempt**](VerifyV2VerificationAttemptApi.md#fetchVerificationAttempt) | **GET** /v2/Attempts/{Sid} | 
[**listVerificationAttempt**](VerifyV2VerificationAttemptApi.md#listVerificationAttempt) | **GET** /v2/Attempts | 



## fetchVerificationAttempt

> VerifyV2VerificationAttempt fetchVerificationAttempt(sid)



Fetch a specific verification attempt.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2VerificationAttemptApi();
let sid = "sid_example"; // String | The unique SID identifier of a Verification Attempt
apiInstance.fetchVerificationAttempt(sid, (error, data, response) => {
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
 **sid** | **String**| The unique SID identifier of a Verification Attempt | 

### Return type

[**VerifyV2VerificationAttempt**](VerifyV2VerificationAttempt.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVerificationAttempt

> ListVerificationAttemptResponse listVerificationAttempt(opts)



List all the verification attempts for a given Account.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2VerificationAttemptApi();
let opts = {
  'dateCreatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
  'dateCreatedBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
  'channelDataTo': "channelDataTo_example", // String | Destination of a verification. It is phone number in E.164 format.
  'country': "country_example", // String | Filter used to query Verification Attempts sent to the specified destination country.
  'channel': "channel_example", // VerificationAttemptEnumChannels | Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
  'verifyServiceSid': "verifyServiceSid_example", // String | Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
  'verificationSid': "verificationSid_example", // String | Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
  'status': "status_example", // VerificationAttemptEnumConversionStatus | Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listVerificationAttempt(opts, (error, data, response) => {
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
 **dateCreatedAfter** | **Date**| Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z. | [optional] 
 **dateCreatedBefore** | **Date**| Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z. | [optional] 
 **channelDataTo** | **String**| Destination of a verification. It is phone number in E.164 format. | [optional] 
 **country** | **String**| Filter used to query Verification Attempts sent to the specified destination country. | [optional] 
 **channel** | **VerificationAttemptEnumChannels**| Filter used to query Verification Attempts by communication channel. Valid values are &#x60;SMS&#x60; and &#x60;CALL&#x60; | [optional] 
 **verifyServiceSid** | **String**| Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned. | [optional] 
 **verificationSid** | **String**| Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned. | [optional] 
 **status** | **VerificationAttemptEnumConversionStatus**| Filter used to query Verification Attempts by conversion status. Valid values are &#x60;UNCONVERTED&#x60;, for attempts that were not converted, and &#x60;CONVERTED&#x60;, for attempts that were confirmed. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListVerificationAttemptResponse**](ListVerificationAttemptResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

