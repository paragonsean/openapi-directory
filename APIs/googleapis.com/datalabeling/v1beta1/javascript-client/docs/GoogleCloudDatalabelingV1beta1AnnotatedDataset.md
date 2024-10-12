# DataLabelingApi.GoogleCloudDatalabelingV1beta1AnnotatedDataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationSource** | **String** | Output only. Source of the annotation. | [optional] 
**annotationType** | **String** | Output only. Type of the annotation. It is specified when starting labeling task. | [optional] 
**blockingResources** | **[String]** | Output only. The names of any related resources that are blocking changes to the annotated dataset. | [optional] 
**completedExampleCount** | **String** | Output only. Number of examples that have annotation in the annotated dataset. | [optional] 
**createTime** | **String** | Output only. Time the AnnotatedDataset was created. | [optional] 
**description** | **String** | Output only. The description of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 10000 characters. | [optional] 
**displayName** | **String** | Output only. The display name of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 64 characters. | [optional] 
**exampleCount** | **String** | Output only. Number of examples in the annotated dataset. | [optional] 
**labelStats** | [**GoogleCloudDatalabelingV1beta1LabelStats**](GoogleCloudDatalabelingV1beta1LabelStats.md) |  | [optional] 
**metadata** | [**GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadata**](GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadata.md) |  | [optional] 
**name** | **String** | Output only. AnnotatedDataset resource name in format of: projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/ {annotated_dataset_id} | [optional] 



## Enum: AnnotationSourceEnum


* `ANNOTATION_SOURCE_UNSPECIFIED` (value: `"ANNOTATION_SOURCE_UNSPECIFIED"`)

* `OPERATOR` (value: `"OPERATOR"`)





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




