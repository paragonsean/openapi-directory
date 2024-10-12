# TwilioStudio.StudioV1StepContextApi

All URIs are relative to *https://studio.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchStepContext**](StudioV1StepContextApi.md#fetchStepContext) | **GET** /v1/Flows/{FlowSid}/Engagements/{EngagementSid}/Steps/{StepSid}/Context | 



## fetchStepContext

> StudioV1FlowEngagementStepStepContext fetchStepContext(flowSid, engagementSid, stepSid)



Retrieve the context for an Engagement Step.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV1StepContextApi();
let flowSid = "flowSid_example"; // String | The SID of the Flow with the Step to fetch.
let engagementSid = "engagementSid_example"; // String | The SID of the Engagement with the Step to fetch.
let stepSid = "stepSid_example"; // String | The SID of the Step to fetch
apiInstance.fetchStepContext(flowSid, engagementSid, stepSid, (error, data, response) => {
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
 **flowSid** | **String**| The SID of the Flow with the Step to fetch. | 
 **engagementSid** | **String**| The SID of the Engagement with the Step to fetch. | 
 **stepSid** | **String**| The SID of the Step to fetch | 

### Return type

[**StudioV1FlowEngagementStepStepContext**](StudioV1FlowEngagementStepStepContext.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

