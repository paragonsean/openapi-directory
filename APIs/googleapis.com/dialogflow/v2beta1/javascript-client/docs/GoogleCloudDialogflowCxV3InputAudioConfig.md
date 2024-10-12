# DialogflowApi.GoogleCloudDialogflowCxV3InputAudioConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioEncoding** | **String** | Required. Audio encoding of the audio content to process. | [optional] 
**bargeInConfig** | [**GoogleCloudDialogflowCxV3BargeInConfig**](GoogleCloudDialogflowCxV3BargeInConfig.md) |  | [optional] 
**enableWordInfo** | **Boolean** | Optional. If &#x60;true&#x60;, Dialogflow returns SpeechWordInfo in StreamingRecognitionResult with information about the recognized speech words, e.g. start and end time offsets. If false or unspecified, Speech doesn&#39;t return any word-level information. | [optional] 
**model** | **String** | Optional. Which Speech model to select for the given request. For more information, see [Speech models](https://cloud.google.com/dialogflow/cx/docs/concept/speech-models). | [optional] 
**modelVariant** | **String** | Optional. Which variant of the Speech model to use. | [optional] 
**optOutConformerModelMigration** | **Boolean** | If &#x60;true&#x60;, the request will opt out for STT conformer model migration. This field will be deprecated once force migration takes place in June 2024. Please refer to [Dialogflow CX Speech model migration](https://cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration). | [optional] 
**phraseHints** | **[String]** | Optional. A list of strings containing words and phrases that the speech recognizer should recognize with higher likelihood. See [the Cloud Speech documentation](https://cloud.google.com/speech-to-text/docs/basics#phrase-hints) for more details. | [optional] 
**sampleRateHertz** | **Number** | Sample rate (in Hertz) of the audio content sent in the query. Refer to [Cloud Speech API documentation](https://cloud.google.com/speech-to-text/docs/basics) for more details. | [optional] 
**singleUtterance** | **Boolean** | Optional. If &#x60;false&#x60; (default), recognition does not cease until the client closes the stream. If &#x60;true&#x60;, the recognizer will detect a single spoken utterance in input audio. Recognition ceases when it detects the audio&#39;s voice has stopped or paused. In this case, once a detected intent is received, the client should close the stream and start a new request with a new stream as needed. Note: This setting is relevant only for streaming methods. | [optional] 



## Enum: AudioEncodingEnum


* `UNSPECIFIED` (value: `"AUDIO_ENCODING_UNSPECIFIED"`)

* `LINEAR_16` (value: `"AUDIO_ENCODING_LINEAR_16"`)

* `FLAC` (value: `"AUDIO_ENCODING_FLAC"`)

* `MULAW` (value: `"AUDIO_ENCODING_MULAW"`)

* `AMR` (value: `"AUDIO_ENCODING_AMR"`)

* `AMR_WB` (value: `"AUDIO_ENCODING_AMR_WB"`)

* `OGG_OPUS` (value: `"AUDIO_ENCODING_OGG_OPUS"`)

* `SPEEX_WITH_HEADER_BYTE` (value: `"AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE"`)





## Enum: ModelVariantEnum


* `SPEECH_MODEL_VARIANT_UNSPECIFIED` (value: `"SPEECH_MODEL_VARIANT_UNSPECIFIED"`)

* `USE_BEST_AVAILABLE` (value: `"USE_BEST_AVAILABLE"`)

* `USE_STANDARD` (value: `"USE_STANDARD"`)

* `USE_ENHANCED` (value: `"USE_ENHANCED"`)




