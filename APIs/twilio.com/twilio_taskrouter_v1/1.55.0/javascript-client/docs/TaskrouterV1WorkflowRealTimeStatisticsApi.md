# TwilioTaskrouter.TaskrouterV1WorkflowRealTimeStatisticsApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchWorkflowRealTimeStatistics**](TaskrouterV1WorkflowRealTimeStatisticsApi.md#fetchWorkflowRealTimeStatistics) | **GET** /v1/Workspaces/{WorkspaceSid}/Workflows/{WorkflowSid}/RealTimeStatistics | 



## fetchWorkflowRealTimeStatistics

> TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics fetchWorkflowRealTimeStatistics(workspaceSid, workflowSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkflowRealTimeStatisticsApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Workflow to fetch.
let workflowSid = "workflowSid_example"; // String | Returns the list of Tasks that are being controlled by the Workflow with the specified SID value.
let opts = {
  'taskChannel': "taskChannel_example" // String | Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
};
apiInstance.fetchWorkflowRealTimeStatistics(workspaceSid, workflowSid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Workflow to fetch. | 
 **workflowSid** | **String**| Returns the list of Tasks that are being controlled by the Workflow with the specified SID value. | 
 **taskChannel** | **String**| Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] 

### Return type

[**TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics**](TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

