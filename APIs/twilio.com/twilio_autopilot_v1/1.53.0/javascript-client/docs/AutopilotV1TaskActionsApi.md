# TwilioAutopilot.AutopilotV1TaskActionsApi

All URIs are relative to *https://autopilot.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchTaskActions**](AutopilotV1TaskActionsApi.md#fetchTaskActions) | **GET** /v1/Assistants/{AssistantSid}/Tasks/{TaskSid}/Actions | 
[**updateTaskActions**](AutopilotV1TaskActionsApi.md#updateTaskActions) | **POST** /v1/Assistants/{AssistantSid}/Tasks/{TaskSid}/Actions | 



## fetchTaskActions

> AutopilotV1AssistantTaskTaskActions fetchTaskActions(assistantSid, taskSid)



Returns JSON actions for the Task.

### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1TaskActionsApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task for which the task actions to fetch were defined.
let taskSid = "taskSid_example"; // String | The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) for which the task actions to fetch were defined.
apiInstance.fetchTaskActions(assistantSid, taskSid, (error, data, response) => {
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
 **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task for which the task actions to fetch were defined. | 
 **taskSid** | **String**| The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) for which the task actions to fetch were defined. | 

### Return type

[**AutopilotV1AssistantTaskTaskActions**](AutopilotV1AssistantTaskTaskActions.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTaskActions

> AutopilotV1AssistantTaskTaskActions updateTaskActions(assistantSid, taskSid, opts)



Updates the actions of an Task identified by {TaskSid} or {TaskUniqueName}.

### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1TaskActionsApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task for which the task actions to update were defined.
let taskSid = "taskSid_example"; // String | The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) for which the task actions to update were defined.
let opts = {
  'actions': null // Object | The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task.
};
apiInstance.updateTaskActions(assistantSid, taskSid, opts, (error, data, response) => {
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
 **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task for which the task actions to update were defined. | 
 **taskSid** | **String**| The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) for which the task actions to update were defined. | 
 **actions** | [**Object**](Object.md)| The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task. | [optional] 

### Return type

[**AutopilotV1AssistantTaskTaskActions**](AutopilotV1AssistantTaskTaskActions.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

