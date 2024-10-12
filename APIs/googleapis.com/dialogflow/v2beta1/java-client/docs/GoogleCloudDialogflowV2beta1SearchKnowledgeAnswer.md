

# GoogleCloudDialogflowV2beta1SearchKnowledgeAnswer

Represents a SearchKnowledge answer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answer** | **String** | The piece of text from the knowledge base documents that answers the search query |  [optional] |
|**answerRecord** | **String** | The name of the answer record. Format: &#x60;projects//locations//answer Records/&#x60; |  [optional] |
|**answerSources** | [**List&lt;GoogleCloudDialogflowV2beta1SearchKnowledgeAnswerAnswerSource&gt;**](GoogleCloudDialogflowV2beta1SearchKnowledgeAnswerAnswerSource.md) | All sources used to generate the answer. |  [optional] |
|**answerType** | [**AnswerTypeEnum**](#AnswerTypeEnum) | The type of the answer. |  [optional] |



## Enum: AnswerTypeEnum

| Name | Value |
|---- | -----|
| ANSWER_TYPE_UNSPECIFIED | &quot;ANSWER_TYPE_UNSPECIFIED&quot; |
| FAQ | &quot;FAQ&quot; |
| GENERATIVE | &quot;GENERATIVE&quot; |
| INTENT | &quot;INTENT&quot; |



