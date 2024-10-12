# CloudSpeechToTextApi.LongRunningRecognizeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outputConfig** | [**TranscriptOutputConfig**](TranscriptOutputConfig.md) |  | [optional] 
**outputError** | [**Status**](Status.md) |  | [optional] 
**requestId** | **String** | The ID associated with the request. This is a unique ID specific only to the given request. | [optional] 
**results** | [**[SpeechRecognitionResult]**](SpeechRecognitionResult.md) | Sequential list of transcription results corresponding to sequential portions of audio. | [optional] 
**speechAdaptationInfo** | [**SpeechAdaptationInfo**](SpeechAdaptationInfo.md) |  | [optional] 
**totalBilledTime** | **String** | When available, billed audio seconds for the corresponding request. | [optional] 


