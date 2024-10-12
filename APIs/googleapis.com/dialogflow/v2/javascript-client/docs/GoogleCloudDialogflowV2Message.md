# DialogflowApi.GoogleCloudDialogflowV2Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **String** | Required. The message content. | [optional] 
**createTime** | **String** | Output only. The time when the message was created in Contact Center AI. | [optional] [readonly] 
**languageCode** | **String** | Optional. The message language. This should be a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: \&quot;en-US\&quot;. | [optional] 
**messageAnnotation** | [**GoogleCloudDialogflowV2MessageAnnotation**](GoogleCloudDialogflowV2MessageAnnotation.md) |  | [optional] 
**name** | **String** | Optional. The unique identifier of the message. Format: &#x60;projects//locations//conversations//messages/&#x60;. | [optional] 
**participant** | **String** | Output only. The participant that sends this message. | [optional] [readonly] 
**participantRole** | **String** | Output only. The role of the participant. | [optional] [readonly] 
**sendTime** | **String** | Optional. The time when the message was sent. | [optional] 
**sentimentAnalysis** | [**GoogleCloudDialogflowV2SentimentAnalysisResult**](GoogleCloudDialogflowV2SentimentAnalysisResult.md) |  | [optional] 



## Enum: ParticipantRoleEnum


* `ROLE_UNSPECIFIED` (value: `"ROLE_UNSPECIFIED"`)

* `HUMAN_AGENT` (value: `"HUMAN_AGENT"`)

* `AUTOMATED_AGENT` (value: `"AUTOMATED_AGENT"`)

* `END_USER` (value: `"END_USER"`)




