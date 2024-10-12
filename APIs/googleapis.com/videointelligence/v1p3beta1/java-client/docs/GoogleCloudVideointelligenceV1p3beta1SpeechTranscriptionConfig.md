

# GoogleCloudVideointelligenceV1p3beta1SpeechTranscriptionConfig

Config for SPEECH_TRANSCRIPTION.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioTracks** | **List&lt;Integer&gt;** | Optional. For file formats, such as MXF or MKV, supporting multiple audio tracks, specify up to two tracks. Default: track 0. |  [optional] |
|**diarizationSpeakerCount** | **Integer** | Optional. If set, specifies the estimated number of speakers in the conversation. If not set, defaults to &#39;2&#39;. Ignored unless enable_speaker_diarization is set to true. |  [optional] |
|**enableAutomaticPunctuation** | **Boolean** | Optional. If &#39;true&#39;, adds punctuation to recognition result hypotheses. This feature is only available in select languages. Setting this for requests in other languages has no effect at all. The default &#39;false&#39; value does not add punctuation to result hypotheses. NOTE: \&quot;This is currently offered as an experimental service, complimentary to all users. In the future this may be exclusively available as a premium feature.\&quot; |  [optional] |
|**enableSpeakerDiarization** | **Boolean** | Optional. If &#39;true&#39;, enables speaker detection for each recognized word in the top alternative of the recognition result using a speaker_tag provided in the WordInfo. Note: When this is true, we send all the words from the beginning of the audio for the top alternative in every consecutive response. This is done in order to improve our speaker tags as our models learn to identify the speakers in the conversation over time. |  [optional] |
|**enableWordConfidence** | **Boolean** | Optional. If &#x60;true&#x60;, the top result includes a list of words and the confidence for those words. If &#x60;false&#x60;, no word-level confidence information is returned. The default is &#x60;false&#x60;. |  [optional] |
|**filterProfanity** | **Boolean** | Optional. If set to &#x60;true&#x60;, the server will attempt to filter out profanities, replacing all but the initial character in each filtered word with asterisks, e.g. \&quot;f***\&quot;. If set to &#x60;false&#x60; or omitted, profanities won&#39;t be filtered out. |  [optional] |
|**languageCode** | **String** | Required. *Required* The language of the supplied audio as a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: \&quot;en-US\&quot;. See [Language Support](https://cloud.google.com/speech/docs/languages) for a list of the currently supported language codes. |  [optional] |
|**maxAlternatives** | **Integer** | Optional. Maximum number of recognition hypotheses to be returned. Specifically, the maximum number of &#x60;SpeechRecognitionAlternative&#x60; messages within each &#x60;SpeechTranscription&#x60;. The server may return fewer than &#x60;max_alternatives&#x60;. Valid values are &#x60;0&#x60;-&#x60;30&#x60;. A value of &#x60;0&#x60; or &#x60;1&#x60; will return a maximum of one. If omitted, will return a maximum of one. |  [optional] |
|**speechContexts** | [**List&lt;GoogleCloudVideointelligenceV1p3beta1SpeechContext&gt;**](GoogleCloudVideointelligenceV1p3beta1SpeechContext.md) | Optional. A means to provide context to assist the speech recognition. |  [optional] |



