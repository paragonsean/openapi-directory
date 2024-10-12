

# SapHanaDatabaseDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainType** | **ConfiguredSlaType** |  |  [optional] |
|**id** | **String** | The ID of the SAP HANA database. |  |
|**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. |  [optional] |
|**name** | **String** | The name of the SAP HANA database. |  |
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
|**dataPathType** | **SapHanaDataPathType** |  |  |
|**dbStatus** | [**DbStatusEnum**](#DbStatusEnum) | Whether the database is in an ACTIVE,INACTIVE, or UNKNOWN state. |  |
|**dbType** | [**DbTypeEnum**](#DbTypeEnum) | The type of SAP HANA database. Possible values are SYSTEM or TENANT. The SYSTEM database stores information about SAP HANA users and central system management. The TENANT database contains databases used by applications. |  |
|**isRelic** | **Boolean** | Specifies whether the SAP HANA database is accessible on the CDM cluster. |  |
|**logBackupIntervalInSecs** | **Integer** | The log backup interval in seconds. |  [optional] |
|**primaryClusterUuid** | **String** | The ID of the CDM cluster that protects the SAP HANA database. |  |
|**protectionDate** | **OffsetDateTime** | The UTC timestamp for when the SAP HANA database was first protected. |  [optional] |
|**sapHanaSystemId** | **String** | The ID of the SAP HANA system that owns the database. |  |
|**sapHanaSystemName** | **String** | Name of the SAP HANA system that owns the database. |  |
|**dataPathSpec** | [**SapHanaDataPathSpec**](SapHanaDataPathSpec.md) |  |  [optional] |
|**forceFull** | **Boolean** | Determines whether to force a full snapshot for the next backup of the SAP HANA database. Use true to force a full snapshot and false to use the default. The backup job resets the parameter to false after a successful full backup. |  |
|**latestRecoveryPoint** | **OffsetDateTime** | The most recent recovery point for the database. |  [optional] |
|**logSnapshotJobIntervalInMinutes** | **Integer** | The log snapshot job interval in minutes. |  |
|**numChannels** | **Integer** | The number of channels for multistream backups. |  [optional] |
|**oldestRecoveryPoint** | **OffsetDateTime** | The earliest recovery point for the database. |  [optional] |
|**previousFailedBackupPrefixes** | **List&lt;String&gt;** | The Prefixes of previous failed backup jobs. Prefix is an identifier used by SAP HANA BACKINT to uniquely identify backups. |  |
|**snapshotCount** | **Integer** | The total number of SAP HANA snapshots that have been taken. |  |



## Enum: SlaAssignmentEnum

| Name | Value |
|---- | -----|
| DERIVED | &quot;Derived&quot; |
| DIRECT | &quot;Direct&quot; |
| UNASSIGNED | &quot;Unassigned&quot; |



## Enum: DbStatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



## Enum: DbTypeEnum

| Name | Value |
|---- | -----|
| SYSTEM | &quot;SYSTEM&quot; |
| TENANT | &quot;TENANT&quot; |



