# DataLabelingApi.GoogleCloudDatalabelingV1beta1ImageClassificationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowMultiLabel** | **Boolean** | Optional. If allow_multi_label is true, contributors are able to choose multiple labels for one image. | [optional] 
**annotationSpecSet** | **String** | Required. Annotation spec set resource name. | [optional] 
**answerAggregationType** | **String** | Optional. The type of how to aggregate answers. | [optional] 



## Enum: AnswerAggregationTypeEnum


* `STRING_AGGREGATION_TYPE_UNSPECIFIED` (value: `"STRING_AGGREGATION_TYPE_UNSPECIFIED"`)

* `MAJORITY_VOTE` (value: `"MAJORITY_VOTE"`)

* `UNANIMOUS_VOTE` (value: `"UNANIMOUS_VOTE"`)

* `NO_AGGREGATION` (value: `"NO_AGGREGATION"`)




