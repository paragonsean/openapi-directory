# KubernetesEngineApi.NodePoolAutoscaling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoprovisioned** | **Boolean** | Can this node pool be deleted automatically. | [optional] 
**enabled** | **Boolean** | Is autoscaling enabled for this node pool. | [optional] 
**locationPolicy** | **String** | Location policy used when scaling up a nodepool. | [optional] 
**maxNodeCount** | **Number** | Maximum number of nodes for one location in the NodePool. Must be &gt;&#x3D; min_node_count. There has to be enough quota to scale up the cluster. | [optional] 
**minNodeCount** | **Number** | Minimum number of nodes for one location in the NodePool. Must be &gt;&#x3D; 1 and &lt;&#x3D; max_node_count. | [optional] 
**totalMaxNodeCount** | **Number** | Maximum number of nodes in the node pool. Must be greater than total_min_node_count. There has to be enough quota to scale up the cluster. The total_*_node_count fields are mutually exclusive with the *_node_count fields. | [optional] 
**totalMinNodeCount** | **Number** | Minimum number of nodes in the node pool. Must be greater than 1 less than total_max_node_count. The total_*_node_count fields are mutually exclusive with the *_node_count fields. | [optional] 



## Enum: LocationPolicyEnum


* `LOCATION_POLICY_UNSPECIFIED` (value: `"LOCATION_POLICY_UNSPECIFIED"`)

* `BALANCED` (value: `"BALANCED"`)

* `ANY` (value: `"ANY"`)




