

# GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoObjectTrackingMetrics

Model evaluation metrics for video object tracking problems. Evaluates prediction quality of both labeled bounding boxes and labeled tracks (i.e. series of bounding boxes sharing same label and instance ID).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingBoxMeanAveragePrecision** | **Float** | The single metric for bounding boxes evaluation: the &#x60;meanAveragePrecision&#x60; averaged over all &#x60;boundingBoxMetrics&#x60;. |  [optional] |
|**boundingBoxMetrics** | [**List&lt;GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetrics&gt;**](GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetrics.md) | The bounding boxes match metrics for each intersection-over-union threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each label confidence threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair. |  [optional] |
|**evaluatedBoundingBoxCount** | **Integer** | UNIMPLEMENTED. The total number of bounding boxes (i.e. summed over all frames) the ground truth used to create this evaluation had. |  [optional] |
|**evaluatedFrameCount** | **Integer** | UNIMPLEMENTED. The number of video frames used to create this evaluation. |  [optional] |
|**evaluatedTrackCount** | **Integer** | UNIMPLEMENTED. The total number of tracks (i.e. as seen across all frames) the ground truth used to create this evaluation had. |  [optional] |
|**trackMeanAveragePrecision** | **Float** | UNIMPLEMENTED. The single metric for tracks accuracy evaluation: the &#x60;meanAveragePrecision&#x60; averaged over all &#x60;trackMetrics&#x60;. |  [optional] |
|**trackMeanBoundingBoxIou** | **Float** | UNIMPLEMENTED. The single metric for tracks bounding box iou evaluation: the &#x60;meanBoundingBoxIou&#x60; averaged over all &#x60;trackMetrics&#x60;. |  [optional] |
|**trackMeanMismatchRate** | **Float** | UNIMPLEMENTED. The single metric for tracking consistency evaluation: the &#x60;meanMismatchRate&#x60; averaged over all &#x60;trackMetrics&#x60;. |  [optional] |
|**trackMetrics** | [**List&lt;GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetrics&gt;**](GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetrics.md) | UNIMPLEMENTED. The tracks match metrics for each intersection-over-union threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each label confidence threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair. |  [optional] |



