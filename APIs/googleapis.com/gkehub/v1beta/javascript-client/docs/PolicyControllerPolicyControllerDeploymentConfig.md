# GkeHubApi.PolicyControllerPolicyControllerDeploymentConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerResources** | [**PolicyControllerResourceRequirements**](PolicyControllerResourceRequirements.md) |  | [optional] 
**podAffinity** | **String** | Pod affinity configuration. | [optional] 
**podAntiAffinity** | **Boolean** | Pod anti-affinity enablement. Deprecated: use &#x60;pod_affinity&#x60; instead. | [optional] 
**podTolerations** | [**[PolicyControllerToleration]**](PolicyControllerToleration.md) | Pod tolerations of node taints. | [optional] 
**replicaCount** | **String** | Pod replica count. | [optional] 



## Enum: PodAffinityEnum


* `AFFINITY_UNSPECIFIED` (value: `"AFFINITY_UNSPECIFIED"`)

* `NO_AFFINITY` (value: `"NO_AFFINITY"`)

* `ANTI_AFFINITY` (value: `"ANTI_AFFINITY"`)




