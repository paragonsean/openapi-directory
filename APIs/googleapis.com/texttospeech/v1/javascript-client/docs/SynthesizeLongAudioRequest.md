# CloudTextToSpeechApi.SynthesizeLongAudioRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioConfig** | [**AudioConfig**](AudioConfig.md) |  | [optional] 
**input** | [**SynthesisInput**](SynthesisInput.md) |  | [optional] 
**outputGcsUri** | **String** | Required. Specifies a Cloud Storage URI for the synthesis results. Must be specified in the format: &#x60;gs://bucket_name/object_name&#x60;, and the bucket must already exist. | [optional] 
**voice** | [**VoiceSelectionParams**](VoiceSelectionParams.md) |  | [optional] 


