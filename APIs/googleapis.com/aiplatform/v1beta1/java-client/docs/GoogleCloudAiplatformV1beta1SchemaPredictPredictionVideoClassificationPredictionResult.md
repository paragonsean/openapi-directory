

# GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoClassificationPredictionResult

Prediction output format for Video Classification.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidence** | **Float** | The Model&#39;s confidence in correction of this prediction, higher value means higher confidence. |  [optional] |
|**displayName** | **String** | The display name of the AnnotationSpec that had been identified. |  [optional] |
|**id** | **String** | The resource ID of the AnnotationSpec that had been identified. |  [optional] |
|**timeSegmentEnd** | **String** | The end, exclusive, of the video&#39;s time segment in which the AnnotationSpec has been identified. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with \&quot;s\&quot; appended at the end. Note that for &#39;segment-classification&#39; prediction type, this equals the original &#39;timeSegmentEnd&#39; from the input instance, for other types it is the end of a shot or a 1 second interval respectively. |  [optional] |
|**timeSegmentStart** | **String** | The beginning, inclusive, of the video&#39;s time segment in which the AnnotationSpec has been identified. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with \&quot;s\&quot; appended at the end. Note that for &#39;segment-classification&#39; prediction type, this equals the original &#39;timeSegmentStart&#39; from the input instance, for other types it is the start of a shot or a 1 second interval respectively. |  [optional] |
|**type** | **String** | The type of the prediction. The requested types can be configured via parameters. This will be one of - segment-classification - shot-classification - one-sec-interval-classification |  [optional] |



