

# GoogleCloudDialogflowV2WebhookRequest

The request message for a webhook call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**originalDetectIntentRequest** | [**GoogleCloudDialogflowV2OriginalDetectIntentRequest**](GoogleCloudDialogflowV2OriginalDetectIntentRequest.md) |  |  [optional] |
|**queryResult** | [**GoogleCloudDialogflowV2QueryResult**](GoogleCloudDialogflowV2QueryResult.md) |  |  [optional] |
|**responseId** | **String** | The unique identifier of the response. Contains the same value as &#x60;[Streaming]DetectIntentResponse.response_id&#x60;. |  [optional] |
|**session** | **String** | The unique identifier of detectIntent request session. Can be used to identify end-user inside webhook implementation. Format: &#x60;projects//agent/sessions/&#x60;, or &#x60;projects//agent/environments//users//sessions/&#x60;. |  [optional] |



