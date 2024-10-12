

# ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this service. |  [optional] |
|**chatServiceSid** | **String** | The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to. |  [optional] |
|**filters** | **List&lt;String&gt;** | The list of events that your configured webhook targets will receive. Events not configured here will not fire. Possible values are &#x60;onParticipantAdd&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onDeliveryUpdated&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationRemove&#x60;, &#x60;onParticipantRemove&#x60;, &#x60;onConversationUpdate&#x60;, &#x60;onMessageAdd&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onConversationAdded&#x60;, &#x60;onMessageAdded&#x60;, &#x60;onConversationAdd&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantUpdate&#x60;, &#x60;onMessageRemove&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onParticipantRemoved&#x60;, &#x60;onMessageUpdate&#x60; or &#x60;onConversationStateUpdated&#x60;. |  [optional] |
|**method** | **ServiceWebhookConfigurationEnumMethod** |  |  [optional] |
|**postWebhookUrl** | **URI** | The absolute url the post-event webhook request should be sent to. |  [optional] |
|**preWebhookUrl** | **URI** | The absolute url the pre-event webhook request should be sent to. |  [optional] |
|**url** | **URI** | An absolute API resource URL for this webhook. |  [optional] |



