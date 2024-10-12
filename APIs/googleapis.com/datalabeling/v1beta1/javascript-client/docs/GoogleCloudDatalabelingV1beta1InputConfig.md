# DataLabelingApi.GoogleCloudDatalabelingV1beta1InputConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationType** | **String** | Optional. The type of annotation to be performed on this data. You must specify this field if you are using this InputConfig in an EvaluationJob. | [optional] 
**bigquerySource** | [**GoogleCloudDatalabelingV1beta1BigQuerySource**](GoogleCloudDatalabelingV1beta1BigQuerySource.md) |  | [optional] 
**classificationMetadata** | [**GoogleCloudDatalabelingV1beta1ClassificationMetadata**](GoogleCloudDatalabelingV1beta1ClassificationMetadata.md) |  | [optional] 
**dataType** | **String** | Required. Data type must be specifed when user tries to import data. | [optional] 
**gcsSource** | [**GoogleCloudDatalabelingV1beta1GcsSource**](GoogleCloudDatalabelingV1beta1GcsSource.md) |  | [optional] 
**textMetadata** | [**GoogleCloudDatalabelingV1beta1TextMetadata**](GoogleCloudDatalabelingV1beta1TextMetadata.md) |  | [optional] 



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





## Enum: DataTypeEnum


* `DATA_TYPE_UNSPECIFIED` (value: `"DATA_TYPE_UNSPECIFIED"`)

* `IMAGE` (value: `"IMAGE"`)

* `VIDEO` (value: `"VIDEO"`)

* `TEXT` (value: `"TEXT"`)

* `GENERAL_DATA` (value: `"GENERAL_DATA"`)




