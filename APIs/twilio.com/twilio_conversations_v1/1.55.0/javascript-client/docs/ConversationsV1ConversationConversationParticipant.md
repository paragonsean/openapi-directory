# TwilioConversations.ConversationsV1ConversationConversationParticipant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this participant. | [optional] 
**attributes** | **String** | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \&quot;{}\&quot; will be returned. | [optional] 
**conversationSid** | **String** | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | [optional] 
**dateCreated** | **Date** | The date that this resource was created. | [optional] 
**dateUpdated** | **Date** | The date that this resource was last updated. | [optional] 
**identity** | **String** | A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters. | [optional] 
**lastReadMessageIndex** | **Number** | Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant. | [optional] 
**lastReadTimestamp** | **String** | Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant. | [optional] 
**messagingBinding** | **Object** | Information about how this participant exchanges messages with the conversation. A JSON parameter consisting of type and address fields of the participant. | [optional] 
**roleSid** | **String** | The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant. | [optional] 
**sid** | **String** | A 34 character string that uniquely identifies this resource. | [optional] 
**url** | **String** | An absolute API resource URL for this participant. | [optional] 


