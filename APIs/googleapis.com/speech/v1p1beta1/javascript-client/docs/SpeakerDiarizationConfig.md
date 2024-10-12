# CloudSpeechToTextApi.SpeakerDiarizationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableSpeakerDiarization** | **Boolean** | If &#39;true&#39;, enables speaker detection for each recognized word in the top alternative of the recognition result using a speaker_label provided in the WordInfo. | [optional] 
**maxSpeakerCount** | **Number** | Maximum number of speakers in the conversation. This range gives you more flexibility by allowing the system to automatically determine the correct number of speakers. If not set, the default value is 6. | [optional] 
**minSpeakerCount** | **Number** | Minimum number of speakers in the conversation. This range gives you more flexibility by allowing the system to automatically determine the correct number of speakers. If not set, the default value is 2. | [optional] 
**speakerTag** | **Number** | Output only. Unused. | [optional] [readonly] 


