# BackupForGkeApi.RestoreConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allNamespaces** | **Boolean** | Restore all namespaced resources in the Backup if set to \&quot;True\&quot;. Specifying this field to \&quot;False\&quot; is an error. | [optional] 
**clusterResourceConflictPolicy** | **String** | Optional. Defines the behavior for handling the situation where cluster-scoped resources being restored already exist in the target cluster. This MUST be set to a value other than CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED if cluster_resource_restore_scope is not empty. | [optional] 
**clusterResourceRestoreScope** | [**ClusterResourceRestoreScope**](ClusterResourceRestoreScope.md) |  | [optional] 
**excludedNamespaces** | [**Namespaces**](Namespaces.md) |  | [optional] 
**namespacedResourceRestoreMode** | **String** | Optional. Defines the behavior for handling the situation where sets of namespaced resources being restored already exist in the target cluster. This MUST be set to a value other than NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED. | [optional] 
**noNamespaces** | **Boolean** | Do not restore any namespaced resources if set to \&quot;True\&quot;. Specifying this field to \&quot;False\&quot; is not allowed. | [optional] 
**selectedApplications** | [**NamespacedNames**](NamespacedNames.md) |  | [optional] 
**selectedNamespaces** | [**Namespaces**](Namespaces.md) |  | [optional] 
**substitutionRules** | [**[SubstitutionRule]**](SubstitutionRule.md) | Optional. A list of transformation rules to be applied against Kubernetes resources as they are selected for restoration from a Backup. Rules are executed in order defined - this order matters, as changes made by a rule may impact the filtering logic of subsequent rules. An empty list means no substitution will occur. | [optional] 
**transformationRules** | [**[TransformationRule]**](TransformationRule.md) | Optional. A list of transformation rules to be applied against Kubernetes resources as they are selected for restoration from a Backup. Rules are executed in order defined - this order matters, as changes made by a rule may impact the filtering logic of subsequent rules. An empty list means no transformation will occur. | [optional] 
**volumeDataRestorePolicy** | **String** | Optional. Specifies the mechanism to be used to restore volume data. Default: VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED (will be treated as NO_VOLUME_DATA_RESTORATION). | [optional] 



## Enum: ClusterResourceConflictPolicyEnum


* `CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED` (value: `"CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED"`)

* `USE_EXISTING_VERSION` (value: `"USE_EXISTING_VERSION"`)

* `USE_BACKUP_VERSION` (value: `"USE_BACKUP_VERSION"`)





## Enum: NamespacedResourceRestoreModeEnum


* `NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED` (value: `"NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED"`)

* `DELETE_AND_RESTORE` (value: `"DELETE_AND_RESTORE"`)

* `FAIL_ON_CONFLICT` (value: `"FAIL_ON_CONFLICT"`)





## Enum: VolumeDataRestorePolicyEnum


* `VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED` (value: `"VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED"`)

* `RESTORE_VOLUME_DATA_FROM_BACKUP` (value: `"RESTORE_VOLUME_DATA_FROM_BACKUP"`)

* `REUSE_VOLUME_HANDLE_FROM_BACKUP` (value: `"REUSE_VOLUME_HANDLE_FROM_BACKUP"`)

* `NO_VOLUME_DATA_RESTORATION` (value: `"NO_VOLUME_DATA_RESTORATION"`)




