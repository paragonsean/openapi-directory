

# ConfigManagementMembershipSpec

**Anthos Config Management**: Configuration for a single cluster. Intended to parallel the ConfigManagement CR.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**binauthz** | [**ConfigManagementBinauthzConfig**](ConfigManagementBinauthzConfig.md) |  |  [optional] |
|**cluster** | **String** | The user-specified cluster name used by Config Sync cluster-name-selector annotation or ClusterSelector, for applying configs to only a subset of clusters. Omit this field if the cluster&#39;s fleet membership name is used by Config Sync cluster-name-selector annotation or ClusterSelector. Set this field if a name different from the cluster&#39;s fleet membership name is used by Config Sync cluster-name-selector annotation or ClusterSelector. |  [optional] |
|**configSync** | [**ConfigManagementConfigSync**](ConfigManagementConfigSync.md) |  |  [optional] |
|**hierarchyController** | [**ConfigManagementHierarchyControllerConfig**](ConfigManagementHierarchyControllerConfig.md) |  |  [optional] |
|**management** | [**ManagementEnum**](#ManagementEnum) | Enables automatic Feature management. |  [optional] |
|**policyController** | [**ConfigManagementPolicyController**](ConfigManagementPolicyController.md) |  |  [optional] |
|**version** | **String** | Version of ACM installed. |  [optional] |



## Enum: ManagementEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MANAGEMENT_UNSPECIFIED&quot; |
| AUTOMATIC | &quot;MANAGEMENT_AUTOMATIC&quot; |
| MANUAL | &quot;MANAGEMENT_MANUAL&quot; |



