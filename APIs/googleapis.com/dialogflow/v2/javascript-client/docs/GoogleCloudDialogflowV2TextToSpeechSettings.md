# DialogflowApi.GoogleCloudDialogflowV2TextToSpeechSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableTextToSpeech** | **Boolean** | Optional. Indicates whether text to speech is enabled. Even when this field is false, other settings in this proto are still retained. | [optional] 
**outputAudioEncoding** | **String** | Required. Audio encoding of the synthesized audio content. | [optional] 
**sampleRateHertz** | **Number** | Optional. The synthesis sample rate (in hertz) for this audio. If not provided, then the synthesizer will use the default sample rate based on the audio encoding. If this is different from the voice&#39;s natural sample rate, then the synthesizer will honor this request by converting to the desired sample rate (which might result in worse audio quality). | [optional] 
**synthesizeSpeechConfigs** | [**{String: GoogleCloudDialogflowV2SynthesizeSpeechConfig}**](GoogleCloudDialogflowV2SynthesizeSpeechConfig.md) | Optional. Configuration of how speech should be synthesized, mapping from language (https://cloud.google.com/dialogflow/docs/reference/language) to SynthesizeSpeechConfig. | [optional] 



## Enum: OutputAudioEncodingEnum


* `UNSPECIFIED` (value: `"OUTPUT_AUDIO_ENCODING_UNSPECIFIED"`)

* `LINEAR_16` (value: `"OUTPUT_AUDIO_ENCODING_LINEAR_16"`)

* `MP3` (value: `"OUTPUT_AUDIO_ENCODING_MP3"`)

* `MP3_64_KBPS` (value: `"OUTPUT_AUDIO_ENCODING_MP3_64_KBPS"`)

* `OGG_OPUS` (value: `"OUTPUT_AUDIO_ENCODING_OGG_OPUS"`)

* `MULAW` (value: `"OUTPUT_AUDIO_ENCODING_MULAW"`)




