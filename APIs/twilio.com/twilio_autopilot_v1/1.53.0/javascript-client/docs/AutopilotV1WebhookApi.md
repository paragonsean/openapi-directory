# TwilioAutopilot.AutopilotV1WebhookApi

All URIs are relative to *https://autopilot.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWebhook**](AutopilotV1WebhookApi.md#createWebhook) | **POST** /v1/Assistants/{AssistantSid}/Webhooks | 
[**deleteWebhook**](AutopilotV1WebhookApi.md#deleteWebhook) | **DELETE** /v1/Assistants/{AssistantSid}/Webhooks/{Sid} | 
[**fetchWebhook**](AutopilotV1WebhookApi.md#fetchWebhook) | **GET** /v1/Assistants/{AssistantSid}/Webhooks/{Sid} | 
[**listWebhook**](AutopilotV1WebhookApi.md#listWebhook) | **GET** /v1/Assistants/{AssistantSid}/Webhooks | 
[**updateWebhook**](AutopilotV1WebhookApi.md#updateWebhook) | **POST** /v1/Assistants/{AssistantSid}/Webhooks/{Sid} | 



## createWebhook

> AutopilotV1AssistantWebhook createWebhook(assistantSid, events, uniqueName, webhookUrl, opts)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1WebhookApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the new resource.
let events = "events_example"; // String | The list of space-separated events that this Webhook will subscribe to.
let uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the `sid` in the URL path to address the resource. This value must be unique and 64 characters or less in length.
let webhookUrl = "webhookUrl_example"; // String | The URL associated with this Webhook.
let opts = {
  'webhookMethod': "webhookMethod_example" // String | The method to be used when calling the webhook's URL.
};
apiInstance.createWebhook(assistantSid, events, uniqueName, webhookUrl, opts, (error, data, response) => {
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
 **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the new resource. | 
 **events** | **String**| The list of space-separated events that this Webhook will subscribe to. | 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. This value must be unique and 64 characters or less in length. | 
 **webhookUrl** | **String**| The URL associated with this Webhook. | 
 **webhookMethod** | **String**| The method to be used when calling the webhook&#39;s URL. | [optional] 

### Return type

[**AutopilotV1AssistantWebhook**](AutopilotV1AssistantWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteWebhook

> deleteWebhook(assistantSid, sid)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1WebhookApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Webhook resource to delete.
apiInstance.deleteWebhook(assistantSid, sid, (error, data, response) => {
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
 **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to delete. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Webhook resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchWebhook

> AutopilotV1AssistantWebhook fetchWebhook(assistantSid, sid)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1WebhookApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Webhook resource to fetch.
apiInstance.fetchWebhook(assistantSid, sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Webhook resource to fetch. | 

### Return type

[**AutopilotV1AssistantWebhook**](AutopilotV1AssistantWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWebhook

> ListWebhookResponse listWebhook(assistantSid, opts)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1WebhookApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listWebhook(assistantSid, opts, (error, data, response) => {
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
 **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListWebhookResponse**](ListWebhookResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWebhook

> AutopilotV1AssistantWebhook updateWebhook(assistantSid, sid, opts)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1WebhookApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Webhook resource to update.
let opts = {
  'events': "events_example", // String | The list of space-separated events that this Webhook will subscribe to.
  'uniqueName': "uniqueName_example", // String | An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the `sid` in the URL path to address the resource. This value must be unique and 64 characters or less in length.
  'webhookMethod': "webhookMethod_example", // String | The method to be used when calling the webhook's URL.
  'webhookUrl': "webhookUrl_example" // String | The URL associated with this Webhook.
};
apiInstance.updateWebhook(assistantSid, sid, opts, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Webhook resource to update. | 
 **events** | **String**| The list of space-separated events that this Webhook will subscribe to. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. This value must be unique and 64 characters or less in length. | [optional] 
 **webhookMethod** | **String**| The method to be used when calling the webhook&#39;s URL. | [optional] 
 **webhookUrl** | **String**| The URL associated with this Webhook. | [optional] 

### Return type

[**AutopilotV1AssistantWebhook**](AutopilotV1AssistantWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

