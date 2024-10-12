# TwilioTaskrouter.TaskrouterV1TaskQueueStatisticsApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchTaskQueueStatistics**](TaskrouterV1TaskQueueStatisticsApi.md#fetchTaskQueueStatistics) | **GET** /v1/Workspaces/{WorkspaceSid}/TaskQueues/{TaskQueueSid}/Statistics | 



## fetchTaskQueueStatistics

> TaskrouterV1WorkspaceTaskQueueTaskQueueStatistics fetchTaskQueueStatistics(workspaceSid, taskQueueSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskQueueStatisticsApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskQueue to fetch.
let taskQueueSid = "taskQueueSid_example"; // String | The SID of the TaskQueue for which to fetch statistics.
let opts = {
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
  'minutes': 56, // Number | Only calculate statistics since this many minutes in the past. The default is 15 minutes.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
  'taskChannel': "taskChannel_example", // String | Only calculate real-time and cumulative statistics for the specified TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
  'splitByWaitTime': "splitByWaitTime_example" // String | A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.
};
apiInstance.fetchTaskQueueStatistics(workspaceSid, taskQueueSid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the TaskQueue to fetch. | 
 **taskQueueSid** | **String**| The SID of the TaskQueue for which to fetch statistics. | 
 **endDate** | **Date**| Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time. | [optional] 
 **minutes** | **Number**| Only calculate statistics since this many minutes in the past. The default is 15 minutes. | [optional] 
 **startDate** | **Date**| Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
 **taskChannel** | **String**| Only calculate real-time and cumulative statistics for the specified TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] 
 **splitByWaitTime** | **String**| A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. | [optional] 

### Return type

[**TaskrouterV1WorkspaceTaskQueueTaskQueueStatistics**](TaskrouterV1WorkspaceTaskQueueTaskQueueStatistics.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

