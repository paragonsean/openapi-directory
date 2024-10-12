# TwilioConversations.ConversationsV1NotificationApi

All URIs are relative to *https://conversations.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchServiceNotification**](ConversationsV1NotificationApi.md#fetchServiceNotification) | **GET** /v1/Services/{ChatServiceSid}/Configuration/Notifications | 
[**updateServiceNotification**](ConversationsV1NotificationApi.md#updateServiceNotification) | **POST** /v1/Services/{ChatServiceSid}/Configuration/Notifications | 



## fetchServiceNotification

> ConversationsV1ServiceServiceConfigurationServiceNotification fetchServiceNotification(chatServiceSid)



Fetch push notification service settings

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1NotificationApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Configuration applies to.
apiInstance.fetchServiceNotification(chatServiceSid, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Configuration applies to. | 

### Return type

[**ConversationsV1ServiceServiceConfigurationServiceNotification**](ConversationsV1ServiceServiceConfigurationServiceNotification.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateServiceNotification

> ConversationsV1ServiceServiceConfigurationServiceNotification updateServiceNotification(chatServiceSid, opts)



Update push notification service settings

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1NotificationApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Configuration applies to.
let opts = {
  'addedToConversationEnabled': true, // Boolean | Whether to send a notification when a participant is added to a conversation. The default is `false`.
  'addedToConversationSound': "addedToConversationSound_example", // String | The name of the sound to play when a participant is added to a conversation and `added_to_conversation.enabled` is `true`.
  'addedToConversationTemplate': "addedToConversationTemplate_example", // String | The template to use to create the notification text displayed when a participant is added to a conversation and `added_to_conversation.enabled` is `true`.
  'logEnabled': true, // Boolean | Weather the notification logging is enabled.
  'newMessageBadgeCountEnabled': true, // Boolean | Whether the new message badge is enabled. The default is `false`.
  'newMessageEnabled': true, // Boolean | Whether to send a notification when a new message is added to a conversation. The default is `false`.
  'newMessageSound': "newMessageSound_example", // String | The name of the sound to play when a new message is added to a conversation and `new_message.enabled` is `true`.
  'newMessageTemplate': "newMessageTemplate_example", // String | The template to use to create the notification text displayed when a new message is added to a conversation and `new_message.enabled` is `true`.
  'newMessageWithMediaEnabled': true, // Boolean | Whether to send a notification when a new message with media/file attachments is added to a conversation. The default is `false`.
  'newMessageWithMediaTemplate': "newMessageWithMediaTemplate_example", // String | The template to use to create the notification text displayed when a new message with media/file attachments is added to a conversation and `new_message.attachments.enabled` is `true`.
  'removedFromConversationEnabled': true, // Boolean | Whether to send a notification to a user when they are removed from a conversation. The default is `false`.
  'removedFromConversationSound': "removedFromConversationSound_example", // String | The name of the sound to play to a user when they are removed from a conversation and `removed_from_conversation.enabled` is `true`.
  'removedFromConversationTemplate': "removedFromConversationTemplate_example" // String | The template to use to create the notification text displayed to a user when they are removed from a conversation and `removed_from_conversation.enabled` is `true`.
};
apiInstance.updateServiceNotification(chatServiceSid, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Configuration applies to. | 
 **addedToConversationEnabled** | **Boolean**| Whether to send a notification when a participant is added to a conversation. The default is &#x60;false&#x60;. | [optional] 
 **addedToConversationSound** | **String**| The name of the sound to play when a participant is added to a conversation and &#x60;added_to_conversation.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **addedToConversationTemplate** | **String**| The template to use to create the notification text displayed when a participant is added to a conversation and &#x60;added_to_conversation.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **logEnabled** | **Boolean**| Weather the notification logging is enabled. | [optional] 
 **newMessageBadgeCountEnabled** | **Boolean**| Whether the new message badge is enabled. The default is &#x60;false&#x60;. | [optional] 
 **newMessageEnabled** | **Boolean**| Whether to send a notification when a new message is added to a conversation. The default is &#x60;false&#x60;. | [optional] 
 **newMessageSound** | **String**| The name of the sound to play when a new message is added to a conversation and &#x60;new_message.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **newMessageTemplate** | **String**| The template to use to create the notification text displayed when a new message is added to a conversation and &#x60;new_message.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **newMessageWithMediaEnabled** | **Boolean**| Whether to send a notification when a new message with media/file attachments is added to a conversation. The default is &#x60;false&#x60;. | [optional] 
 **newMessageWithMediaTemplate** | **String**| The template to use to create the notification text displayed when a new message with media/file attachments is added to a conversation and &#x60;new_message.attachments.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **removedFromConversationEnabled** | **Boolean**| Whether to send a notification to a user when they are removed from a conversation. The default is &#x60;false&#x60;. | [optional] 
 **removedFromConversationSound** | **String**| The name of the sound to play to a user when they are removed from a conversation and &#x60;removed_from_conversation.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **removedFromConversationTemplate** | **String**| The template to use to create the notification text displayed to a user when they are removed from a conversation and &#x60;removed_from_conversation.enabled&#x60; is &#x60;true&#x60;. | [optional] 

### Return type

[**ConversationsV1ServiceServiceConfigurationServiceNotification**](ConversationsV1ServiceServiceConfigurationServiceNotification.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

