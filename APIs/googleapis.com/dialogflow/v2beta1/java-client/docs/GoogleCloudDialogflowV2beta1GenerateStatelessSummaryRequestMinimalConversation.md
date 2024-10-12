

# GoogleCloudDialogflowV2beta1GenerateStatelessSummaryRequestMinimalConversation

The minimum amount of information required to generate a Summary without having a Conversation resource created.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messages** | [**List&lt;GoogleCloudDialogflowV2beta1Message&gt;**](GoogleCloudDialogflowV2beta1Message.md) | Required. The messages that the Summary will be generated from. It is expected that this message content is already redacted and does not contain any PII. Required fields: {content, language_code, participant, participant_role} Optional fields: {send_time} If send_time is not provided, then the messages must be provided in chronological order. |  [optional] |



