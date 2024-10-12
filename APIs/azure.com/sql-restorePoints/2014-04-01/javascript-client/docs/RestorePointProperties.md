# AzureSqlDatabaseBackup.RestorePointProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earliestRestoreDate** | **Date** | Earliest restore time (ISO8601 format). Populated when restorePointType &#x3D; DISCRETE. Null otherwise. | [optional] [readonly] 
**restorePointCreationDate** | **Date** | Restore point creation time (ISO8601 format). Populated when restorePointType &#x3D; CONTINUOUS. Null otherwise. | [optional] [readonly] 
**restorePointType** | **String** | The restore point type of the database restore point. | [optional] [readonly] 



## Enum: RestorePointTypeEnum


* `DISCRETE` (value: `"DISCRETE"`)

* `CONTINUOUS` (value: `"CONTINUOUS"`)




