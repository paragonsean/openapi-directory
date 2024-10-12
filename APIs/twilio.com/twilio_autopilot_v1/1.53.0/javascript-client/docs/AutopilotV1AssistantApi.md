# TwilioAutopilot.AutopilotV1AssistantApi

All URIs are relative to *https://autopilot.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAssistant**](AutopilotV1AssistantApi.md#createAssistant) | **POST** /v1/Assistants | 
[**deleteAssistant**](AutopilotV1AssistantApi.md#deleteAssistant) | **DELETE** /v1/Assistants/{Sid} | 
[**fetchAssistant**](AutopilotV1AssistantApi.md#fetchAssistant) | **GET** /v1/Assistants/{Sid} | 
[**listAssistant**](AutopilotV1AssistantApi.md#listAssistant) | **GET** /v1/Assistants | 
[**updateAssistant**](AutopilotV1AssistantApi.md#updateAssistant) | **POST** /v1/Assistants/{Sid} | 



## createAssistant

> AutopilotV1Assistant createAssistant(opts)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1AssistantApi();
let opts = {
  'callbackEvents': "callbackEvents_example", // String | Reserved.
  'callbackUrl': "callbackUrl_example", // String | Reserved.
  'defaults': null, // Object | A JSON object that defines the Assistant's [default tasks](https://www.twilio.com/docs/autopilot/api/assistant/defaults) for various scenarios, including initiation actions and fallback tasks.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the new resource. It is not unique and can be up to 255 characters long.
  'logQueries': true, // Boolean | Whether queries should be logged and kept after training. Can be: `true` or `false` and defaults to `true`. If `true`, queries are stored for 30 days, and then deleted. If `false`, no queries are stored.
  'styleSheet': null, // Object | The JSON string that defines the Assistant's [style sheet](https://www.twilio.com/docs/autopilot/api/assistant/stylesheet)
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the `sid` in the URL path to address the resource. The first 64 characters must be unique.
};
apiInstance.createAssistant(opts, (error, data, response) => {
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
 **callbackEvents** | **String**| Reserved. | [optional] 
 **callbackUrl** | **String**| Reserved. | [optional] 
 **defaults** | [**Object**](Object.md)| A JSON object that defines the Assistant&#39;s [default tasks](https://www.twilio.com/docs/autopilot/api/assistant/defaults) for various scenarios, including initiation actions and fallback tasks. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the new resource. It is not unique and can be up to 255 characters long. | [optional] 
 **logQueries** | **Boolean**| Whether queries should be logged and kept after training. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;true&#x60;. If &#x60;true&#x60;, queries are stored for 30 days, and then deleted. If &#x60;false&#x60;, no queries are stored. | [optional] 
 **styleSheet** | [**Object**](Object.md)| The JSON string that defines the Assistant&#39;s [style sheet](https://www.twilio.com/docs/autopilot/api/assistant/stylesheet) | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. The first 64 characters must be unique. | [optional] 

### Return type

[**AutopilotV1Assistant**](AutopilotV1Assistant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteAssistant

> deleteAssistant(sid)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1AssistantApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Assistant resource to delete.
apiInstance.deleteAssistant(sid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Assistant resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchAssistant

> AutopilotV1Assistant fetchAssistant(sid)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1AssistantApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Assistant resource to fetch.
apiInstance.fetchAssistant(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Assistant resource to fetch. | 

### Return type

[**AutopilotV1Assistant**](AutopilotV1Assistant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssistant

> ListAssistantResponse listAssistant(opts)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1AssistantApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listAssistant(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListAssistantResponse**](ListAssistantResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAssistant

> AutopilotV1Assistant updateAssistant(sid, opts)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1AssistantApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Assistant resource to update.
let opts = {
  'callbackEvents': "callbackEvents_example", // String | Reserved.
  'callbackUrl': "callbackUrl_example", // String | Reserved.
  'defaults': null, // Object | A JSON object that defines the Assistant's [default tasks](https://www.twilio.com/docs/autopilot/api/assistant/defaults) for various scenarios, including initiation actions and fallback tasks.
  'developmentStage': "developmentStage_example", // String | A string describing the state of the assistant.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
  'logQueries': true, // Boolean | Whether queries should be logged and kept after training. Can be: `true` or `false` and defaults to `true`. If `true`, queries are stored for 30 days, and then deleted. If `false`, no queries are stored.
  'styleSheet': null, // Object | The JSON string that defines the Assistant's [style sheet](https://www.twilio.com/docs/autopilot/api/assistant/stylesheet)
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used as an alternative to the `sid` in the URL path to address the resource. The first 64 characters must be unique.
};
apiInstance.updateAssistant(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Assistant resource to update. | 
 **callbackEvents** | **String**| Reserved. | [optional] 
 **callbackUrl** | **String**| Reserved. | [optional] 
 **defaults** | [**Object**](Object.md)| A JSON object that defines the Assistant&#39;s [default tasks](https://www.twilio.com/docs/autopilot/api/assistant/defaults) for various scenarios, including initiation actions and fallback tasks. | [optional] 
 **developmentStage** | **String**| A string describing the state of the assistant. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] 
 **logQueries** | **Boolean**| Whether queries should be logged and kept after training. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;true&#x60;. If &#x60;true&#x60;, queries are stored for 30 days, and then deleted. If &#x60;false&#x60;, no queries are stored. | [optional] 
 **styleSheet** | [**Object**](Object.md)| The JSON string that defines the Assistant&#39;s [style sheet](https://www.twilio.com/docs/autopilot/api/assistant/stylesheet) | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. The first 64 characters must be unique. | [optional] 

### Return type

[**AutopilotV1Assistant**](AutopilotV1Assistant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

