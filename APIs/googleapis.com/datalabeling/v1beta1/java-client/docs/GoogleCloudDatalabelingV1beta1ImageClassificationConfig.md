

# GoogleCloudDatalabelingV1beta1ImageClassificationConfig

Config for image classification human labeling task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowMultiLabel** | **Boolean** | Optional. If allow_multi_label is true, contributors are able to choose multiple labels for one image. |  [optional] |
|**annotationSpecSet** | **String** | Required. Annotation spec set resource name. |  [optional] |
|**answerAggregationType** | [**AnswerAggregationTypeEnum**](#AnswerAggregationTypeEnum) | Optional. The type of how to aggregate answers. |  [optional] |



## Enum: AnswerAggregationTypeEnum

| Name | Value |
|---- | -----|
| STRING_AGGREGATION_TYPE_UNSPECIFIED | &quot;STRING_AGGREGATION_TYPE_UNSPECIFIED&quot; |
| MAJORITY_VOTE | &quot;MAJORITY_VOTE&quot; |
| UNANIMOUS_VOTE | &quot;UNANIMOUS_VOTE&quot; |
| NO_AGGREGATION | &quot;NO_AGGREGATION&quot; |



