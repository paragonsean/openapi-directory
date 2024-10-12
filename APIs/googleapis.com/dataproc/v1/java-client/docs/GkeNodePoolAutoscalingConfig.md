

# GkeNodePoolAutoscalingConfig

GkeNodePoolAutoscaling contains information the cluster autoscaler needs to adjust the size of the node pool to the current cluster usage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxNodeCount** | **Integer** | The maximum number of nodes in the node pool. Must be &gt;&#x3D; min_node_count, and must be &gt; 0. Note: Quota must be sufficient to scale up the cluster. |  [optional] |
|**minNodeCount** | **Integer** | The minimum number of nodes in the node pool. Must be &gt;&#x3D; 0 and &lt;&#x3D; max_node_count. |  [optional] |



