

# GoogleCloudDialogflowV2OutputAudioConfig

Instructs the speech synthesizer on how to generate the output audio content. If this audio config is supplied in a request, it overrides all existing text-to-speech settings applied to the agent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioEncoding** | [**AudioEncodingEnum**](#AudioEncodingEnum) | Required. Audio encoding of the synthesized audio content. |  [optional] |
|**sampleRateHertz** | **Integer** | The synthesis sample rate (in hertz) for this audio. If not provided, then the synthesizer will use the default sample rate based on the audio encoding. If this is different from the voice&#39;s natural sample rate, then the synthesizer will honor this request by converting to the desired sample rate (which might result in worse audio quality). |  [optional] |
|**synthesizeSpeechConfig** | [**GoogleCloudDialogflowV2SynthesizeSpeechConfig**](GoogleCloudDialogflowV2SynthesizeSpeechConfig.md) |  |  [optional] |



## Enum: AudioEncodingEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;OUTPUT_AUDIO_ENCODING_UNSPECIFIED&quot; |
| LINEAR_16 | &quot;OUTPUT_AUDIO_ENCODING_LINEAR_16&quot; |
| MP3 | &quot;OUTPUT_AUDIO_ENCODING_MP3&quot; |
| MP3_64_KBPS | &quot;OUTPUT_AUDIO_ENCODING_MP3_64_KBPS&quot; |
| OGG_OPUS | &quot;OUTPUT_AUDIO_ENCODING_OGG_OPUS&quot; |
| MULAW | &quot;OUTPUT_AUDIO_ENCODING_MULAW&quot; |



