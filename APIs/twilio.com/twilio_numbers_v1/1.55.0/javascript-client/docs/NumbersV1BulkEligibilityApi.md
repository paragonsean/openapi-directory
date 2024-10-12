# TwilioNumbers.NumbersV1BulkEligibilityApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchBulkEligibility**](NumbersV1BulkEligibilityApi.md#fetchBulkEligibility) | **GET** /v1/HostedNumber/Eligibility/Bulk/{RequestId} | 



## fetchBulkEligibility

> NumbersV1BulkEligibility fetchBulkEligibility(requestId)



Fetch an eligibility bulk check that you requested to host in Twilio.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV1BulkEligibilityApi();
let requestId = "requestId_example"; // String | The SID of the bulk eligibility check that you want to know about.
apiInstance.fetchBulkEligibility(requestId, (error, data, response) => {
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
 **requestId** | **String**| The SID of the bulk eligibility check that you want to know about. | 

### Return type

[**NumbersV1BulkEligibility**](NumbersV1BulkEligibility.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

