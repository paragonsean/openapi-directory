# CloudVideoIntelligenceApi.GoogleCloudVideointelligenceV1VideoAnnotationProgress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **String** | Specifies which feature is being tracked if the request contains more than one feature. | [optional] 
**inputUri** | **String** | Video file location in [Cloud Storage](https://cloud.google.com/storage/). | [optional] 
**progressPercent** | **Number** | Approximate percentage processed thus far. Guaranteed to be 100 when fully processed. | [optional] 
**segment** | [**GoogleCloudVideointelligenceV1VideoSegment**](GoogleCloudVideointelligenceV1VideoSegment.md) |  | [optional] 
**startTime** | **String** | Time when the request was received. | [optional] 
**updateTime** | **String** | Time of the most recent update. | [optional] 



## Enum: FeatureEnum


* `FEATURE_UNSPECIFIED` (value: `"FEATURE_UNSPECIFIED"`)

* `LABEL_DETECTION` (value: `"LABEL_DETECTION"`)

* `SHOT_CHANGE_DETECTION` (value: `"SHOT_CHANGE_DETECTION"`)

* `EXPLICIT_CONTENT_DETECTION` (value: `"EXPLICIT_CONTENT_DETECTION"`)

* `FACE_DETECTION` (value: `"FACE_DETECTION"`)

* `SPEECH_TRANSCRIPTION` (value: `"SPEECH_TRANSCRIPTION"`)

* `TEXT_DETECTION` (value: `"TEXT_DETECTION"`)

* `OBJECT_TRACKING` (value: `"OBJECT_TRACKING"`)

* `LOGO_RECOGNITION` (value: `"LOGO_RECOGNITION"`)

* `PERSON_DETECTION` (value: `"PERSON_DETECTION"`)




