# PineconeApi.IndexDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | **Number** | The number of dimensions in the vector representation | 
**metadataConfig** | [**IndexMetadataConfig**](IndexMetadataConfig.md) |  | [optional] 
**metric** | [**IndexMetric**](IndexMetric.md) |  | [optional] 
**name** | **String** | The unique name of an index. | 
**podType** | [**PodType**](PodType.md) |  | [optional] 
**pods** | **Number** | The number of pods for the index to use,including replicas. | [optional] [default to 1]
**replicas** | **Number** | The number of replicas. Replicas duplicate your index. They provide higher availability and throughput. | [optional] [default to 1]
**sourceCollection** | **String** | The unique name of a collection. | [optional] 


