

# ClusterAutoscaling

ClusterAutoscaling contains global, per-cluster information required by Cluster Autoscaler to automatically adjust the size of the cluster and create/delete node pools based on the current needs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoprovisioningLocations** | **List&lt;String&gt;** | The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool&#39;s nodes can be created by NAP. |  [optional] |
|**autoprovisioningNodePoolDefaults** | [**AutoprovisioningNodePoolDefaults**](AutoprovisioningNodePoolDefaults.md) |  |  [optional] |
|**autoscalingProfile** | [**AutoscalingProfileEnum**](#AutoscalingProfileEnum) | Defines autoscaling behaviour. |  [optional] |
|**enableNodeAutoprovisioning** | **Boolean** | Enables automatic node pool creation and deletion. |  [optional] |
|**resourceLimits** | [**List&lt;ResourceLimit&gt;**](ResourceLimit.md) | Contains global constraints regarding minimum and maximum amount of resources in the cluster. |  [optional] |



## Enum: AutoscalingProfileEnum

| Name | Value |
|---- | -----|
| PROFILE_UNSPECIFIED | &quot;PROFILE_UNSPECIFIED&quot; |
| OPTIMIZE_UTILIZATION | &quot;OPTIMIZE_UTILIZATION&quot; |
| BALANCED | &quot;BALANCED&quot; |



