# DialogflowApi.GoogleCloudDialogflowV2beta1DetectIntentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputAudio** | **Blob** | The natural language speech audio to be processed. This field should be populated iff &#x60;query_input&#x60; is set to an input audio config. A single request can contain up to 1 minute of speech audio data. | [optional] 
**outputAudioConfig** | [**GoogleCloudDialogflowV2beta1OutputAudioConfig**](GoogleCloudDialogflowV2beta1OutputAudioConfig.md) |  | [optional] 
**outputAudioConfigMask** | **String** | Mask for output_audio_config indicating which settings in this request-level config should override speech synthesizer settings defined at agent-level. If unspecified or empty, output_audio_config replaces the agent-level config in its entirety. | [optional] 
**queryInput** | [**GoogleCloudDialogflowV2beta1QueryInput**](GoogleCloudDialogflowV2beta1QueryInput.md) |  | [optional] 
**queryParams** | [**GoogleCloudDialogflowV2beta1QueryParameters**](GoogleCloudDialogflowV2beta1QueryParameters.md) |  | [optional] 


