

# GoogleCloudDatalabelingV1beta1InputConfig

The configuration of input data, including data type, location, etc.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationType** | [**AnnotationTypeEnum**](#AnnotationTypeEnum) | Optional. The type of annotation to be performed on this data. You must specify this field if you are using this InputConfig in an EvaluationJob. |  [optional] |
|**bigquerySource** | [**GoogleCloudDatalabelingV1beta1BigQuerySource**](GoogleCloudDatalabelingV1beta1BigQuerySource.md) |  |  [optional] |
|**classificationMetadata** | [**GoogleCloudDatalabelingV1beta1ClassificationMetadata**](GoogleCloudDatalabelingV1beta1ClassificationMetadata.md) |  |  [optional] |
|**dataType** | [**DataTypeEnum**](#DataTypeEnum) | Required. Data type must be specifed when user tries to import data. |  [optional] |
|**gcsSource** | [**GoogleCloudDatalabelingV1beta1GcsSource**](GoogleCloudDatalabelingV1beta1GcsSource.md) |  |  [optional] |
|**textMetadata** | [**GoogleCloudDatalabelingV1beta1TextMetadata**](GoogleCloudDatalabelingV1beta1TextMetadata.md) |  |  [optional] |



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



## Enum: DataTypeEnum

| Name | Value |
|---- | -----|
| DATA_TYPE_UNSPECIFIED | &quot;DATA_TYPE_UNSPECIFIED&quot; |
| IMAGE | &quot;IMAGE&quot; |
| VIDEO | &quot;VIDEO&quot; |
| TEXT | &quot;TEXT&quot; |
| GENERAL_DATA | &quot;GENERAL_DATA&quot; |



