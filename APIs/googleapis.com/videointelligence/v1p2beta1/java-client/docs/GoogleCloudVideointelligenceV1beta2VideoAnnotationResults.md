

# GoogleCloudVideointelligenceV1beta2VideoAnnotationResults

Annotation results for a single video.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**explicitAnnotation** | [**GoogleCloudVideointelligenceV1beta2ExplicitContentAnnotation**](GoogleCloudVideointelligenceV1beta2ExplicitContentAnnotation.md) |  |  [optional] |
|**faceAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1beta2FaceAnnotation&gt;**](GoogleCloudVideointelligenceV1beta2FaceAnnotation.md) | Deprecated. Please use &#x60;face_detection_annotations&#x60; instead. |  [optional] |
|**faceDetectionAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1beta2FaceDetectionAnnotation&gt;**](GoogleCloudVideointelligenceV1beta2FaceDetectionAnnotation.md) | Face detection annotations. |  [optional] |
|**frameLabelAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1beta2LabelAnnotation&gt;**](GoogleCloudVideointelligenceV1beta2LabelAnnotation.md) | Label annotations on frame level. There is exactly one element for each unique label. |  [optional] |
|**inputUri** | **String** | Video file location in [Cloud Storage](https://cloud.google.com/storage/). |  [optional] |
|**logoRecognitionAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1beta2LogoRecognitionAnnotation&gt;**](GoogleCloudVideointelligenceV1beta2LogoRecognitionAnnotation.md) | Annotations for list of logos detected, tracked and recognized in video. |  [optional] |
|**objectAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1beta2ObjectTrackingAnnotation&gt;**](GoogleCloudVideointelligenceV1beta2ObjectTrackingAnnotation.md) | Annotations for list of objects detected and tracked in video. |  [optional] |
|**personDetectionAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1beta2PersonDetectionAnnotation&gt;**](GoogleCloudVideointelligenceV1beta2PersonDetectionAnnotation.md) | Person detection annotations. |  [optional] |
|**segment** | [**GoogleCloudVideointelligenceV1beta2VideoSegment**](GoogleCloudVideointelligenceV1beta2VideoSegment.md) |  |  [optional] |
|**segmentLabelAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1beta2LabelAnnotation&gt;**](GoogleCloudVideointelligenceV1beta2LabelAnnotation.md) | Topical label annotations on video level or user-specified segment level. There is exactly one element for each unique label. |  [optional] |
|**segmentPresenceLabelAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1beta2LabelAnnotation&gt;**](GoogleCloudVideointelligenceV1beta2LabelAnnotation.md) | Presence label annotations on video level or user-specified segment level. There is exactly one element for each unique label. Compared to the existing topical &#x60;segment_label_annotations&#x60;, this field presents more fine-grained, segment-level labels detected in video content and is made available only when the client sets &#x60;LabelDetectionConfig.model&#x60; to \&quot;builtin/latest\&quot; in the request. |  [optional] |
|**shotAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1beta2VideoSegment&gt;**](GoogleCloudVideointelligenceV1beta2VideoSegment.md) | Shot annotations. Each shot is represented as a video segment. |  [optional] |
|**shotLabelAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1beta2LabelAnnotation&gt;**](GoogleCloudVideointelligenceV1beta2LabelAnnotation.md) | Topical label annotations on shot level. There is exactly one element for each unique label. |  [optional] |
|**shotPresenceLabelAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1beta2LabelAnnotation&gt;**](GoogleCloudVideointelligenceV1beta2LabelAnnotation.md) | Presence label annotations on shot level. There is exactly one element for each unique label. Compared to the existing topical &#x60;shot_label_annotations&#x60;, this field presents more fine-grained, shot-level labels detected in video content and is made available only when the client sets &#x60;LabelDetectionConfig.model&#x60; to \&quot;builtin/latest\&quot; in the request. |  [optional] |
|**speechTranscriptions** | [**List&lt;GoogleCloudVideointelligenceV1beta2SpeechTranscription&gt;**](GoogleCloudVideointelligenceV1beta2SpeechTranscription.md) | Speech transcription. |  [optional] |
|**textAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1beta2TextAnnotation&gt;**](GoogleCloudVideointelligenceV1beta2TextAnnotation.md) | OCR text detection and tracking. Annotations for list of detected text snippets. Each will have list of frame information associated with it. |  [optional] |



