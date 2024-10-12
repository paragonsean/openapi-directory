# TwilioConversations.ConversationsV1MessageApi

All URIs are relative to *https://conversations.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createConversationMessage**](ConversationsV1MessageApi.md#createConversationMessage) | **POST** /v1/Conversations/{ConversationSid}/Messages | 
[**createServiceConversationMessage**](ConversationsV1MessageApi.md#createServiceConversationMessage) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages | 
[**deleteConversationMessage**](ConversationsV1MessageApi.md#deleteConversationMessage) | **DELETE** /v1/Conversations/{ConversationSid}/Messages/{Sid} | 
[**deleteServiceConversationMessage**](ConversationsV1MessageApi.md#deleteServiceConversationMessage) | **DELETE** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid} | 
[**fetchConversationMessage**](ConversationsV1MessageApi.md#fetchConversationMessage) | **GET** /v1/Conversations/{ConversationSid}/Messages/{Sid} | 
[**fetchServiceConversationMessage**](ConversationsV1MessageApi.md#fetchServiceConversationMessage) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid} | 
[**listConversationMessage**](ConversationsV1MessageApi.md#listConversationMessage) | **GET** /v1/Conversations/{ConversationSid}/Messages | 
[**listServiceConversationMessage**](ConversationsV1MessageApi.md#listServiceConversationMessage) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages | 
[**updateConversationMessage**](ConversationsV1MessageApi.md#updateConversationMessage) | **POST** /v1/Conversations/{ConversationSid}/Messages/{Sid} | 
[**updateServiceConversationMessage**](ConversationsV1MessageApi.md#updateServiceConversationMessage) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid} | 



## createConversationMessage

> ConversationsV1ConversationConversationMessage createConversationMessage(conversationSid, opts)



Add a new message to the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1MessageApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ConversationMessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
  'author': "author_example", // String | The channel specific identifier of the message's author. Defaults to `system`.
  'body': "body_example", // String | The content of the message, can be up to 1,600 characters long.
  'contentSid': "contentSid_example", // String | The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content) template, required for template-generated messages.  **Note** that if this field is set, `Body` and `MediaSid` parameters are ignored.
  'contentVariables': "contentVariables_example", // String | A structurally valid JSON string that contains values to resolve Rich Content template variables.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was created.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was last updated. `null` if the message has not been edited.
  'mediaSid': "mediaSid_example", // String | The Media SID to be attached to the new Message.
  'subject': "subject_example" // String | The subject of the message, can be up to 256 characters long.
};
apiInstance.createConversationMessage(conversationSid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | 
 **xTwilioWebhookEnabled** | **ConversationMessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] 
 **author** | **String**| The channel specific identifier of the message&#39;s author. Defaults to &#x60;system&#x60;. | [optional] 
 **body** | **String**| The content of the message, can be up to 1,600 characters long. | [optional] 
 **contentSid** | **String**| The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content) template, required for template-generated messages.  **Note** that if this field is set, &#x60;Body&#x60; and &#x60;MediaSid&#x60; parameters are ignored. | [optional] 
 **contentVariables** | **String**| A structurally valid JSON string that contains values to resolve Rich Content template variables. | [optional] 
 **dateCreated** | **Date**| The date that this resource was created. | [optional] 
 **dateUpdated** | **Date**| The date that this resource was last updated. &#x60;null&#x60; if the message has not been edited. | [optional] 
 **mediaSid** | **String**| The Media SID to be attached to the new Message. | [optional] 
 **subject** | **String**| The subject of the message, can be up to 256 characters long. | [optional] 

### Return type

[**ConversationsV1ConversationConversationMessage**](ConversationsV1ConversationConversationMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## createServiceConversationMessage

> ConversationsV1ServiceServiceConversationServiceConversationMessage createServiceConversationMessage(chatServiceSid, conversationSid, opts)



Add a new message to the conversation in a specific service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1MessageApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ServiceConversationMessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
  'author': "author_example", // String | The channel specific identifier of the message's author. Defaults to `system`.
  'body': "body_example", // String | The content of the message, can be up to 1,600 characters long.
  'contentSid': "contentSid_example", // String | The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content) template, required for template-generated messages.  **Note** that if this field is set, `Body` and `MediaSid` parameters are ignored.
  'contentVariables': "contentVariables_example", // String | A structurally valid JSON string that contains values to resolve Rich Content template variables.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was created.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was last updated. `null` if the message has not been edited.
  'mediaSid': "mediaSid_example", // String | The Media SID to be attached to the new Message.
  'subject': "subject_example" // String | The subject of the message, can be up to 256 characters long.
};
apiInstance.createServiceConversationMessage(chatServiceSid, conversationSid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | 
 **xTwilioWebhookEnabled** | **ServiceConversationMessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] 
 **author** | **String**| The channel specific identifier of the message&#39;s author. Defaults to &#x60;system&#x60;. | [optional] 
 **body** | **String**| The content of the message, can be up to 1,600 characters long. | [optional] 
 **contentSid** | **String**| The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content) template, required for template-generated messages.  **Note** that if this field is set, &#x60;Body&#x60; and &#x60;MediaSid&#x60; parameters are ignored. | [optional] 
 **contentVariables** | **String**| A structurally valid JSON string that contains values to resolve Rich Content template variables. | [optional] 
 **dateCreated** | **Date**| The date that this resource was created. | [optional] 
 **dateUpdated** | **Date**| The date that this resource was last updated. &#x60;null&#x60; if the message has not been edited. | [optional] 
 **mediaSid** | **String**| The Media SID to be attached to the new Message. | [optional] 
 **subject** | **String**| The subject of the message, can be up to 256 characters long. | [optional] 

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationMessage**](ConversationsV1ServiceServiceConversationServiceConversationMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteConversationMessage

> deleteConversationMessage(conversationSid, sid, opts)



Remove a message from the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1MessageApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // ConversationMessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteConversationMessage(conversationSid, sid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 
 **xTwilioWebhookEnabled** | **ConversationMessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteServiceConversationMessage

> deleteServiceConversationMessage(chatServiceSid, conversationSid, sid, opts)



Remove a message from the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1MessageApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // ServiceConversationMessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteServiceConversationMessage(chatServiceSid, conversationSid, sid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 
 **xTwilioWebhookEnabled** | **ServiceConversationMessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchConversationMessage

> ConversationsV1ConversationConversationMessage fetchConversationMessage(conversationSid, sid)



Fetch a message from the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1MessageApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
apiInstance.fetchConversationMessage(conversationSid, sid, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 

### Return type

[**ConversationsV1ConversationConversationMessage**](ConversationsV1ConversationConversationMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchServiceConversationMessage

> ConversationsV1ServiceServiceConversationServiceConversationMessage fetchServiceConversationMessage(chatServiceSid, conversationSid, sid)



Fetch a message from the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1MessageApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
apiInstance.fetchServiceConversationMessage(chatServiceSid, conversationSid, sid, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationMessage**](ConversationsV1ServiceServiceConversationServiceConversationMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConversationMessage

> ListConversationMessageResponse listConversationMessage(conversationSid, opts)



Retrieve a list of all messages in the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1MessageApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for messages.
let opts = {
  'order': "order_example", // ConversationMessageEnumOrderType | The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listConversationMessage(conversationSid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for messages. | 
 **order** | **ConversationMessageEnumOrderType**| The sort order of the returned messages. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending), with &#x60;asc&#x60; as the default. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListConversationMessageResponse**](ListConversationMessageResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServiceConversationMessage

> ListServiceConversationMessageResponse listServiceConversationMessage(chatServiceSid, conversationSid, opts)



Retrieve a list of all messages in the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1MessageApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for messages.
let opts = {
  'order': "order_example", // ServiceConversationMessageEnumOrderType | The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listServiceConversationMessage(chatServiceSid, conversationSid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for messages. | 
 **order** | **ServiceConversationMessageEnumOrderType**| The sort order of the returned messages. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending), with &#x60;asc&#x60; as the default. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListServiceConversationMessageResponse**](ListServiceConversationMessageResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateConversationMessage

> ConversationsV1ConversationConversationMessage updateConversationMessage(conversationSid, sid, opts)



Update an existing message in the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1MessageApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ConversationMessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
  'author': "author_example", // String | The channel specific identifier of the message's author. Defaults to `system`.
  'body': "body_example", // String | The content of the message, can be up to 1,600 characters long.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was created.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was last updated. `null` if the message has not been edited.
  'subject': "subject_example" // String | The subject of the message, can be up to 256 characters long.
};
apiInstance.updateConversationMessage(conversationSid, sid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 
 **xTwilioWebhookEnabled** | **ConversationMessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] 
 **author** | **String**| The channel specific identifier of the message&#39;s author. Defaults to &#x60;system&#x60;. | [optional] 
 **body** | **String**| The content of the message, can be up to 1,600 characters long. | [optional] 
 **dateCreated** | **Date**| The date that this resource was created. | [optional] 
 **dateUpdated** | **Date**| The date that this resource was last updated. &#x60;null&#x60; if the message has not been edited. | [optional] 
 **subject** | **String**| The subject of the message, can be up to 256 characters long. | [optional] 

### Return type

[**ConversationsV1ConversationConversationMessage**](ConversationsV1ConversationConversationMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## updateServiceConversationMessage

> ConversationsV1ServiceServiceConversationServiceConversationMessage updateServiceConversationMessage(chatServiceSid, conversationSid, sid, opts)



Update an existing message in the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1MessageApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ServiceConversationMessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
  'author': "author_example", // String | The channel specific identifier of the message's author. Defaults to `system`.
  'body': "body_example", // String | The content of the message, can be up to 1,600 characters long.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was created.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was last updated. `null` if the message has not been edited.
  'subject': "subject_example" // String | The subject of the message, can be up to 256 characters long.
};
apiInstance.updateServiceConversationMessage(chatServiceSid, conversationSid, sid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 
 **xTwilioWebhookEnabled** | **ServiceConversationMessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] 
 **author** | **String**| The channel specific identifier of the message&#39;s author. Defaults to &#x60;system&#x60;. | [optional] 
 **body** | **String**| The content of the message, can be up to 1,600 characters long. | [optional] 
 **dateCreated** | **Date**| The date that this resource was created. | [optional] 
 **dateUpdated** | **Date**| The date that this resource was last updated. &#x60;null&#x60; if the message has not been edited. | [optional] 
 **subject** | **String**| The subject of the message, can be up to 256 characters long. | [optional] 

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationMessage**](ConversationsV1ServiceServiceConversationServiceConversationMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

