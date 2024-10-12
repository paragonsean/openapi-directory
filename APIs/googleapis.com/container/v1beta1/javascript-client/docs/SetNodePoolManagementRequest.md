# KubernetesEngineApi.SetNodePoolManagementRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterId** | **String** | Required. Deprecated. The name of the cluster to update. This field has been deprecated and replaced by the name field. | [optional] 
**management** | [**NodeManagement**](NodeManagement.md) |  | [optional] 
**name** | **String** | The name (project, location, cluster, node pool id) of the node pool to set management properties. Specified in the format &#x60;projects/_*_/locations/_*_/clusters/_*_/nodePools/_*&#x60;. | [optional] 
**nodePoolId** | **String** | Required. Deprecated. The name of the node pool to update. This field has been deprecated and replaced by the name field. | [optional] 
**projectId** | **String** | Required. Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field. | [optional] 
**zone** | **String** | Required. Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field. | [optional] 


