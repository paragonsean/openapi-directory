# CloudSpeechToTextApi.LongRunningRecognizeMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lastUpdateTime** | **String** | Time of the most recent processing update. | [optional] 
**outputConfig** | [**TranscriptOutputConfig**](TranscriptOutputConfig.md) |  | [optional] 
**progressPercent** | **Number** | Approximate percentage of audio processed thus far. Guaranteed to be 100 when the audio is fully processed and the results are available. | [optional] 
**startTime** | **String** | Time when the request was received. | [optional] 
**uri** | **String** | Output only. The URI of the audio file being transcribed. Empty if the audio was sent as byte content. | [optional] [readonly] 


