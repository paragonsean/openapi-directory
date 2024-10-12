# PineconeApi.DescribeIndexStatsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | **Number** | The number of dimensions in the vector representation | [optional] 
**indexFullness** | **Number** | The fullness of the index, regardless of whether a metadata filter expression was passed. The granularity of this metric is 10%. | [optional] 
**namespaces** | [**{String: IndexNamespaceStats}**](IndexNamespaceStats.md) |  | [optional] 
**totalVectorCount** | **Number** |  | [optional] 


