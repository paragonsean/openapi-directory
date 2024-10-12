

# GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegment

Represents one segment of audio.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowPlaybackInterruption** | **Boolean** | Output only. Whether the playback of this segment can be interrupted by the end user&#39;s speech and the client should then start the next Dialogflow request. |  [optional] [readonly] |
|**audio** | **byte[]** | Raw audio synthesized from the Dialogflow agent&#39;s response using the output config specified in the request. |  [optional] |
|**uri** | **String** | Client-specific URI that points to an audio clip accessible to the client. Dialogflow does not impose any validation on it. |  [optional] |



