# SqlManagementClient.DatabaseProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalogCollation** | **String** | Collation of the metadata catalog. | [optional] 
**collation** | **String** | The collation of the database. | [optional] 
**createMode** | **String** | Specifies the mode of database creation.    Default: regular database creation.    Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database.    Secondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database.    PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified.    Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore.    Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database&#39;s original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time.    RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID.    Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition. | [optional] 
**creationDate** | **Date** | The creation date of the database (ISO8601 format). | [optional] [readonly] 
**currentServiceObjectiveName** | **String** | The current service level objective name of the database. | [optional] [readonly] 
**databaseId** | **String** | The ID of the database. | [optional] [readonly] 
**defaultSecondaryLocation** | **String** | The default secondary region for this database. | [optional] [readonly] 
**elasticPoolId** | **String** | The resource identifier of the elastic pool containing this database. | [optional] 
**failoverGroupId** | **String** | Failover Group resource identifier that this database belongs to. | [optional] [readonly] 
**longTermRetentionBackupResourceId** | **String** | The resource identifier of the long term retention backup associated with create operation of this database. | [optional] 
**maxSizeBytes** | **Number** | The max size of the database expressed in bytes. | [optional] 
**recoverableDatabaseId** | **String** | The resource identifier of the recoverable database associated with create operation of this database. | [optional] 
**recoveryServicesRecoveryPointId** | **String** | The resource identifier of the recovery point associated with create operation of this database. | [optional] 
**restorableDroppedDatabaseId** | **String** | The resource identifier of the restorable dropped database associated with create operation of this database. | [optional] 
**restorePointInTime** | **Date** | Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. | [optional] 
**sampleName** | **String** | The name of the sample schema to apply when creating this database. | [optional] 
**sourceDatabaseDeletionDate** | **Date** | Specifies the time that the database was deleted. | [optional] 
**sourceDatabaseId** | **String** | The resource identifier of the source database associated with create operation of this database. | [optional] 
**status** | **String** | The status of the database. | [optional] [readonly] 
**zoneRedundant** | **Boolean** | Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. | [optional] 



## Enum: CatalogCollationEnum


* `DATABASE_DEFAULT` (value: `"DATABASE_DEFAULT"`)

* `SQL_Latin1_General_CP1_CI_AS` (value: `"SQL_Latin1_General_CP1_CI_AS"`)





## Enum: CreateModeEnum


* `Default` (value: `"Default"`)

* `Copy` (value: `"Copy"`)

* `Secondary` (value: `"Secondary"`)

* `OnlineSecondary` (value: `"OnlineSecondary"`)

* `PointInTimeRestore` (value: `"PointInTimeRestore"`)

* `Restore` (value: `"Restore"`)

* `Recovery` (value: `"Recovery"`)

* `RestoreExternalBackup` (value: `"RestoreExternalBackup"`)

* `RestoreExternalBackupSecondary` (value: `"RestoreExternalBackupSecondary"`)

* `RestoreLongTermRetentionBackup` (value: `"RestoreLongTermRetentionBackup"`)





## Enum: SampleNameEnum


* `AdventureWorksLT` (value: `"AdventureWorksLT"`)

* `WideWorldImportersStd` (value: `"WideWorldImportersStd"`)

* `WideWorldImportersFull` (value: `"WideWorldImportersFull"`)





## Enum: StatusEnum


* `Online` (value: `"Online"`)

* `Restoring` (value: `"Restoring"`)

* `RecoveryPending` (value: `"RecoveryPending"`)

* `Recovering` (value: `"Recovering"`)

* `Suspect` (value: `"Suspect"`)

* `Offline` (value: `"Offline"`)

* `Standby` (value: `"Standby"`)

* `Shutdown` (value: `"Shutdown"`)

* `EmergencyMode` (value: `"EmergencyMode"`)

* `AutoClosed` (value: `"AutoClosed"`)

* `Copying` (value: `"Copying"`)

* `Creating` (value: `"Creating"`)

* `Inaccessible` (value: `"Inaccessible"`)

* `OfflineSecondary` (value: `"OfflineSecondary"`)

* `Pausing` (value: `"Pausing"`)

* `Paused` (value: `"Paused"`)

* `Resuming` (value: `"Resuming"`)

* `Scaling` (value: `"Scaling"`)




