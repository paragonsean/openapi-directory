# CloudSpeechToTextApi.SpeechRecognitionResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternatives** | [**[SpeechRecognitionAlternative]**](SpeechRecognitionAlternative.md) | Output only. May contain one or more recognition hypotheses (up to the maximum specified in &#x60;max_alternatives&#x60;). These alternatives are ordered in terms of accuracy, with the top (first) alternative being the most probable, as ranked by the recognizer. | [optional] [readonly] 
**channelTag** | **Number** | Output only. For multi-channel audio, this is the channel number corresponding to the recognized result for the audio from that channel. For &#x60;audio_channel_count&#x60; &#x3D; N, its output values can range from &#x60;1&#x60; to &#x60;N&#x60;. | [optional] [readonly] 
**languageCode** | **String** | Output only. The [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag of the language in this result. This language code was detected to have the most likelihood of being spoken in the audio. | [optional] [readonly] 


