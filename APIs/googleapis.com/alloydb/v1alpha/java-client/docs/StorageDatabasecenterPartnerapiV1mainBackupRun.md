

# StorageDatabasecenterPartnerapiV1mainBackupRun

A backup run.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | The time the backup operation completed. REQUIRED |  [optional] |
|**error** | [**StorageDatabasecenterPartnerapiV1mainOperationError**](StorageDatabasecenterPartnerapiV1mainOperationError.md) |  |  [optional] |
|**startTime** | **String** | The time the backup operation started. REQUIRED |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of this run. REQUIRED |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| SUCCESSFUL | &quot;SUCCESSFUL&quot; |
| FAILED | &quot;FAILED&quot; |



