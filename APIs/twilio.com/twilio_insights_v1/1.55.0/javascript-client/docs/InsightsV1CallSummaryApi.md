# TwilioInsights.InsightsV1CallSummaryApi

All URIs are relative to *https://insights.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchSummary**](InsightsV1CallSummaryApi.md#fetchSummary) | **GET** /v1/Voice/{CallSid}/Summary | 



## fetchSummary

> InsightsV1CallSummary fetchSummary(callSid, opts)



Get a specific Call Summary.

### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1CallSummaryApi();
let callSid = "callSid_example"; // String | The unique SID identifier of the Call.
let opts = {
  'processingState': "processingState_example" // SummaryEnumProcessingState | The Processing State of this Call Summary. One of `complete`, `partial` or `all`.
};
apiInstance.fetchSummary(callSid, opts, (error, data, response) => {
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
 **callSid** | **String**| The unique SID identifier of the Call. | 
 **processingState** | **SummaryEnumProcessingState**| The Processing State of this Call Summary. One of &#x60;complete&#x60;, &#x60;partial&#x60; or &#x60;all&#x60;. | [optional] 

### Return type

[**InsightsV1CallSummary**](InsightsV1CallSummary.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

