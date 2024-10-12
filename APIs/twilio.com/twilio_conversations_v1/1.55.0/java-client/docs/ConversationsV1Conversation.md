

# ConversationsV1Conversation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this conversation. |  [optional] |
|**attributes** | **String** | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \&quot;{}\&quot; will be returned. |  [optional] |
|**bindings** | **Object** |  |  [optional] |
|**chatServiceSid** | **String** | The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date that this resource was created. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date that this resource was last updated. |  [optional] |
|**friendlyName** | **String** | The human-readable name of this conversation, limited to 256 characters. Optional. |  [optional] |
|**links** | **Object** | Contains absolute URLs to access the [participants](https://www.twilio.com/docs/conversations/api/conversation-participant-resource), [messages](https://www.twilio.com/docs/conversations/api/conversation-message-resource) and [webhooks](https://www.twilio.com/docs/conversations/api/conversation-scoped-webhook-resource) of this conversation. |  [optional] |
|**messagingServiceSid** | **String** | The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to. |  [optional] |
|**sid** | **String** | A 34 character string that uniquely identifies this resource. |  [optional] |
|**state** | **ConversationEnumState** |  |  [optional] |
|**timers** | **Object** | Timer date values representing state update for this conversation. |  [optional] |
|**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. |  [optional] |
|**url** | **URI** | An absolute API resource URL for this conversation. |  [optional] |



