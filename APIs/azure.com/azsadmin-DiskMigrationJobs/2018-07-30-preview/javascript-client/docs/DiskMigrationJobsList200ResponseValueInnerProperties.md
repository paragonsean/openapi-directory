# ComputeDiskAdminManagementClient.DiskMigrationJobsList200ResponseValueInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **Date** | The job creation time. | [optional] [readonly] 
**endTime** | **Date** | The job end time. | [optional] [readonly] 
**migrationId** | **String** | The disk migration id. | [optional] 
**startTime** | **Date** | The job start time. | [optional] [readonly] 
**status** | **String** | Migration job status. | [optional] 
**subtasks** | [**[DiskMigrationJobsList200ResponseValueInnerPropertiesSubtasksInner]**](DiskMigrationJobsList200ResponseValueInnerPropertiesSubtasksInner.md) | List of disk migration tasks. | [optional] 
**targetShare** | **String** | The target share of migration job. | [optional] [readonly] 



## Enum: StatusEnum


* `Undefined` (value: `"Undefined"`)

* `Running` (value: `"Running"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)

* `Pending` (value: `"Pending"`)




