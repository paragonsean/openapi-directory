# DataLabelingApi.GoogleCloudDatalabelingV1beta1Annotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationMetadata** | [**GoogleCloudDatalabelingV1beta1AnnotationMetadata**](GoogleCloudDatalabelingV1beta1AnnotationMetadata.md) |  | [optional] 
**annotationSentiment** | **String** | Output only. Sentiment for this annotation. | [optional] 
**annotationSource** | **String** | Output only. The source of the annotation. | [optional] 
**annotationValue** | [**GoogleCloudDatalabelingV1beta1AnnotationValue**](GoogleCloudDatalabelingV1beta1AnnotationValue.md) |  | [optional] 
**name** | **String** | Output only. Unique name of this annotation, format is: projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/{annotated_dataset}/examples/{example_id}/annotations/{annotation_id} | [optional] 



## Enum: AnnotationSentimentEnum


* `ANNOTATION_SENTIMENT_UNSPECIFIED` (value: `"ANNOTATION_SENTIMENT_UNSPECIFIED"`)

* `NEGATIVE` (value: `"NEGATIVE"`)

* `POSITIVE` (value: `"POSITIVE"`)





## Enum: AnnotationSourceEnum


* `ANNOTATION_SOURCE_UNSPECIFIED` (value: `"ANNOTATION_SOURCE_UNSPECIFIED"`)

* `OPERATOR` (value: `"OPERATOR"`)




