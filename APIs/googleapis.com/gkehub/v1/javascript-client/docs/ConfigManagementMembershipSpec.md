# GkeHubApi.ConfigManagementMembershipSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **String** | The user-specified cluster name used by Config Sync cluster-name-selector annotation or ClusterSelector, for applying configs to only a subset of clusters. Omit this field if the cluster&#39;s fleet membership name is used by Config Sync cluster-name-selector annotation or ClusterSelector. Set this field if a name different from the cluster&#39;s fleet membership name is used by Config Sync cluster-name-selector annotation or ClusterSelector. | [optional] 
**configSync** | [**ConfigManagementConfigSync**](ConfigManagementConfigSync.md) |  | [optional] 
**hierarchyController** | [**ConfigManagementHierarchyControllerConfig**](ConfigManagementHierarchyControllerConfig.md) |  | [optional] 
**management** | **String** | Enables automatic Feature management. | [optional] 
**policyController** | [**ConfigManagementPolicyController**](ConfigManagementPolicyController.md) |  | [optional] 
**version** | **String** | Version of ACM installed. | [optional] 



## Enum: ManagementEnum


* `UNSPECIFIED` (value: `"MANAGEMENT_UNSPECIFIED"`)

* `AUTOMATIC` (value: `"MANAGEMENT_AUTOMATIC"`)

* `MANUAL` (value: `"MANAGEMENT_MANUAL"`)




