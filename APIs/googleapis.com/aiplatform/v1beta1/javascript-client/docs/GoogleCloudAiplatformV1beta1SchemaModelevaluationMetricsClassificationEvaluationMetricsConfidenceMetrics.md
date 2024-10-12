# VertexAiApi.GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsClassificationEvaluationMetricsConfidenceMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidenceThreshold** | **Number** | Metrics are computed with an assumption that the Model never returns predictions with score lower than this value. | [optional] 
**confusionMatrix** | [**GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix**](GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix.md) |  | [optional] 
**f1Score** | **Number** | The harmonic mean of recall and precision. For summary metrics, it computes the micro-averaged F1 score. | [optional] 
**f1ScoreAt1** | **Number** | The harmonic mean of recallAt1 and precisionAt1. | [optional] 
**f1ScoreMacro** | **Number** | Macro-averaged F1 Score. | [optional] 
**f1ScoreMicro** | **Number** | Micro-averaged F1 Score. | [optional] 
**falseNegativeCount** | **String** | The number of ground truth labels that are not matched by a Model created label. | [optional] 
**falsePositiveCount** | **String** | The number of Model created labels that do not match a ground truth label. | [optional] 
**falsePositiveRate** | **Number** | False Positive Rate for the given confidence threshold. | [optional] 
**falsePositiveRateAt1** | **Number** | The False Positive Rate when only considering the label that has the highest prediction score and not below the confidence threshold for each DataItem. | [optional] 
**maxPredictions** | **Number** | Metrics are computed with an assumption that the Model always returns at most this many predictions (ordered by their score, descendingly), but they all still need to meet the &#x60;confidenceThreshold&#x60;. | [optional] 
**precision** | **Number** | Precision for the given confidence threshold. | [optional] 
**precisionAt1** | **Number** | The precision when only considering the label that has the highest prediction score and not below the confidence threshold for each DataItem. | [optional] 
**recall** | **Number** | Recall (True Positive Rate) for the given confidence threshold. | [optional] 
**recallAt1** | **Number** | The Recall (True Positive Rate) when only considering the label that has the highest prediction score and not below the confidence threshold for each DataItem. | [optional] 
**trueNegativeCount** | **String** | The number of labels that were not created by the Model, but if they would, they would not match a ground truth label. | [optional] 
**truePositiveCount** | **String** | The number of Model created labels that match a ground truth label. | [optional] 


