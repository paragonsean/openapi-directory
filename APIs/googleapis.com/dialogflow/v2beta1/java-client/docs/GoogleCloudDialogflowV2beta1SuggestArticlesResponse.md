

# GoogleCloudDialogflowV2beta1SuggestArticlesResponse

The response message for Participants.SuggestArticles.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**articleAnswers** | [**List&lt;GoogleCloudDialogflowV2beta1ArticleAnswer&gt;**](GoogleCloudDialogflowV2beta1ArticleAnswer.md) | Output only. Articles ordered by score in descending order. |  [optional] |
|**contextSize** | **Integer** | Number of messages prior to and including latest_message to compile the suggestion. It may be smaller than the SuggestArticlesResponse.context_size field in the request if there aren&#39;t that many messages in the conversation. |  [optional] |
|**latestMessage** | **String** | The name of the latest conversation message used to compile suggestion for. Format: &#x60;projects//locations//conversations//messages/&#x60;. |  [optional] |



