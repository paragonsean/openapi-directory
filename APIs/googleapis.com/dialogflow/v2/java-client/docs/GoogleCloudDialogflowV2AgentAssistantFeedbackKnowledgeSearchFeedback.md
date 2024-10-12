

# GoogleCloudDialogflowV2AgentAssistantFeedbackKnowledgeSearchFeedback

Feedback for knowledge search.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answerCopied** | **Boolean** | Whether the answer was copied by the human agent or not. If the value is set to be true, AnswerFeedback.clicked will be updated to be true. |  [optional] |
|**clickedUris** | **List&lt;String&gt;** | The URIs clicked by the human agent. The value is appended for each UpdateAnswerRecordRequest. If the value is not empty, AnswerFeedback.clicked will be updated to be true. |  [optional] |



