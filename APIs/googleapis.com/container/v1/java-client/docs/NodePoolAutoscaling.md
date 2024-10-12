

# NodePoolAutoscaling

NodePoolAutoscaling contains information required by cluster autoscaler to adjust the size of the node pool to the current cluster usage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoprovisioned** | **Boolean** | Can this node pool be deleted automatically. |  [optional] |
|**enabled** | **Boolean** | Is autoscaling enabled for this node pool. |  [optional] |
|**locationPolicy** | [**LocationPolicyEnum**](#LocationPolicyEnum) | Location policy used when scaling up a nodepool. |  [optional] |
|**maxNodeCount** | **Integer** | Maximum number of nodes for one location in the NodePool. Must be &gt;&#x3D; min_node_count. There has to be enough quota to scale up the cluster. |  [optional] |
|**minNodeCount** | **Integer** | Minimum number of nodes for one location in the NodePool. Must be &gt;&#x3D; 1 and &lt;&#x3D; max_node_count. |  [optional] |
|**totalMaxNodeCount** | **Integer** | Maximum number of nodes in the node pool. Must be greater than total_min_node_count. There has to be enough quota to scale up the cluster. The total_*_node_count fields are mutually exclusive with the *_node_count fields. |  [optional] |
|**totalMinNodeCount** | **Integer** | Minimum number of nodes in the node pool. Must be greater than 1 less than total_max_node_count. The total_*_node_count fields are mutually exclusive with the *_node_count fields. |  [optional] |



## Enum: LocationPolicyEnum

| Name | Value |
|---- | -----|
| LOCATION_POLICY_UNSPECIFIED | &quot;LOCATION_POLICY_UNSPECIFIED&quot; |
| BALANCED | &quot;BALANCED&quot; |
| ANY | &quot;ANY&quot; |



