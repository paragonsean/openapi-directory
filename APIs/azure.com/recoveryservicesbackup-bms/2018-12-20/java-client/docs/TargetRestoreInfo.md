

# TargetRestoreInfo

Details about target workload during restore operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerId** | **String** | Resource Id name of the container in which Target DataBase resides |  [optional] |
|**databaseName** | **String** | Database name InstanceName/DataBaseName for SQL or System/DbName for SAP Hana |  [optional] |
|**overwriteOption** | [**OverwriteOptionEnum**](#OverwriteOptionEnum) | Can Overwrite if Target DataBase already exists |  [optional] |
|**targetDirectoryMapping** | **Map&lt;String, String&gt;** | This will contain the target folder mapping for the Full/Diff/Log/Incremental pits. |  [optional] |



## Enum: OverwriteOptionEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| FAIL_ON_CONFLICT | &quot;FailOnConflict&quot; |
| OVERWRITE | &quot;Overwrite&quot; |



