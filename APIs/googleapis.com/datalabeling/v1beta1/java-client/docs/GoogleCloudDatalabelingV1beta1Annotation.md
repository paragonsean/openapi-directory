

# GoogleCloudDatalabelingV1beta1Annotation

Annotation for Example. Each example may have one or more annotations. For example in image classification problem, each image might have one or more labels. We call labels binded with this image an Annotation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationMetadata** | [**GoogleCloudDatalabelingV1beta1AnnotationMetadata**](GoogleCloudDatalabelingV1beta1AnnotationMetadata.md) |  |  [optional] |
|**annotationSentiment** | [**AnnotationSentimentEnum**](#AnnotationSentimentEnum) | Output only. Sentiment for this annotation. |  [optional] |
|**annotationSource** | [**AnnotationSourceEnum**](#AnnotationSourceEnum) | Output only. The source of the annotation. |  [optional] |
|**annotationValue** | [**GoogleCloudDatalabelingV1beta1AnnotationValue**](GoogleCloudDatalabelingV1beta1AnnotationValue.md) |  |  [optional] |
|**name** | **String** | Output only. Unique name of this annotation, format is: projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/{annotated_dataset}/examples/{example_id}/annotations/{annotation_id} |  [optional] |



## Enum: AnnotationSentimentEnum

| Name | Value |
|---- | -----|
| ANNOTATION_SENTIMENT_UNSPECIFIED | &quot;ANNOTATION_SENTIMENT_UNSPECIFIED&quot; |
| NEGATIVE | &quot;NEGATIVE&quot; |
| POSITIVE | &quot;POSITIVE&quot; |



## Enum: AnnotationSourceEnum

| Name | Value |
|---- | -----|
| ANNOTATION_SOURCE_UNSPECIFIED | &quot;ANNOTATION_SOURCE_UNSPECIFIED&quot; |
| OPERATOR | &quot;OPERATOR&quot; |



