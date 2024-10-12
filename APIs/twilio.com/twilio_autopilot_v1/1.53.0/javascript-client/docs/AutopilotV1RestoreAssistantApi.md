# TwilioAutopilot.AutopilotV1RestoreAssistantApi

All URIs are relative to *https://autopilot.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateRestoreAssistant**](AutopilotV1RestoreAssistantApi.md#updateRestoreAssistant) | **POST** /v1/Assistants/Restore | 



## updateRestoreAssistant

> AutopilotV1RestoreAssistant updateRestoreAssistant(assistant)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1RestoreAssistantApi();
let assistant = "assistant_example"; // String | The Twilio-provided string that uniquely identifies the Assistant resource to restore.
apiInstance.updateRestoreAssistant(assistant, (error, data, response) => {
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
 **assistant** | **String**| The Twilio-provided string that uniquely identifies the Assistant resource to restore. | 

### Return type

[**AutopilotV1RestoreAssistant**](AutopilotV1RestoreAssistant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

