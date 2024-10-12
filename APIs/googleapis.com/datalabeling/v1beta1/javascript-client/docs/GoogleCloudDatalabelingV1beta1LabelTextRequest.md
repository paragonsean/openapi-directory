# DataLabelingApi.GoogleCloudDatalabelingV1beta1LabelTextRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basicConfig** | [**GoogleCloudDatalabelingV1beta1HumanAnnotationConfig**](GoogleCloudDatalabelingV1beta1HumanAnnotationConfig.md) |  | [optional] 
**feature** | **String** | Required. The type of text labeling task. | [optional] 
**textClassificationConfig** | [**GoogleCloudDatalabelingV1beta1TextClassificationConfig**](GoogleCloudDatalabelingV1beta1TextClassificationConfig.md) |  | [optional] 
**textEntityExtractionConfig** | [**GoogleCloudDatalabelingV1beta1TextEntityExtractionConfig**](GoogleCloudDatalabelingV1beta1TextEntityExtractionConfig.md) |  | [optional] 



## Enum: FeatureEnum


* `FEATURE_UNSPECIFIED` (value: `"FEATURE_UNSPECIFIED"`)

* `TEXT_CLASSIFICATION` (value: `"TEXT_CLASSIFICATION"`)

* `TEXT_ENTITY_EXTRACTION` (value: `"TEXT_ENTITY_EXTRACTION"`)




