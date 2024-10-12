# CloudSpeechToTextApi.WordInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **Number** | Output only. The confidence estimate between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. This field is set only for the top alternative of a non-streaming result or, of a streaming result where &#x60;is_final&#x3D;true&#x60;. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating &#x60;confidence&#x60; was not set. | [optional] [readonly] 
**endOffset** | **String** | Output only. Time offset relative to the beginning of the audio, and corresponding to the end of the spoken word. This field is only set if &#x60;enable_word_time_offsets&#x3D;true&#x60; and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary. | [optional] [readonly] 
**speakerTag** | **Number** | Output only. A distinct integer value is assigned for every speaker within the audio. This field specifies which one of those speakers was detected to have spoken this word. Value ranges from &#x60;1&#x60; to &#x60;diarization_config.max_speaker_count&#x60; . &#x60;speaker_tag&#x60; is set if &#x60;diarization_config.enable_speaker_diarization&#x60; &#x3D; &#x60;true&#x60; and only in the top alternative. | [optional] [readonly] 
**startOffset** | **String** | Output only. Time offset relative to the beginning of the audio, and corresponding to the start of the spoken word. This field is only set if &#x60;enable_word_time_offsets&#x3D;true&#x60; and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary. | [optional] [readonly] 
**word** | **String** | Output only. The word corresponding to this set of information. | [optional] [readonly] 


