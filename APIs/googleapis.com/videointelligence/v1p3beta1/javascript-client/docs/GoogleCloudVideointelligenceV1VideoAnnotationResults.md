# CloudVideoIntelligenceApi.GoogleCloudVideointelligenceV1VideoAnnotationResults

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**explicitAnnotation** | [**GoogleCloudVideointelligenceV1ExplicitContentAnnotation**](GoogleCloudVideointelligenceV1ExplicitContentAnnotation.md) |  | [optional] 
**faceAnnotations** | [**[GoogleCloudVideointelligenceV1FaceAnnotation]**](GoogleCloudVideointelligenceV1FaceAnnotation.md) | Deprecated. Please use &#x60;face_detection_annotations&#x60; instead. | [optional] 
**faceDetectionAnnotations** | [**[GoogleCloudVideointelligenceV1FaceDetectionAnnotation]**](GoogleCloudVideointelligenceV1FaceDetectionAnnotation.md) | Face detection annotations. | [optional] 
**frameLabelAnnotations** | [**[GoogleCloudVideointelligenceV1LabelAnnotation]**](GoogleCloudVideointelligenceV1LabelAnnotation.md) | Label annotations on frame level. There is exactly one element for each unique label. | [optional] 
**inputUri** | **String** | Video file location in [Cloud Storage](https://cloud.google.com/storage/). | [optional] 
**logoRecognitionAnnotations** | [**[GoogleCloudVideointelligenceV1LogoRecognitionAnnotation]**](GoogleCloudVideointelligenceV1LogoRecognitionAnnotation.md) | Annotations for list of logos detected, tracked and recognized in video. | [optional] 
**objectAnnotations** | [**[GoogleCloudVideointelligenceV1ObjectTrackingAnnotation]**](GoogleCloudVideointelligenceV1ObjectTrackingAnnotation.md) | Annotations for list of objects detected and tracked in video. | [optional] 
**personDetectionAnnotations** | [**[GoogleCloudVideointelligenceV1PersonDetectionAnnotation]**](GoogleCloudVideointelligenceV1PersonDetectionAnnotation.md) | Person detection annotations. | [optional] 
**segment** | [**GoogleCloudVideointelligenceV1VideoSegment**](GoogleCloudVideointelligenceV1VideoSegment.md) |  | [optional] 
**segmentLabelAnnotations** | [**[GoogleCloudVideointelligenceV1LabelAnnotation]**](GoogleCloudVideointelligenceV1LabelAnnotation.md) | Topical label annotations on video level or user-specified segment level. There is exactly one element for each unique label. | [optional] 
**segmentPresenceLabelAnnotations** | [**[GoogleCloudVideointelligenceV1LabelAnnotation]**](GoogleCloudVideointelligenceV1LabelAnnotation.md) | Presence label annotations on video level or user-specified segment level. There is exactly one element for each unique label. Compared to the existing topical &#x60;segment_label_annotations&#x60;, this field presents more fine-grained, segment-level labels detected in video content and is made available only when the client sets &#x60;LabelDetectionConfig.model&#x60; to \&quot;builtin/latest\&quot; in the request. | [optional] 
**shotAnnotations** | [**[GoogleCloudVideointelligenceV1VideoSegment]**](GoogleCloudVideointelligenceV1VideoSegment.md) | Shot annotations. Each shot is represented as a video segment. | [optional] 
**shotLabelAnnotations** | [**[GoogleCloudVideointelligenceV1LabelAnnotation]**](GoogleCloudVideointelligenceV1LabelAnnotation.md) | Topical label annotations on shot level. There is exactly one element for each unique label. | [optional] 
**shotPresenceLabelAnnotations** | [**[GoogleCloudVideointelligenceV1LabelAnnotation]**](GoogleCloudVideointelligenceV1LabelAnnotation.md) | Presence label annotations on shot level. There is exactly one element for each unique label. Compared to the existing topical &#x60;shot_label_annotations&#x60;, this field presents more fine-grained, shot-level labels detected in video content and is made available only when the client sets &#x60;LabelDetectionConfig.model&#x60; to \&quot;builtin/latest\&quot; in the request. | [optional] 
**speechTranscriptions** | [**[GoogleCloudVideointelligenceV1SpeechTranscription]**](GoogleCloudVideointelligenceV1SpeechTranscription.md) | Speech transcription. | [optional] 
**textAnnotations** | [**[GoogleCloudVideointelligenceV1TextAnnotation]**](GoogleCloudVideointelligenceV1TextAnnotation.md) | OCR text detection and tracking. Annotations for list of detected text snippets. Each will have list of frame information associated with it. | [optional] 


