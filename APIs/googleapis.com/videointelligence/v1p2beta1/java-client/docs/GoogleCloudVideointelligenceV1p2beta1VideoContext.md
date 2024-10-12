

# GoogleCloudVideointelligenceV1p2beta1VideoContext

Video context and/or feature-specific parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**explicitContentDetectionConfig** | [**GoogleCloudVideointelligenceV1p2beta1ExplicitContentDetectionConfig**](GoogleCloudVideointelligenceV1p2beta1ExplicitContentDetectionConfig.md) |  |  [optional] |
|**faceDetectionConfig** | [**GoogleCloudVideointelligenceV1p2beta1FaceDetectionConfig**](GoogleCloudVideointelligenceV1p2beta1FaceDetectionConfig.md) |  |  [optional] |
|**labelDetectionConfig** | [**GoogleCloudVideointelligenceV1p2beta1LabelDetectionConfig**](GoogleCloudVideointelligenceV1p2beta1LabelDetectionConfig.md) |  |  [optional] |
|**objectTrackingConfig** | [**GoogleCloudVideointelligenceV1p2beta1ObjectTrackingConfig**](GoogleCloudVideointelligenceV1p2beta1ObjectTrackingConfig.md) |  |  [optional] |
|**personDetectionConfig** | [**GoogleCloudVideointelligenceV1p2beta1PersonDetectionConfig**](GoogleCloudVideointelligenceV1p2beta1PersonDetectionConfig.md) |  |  [optional] |
|**segments** | [**List&lt;GoogleCloudVideointelligenceV1p2beta1VideoSegment&gt;**](GoogleCloudVideointelligenceV1p2beta1VideoSegment.md) | Video segments to annotate. The segments may overlap and are not required to be contiguous or span the whole video. If unspecified, each video is treated as a single segment. |  [optional] |
|**shotChangeDetectionConfig** | [**GoogleCloudVideointelligenceV1p2beta1ShotChangeDetectionConfig**](GoogleCloudVideointelligenceV1p2beta1ShotChangeDetectionConfig.md) |  |  [optional] |
|**speechTranscriptionConfig** | [**GoogleCloudVideointelligenceV1p2beta1SpeechTranscriptionConfig**](GoogleCloudVideointelligenceV1p2beta1SpeechTranscriptionConfig.md) |  |  [optional] |
|**textDetectionConfig** | [**GoogleCloudVideointelligenceV1p2beta1TextDetectionConfig**](GoogleCloudVideointelligenceV1p2beta1TextDetectionConfig.md) |  |  [optional] |



