# TwilioStudio.StudioV1ExecutionStepContextApi

All URIs are relative to *https://studio.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchExecutionStepContext**](StudioV1ExecutionStepContextApi.md#fetchExecutionStepContext) | **GET** /v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Steps/{StepSid}/Context | 



## fetchExecutionStepContext

> StudioV1FlowExecutionExecutionStepExecutionStepContext fetchExecutionStepContext(flowSid, executionSid, stepSid)



Retrieve the context for an Execution Step.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV1ExecutionStepContextApi();
let flowSid = "flowSid_example"; // String | The SID of the Flow with the Step to fetch.
let executionSid = "executionSid_example"; // String | The SID of the Execution resource with the Step to fetch.
let stepSid = "stepSid_example"; // String | The SID of the Step to fetch.
apiInstance.fetchExecutionStepContext(flowSid, executionSid, stepSid, (error, data, response) => {
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
 **executionSid** | **String**| The SID of the Execution resource with the Step to fetch. | 
 **stepSid** | **String**| The SID of the Step to fetch. | 

### Return type

[**StudioV1FlowExecutionExecutionStepExecutionStepContext**](StudioV1FlowExecutionExecutionStepExecutionStepContext.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

