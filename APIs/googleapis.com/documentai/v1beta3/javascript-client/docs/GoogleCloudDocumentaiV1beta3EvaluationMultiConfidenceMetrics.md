# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3EvaluationMultiConfidenceMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auprc** | **Number** | The calculated area under the precision recall curve (AUPRC), computed by integrating over all confidence thresholds. | [optional] 
**auprcExact** | **Number** | The AUPRC for metrics with fuzzy matching disabled, i.e., exact matching only. | [optional] 
**confidenceLevelMetrics** | [**[GoogleCloudDocumentaiV1beta3EvaluationConfidenceLevelMetrics]**](GoogleCloudDocumentaiV1beta3EvaluationConfidenceLevelMetrics.md) | Metrics across confidence levels with fuzzy matching enabled. | [optional] 
**confidenceLevelMetricsExact** | [**[GoogleCloudDocumentaiV1beta3EvaluationConfidenceLevelMetrics]**](GoogleCloudDocumentaiV1beta3EvaluationConfidenceLevelMetrics.md) | Metrics across confidence levels with only exact matching. | [optional] 
**estimatedCalibrationError** | **Number** | The Estimated Calibration Error (ECE) of the confidence of the predicted entities. | [optional] 
**estimatedCalibrationErrorExact** | **Number** | The ECE for the predicted entities with fuzzy matching disabled, i.e., exact matching only. | [optional] 
**metricsType** | **String** | The metrics type for the label. | [optional] 



## Enum: MetricsTypeEnum


* `METRICS_TYPE_UNSPECIFIED` (value: `"METRICS_TYPE_UNSPECIFIED"`)

* `AGGREGATE` (value: `"AGGREGATE"`)




