

# LongRunningRecognizeMetadata

Describes the progress of a long-running `LongRunningRecognize` call. It is included in the `metadata` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastUpdateTime** | **String** | Output only. Time of the most recent processing update. |  [optional] [readonly] |
|**progressPercent** | **Integer** | Output only. Approximate percentage of audio processed thus far. Guaranteed to be 100 when the audio is fully processed and the results are available. |  [optional] [readonly] |
|**startTime** | **String** | Output only. Time when the request was received. |  [optional] [readonly] |
|**uri** | **String** | The URI of the audio file being transcribed. Empty if the audio was sent as byte content. |  [optional] |



