# TwilioTaskrouter.TaskrouterV1WorkflowStatisticsApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchWorkflowStatistics**](TaskrouterV1WorkflowStatisticsApi.md#fetchWorkflowStatistics) | **GET** /v1/Workspaces/{WorkspaceSid}/Workflows/{WorkflowSid}/Statistics | 



## fetchWorkflowStatistics

> TaskrouterV1WorkspaceWorkflowWorkflowStatistics fetchWorkflowStatistics(workspaceSid, workflowSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkflowStatisticsApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Workflow to fetch.
let workflowSid = "workflowSid_example"; // String | Returns the list of Tasks that are being controlled by the Workflow with the specified SID value.
let opts = {
  'minutes': 56, // Number | Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
  'taskChannel': "taskChannel_example", // String | Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
  'splitByWaitTime': "splitByWaitTime_example" // String | A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, `5,30` would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA.
};
apiInstance.fetchWorkflowStatistics(workspaceSid, workflowSid, opts, (error, data, response) => {
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
 **minutes** | **Number**| Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends. | [optional] 
 **startDate** | **Date**| Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
 **endDate** | **Date**| Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time. | [optional] 
 **taskChannel** | **String**| Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] 
 **splitByWaitTime** | **String**| A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, &#x60;5,30&#x60; would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA. | [optional] 

### Return type

[**TaskrouterV1WorkspaceWorkflowWorkflowStatistics**](TaskrouterV1WorkspaceWorkflowWorkflowStatistics.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

