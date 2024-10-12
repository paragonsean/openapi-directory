# AzureSqlDatabase.RecommendedElasticPoolPropertiesDatabasesInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collation** | **String** | The collation of the database. If createMode is not Default, this value is ignored. | [optional] 
**containmentState** | **Number** | The containment state of the database. | [optional] [readonly] 
**createMode** | **String** | Specifies the mode of database creation.  Default: regular database creation.  Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database.  OnlineSecondary/NonReadableSecondary: creates a database as a (readable or nonreadable) secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database.  PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified.  Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore.  Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database&#39;s original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time.  RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID.  Copy, NonReadableSecondary, OnlineSecondary and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition. | [optional] 
**creationDate** | **Date** | The creation date of the database (ISO8601 format). | [optional] [readonly] 
**currentServiceObjectiveId** | **String** | The current service level objective ID of the database. This is the ID of the service level objective that is currently active. | [optional] [readonly] 
**databaseId** | **String** | The ID of the database. | [optional] [readonly] 
**defaultSecondaryLocation** | **String** | The default secondary region for this database. | [optional] [readonly] 
**earliestRestoreDate** | **Date** | This records the earliest start date and time that restore is available for this database (ISO8601 format). | [optional] [readonly] 
**edition** | **String** | The edition of the database. The DatabaseEditions enumeration contains all the valid editions. If createMode is NonReadableSecondary or OnlineSecondary, this value is ignored.    The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the &#x60;Capabilities_ListByLocation&#x60; REST API or one of the following commands:    &#x60;&#x60;&#x60;azurecli  az sql db list-editions -l &lt;location&gt; -o table  &#x60;&#x60;&#x60;&#x60;    &#x60;&#x60;&#x60;powershell  Get-AzSqlServerServiceObjective -Location &lt;location&gt;  &#x60;&#x60;&#x60;&#x60;   | [optional] 
**elasticPoolName** | **String** | The name of the elastic pool the database is in. If elasticPoolName and requestedServiceObjectiveName are both updated, the value of requestedServiceObjectiveName is ignored. Not supported for DataWarehouse edition. | [optional] 
**failoverGroupId** | **String** | The resource identifier of the failover group containing this database. | [optional] [readonly] 
**maxSizeBytes** | **String** | The max size of the database expressed in bytes. If createMode is not Default, this value is ignored. To see possible values, query the capabilities API (/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationID}/capabilities) referred to by operationId: \&quot;Capabilities_ListByLocation.\&quot; | [optional] 
**readScale** | **String** | Conditional. If the database is a geo-secondary, readScale indicates whether read-only connections are allowed to this database or not. Not supported for DataWarehouse edition. | [optional] 
**recommendedIndex** | [**[RecommendedElasticPoolPropertiesDatabasesInnerPropertiesRecommendedIndexInner]**](RecommendedElasticPoolPropertiesDatabasesInnerPropertiesRecommendedIndexInner.md) | The recommended indices for this database. | [optional] [readonly] 
**recoveryServicesRecoveryPointResourceId** | **String** | Conditional. If createMode is RestoreLongTermRetentionBackup, then this value is required. Specifies the resource ID of the recovery point to restore from. | [optional] 
**requestedServiceObjectiveId** | **String** | The configured service level objective ID of the database. This is the service level objective that is in the process of being applied to the database. Once successfully updated, it will match the value of currentServiceObjectiveId property. If requestedServiceObjectiveId and requestedServiceObjectiveName are both updated, the value of requestedServiceObjectiveId overrides the value of requestedServiceObjectiveName.    The list of SKUs may vary by region and support offer. To determine the service objective ids that are available to your subscription in an Azure region, use the &#x60;Capabilities_ListByLocation&#x60; REST API. | [optional] 
**requestedServiceObjectiveName** | **String** | The name of the configured service level objective of the database. This is the service level objective that is in the process of being applied to the database. Once successfully updated, it will match the value of serviceLevelObjective property.     The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the &#x60;Capabilities_ListByLocation&#x60; REST API or one of the following commands:    &#x60;&#x60;&#x60;azurecli  az sql db list-editions -l &lt;location&gt; -o table  &#x60;&#x60;&#x60;&#x60;    &#x60;&#x60;&#x60;powershell  Get-AzSqlServerServiceObjective -Location &lt;location&gt;  &#x60;&#x60;&#x60;&#x60;   | [optional] 
**restorePointInTime** | **Date** | Conditional. If createMode is PointInTimeRestore, this value is required. If createMode is Restore, this value is optional. Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. Must be greater than or equal to the source database&#39;s earliestRestoreDate value. | [optional] 
**sampleName** | **String** | Indicates the name of the sample schema to apply when creating this database. If createMode is not Default, this value is ignored. Not supported for DataWarehouse edition. | [optional] 
**serviceLevelObjective** | **String** | The current service level objective of the database. | [optional] [readonly] 
**serviceTierAdvisors** | [**[RecommendedElasticPoolPropertiesDatabasesInnerPropertiesServiceTierAdvisorsInner]**](RecommendedElasticPoolPropertiesDatabasesInnerPropertiesServiceTierAdvisorsInner.md) | The list of service tier advisors for this database. Expanded property | [optional] [readonly] 
**sourceDatabaseDeletionDate** | **Date** | Conditional. If createMode is Restore and sourceDatabaseId is the deleted database&#39;s original resource id when it existed (as opposed to its current restorable dropped database id), then this value is required. Specifies the time that the database was deleted. | [optional] 
**sourceDatabaseId** | **String** | Conditional. If createMode is Copy, NonReadableSecondary, OnlineSecondary, PointInTimeRestore, Recovery, or Restore, then this value is required. Specifies the resource ID of the source database. If createMode is NonReadableSecondary or OnlineSecondary, the name of the source database must be the same as the new database being created. | [optional] 
**status** | **String** | The status of the database. | [optional] [readonly] 
**transparentDataEncryption** | [**[RecommendedElasticPoolPropertiesDatabasesInnerPropertiesTransparentDataEncryptionInner]**](RecommendedElasticPoolPropertiesDatabasesInnerPropertiesTransparentDataEncryptionInner.md) | The transparent data encryption info for this database. | [optional] [readonly] 
**zoneRedundant** | **Boolean** | Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. | [optional] 



## Enum: CreateModeEnum


* `Copy` (value: `"Copy"`)

* `Default` (value: `"Default"`)

* `NonReadableSecondary` (value: `"NonReadableSecondary"`)

* `OnlineSecondary` (value: `"OnlineSecondary"`)

* `PointInTimeRestore` (value: `"PointInTimeRestore"`)

* `Recovery` (value: `"Recovery"`)

* `Restore` (value: `"Restore"`)

* `RestoreLongTermRetentionBackup` (value: `"RestoreLongTermRetentionBackup"`)





## Enum: EditionEnum


* `Web` (value: `"Web"`)

* `Business` (value: `"Business"`)

* `Basic` (value: `"Basic"`)

* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)

* `PremiumRS` (value: `"PremiumRS"`)

* `Free` (value: `"Free"`)

* `Stretch` (value: `"Stretch"`)

* `DataWarehouse` (value: `"DataWarehouse"`)

* `System` (value: `"System"`)

* `System2` (value: `"System2"`)

* `GeneralPurpose` (value: `"GeneralPurpose"`)

* `BusinessCritical` (value: `"BusinessCritical"`)

* `Hyperscale` (value: `"Hyperscale"`)





## Enum: ReadScaleEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: RequestedServiceObjectiveNameEnum


* `System` (value: `"System"`)

* `System0` (value: `"System0"`)

* `System1` (value: `"System1"`)

* `System2` (value: `"System2"`)

* `System3` (value: `"System3"`)

* `System4` (value: `"System4"`)

* `System2L` (value: `"System2L"`)

* `System3L` (value: `"System3L"`)

* `System4L` (value: `"System4L"`)

* `Free` (value: `"Free"`)

* `Basic` (value: `"Basic"`)

* `S0` (value: `"S0"`)

* `S1` (value: `"S1"`)

* `S2` (value: `"S2"`)

* `S3` (value: `"S3"`)

* `S4` (value: `"S4"`)

* `S6` (value: `"S6"`)

* `S7` (value: `"S7"`)

* `S9` (value: `"S9"`)

* `S12` (value: `"S12"`)

* `P1` (value: `"P1"`)

* `P2` (value: `"P2"`)

* `P3` (value: `"P3"`)

* `P4` (value: `"P4"`)

* `P6` (value: `"P6"`)

* `P11` (value: `"P11"`)

* `P15` (value: `"P15"`)

* `PRS1` (value: `"PRS1"`)

* `PRS2` (value: `"PRS2"`)

* `PRS4` (value: `"PRS4"`)

* `PRS6` (value: `"PRS6"`)

* `DW100` (value: `"DW100"`)

* `DW200` (value: `"DW200"`)

* `DW300` (value: `"DW300"`)

* `DW400` (value: `"DW400"`)

* `DW500` (value: `"DW500"`)

* `DW600` (value: `"DW600"`)

* `DW1000` (value: `"DW1000"`)

* `DW1200` (value: `"DW1200"`)

* `DW1000c` (value: `"DW1000c"`)

* `DW1500` (value: `"DW1500"`)

* `DW1500c` (value: `"DW1500c"`)

* `DW2000` (value: `"DW2000"`)

* `DW2000c` (value: `"DW2000c"`)

* `DW3000` (value: `"DW3000"`)

* `DW2500c` (value: `"DW2500c"`)

* `DW3000c` (value: `"DW3000c"`)

* `DW6000` (value: `"DW6000"`)

* `DW5000c` (value: `"DW5000c"`)

* `DW6000c` (value: `"DW6000c"`)

* `DW7500c` (value: `"DW7500c"`)

* `DW10000c` (value: `"DW10000c"`)

* `DW15000c` (value: `"DW15000c"`)

* `DW30000c` (value: `"DW30000c"`)

* `DS100` (value: `"DS100"`)

* `DS200` (value: `"DS200"`)

* `DS300` (value: `"DS300"`)

* `DS400` (value: `"DS400"`)

* `DS500` (value: `"DS500"`)

* `DS600` (value: `"DS600"`)

* `DS1000` (value: `"DS1000"`)

* `DS1200` (value: `"DS1200"`)

* `DS1500` (value: `"DS1500"`)

* `DS2000` (value: `"DS2000"`)

* `ElasticPool` (value: `"ElasticPool"`)





## Enum: SampleNameEnum


* `AdventureWorksLT` (value: `"AdventureWorksLT"`)





## Enum: ServiceLevelObjectiveEnum


* `System` (value: `"System"`)

* `System0` (value: `"System0"`)

* `System1` (value: `"System1"`)

* `System2` (value: `"System2"`)

* `System3` (value: `"System3"`)

* `System4` (value: `"System4"`)

* `System2L` (value: `"System2L"`)

* `System3L` (value: `"System3L"`)

* `System4L` (value: `"System4L"`)

* `Free` (value: `"Free"`)

* `Basic` (value: `"Basic"`)

* `S0` (value: `"S0"`)

* `S1` (value: `"S1"`)

* `S2` (value: `"S2"`)

* `S3` (value: `"S3"`)

* `S4` (value: `"S4"`)

* `S6` (value: `"S6"`)

* `S7` (value: `"S7"`)

* `S9` (value: `"S9"`)

* `S12` (value: `"S12"`)

* `P1` (value: `"P1"`)

* `P2` (value: `"P2"`)

* `P3` (value: `"P3"`)

* `P4` (value: `"P4"`)

* `P6` (value: `"P6"`)

* `P11` (value: `"P11"`)

* `P15` (value: `"P15"`)

* `PRS1` (value: `"PRS1"`)

* `PRS2` (value: `"PRS2"`)

* `PRS4` (value: `"PRS4"`)

* `PRS6` (value: `"PRS6"`)

* `DW100` (value: `"DW100"`)

* `DW200` (value: `"DW200"`)

* `DW300` (value: `"DW300"`)

* `DW400` (value: `"DW400"`)

* `DW500` (value: `"DW500"`)

* `DW600` (value: `"DW600"`)

* `DW1000` (value: `"DW1000"`)

* `DW1200` (value: `"DW1200"`)

* `DW1000c` (value: `"DW1000c"`)

* `DW1500` (value: `"DW1500"`)

* `DW1500c` (value: `"DW1500c"`)

* `DW2000` (value: `"DW2000"`)

* `DW2000c` (value: `"DW2000c"`)

* `DW3000` (value: `"DW3000"`)

* `DW2500c` (value: `"DW2500c"`)

* `DW3000c` (value: `"DW3000c"`)

* `DW6000` (value: `"DW6000"`)

* `DW5000c` (value: `"DW5000c"`)

* `DW6000c` (value: `"DW6000c"`)

* `DW7500c` (value: `"DW7500c"`)

* `DW10000c` (value: `"DW10000c"`)

* `DW15000c` (value: `"DW15000c"`)

* `DW30000c` (value: `"DW30000c"`)

* `DS100` (value: `"DS100"`)

* `DS200` (value: `"DS200"`)

* `DS300` (value: `"DS300"`)

* `DS400` (value: `"DS400"`)

* `DS500` (value: `"DS500"`)

* `DS600` (value: `"DS600"`)

* `DS1000` (value: `"DS1000"`)

* `DS1200` (value: `"DS1200"`)

* `DS1500` (value: `"DS1500"`)

* `DS2000` (value: `"DS2000"`)

* `ElasticPool` (value: `"ElasticPool"`)




