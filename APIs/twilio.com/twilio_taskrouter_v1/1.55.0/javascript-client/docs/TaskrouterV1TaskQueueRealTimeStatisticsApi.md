# TwilioTaskrouter.TaskrouterV1TaskQueueRealTimeStatisticsApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchTaskQueueRealTimeStatistics**](TaskrouterV1TaskQueueRealTimeStatisticsApi.md#fetchTaskQueueRealTimeStatistics) | **GET** /v1/Workspaces/{WorkspaceSid}/TaskQueues/{TaskQueueSid}/RealTimeStatistics | 



## fetchTaskQueueRealTimeStatistics

> TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics fetchTaskQueueRealTimeStatistics(workspaceSid, taskQueueSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskQueueRealTimeStatisticsApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskQueue to fetch.
let taskQueueSid = "taskQueueSid_example"; // String | The SID of the TaskQueue for which to fetch statistics.
let opts = {
  'taskChannel': "taskChannel_example" // String | The TaskChannel for which to fetch statistics. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
};
apiInstance.fetchTaskQueueRealTimeStatistics(workspaceSid, taskQueueSid, opts, (error, data, response) => {
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
 **taskChannel** | **String**| The TaskChannel for which to fetch statistics. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] 

### Return type

[**TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics**](TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

