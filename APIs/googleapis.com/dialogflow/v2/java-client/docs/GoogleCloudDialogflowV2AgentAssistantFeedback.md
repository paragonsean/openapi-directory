

# GoogleCloudDialogflowV2AgentAssistantFeedback

Detail feedback of Agent Assist result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answerRelevance** | [**AnswerRelevanceEnum**](#AnswerRelevanceEnum) | Optional. Whether or not the suggested answer is relevant. For example: * Query: \&quot;Can I change my mailing address?\&quot; * Suggested document says: \&quot;Items must be returned/exchanged within 60 days of the purchase date.\&quot; * answer_relevance: AnswerRelevance.IRRELEVANT |  [optional] |
|**documentCorrectness** | [**DocumentCorrectnessEnum**](#DocumentCorrectnessEnum) | Optional. Whether or not the information in the document is correct. For example: * Query: \&quot;Can I return the package in 2 days once received?\&quot; * Suggested document says: \&quot;Items must be returned/exchanged within 60 days of the purchase date.\&quot; * Ground truth: \&quot;No return or exchange is allowed.\&quot; * [document_correctness]: INCORRECT |  [optional] |
|**documentEfficiency** | [**DocumentEfficiencyEnum**](#DocumentEfficiencyEnum) | Optional. Whether or not the suggested document is efficient. For example, if the document is poorly written, hard to understand, hard to use or too long to find useful information, document_efficiency is DocumentEfficiency.INEFFICIENT. |  [optional] |
|**knowledgeSearchFeedback** | [**GoogleCloudDialogflowV2AgentAssistantFeedbackKnowledgeSearchFeedback**](GoogleCloudDialogflowV2AgentAssistantFeedbackKnowledgeSearchFeedback.md) |  |  [optional] |
|**summarizationFeedback** | [**GoogleCloudDialogflowV2AgentAssistantFeedbackSummarizationFeedback**](GoogleCloudDialogflowV2AgentAssistantFeedbackSummarizationFeedback.md) |  |  [optional] |



## Enum: AnswerRelevanceEnum

| Name | Value |
|---- | -----|
| ANSWER_RELEVANCE_UNSPECIFIED | &quot;ANSWER_RELEVANCE_UNSPECIFIED&quot; |
| IRRELEVANT | &quot;IRRELEVANT&quot; |
| RELEVANT | &quot;RELEVANT&quot; |



## Enum: DocumentCorrectnessEnum

| Name | Value |
|---- | -----|
| DOCUMENT_CORRECTNESS_UNSPECIFIED | &quot;DOCUMENT_CORRECTNESS_UNSPECIFIED&quot; |
| INCORRECT | &quot;INCORRECT&quot; |
| CORRECT | &quot;CORRECT&quot; |



## Enum: DocumentEfficiencyEnum

| Name | Value |
|---- | -----|
| DOCUMENT_EFFICIENCY_UNSPECIFIED | &quot;DOCUMENT_EFFICIENCY_UNSPECIFIED&quot; |
| INEFFICIENT | &quot;INEFFICIENT&quot; |
| EFFICIENT | &quot;EFFICIENT&quot; |



