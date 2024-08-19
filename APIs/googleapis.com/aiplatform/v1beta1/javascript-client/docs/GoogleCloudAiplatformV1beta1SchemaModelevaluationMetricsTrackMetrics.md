# VertexAiApi.GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidenceMetrics** | [**[GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetricsConfidenceMetrics]**](GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetricsConfidenceMetrics.md) | Metrics for each label-match &#x60;confidenceThreshold&#x60; from 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99. Precision-recall curve is derived from them. | [optional] 
**iouThreshold** | **Number** | The intersection-over-union threshold value between bounding boxes across frames used to compute this metric entry. | [optional] 
**meanBoundingBoxIou** | **Number** | The mean bounding box iou over all confidence thresholds. | [optional] 
**meanMismatchRate** | **Number** | The mean mismatch rate over all confidence thresholds. | [optional] 
**meanTrackingAveragePrecision** | **Number** | The mean average precision over all confidence thresholds. | [optional] 


