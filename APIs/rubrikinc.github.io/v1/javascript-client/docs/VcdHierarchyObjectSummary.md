# RubrikRestApi.VcdHierarchyObjectSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainType** | [**ConfiguredSlaType**](ConfiguredSlaType.md) |  | [optional] 
**id** | **String** | The ID of the Rubrik object. | 
**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. | [optional] 
**name** | **String** | The name of the Rubrik object. | 
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
**infraPath** | [**[ManagedHierarchyObjectAncestor]**](ManagedHierarchyObjectAncestor.md) |  | [optional] 
**isDeleted** | **Boolean** | Indicates whether the vCD hierarchy object is deleted. | 
**isRelic** | **Boolean** | Whether this managed object is a relic (an archived snappable with unexpired snapshots). | 
**slaPath** | [**[ManagedHierarchyObjectAncestor]**](ManagedHierarchyObjectAncestor.md) |  | [optional] 
**connectionStatus** | [**VcdConnectionStatus**](VcdConnectionStatus.md) |  | [optional] 
**descendantCount** | [**VcdHierarchyObjectDescendantCount**](VcdHierarchyObjectDescendantCount.md) |  | 
**extendedAttributes** | [**VcdHierarchyObjectAttributes**](VcdHierarchyObjectAttributes.md) |  | [optional] 
**ipAddress** | **String** | IPv4 address for a vCD cluster or vCenter Server that is managed through a VIM Server. | [optional] 
**objectType** | [**VcdObjectType**](VcdObjectType.md) |  | 
**pendingSlaDomain** | [**ManagedObjectPendingSlaInfo**](ManagedObjectPendingSlaInfo.md) |  | [optional] 
**vcenterId** | **String** | ID assigned to a vCenter Server instance that is managed through a VIM Server. | [optional] 



## Enum: SlaAssignmentEnum


* `Derived` (value: `"Derived"`)

* `Direct` (value: `"Direct"`)

* `Unassigned` (value: `"Unassigned"`)




