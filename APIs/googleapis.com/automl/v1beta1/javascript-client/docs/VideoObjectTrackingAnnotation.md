# CloudAutoMlApi.VideoObjectTrackingAnnotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundingBox** | [**BoundingPoly**](BoundingPoly.md) |  | [optional] 
**instanceId** | **String** | Optional. The instance of the object, expressed as a positive integer. Used to tell apart objects of the same type (i.e. AnnotationSpec) when multiple are present on a single example. NOTE: Instance ID prediction quality is not a part of model evaluation and is done as best effort. Especially in cases when an entity goes off-screen for a longer time (minutes), when it comes back it may be given a new instance ID. | [optional] 
**score** | **Number** | Output only. The confidence that this annotation is positive for the video at the time_offset, value in [0, 1], higher means higher positivity confidence. For annotations created by the user the score is 1. When user approves an annotation, the original float score is kept (and not changed to 1). | [optional] 
**timeOffset** | **String** | Required. A time (frame) of a video to which this annotation pertains. Represented as the duration since the video&#39;s start. | [optional] 


