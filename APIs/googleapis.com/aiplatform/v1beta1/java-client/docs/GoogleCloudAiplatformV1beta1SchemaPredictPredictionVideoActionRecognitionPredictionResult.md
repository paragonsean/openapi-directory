

# GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoActionRecognitionPredictionResult

Prediction output format for Video Action Recognition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidence** | **Float** | The Model&#39;s confidence in correction of this prediction, higher value means higher confidence. |  [optional] |
|**displayName** | **String** | The display name of the AnnotationSpec that had been identified. |  [optional] |
|**id** | **String** | The resource ID of the AnnotationSpec that had been identified. |  [optional] |
|**timeSegmentEnd** | **String** | The end, exclusive, of the video&#39;s time segment in which the AnnotationSpec has been identified. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with \&quot;s\&quot; appended at the end. |  [optional] |
|**timeSegmentStart** | **String** | The beginning, inclusive, of the video&#39;s time segment in which the AnnotationSpec has been identified. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with \&quot;s\&quot; appended at the end. |  [optional] |



