# TwilioTaskrouter.TaskrouterV1WorkerStatisticsApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchWorkerInstanceStatistics**](TaskrouterV1WorkerStatisticsApi.md#fetchWorkerInstanceStatistics) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Statistics | 



## fetchWorkerInstanceStatistics

> TaskrouterV1WorkspaceWorkerWorkerInstanceStatistics fetchWorkerInstanceStatistics(workspaceSid, workerSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkerStatisticsApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the WorkerChannel to fetch.
let workerSid = "workerSid_example"; // String | The SID of the Worker with the WorkerChannel to fetch.
let opts = {
  'minutes': 56, // Number | Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only include usage that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
  'taskChannel': "taskChannel_example" // String | Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
};
apiInstance.fetchWorkerInstanceStatistics(workspaceSid, workerSid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the WorkerChannel to fetch. | 
 **workerSid** | **String**| The SID of the Worker with the WorkerChannel to fetch. | 
 **minutes** | **Number**| Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends. | [optional] 
 **startDate** | **Date**| Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
 **endDate** | **Date**| Only include usage that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time. | [optional] 
 **taskChannel** | **String**| Only calculate statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] 

### Return type

[**TaskrouterV1WorkspaceWorkerWorkerInstanceStatistics**](TaskrouterV1WorkspaceWorkerWorkerInstanceStatistics.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

