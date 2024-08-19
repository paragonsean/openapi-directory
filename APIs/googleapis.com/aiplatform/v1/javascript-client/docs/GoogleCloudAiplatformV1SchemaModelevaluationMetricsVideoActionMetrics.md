# VertexAiApi.GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoActionMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidenceMetrics** | [**[GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoActionMetricsConfidenceMetrics]**](GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoActionMetricsConfidenceMetrics.md) | Metrics for each label-match confidence_threshold from 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99. | [optional] 
**meanAveragePrecision** | **Number** | The mean average precision. | [optional] 
**precisionWindowLength** | **String** | This VideoActionMetrics is calculated based on this prediction window length. If the predicted action&#39;s timestamp is inside the time window whose center is the ground truth action&#39;s timestamp with this specific length, the prediction result is treated as a true positive. | [optional] 


