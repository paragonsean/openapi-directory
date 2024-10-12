

# LongRunningRecognizeResponse

The only message returned to the client by the `LongRunningRecognize` method. It contains the result as zero or more sequential `SpeechRecognitionResult` messages. It is included in the `result.response` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**outputConfig** | [**TranscriptOutputConfig**](TranscriptOutputConfig.md) |  |  [optional] |
|**outputError** | [**Status**](Status.md) |  |  [optional] |
|**requestId** | **String** | The ID associated with the request. This is a unique ID specific only to the given request. |  [optional] |
|**results** | [**List&lt;SpeechRecognitionResult&gt;**](SpeechRecognitionResult.md) | Sequential list of transcription results corresponding to sequential portions of audio. |  [optional] |
|**speechAdaptationInfo** | [**SpeechAdaptationInfo**](SpeechAdaptationInfo.md) |  |  [optional] |
|**totalBilledTime** | **String** | When available, billed audio seconds for the corresponding request. |  [optional] |



