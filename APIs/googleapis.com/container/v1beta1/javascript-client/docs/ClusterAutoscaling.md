# KubernetesEngineApi.ClusterAutoscaling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoprovisioningLocations** | **[String]** | The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool&#39;s nodes can be created by NAP. | [optional] 
**autoprovisioningNodePoolDefaults** | [**AutoprovisioningNodePoolDefaults**](AutoprovisioningNodePoolDefaults.md) |  | [optional] 
**autoscalingProfile** | **String** | Defines autoscaling behaviour. | [optional] 
**enableNodeAutoprovisioning** | **Boolean** | Enables automatic node pool creation and deletion. | [optional] 
**resourceLimits** | [**[ResourceLimit]**](ResourceLimit.md) | Contains global constraints regarding minimum and maximum amount of resources in the cluster. | [optional] 



## Enum: AutoscalingProfileEnum


* `PROFILE_UNSPECIFIED` (value: `"PROFILE_UNSPECIFIED"`)

* `OPTIMIZE_UTILIZATION` (value: `"OPTIMIZE_UTILIZATION"`)

* `BALANCED` (value: `"BALANCED"`)




