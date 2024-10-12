# TwilioConversations.ConversationsV1ServiceServiceParticipantConversation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this conversation. | [optional] 
**chatServiceSid** | **String** | The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to. | [optional] 
**conversationAttributes** | **String** | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \&quot;{}\&quot; will be returned. | [optional] 
**conversationCreatedBy** | **String** | Identity of the creator of this Conversation. | [optional] 
**conversationDateCreated** | **Date** | The date that this conversation was created, given in ISO 8601 format. | [optional] 
**conversationDateUpdated** | **Date** | The date that this conversation was last updated, given in ISO 8601 format. | [optional] 
**conversationFriendlyName** | **String** | The human-readable name of this conversation, limited to 256 characters. Optional. | [optional] 
**conversationSid** | **String** | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) this Participant belongs to. | [optional] 
**conversationState** | [**ServiceParticipantConversationEnumState**](ServiceParticipantConversationEnumState.md) |  | [optional] 
**conversationTimers** | **Object** | Timer date values representing state update for this conversation. | [optional] 
**conversationUniqueName** | **String** | An application-defined string that uniquely identifies the Conversation resource. | [optional] 
**links** | **Object** | Contains absolute URLs to access the [participant](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) and [conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) of this conversation. | [optional] 
**participantIdentity** | **String** | A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters. | [optional] 
**participantMessagingBinding** | **Object** | Information about how this participant exchanges messages with the conversation. A JSON parameter consisting of type and address fields of the participant. | [optional] 
**participantSid** | **String** | The unique ID of the [Participant](https://www.twilio.com/docs/conversations/api/conversation-participant-resource). | [optional] 
**participantUserSid** | **String** | The unique string that identifies the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). | [optional] 


