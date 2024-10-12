# DialogflowApi.GoogleCloudDialogflowV2SuggestFaqAnswersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contextSize** | **Number** | Number of messages prior to and including latest_message to compile the suggestion. It may be smaller than the SuggestFaqAnswersRequest.context_size field in the request if there aren&#39;t that many messages in the conversation. | [optional] 
**faqAnswers** | [**[GoogleCloudDialogflowV2FaqAnswer]**](GoogleCloudDialogflowV2FaqAnswer.md) | Answers extracted from FAQ documents. | [optional] 
**latestMessage** | **String** | The name of the latest conversation message used to compile suggestion for. Format: &#x60;projects//locations//conversations//messages/&#x60;. | [optional] 


