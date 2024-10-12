# TwilioTaskrouter.TaskrouterV1WorkersCumulativeStatisticsApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchWorkersCumulativeStatistics**](TaskrouterV1WorkersCumulativeStatisticsApi.md#fetchWorkersCumulativeStatistics) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/CumulativeStatistics | 



## fetchWorkersCumulativeStatistics

> TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics fetchWorkersCumulativeStatistics(workspaceSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1WorkersCumulativeStatisticsApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the resource to fetch.
let opts = {
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only calculate statistics from this date and time and earlier, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
  'minutes': 56, // Number | Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
  'taskChannel': "taskChannel_example" // String | Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
};
apiInstance.fetchWorkersCumulativeStatistics(workspaceSid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the resource to fetch. | 
 **endDate** | **Date**| Only calculate statistics from this date and time and earlier, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
 **minutes** | **Number**| Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends. | [optional] 
 **startDate** | **Date**| Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
 **taskChannel** | **String**| Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] 

### Return type

[**TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics**](TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

