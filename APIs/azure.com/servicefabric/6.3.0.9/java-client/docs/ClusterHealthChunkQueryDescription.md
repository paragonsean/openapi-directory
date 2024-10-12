

# ClusterHealthChunkQueryDescription

The cluster health chunk query description, which can specify the health policies to evaluate cluster health and very expressive filters to select which cluster entities to include in response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationFilters** | [**List&lt;ApplicationHealthStateFilter&gt;**](ApplicationHealthStateFilter.md) | Defines a list of filters that specify which applications to be included in the returned cluster health chunk. If no filters are specified, no applications are returned. All the applications are used to evaluate the cluster&#39;s aggregated health state, regardless of the input filters. The cluster health chunk query may specify multiple application filters. For example, it can specify a filter to return all applications with health state Error and another filter to always include applications of a specified application type. |  [optional] |
|**applicationHealthPolicies** | [**ApplicationHealthPolicies**](ApplicationHealthPolicies.md) |  |  [optional] |
|**clusterHealthPolicy** | [**ClusterHealthPolicy**](ClusterHealthPolicy.md) |  |  [optional] |
|**nodeFilters** | [**List&lt;NodeHealthStateFilter&gt;**](NodeHealthStateFilter.md) | Defines a list of filters that specify which nodes to be included in the returned cluster health chunk. If no filters are specified, no nodes are returned. All the nodes are used to evaluate the cluster&#39;s aggregated health state, regardless of the input filters. The cluster health chunk query may specify multiple node filters. For example, it can specify a filter to return all nodes with health state Error and another filter to always include a node identified by its NodeName. |  [optional] |



