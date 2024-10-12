

# GoogleCloudDialogflowV2TextToSpeechSettings

Instructs the speech synthesizer on how to generate the output audio content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableTextToSpeech** | **Boolean** | Optional. Indicates whether text to speech is enabled. Even when this field is false, other settings in this proto are still retained. |  [optional] |
|**outputAudioEncoding** | [**OutputAudioEncodingEnum**](#OutputAudioEncodingEnum) | Required. Audio encoding of the synthesized audio content. |  [optional] |
|**sampleRateHertz** | **Integer** | Optional. The synthesis sample rate (in hertz) for this audio. If not provided, then the synthesizer will use the default sample rate based on the audio encoding. If this is different from the voice&#39;s natural sample rate, then the synthesizer will honor this request by converting to the desired sample rate (which might result in worse audio quality). |  [optional] |
|**synthesizeSpeechConfigs** | [**Map&lt;String, GoogleCloudDialogflowV2SynthesizeSpeechConfig&gt;**](GoogleCloudDialogflowV2SynthesizeSpeechConfig.md) | Optional. Configuration of how speech should be synthesized, mapping from language (https://cloud.google.com/dialogflow/docs/reference/language) to SynthesizeSpeechConfig. |  [optional] |



## Enum: OutputAudioEncodingEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;OUTPUT_AUDIO_ENCODING_UNSPECIFIED&quot; |
| LINEAR_16 | &quot;OUTPUT_AUDIO_ENCODING_LINEAR_16&quot; |
| MP3 | &quot;OUTPUT_AUDIO_ENCODING_MP3&quot; |
| MP3_64_KBPS | &quot;OUTPUT_AUDIO_ENCODING_MP3_64_KBPS&quot; |
| OGG_OPUS | &quot;OUTPUT_AUDIO_ENCODING_OGG_OPUS&quot; |
| MULAW | &quot;OUTPUT_AUDIO_ENCODING_MULAW&quot; |



