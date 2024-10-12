# DialogflowApi.GoogleCloudDialogflowV2DetectIntentResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outputAudio** | **Blob** | The audio data bytes encoded as specified in the request. Note: The output audio is generated based on the values of default platform text responses found in the &#x60;query_result.fulfillment_messages&#x60; field. If multiple default text responses exist, they will be concatenated when generating audio. If no default platform text responses exist, the generated audio content will be empty. In some scenarios, multiple output audio fields may be present in the response structure. In these cases, only the top-most-level audio output has content. | [optional] 
**outputAudioConfig** | [**GoogleCloudDialogflowV2OutputAudioConfig**](GoogleCloudDialogflowV2OutputAudioConfig.md) |  | [optional] 
**queryResult** | [**GoogleCloudDialogflowV2QueryResult**](GoogleCloudDialogflowV2QueryResult.md) |  | [optional] 
**responseId** | **String** | The unique identifier of the response. It can be used to locate a response in the training example set or for reporting issues. | [optional] 
**webhookStatus** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 


