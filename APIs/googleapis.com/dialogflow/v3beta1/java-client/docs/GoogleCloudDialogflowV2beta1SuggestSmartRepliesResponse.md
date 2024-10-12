

# GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponse

The response message for Participants.SuggestSmartReplies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contextSize** | **Integer** | Number of messages prior to and including latest_message to compile the suggestion. It may be smaller than the SuggestSmartRepliesRequest.context_size field in the request if there aren&#39;t that many messages in the conversation. |  [optional] |
|**latestMessage** | **String** | The name of the latest conversation message used to compile suggestion for. Format: &#x60;projects//locations//conversations//messages/&#x60;. |  [optional] |
|**smartReplyAnswers** | [**List&lt;GoogleCloudDialogflowV2beta1SmartReplyAnswer&gt;**](GoogleCloudDialogflowV2beta1SmartReplyAnswer.md) | Output only. Multiple reply options provided by smart reply service. The order is based on the rank of the model prediction. The maximum number of the returned replies is set in SmartReplyConfig. |  [optional] |



