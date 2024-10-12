

# ConversationsV1ConversationConversationMessageConversationMessageReceipt


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this participant. |  [optional] |
|**channelMessageSid** | **String** | A messaging channel-specific identifier for the message delivered to participant e.g. &#x60;SMxx&#x60; for SMS, &#x60;WAxx&#x60; for Whatsapp etc.  |  [optional] |
|**conversationSid** | **String** | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date that this resource was created. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date that this resource was last updated. &#x60;null&#x60; if the delivery receipt has not been updated. |  [optional] |
|**errorCode** | **Integer** | The message [delivery error code](https://www.twilio.com/docs/sms/api/message-resource#delivery-related-errors) for a &#x60;failed&#x60; status,  |  [optional] |
|**messageSid** | **String** | The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to |  [optional] |
|**participantSid** | **String** | The unique ID of the participant the delivery receipt belongs to. |  [optional] |
|**sid** | **String** | A 34 character string that uniquely identifies this resource. |  [optional] |
|**status** | **ConversationMessageReceiptEnumDeliveryStatus** |  |  [optional] |
|**url** | **URI** | An absolute API resource URL for this delivery receipt. |  [optional] |



