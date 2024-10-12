

# DiskMigrationJobsList200ResponseValueInnerProperties

Disk migration job properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | The job creation time. |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | The job end time. |  [optional] [readonly] |
|**migrationId** | **String** | The disk migration id. |  [optional] |
|**startTime** | **OffsetDateTime** | The job start time. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Migration job status. |  [optional] |
|**subtasks** | [**List&lt;DiskMigrationJobsList200ResponseValueInnerPropertiesSubtasksInner&gt;**](DiskMigrationJobsList200ResponseValueInnerPropertiesSubtasksInner.md) | List of disk migration tasks. |  [optional] |
|**targetShare** | **String** | The target share of migration job. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;Undefined&quot; |
| RUNNING | &quot;Running&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |
| PENDING | &quot;Pending&quot; |



