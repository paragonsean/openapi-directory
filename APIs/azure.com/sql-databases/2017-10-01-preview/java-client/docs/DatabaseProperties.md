

# DatabaseProperties

The database's properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoPauseDelay** | **Integer** | Time in minutes after which database is automatically paused. A value of -1 means that automatic pause is disabled |  [optional] |
|**catalogCollation** | [**CatalogCollationEnum**](#CatalogCollationEnum) | Collation of the metadata catalog. |  [optional] |
|**collation** | **String** | The collation of the database. |  [optional] |
|**createMode** | [**CreateModeEnum**](#CreateModeEnum) | Specifies the mode of database creation.    Default: regular database creation.    Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database.    Secondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database.    PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified.    Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore.    Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database&#39;s original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time.    RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID.    Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition. |  [optional] |
|**creationDate** | **OffsetDateTime** | The creation date of the database (ISO8601 format). |  [optional] [readonly] |
|**currentServiceObjectiveName** | **String** | The current service level objective name of the database. |  [optional] [readonly] |
|**currentSku** | [**Sku**](Sku.md) |  |  [optional] |
|**databaseId** | **UUID** | The ID of the database. |  [optional] [readonly] |
|**defaultSecondaryLocation** | **String** | The default secondary region for this database. |  [optional] [readonly] |
|**earliestRestoreDate** | **OffsetDateTime** | This records the earliest start date and time that restore is available for this database (ISO8601 format). |  [optional] [readonly] |
|**elasticPoolId** | **String** | The resource identifier of the elastic pool containing this database. |  [optional] |
|**failoverGroupId** | **String** | Failover Group resource identifier that this database belongs to. |  [optional] [readonly] |
|**licenseType** | [**LicenseTypeEnum**](#LicenseTypeEnum) | The license type to apply for this database. |  [optional] |
|**longTermRetentionBackupResourceId** | **String** | The resource identifier of the long term retention backup associated with create operation of this database. |  [optional] |
|**maxLogSizeBytes** | **Long** | The max log size for this database. |  [optional] [readonly] |
|**maxSizeBytes** | **Long** | The max size of the database expressed in bytes. |  [optional] |
|**minCapacity** | **Double** | Minimal capacity that database will always have allocated, if not paused |  [optional] |
|**pausedDate** | **OffsetDateTime** | The date when database was paused by user configuration or action (ISO8601 format). Null if the database is ready. |  [optional] [readonly] |
|**readReplicaCount** | **Integer** | The number of readonly secondary replicas associated with the database to which readonly application intent connections may be routed. This property is only settable for Hyperscale edition databases. |  [optional] |
|**readScale** | [**ReadScaleEnum**](#ReadScaleEnum) | If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases. |  [optional] |
|**recoverableDatabaseId** | **String** | The resource identifier of the recoverable database associated with create operation of this database. |  [optional] |
|**recoveryServicesRecoveryPointId** | **String** | The resource identifier of the recovery point associated with create operation of this database. |  [optional] |
|**requestedServiceObjectiveName** | **String** | The requested service level objective name of the database. |  [optional] [readonly] |
|**restorableDroppedDatabaseId** | **String** | The resource identifier of the restorable dropped database associated with create operation of this database. |  [optional] |
|**restorePointInTime** | **OffsetDateTime** | Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. |  [optional] |
|**resumedDate** | **OffsetDateTime** | The date when database was resumed by user action or database login (ISO8601 format). Null if the database is paused. |  [optional] [readonly] |
|**sampleName** | [**SampleNameEnum**](#SampleNameEnum) | The name of the sample schema to apply when creating this database. |  [optional] |
|**sourceDatabaseDeletionDate** | **OffsetDateTime** | Specifies the time that the database was deleted. |  [optional] |
|**sourceDatabaseId** | **String** | The resource identifier of the source database associated with create operation of this database. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the database. |  [optional] [readonly] |
|**zoneRedundant** | **Boolean** | Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. |  [optional] |



## Enum: CatalogCollationEnum

| Name | Value |
|---- | -----|
| DATABASE_DEFAULT | &quot;DATABASE_DEFAULT&quot; |
| SQL_LATIN1_GENERAL_CP1_CI_AS | &quot;SQL_Latin1_General_CP1_CI_AS&quot; |



## Enum: CreateModeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| COPY | &quot;Copy&quot; |
| SECONDARY | &quot;Secondary&quot; |
| POINT_IN_TIME_RESTORE | &quot;PointInTimeRestore&quot; |
| RESTORE | &quot;Restore&quot; |
| RECOVERY | &quot;Recovery&quot; |
| RESTORE_EXTERNAL_BACKUP | &quot;RestoreExternalBackup&quot; |
| RESTORE_EXTERNAL_BACKUP_SECONDARY | &quot;RestoreExternalBackupSecondary&quot; |
| RESTORE_LONG_TERM_RETENTION_BACKUP | &quot;RestoreLongTermRetentionBackup&quot; |
| ONLINE_SECONDARY | &quot;OnlineSecondary&quot; |



## Enum: LicenseTypeEnum

| Name | Value |
|---- | -----|
| LICENSE_INCLUDED | &quot;LicenseIncluded&quot; |
| BASE_PRICE | &quot;BasePrice&quot; |



## Enum: ReadScaleEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: SampleNameEnum

| Name | Value |
|---- | -----|
| ADVENTURE_WORKS_LT | &quot;AdventureWorksLT&quot; |
| WIDE_WORLD_IMPORTERS_STD | &quot;WideWorldImportersStd&quot; |
| WIDE_WORLD_IMPORTERS_FULL | &quot;WideWorldImportersFull&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ONLINE | &quot;Online&quot; |
| RESTORING | &quot;Restoring&quot; |
| RECOVERY_PENDING | &quot;RecoveryPending&quot; |
| RECOVERING | &quot;Recovering&quot; |
| SUSPECT | &quot;Suspect&quot; |
| OFFLINE | &quot;Offline&quot; |
| STANDBY | &quot;Standby&quot; |
| SHUTDOWN | &quot;Shutdown&quot; |
| EMERGENCY_MODE | &quot;EmergencyMode&quot; |
| AUTO_CLOSED | &quot;AutoClosed&quot; |
| COPYING | &quot;Copying&quot; |
| CREATING | &quot;Creating&quot; |
| INACCESSIBLE | &quot;Inaccessible&quot; |
| OFFLINE_SECONDARY | &quot;OfflineSecondary&quot; |
| PAUSING | &quot;Pausing&quot; |
| PAUSED | &quot;Paused&quot; |
| RESUMING | &quot;Resuming&quot; |
| SCALING | &quot;Scaling&quot; |
| OFFLINE_CHANGING_DW_PERFORMANCE_TIERS | &quot;OfflineChangingDwPerformanceTiers&quot; |
| ONLINE_CHANGING_DW_PERFORMANCE_TIERS | &quot;OnlineChangingDwPerformanceTiers&quot; |
| DISABLED | &quot;Disabled&quot; |



