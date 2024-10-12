# AutomationManagement.JobProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **Date** | Gets or sets the creation time of the job. | [optional] 
**endTime** | **Date** | Gets or sets the end time of the job. | [optional] 
**exception** | **String** | Gets or sets the exception of the job. | [optional] 
**jobId** | **String** | Gets or sets the id of the job. | [optional] 
**lastModifiedTime** | **Date** | Gets or sets the last modified time of the job. | [optional] 
**lastStatusModifiedTime** | **Date** | Gets or sets the last status modified time of the job. | [optional] 
**parameters** | **{String: String}** | Gets or sets the parameters of the job. | [optional] 
**provisioningState** | [**JobProvisioningStateProperty**](JobProvisioningStateProperty.md) |  | [optional] 
**runOn** | **String** | Gets or sets the runOn which specifies the group name where the job is to be executed. | [optional] 
**runbook** | [**RunbookAssociationProperty**](RunbookAssociationProperty.md) |  | [optional] 
**startTime** | **Date** | Gets or sets the start time of the job. | [optional] 
**startedBy** | **String** | Gets or sets the job started by. | [optional] 
**status** | **String** | Gets or sets the status of the job. | [optional] 
**statusDetails** | **String** | Gets or sets the status details of the job. | [optional] 



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




