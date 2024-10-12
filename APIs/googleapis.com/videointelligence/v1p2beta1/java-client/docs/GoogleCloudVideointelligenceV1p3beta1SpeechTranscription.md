

# GoogleCloudVideointelligenceV1p3beta1SpeechTranscription

A speech recognition result corresponding to a portion of the audio.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternatives** | [**List&lt;GoogleCloudVideointelligenceV1p3beta1SpeechRecognitionAlternative&gt;**](GoogleCloudVideointelligenceV1p3beta1SpeechRecognitionAlternative.md) | May contain one or more recognition hypotheses (up to the maximum specified in &#x60;max_alternatives&#x60;). These alternatives are ordered in terms of accuracy, with the top (first) alternative being the most probable, as ranked by the recognizer. |  [optional] |
|**languageCode** | **String** | Output only. The [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag of the language in this result. This language code was detected to have the most likelihood of being spoken in the audio. |  [optional] [readonly] |



