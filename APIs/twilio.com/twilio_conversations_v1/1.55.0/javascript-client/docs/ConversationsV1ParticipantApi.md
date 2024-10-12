# TwilioConversations.ConversationsV1ParticipantApi

All URIs are relative to *https://conversations.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createConversationParticipant**](ConversationsV1ParticipantApi.md#createConversationParticipant) | **POST** /v1/Conversations/{ConversationSid}/Participants | 
[**createServiceConversationParticipant**](ConversationsV1ParticipantApi.md#createServiceConversationParticipant) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants | 
[**deleteConversationParticipant**](ConversationsV1ParticipantApi.md#deleteConversationParticipant) | **DELETE** /v1/Conversations/{ConversationSid}/Participants/{Sid} | 
[**deleteServiceConversationParticipant**](ConversationsV1ParticipantApi.md#deleteServiceConversationParticipant) | **DELETE** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid} | 
[**fetchConversationParticipant**](ConversationsV1ParticipantApi.md#fetchConversationParticipant) | **GET** /v1/Conversations/{ConversationSid}/Participants/{Sid} | 
[**fetchServiceConversationParticipant**](ConversationsV1ParticipantApi.md#fetchServiceConversationParticipant) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid} | 
[**listConversationParticipant**](ConversationsV1ParticipantApi.md#listConversationParticipant) | **GET** /v1/Conversations/{ConversationSid}/Participants | 
[**listServiceConversationParticipant**](ConversationsV1ParticipantApi.md#listServiceConversationParticipant) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants | 
[**updateConversationParticipant**](ConversationsV1ParticipantApi.md#updateConversationParticipant) | **POST** /v1/Conversations/{ConversationSid}/Participants/{Sid} | 
[**updateServiceConversationParticipant**](ConversationsV1ParticipantApi.md#updateServiceConversationParticipant) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid} | 



## createConversationParticipant

> ConversationsV1ConversationConversationParticipant createConversationParticipant(conversationSid, opts)



Add a new participant to the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ParticipantApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ConversationParticipantEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was created.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was last updated.
  'identity': "identity_example", // String | A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
  'messagingBindingAddress': "messagingBindingAddress_example", // String | The address of the participant's device, e.g. a phone or WhatsApp number. Together with the Proxy address, this determines a participant uniquely. This field (with proxy_address) is only null when the participant is interacting from an SDK endpoint (see the 'identity' field).
  'messagingBindingProjectedAddress': "messagingBindingProjectedAddress_example", // String | The address of the Twilio phone number that is used in Group MMS. Communication mask for the Conversation participant with Identity.
  'messagingBindingProxyAddress': "messagingBindingProxyAddress_example", // String | The address of the Twilio phone number (or WhatsApp number) that the participant is in contact with. This field, together with participant address, is only null when the participant is interacting from an SDK endpoint (see the 'identity' field).
  'roleSid': "roleSid_example" // String | The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
};
apiInstance.createConversationParticipant(conversationSid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | 
 **xTwilioWebhookEnabled** | **ConversationParticipantEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] 
 **dateCreated** | **Date**| The date that this resource was created. | [optional] 
 **dateUpdated** | **Date**| The date that this resource was last updated. | [optional] 
 **identity** | **String**| A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters. | [optional] 
 **messagingBindingAddress** | **String**| The address of the participant&#39;s device, e.g. a phone or WhatsApp number. Together with the Proxy address, this determines a participant uniquely. This field (with proxy_address) is only null when the participant is interacting from an SDK endpoint (see the &#39;identity&#39; field). | [optional] 
 **messagingBindingProjectedAddress** | **String**| The address of the Twilio phone number that is used in Group MMS. Communication mask for the Conversation participant with Identity. | [optional] 
 **messagingBindingProxyAddress** | **String**| The address of the Twilio phone number (or WhatsApp number) that the participant is in contact with. This field, together with participant address, is only null when the participant is interacting from an SDK endpoint (see the &#39;identity&#39; field). | [optional] 
 **roleSid** | **String**| The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant. | [optional] 

### Return type

[**ConversationsV1ConversationConversationParticipant**](ConversationsV1ConversationConversationParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## createServiceConversationParticipant

> ConversationsV1ServiceServiceConversationServiceConversationParticipant createServiceConversationParticipant(chatServiceSid, conversationSid, opts)



Add a new participant to the conversation in a specific service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ParticipantApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ServiceConversationParticipantEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set `{}` will be returned.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date on which this resource was created.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date on which this resource was last updated.
  'identity': "identity_example", // String | A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the [Conversation SDK](https://www.twilio.com/docs/conversations/sdk-overview) to communicate. Limited to 256 characters.
  'messagingBindingAddress': "messagingBindingAddress_example", // String | The address of the participant's device, e.g. a phone or WhatsApp number. Together with the Proxy address, this determines a participant uniquely. This field (with `proxy_address`) is only null when the participant is interacting from an SDK endpoint (see the `identity` field).
  'messagingBindingProjectedAddress': "messagingBindingProjectedAddress_example", // String | The address of the Twilio phone number that is used in Group MMS.
  'messagingBindingProxyAddress': "messagingBindingProxyAddress_example", // String | The address of the Twilio phone number (or WhatsApp number) that the participant is in contact with. This field, together with participant address, is only null when the participant is interacting from an SDK endpoint (see the `identity` field).
  'roleSid': "roleSid_example" // String | The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
};
apiInstance.createServiceConversationParticipant(chatServiceSid, conversationSid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | 
 **xTwilioWebhookEnabled** | **ServiceConversationParticipantEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set &#x60;{}&#x60; will be returned. | [optional] 
 **dateCreated** | **Date**| The date on which this resource was created. | [optional] 
 **dateUpdated** | **Date**| The date on which this resource was last updated. | [optional] 
 **identity** | **String**| A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the [Conversation SDK](https://www.twilio.com/docs/conversations/sdk-overview) to communicate. Limited to 256 characters. | [optional] 
 **messagingBindingAddress** | **String**| The address of the participant&#39;s device, e.g. a phone or WhatsApp number. Together with the Proxy address, this determines a participant uniquely. This field (with &#x60;proxy_address&#x60;) is only null when the participant is interacting from an SDK endpoint (see the &#x60;identity&#x60; field). | [optional] 
 **messagingBindingProjectedAddress** | **String**| The address of the Twilio phone number that is used in Group MMS. | [optional] 
 **messagingBindingProxyAddress** | **String**| The address of the Twilio phone number (or WhatsApp number) that the participant is in contact with. This field, together with participant address, is only null when the participant is interacting from an SDK endpoint (see the &#x60;identity&#x60; field). | [optional] 
 **roleSid** | **String**| The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant. | [optional] 

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationParticipant**](ConversationsV1ServiceServiceConversationServiceConversationParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteConversationParticipant

> deleteConversationParticipant(conversationSid, sid, opts)



Remove a participant from the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ParticipantApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // ConversationParticipantEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteConversationParticipant(conversationSid, sid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 
 **xTwilioWebhookEnabled** | **ConversationParticipantEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteServiceConversationParticipant

> deleteServiceConversationParticipant(chatServiceSid, conversationSid, sid, opts)



Remove a participant from the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ParticipantApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // ServiceConversationParticipantEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteServiceConversationParticipant(chatServiceSid, conversationSid, sid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 
 **xTwilioWebhookEnabled** | **ServiceConversationParticipantEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchConversationParticipant

> ConversationsV1ConversationConversationParticipant fetchConversationParticipant(conversationSid, sid)



Fetch a participant of the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ParticipantApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Alternatively, you can pass a Participant's `identity` rather than the SID.
apiInstance.fetchConversationParticipant(conversationSid, sid, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. Alternatively, you can pass a Participant&#39;s &#x60;identity&#x60; rather than the SID. | 

### Return type

[**ConversationsV1ConversationConversationParticipant**](ConversationsV1ConversationConversationParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchServiceConversationParticipant

> ConversationsV1ServiceServiceConversationServiceConversationParticipant fetchServiceConversationParticipant(chatServiceSid, conversationSid, sid)



Fetch a participant of the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ParticipantApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Alternatively, you can pass a Participant's `identity` rather than the SID.
apiInstance.fetchServiceConversationParticipant(chatServiceSid, conversationSid, sid, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. Alternatively, you can pass a Participant&#39;s &#x60;identity&#x60; rather than the SID. | 

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationParticipant**](ConversationsV1ServiceServiceConversationServiceConversationParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConversationParticipant

> ListConversationParticipantResponse listConversationParticipant(conversationSid, opts)



Retrieve a list of all participants of the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ParticipantApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for participants.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listConversationParticipant(conversationSid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for participants. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListConversationParticipantResponse**](ListConversationParticipantResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServiceConversationParticipant

> ListServiceConversationParticipantResponse listServiceConversationParticipant(chatServiceSid, conversationSid, opts)



Retrieve a list of all participants of the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ParticipantApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for participants.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listServiceConversationParticipant(chatServiceSid, conversationSid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for participants. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListServiceConversationParticipantResponse**](ListServiceConversationParticipantResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateConversationParticipant

> ConversationsV1ConversationConversationParticipant updateConversationParticipant(conversationSid, sid, opts)



Update an existing participant in the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ParticipantApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ConversationParticipantEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was created.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was last updated.
  'identity': "identity_example", // String | A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
  'lastReadMessageIndex': 56, // Number | Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
  'lastReadTimestamp': "lastReadTimestamp_example", // String | Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
  'messagingBindingProjectedAddress': "messagingBindingProjectedAddress_example", // String | The address of the Twilio phone number that is used in Group MMS. 'null' value will remove it.
  'messagingBindingProxyAddress': "messagingBindingProxyAddress_example", // String | The address of the Twilio phone number that the participant is in contact with. 'null' value will remove it.
  'roleSid': "roleSid_example" // String | The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
};
apiInstance.updateConversationParticipant(conversationSid, sid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 
 **xTwilioWebhookEnabled** | **ConversationParticipantEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] 
 **dateCreated** | **Date**| The date that this resource was created. | [optional] 
 **dateUpdated** | **Date**| The date that this resource was last updated. | [optional] 
 **identity** | **String**| A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters. | [optional] 
 **lastReadMessageIndex** | **Number**| Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant. | [optional] 
 **lastReadTimestamp** | **String**| Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant. | [optional] 
 **messagingBindingProjectedAddress** | **String**| The address of the Twilio phone number that is used in Group MMS. &#39;null&#39; value will remove it. | [optional] 
 **messagingBindingProxyAddress** | **String**| The address of the Twilio phone number that the participant is in contact with. &#39;null&#39; value will remove it. | [optional] 
 **roleSid** | **String**| The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant. | [optional] 

### Return type

[**ConversationsV1ConversationConversationParticipant**](ConversationsV1ConversationConversationParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## updateServiceConversationParticipant

> ConversationsV1ServiceServiceConversationServiceConversationParticipant updateServiceConversationParticipant(chatServiceSid, conversationSid, sid, opts)



Update an existing participant in the conversation

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ParticipantApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ServiceConversationParticipantEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set `{}` will be returned.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date on which this resource was created.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date on which this resource was last updated.
  'identity': "identity_example", // String | A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the [Conversation SDK](https://www.twilio.com/docs/conversations/sdk-overview) to communicate. Limited to 256 characters.
  'lastReadMessageIndex': 56, // Number | Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
  'lastReadTimestamp': "lastReadTimestamp_example", // String | Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
  'messagingBindingProjectedAddress': "messagingBindingProjectedAddress_example", // String | The address of the Twilio phone number that is used in Group MMS. 'null' value will remove it.
  'messagingBindingProxyAddress': "messagingBindingProxyAddress_example", // String | The address of the Twilio phone number that the participant is in contact with. 'null' value will remove it.
  'roleSid': "roleSid_example" // String | The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
};
apiInstance.updateServiceConversationParticipant(chatServiceSid, conversationSid, sid, opts, (error, data, response) => {
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
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 
 **xTwilioWebhookEnabled** | **ServiceConversationParticipantEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set &#x60;{}&#x60; will be returned. | [optional] 
 **dateCreated** | **Date**| The date on which this resource was created. | [optional] 
 **dateUpdated** | **Date**| The date on which this resource was last updated. | [optional] 
 **identity** | **String**| A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the [Conversation SDK](https://www.twilio.com/docs/conversations/sdk-overview) to communicate. Limited to 256 characters. | [optional] 
 **lastReadMessageIndex** | **Number**| Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant. | [optional] 
 **lastReadTimestamp** | **String**| Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant. | [optional] 
 **messagingBindingProjectedAddress** | **String**| The address of the Twilio phone number that is used in Group MMS. &#39;null&#39; value will remove it. | [optional] 
 **messagingBindingProxyAddress** | **String**| The address of the Twilio phone number that the participant is in contact with. &#39;null&#39; value will remove it. | [optional] 
 **roleSid** | **String**| The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant. | [optional] 

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationParticipant**](ConversationsV1ServiceServiceConversationServiceConversationParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

