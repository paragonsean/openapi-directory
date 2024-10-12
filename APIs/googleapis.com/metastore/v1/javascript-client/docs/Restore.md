# DataprocMetastoreApi.Restore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup** | **String** | Output only. The relative resource name of the metastore service backup to restore from, in the following form:projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}. | [optional] [readonly] 
**backupLocation** | **String** | Optional. A Cloud Storage URI specifying where the backup artifacts are stored, in the format gs:///. | [optional] 
**details** | **String** | Output only. The restore details containing the revision of the service to be restored to, in format of JSON. | [optional] [readonly] 
**endTime** | **String** | Output only. The time when the restore ended. | [optional] [readonly] 
**startTime** | **String** | Output only. The time when the restore started. | [optional] [readonly] 
**state** | **String** | Output only. The current state of the restore. | [optional] [readonly] 
**type** | **String** | Output only. The type of restore. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)





## Enum: TypeEnum


* `RESTORE_TYPE_UNSPECIFIED` (value: `"RESTORE_TYPE_UNSPECIFIED"`)

* `FULL` (value: `"FULL"`)

* `METADATA_ONLY` (value: `"METADATA_ONLY"`)




