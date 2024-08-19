

# GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetricsConfidenceMetrics

Metrics for a single confidence threshold.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingBoxIou** | **Float** | Bounding box intersection-over-union precision. Measures how well the bounding boxes overlap between each other (e.g. complete overlap or just barely above iou_threshold). |  [optional] |
|**confidenceThreshold** | **Float** | The confidence threshold value used to compute the metrics. |  [optional] |
|**mismatchRate** | **Float** | Mismatch rate, which measures the tracking consistency, i.e. correctness of instance ID continuity. |  [optional] |
|**trackingPrecision** | **Float** | Tracking precision. |  [optional] |
|**trackingRecall** | **Float** | Tracking recall. |  [optional] |



