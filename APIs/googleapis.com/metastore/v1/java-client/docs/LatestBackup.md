

# LatestBackup

The details of the latest scheduled backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupId** | **String** | Output only. The ID of an in-progress scheduled backup. Empty if no backup is in progress. |  [optional] [readonly] |
|**duration** | **String** | Output only. The duration of the backup completion. |  [optional] [readonly] |
|**startTime** | **String** | Output only. The time when the backup was started. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the backup. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



