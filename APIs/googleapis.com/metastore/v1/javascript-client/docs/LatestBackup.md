# DataprocMetastoreApi.LatestBackup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupId** | **String** | Output only. The ID of an in-progress scheduled backup. Empty if no backup is in progress. | [optional] [readonly] 
**duration** | **String** | Output only. The duration of the backup completion. | [optional] [readonly] 
**startTime** | **String** | Output only. The time when the backup was started. | [optional] [readonly] 
**state** | **String** | Output only. The current state of the backup. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)




