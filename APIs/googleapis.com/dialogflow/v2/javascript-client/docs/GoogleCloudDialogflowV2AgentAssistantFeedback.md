# DialogflowApi.GoogleCloudDialogflowV2AgentAssistantFeedback

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answerRelevance** | **String** | Optional. Whether or not the suggested answer is relevant. For example: * Query: \&quot;Can I change my mailing address?\&quot; * Suggested document says: \&quot;Items must be returned/exchanged within 60 days of the purchase date.\&quot; * answer_relevance: AnswerRelevance.IRRELEVANT | [optional] 
**documentCorrectness** | **String** | Optional. Whether or not the information in the document is correct. For example: * Query: \&quot;Can I return the package in 2 days once received?\&quot; * Suggested document says: \&quot;Items must be returned/exchanged within 60 days of the purchase date.\&quot; * Ground truth: \&quot;No return or exchange is allowed.\&quot; * [document_correctness]: INCORRECT | [optional] 
**documentEfficiency** | **String** | Optional. Whether or not the suggested document is efficient. For example, if the document is poorly written, hard to understand, hard to use or too long to find useful information, document_efficiency is DocumentEfficiency.INEFFICIENT. | [optional] 
**knowledgeSearchFeedback** | [**GoogleCloudDialogflowV2AgentAssistantFeedbackKnowledgeSearchFeedback**](GoogleCloudDialogflowV2AgentAssistantFeedbackKnowledgeSearchFeedback.md) |  | [optional] 
**summarizationFeedback** | [**GoogleCloudDialogflowV2AgentAssistantFeedbackSummarizationFeedback**](GoogleCloudDialogflowV2AgentAssistantFeedbackSummarizationFeedback.md) |  | [optional] 



## Enum: AnswerRelevanceEnum


* `ANSWER_RELEVANCE_UNSPECIFIED` (value: `"ANSWER_RELEVANCE_UNSPECIFIED"`)

* `IRRELEVANT` (value: `"IRRELEVANT"`)

* `RELEVANT` (value: `"RELEVANT"`)





## Enum: DocumentCorrectnessEnum


* `DOCUMENT_CORRECTNESS_UNSPECIFIED` (value: `"DOCUMENT_CORRECTNESS_UNSPECIFIED"`)

* `INCORRECT` (value: `"INCORRECT"`)

* `CORRECT` (value: `"CORRECT"`)





## Enum: DocumentEfficiencyEnum


* `DOCUMENT_EFFICIENCY_UNSPECIFIED` (value: `"DOCUMENT_EFFICIENCY_UNSPECIFIED"`)

* `INEFFICIENT` (value: `"INEFFICIENT"`)

* `EFFICIENT` (value: `"EFFICIENT"`)




