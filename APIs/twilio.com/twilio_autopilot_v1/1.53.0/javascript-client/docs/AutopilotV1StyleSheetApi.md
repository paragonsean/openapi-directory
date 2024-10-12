# TwilioAutopilot.AutopilotV1StyleSheetApi

All URIs are relative to *https://autopilot.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchStyleSheet**](AutopilotV1StyleSheetApi.md#fetchStyleSheet) | **GET** /v1/Assistants/{AssistantSid}/StyleSheet | 
[**updateStyleSheet**](AutopilotV1StyleSheetApi.md#updateStyleSheet) | **POST** /v1/Assistants/{AssistantSid}/StyleSheet | 



## fetchStyleSheet

> AutopilotV1AssistantStyleSheet fetchStyleSheet(assistantSid)



Returns Style sheet JSON object for the Assistant

### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1StyleSheetApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
apiInstance.fetchStyleSheet(assistantSid, (error, data, response) => {
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

### Return type

[**AutopilotV1AssistantStyleSheet**](AutopilotV1AssistantStyleSheet.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateStyleSheet

> AutopilotV1AssistantStyleSheet updateStyleSheet(assistantSid, opts)



Updates the style sheet for an Assistant identified by &#x60;assistant_sid&#x60;.

### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1StyleSheetApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
let opts = {
  'styleSheet': null // Object | The JSON string that describes the style sheet object.
};
apiInstance.updateStyleSheet(assistantSid, opts, (error, data, response) => {
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
 **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update. | 
 **styleSheet** | [**Object**](Object.md)| The JSON string that describes the style sheet object. | [optional] 

### Return type

[**AutopilotV1AssistantStyleSheet**](AutopilotV1AssistantStyleSheet.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

