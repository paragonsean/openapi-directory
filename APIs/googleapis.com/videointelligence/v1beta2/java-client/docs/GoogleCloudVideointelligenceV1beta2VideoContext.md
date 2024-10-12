

# GoogleCloudVideointelligenceV1beta2VideoContext

Video context and/or feature-specific parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**explicitContentDetectionConfig** | [**GoogleCloudVideointelligenceV1beta2ExplicitContentDetectionConfig**](GoogleCloudVideointelligenceV1beta2ExplicitContentDetectionConfig.md) |  |  [optional] |
|**faceDetectionConfig** | [**GoogleCloudVideointelligenceV1beta2FaceDetectionConfig**](GoogleCloudVideointelligenceV1beta2FaceDetectionConfig.md) |  |  [optional] |
|**labelDetectionConfig** | [**GoogleCloudVideointelligenceV1beta2LabelDetectionConfig**](GoogleCloudVideointelligenceV1beta2LabelDetectionConfig.md) |  |  [optional] |
|**objectTrackingConfig** | [**GoogleCloudVideointelligenceV1beta2ObjectTrackingConfig**](GoogleCloudVideointelligenceV1beta2ObjectTrackingConfig.md) |  |  [optional] |
|**personDetectionConfig** | [**GoogleCloudVideointelligenceV1beta2PersonDetectionConfig**](GoogleCloudVideointelligenceV1beta2PersonDetectionConfig.md) |  |  [optional] |
|**segments** | [**List&lt;GoogleCloudVideointelligenceV1beta2VideoSegment&gt;**](GoogleCloudVideointelligenceV1beta2VideoSegment.md) | Video segments to annotate. The segments may overlap and are not required to be contiguous or span the whole video. If unspecified, each video is treated as a single segment. |  [optional] |
|**shotChangeDetectionConfig** | [**GoogleCloudVideointelligenceV1beta2ShotChangeDetectionConfig**](GoogleCloudVideointelligenceV1beta2ShotChangeDetectionConfig.md) |  |  [optional] |
|**speechTranscriptionConfig** | [**GoogleCloudVideointelligenceV1beta2SpeechTranscriptionConfig**](GoogleCloudVideointelligenceV1beta2SpeechTranscriptionConfig.md) |  |  [optional] |
|**textDetectionConfig** | [**GoogleCloudVideointelligenceV1beta2TextDetectionConfig**](GoogleCloudVideointelligenceV1beta2TextDetectionConfig.md) |  |  [optional] |



