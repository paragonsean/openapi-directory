# TwilioConversations.ConversationsV1ServiceServiceConversationServiceConversationMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this message. | [optional] 
**attributes** | **String** | A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \&quot;{}\&quot; will be returned. | [optional] 
**author** | **String** | The channel specific identifier of the message&#39;s author. Defaults to &#x60;system&#x60;. | [optional] 
**body** | **String** | The content of the message, can be up to 1,600 characters long. | [optional] 
**chatServiceSid** | **String** | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with. | [optional] 
**contentSid** | **String** | The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content) template. | [optional] 
**conversationSid** | **String** | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | [optional] 
**dateCreated** | **Date** | The date that this resource was created. | [optional] 
**dateUpdated** | **Date** | The date that this resource was last updated. &#x60;null&#x60; if the message has not been edited. | [optional] 
**delivery** | **Object** | An object that contains the summary of delivery statuses for the message to non-chat participants. | [optional] 
**index** | **Number** | The index of the message within the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource). | [optional] 
**links** | **Object** | Contains an absolute API resource URL to access the delivery &amp; read receipts of this message. | [optional] 
**media** | **[Object]** | An array of objects that describe the Message&#39;s media, if the message contains media. Each object contains these fields: &#x60;content_type&#x60; with the MIME type of the media, &#x60;filename&#x60; with the name of the media, &#x60;sid&#x60; with the SID of the Media resource, and &#x60;size&#x60; with the media object&#39;s file size in bytes. If the Message has no media, this value is &#x60;null&#x60;. | [optional] 
**participantSid** | **String** | The unique ID of messages&#39;s author participant. Null in case of &#x60;system&#x60; sent message. | [optional] 
**sid** | **String** | A 34 character string that uniquely identifies this resource. | [optional] 
**url** | **String** | An absolute API resource URL for this message. | [optional] 


