# MuxApi.CreateTranscriptionVocabularyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The user-supplied name of the Transcription Vocabulary. | [optional] 
**passthrough** | **String** | Arbitrary user-supplied metadata set for the Transcription Vocabulary. Max 255 characters. | [optional] 
**phrases** | **[String]** | Phrases, individual words, or proper names to include in the Transcription Vocabulary. When the Transcription Vocabulary is attached to a live stream&#39;s &#x60;generated_subtitles&#x60;, the probability of successful speech recognition for these words or phrases is boosted. | 


