# AzureMediaServices.LiveEventTranscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputTrackSelection** | [**[LiveEventInputTrackSelection]**](LiveEventInputTrackSelection.md) | Provides a mechanism to select the audio track in the input live feed, to which speech-to-text transcription is applied. | [optional] 
**language** | **String** | Specifies the language (locale) used for speech-to-text transcription � it should match the spoken language in the audio track. The value should be in BCP-47 format of &#39;language tag-region&#39; (e.g: &#39;en-US&#39;). The list of supported languages are &#39;en-US&#39; and &#39;en-GB&#39;. | [optional] 
**outputTranscriptionTrack** | [**LiveEventOutputTranscriptionTrack**](LiveEventOutputTranscriptionTrack.md) |  | [optional] 


