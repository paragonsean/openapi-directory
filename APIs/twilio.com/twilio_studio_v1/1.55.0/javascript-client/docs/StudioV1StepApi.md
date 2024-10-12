# TwilioStudio.StudioV1StepApi

All URIs are relative to *https://studio.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchStep**](StudioV1StepApi.md#fetchStep) | **GET** /v1/Flows/{FlowSid}/Engagements/{EngagementSid}/Steps/{Sid} | 
[**listStep**](StudioV1StepApi.md#listStep) | **GET** /v1/Flows/{FlowSid}/Engagements/{EngagementSid}/Steps | 



## fetchStep

> StudioV1FlowEngagementStep fetchStep(flowSid, engagementSid, sid)



Retrieve a Step.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV1StepApi();
let flowSid = "flowSid_example"; // String | The SID of the Flow with the Step to fetch.
let engagementSid = "engagementSid_example"; // String | The SID of the Engagement with the Step to fetch.
let sid = "sid_example"; // String | The SID of the Step resource to fetch.
apiInstance.fetchStep(flowSid, engagementSid, sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Step resource to fetch. | 

### Return type

[**StudioV1FlowEngagementStep**](StudioV1FlowEngagementStep.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listStep

> ListStepResponse listStep(flowSid, engagementSid, opts)



Retrieve a list of all Steps for an Engagement.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV1StepApi();
let flowSid = "flowSid_example"; // String | The SID of the Flow with the Step to read.
let engagementSid = "engagementSid_example"; // String | The SID of the Engagement with the Step to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listStep(flowSid, engagementSid, opts, (error, data, response) => {
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
 **flowSid** | **String**| The SID of the Flow with the Step to read. | 
 **engagementSid** | **String**| The SID of the Engagement with the Step to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListStepResponse**](ListStepResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

