# TwilioAutopilot.AutopilotV1TaskStatisticsApi

All URIs are relative to *https://autopilot.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchTaskStatistics**](AutopilotV1TaskStatisticsApi.md#fetchTaskStatistics) | **GET** /v1/Assistants/{AssistantSid}/Tasks/{TaskSid}/Statistics | 



## fetchTaskStatistics

> AutopilotV1AssistantTaskTaskStatistics fetchTaskStatistics(assistantSid, taskSid)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1TaskStatisticsApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
let taskSid = "taskSid_example"; // String | The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) that is associated with the resource to fetch.
apiInstance.fetchTaskStatistics(assistantSid, taskSid, (error, data, response) => {
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
 **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch. | 
 **taskSid** | **String**| The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) that is associated with the resource to fetch. | 

### Return type

[**AutopilotV1AssistantTaskTaskStatistics**](AutopilotV1AssistantTaskTaskStatistics.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

