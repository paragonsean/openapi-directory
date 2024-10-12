

# RollbackNodePoolUpgradeRequest

RollbackNodePoolUpgradeRequest rollbacks the previously Aborted or Failed NodePool upgrade. This will be an no-op if the last upgrade successfully completed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterId** | **String** | Deprecated. The name of the cluster to rollback. This field has been deprecated and replaced by the name field. |  [optional] |
|**name** | **String** | The name (project, location, cluster, node pool id) of the node poll to rollback upgrade. Specified in the format &#x60;projects/_*_/locations/_*_/clusters/_*_/nodePools/_*&#x60;. |  [optional] |
|**nodePoolId** | **String** | Deprecated. The name of the node pool to rollback. This field has been deprecated and replaced by the name field. |  [optional] |
|**projectId** | **String** | Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field. |  [optional] |
|**respectPdb** | **Boolean** | Option for rollback to ignore the PodDisruptionBudget. Default value is false. |  [optional] |
|**zone** | **String** | Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field. |  [optional] |



