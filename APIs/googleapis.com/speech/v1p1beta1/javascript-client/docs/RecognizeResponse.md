# CloudSpeechToTextApi.RecognizeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestId** | **String** | The ID associated with the request. This is a unique ID specific only to the given request. | [optional] 
**results** | [**[SpeechRecognitionResult]**](SpeechRecognitionResult.md) | Sequential list of transcription results corresponding to sequential portions of audio. | [optional] 
**speechAdaptationInfo** | [**SpeechAdaptationInfo**](SpeechAdaptationInfo.md) |  | [optional] 
**totalBilledTime** | **String** | When available, billed audio seconds for the corresponding request. | [optional] 
**usingLegacyModels** | **Boolean** | Whether request used legacy asr models (was not automatically migrated to use conformer models). | [optional] 


