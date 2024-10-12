

# GoogleCloudAiplatformV1SchemaModelevaluationMetricsImageSegmentationEvaluationMetricsConfidenceMetricsEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidenceThreshold** | **Float** | Metrics are computed with an assumption that the model never returns predictions with score lower than this value. |  [optional] |
|**confusionMatrix** | [**GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrix**](GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrix.md) |  |  [optional] |
|**diceScoreCoefficient** | **Float** | DSC or the F1 score, The harmonic mean of recall and precision. |  [optional] |
|**iouScore** | **Float** | The intersection-over-union score. The measure of overlap of the annotation&#39;s category mask with ground truth category mask on the DataItem. |  [optional] |
|**precision** | **Float** | Precision for the given confidence threshold. |  [optional] |
|**recall** | **Float** | Recall (True Positive Rate) for the given confidence threshold. |  [optional] |



