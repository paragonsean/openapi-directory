

# ClassificationEvaluationMetricsConfidenceMetricsEntry

Metrics for a single confidence threshold.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidenceThreshold** | **Float** | Output only. Metrics are computed with an assumption that the model never returns predictions with score lower than this value. |  [optional] |
|**f1Score** | **Float** | Output only. The harmonic mean of recall and precision. |  [optional] |
|**f1ScoreAt1** | **Float** | Output only. The harmonic mean of recall_at1 and precision_at1. |  [optional] |
|**falseNegativeCount** | **String** | Output only. The number of ground truth labels that are not matched by a model created label. |  [optional] |
|**falsePositiveCount** | **String** | Output only. The number of model created labels that do not match a ground truth label. |  [optional] |
|**falsePositiveRate** | **Float** | Output only. False Positive Rate for the given confidence threshold. |  [optional] |
|**falsePositiveRateAt1** | **Float** | Output only. The False Positive Rate when only considering the label that has the highest prediction score and not below the confidence threshold for each example. |  [optional] |
|**positionThreshold** | **Integer** | Output only. Metrics are computed with an assumption that the model always returns at most this many predictions (ordered by their score, descendingly), but they all still need to meet the confidence_threshold. |  [optional] |
|**precision** | **Float** | Output only. Precision for the given confidence threshold. |  [optional] |
|**precisionAt1** | **Float** | Output only. The precision when only considering the label that has the highest prediction score and not below the confidence threshold for each example. |  [optional] |
|**recall** | **Float** | Output only. Recall (True Positive Rate) for the given confidence threshold. |  [optional] |
|**recallAt1** | **Float** | Output only. The Recall (True Positive Rate) when only considering the label that has the highest prediction score and not below the confidence threshold for each example. |  [optional] |
|**trueNegativeCount** | **String** | Output only. The number of labels that were not created by the model, but if they would, they would not match a ground truth label. |  [optional] |
|**truePositiveCount** | **String** | Output only. The number of model created labels that match a ground truth label. |  [optional] |



