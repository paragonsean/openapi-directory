# VertexAiApi.GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bruteForceConfig** | **Object** |  | [optional] 
**crowdingColumn** | **String** | Optional. Column of crowding. This column contains crowding attribute which is a constraint on a neighbor list produced by nearest neighbor search requiring that no more than some value k&#39; of the k neighbors returned have the same value of crowding_attribute. | [optional] 
**distanceMeasureType** | **String** | Optional. The distance measure used in nearest neighbor search. | [optional] 
**embeddingColumn** | **String** | Optional. Column of embedding. This column contains the source data to create index for vector search. embedding_column must be set when using vector search. | [optional] 
**embeddingDimension** | **Number** | Optional. The number of dimensions of the input embedding. | [optional] 
**filterColumns** | **[String]** | Optional. Columns of features that&#39;re used to filter vector search results. | [optional] 
**treeAhConfig** | [**GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfigTreeAHConfig**](GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfigTreeAHConfig.md) |  | [optional] 



## Enum: DistanceMeasureTypeEnum


* `DISTANCE_MEASURE_TYPE_UNSPECIFIED` (value: `"DISTANCE_MEASURE_TYPE_UNSPECIFIED"`)

* `SQUARED_L2_DISTANCE` (value: `"SQUARED_L2_DISTANCE"`)

* `COSINE_DISTANCE` (value: `"COSINE_DISTANCE"`)

* `DOT_PRODUCT_DISTANCE` (value: `"DOT_PRODUCT_DISTANCE"`)




