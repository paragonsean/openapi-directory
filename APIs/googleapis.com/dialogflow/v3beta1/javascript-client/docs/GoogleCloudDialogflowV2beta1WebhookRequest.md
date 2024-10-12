# DialogflowApi.GoogleCloudDialogflowV2beta1WebhookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternativeQueryResults** | [**[GoogleCloudDialogflowV2beta1QueryResult]**](GoogleCloudDialogflowV2beta1QueryResult.md) | Alternative query results from KnowledgeService. | [optional] 
**originalDetectIntentRequest** | [**GoogleCloudDialogflowV2beta1OriginalDetectIntentRequest**](GoogleCloudDialogflowV2beta1OriginalDetectIntentRequest.md) |  | [optional] 
**queryResult** | [**GoogleCloudDialogflowV2beta1QueryResult**](GoogleCloudDialogflowV2beta1QueryResult.md) |  | [optional] 
**responseId** | **String** | The unique identifier of the response. Contains the same value as &#x60;[Streaming]DetectIntentResponse.response_id&#x60;. | [optional] 
**session** | **String** | The unique identifier of detectIntent request session. Can be used to identify end-user inside webhook implementation. Supported formats: - &#x60;projects//agent/sessions/, - &#x60;projects//locations//agent/sessions/&#x60;, - &#x60;projects//agent/environments//users//sessions/&#x60;, - &#x60;projects//locations//agent/environments//users//sessions/&#x60;, | [optional] 


