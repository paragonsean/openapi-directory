

# GoogleCloudDatalabelingV1beta1LabelTextRequest

Request message for LabelText.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**basicConfig** | [**GoogleCloudDatalabelingV1beta1HumanAnnotationConfig**](GoogleCloudDatalabelingV1beta1HumanAnnotationConfig.md) |  |  [optional] |
|**feature** | [**FeatureEnum**](#FeatureEnum) | Required. The type of text labeling task. |  [optional] |
|**textClassificationConfig** | [**GoogleCloudDatalabelingV1beta1TextClassificationConfig**](GoogleCloudDatalabelingV1beta1TextClassificationConfig.md) |  |  [optional] |
|**textEntityExtractionConfig** | [**GoogleCloudDatalabelingV1beta1TextEntityExtractionConfig**](GoogleCloudDatalabelingV1beta1TextEntityExtractionConfig.md) |  |  [optional] |



## Enum: FeatureEnum

| Name | Value |
|---- | -----|
| FEATURE_UNSPECIFIED | &quot;FEATURE_UNSPECIFIED&quot; |
| TEXT_CLASSIFICATION | &quot;TEXT_CLASSIFICATION&quot; |
| TEXT_ENTITY_EXTRACTION | &quot;TEXT_ENTITY_EXTRACTION&quot; |



