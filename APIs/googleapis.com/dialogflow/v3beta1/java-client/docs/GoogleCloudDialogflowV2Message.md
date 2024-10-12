

# GoogleCloudDialogflowV2Message

Represents a message posted into a conversation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | Required. The message content. |  [optional] |
|**createTime** | **String** | Output only. The time when the message was created in Contact Center AI. |  [optional] [readonly] |
|**languageCode** | **String** | Optional. The message language. This should be a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: \&quot;en-US\&quot;. |  [optional] |
|**messageAnnotation** | [**GoogleCloudDialogflowV2MessageAnnotation**](GoogleCloudDialogflowV2MessageAnnotation.md) |  |  [optional] |
|**name** | **String** | Optional. The unique identifier of the message. Format: &#x60;projects//locations//conversations//messages/&#x60;. |  [optional] |
|**participant** | **String** | Output only. The participant that sends this message. |  [optional] [readonly] |
|**participantRole** | [**ParticipantRoleEnum**](#ParticipantRoleEnum) | Output only. The role of the participant. |  [optional] [readonly] |
|**sendTime** | **String** | Optional. The time when the message was sent. |  [optional] |
|**sentimentAnalysis** | [**GoogleCloudDialogflowV2SentimentAnalysisResult**](GoogleCloudDialogflowV2SentimentAnalysisResult.md) |  |  [optional] |



## Enum: ParticipantRoleEnum

| Name | Value |
|---- | -----|
| ROLE_UNSPECIFIED | &quot;ROLE_UNSPECIFIED&quot; |
| HUMAN_AGENT | &quot;HUMAN_AGENT&quot; |
| AUTOMATED_AGENT | &quot;AUTOMATED_AGENT&quot; |
| END_USER | &quot;END_USER&quot; |



