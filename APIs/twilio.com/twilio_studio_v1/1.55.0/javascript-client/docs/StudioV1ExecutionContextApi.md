# TwilioStudio.StudioV1ExecutionContextApi

All URIs are relative to *https://studio.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchExecutionContext**](StudioV1ExecutionContextApi.md#fetchExecutionContext) | **GET** /v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Context | 



## fetchExecutionContext

> StudioV1FlowExecutionExecutionContext fetchExecutionContext(flowSid, executionSid)



Retrieve the most recent context for an Execution.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV1ExecutionContextApi();
let flowSid = "flowSid_example"; // String | The SID of the Flow with the Execution context to fetch.
let executionSid = "executionSid_example"; // String | The SID of the Execution context to fetch.
apiInstance.fetchExecutionContext(flowSid, executionSid, (error, data, response) => {
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
 **flowSid** | **String**| The SID of the Flow with the Execution context to fetch. | 
 **executionSid** | **String**| The SID of the Execution context to fetch. | 

### Return type

[**StudioV1FlowExecutionExecutionContext**](StudioV1FlowExecutionExecutionContext.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

