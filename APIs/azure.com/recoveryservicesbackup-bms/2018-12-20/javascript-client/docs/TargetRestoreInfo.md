# RecoveryServicesBackupClient.TargetRestoreInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerId** | **String** | Resource Id name of the container in which Target DataBase resides | [optional] 
**databaseName** | **String** | Database name InstanceName/DataBaseName for SQL or System/DbName for SAP Hana | [optional] 
**overwriteOption** | **String** | Can Overwrite if Target DataBase already exists | [optional] 
**targetDirectoryMapping** | **{String: String}** | This will contain the target folder mapping for the Full/Diff/Log/Incremental pits. | [optional] 



## Enum: OverwriteOptionEnum


* `Invalid` (value: `"Invalid"`)

* `FailOnConflict` (value: `"FailOnConflict"`)

* `Overwrite` (value: `"Overwrite"`)




