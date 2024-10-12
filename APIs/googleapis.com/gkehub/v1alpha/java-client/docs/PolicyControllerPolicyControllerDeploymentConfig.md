

# PolicyControllerPolicyControllerDeploymentConfig

Deployment-specific configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerResources** | [**PolicyControllerResourceRequirements**](PolicyControllerResourceRequirements.md) |  |  [optional] |
|**podAffinity** | [**PodAffinityEnum**](#PodAffinityEnum) | Pod affinity configuration. |  [optional] |
|**podAntiAffinity** | **Boolean** | Pod anti-affinity enablement. Deprecated: use &#x60;pod_affinity&#x60; instead. |  [optional] |
|**podTolerations** | [**List&lt;PolicyControllerToleration&gt;**](PolicyControllerToleration.md) | Pod tolerations of node taints. |  [optional] |
|**replicaCount** | **String** | Pod replica count. |  [optional] |



## Enum: PodAffinityEnum

| Name | Value |
|---- | -----|
| AFFINITY_UNSPECIFIED | &quot;AFFINITY_UNSPECIFIED&quot; |
| NO_AFFINITY | &quot;NO_AFFINITY&quot; |
| ANTI_AFFINITY | &quot;ANTI_AFFINITY&quot; |



