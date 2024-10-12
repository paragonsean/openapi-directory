# SqlManagementClient.RestorePointProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earliestRestoreDate** | **Date** | The earliest time to which this database can be restored | [optional] [readonly] 
**restorePointCreationDate** | **Date** | The time the backup was taken | [optional] [readonly] 
**restorePointLabel** | **String** | The label of restore point for backup request by user | [optional] [readonly] 
**restorePointType** | **String** | The type of restore point | [optional] [readonly] 



## Enum: RestorePointTypeEnum


* `CONTINUOUS` (value: `"CONTINUOUS"`)

* `DISCRETE` (value: `"DISCRETE"`)




