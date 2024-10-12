

# SetMaintenancePolicyRequest

SetMaintenancePolicyRequest sets the maintenance policy for a cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterId** | **String** | Required. The name of the cluster to update. |  [optional] |
|**maintenancePolicy** | [**MaintenancePolicy**](MaintenancePolicy.md) |  |  [optional] |
|**name** | **String** | The name (project, location, cluster name) of the cluster to set maintenance policy. Specified in the format &#x60;projects/_*_/locations/_*_/clusters/_*&#x60;. |  [optional] |
|**projectId** | **String** | Required. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). |  [optional] |
|**zone** | **String** | Required. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. |  [optional] |



