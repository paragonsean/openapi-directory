

# GoogleCloudAiplatformV1ErrorAnalysisAnnotation

Model error analysis for each annotation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributedItems** | [**List&lt;GoogleCloudAiplatformV1ErrorAnalysisAnnotationAttributedItem&gt;**](GoogleCloudAiplatformV1ErrorAnalysisAnnotationAttributedItem.md) | Attributed items for a given annotation, typically representing neighbors from the training sets constrained by the query type. |  [optional] |
|**outlierScore** | **Double** | The outlier score of this annotated item. Usually defined as the min of all distances from attributed items. |  [optional] |
|**outlierThreshold** | **Double** | The threshold used to determine if this annotation is an outlier or not. |  [optional] |
|**queryType** | [**QueryTypeEnum**](#QueryTypeEnum) | The query type used for finding the attributed items. |  [optional] |



## Enum: QueryTypeEnum

| Name | Value |
|---- | -----|
| QUERY_TYPE_UNSPECIFIED | &quot;QUERY_TYPE_UNSPECIFIED&quot; |
| ALL_SIMILAR | &quot;ALL_SIMILAR&quot; |
| SAME_CLASS_SIMILAR | &quot;SAME_CLASS_SIMILAR&quot; |
| SAME_CLASS_DISSIMILAR | &quot;SAME_CLASS_DISSIMILAR&quot; |



