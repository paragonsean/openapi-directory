# TwilioConversations.ConversationsV1ConfigurationConfigurationWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this conversation. | [optional] 
**filters** | **[String]** | The list of webhook event triggers that are enabled for this Service: &#x60;onMessageAdded&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onParticipantRemoved&#x60; | [optional] 
**method** | [**ConfigurationWebhookEnumMethod**](ConfigurationWebhookEnumMethod.md) |  | [optional] 
**postWebhookUrl** | **String** | The absolute url the post-event webhook request should be sent to. | [optional] 
**preWebhookUrl** | **String** | The absolute url the pre-event webhook request should be sent to. | [optional] 
**target** | [**ConfigurationWebhookEnumTarget**](ConfigurationWebhookEnumTarget.md) |  | [optional] 
**url** | **String** | An absolute API resource API resource URL for this webhook. | [optional] 


