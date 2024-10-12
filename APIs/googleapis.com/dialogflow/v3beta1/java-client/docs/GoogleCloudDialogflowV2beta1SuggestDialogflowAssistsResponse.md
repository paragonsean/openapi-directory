

# GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponse

The response message for Participants.SuggestDialogflowAssists.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contextSize** | **Integer** | Number of messages prior to and including latest_message to compile the suggestion. It may be smaller than the SuggestDialogflowAssistsRequest.context_size field in the request if there aren&#39;t that many messages in the conversation. |  [optional] |
|**dialogflowAssistAnswers** | [**List&lt;GoogleCloudDialogflowV2beta1DialogflowAssistAnswer&gt;**](GoogleCloudDialogflowV2beta1DialogflowAssistAnswer.md) | Output only. Multiple reply options provided by Dialogflow assist service. The order is based on the rank of the model prediction. |  [optional] |
|**latestMessage** | **String** | The name of the latest conversation message used to suggest answer. Format: &#x60;projects//locations//conversations//messages/&#x60;. |  [optional] |



