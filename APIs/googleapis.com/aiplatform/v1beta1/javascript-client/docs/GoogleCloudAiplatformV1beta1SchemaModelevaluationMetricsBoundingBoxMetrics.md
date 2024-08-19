# VertexAiApi.GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidenceMetrics** | [**[GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetricsConfidenceMetrics]**](GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetricsConfidenceMetrics.md) | Metrics for each label-match confidence_threshold from 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99. Precision-recall curve is derived from them. | [optional] 
**iouThreshold** | **Number** | The intersection-over-union threshold value used to compute this metrics entry. | [optional] 
**meanAveragePrecision** | **Number** | The mean average precision, most often close to &#x60;auPrc&#x60;. | [optional] 


