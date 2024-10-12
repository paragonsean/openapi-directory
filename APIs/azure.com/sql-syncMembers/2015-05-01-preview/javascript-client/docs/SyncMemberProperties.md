# SqlManagementClient.SyncMemberProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databaseName** | **String** | Database name of the member database in the sync member. | [optional] 
**databaseType** | **String** | Database type of the sync member. | [optional] 
**password** | **String** | Password of the member database in the sync member. | [optional] 
**serverName** | **String** | Server name of the member database in the sync member | [optional] 
**sqlServerDatabaseId** | **String** | SQL Server database id of the sync member. | [optional] 
**syncAgentId** | **String** | ARM resource id of the sync agent in the sync member. | [optional] 
**syncDirection** | **String** | Sync direction of the sync member. | [optional] 
**syncState** | **String** | Sync state of the sync member. | [optional] [readonly] 
**userName** | **String** | User name of the member database in the sync member. | [optional] 



## Enum: DatabaseTypeEnum


* `AzureSqlDatabase` (value: `"AzureSqlDatabase"`)

* `SqlServerDatabase` (value: `"SqlServerDatabase"`)





## Enum: SyncDirectionEnum


* `Bidirectional` (value: `"Bidirectional"`)

* `OneWayMemberToHub` (value: `"OneWayMemberToHub"`)

* `OneWayHubToMember` (value: `"OneWayHubToMember"`)





## Enum: SyncStateEnum


* `SyncInProgress` (value: `"SyncInProgress"`)

* `SyncSucceeded` (value: `"SyncSucceeded"`)

* `SyncFailed` (value: `"SyncFailed"`)

* `DisabledTombstoneCleanup` (value: `"DisabledTombstoneCleanup"`)

* `DisabledBackupRestore` (value: `"DisabledBackupRestore"`)

* `SyncSucceededWithWarnings` (value: `"SyncSucceededWithWarnings"`)

* `SyncCancelling` (value: `"SyncCancelling"`)

* `SyncCancelled` (value: `"SyncCancelled"`)

* `UnProvisioned` (value: `"UnProvisioned"`)

* `Provisioning` (value: `"Provisioning"`)

* `Provisioned` (value: `"Provisioned"`)

* `ProvisionFailed` (value: `"ProvisionFailed"`)

* `DeProvisioning` (value: `"DeProvisioning"`)

* `DeProvisioned` (value: `"DeProvisioned"`)

* `DeProvisionFailed` (value: `"DeProvisionFailed"`)

* `Reprovisioning` (value: `"Reprovisioning"`)

* `ReprovisionFailed` (value: `"ReprovisionFailed"`)

* `UnReprovisioned` (value: `"UnReprovisioned"`)




