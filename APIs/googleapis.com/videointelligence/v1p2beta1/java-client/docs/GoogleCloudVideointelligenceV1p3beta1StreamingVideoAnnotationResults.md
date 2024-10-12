

# GoogleCloudVideointelligenceV1p3beta1StreamingVideoAnnotationResults

Streaming annotation results corresponding to a portion of the video that is currently being processed. Only ONE type of annotation will be specified in the response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**explicitAnnotation** | [**GoogleCloudVideointelligenceV1p3beta1ExplicitContentAnnotation**](GoogleCloudVideointelligenceV1p3beta1ExplicitContentAnnotation.md) |  |  [optional] |
|**frameTimestamp** | **String** | Timestamp of the processed frame in microseconds. |  [optional] |
|**labelAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1p3beta1LabelAnnotation&gt;**](GoogleCloudVideointelligenceV1p3beta1LabelAnnotation.md) | Label annotation results. |  [optional] |
|**objectAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1p3beta1ObjectTrackingAnnotation&gt;**](GoogleCloudVideointelligenceV1p3beta1ObjectTrackingAnnotation.md) | Object tracking results. |  [optional] |
|**shotAnnotations** | [**List&lt;GoogleCloudVideointelligenceV1p3beta1VideoSegment&gt;**](GoogleCloudVideointelligenceV1p3beta1VideoSegment.md) | Shot annotation results. Each shot is represented as a video segment. |  [optional] |



