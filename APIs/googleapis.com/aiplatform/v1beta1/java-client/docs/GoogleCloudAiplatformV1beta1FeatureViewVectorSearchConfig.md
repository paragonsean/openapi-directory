

# GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfig

Deprecated. Use IndexConfig instead.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bruteForceConfig** | **Object** |  |  [optional] |
|**crowdingColumn** | **String** | Optional. Column of crowding. This column contains crowding attribute which is a constraint on a neighbor list produced by nearest neighbor search requiring that no more than some value k&#39; of the k neighbors returned have the same value of crowding_attribute. |  [optional] |
|**distanceMeasureType** | [**DistanceMeasureTypeEnum**](#DistanceMeasureTypeEnum) | Optional. The distance measure used in nearest neighbor search. |  [optional] |
|**embeddingColumn** | **String** | Optional. Column of embedding. This column contains the source data to create index for vector search. embedding_column must be set when using vector search. |  [optional] |
|**embeddingDimension** | **Integer** | Optional. The number of dimensions of the input embedding. |  [optional] |
|**filterColumns** | **List&lt;String&gt;** | Optional. Columns of features that&#39;re used to filter vector search results. |  [optional] |
|**treeAhConfig** | [**GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfigTreeAHConfig**](GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfigTreeAHConfig.md) |  |  [optional] |



## Enum: DistanceMeasureTypeEnum

| Name | Value |
|---- | -----|
| DISTANCE_MEASURE_TYPE_UNSPECIFIED | &quot;DISTANCE_MEASURE_TYPE_UNSPECIFIED&quot; |
| SQUARED_L2_DISTANCE | &quot;SQUARED_L2_DISTANCE&quot; |
| COSINE_DISTANCE | &quot;COSINE_DISTANCE&quot; |
| DOT_PRODUCT_DISTANCE | &quot;DOT_PRODUCT_DISTANCE&quot; |



