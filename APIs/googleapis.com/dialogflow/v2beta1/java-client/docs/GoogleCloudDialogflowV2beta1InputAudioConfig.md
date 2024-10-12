

# GoogleCloudDialogflowV2beta1InputAudioConfig

Instructs the speech recognizer on how to process the audio content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioEncoding** | [**AudioEncodingEnum**](#AudioEncodingEnum) | Required. Audio encoding of the audio content to process. |  [optional] |
|**bargeInConfig** | [**GoogleCloudDialogflowV2beta1BargeInConfig**](GoogleCloudDialogflowV2beta1BargeInConfig.md) |  |  [optional] |
|**disableNoSpeechRecognizedEvent** | **Boolean** | Only used in Participants.AnalyzeContent and Participants.StreamingAnalyzeContent. If &#x60;false&#x60; and recognition doesn&#39;t return any result, trigger &#x60;NO_SPEECH_RECOGNIZED&#x60; event to Dialogflow agent. |  [optional] |
|**enableAutomaticPunctuation** | **Boolean** | Enable automatic punctuation option at the speech backend. |  [optional] |
|**enableWordInfo** | **Boolean** | If &#x60;true&#x60;, Dialogflow returns SpeechWordInfo in StreamingRecognitionResult with information about the recognized speech words, e.g. start and end time offsets. If false or unspecified, Speech doesn&#39;t return any word-level information. |  [optional] |
|**languageCode** | **String** | Required. The language of the supplied audio. Dialogflow does not do translations. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes. Note that queries in the same session do not necessarily need to specify the same language. |  [optional] |
|**model** | **String** | Optional. Which Speech model to select for the given request. For more information, see [Speech models](https://cloud.google.com/dialogflow/es/docs/speech-models). |  [optional] |
|**modelVariant** | [**ModelVariantEnum**](#ModelVariantEnum) | Which variant of the Speech model to use. |  [optional] |
|**optOutConformerModelMigration** | **Boolean** | If &#x60;true&#x60;, the request will opt out for STT conformer model migration. This field will be deprecated once force migration takes place in June 2024. Please refer to [Dialogflow ES Speech model migration](https://cloud.google.com/dialogflow/es/docs/speech-model-migration). |  [optional] |
|**phraseHints** | **List&lt;String&gt;** | A list of strings containing words and phrases that the speech recognizer should recognize with higher likelihood. See [the Cloud Speech documentation](https://cloud.google.com/speech-to-text/docs/basics#phrase-hints) for more details. This field is deprecated. Please use [&#x60;speech_contexts&#x60;]() instead. If you specify both [&#x60;phrase_hints&#x60;]() and [&#x60;speech_contexts&#x60;](), Dialogflow will treat the [&#x60;phrase_hints&#x60;]() as a single additional [&#x60;SpeechContext&#x60;](). |  [optional] |
|**sampleRateHertz** | **Integer** | Required. Sample rate (in Hertz) of the audio content sent in the query. Refer to [Cloud Speech API documentation](https://cloud.google.com/speech-to-text/docs/basics) for more details. |  [optional] |
|**singleUtterance** | **Boolean** | If &#x60;false&#x60; (default), recognition does not cease until the client closes the stream. If &#x60;true&#x60;, the recognizer will detect a single spoken utterance in input audio. Recognition ceases when it detects the audio&#39;s voice has stopped or paused. In this case, once a detected intent is received, the client should close the stream and start a new request with a new stream as needed. Note: This setting is relevant only for streaming methods. Note: When specified, InputAudioConfig.single_utterance takes precedence over StreamingDetectIntentRequest.single_utterance. |  [optional] |
|**speechContexts** | [**List&lt;GoogleCloudDialogflowV2beta1SpeechContext&gt;**](GoogleCloudDialogflowV2beta1SpeechContext.md) | Context information to assist speech recognition. See [the Cloud Speech documentation](https://cloud.google.com/speech-to-text/docs/basics#phrase-hints) for more details. |  [optional] |



## Enum: AudioEncodingEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AUDIO_ENCODING_UNSPECIFIED&quot; |
| LINEAR_16 | &quot;AUDIO_ENCODING_LINEAR_16&quot; |
| FLAC | &quot;AUDIO_ENCODING_FLAC&quot; |
| MULAW | &quot;AUDIO_ENCODING_MULAW&quot; |
| AMR | &quot;AUDIO_ENCODING_AMR&quot; |
| AMR_WB | &quot;AUDIO_ENCODING_AMR_WB&quot; |
| OGG_OPUS | &quot;AUDIO_ENCODING_OGG_OPUS&quot; |
| SPEEX_WITH_HEADER_BYTE | &quot;AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE&quot; |



## Enum: ModelVariantEnum

| Name | Value |
|---- | -----|
| SPEECH_MODEL_VARIANT_UNSPECIFIED | &quot;SPEECH_MODEL_VARIANT_UNSPECIFIED&quot; |
| USE_BEST_AVAILABLE | &quot;USE_BEST_AVAILABLE&quot; |
| USE_STANDARD | &quot;USE_STANDARD&quot; |
| USE_ENHANCED | &quot;USE_ENHANCED&quot; |



