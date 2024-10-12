# ComputeDiskAdminManagementClient.MigrationSubTaskProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskId** | **String** | The id of disk. | [optional] [readonly] 
**endTime** | **Date** | The task end time. | [optional] [readonly] 
**migrationSubtaskStatus** | **String** | Migration child task status. | [optional] 
**reason** | **String** | The reason of task failure. | [optional] [readonly] 
**sourceShare** | **String** | The source share of migration task. | [optional] [readonly] 
**startTime** | **Date** | The task start time. | [optional] [readonly] 
**targetDiskStateForMigration** | **String** | Disk State. | [optional] 
**targetShare** | **String** | The target share of migration task. | [optional] [readonly] 



## Enum: MigrationSubtaskStatusEnum


* `Undefined` (value: `"Undefined"`)

* `Running` (value: `"Running"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)

* `Pending` (value: `"Pending"`)

* `Skipped` (value: `"Skipped"`)





## Enum: TargetDiskStateForMigrationEnum


* `Undefined` (value: `"Undefined"`)

* `Unattached` (value: `"Unattached"`)

* `Attached` (value: `"Attached"`)

* `Reserved` (value: `"Reserved"`)

* `ActiveSAS` (value: `"ActiveSAS"`)

* `Unknown` (value: `"Unknown"`)

* `All` (value: `"All"`)

* `Recommended` (value: `"Recommended"`)

* `OfflineMigration` (value: `"OfflineMigration"`)

* `OnlineMigration` (value: `"OnlineMigration"`)




