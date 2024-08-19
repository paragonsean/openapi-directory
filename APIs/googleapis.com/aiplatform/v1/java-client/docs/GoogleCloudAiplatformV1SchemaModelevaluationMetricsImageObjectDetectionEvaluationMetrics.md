

# GoogleCloudAiplatformV1SchemaModelevaluationMetricsImageObjectDetectionEvaluationMetrics

Metrics for image object detection evaluation results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingBoxMeanAveragePrecision** | **Float** | The single metric for bounding boxes evaluation: the &#x60;meanAveragePrecision&#x60; averaged over all &#x60;boundingBoxMetricsEntries&#x60;. |  [optional] |
|**boundingBoxMetrics** | [**List&lt;GoogleCloudAiplatformV1SchemaModelevaluationMetricsBoundingBoxMetrics&gt;**](GoogleCloudAiplatformV1SchemaModelevaluationMetricsBoundingBoxMetrics.md) | The bounding boxes match metrics for each intersection-over-union threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each label confidence threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair. |  [optional] |
|**evaluatedBoundingBoxCount** | **Integer** | The total number of bounding boxes (i.e. summed over all images) the ground truth used to create this evaluation had. |  [optional] |



