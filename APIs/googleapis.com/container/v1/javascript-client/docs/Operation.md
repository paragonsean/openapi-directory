# KubernetesEngineApi.Operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterConditions** | [**[StatusCondition]**](StatusCondition.md) | Which conditions caused the current cluster state. Deprecated. Use field error instead. | [optional] 
**detail** | **String** | Detailed operation progress, if available. | [optional] 
**endTime** | **String** | [Output only] The time the operation completed, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**location** | **String** | [Output only] The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) or [region](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) in which the cluster resides. | [optional] 
**name** | **String** | The server-assigned ID for the operation. | [optional] 
**nodepoolConditions** | [**[StatusCondition]**](StatusCondition.md) | Which conditions caused the current node pool state. Deprecated. Use field error instead. | [optional] 
**operationType** | **String** | The operation type. | [optional] 
**progress** | [**OperationProgress**](OperationProgress.md) |  | [optional] 
**selfLink** | **String** | Server-defined URI for the operation. Example: &#x60;https://container.googleapis.com/v1alpha1/projects/123/locations/us-central1/operations/operation-123&#x60;. | [optional] 
**startTime** | **String** | [Output only] The time the operation started, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. | [optional] 
**status** | **String** | The current status of the operation. | [optional] 
**statusMessage** | **String** | Output only. If an error has occurred, a textual description of the error. Deprecated. Use the field error instead. | [optional] [readonly] 
**targetLink** | **String** | Server-defined URI for the target of the operation. The format of this is a URI to the resource being modified (such as a cluster, node pool, or node). For node pool repairs, there may be multiple nodes being repaired, but only one will be the target. Examples: - ## &#x60;https://container.googleapis.com/v1/projects/123/locations/us-central1/clusters/my-cluster&#x60; ## &#x60;https://container.googleapis.com/v1/projects/123/zones/us-central1-c/clusters/my-cluster/nodePools/my-np&#x60; &#x60;https://container.googleapis.com/v1/projects/123/zones/us-central1-c/clusters/my-cluster/nodePools/my-np/node/my-node&#x60; | [optional] 
**zone** | **String** | The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the operation is taking place. This field is deprecated, use location instead. | [optional] 



## Enum: OperationTypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `CREATE_CLUSTER` (value: `"CREATE_CLUSTER"`)

* `DELETE_CLUSTER` (value: `"DELETE_CLUSTER"`)

* `UPGRADE_MASTER` (value: `"UPGRADE_MASTER"`)

* `UPGRADE_NODES` (value: `"UPGRADE_NODES"`)

* `REPAIR_CLUSTER` (value: `"REPAIR_CLUSTER"`)

* `UPDATE_CLUSTER` (value: `"UPDATE_CLUSTER"`)

* `CREATE_NODE_POOL` (value: `"CREATE_NODE_POOL"`)

* `DELETE_NODE_POOL` (value: `"DELETE_NODE_POOL"`)

* `SET_NODE_POOL_MANAGEMENT` (value: `"SET_NODE_POOL_MANAGEMENT"`)

* `AUTO_REPAIR_NODES` (value: `"AUTO_REPAIR_NODES"`)

* `AUTO_UPGRADE_NODES` (value: `"AUTO_UPGRADE_NODES"`)

* `SET_LABELS` (value: `"SET_LABELS"`)

* `SET_MASTER_AUTH` (value: `"SET_MASTER_AUTH"`)

* `SET_NODE_POOL_SIZE` (value: `"SET_NODE_POOL_SIZE"`)

* `SET_NETWORK_POLICY` (value: `"SET_NETWORK_POLICY"`)

* `SET_MAINTENANCE_POLICY` (value: `"SET_MAINTENANCE_POLICY"`)

* `RESIZE_CLUSTER` (value: `"RESIZE_CLUSTER"`)

* `FLEET_FEATURE_UPGRADE` (value: `"FLEET_FEATURE_UPGRADE"`)





## Enum: StatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `DONE` (value: `"DONE"`)

* `ABORTING` (value: `"ABORTING"`)




