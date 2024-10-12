# DialogflowApi.GoogleCloudDialogflowV2beta1SuggestArticlesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**articleAnswers** | [**[GoogleCloudDialogflowV2beta1ArticleAnswer]**](GoogleCloudDialogflowV2beta1ArticleAnswer.md) | Output only. Articles ordered by score in descending order. | [optional] 
**contextSize** | **Number** | Number of messages prior to and including latest_message to compile the suggestion. It may be smaller than the SuggestArticlesResponse.context_size field in the request if there aren&#39;t that many messages in the conversation. | [optional] 
**latestMessage** | **String** | The name of the latest conversation message used to compile suggestion for. Format: &#x60;projects//locations//conversations//messages/&#x60;. | [optional] 


