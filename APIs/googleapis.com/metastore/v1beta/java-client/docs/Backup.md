

# Backup

The details of a backup resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time when the backup was started. |  [optional] [readonly] |
|**description** | **String** | The description of the backup. |  [optional] |
|**endTime** | **String** | Output only. The time when the backup finished creating. |  [optional] [readonly] |
|**name** | **String** | Immutable. The relative resource name of the backup, in the following form:projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id} |  [optional] |
|**restoringServices** | **List&lt;String&gt;** | Output only. Services that are restoring from the backup. |  [optional] [readonly] |
|**serviceRevision** | [**Service**](Service.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the backup. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| DELETING | &quot;DELETING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| FAILED | &quot;FAILED&quot; |
| RESTORING | &quot;RESTORING&quot; |



