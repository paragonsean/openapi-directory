# KubernetesEngineApi.SetMasterAuthRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Required. The exact form of action to be taken on the master auth. | [optional] 
**clusterId** | **String** | Required. Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field. | [optional] 
**name** | **String** | The name (project, location, cluster) of the cluster to set auth. Specified in the format &#x60;projects/_*_/locations/_*_/clusters/_*&#x60;. | [optional] 
**projectId** | **String** | Required. Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field. | [optional] 
**update** | [**MasterAuth**](MasterAuth.md) |  | [optional] 
**zone** | **String** | Required. Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field. | [optional] 



## Enum: ActionEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `SET_PASSWORD` (value: `"SET_PASSWORD"`)

* `GENERATE_PASSWORD` (value: `"GENERATE_PASSWORD"`)

* `SET_USERNAME` (value: `"SET_USERNAME"`)




