# TwilioAutopilot.AutopilotV1DialogueApi

All URIs are relative to *https://autopilot.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchDialogue**](AutopilotV1DialogueApi.md#fetchDialogue) | **GET** /v1/Assistants/{AssistantSid}/Dialogues/{Sid} | 



## fetchDialogue

> AutopilotV1AssistantDialogue fetchDialogue(assistantSid, sid)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1DialogueApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Dialogue resource to fetch.
apiInstance.fetchDialogue(assistantSid, sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Dialogue resource to fetch. | 

### Return type

[**AutopilotV1AssistantDialogue**](AutopilotV1AssistantDialogue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

