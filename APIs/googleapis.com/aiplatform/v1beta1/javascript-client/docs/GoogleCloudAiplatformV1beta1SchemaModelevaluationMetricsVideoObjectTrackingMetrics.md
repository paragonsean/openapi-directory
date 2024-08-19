# VertexAiApi.GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoObjectTrackingMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundingBoxMeanAveragePrecision** | **Number** | The single metric for bounding boxes evaluation: the &#x60;meanAveragePrecision&#x60; averaged over all &#x60;boundingBoxMetrics&#x60;. | [optional] 
**boundingBoxMetrics** | [**[GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetrics]**](GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetrics.md) | The bounding boxes match metrics for each intersection-over-union threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each label confidence threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair. | [optional] 
**evaluatedBoundingBoxCount** | **Number** | UNIMPLEMENTED. The total number of bounding boxes (i.e. summed over all frames) the ground truth used to create this evaluation had. | [optional] 
**evaluatedFrameCount** | **Number** | UNIMPLEMENTED. The number of video frames used to create this evaluation. | [optional] 
**evaluatedTrackCount** | **Number** | UNIMPLEMENTED. The total number of tracks (i.e. as seen across all frames) the ground truth used to create this evaluation had. | [optional] 
**trackMeanAveragePrecision** | **Number** | UNIMPLEMENTED. The single metric for tracks accuracy evaluation: the &#x60;meanAveragePrecision&#x60; averaged over all &#x60;trackMetrics&#x60;. | [optional] 
**trackMeanBoundingBoxIou** | **Number** | UNIMPLEMENTED. The single metric for tracks bounding box iou evaluation: the &#x60;meanBoundingBoxIou&#x60; averaged over all &#x60;trackMetrics&#x60;. | [optional] 
**trackMeanMismatchRate** | **Number** | UNIMPLEMENTED. The single metric for tracking consistency evaluation: the &#x60;meanMismatchRate&#x60; averaged over all &#x60;trackMetrics&#x60;. | [optional] 
**trackMetrics** | [**[GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetrics]**](GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetrics.md) | UNIMPLEMENTED. The tracks match metrics for each intersection-over-union threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each label confidence threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair. | [optional] 


