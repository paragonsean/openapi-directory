

# SpeechRecognitionResult

A speech recognition result corresponding to a portion of the audio.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternatives** | [**List&lt;SpeechRecognitionAlternative&gt;**](SpeechRecognitionAlternative.md) | May contain one or more recognition hypotheses (up to the maximum specified in &#x60;max_alternatives&#x60;). These alternatives are ordered in terms of accuracy, with the top (first) alternative being the most probable, as ranked by the recognizer. |  [optional] |
|**channelTag** | **Integer** | For multi-channel audio, this is the channel number corresponding to the recognized result for the audio from that channel. For audio_channel_count &#x3D; N, its output values can range from &#39;1&#39; to &#39;N&#39;. |  [optional] |
|**languageCode** | **String** | Output only. The [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag of the language in this result. This language code was detected to have the most likelihood of being spoken in the audio. |  [optional] [readonly] |
|**resultEndTime** | **String** | Time offset of the end of this result relative to the beginning of the audio. |  [optional] |



