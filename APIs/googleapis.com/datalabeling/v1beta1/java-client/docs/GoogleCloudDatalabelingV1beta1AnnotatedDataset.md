

# GoogleCloudDatalabelingV1beta1AnnotatedDataset

AnnotatedDataset is a set holding annotations for data in a Dataset. Each labeling task will generate an AnnotatedDataset under the Dataset that the task is requested for.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationSource** | [**AnnotationSourceEnum**](#AnnotationSourceEnum) | Output only. Source of the annotation. |  [optional] |
|**annotationType** | [**AnnotationTypeEnum**](#AnnotationTypeEnum) | Output only. Type of the annotation. It is specified when starting labeling task. |  [optional] |
|**blockingResources** | **List&lt;String&gt;** | Output only. The names of any related resources that are blocking changes to the annotated dataset. |  [optional] |
|**completedExampleCount** | **String** | Output only. Number of examples that have annotation in the annotated dataset. |  [optional] |
|**createTime** | **String** | Output only. Time the AnnotatedDataset was created. |  [optional] |
|**description** | **String** | Output only. The description of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 10000 characters. |  [optional] |
|**displayName** | **String** | Output only. The display name of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 64 characters. |  [optional] |
|**exampleCount** | **String** | Output only. Number of examples in the annotated dataset. |  [optional] |
|**labelStats** | [**GoogleCloudDatalabelingV1beta1LabelStats**](GoogleCloudDatalabelingV1beta1LabelStats.md) |  |  [optional] |
|**metadata** | [**GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadata**](GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadata.md) |  |  [optional] |
|**name** | **String** | Output only. AnnotatedDataset resource name in format of: projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/ {annotated_dataset_id} |  [optional] |



## Enum: AnnotationSourceEnum

| Name | Value |
|---- | -----|
| ANNOTATION_SOURCE_UNSPECIFIED | &quot;ANNOTATION_SOURCE_UNSPECIFIED&quot; |
| OPERATOR | &quot;OPERATOR&quot; |



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



