

# RestoreConfig

Configuration of a restore. Next id: 14

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allNamespaces** | **Boolean** | Restore all namespaced resources in the Backup if set to \&quot;True\&quot;. Specifying this field to \&quot;False\&quot; is an error. |  [optional] |
|**clusterResourceConflictPolicy** | [**ClusterResourceConflictPolicyEnum**](#ClusterResourceConflictPolicyEnum) | Optional. Defines the behavior for handling the situation where cluster-scoped resources being restored already exist in the target cluster. This MUST be set to a value other than CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED if cluster_resource_restore_scope is not empty. |  [optional] |
|**clusterResourceRestoreScope** | [**ClusterResourceRestoreScope**](ClusterResourceRestoreScope.md) |  |  [optional] |
|**excludedNamespaces** | [**Namespaces**](Namespaces.md) |  |  [optional] |
|**namespacedResourceRestoreMode** | [**NamespacedResourceRestoreModeEnum**](#NamespacedResourceRestoreModeEnum) | Optional. Defines the behavior for handling the situation where sets of namespaced resources being restored already exist in the target cluster. This MUST be set to a value other than NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED. |  [optional] |
|**noNamespaces** | **Boolean** | Do not restore any namespaced resources if set to \&quot;True\&quot;. Specifying this field to \&quot;False\&quot; is not allowed. |  [optional] |
|**selectedApplications** | [**NamespacedNames**](NamespacedNames.md) |  |  [optional] |
|**selectedNamespaces** | [**Namespaces**](Namespaces.md) |  |  [optional] |
|**substitutionRules** | [**List&lt;SubstitutionRule&gt;**](SubstitutionRule.md) | Optional. A list of transformation rules to be applied against Kubernetes resources as they are selected for restoration from a Backup. Rules are executed in order defined - this order matters, as changes made by a rule may impact the filtering logic of subsequent rules. An empty list means no substitution will occur. |  [optional] |
|**transformationRules** | [**List&lt;TransformationRule&gt;**](TransformationRule.md) | Optional. A list of transformation rules to be applied against Kubernetes resources as they are selected for restoration from a Backup. Rules are executed in order defined - this order matters, as changes made by a rule may impact the filtering logic of subsequent rules. An empty list means no transformation will occur. |  [optional] |
|**volumeDataRestorePolicy** | [**VolumeDataRestorePolicyEnum**](#VolumeDataRestorePolicyEnum) | Optional. Specifies the mechanism to be used to restore volume data. Default: VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED (will be treated as NO_VOLUME_DATA_RESTORATION). |  [optional] |



## Enum: ClusterResourceConflictPolicyEnum

| Name | Value |
|---- | -----|
| CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED | &quot;CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED&quot; |
| USE_EXISTING_VERSION | &quot;USE_EXISTING_VERSION&quot; |
| USE_BACKUP_VERSION | &quot;USE_BACKUP_VERSION&quot; |



## Enum: NamespacedResourceRestoreModeEnum

| Name | Value |
|---- | -----|
| NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED | &quot;NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED&quot; |
| DELETE_AND_RESTORE | &quot;DELETE_AND_RESTORE&quot; |
| FAIL_ON_CONFLICT | &quot;FAIL_ON_CONFLICT&quot; |



## Enum: VolumeDataRestorePolicyEnum

| Name | Value |
|---- | -----|
| VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED | &quot;VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED&quot; |
| RESTORE_VOLUME_DATA_FROM_BACKUP | &quot;RESTORE_VOLUME_DATA_FROM_BACKUP&quot; |
| REUSE_VOLUME_HANDLE_FROM_BACKUP | &quot;REUSE_VOLUME_HANDLE_FROM_BACKUP&quot; |
| NO_VOLUME_DATA_RESTORATION | &quot;NO_VOLUME_DATA_RESTORATION&quot; |



