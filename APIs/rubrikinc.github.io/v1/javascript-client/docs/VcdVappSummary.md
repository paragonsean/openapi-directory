# RubrikRestApi.VcdVappSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainType** | [**ConfiguredSlaType**](ConfiguredSlaType.md) |  | [optional] 
**id** | **String** | ID assigned to a vCD vApp object. | 
**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. | [optional] 
**name** | **String** | Name assigned to a vCD vApp object. | 
**primaryClusterId** | **String** | The ID of the cluster that manages the Rubrik object. | 
**slaLastUpdateTime** | **Date** | The UTC time when the SLA Domain was last updated. | [optional] 
**effectiveSlaDomainId** | **String** | The ID of the SLA Domain that controls the protection of the Rubrik object. | 
**effectiveSlaDomainName** | **String** | The name of the SLA Domain that controls the protection of the Rubrik object. | 
**effectiveSlaDomainPolarisManagedId** | **String** | Optional. This field contains the managed ID of of the Polaris-managed effective SLA Domain. | [optional] 
**effectiveSlaSourceObjectId** | **String** | The ID of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. | [optional] 
**effectiveSlaSourceObjectName** | **String** | The name of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. | [optional] 
**isEffectiveSlaDomainRetentionLocked** | **Boolean** | Indicates whether the effective SLA Domain is Retention Locked. When this value is &#39;true&#39;, the effective SLA domain is a Retention Lock SLA Domain. | [optional] 
**retentionSlaDomainId** | **String** | The ID of the SLA Domain whose retention policy is in use. | [optional] 
**slaAssignment** | **String** | The SLA assignment type. Direct SLA assignment means that a SLA Domain was configured directly on the Rubrik object by the user. Derived SLA assignment means that the Rubrik object inherits an SLA Domain from its parent Rubrik object. | 
**catalogId** | **String** | ID of the parent catalog if the vApp object is a template. | [optional] 
**currentBackupTaskInfo** | [**BackupTaskDiagnosticInfo**](BackupTaskDiagnosticInfo.md) |  | [optional] 
**includeBackupTaskInfo** | **Boolean** | Boolean value that indicates if backup task information isincluded in the response. | [optional] 
**infraPath** | [**[ManagedHierarchyObjectAncestor]**](ManagedHierarchyObjectAncestor.md) | Brief information of all the objects in the infrastructure path to this vCD vApp object. | 
**isRelic** | **Boolean** | Boolean value that indicates whether a vApp is present on the specified vCD cluster. Set to &#39;true&#39; when the vApp is present and &#39;false&#39; when the vApp is not present. | [optional] 
**isTemplate** | **Boolean** | A Boolean value that indicates whether the vApp object is a template. When this value is &#39;true,&#39; the vApp object is a template. When this value is &#39;false,&#39; the vApp object is not a template. | [optional] 
**lastSnapshotTime** | **Date** | The timestamp of the previous snapshot. | [optional] 
**numMissedSnapshot** | **Number** | An integer that specifies the number of missed snapshots. | 
**pendingSlaDomain** | [**ManagedObjectPendingSlaInfo**](ManagedObjectPendingSlaInfo.md) |  | [optional] 
**vcdClusterId** | **String** | ID assigned to a vCD Cluster object that contains a specified vApp object. | [optional] 
**vcdClusterName** | **String** | Name assigned to a vCD Cluster object that contains a specified vApp object. | [optional] 



## Enum: SlaAssignmentEnum


* `Derived` (value: `"Derived"`)

* `Direct` (value: `"Direct"`)

* `Unassigned` (value: `"Unassigned"`)




