

# GoogleCloudVideointelligenceV1beta2VideoAnnotationProgress

Annotation progress for a single video.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**feature** | [**FeatureEnum**](#FeatureEnum) | Specifies which feature is being tracked if the request contains more than one feature. |  [optional] |
|**inputUri** | **String** | Video file location in [Cloud Storage](https://cloud.google.com/storage/). |  [optional] |
|**progressPercent** | **Integer** | Approximate percentage processed thus far. Guaranteed to be 100 when fully processed. |  [optional] |
|**segment** | [**GoogleCloudVideointelligenceV1beta2VideoSegment**](GoogleCloudVideointelligenceV1beta2VideoSegment.md) |  |  [optional] |
|**startTime** | **String** | Time when the request was received. |  [optional] |
|**updateTime** | **String** | Time of the most recent update. |  [optional] |



## Enum: FeatureEnum

| Name | Value |
|---- | -----|
| FEATURE_UNSPECIFIED | &quot;FEATURE_UNSPECIFIED&quot; |
| LABEL_DETECTION | &quot;LABEL_DETECTION&quot; |
| SHOT_CHANGE_DETECTION | &quot;SHOT_CHANGE_DETECTION&quot; |
| EXPLICIT_CONTENT_DETECTION | &quot;EXPLICIT_CONTENT_DETECTION&quot; |
| FACE_DETECTION | &quot;FACE_DETECTION&quot; |
| SPEECH_TRANSCRIPTION | &quot;SPEECH_TRANSCRIPTION&quot; |
| TEXT_DETECTION | &quot;TEXT_DETECTION&quot; |
| OBJECT_TRACKING | &quot;OBJECT_TRACKING&quot; |
| LOGO_RECOGNITION | &quot;LOGO_RECOGNITION&quot; |
| PERSON_DETECTION | &quot;PERSON_DETECTION&quot; |



