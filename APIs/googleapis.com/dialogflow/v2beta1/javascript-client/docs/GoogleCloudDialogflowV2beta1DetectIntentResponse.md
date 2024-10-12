# DialogflowApi.GoogleCloudDialogflowV2beta1DetectIntentResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternativeQueryResults** | [**[GoogleCloudDialogflowV2beta1QueryResult]**](GoogleCloudDialogflowV2beta1QueryResult.md) | If Knowledge Connectors are enabled, there could be more than one result returned for a given query or event, and this field will contain all results except for the top one, which is captured in query_result. The alternative results are ordered by decreasing &#x60;QueryResult.intent_detection_confidence&#x60;. If Knowledge Connectors are disabled, this field will be empty until multiple responses for regular intents are supported, at which point those additional results will be surfaced here. | [optional] 
**outputAudio** | **Blob** | The audio data bytes encoded as specified in the request. Note: The output audio is generated based on the values of default platform text responses found in the &#x60;query_result.fulfillment_messages&#x60; field. If multiple default text responses exist, they will be concatenated when generating audio. If no default platform text responses exist, the generated audio content will be empty. In some scenarios, multiple output audio fields may be present in the response structure. In these cases, only the top-most-level audio output has content. | [optional] 
**outputAudioConfig** | [**GoogleCloudDialogflowV2beta1OutputAudioConfig**](GoogleCloudDialogflowV2beta1OutputAudioConfig.md) |  | [optional] 
**queryResult** | [**GoogleCloudDialogflowV2beta1QueryResult**](GoogleCloudDialogflowV2beta1QueryResult.md) |  | [optional] 
**responseId** | **String** | The unique identifier of the response. It can be used to locate a response in the training example set or for reporting issues. | [optional] 
**webhookStatus** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 


