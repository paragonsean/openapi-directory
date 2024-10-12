

# GoogleCloudDialogflowV2beta1Suggestion

Represents a suggestion for a human agent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**articles** | [**List&lt;GoogleCloudDialogflowV2beta1SuggestionArticle&gt;**](GoogleCloudDialogflowV2beta1SuggestionArticle.md) | Output only. Articles ordered by score in descending order. |  [optional] |
|**createTime** | **String** | Output only. The time the suggestion was created. |  [optional] |
|**faqAnswers** | [**List&lt;GoogleCloudDialogflowV2beta1SuggestionFaqAnswer&gt;**](GoogleCloudDialogflowV2beta1SuggestionFaqAnswer.md) | Output only. Answers extracted from FAQ documents. |  [optional] |
|**latestMessage** | **String** | Output only. Latest message used as context to compile this suggestion. Format: &#x60;projects//locations//conversations//messages/&#x60;. |  [optional] |
|**name** | **String** | Output only. The name of this suggestion. Format: &#x60;projects//locations//conversations//participants/_*_/suggestions/&#x60;. |  [optional] |



