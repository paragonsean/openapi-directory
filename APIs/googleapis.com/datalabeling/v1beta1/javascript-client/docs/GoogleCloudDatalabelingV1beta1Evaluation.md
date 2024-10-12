# DataLabelingApi.GoogleCloudDatalabelingV1beta1Evaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationType** | **String** | Output only. Type of task that the model version being evaluated performs, as defined in the evaluationJobConfig.inputConfig.annotationType field of the evaluation job that created this evaluation. | [optional] 
**config** | [**GoogleCloudDatalabelingV1beta1EvaluationConfig**](GoogleCloudDatalabelingV1beta1EvaluationConfig.md) |  | [optional] 
**createTime** | **String** | Output only. Timestamp for when this evaluation was created. | [optional] 
**evaluatedItemCount** | **String** | Output only. The number of items in the ground truth dataset that were used for this evaluation. Only populated when the evaulation is for certain AnnotationTypes. | [optional] 
**evaluationJobRunTime** | **String** | Output only. Timestamp for when the evaluation job that created this evaluation ran. | [optional] 
**evaluationMetrics** | [**GoogleCloudDatalabelingV1beta1EvaluationMetrics**](GoogleCloudDatalabelingV1beta1EvaluationMetrics.md) |  | [optional] 
**name** | **String** | Output only. Resource name of an evaluation. The name has the following format: \&quot;projects/{project_id}/datasets/{dataset_id}/evaluations/ {evaluation_id}&#39; | [optional] 



## Enum: AnnotationTypeEnum


* `ANNOTATION_TYPE_UNSPECIFIED` (value: `"ANNOTATION_TYPE_UNSPECIFIED"`)

* `IMAGE_CLASSIFICATION_ANNOTATION` (value: `"IMAGE_CLASSIFICATION_ANNOTATION"`)

* `IMAGE_BOUNDING_BOX_ANNOTATION` (value: `"IMAGE_BOUNDING_BOX_ANNOTATION"`)

* `IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION` (value: `"IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION"`)

* `IMAGE_BOUNDING_POLY_ANNOTATION` (value: `"IMAGE_BOUNDING_POLY_ANNOTATION"`)

* `IMAGE_POLYLINE_ANNOTATION` (value: `"IMAGE_POLYLINE_ANNOTATION"`)

* `IMAGE_SEGMENTATION_ANNOTATION` (value: `"IMAGE_SEGMENTATION_ANNOTATION"`)

* `VIDEO_SHOTS_CLASSIFICATION_ANNOTATION` (value: `"VIDEO_SHOTS_CLASSIFICATION_ANNOTATION"`)

* `VIDEO_OBJECT_TRACKING_ANNOTATION` (value: `"VIDEO_OBJECT_TRACKING_ANNOTATION"`)

* `VIDEO_OBJECT_DETECTION_ANNOTATION` (value: `"VIDEO_OBJECT_DETECTION_ANNOTATION"`)

* `VIDEO_EVENT_ANNOTATION` (value: `"VIDEO_EVENT_ANNOTATION"`)

* `TEXT_CLASSIFICATION_ANNOTATION` (value: `"TEXT_CLASSIFICATION_ANNOTATION"`)

* `TEXT_ENTITY_EXTRACTION_ANNOTATION` (value: `"TEXT_ENTITY_EXTRACTION_ANNOTATION"`)

* `GENERAL_CLASSIFICATION_ANNOTATION` (value: `"GENERAL_CLASSIFICATION_ANNOTATION"`)




