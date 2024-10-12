

# GoogleCloudDialogflowV2NotificationConfig

Defines notification behavior.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messageFormat** | [**MessageFormatEnum**](#MessageFormatEnum) | Format of message. |  [optional] |
|**topic** | **String** | Name of the Pub/Sub topic to publish conversation events like CONVERSATION_STARTED as serialized ConversationEvent protos. For telephony integration to receive notification, make sure either this topic is in the same project as the conversation or you grant &#x60;service-@gcp-sa-dialogflow.iam.gserviceaccount.com&#x60; the &#x60;Dialogflow Service Agent&#x60; role in the topic project. For chat integration to receive notification, make sure API caller has been granted the &#x60;Dialogflow Service Agent&#x60; role for the topic. Format: &#x60;projects//locations//topics/&#x60;. |  [optional] |



## Enum: MessageFormatEnum

| Name | Value |
|---- | -----|
| MESSAGE_FORMAT_UNSPECIFIED | &quot;MESSAGE_FORMAT_UNSPECIFIED&quot; |
| PROTO | &quot;PROTO&quot; |
| JSON | &quot;JSON&quot; |



