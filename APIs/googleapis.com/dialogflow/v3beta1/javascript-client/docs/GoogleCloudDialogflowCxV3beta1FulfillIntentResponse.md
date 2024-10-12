# DialogflowApi.GoogleCloudDialogflowCxV3beta1FulfillIntentResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outputAudio** | **Blob** | The audio data bytes encoded as specified in the request. Note: The output audio is generated based on the values of default platform text responses found in the &#x60;query_result.response_messages&#x60; field. If multiple default text responses exist, they will be concatenated when generating audio. If no default platform text responses exist, the generated audio content will be empty. In some scenarios, multiple output audio fields may be present in the response structure. In these cases, only the top-most-level audio output has content. | [optional] 
**outputAudioConfig** | [**GoogleCloudDialogflowCxV3beta1OutputAudioConfig**](GoogleCloudDialogflowCxV3beta1OutputAudioConfig.md) |  | [optional] 
**queryResult** | [**GoogleCloudDialogflowCxV3beta1QueryResult**](GoogleCloudDialogflowCxV3beta1QueryResult.md) |  | [optional] 
**responseId** | **String** | Output only. The unique identifier of the response. It can be used to locate a response in the training example set or for reporting issues. | [optional] 


