# VertexAiApi.GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributedItems** | [**[GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotationAttributedItem]**](GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotationAttributedItem.md) | Attributed items for a given annotation, typically representing neighbors from the training sets constrained by the query type. | [optional] 
**outlierScore** | **Number** | The outlier score of this annotated item. Usually defined as the min of all distances from attributed items. | [optional] 
**outlierThreshold** | **Number** | The threshold used to determine if this annotation is an outlier or not. | [optional] 
**queryType** | **String** | The query type used for finding the attributed items. | [optional] 



## Enum: QueryTypeEnum


* `QUERY_TYPE_UNSPECIFIED` (value: `"QUERY_TYPE_UNSPECIFIED"`)

* `ALL_SIMILAR` (value: `"ALL_SIMILAR"`)

* `SAME_CLASS_SIMILAR` (value: `"SAME_CLASS_SIMILAR"`)

* `SAME_CLASS_DISSIMILAR` (value: `"SAME_CLASS_DISSIMILAR"`)




