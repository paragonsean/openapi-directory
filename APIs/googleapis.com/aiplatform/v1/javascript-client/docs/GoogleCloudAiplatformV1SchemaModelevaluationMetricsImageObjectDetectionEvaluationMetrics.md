# VertexAiApi.GoogleCloudAiplatformV1SchemaModelevaluationMetricsImageObjectDetectionEvaluationMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundingBoxMeanAveragePrecision** | **Number** | The single metric for bounding boxes evaluation: the &#x60;meanAveragePrecision&#x60; averaged over all &#x60;boundingBoxMetricsEntries&#x60;. | [optional] 
**boundingBoxMetrics** | [**[GoogleCloudAiplatformV1SchemaModelevaluationMetricsBoundingBoxMetrics]**](GoogleCloudAiplatformV1SchemaModelevaluationMetricsBoundingBoxMetrics.md) | The bounding boxes match metrics for each intersection-over-union threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each label confidence threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair. | [optional] 
**evaluatedBoundingBoxCount** | **Number** | The total number of bounding boxes (i.e. summed over all images) the ground truth used to create this evaluation had. | [optional] 


