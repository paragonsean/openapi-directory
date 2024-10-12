# DialogflowApi.GoogleCloudDialogflowV2GenerateStatelessSummaryRequestMinimalConversation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**[GoogleCloudDialogflowV2Message]**](GoogleCloudDialogflowV2Message.md) | Required. The messages that the Summary will be generated from. It is expected that this message content is already redacted and does not contain any PII. Required fields: {content, language_code, participant, participant_role} Optional fields: {send_time} If send_time is not provided, then the messages must be provided in chronological order. | [optional] 


