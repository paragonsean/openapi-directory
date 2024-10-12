

# ClassificationEvaluationMetrics

Model evaluation metrics for classification problems. Note: For Video Classification this metrics only describe quality of the Video Classification predictions of \"segment_classification\" type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationSpecId** | **List&lt;String&gt;** | Output only. The annotation spec ids used for this evaluation. |  [optional] |
|**auPrc** | **Float** | Output only. The Area Under Precision-Recall Curve metric. Micro-averaged for the overall evaluation. |  [optional] |
|**auRoc** | **Float** | Output only. The Area Under Receiver Operating Characteristic curve metric. Micro-averaged for the overall evaluation. |  [optional] |
|**baseAuPrc** | **Float** | Output only. The Area Under Precision-Recall Curve metric based on priors. Micro-averaged for the overall evaluation. Deprecated. |  [optional] |
|**confidenceMetricsEntry** | [**List&lt;ClassificationEvaluationMetricsConfidenceMetricsEntry&gt;**](ClassificationEvaluationMetricsConfidenceMetricsEntry.md) | Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold &#x3D; INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed. |  [optional] |
|**confusionMatrix** | [**ConfusionMatrix**](ConfusionMatrix.md) |  |  [optional] |
|**logLoss** | **Float** | Output only. The Log Loss metric. |  [optional] |



