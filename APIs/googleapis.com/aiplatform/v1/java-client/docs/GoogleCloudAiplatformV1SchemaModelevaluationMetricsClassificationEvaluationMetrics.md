

# GoogleCloudAiplatformV1SchemaModelevaluationMetricsClassificationEvaluationMetrics

Metrics for classification evaluation results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auPrc** | **Float** | The Area Under Precision-Recall Curve metric. Micro-averaged for the overall evaluation. |  [optional] |
|**auRoc** | **Float** | The Area Under Receiver Operating Characteristic curve metric. Micro-averaged for the overall evaluation. |  [optional] |
|**confidenceMetrics** | [**List&lt;GoogleCloudAiplatformV1SchemaModelevaluationMetricsClassificationEvaluationMetricsConfidenceMetrics&gt;**](GoogleCloudAiplatformV1SchemaModelevaluationMetricsClassificationEvaluationMetricsConfidenceMetrics.md) | Metrics for each &#x60;confidenceThreshold&#x60; in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and &#x60;positionThreshold&#x60; &#x3D; INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of &#x60;positionThreshold&#x60;, but from these no aggregated metrics are computed. |  [optional] |
|**confusionMatrix** | [**GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrix**](GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrix.md) |  |  [optional] |
|**logLoss** | **Float** | The Log Loss metric. |  [optional] |



