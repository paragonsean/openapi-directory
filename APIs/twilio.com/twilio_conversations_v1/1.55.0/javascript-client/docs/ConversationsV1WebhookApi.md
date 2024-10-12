# TwilioConversations.ConversationsV1WebhookApi

All URIs are relative to *https://conversations.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createConversationScopedWebhook**](ConversationsV1WebhookApi.md#createConversationScopedWebhook) | **POST** /v1/Conversations/{ConversationSid}/Webhooks | 
[**createServiceConversationScopedWebhook**](ConversationsV1WebhookApi.md#createServiceConversationScopedWebhook) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks | 
[**deleteConversationScopedWebhook**](ConversationsV1WebhookApi.md#deleteConversationScopedWebhook) | **DELETE** /v1/Conversations/{ConversationSid}/Webhooks/{Sid} | 
[**deleteServiceConversationScopedWebhook**](ConversationsV1WebhookApi.md#deleteServiceConversationScopedWebhook) | **DELETE** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid} | 
[**fetchConfigurationWebhook**](ConversationsV1WebhookApi.md#fetchConfigurationWebhook) | **GET** /v1/Configuration/Webhooks | 
[**fetchConversationScopedWebhook**](ConversationsV1WebhookApi.md#fetchConversationScopedWebhook) | **GET** /v1/Conversations/{ConversationSid}/Webhooks/{Sid} | 
[**fetchServiceConversationScopedWebhook**](ConversationsV1WebhookApi.md#fetchServiceConversationScopedWebhook) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid} | 
[**fetchServiceWebhookConfiguration**](ConversationsV1WebhookApi.md#fetchServiceWebhookConfiguration) | **GET** /v1/Services/{ChatServiceSid}/Configuration/Webhooks | 
[**listConversationScopedWebhook**](ConversationsV1WebhookApi.md#listConversationScopedWebhook) | **GET** /v1/Conversations/{ConversationSid}/Webhooks | 
[**listServiceConversationScopedWebhook**](ConversationsV1WebhookApi.md#listServiceConversationScopedWebhook) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks | 
[**updateConfigurationWebhook**](ConversationsV1WebhookApi.md#updateConfigurationWebhook) | **POST** /v1/Configuration/Webhooks | 
[**updateConversationScopedWebhook**](ConversationsV1WebhookApi.md#updateConversationScopedWebhook) | **POST** /v1/Conversations/{ConversationSid}/Webhooks/{Sid} | 
[**updateServiceConversationScopedWebhook**](ConversationsV1WebhookApi.md#updateServiceConversationScopedWebhook) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid} | 
[**updateServiceWebhookConfiguration**](ConversationsV1WebhookApi.md#updateServiceWebhookConfiguration) | **POST** /v1/Services/{ChatServiceSid}/Configuration/Webhooks | 



## createConversationScopedWebhook

> ConversationsV1ConversationConversationScopedWebhook createConversationScopedWebhook(conversationSid, target, opts)



Create a new webhook scoped to the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
let target = "target_example"; // ConversationScopedWebhookEnumTarget | 
let opts = {
  'configurationFilters': ["null"], // [String] | The list of events, firing webhook event for this Conversation.
  'configurationFlowSid': "configurationFlowSid_example", // String | The studio flow SID, where the webhook should be sent to.
  'configurationMethod': "configurationMethod_example", // ConversationScopedWebhookEnumMethod | 
  'configurationReplayAfter': 56, // Number | The message index for which and it's successors the webhook will be replayed. Not set by default
  'configurationTriggers': ["null"], // [String] | The list of keywords, firing webhook event for this Conversation.
  'configurationUrl': "configurationUrl_example" // String | The absolute url the webhook request should be sent to.
};
apiInstance.createConversationScopedWebhook(conversationSid, target, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | 
 **target** | **ConversationScopedWebhookEnumTarget**|  | 
 **configurationFilters** | [**[String]**](String.md)| The list of events, firing webhook event for this Conversation. | [optional] 
 **configurationFlowSid** | **String**| The studio flow SID, where the webhook should be sent to. | [optional] 
 **configurationMethod** | **ConversationScopedWebhookEnumMethod**|  | [optional] 
 **configurationReplayAfter** | **Number**| The message index for which and it&#39;s successors the webhook will be replayed. Not set by default | [optional] 
 **configurationTriggers** | [**[String]**](String.md)| The list of keywords, firing webhook event for this Conversation. | [optional] 
 **configurationUrl** | **String**| The absolute url the webhook request should be sent to. | [optional] 

### Return type

[**ConversationsV1ConversationConversationScopedWebhook**](ConversationsV1ConversationConversationScopedWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## createServiceConversationScopedWebhook

> ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook createServiceConversationScopedWebhook(chatServiceSid, conversationSid, target, opts)



Create a new webhook scoped to the conversation in a specific service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
let target = "target_example"; // ServiceConversationScopedWebhookEnumTarget | 
let opts = {
  'configurationFilters': ["null"], // [String] | The list of events, firing webhook event for this Conversation.
  'configurationFlowSid': "configurationFlowSid_example", // String | The studio flow SID, where the webhook should be sent to.
  'configurationMethod': "configurationMethod_example", // ServiceConversationScopedWebhookEnumMethod | 
  'configurationReplayAfter': 56, // Number | The message index for which and it's successors the webhook will be replayed. Not set by default
  'configurationTriggers': ["null"], // [String] | The list of keywords, firing webhook event for this Conversation.
  'configurationUrl': "configurationUrl_example" // String | The absolute url the webhook request should be sent to.
};
apiInstance.createServiceConversationScopedWebhook(chatServiceSid, conversationSid, target, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with. | 
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | 
 **target** | **ServiceConversationScopedWebhookEnumTarget**|  | 
 **configurationFilters** | [**[String]**](String.md)| The list of events, firing webhook event for this Conversation. | [optional] 
 **configurationFlowSid** | **String**| The studio flow SID, where the webhook should be sent to. | [optional] 
 **configurationMethod** | **ServiceConversationScopedWebhookEnumMethod**|  | [optional] 
 **configurationReplayAfter** | **Number**| The message index for which and it&#39;s successors the webhook will be replayed. Not set by default | [optional] 
 **configurationTriggers** | [**[String]**](String.md)| The list of keywords, firing webhook event for this Conversation. | [optional] 
 **configurationUrl** | **String**| The absolute url the webhook request should be sent to. | [optional] 

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook**](ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteConversationScopedWebhook

> deleteConversationScopedWebhook(conversationSid, sid)



Remove an existing webhook scoped to the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
apiInstance.deleteConversationScopedWebhook(conversationSid, sid, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteServiceConversationScopedWebhook

> deleteServiceConversationScopedWebhook(chatServiceSid, conversationSid, sid)



Remove an existing webhook scoped to the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
apiInstance.deleteServiceConversationScopedWebhook(chatServiceSid, conversationSid, sid, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with. | 
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchConfigurationWebhook

> ConversationsV1ConfigurationConfigurationWebhook fetchConfigurationWebhook()





### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
apiInstance.fetchConfigurationWebhook((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ConversationsV1ConfigurationConfigurationWebhook**](ConversationsV1ConfigurationConfigurationWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchConversationScopedWebhook

> ConversationsV1ConversationConversationScopedWebhook fetchConversationScopedWebhook(conversationSid, sid)



Fetch the configuration of a conversation-scoped webhook

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
apiInstance.fetchConversationScopedWebhook(conversationSid, sid, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 

### Return type

[**ConversationsV1ConversationConversationScopedWebhook**](ConversationsV1ConversationConversationScopedWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchServiceConversationScopedWebhook

> ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook fetchServiceConversationScopedWebhook(chatServiceSid, conversationSid, sid)



Fetch the configuration of a conversation-scoped webhook

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
apiInstance.fetchServiceConversationScopedWebhook(chatServiceSid, conversationSid, sid, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with. | 
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook**](ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchServiceWebhookConfiguration

> ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration fetchServiceWebhookConfiguration(chatServiceSid)



Fetch a specific service webhook configuration.

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
let chatServiceSid = "chatServiceSid_example"; // String | The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.
apiInstance.fetchServiceWebhookConfiguration(chatServiceSid, (error, data, response) => {
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
 **chatServiceSid** | **String**| The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to. | 

### Return type

[**ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration**](ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConversationScopedWebhook

> ListConversationScopedWebhookResponse listConversationScopedWebhook(conversationSid, opts)



Retrieve a list of all webhooks scoped to the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listConversationScopedWebhook(conversationSid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListConversationScopedWebhookResponse**](ListConversationScopedWebhookResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServiceConversationScopedWebhook

> ListServiceConversationScopedWebhookResponse listServiceConversationScopedWebhook(chatServiceSid, conversationSid, opts)



Retrieve a list of all webhooks scoped to the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listServiceConversationScopedWebhook(chatServiceSid, conversationSid, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with. | 
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListServiceConversationScopedWebhookResponse**](ListServiceConversationScopedWebhookResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateConfigurationWebhook

> ConversationsV1ConfigurationConfigurationWebhook updateConfigurationWebhook(opts)





### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
let opts = {
  'filters': ["null"], // [String] | The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`
  'method': "method_example", // String | The HTTP method to be used when sending a webhook request.
  'postWebhookUrl': "postWebhookUrl_example", // String | The absolute url the post-event webhook request should be sent to.
  'preWebhookUrl': "preWebhookUrl_example", // String | The absolute url the pre-event webhook request should be sent to.
  'target': "target_example" // ConfigurationWebhookEnumTarget | 
};
apiInstance.updateConfigurationWebhook(opts, (error, data, response) => {
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
 **filters** | [**[String]**](String.md)| The list of webhook event triggers that are enabled for this Service: &#x60;onMessageAdded&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onParticipantRemoved&#x60; | [optional] 
 **method** | **String**| The HTTP method to be used when sending a webhook request. | [optional] 
 **postWebhookUrl** | **String**| The absolute url the post-event webhook request should be sent to. | [optional] 
 **preWebhookUrl** | **String**| The absolute url the pre-event webhook request should be sent to. | [optional] 
 **target** | **ConfigurationWebhookEnumTarget**|  | [optional] 

### Return type

[**ConversationsV1ConfigurationConfigurationWebhook**](ConversationsV1ConfigurationConfigurationWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## updateConversationScopedWebhook

> ConversationsV1ConversationConversationScopedWebhook updateConversationScopedWebhook(conversationSid, sid, opts)



Update an existing conversation-scoped webhook

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
let opts = {
  'configurationFilters': ["null"], // [String] | The list of events, firing webhook event for this Conversation.
  'configurationFlowSid': "configurationFlowSid_example", // String | The studio flow SID, where the webhook should be sent to.
  'configurationMethod': "configurationMethod_example", // ConversationScopedWebhookEnumMethod | 
  'configurationTriggers': ["null"], // [String] | The list of keywords, firing webhook event for this Conversation.
  'configurationUrl': "configurationUrl_example" // String | The absolute url the webhook request should be sent to.
};
apiInstance.updateConversationScopedWebhook(conversationSid, sid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 
 **configurationFilters** | [**[String]**](String.md)| The list of events, firing webhook event for this Conversation. | [optional] 
 **configurationFlowSid** | **String**| The studio flow SID, where the webhook should be sent to. | [optional] 
 **configurationMethod** | **ConversationScopedWebhookEnumMethod**|  | [optional] 
 **configurationTriggers** | [**[String]**](String.md)| The list of keywords, firing webhook event for this Conversation. | [optional] 
 **configurationUrl** | **String**| The absolute url the webhook request should be sent to. | [optional] 

### Return type

[**ConversationsV1ConversationConversationScopedWebhook**](ConversationsV1ConversationConversationScopedWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## updateServiceConversationScopedWebhook

> ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook updateServiceConversationScopedWebhook(chatServiceSid, conversationSid, sid, opts)



Update an existing conversation-scoped webhook

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
let opts = {
  'configurationFilters': ["null"], // [String] | The list of events, firing webhook event for this Conversation.
  'configurationFlowSid': "configurationFlowSid_example", // String | The studio flow SID, where the webhook should be sent to.
  'configurationMethod': "configurationMethod_example", // ServiceConversationScopedWebhookEnumMethod | 
  'configurationTriggers': ["null"], // [String] | The list of keywords, firing webhook event for this Conversation.
  'configurationUrl': "configurationUrl_example" // String | The absolute url the webhook request should be sent to.
};
apiInstance.updateServiceConversationScopedWebhook(chatServiceSid, conversationSid, sid, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with. | 
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 
 **configurationFilters** | [**[String]**](String.md)| The list of events, firing webhook event for this Conversation. | [optional] 
 **configurationFlowSid** | **String**| The studio flow SID, where the webhook should be sent to. | [optional] 
 **configurationMethod** | **ServiceConversationScopedWebhookEnumMethod**|  | [optional] 
 **configurationTriggers** | [**[String]**](String.md)| The list of keywords, firing webhook event for this Conversation. | [optional] 
 **configurationUrl** | **String**| The absolute url the webhook request should be sent to. | [optional] 

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook**](ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## updateServiceWebhookConfiguration

> ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration updateServiceWebhookConfiguration(chatServiceSid, opts)



Update a specific Webhook.

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1WebhookApi();
let chatServiceSid = "chatServiceSid_example"; // String | The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.
let opts = {
  'filters': ["null"], // [String] | The list of events that your configured webhook targets will receive. Events not configured here will not fire. Possible values are `onParticipantAdd`, `onParticipantAdded`, `onDeliveryUpdated`, `onConversationUpdated`, `onConversationRemove`, `onParticipantRemove`, `onConversationUpdate`, `onMessageAdd`, `onMessageRemoved`, `onParticipantUpdated`, `onConversationAdded`, `onMessageAdded`, `onConversationAdd`, `onConversationRemoved`, `onParticipantUpdate`, `onMessageRemove`, `onMessageUpdated`, `onParticipantRemoved`, `onMessageUpdate` or `onConversationStateUpdated`.
  'method': "method_example", // String | The HTTP method to be used when sending a webhook request. One of `GET` or `POST`.
  'postWebhookUrl': "postWebhookUrl_example", // String | The absolute url the post-event webhook request should be sent to.
  'preWebhookUrl': "preWebhookUrl_example" // String | The absolute url the pre-event webhook request should be sent to.
};
apiInstance.updateServiceWebhookConfiguration(chatServiceSid, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to. | 
 **filters** | [**[String]**](String.md)| The list of events that your configured webhook targets will receive. Events not configured here will not fire. Possible values are &#x60;onParticipantAdd&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onDeliveryUpdated&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationRemove&#x60;, &#x60;onParticipantRemove&#x60;, &#x60;onConversationUpdate&#x60;, &#x60;onMessageAdd&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onConversationAdded&#x60;, &#x60;onMessageAdded&#x60;, &#x60;onConversationAdd&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantUpdate&#x60;, &#x60;onMessageRemove&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onParticipantRemoved&#x60;, &#x60;onMessageUpdate&#x60; or &#x60;onConversationStateUpdated&#x60;. | [optional] 
 **method** | **String**| The HTTP method to be used when sending a webhook request. One of &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **postWebhookUrl** | **String**| The absolute url the post-event webhook request should be sent to. | [optional] 
 **preWebhookUrl** | **String**| The absolute url the pre-event webhook request should be sent to. | [optional] 

### Return type

[**ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration**](ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

