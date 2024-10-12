

# TextExtractionEvaluationMetricsConfidenceMetricsEntry

Metrics for a single confidence threshold.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidenceThreshold** | **Float** | Output only. The confidence threshold value used to compute the metrics. Only annotations with score of at least this threshold are considered to be ones the model would return. |  [optional] |
|**f1Score** | **Float** | Output only. The harmonic mean of recall and precision. |  [optional] |
|**precision** | **Float** | Output only. Precision under the given confidence threshold. |  [optional] |
|**recall** | **Float** | Output only. Recall under the given confidence threshold. |  [optional] |



