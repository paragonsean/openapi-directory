# KubernetesEngineApi.CompleteIPRotationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterId** | **String** | Required. Deprecated. The name of the cluster. This field has been deprecated and replaced by the name field. | [optional] 
**name** | **String** | The name (project, location, cluster name) of the cluster to complete IP rotation. Specified in the format &#x60;projects/_*_/locations/_*_/clusters/_*&#x60;. | [optional] 
**projectId** | **String** | Required. Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field. | [optional] 
**zone** | **String** | Required. Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field. | [optional] 


