

# GoogleCloudAiplatformV1beta1SchemaVideoObjectTrackingAnnotation

Annotation details specific to video object tracking.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationSpecId** | **String** | The resource Id of the AnnotationSpec that this Annotation pertains to. |  [optional] |
|**displayName** | **String** | The display name of the AnnotationSpec that this Annotation pertains to. |  [optional] |
|**instanceId** | **String** | The instance of the object, expressed as a positive integer. Used to track the same object across different frames. |  [optional] |
|**timeOffset** | **String** | A time (frame) of a video to which this annotation pertains. Represented as the duration since the video&#39;s start. |  [optional] |
|**xMax** | **Double** | The rightmost coordinate of the bounding box. |  [optional] |
|**xMin** | **Double** | The leftmost coordinate of the bounding box. |  [optional] |
|**yMax** | **Double** | The bottommost coordinate of the bounding box. |  [optional] |
|**yMin** | **Double** | The topmost coordinate of the bounding box. |  [optional] |



