

# GoogleCloudVideointelligenceV1VideoContext

Video context and/or feature-specific parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**explicitContentDetectionConfig** | [**GoogleCloudVideointelligenceV1ExplicitContentDetectionConfig**](GoogleCloudVideointelligenceV1ExplicitContentDetectionConfig.md) |  |  [optional] |
|**faceDetectionConfig** | [**GoogleCloudVideointelligenceV1FaceDetectionConfig**](GoogleCloudVideointelligenceV1FaceDetectionConfig.md) |  |  [optional] |
|**labelDetectionConfig** | [**GoogleCloudVideointelligenceV1LabelDetectionConfig**](GoogleCloudVideointelligenceV1LabelDetectionConfig.md) |  |  [optional] |
|**objectTrackingConfig** | [**GoogleCloudVideointelligenceV1ObjectTrackingConfig**](GoogleCloudVideointelligenceV1ObjectTrackingConfig.md) |  |  [optional] |
|**personDetectionConfig** | [**GoogleCloudVideointelligenceV1PersonDetectionConfig**](GoogleCloudVideointelligenceV1PersonDetectionConfig.md) |  |  [optional] |
|**segments** | [**List&lt;GoogleCloudVideointelligenceV1VideoSegment&gt;**](GoogleCloudVideointelligenceV1VideoSegment.md) | Video segments to annotate. The segments may overlap and are not required to be contiguous or span the whole video. If unspecified, each video is treated as a single segment. |  [optional] |
|**shotChangeDetectionConfig** | [**GoogleCloudVideointelligenceV1ShotChangeDetectionConfig**](GoogleCloudVideointelligenceV1ShotChangeDetectionConfig.md) |  |  [optional] |
|**speechTranscriptionConfig** | [**GoogleCloudVideointelligenceV1SpeechTranscriptionConfig**](GoogleCloudVideointelligenceV1SpeechTranscriptionConfig.md) |  |  [optional] |
|**textDetectionConfig** | [**GoogleCloudVideointelligenceV1TextDetectionConfig**](GoogleCloudVideointelligenceV1TextDetectionConfig.md) |  |  [optional] |



