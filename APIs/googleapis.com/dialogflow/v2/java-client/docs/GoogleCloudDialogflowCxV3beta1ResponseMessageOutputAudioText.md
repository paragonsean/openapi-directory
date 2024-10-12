

# GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioText

A text or ssml response that is preferentially used for TTS output audio synthesis, as described in the comment on the ResponseMessage message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowPlaybackInterruption** | **Boolean** | Output only. Whether the playback of this message can be interrupted by the end user&#39;s speech and the client can then starts the next Dialogflow request. |  [optional] [readonly] |
|**ssml** | **String** | The SSML text to be synthesized. For more information, see [SSML](/speech/text-to-speech/docs/ssml). |  [optional] |
|**text** | **String** | The raw text to be synthesized. |  [optional] |



