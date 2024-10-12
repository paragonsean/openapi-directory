# KubernetesEngineApi.SetNodePoolAutoscalingRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscaling** | [**NodePoolAutoscaling**](NodePoolAutoscaling.md) |  | [optional] 
**clusterId** | **String** | Required. Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field. | [optional] 
**name** | **String** | The name (project, location, cluster, node pool) of the node pool to set autoscaler settings. Specified in the format &#x60;projects/_*_/locations/_*_/clusters/_*_/nodePools/_*&#x60;. | [optional] 
**nodePoolId** | **String** | Required. Deprecated. The name of the node pool to upgrade. This field has been deprecated and replaced by the name field. | [optional] 
**projectId** | **String** | Required. Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field. | [optional] 
**zone** | **String** | Required. Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field. | [optional] 


