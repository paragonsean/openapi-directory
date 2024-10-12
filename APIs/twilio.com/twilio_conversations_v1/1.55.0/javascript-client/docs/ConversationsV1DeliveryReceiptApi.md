# TwilioConversations.ConversationsV1DeliveryReceiptApi

All URIs are relative to *https://conversations.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchConversationMessageReceipt**](ConversationsV1DeliveryReceiptApi.md#fetchConversationMessageReceipt) | **GET** /v1/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts/{Sid} | 
[**fetchServiceConversationMessageReceipt**](ConversationsV1DeliveryReceiptApi.md#fetchServiceConversationMessageReceipt) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts/{Sid} | 
[**listConversationMessageReceipt**](ConversationsV1DeliveryReceiptApi.md#listConversationMessageReceipt) | **GET** /v1/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts | 
[**listServiceConversationMessageReceipt**](ConversationsV1DeliveryReceiptApi.md#listServiceConversationMessageReceipt) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts | 



## fetchConversationMessageReceipt

> ConversationsV1ConversationConversationMessageConversationMessageReceipt fetchConversationMessageReceipt(conversationSid, messageSid, sid)



Fetch the delivery and read receipts of the conversation message

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1DeliveryReceiptApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
let messageSid = "messageSid_example"; // String | The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
apiInstance.fetchConversationMessageReceipt(conversationSid, messageSid, sid, (error, data, response) => {
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
 **messageSid** | **String**| The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 

### Return type

[**ConversationsV1ConversationConversationMessageConversationMessageReceipt**](ConversationsV1ConversationConversationMessageConversationMessageReceipt.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchServiceConversationMessageReceipt

> ConversationsV1ServiceServiceConversationServiceConversationMessageServiceConversationMessageReceipt fetchServiceConversationMessageReceipt(chatServiceSid, conversationSid, messageSid, sid)



Fetch the delivery and read receipts of the conversation message

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1DeliveryReceiptApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Message resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
let messageSid = "messageSid_example"; // String | The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
apiInstance.fetchServiceConversationMessageReceipt(chatServiceSid, conversationSid, messageSid, sid, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Message resource is associated with. | 
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | 
 **messageSid** | **String**| The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. | 

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationMessageServiceConversationMessageReceipt**](ConversationsV1ServiceServiceConversationServiceConversationMessageServiceConversationMessageReceipt.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConversationMessageReceipt

> ListConversationMessageReceiptResponse listConversationMessageReceipt(conversationSid, messageSid, opts)



Retrieve a list of all delivery and read receipts of the conversation message

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1DeliveryReceiptApi();
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
let messageSid = "messageSid_example"; // String | The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listConversationMessageReceipt(conversationSid, messageSid, opts, (error, data, response) => {
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
 **messageSid** | **String**| The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListConversationMessageReceiptResponse**](ListConversationMessageReceiptResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServiceConversationMessageReceipt

> ListServiceConversationMessageReceiptResponse listServiceConversationMessageReceipt(chatServiceSid, conversationSid, messageSid, opts)



Retrieve a list of all delivery and read receipts of the conversation message

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1DeliveryReceiptApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Message resource is associated with.
let conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
let messageSid = "messageSid_example"; // String | The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listServiceConversationMessageReceipt(chatServiceSid, conversationSid, messageSid, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Message resource is associated with. | 
 **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | 
 **messageSid** | **String**| The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListServiceConversationMessageReceiptResponse**](ListServiceConversationMessageReceiptResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

