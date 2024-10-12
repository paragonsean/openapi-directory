

# DescribeIndexStatsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimension** | **Integer** | The number of dimensions in the vector representation |  [optional] |
|**indexFullness** | **Float** | The fullness of the index, regardless of whether a metadata filter expression was passed. The granularity of this metric is 10%. |  [optional] |
|**namespaces** | [**Map&lt;String, IndexNamespaceStats&gt;**](IndexNamespaceStats.md) |  |  [optional] |
|**totalVectorCount** | **Long** |  |  [optional] |



