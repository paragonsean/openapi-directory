

# IndexDefinition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimension** | **Integer** | The number of dimensions in the vector representation |  |
|**metadataConfig** | [**IndexMetadataConfig**](IndexMetadataConfig.md) |  |  [optional] |
|**metric** | **IndexMetric** |  |  [optional] |
|**name** | **String** | The unique name of an index. |  |
|**podType** | **PodType** |  |  [optional] |
|**pods** | **Integer** | The number of pods for the index to use,including replicas. |  [optional] |
|**replicas** | **Integer** | The number of replicas. Replicas duplicate your index. They provide higher availability and throughput. |  [optional] |
|**sourceCollection** | **String** | The unique name of a collection. |  [optional] |



