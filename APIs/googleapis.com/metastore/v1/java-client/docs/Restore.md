

# Restore

The details of a metadata restore operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backup** | **String** | Output only. The relative resource name of the metastore service backup to restore from, in the following form:projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}. |  [optional] [readonly] |
|**backupLocation** | **String** | Optional. A Cloud Storage URI specifying where the backup artifacts are stored, in the format gs:///. |  [optional] |
|**details** | **String** | Output only. The restore details containing the revision of the service to be restored to, in format of JSON. |  [optional] [readonly] |
|**endTime** | **String** | Output only. The time when the restore ended. |  [optional] [readonly] |
|**startTime** | **String** | Output only. The time when the restore started. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the restore. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type of restore. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RESTORE_TYPE_UNSPECIFIED | &quot;RESTORE_TYPE_UNSPECIFIED&quot; |
| FULL | &quot;FULL&quot; |
| METADATA_ONLY | &quot;METADATA_ONLY&quot; |



