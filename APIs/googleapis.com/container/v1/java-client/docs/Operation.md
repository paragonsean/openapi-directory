

# Operation

This operation resource represents operations that may have happened or are happening on the cluster. All fields are output only.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterConditions** | [**List&lt;StatusCondition&gt;**](StatusCondition.md) | Which conditions caused the current cluster state. Deprecated. Use field error instead. |  [optional] |
|**detail** | **String** | Detailed operation progress, if available. |  [optional] |
|**endTime** | **String** | [Output only] The time the operation completed, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |  [optional] |
|**error** | [**Status**](Status.md) |  |  [optional] |
|**location** | **String** | [Output only] The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) or [region](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) in which the cluster resides. |  [optional] |
|**name** | **String** | The server-assigned ID for the operation. |  [optional] |
|**nodepoolConditions** | [**List&lt;StatusCondition&gt;**](StatusCondition.md) | Which conditions caused the current node pool state. Deprecated. Use field error instead. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | The operation type. |  [optional] |
|**progress** | [**OperationProgress**](OperationProgress.md) |  |  [optional] |
|**selfLink** | **String** | Server-defined URI for the operation. Example: &#x60;https://container.googleapis.com/v1alpha1/projects/123/locations/us-central1/operations/operation-123&#x60;. |  [optional] |
|**startTime** | **String** | [Output only] The time the operation started, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the operation. |  [optional] |
|**statusMessage** | **String** | Output only. If an error has occurred, a textual description of the error. Deprecated. Use the field error instead. |  [optional] [readonly] |
|**targetLink** | **String** | Server-defined URI for the target of the operation. The format of this is a URI to the resource being modified (such as a cluster, node pool, or node). For node pool repairs, there may be multiple nodes being repaired, but only one will be the target. Examples: - ## &#x60;https://container.googleapis.com/v1/projects/123/locations/us-central1/clusters/my-cluster&#x60; ## &#x60;https://container.googleapis.com/v1/projects/123/zones/us-central1-c/clusters/my-cluster/nodePools/my-np&#x60; &#x60;https://container.googleapis.com/v1/projects/123/zones/us-central1-c/clusters/my-cluster/nodePools/my-np/node/my-node&#x60; |  [optional] |
|**zone** | **String** | The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the operation is taking place. This field is deprecated, use location instead. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| CREATE_CLUSTER | &quot;CREATE_CLUSTER&quot; |
| DELETE_CLUSTER | &quot;DELETE_CLUSTER&quot; |
| UPGRADE_MASTER | &quot;UPGRADE_MASTER&quot; |
| UPGRADE_NODES | &quot;UPGRADE_NODES&quot; |
| REPAIR_CLUSTER | &quot;REPAIR_CLUSTER&quot; |
| UPDATE_CLUSTER | &quot;UPDATE_CLUSTER&quot; |
| CREATE_NODE_POOL | &quot;CREATE_NODE_POOL&quot; |
| DELETE_NODE_POOL | &quot;DELETE_NODE_POOL&quot; |
| SET_NODE_POOL_MANAGEMENT | &quot;SET_NODE_POOL_MANAGEMENT&quot; |
| AUTO_REPAIR_NODES | &quot;AUTO_REPAIR_NODES&quot; |
| AUTO_UPGRADE_NODES | &quot;AUTO_UPGRADE_NODES&quot; |
| SET_LABELS | &quot;SET_LABELS&quot; |
| SET_MASTER_AUTH | &quot;SET_MASTER_AUTH&quot; |
| SET_NODE_POOL_SIZE | &quot;SET_NODE_POOL_SIZE&quot; |
| SET_NETWORK_POLICY | &quot;SET_NETWORK_POLICY&quot; |
| SET_MAINTENANCE_POLICY | &quot;SET_MAINTENANCE_POLICY&quot; |
| RESIZE_CLUSTER | &quot;RESIZE_CLUSTER&quot; |
| FLEET_FEATURE_UPGRADE | &quot;FLEET_FEATURE_UPGRADE&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| DONE | &quot;DONE&quot; |
| ABORTING | &quot;ABORTING&quot; |



