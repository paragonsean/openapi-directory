

# DatabaseProperties

The database's properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalogCollation** | [**CatalogCollationEnum**](#CatalogCollationEnum) | Collation of the metadata catalog. |  [optional] |
|**collation** | **String** | The collation of the database. |  [optional] |
|**createMode** | [**CreateModeEnum**](#CreateModeEnum) | Specifies the mode of database creation.    Default: regular database creation.    Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database.    Secondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database.    PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified.    Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore.    Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database&#39;s original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time.    RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID.    Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition. |  [optional] |
|**creationDate** | **OffsetDateTime** | The creation date of the database (ISO8601 format). |  [optional] [readonly] |
|**currentServiceObjectiveName** | **String** | The current service level objective name of the database. |  [optional] [readonly] |
|**databaseId** | **UUID** | The ID of the database. |  [optional] [readonly] |
|**defaultSecondaryLocation** | **String** | The default secondary region for this database. |  [optional] [readonly] |
|**elasticPoolId** | **String** | The resource identifier of the elastic pool containing this database. |  [optional] |
|**failoverGroupId** | **String** | Failover Group resource identifier that this database belongs to. |  [optional] [readonly] |
|**longTermRetentionBackupResourceId** | **String** | The resource identifier of the long term retention backup associated with create operation of this database. |  [optional] |
|**maxSizeBytes** | **Long** | The max size of the database expressed in bytes. |  [optional] |
|**recoverableDatabaseId** | **String** | The resource identifier of the recoverable database associated with create operation of this database. |  [optional] |
|**recoveryServicesRecoveryPointId** | **String** | The resource identifier of the recovery point associated with create operation of this database. |  [optional] |
|**restorableDroppedDatabaseId** | **String** | The resource identifier of the restorable dropped database associated with create operation of this database. |  [optional] |
|**restorePointInTime** | **OffsetDateTime** | Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. |  [optional] |
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
| ONLINE_SECONDARY | &quot;OnlineSecondary&quot; |
| POINT_IN_TIME_RESTORE | &quot;PointInTimeRestore&quot; |
| RESTORE | &quot;Restore&quot; |
| RECOVERY | &quot;Recovery&quot; |
| RESTORE_EXTERNAL_BACKUP | &quot;RestoreExternalBackup&quot; |
| RESTORE_EXTERNAL_BACKUP_SECONDARY | &quot;RestoreExternalBackupSecondary&quot; |
| RESTORE_LONG_TERM_RETENTION_BACKUP | &quot;RestoreLongTermRetentionBackup&quot; |



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



