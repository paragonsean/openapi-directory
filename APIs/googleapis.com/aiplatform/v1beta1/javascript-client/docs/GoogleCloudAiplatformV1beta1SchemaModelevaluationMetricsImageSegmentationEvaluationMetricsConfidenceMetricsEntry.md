# VertexAiApi.GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsImageSegmentationEvaluationMetricsConfidenceMetricsEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidenceThreshold** | **Number** | Metrics are computed with an assumption that the model never returns predictions with score lower than this value. | [optional] 
**confusionMatrix** | [**GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix**](GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix.md) |  | [optional] 
**diceScoreCoefficient** | **Number** | DSC or the F1 score, The harmonic mean of recall and precision. | [optional] 
**iouScore** | **Number** | The intersection-over-union score. The measure of overlap of the annotation&#39;s category mask with ground truth category mask on the DataItem. | [optional] 
**precision** | **Number** | Precision for the given confidence threshold. | [optional] 
**recall** | **Number** | Recall (True Positive Rate) for the given confidence threshold. | [optional] 


