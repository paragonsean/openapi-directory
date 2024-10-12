

# VideoObjectTrackingEvaluationMetrics

Model evaluation metrics for video object tracking problems. Evaluates prediction quality of both labeled bounding boxes and labeled tracks (i.e. series of bounding boxes sharing same label and instance ID).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingBoxMeanAveragePrecision** | **Float** | Output only. The single metric for bounding boxes evaluation: the mean_average_precision averaged over all bounding_box_metrics_entries. |  [optional] |
|**boundingBoxMetricsEntries** | [**List&lt;BoundingBoxMetricsEntry&gt;**](BoundingBoxMetricsEntry.md) | Output only. The bounding boxes match metrics for each Intersection-over-union threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each label confidence threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair. |  [optional] |
|**evaluatedBoundingBoxCount** | **Integer** | Output only. The total number of bounding boxes (i.e. summed over all frames) the ground truth used to create this evaluation had. |  [optional] |
|**evaluatedFrameCount** | **Integer** | Output only. The number of video frames used to create this evaluation. |  [optional] |



