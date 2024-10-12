# DialogflowApi.GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contextSize** | **Number** | Number of messages prior to and including latest_message to compile the suggestion. It may be smaller than the SuggestDialogflowAssistsRequest.context_size field in the request if there aren&#39;t that many messages in the conversation. | [optional] 
**dialogflowAssistAnswers** | [**[GoogleCloudDialogflowV2beta1DialogflowAssistAnswer]**](GoogleCloudDialogflowV2beta1DialogflowAssistAnswer.md) | Output only. Multiple reply options provided by Dialogflow assist service. The order is based on the rank of the model prediction. | [optional] 
**latestMessage** | **String** | The name of the latest conversation message used to suggest answer. Format: &#x60;projects//locations//conversations//messages/&#x60;. | [optional] 


