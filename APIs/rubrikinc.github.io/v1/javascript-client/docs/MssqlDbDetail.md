# RubrikRestApi.MssqlDbDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainType** | [**ConfiguredSlaType**](ConfiguredSlaType.md) |  | [optional] 
**id** | **String** |  | 
**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. | [optional] 
**name** | **String** |  | 
**primaryClusterId** | **String** |  | 
**slaLastUpdateTime** | **Date** | The UTC time when the SLA Domain was last updated. | [optional] 
**effectiveSlaDomainId** | **String** | The ID of the SLA Domain that controls the protection of the Rubrik object. | 
**effectiveSlaDomainName** | **String** | The name of the SLA Domain that controls the protection of the Rubrik object. | 
**effectiveSlaDomainPolarisManagedId** | **String** | Optional. This field contains the managed ID of of the Polaris-managed effective SLA Domain. | [optional] 
**effectiveSlaSourceObjectId** | **String** | The ID of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. | [optional] 
**effectiveSlaSourceObjectName** | **String** | The name of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. | [optional] 
**isEffectiveSlaDomainRetentionLocked** | **Boolean** | Indicates whether the effective SLA Domain is Retention Locked. When this value is &#39;true&#39;, the effective SLA domain is a Retention Lock SLA Domain. | [optional] 
**retentionSlaDomainId** | **String** | The ID of the SLA Domain whose retention policy is in use. | [optional] 
**slaAssignment** | **String** | The SLA assignment type. Direct SLA assignment means that a SLA Domain was configured directly on the Rubrik object by the user. Derived SLA assignment means that the Rubrik object inherits an SLA Domain from its parent Rubrik object. | 
**availabilityGroupId** | **String** | For an availability database, the ID of the availability group that the database belongs to. | [optional] 
**copyOnly** | **Boolean** | Boolean value that specifies whether or not to perform copy-only backups of the database. When true, database backups are copy-only backups. When false, database backups are full backups. | 
**currentBackupTaskInfo** | [**BackupTaskDiagnosticInfo**](BackupTaskDiagnosticInfo.md) |  | [optional] 
**hasPermissions** | **Boolean** | A Boolean value that specifies whether the cluster has permission to back up the database. When this value is &#39;true&#39;, the cluster has permission to back up the database. | 
**includeBackupTaskInfo** | **Boolean** | True/false value indicating if backup task information is included in the response. | [optional] 
**instanceId** | **String** | This field is deprecated. Use the instanceId field on the replicas list instead. This field will continue to work for non-availability databases, but it is meaningless for availability databases. | [optional] 
**instanceName** | **String** | This field is deprecated. Use the instanceName field on the replicas list instead. This field will continue to work for non-availability databases, but it is meaningless for availability databases. | [optional] 
**isInAvailabilityGroup** | **Boolean** |  | 
**isLiveMount** | **Boolean** | Boolean value that specifies whether a database object is a Live Mount. Value is &#39;true&#39; when the database object is a Live Mount. | 
**isLogShippingSecondary** | **Boolean** | Boolean value that specifies whether a database object represents a secondary database. Value is &#39;true&#39; when the database object represents a secondary database in a log shipping configuration. | 
**isOnline** | **Boolean** | A Boolean value that specifies whether the database is in the ONLINE state. When this value is &#39;true&#39;, the database is in the ONLINE state. | 
**isRelic** | **Boolean** |  | 
**lastSnapshotTime** | **Date** | The timestamp of the previous snapshot.. Only available in the /v1/mssql/db endpoint request body. The information will not be available for other endpoints. | [optional] 
**logBackupFrequencyInSeconds** | **Number** |  | 
**logBackupRetentionHours** | **Number** | Hours to keep a log backup. A value of -1 indicates that a log will only expire when the preceding snapshots have expired. | 
**numMissedSnapshot** | **Number** | An integer that specifies the number of missed snapshots. Only available in the /v1/mssql/db endpoint request body. The information will not be available for other endpoints. | 
**pendingSlaDomain** | [**ManagedObjectPendingSlaInfo**](ManagedObjectPendingSlaInfo.md) |  | [optional] 
**recoveryModel** | **String** | This field is deprecated. Use the recoveryModel field on the replicas list instead. This field will continue to work for non-availability databases, but it is meaningless for availability databases. | [optional] 
**replicas** | [**[MssqlDbReplica]**](MssqlDbReplica.md) | List of replicas of this database. An availability database may have multiple replicas, while other databases will have only one replica. | 
**rootProperties** | [**MssqlRootProperties**](MssqlRootProperties.md) |  | 
**state** | **String** | This field is deprecated. Use the state field on the replicas list instead. This field will continue to work for non-availability databases, but it is meaningless for availability databases. | [optional] 
**unprotectableReasons** | **[String]** | A list of reasons that a SQL Server database cannot be protected by the Rubrik CDM. | 
**blackoutWindowStatus** | [**BlackoutWindowStatus**](BlackoutWindowStatus.md) |  | 
**blackoutWindows** | [**BlackoutWindows**](BlackoutWindows.md) |  | 
**archiveStorage** | **Number** |  | [optional] 
**isLocal** | **Boolean** |  | [optional] 
**isStandby** | **Boolean** | This field is deprecated. Use the isStandby field on the replicas list instead. This field will continue to work for non-availability databases, but it is meaningless for availability databases. | [optional] 
**latestRecoveryPoint** | **Date** |  | [optional] 
**localStorage** | **Number** |  | [optional] 
**maxDataStreams** | **Number** |  | [optional] 
**oldestRecoveryPoint** | **Date** |  | [optional] 
**postBackupScript** | [**MssqlScriptDetail**](MssqlScriptDetail.md) |  | [optional] 
**preBackupScript** | [**MssqlScriptDetail**](MssqlScriptDetail.md) |  | [optional] 
**protectionDate** | **Date** |  | [optional] 
**recoveryForkGuid** | **String** | This field is deprecated. Use the recoveryForkGuid field on the replicas list instead. This field will continue to work for non-availability databases, but it is meaningless for availability databases. | [optional] 
**snapshotCount** | **Number** |  | 



## Enum: SlaAssignmentEnum


* `Derived` (value: `"Derived"`)

* `Direct` (value: `"Direct"`)

* `Unassigned` (value: `"Unassigned"`)





## Enum: RecoveryModelEnum


* `SIMPLE` (value: `"SIMPLE"`)

* `FULL` (value: `"FULL"`)

* `BULK_LOGGED` (value: `"BULK_LOGGED"`)




