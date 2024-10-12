# CloudVideoIntelligenceApi.GoogleCloudVideointelligenceV1p1beta1VideoAnnotationResults

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**explicitAnnotation** | [**GoogleCloudVideointelligenceV1p1beta1ExplicitContentAnnotation**](GoogleCloudVideointelligenceV1p1beta1ExplicitContentAnnotation.md) |  | [optional] 
**faceAnnotations** | [**[GoogleCloudVideointelligenceV1p1beta1FaceAnnotation]**](GoogleCloudVideointelligenceV1p1beta1FaceAnnotation.md) | Deprecated. Please use &#x60;face_detection_annotations&#x60; instead. | [optional] 
**faceDetectionAnnotations** | [**[GoogleCloudVideointelligenceV1p1beta1FaceDetectionAnnotation]**](GoogleCloudVideointelligenceV1p1beta1FaceDetectionAnnotation.md) | Face detection annotations. | [optional] 
**frameLabelAnnotations** | [**[GoogleCloudVideointelligenceV1p1beta1LabelAnnotation]**](GoogleCloudVideointelligenceV1p1beta1LabelAnnotation.md) | Label annotations on frame level. There is exactly one element for each unique label. | [optional] 
**inputUri** | **String** | Video file location in [Cloud Storage](https://cloud.google.com/storage/). | [optional] 
**logoRecognitionAnnotations** | [**[GoogleCloudVideointelligenceV1p1beta1LogoRecognitionAnnotation]**](GoogleCloudVideointelligenceV1p1beta1LogoRecognitionAnnotation.md) | Annotations for list of logos detected, tracked and recognized in video. | [optional] 
**objectAnnotations** | [**[GoogleCloudVideointelligenceV1p1beta1ObjectTrackingAnnotation]**](GoogleCloudVideointelligenceV1p1beta1ObjectTrackingAnnotation.md) | Annotations for list of objects detected and tracked in video. | [optional] 
**personDetectionAnnotations** | [**[GoogleCloudVideointelligenceV1p1beta1PersonDetectionAnnotation]**](GoogleCloudVideointelligenceV1p1beta1PersonDetectionAnnotation.md) | Person detection annotations. | [optional] 
**segment** | [**GoogleCloudVideointelligenceV1p1beta1VideoSegment**](GoogleCloudVideointelligenceV1p1beta1VideoSegment.md) |  | [optional] 
**segmentLabelAnnotations** | [**[GoogleCloudVideointelligenceV1p1beta1LabelAnnotation]**](GoogleCloudVideointelligenceV1p1beta1LabelAnnotation.md) | Topical label annotations on video level or user-specified segment level. There is exactly one element for each unique label. | [optional] 
**segmentPresenceLabelAnnotations** | [**[GoogleCloudVideointelligenceV1p1beta1LabelAnnotation]**](GoogleCloudVideointelligenceV1p1beta1LabelAnnotation.md) | Presence label annotations on video level or user-specified segment level. There is exactly one element for each unique label. Compared to the existing topical &#x60;segment_label_annotations&#x60;, this field presents more fine-grained, segment-level labels detected in video content and is made available only when the client sets &#x60;LabelDetectionConfig.model&#x60; to \&quot;builtin/latest\&quot; in the request. | [optional] 
**shotAnnotations** | [**[GoogleCloudVideointelligenceV1p1beta1VideoSegment]**](GoogleCloudVideointelligenceV1p1beta1VideoSegment.md) | Shot annotations. Each shot is represented as a video segment. | [optional] 
**shotLabelAnnotations** | [**[GoogleCloudVideointelligenceV1p1beta1LabelAnnotation]**](GoogleCloudVideointelligenceV1p1beta1LabelAnnotation.md) | Topical label annotations on shot level. There is exactly one element for each unique label. | [optional] 
**shotPresenceLabelAnnotations** | [**[GoogleCloudVideointelligenceV1p1beta1LabelAnnotation]**](GoogleCloudVideointelligenceV1p1beta1LabelAnnotation.md) | Presence label annotations on shot level. There is exactly one element for each unique label. Compared to the existing topical &#x60;shot_label_annotations&#x60;, this field presents more fine-grained, shot-level labels detected in video content and is made available only when the client sets &#x60;LabelDetectionConfig.model&#x60; to \&quot;builtin/latest\&quot; in the request. | [optional] 
**speechTranscriptions** | [**[GoogleCloudVideointelligenceV1p1beta1SpeechTranscription]**](GoogleCloudVideointelligenceV1p1beta1SpeechTranscription.md) | Speech transcription. | [optional] 
**textAnnotations** | [**[GoogleCloudVideointelligenceV1p1beta1TextAnnotation]**](GoogleCloudVideointelligenceV1p1beta1TextAnnotation.md) | OCR text detection and tracking. Annotations for list of detected text snippets. Each will have list of frame information associated with it. | [optional] 


