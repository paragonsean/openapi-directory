

# GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetrics

Metrics across multiple confidence levels.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auprc** | **Float** | The calculated area under the precision recall curve (AUPRC), computed by integrating over all confidence thresholds. |  [optional] |
|**auprcExact** | **Float** | The AUPRC for metrics with fuzzy matching disabled, i.e., exact matching only. |  [optional] |
|**confidenceLevelMetrics** | [**List&lt;GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetrics&gt;**](GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetrics.md) | Metrics across confidence levels with fuzzy matching enabled. |  [optional] |
|**confidenceLevelMetricsExact** | [**List&lt;GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetrics&gt;**](GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetrics.md) | Metrics across confidence levels with only exact matching. |  [optional] |
|**estimatedCalibrationError** | **Float** | The Estimated Calibration Error (ECE) of the confidence of the predicted entities. |  [optional] |
|**estimatedCalibrationErrorExact** | **Float** | The ECE for the predicted entities with fuzzy matching disabled, i.e., exact matching only. |  [optional] |
|**metricsType** | [**MetricsTypeEnum**](#MetricsTypeEnum) | The metrics type for the label. |  [optional] |



## Enum: MetricsTypeEnum

| Name | Value |
|---- | -----|
| METRICS_TYPE_UNSPECIFIED | &quot;METRICS_TYPE_UNSPECIFIED&quot; |
| AGGREGATE | &quot;AGGREGATE&quot; |



