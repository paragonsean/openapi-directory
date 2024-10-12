

# ImageObjectDetectionEvaluationMetrics

Model evaluation metrics for image object detection problems. Evaluates prediction quality of labeled bounding boxes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingBoxMeanAveragePrecision** | **Float** | Output only. The single metric for bounding boxes evaluation: the mean_average_precision averaged over all bounding_box_metrics_entries. |  [optional] |
|**boundingBoxMetricsEntries** | [**List&lt;BoundingBoxMetricsEntry&gt;**](BoundingBoxMetricsEntry.md) | Output only. The bounding boxes match metrics for each Intersection-over-union threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each label confidence threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair. |  [optional] |
|**evaluatedBoundingBoxCount** | **Integer** | Output only. The total number of bounding boxes (i.e. summed over all images) the ground truth used to create this evaluation had. |  [optional] |



