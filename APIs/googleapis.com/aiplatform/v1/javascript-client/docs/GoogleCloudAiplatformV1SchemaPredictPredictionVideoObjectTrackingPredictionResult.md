# VertexAiApi.GoogleCloudAiplatformV1SchemaPredictPredictionVideoObjectTrackingPredictionResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **Number** | The Model&#39;s confidence in correction of this prediction, higher value means higher confidence. | [optional] 
**displayName** | **String** | The display name of the AnnotationSpec that had been identified. | [optional] 
**frames** | [**[GoogleCloudAiplatformV1SchemaPredictPredictionVideoObjectTrackingPredictionResultFrame]**](GoogleCloudAiplatformV1SchemaPredictPredictionVideoObjectTrackingPredictionResultFrame.md) | All of the frames of the video in which a single object instance has been detected. The bounding boxes in the frames identify the same object. | [optional] 
**id** | **String** | The resource ID of the AnnotationSpec that had been identified. | [optional] 
**timeSegmentEnd** | **String** | The end, inclusive, of the video&#39;s time segment in which the object instance has been detected. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with \&quot;s\&quot; appended at the end. | [optional] 
**timeSegmentStart** | **String** | The beginning, inclusive, of the video&#39;s time segment in which the object instance has been detected. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with \&quot;s\&quot; appended at the end. | [optional] 


