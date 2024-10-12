# AutomationManagement.JobCollectionItemProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **Date** | The creation time of the job. | [optional] [readonly] 
**endTime** | **Date** | The end time of the job. | [optional] [readonly] 
**jobId** | **String** | The id of the job. | [optional] [readonly] 
**lastModifiedTime** | **Date** | The last modified time of the job. | [optional] [readonly] 
**provisioningState** | **String** | The provisioning state of a resource. | [optional] [readonly] 
**runOn** | **String** | Specifies the runOn group name where the job was executed. | [optional] 
**runbook** | [**RunbookAssociationProperty**](RunbookAssociationProperty.md) |  | [optional] 
**startTime** | **Date** | The start time of the job. | [optional] [readonly] 
**status** | **String** | The status of the job. | [optional] [readonly] 



## Enum: StatusEnum


* `New` (value: `"New"`)

* `Activating` (value: `"Activating"`)

* `Running` (value: `"Running"`)

* `Completed` (value: `"Completed"`)

* `Failed` (value: `"Failed"`)

* `Stopped` (value: `"Stopped"`)

* `Blocked` (value: `"Blocked"`)

* `Suspended` (value: `"Suspended"`)

* `Disconnected` (value: `"Disconnected"`)

* `Suspending` (value: `"Suspending"`)

* `Stopping` (value: `"Stopping"`)

* `Resuming` (value: `"Resuming"`)

* `Removing` (value: `"Removing"`)




