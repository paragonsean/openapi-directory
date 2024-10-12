# DataprocMetastoreApi.Backup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when the backup was started. | [optional] [readonly] 
**description** | **String** | The description of the backup. | [optional] 
**endTime** | **String** | Output only. The time when the backup finished creating. | [optional] [readonly] 
**name** | **String** | Immutable. The relative resource name of the backup, in the following form:projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id} | [optional] 
**restoringServices** | **[String]** | Output only. Services that are restoring from the backup. | [optional] [readonly] 
**serviceRevision** | [**Service**](Service.md) |  | [optional] 
**state** | **String** | Output only. The current state of the backup. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `DELETING` (value: `"DELETING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `FAILED` (value: `"FAILED"`)

* `RESTORING` (value: `"RESTORING"`)




