# TwilioAutopilot.AutopilotV1DefaultsApi

All URIs are relative to *https://autopilot.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchDefaults**](AutopilotV1DefaultsApi.md#fetchDefaults) | **GET** /v1/Assistants/{AssistantSid}/Defaults | 
[**updateDefaults**](AutopilotV1DefaultsApi.md#updateDefaults) | **POST** /v1/Assistants/{AssistantSid}/Defaults | 



## fetchDefaults

> AutopilotV1AssistantDefaults fetchDefaults(assistantSid)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1DefaultsApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
apiInstance.fetchDefaults(assistantSid, (error, data, response) => {
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

[**AutopilotV1AssistantDefaults**](AutopilotV1AssistantDefaults.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDefaults

> AutopilotV1AssistantDefaults updateDefaults(assistantSid, opts)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1DefaultsApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
let opts = {
  'defaults': null // Object | A JSON string that describes the default task links for the `assistant_initiation`, `collect`, and `fallback` situations.
};
apiInstance.updateDefaults(assistantSid, opts, (error, data, response) => {
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
 **defaults** | [**Object**](Object.md)| A JSON string that describes the default task links for the &#x60;assistant_initiation&#x60;, &#x60;collect&#x60;, and &#x60;fallback&#x60; situations. | [optional] 

### Return type

[**AutopilotV1AssistantDefaults**](AutopilotV1AssistantDefaults.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

