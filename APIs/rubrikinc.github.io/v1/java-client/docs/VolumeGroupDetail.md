

# VolumeGroupDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configuredSlaDomainId** | **String** | The ID of the SLA Domain policy to assign to the Volume Group. |  |
|**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainType** | **ConfiguredSlaType** |  |  [optional] |
|**id** | **String** | The unique ID of the Volume Group. |  |
|**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. |  [optional] |
|**name** | **String** | The name of the Volume Group. |  |
|**primaryClusterId** | **String** | The ID of the cluster that manages the Rubrik object. |  |
|**slaLastUpdateTime** | **OffsetDateTime** | The UTC time when the SLA Domain was last updated. |  [optional] |
|**effectiveSlaDomainId** | **String** | The ID of the SLA Domain that controls the protection of the Rubrik object. |  |
|**effectiveSlaDomainName** | **String** | The name of the SLA Domain that controls the protection of the Rubrik object. |  |
|**effectiveSlaDomainPolarisManagedId** | **String** | Optional. This field contains the managed ID of of the Polaris-managed effective SLA Domain. |  [optional] |
|**effectiveSlaSourceObjectId** | **String** | The ID of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. |  [optional] |
|**effectiveSlaSourceObjectName** | **String** | The name of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. |  [optional] |
|**isEffectiveSlaDomainRetentionLocked** | **Boolean** | Indicates whether the effective SLA Domain is Retention Locked. When this value is &#39;true&#39;, the effective SLA domain is a Retention Lock SLA Domain. |  [optional] |
|**retentionSlaDomainId** | **String** | The ID of the SLA Domain whose retention policy is in use. |  [optional] |
|**slaAssignment** | [**SlaAssignmentEnum**](#SlaAssignmentEnum) | The SLA assignment type. Direct SLA assignment means that a SLA Domain was configured directly on the Rubrik object by the user. Derived SLA assignment means that the Rubrik object inherits an SLA Domain from its parent Rubrik object. |  |
|**forceFull** | **Boolean** | Specifies whether the Volume Group is set to take a full snapshot for the next backup. |  [optional] |
|**hostId** | **String** | The unique ID of the host that contains the Volume Group. |  [optional] |
|**hostname** | **String** | The name of the host that contains the Volume Group. |  [optional] |
|**isRelic** | **Boolean** | Specifies whether the Volume Group is accessible on the Rubrik cluster. |  |
|**needsMigration** | **Boolean** | Specifies whether the Volume Group needs to be migrated in order to use the fast VHDX builder. This flag is set only when the Volume Group&#39;s last backup job failed due to an error during data fetch, and the backup job did not use the fast VHDX builder. |  [optional] |
|**blackoutWindowStatus** | [**BlackoutWindowStatus**](BlackoutWindowStatus.md) |  |  |
|**blackoutWindows** | [**BlackoutWindows**](BlackoutWindows.md) |  |  |
|**isPaused** | **Boolean** | Indicates whether backup, archival, and replication are paused for this Volume Group. |  |
|**pendingSlaDomain** | [**ManagedObjectPendingSlaInfo**](ManagedObjectPendingSlaInfo.md) |  |  [optional] |
|**volumes** | [**List&lt;HostVolumeSummary&gt;**](HostVolumeSummary.md) | Configuration details for the volumes in the Volume Group. |  |



## Enum: SlaAssignmentEnum

| Name | Value |
|---- | -----|
| DERIVED | &quot;Derived&quot; |
| DIRECT | &quot;Direct&quot; |
| UNASSIGNED | &quot;Unassigned&quot; |



