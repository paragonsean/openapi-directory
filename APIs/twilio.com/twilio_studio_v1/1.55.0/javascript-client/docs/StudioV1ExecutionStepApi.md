# TwilioStudio.StudioV1ExecutionStepApi

All URIs are relative to *https://studio.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchExecutionStep**](StudioV1ExecutionStepApi.md#fetchExecutionStep) | **GET** /v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Steps/{Sid} | 
[**listExecutionStep**](StudioV1ExecutionStepApi.md#listExecutionStep) | **GET** /v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Steps | 



## fetchExecutionStep

> StudioV1FlowExecutionExecutionStep fetchExecutionStep(flowSid, executionSid, sid)



Retrieve a Step.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV1ExecutionStepApi();
let flowSid = "flowSid_example"; // String | The SID of the Flow with the Step to fetch.
let executionSid = "executionSid_example"; // String | The SID of the Execution resource with the Step to fetch.
let sid = "sid_example"; // String | The SID of the ExecutionStep resource to fetch.
apiInstance.fetchExecutionStep(flowSid, executionSid, sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the ExecutionStep resource to fetch. | 

### Return type

[**StudioV1FlowExecutionExecutionStep**](StudioV1FlowExecutionExecutionStep.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listExecutionStep

> ListExecutionStepResponse listExecutionStep(flowSid, executionSid, opts)



Retrieve a list of all Steps for an Execution.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV1ExecutionStepApi();
let flowSid = "flowSid_example"; // String | The SID of the Flow with the Steps to read.
let executionSid = "executionSid_example"; // String | The SID of the Execution with the Steps to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listExecutionStep(flowSid, executionSid, opts, (error, data, response) => {
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
 **flowSid** | **String**| The SID of the Flow with the Steps to read. | 
 **executionSid** | **String**| The SID of the Execution with the Steps to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListExecutionStepResponse**](ListExecutionStepResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

