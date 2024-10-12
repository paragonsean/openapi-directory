# DialogflowApi.GoogleCloudDialogflowV2SearchKnowledgeAnswer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **String** | The piece of text from the knowledge base documents that answers the search query | [optional] 
**answerRecord** | **String** | The name of the answer record. Format: &#x60;projects//locations//answer Records/&#x60; | [optional] 
**answerSources** | [**[GoogleCloudDialogflowV2SearchKnowledgeAnswerAnswerSource]**](GoogleCloudDialogflowV2SearchKnowledgeAnswerAnswerSource.md) | All sources used to generate the answer. | [optional] 
**answerType** | **String** | The type of the answer. | [optional] 



## Enum: AnswerTypeEnum


* `ANSWER_TYPE_UNSPECIFIED` (value: `"ANSWER_TYPE_UNSPECIFIED"`)

* `FAQ` (value: `"FAQ"`)

* `GENERATIVE` (value: `"GENERATIVE"`)

* `INTENT` (value: `"INTENT"`)




