# TwilioConversations.ConversationsV1UserUserConversation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this conversation. | [optional] 
**attributes** | **String** | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \&quot;{}\&quot; will be returned. | [optional] 
**chatServiceSid** | **String** | The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to. | [optional] 
**conversationSid** | **String** | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this User Conversation. | [optional] 
**conversationState** | [**UserConversationEnumState**](UserConversationEnumState.md) |  | [optional] 
**createdBy** | **String** | Identity of the creator of this Conversation. | [optional] 
**dateCreated** | **Date** | The date that this conversation was created, given in ISO 8601 format. | [optional] 
**dateUpdated** | **Date** | The date that this conversation was last updated, given in ISO 8601 format. | [optional] 
**friendlyName** | **String** | The human-readable name of this conversation, limited to 256 characters. Optional. | [optional] 
**lastReadMessageIndex** | **Number** | The index of the last Message in the Conversation that the Participant has read. | [optional] 
**links** | **Object** | Contains absolute URLs to access the [participant](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) and [conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) of this conversation. | [optional] 
**notificationLevel** | [**UserConversationEnumNotificationLevel**](UserConversationEnumNotificationLevel.md) |  | [optional] 
**participantSid** | **String** | The unique ID of the [participant](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) the user conversation belongs to. | [optional] 
**timers** | **Object** | Timer date values representing state update for this conversation. | [optional] 
**uniqueName** | **String** | An application-defined string that uniquely identifies the Conversation resource. It can be used to address the resource in place of the resource&#39;s &#x60;conversation_sid&#x60; in the URL. | [optional] 
**unreadMessagesCount** | **Number** | The number of unread Messages in the Conversation for the Participant. | [optional] 
**url** | **String** |  | [optional] 
**userSid** | **String** | The unique string that identifies the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). | [optional] 


