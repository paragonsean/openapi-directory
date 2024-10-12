

# GoogleCloudDatalabelingV1beta1Evaluation

Describes an evaluation between a machine learning model's predictions and ground truth labels. Created when an EvaluationJob runs successfully.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationType** | [**AnnotationTypeEnum**](#AnnotationTypeEnum) | Output only. Type of task that the model version being evaluated performs, as defined in the evaluationJobConfig.inputConfig.annotationType field of the evaluation job that created this evaluation. |  [optional] |
|**config** | [**GoogleCloudDatalabelingV1beta1EvaluationConfig**](GoogleCloudDatalabelingV1beta1EvaluationConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. Timestamp for when this evaluation was created. |  [optional] |
|**evaluatedItemCount** | **String** | Output only. The number of items in the ground truth dataset that were used for this evaluation. Only populated when the evaulation is for certain AnnotationTypes. |  [optional] |
|**evaluationJobRunTime** | **String** | Output only. Timestamp for when the evaluation job that created this evaluation ran. |  [optional] |
|**evaluationMetrics** | [**GoogleCloudDatalabelingV1beta1EvaluationMetrics**](GoogleCloudDatalabelingV1beta1EvaluationMetrics.md) |  |  [optional] |
|**name** | **String** | Output only. Resource name of an evaluation. The name has the following format: \&quot;projects/{project_id}/datasets/{dataset_id}/evaluations/ {evaluation_id}&#39; |  [optional] |



## Enum: AnnotationTypeEnum

| Name | Value |
|---- | -----|
| ANNOTATION_TYPE_UNSPECIFIED | &quot;ANNOTATION_TYPE_UNSPECIFIED&quot; |
| IMAGE_CLASSIFICATION_ANNOTATION | &quot;IMAGE_CLASSIFICATION_ANNOTATION&quot; |
| IMAGE_BOUNDING_BOX_ANNOTATION | &quot;IMAGE_BOUNDING_BOX_ANNOTATION&quot; |
| IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION | &quot;IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION&quot; |
| IMAGE_BOUNDING_POLY_ANNOTATION | &quot;IMAGE_BOUNDING_POLY_ANNOTATION&quot; |
| IMAGE_POLYLINE_ANNOTATION | &quot;IMAGE_POLYLINE_ANNOTATION&quot; |
| IMAGE_SEGMENTATION_ANNOTATION | &quot;IMAGE_SEGMENTATION_ANNOTATION&quot; |
| VIDEO_SHOTS_CLASSIFICATION_ANNOTATION | &quot;VIDEO_SHOTS_CLASSIFICATION_ANNOTATION&quot; |
| VIDEO_OBJECT_TRACKING_ANNOTATION | &quot;VIDEO_OBJECT_TRACKING_ANNOTATION&quot; |
| VIDEO_OBJECT_DETECTION_ANNOTATION | &quot;VIDEO_OBJECT_DETECTION_ANNOTATION&quot; |
| VIDEO_EVENT_ANNOTATION | &quot;VIDEO_EVENT_ANNOTATION&quot; |
| TEXT_CLASSIFICATION_ANNOTATION | &quot;TEXT_CLASSIFICATION_ANNOTATION&quot; |
| TEXT_ENTITY_EXTRACTION_ANNOTATION | &quot;TEXT_ENTITY_EXTRACTION_ANNOTATION&quot; |
| GENERAL_CLASSIFICATION_ANNOTATION | &quot;GENERAL_CLASSIFICATION_ANNOTATION&quot; |



