

# GoogleCloudVideointelligenceV1p3beta1VideoContext

Video context and/or feature-specific parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**explicitContentDetectionConfig** | [**GoogleCloudVideointelligenceV1p3beta1ExplicitContentDetectionConfig**](GoogleCloudVideointelligenceV1p3beta1ExplicitContentDetectionConfig.md) |  |  [optional] |
|**faceDetectionConfig** | [**GoogleCloudVideointelligenceV1p3beta1FaceDetectionConfig**](GoogleCloudVideointelligenceV1p3beta1FaceDetectionConfig.md) |  |  [optional] |
|**labelDetectionConfig** | [**GoogleCloudVideointelligenceV1p3beta1LabelDetectionConfig**](GoogleCloudVideointelligenceV1p3beta1LabelDetectionConfig.md) |  |  [optional] |
|**objectTrackingConfig** | [**GoogleCloudVideointelligenceV1p3beta1ObjectTrackingConfig**](GoogleCloudVideointelligenceV1p3beta1ObjectTrackingConfig.md) |  |  [optional] |
|**personDetectionConfig** | [**GoogleCloudVideointelligenceV1p3beta1PersonDetectionConfig**](GoogleCloudVideointelligenceV1p3beta1PersonDetectionConfig.md) |  |  [optional] |
|**segments** | [**List&lt;GoogleCloudVideointelligenceV1p3beta1VideoSegment&gt;**](GoogleCloudVideointelligenceV1p3beta1VideoSegment.md) | Video segments to annotate. The segments may overlap and are not required to be contiguous or span the whole video. If unspecified, each video is treated as a single segment. |  [optional] |
|**shotChangeDetectionConfig** | [**GoogleCloudVideointelligenceV1p3beta1ShotChangeDetectionConfig**](GoogleCloudVideointelligenceV1p3beta1ShotChangeDetectionConfig.md) |  |  [optional] |
|**speechTranscriptionConfig** | [**GoogleCloudVideointelligenceV1p3beta1SpeechTranscriptionConfig**](GoogleCloudVideointelligenceV1p3beta1SpeechTranscriptionConfig.md) |  |  [optional] |
|**textDetectionConfig** | [**GoogleCloudVideointelligenceV1p3beta1TextDetectionConfig**](GoogleCloudVideointelligenceV1p3beta1TextDetectionConfig.md) |  |  [optional] |



