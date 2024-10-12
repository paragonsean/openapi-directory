

# MigrationItemProperties

Migration item properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedOperations** | [**List&lt;AllowedOperationsEnum&gt;**](#List&lt;AllowedOperationsEnum&gt;) | The allowed operations on the migration item, based on the current migration state of the item. |  [optional] [readonly] |
|**currentJob** | [**CurrentJobDetails**](CurrentJobDetails.md) |  |  [optional] |
|**eventCorrelationId** | **String** | The correlation Id for events associated with this migration item. |  [optional] [readonly] |
|**health** | [**HealthEnum**](#HealthEnum) | The consolidated health. |  [optional] [readonly] |
|**healthErrors** | [**List&lt;HealthError&gt;**](HealthError.md) | The list of health errors. |  [optional] [readonly] |
|**lastTestMigrationStatus** | **String** | The status of the last test migration. |  [optional] [readonly] |
|**lastTestMigrationTime** | **OffsetDateTime** | The last test migration time. |  [optional] [readonly] |
|**machineName** | **String** | The on-premise virtual machine name. |  [optional] [readonly] |
|**migrationState** | [**MigrationStateEnum**](#MigrationStateEnum) | The migration status. |  [optional] [readonly] |
|**migrationStateDescription** | **String** | The migration state description. |  [optional] [readonly] |
|**policyFriendlyName** | **String** | The name of policy governing this item. |  [optional] [readonly] |
|**policyId** | **String** | The ARM Id of policy governing this item. |  [optional] [readonly] |
|**providerSpecificDetails** | [**MigrationProviderSpecificSettings**](MigrationProviderSpecificSettings.md) |  |  [optional] |
|**testMigrateState** | [**TestMigrateStateEnum**](#TestMigrateStateEnum) | The test migrate state. |  [optional] [readonly] |
|**testMigrateStateDescription** | **String** | The test migrate state description. |  [optional] [readonly] |



## Enum: List&lt;AllowedOperationsEnum&gt;

| Name | Value |
|---- | -----|
| DISABLE_MIGRATION | &quot;DisableMigration&quot; |
| TEST_MIGRATE | &quot;TestMigrate&quot; |
| TEST_MIGRATE_CLEANUP | &quot;TestMigrateCleanup&quot; |
| MIGRATE | &quot;Migrate&quot; |
| START_RESYNC | &quot;StartResync&quot; |



## Enum: HealthEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| NORMAL | &quot;Normal&quot; |
| WARNING | &quot;Warning&quot; |
| CRITICAL | &quot;Critical&quot; |



## Enum: MigrationStateEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| ENABLE_MIGRATION_IN_PROGRESS | &quot;EnableMigrationInProgress&quot; |
| ENABLE_MIGRATION_FAILED | &quot;EnableMigrationFailed&quot; |
| DISABLE_MIGRATION_IN_PROGRESS | &quot;DisableMigrationInProgress&quot; |
| DISABLE_MIGRATION_FAILED | &quot;DisableMigrationFailed&quot; |
| INITIAL_SEEDING_IN_PROGRESS | &quot;InitialSeedingInProgress&quot; |
| INITIAL_SEEDING_FAILED | &quot;InitialSeedingFailed&quot; |
| REPLICATING | &quot;Replicating&quot; |
| MIGRATION_IN_PROGRESS | &quot;MigrationInProgress&quot; |
| MIGRATION_SUCCEEDED | &quot;MigrationSucceeded&quot; |
| MIGRATION_FAILED | &quot;MigrationFailed&quot; |



## Enum: TestMigrateStateEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| TEST_MIGRATION_IN_PROGRESS | &quot;TestMigrationInProgress&quot; |
| TEST_MIGRATION_SUCCEEDED | &quot;TestMigrationSucceeded&quot; |
| TEST_MIGRATION_FAILED | &quot;TestMigrationFailed&quot; |
| TEST_MIGRATION_CLEANUP_IN_PROGRESS | &quot;TestMigrationCleanupInProgress&quot; |



