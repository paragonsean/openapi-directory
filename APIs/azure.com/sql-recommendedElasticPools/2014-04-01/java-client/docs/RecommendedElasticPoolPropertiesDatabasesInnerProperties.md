

# RecommendedElasticPoolPropertiesDatabasesInnerProperties

Represents the properties of a database.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collation** | **String** | The collation of the database. If createMode is not Default, this value is ignored. |  [optional] |
|**containmentState** | **Long** | The containment state of the database. |  [optional] [readonly] |
|**createMode** | [**CreateModeEnum**](#CreateModeEnum) | Specifies the mode of database creation.  Default: regular database creation.  Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database.  OnlineSecondary/NonReadableSecondary: creates a database as a (readable or nonreadable) secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database.  PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified.  Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore.  Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database&#39;s original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time.  RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID.  Copy, NonReadableSecondary, OnlineSecondary and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition. |  [optional] |
|**creationDate** | **OffsetDateTime** | The creation date of the database (ISO8601 format). |  [optional] [readonly] |
|**currentServiceObjectiveId** | **UUID** | The current service level objective ID of the database. This is the ID of the service level objective that is currently active. |  [optional] [readonly] |
|**databaseId** | **UUID** | The ID of the database. |  [optional] [readonly] |
|**defaultSecondaryLocation** | **String** | The default secondary region for this database. |  [optional] [readonly] |
|**earliestRestoreDate** | **OffsetDateTime** | This records the earliest start date and time that restore is available for this database (ISO8601 format). |  [optional] [readonly] |
|**edition** | [**EditionEnum**](#EditionEnum) | The edition of the database. The DatabaseEditions enumeration contains all the valid editions. If createMode is NonReadableSecondary or OnlineSecondary, this value is ignored.    The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the &#x60;Capabilities_ListByLocation&#x60; REST API or one of the following commands:    &#x60;&#x60;&#x60;azurecli  az sql db list-editions -l &lt;location&gt; -o table  &#x60;&#x60;&#x60;&#x60;    &#x60;&#x60;&#x60;powershell  Get-AzSqlServerServiceObjective -Location &lt;location&gt;  &#x60;&#x60;&#x60;&#x60;   |  [optional] |
|**elasticPoolName** | **String** | The name of the elastic pool the database is in. If elasticPoolName and requestedServiceObjectiveName are both updated, the value of requestedServiceObjectiveName is ignored. Not supported for DataWarehouse edition. |  [optional] |
|**failoverGroupId** | **String** | The resource identifier of the failover group containing this database. |  [optional] [readonly] |
|**maxSizeBytes** | **String** | The max size of the database expressed in bytes. If createMode is not Default, this value is ignored. To see possible values, query the capabilities API (/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationID}/capabilities) referred to by operationId: \&quot;Capabilities_ListByLocation.\&quot; |  [optional] |
|**readScale** | [**ReadScaleEnum**](#ReadScaleEnum) | Conditional. If the database is a geo-secondary, readScale indicates whether read-only connections are allowed to this database or not. Not supported for DataWarehouse edition. |  [optional] |
|**recommendedIndex** | [**List&lt;RecommendedElasticPoolPropertiesDatabasesInnerPropertiesRecommendedIndexInner&gt;**](RecommendedElasticPoolPropertiesDatabasesInnerPropertiesRecommendedIndexInner.md) | The recommended indices for this database. |  [optional] [readonly] |
|**recoveryServicesRecoveryPointResourceId** | **String** | Conditional. If createMode is RestoreLongTermRetentionBackup, then this value is required. Specifies the resource ID of the recovery point to restore from. |  [optional] |
|**requestedServiceObjectiveId** | **UUID** | The configured service level objective ID of the database. This is the service level objective that is in the process of being applied to the database. Once successfully updated, it will match the value of currentServiceObjectiveId property. If requestedServiceObjectiveId and requestedServiceObjectiveName are both updated, the value of requestedServiceObjectiveId overrides the value of requestedServiceObjectiveName.    The list of SKUs may vary by region and support offer. To determine the service objective ids that are available to your subscription in an Azure region, use the &#x60;Capabilities_ListByLocation&#x60; REST API. |  [optional] |
|**requestedServiceObjectiveName** | [**RequestedServiceObjectiveNameEnum**](#RequestedServiceObjectiveNameEnum) | The name of the configured service level objective of the database. This is the service level objective that is in the process of being applied to the database. Once successfully updated, it will match the value of serviceLevelObjective property.     The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the &#x60;Capabilities_ListByLocation&#x60; REST API or one of the following commands:    &#x60;&#x60;&#x60;azurecli  az sql db list-editions -l &lt;location&gt; -o table  &#x60;&#x60;&#x60;&#x60;    &#x60;&#x60;&#x60;powershell  Get-AzSqlServerServiceObjective -Location &lt;location&gt;  &#x60;&#x60;&#x60;&#x60;   |  [optional] |
|**restorePointInTime** | **OffsetDateTime** | Conditional. If createMode is PointInTimeRestore, this value is required. If createMode is Restore, this value is optional. Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. Must be greater than or equal to the source database&#39;s earliestRestoreDate value. |  [optional] |
|**sampleName** | [**SampleNameEnum**](#SampleNameEnum) | Indicates the name of the sample schema to apply when creating this database. If createMode is not Default, this value is ignored. Not supported for DataWarehouse edition. |  [optional] |
|**serviceLevelObjective** | [**ServiceLevelObjectiveEnum**](#ServiceLevelObjectiveEnum) | The current service level objective of the database. |  [optional] [readonly] |
|**serviceTierAdvisors** | [**List&lt;RecommendedElasticPoolPropertiesDatabasesInnerPropertiesServiceTierAdvisorsInner&gt;**](RecommendedElasticPoolPropertiesDatabasesInnerPropertiesServiceTierAdvisorsInner.md) | The list of service tier advisors for this database. Expanded property |  [optional] [readonly] |
|**sourceDatabaseDeletionDate** | **OffsetDateTime** | Conditional. If createMode is Restore and sourceDatabaseId is the deleted database&#39;s original resource id when it existed (as opposed to its current restorable dropped database id), then this value is required. Specifies the time that the database was deleted. |  [optional] |
|**sourceDatabaseId** | **String** | Conditional. If createMode is Copy, NonReadableSecondary, OnlineSecondary, PointInTimeRestore, Recovery, or Restore, then this value is required. Specifies the resource ID of the source database. If createMode is NonReadableSecondary or OnlineSecondary, the name of the source database must be the same as the new database being created. |  [optional] |
|**status** | **String** | The status of the database. |  [optional] [readonly] |
|**transparentDataEncryption** | [**List&lt;RecommendedElasticPoolPropertiesDatabasesInnerPropertiesTransparentDataEncryptionInner&gt;**](RecommendedElasticPoolPropertiesDatabasesInnerPropertiesTransparentDataEncryptionInner.md) | The transparent data encryption info for this database. |  [optional] [readonly] |
|**zoneRedundant** | **Boolean** | Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. |  [optional] |



## Enum: CreateModeEnum

| Name | Value |
|---- | -----|
| COPY | &quot;Copy&quot; |
| DEFAULT | &quot;Default&quot; |
| NON_READABLE_SECONDARY | &quot;NonReadableSecondary&quot; |
| ONLINE_SECONDARY | &quot;OnlineSecondary&quot; |
| POINT_IN_TIME_RESTORE | &quot;PointInTimeRestore&quot; |
| RECOVERY | &quot;Recovery&quot; |
| RESTORE | &quot;Restore&quot; |
| RESTORE_LONG_TERM_RETENTION_BACKUP | &quot;RestoreLongTermRetentionBackup&quot; |



## Enum: EditionEnum

| Name | Value |
|---- | -----|
| WEB | &quot;Web&quot; |
| BUSINESS | &quot;Business&quot; |
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| PREMIUM_RS | &quot;PremiumRS&quot; |
| FREE | &quot;Free&quot; |
| STRETCH | &quot;Stretch&quot; |
| DATA_WAREHOUSE | &quot;DataWarehouse&quot; |
| SYSTEM | &quot;System&quot; |
| SYSTEM2 | &quot;System2&quot; |
| GENERAL_PURPOSE | &quot;GeneralPurpose&quot; |
| BUSINESS_CRITICAL | &quot;BusinessCritical&quot; |
| HYPERSCALE | &quot;Hyperscale&quot; |



## Enum: ReadScaleEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: RequestedServiceObjectiveNameEnum

| Name | Value |
|---- | -----|
| SYSTEM | &quot;System&quot; |
| SYSTEM0 | &quot;System0&quot; |
| SYSTEM1 | &quot;System1&quot; |
| SYSTEM2 | &quot;System2&quot; |
| SYSTEM3 | &quot;System3&quot; |
| SYSTEM4 | &quot;System4&quot; |
| SYSTEM2_L | &quot;System2L&quot; |
| SYSTEM3_L | &quot;System3L&quot; |
| SYSTEM4_L | &quot;System4L&quot; |
| FREE | &quot;Free&quot; |
| BASIC | &quot;Basic&quot; |
| S0 | &quot;S0&quot; |
| S1 | &quot;S1&quot; |
| S2 | &quot;S2&quot; |
| S3 | &quot;S3&quot; |
| S4 | &quot;S4&quot; |
| S6 | &quot;S6&quot; |
| S7 | &quot;S7&quot; |
| S9 | &quot;S9&quot; |
| S12 | &quot;S12&quot; |
| P1 | &quot;P1&quot; |
| P2 | &quot;P2&quot; |
| P3 | &quot;P3&quot; |
| P4 | &quot;P4&quot; |
| P6 | &quot;P6&quot; |
| P11 | &quot;P11&quot; |
| P15 | &quot;P15&quot; |
| PRS1 | &quot;PRS1&quot; |
| PRS2 | &quot;PRS2&quot; |
| PRS4 | &quot;PRS4&quot; |
| PRS6 | &quot;PRS6&quot; |
| DW100 | &quot;DW100&quot; |
| DW200 | &quot;DW200&quot; |
| DW300 | &quot;DW300&quot; |
| DW400 | &quot;DW400&quot; |
| DW500 | &quot;DW500&quot; |
| DW600 | &quot;DW600&quot; |
| DW1000 | &quot;DW1000&quot; |
| DW1200 | &quot;DW1200&quot; |
| DW1000C | &quot;DW1000c&quot; |
| DW1500 | &quot;DW1500&quot; |
| DW1500C | &quot;DW1500c&quot; |
| DW2000 | &quot;DW2000&quot; |
| DW2000C | &quot;DW2000c&quot; |
| DW3000 | &quot;DW3000&quot; |
| DW2500C | &quot;DW2500c&quot; |
| DW3000C | &quot;DW3000c&quot; |
| DW6000 | &quot;DW6000&quot; |
| DW5000C | &quot;DW5000c&quot; |
| DW6000C | &quot;DW6000c&quot; |
| DW7500C | &quot;DW7500c&quot; |
| DW10000C | &quot;DW10000c&quot; |
| DW15000C | &quot;DW15000c&quot; |
| DW30000C | &quot;DW30000c&quot; |
| DS100 | &quot;DS100&quot; |
| DS200 | &quot;DS200&quot; |
| DS300 | &quot;DS300&quot; |
| DS400 | &quot;DS400&quot; |
| DS500 | &quot;DS500&quot; |
| DS600 | &quot;DS600&quot; |
| DS1000 | &quot;DS1000&quot; |
| DS1200 | &quot;DS1200&quot; |
| DS1500 | &quot;DS1500&quot; |
| DS2000 | &quot;DS2000&quot; |
| ELASTIC_POOL | &quot;ElasticPool&quot; |



## Enum: SampleNameEnum

| Name | Value |
|---- | -----|
| ADVENTURE_WORKS_LT | &quot;AdventureWorksLT&quot; |



## Enum: ServiceLevelObjectiveEnum

| Name | Value |
|---- | -----|
| SYSTEM | &quot;System&quot; |
| SYSTEM0 | &quot;System0&quot; |
| SYSTEM1 | &quot;System1&quot; |
| SYSTEM2 | &quot;System2&quot; |
| SYSTEM3 | &quot;System3&quot; |
| SYSTEM4 | &quot;System4&quot; |
| SYSTEM2_L | &quot;System2L&quot; |
| SYSTEM3_L | &quot;System3L&quot; |
| SYSTEM4_L | &quot;System4L&quot; |
| FREE | &quot;Free&quot; |
| BASIC | &quot;Basic&quot; |
| S0 | &quot;S0&quot; |
| S1 | &quot;S1&quot; |
| S2 | &quot;S2&quot; |
| S3 | &quot;S3&quot; |
| S4 | &quot;S4&quot; |
| S6 | &quot;S6&quot; |
| S7 | &quot;S7&quot; |
| S9 | &quot;S9&quot; |
| S12 | &quot;S12&quot; |
| P1 | &quot;P1&quot; |
| P2 | &quot;P2&quot; |
| P3 | &quot;P3&quot; |
| P4 | &quot;P4&quot; |
| P6 | &quot;P6&quot; |
| P11 | &quot;P11&quot; |
| P15 | &quot;P15&quot; |
| PRS1 | &quot;PRS1&quot; |
| PRS2 | &quot;PRS2&quot; |
| PRS4 | &quot;PRS4&quot; |
| PRS6 | &quot;PRS6&quot; |
| DW100 | &quot;DW100&quot; |
| DW200 | &quot;DW200&quot; |
| DW300 | &quot;DW300&quot; |
| DW400 | &quot;DW400&quot; |
| DW500 | &quot;DW500&quot; |
| DW600 | &quot;DW600&quot; |
| DW1000 | &quot;DW1000&quot; |
| DW1200 | &quot;DW1200&quot; |
| DW1000C | &quot;DW1000c&quot; |
| DW1500 | &quot;DW1500&quot; |
| DW1500C | &quot;DW1500c&quot; |
| DW2000 | &quot;DW2000&quot; |
| DW2000C | &quot;DW2000c&quot; |
| DW3000 | &quot;DW3000&quot; |
| DW2500C | &quot;DW2500c&quot; |
| DW3000C | &quot;DW3000c&quot; |
| DW6000 | &quot;DW6000&quot; |
| DW5000C | &quot;DW5000c&quot; |
| DW6000C | &quot;DW6000c&quot; |
| DW7500C | &quot;DW7500c&quot; |
| DW10000C | &quot;DW10000c&quot; |
| DW15000C | &quot;DW15000c&quot; |
| DW30000C | &quot;DW30000c&quot; |
| DS100 | &quot;DS100&quot; |
| DS200 | &quot;DS200&quot; |
| DS300 | &quot;DS300&quot; |
| DS400 | &quot;DS400&quot; |
| DS500 | &quot;DS500&quot; |
| DS600 | &quot;DS600&quot; |
| DS1000 | &quot;DS1000&quot; |
| DS1200 | &quot;DS1200&quot; |
| DS1500 | &quot;DS1500&quot; |
| DS2000 | &quot;DS2000&quot; |
| ELASTIC_POOL | &quot;ElasticPool&quot; |



