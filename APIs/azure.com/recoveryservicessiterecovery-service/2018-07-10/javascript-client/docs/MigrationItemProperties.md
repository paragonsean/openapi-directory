# SiteRecoveryManagementClient.MigrationItemProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedOperations** | **[String]** | The allowed operations on the migration item, based on the current migration state of the item. | [optional] [readonly] 
**currentJob** | [**CurrentJobDetails**](CurrentJobDetails.md) |  | [optional] 
**health** | **String** | The consolidated health. | [optional] [readonly] 
**healthErrors** | [**[HealthError]**](HealthError.md) | The list of health errors. | [optional] [readonly] 
**machineName** | **String** | The on-premise virtual machine name. | [optional] [readonly] 
**migrationState** | **String** | The migration status. | [optional] [readonly] 
**migrationStateDescription** | **String** | The migration state description. | [optional] [readonly] 
**policyFriendlyName** | **String** | The name of policy governing this item. | [optional] [readonly] 
**policyId** | **String** | The ARM Id of policy governing this item. | [optional] [readonly] 
**providerSpecificDetails** | [**MigrationProviderSpecificSettings**](MigrationProviderSpecificSettings.md) |  | [optional] 
**recoveryServicesProviderId** | **String** | The recovery services provider ARM Id. | [optional] [readonly] 
**testMigrateState** | **String** | The test migrate state. | [optional] [readonly] 
**testMigrateStateDescription** | **String** | The test migrate state description. | [optional] [readonly] 



## Enum: [AllowedOperationsEnum]


* `DisableMigration` (value: `"DisableMigration"`)

* `TestMigrate` (value: `"TestMigrate"`)

* `TestMigrateCleanup` (value: `"TestMigrateCleanup"`)

* `Migrate` (value: `"Migrate"`)





## Enum: MigrationStateEnum


* `None` (value: `"None"`)

* `EnableMigrationInProgress` (value: `"EnableMigrationInProgress"`)

* `EnableMigrationFailed` (value: `"EnableMigrationFailed"`)

* `DisableMigrationInProgress` (value: `"DisableMigrationInProgress"`)

* `DisableMigrationFailed` (value: `"DisableMigrationFailed"`)

* `InitialSeedingInProgress` (value: `"InitialSeedingInProgress"`)

* `InitialSeedingFailed` (value: `"InitialSeedingFailed"`)

* `Replicating` (value: `"Replicating"`)

* `MigrationInProgress` (value: `"MigrationInProgress"`)

* `MigrationSucceeded` (value: `"MigrationSucceeded"`)

* `MigrationFailed` (value: `"MigrationFailed"`)





## Enum: TestMigrateStateEnum


* `None` (value: `"None"`)

* `TestMigrationInProgress` (value: `"TestMigrationInProgress"`)

* `TestMigrationSucceeded` (value: `"TestMigrationSucceeded"`)

* `TestMigrationFailed` (value: `"TestMigrationFailed"`)

* `TestMigrationCleanupInProgress` (value: `"TestMigrationCleanupInProgress"`)




