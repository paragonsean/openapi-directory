

# GoogleCloudVideointelligenceV1p3beta1WordInfo

Word-specific information for recognized words. Word information is only included in the response when certain request parameters are set, such as `enable_word_time_offsets`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidence** | **Float** | Output only. The confidence estimate between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. This field is set only for the top alternative. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating &#x60;confidence&#x60; was not set. |  [optional] [readonly] |
|**endTime** | **String** | Time offset relative to the beginning of the audio, and corresponding to the end of the spoken word. This field is only set if &#x60;enable_word_time_offsets&#x3D;true&#x60; and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary. |  [optional] |
|**speakerTag** | **Integer** | Output only. A distinct integer value is assigned for every speaker within the audio. This field specifies which one of those speakers was detected to have spoken this word. Value ranges from 1 up to diarization_speaker_count, and is only set if speaker diarization is enabled. |  [optional] [readonly] |
|**startTime** | **String** | Time offset relative to the beginning of the audio, and corresponding to the start of the spoken word. This field is only set if &#x60;enable_word_time_offsets&#x3D;true&#x60; and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary. |  [optional] |
|**word** | **String** | The word corresponding to this set of information. |  [optional] |



