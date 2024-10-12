

# MssqlAvailabilityGroupDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainType** | **ConfiguredSlaType** |  |  [optional] |
|**id** | **String** | The ID of the Rubrik object. |  |
|**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. |  [optional] |
|**name** | **String** | The name of the Rubrik object. |  |
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
|**copyOnly** | **Boolean** | Boolean value that specifies whether or not to perform copy-only backups of the database. When true, database backups are copy-only backups. When false, database backups are full backups. |  [optional] |
|**logBackupFrequencyInSeconds** | **Integer** | Seconds between two log backups. A value of 0 disables log backup. |  [optional] |
|**logRetentionHours** | **Integer** | Number of hours to retain a log backup. When the value is set to -1 the Rubrik cluster retains the log backup until the database snapshots that precede the log backup have expired. |  [optional] |



## Enum: SlaAssignmentEnum

| Name | Value |
|---- | -----|
| DERIVED | &quot;Derived&quot; |
| DIRECT | &quot;Direct&quot; |
| UNASSIGNED | &quot;Unassigned&quot; |



