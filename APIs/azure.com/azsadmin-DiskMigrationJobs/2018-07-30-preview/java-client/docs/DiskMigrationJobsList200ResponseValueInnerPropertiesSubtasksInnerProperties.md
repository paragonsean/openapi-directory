

# DiskMigrationJobsList200ResponseValueInnerPropertiesSubtasksInnerProperties

Disk migration child task properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskId** | **String** | The id of disk. |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | The task end time. |  [optional] [readonly] |
|**migrationSubtaskStatus** | [**MigrationSubtaskStatusEnum**](#MigrationSubtaskStatusEnum) | Migration child task status. |  [optional] |
|**reason** | **String** | The reason of task failure. |  [optional] [readonly] |
|**sourceShare** | **String** | The source share of migration task. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | The task start time. |  [optional] [readonly] |
|**targetDiskStateForMigration** | [**TargetDiskStateForMigrationEnum**](#TargetDiskStateForMigrationEnum) | Disk State. |  [optional] |
|**targetShare** | **String** | The target share of migration task. |  [optional] [readonly] |



## Enum: MigrationSubtaskStatusEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;Undefined&quot; |
| RUNNING | &quot;Running&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |
| PENDING | &quot;Pending&quot; |
| SKIPPED | &quot;Skipped&quot; |



## Enum: TargetDiskStateForMigrationEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;Undefined&quot; |
| UNATTACHED | &quot;Unattached&quot; |
| ATTACHED | &quot;Attached&quot; |
| RESERVED | &quot;Reserved&quot; |
| ACTIVE_SAS | &quot;ActiveSAS&quot; |
| UNKNOWN | &quot;Unknown&quot; |
| ALL | &quot;All&quot; |
| RECOMMENDED | &quot;Recommended&quot; |
| OFFLINE_MIGRATION | &quot;OfflineMigration&quot; |
| ONLINE_MIGRATION | &quot;OnlineMigration&quot; |



