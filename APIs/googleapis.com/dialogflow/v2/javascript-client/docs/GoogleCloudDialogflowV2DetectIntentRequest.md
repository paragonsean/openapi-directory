# DialogflowApi.GoogleCloudDialogflowV2DetectIntentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputAudio** | **Blob** | The natural language speech audio to be processed. This field should be populated iff &#x60;query_input&#x60; is set to an input audio config. A single request can contain up to 1 minute of speech audio data. | [optional] 
**outputAudioConfig** | [**GoogleCloudDialogflowV2OutputAudioConfig**](GoogleCloudDialogflowV2OutputAudioConfig.md) |  | [optional] 
**outputAudioConfigMask** | **String** | Mask for output_audio_config indicating which settings in this request-level config should override speech synthesizer settings defined at agent-level. If unspecified or empty, output_audio_config replaces the agent-level config in its entirety. | [optional] 
**queryInput** | [**GoogleCloudDialogflowV2QueryInput**](GoogleCloudDialogflowV2QueryInput.md) |  | [optional] 
**queryParams** | [**GoogleCloudDialogflowV2QueryParameters**](GoogleCloudDialogflowV2QueryParameters.md) |  | [optional] 


