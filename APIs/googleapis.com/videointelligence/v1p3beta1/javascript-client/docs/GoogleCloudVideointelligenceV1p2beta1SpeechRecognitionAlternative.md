# CloudVideoIntelligenceApi.GoogleCloudVideointelligenceV1p2beta1SpeechRecognitionAlternative

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **Number** | Output only. The confidence estimate between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. This field is set only for the top alternative. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating &#x60;confidence&#x60; was not set. | [optional] [readonly] 
**transcript** | **String** | Transcript text representing the words that the user spoke. | [optional] 
**words** | [**[GoogleCloudVideointelligenceV1p2beta1WordInfo]**](GoogleCloudVideointelligenceV1p2beta1WordInfo.md) | Output only. A list of word-specific information for each recognized word. Note: When &#x60;enable_speaker_diarization&#x60; is set to true, you will see all the words from the beginning of the audio. | [optional] [readonly] 


