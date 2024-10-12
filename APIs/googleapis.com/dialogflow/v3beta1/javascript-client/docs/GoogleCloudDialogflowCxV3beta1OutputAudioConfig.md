# DialogflowApi.GoogleCloudDialogflowCxV3beta1OutputAudioConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioEncoding** | **String** | Required. Audio encoding of the synthesized audio content. | [optional] 
**sampleRateHertz** | **Number** | Optional. The synthesis sample rate (in hertz) for this audio. If not provided, then the synthesizer will use the default sample rate based on the audio encoding. If this is different from the voice&#39;s natural sample rate, then the synthesizer will honor this request by converting to the desired sample rate (which might result in worse audio quality). | [optional] 
**synthesizeSpeechConfig** | [**GoogleCloudDialogflowCxV3beta1SynthesizeSpeechConfig**](GoogleCloudDialogflowCxV3beta1SynthesizeSpeechConfig.md) |  | [optional] 



## Enum: AudioEncodingEnum


* `UNSPECIFIED` (value: `"OUTPUT_AUDIO_ENCODING_UNSPECIFIED"`)

* `LINEAR_16` (value: `"OUTPUT_AUDIO_ENCODING_LINEAR_16"`)

* `MP3` (value: `"OUTPUT_AUDIO_ENCODING_MP3"`)

* `MP3_64_KBPS` (value: `"OUTPUT_AUDIO_ENCODING_MP3_64_KBPS"`)

* `OGG_OPUS` (value: `"OUTPUT_AUDIO_ENCODING_OGG_OPUS"`)

* `MULAW` (value: `"OUTPUT_AUDIO_ENCODING_MULAW"`)




