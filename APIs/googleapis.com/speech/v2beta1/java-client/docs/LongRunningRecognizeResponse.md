

# LongRunningRecognizeResponse

The only message returned to the client by the `LongRunningRecognize` method. It contains the result as zero or more sequential SpeechRecognitionResult messages. It is included in the `result.response` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**results** | [**List&lt;SpeechRecognitionResult&gt;**](SpeechRecognitionResult.md) | Output only. Sequential list of transcription results corresponding to sequential portions of audio. |  [optional] [readonly] |



