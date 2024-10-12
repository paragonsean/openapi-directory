# AutomationManagement.DscCompilationJobProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**DscConfigurationAssociationProperty**](DscConfigurationAssociationProperty.md) |  | [optional] 
**creationTime** | **Date** | Gets the creation time of the job. | [optional] [readonly] 
**endTime** | **Date** | Gets the end time of the job. | [optional] [readonly] 
**exception** | **String** | Gets the exception of the job. | [optional] [readonly] 
**jobId** | **String** | Gets the id of the job. | [optional] [readonly] 
**lastModifiedTime** | **Date** | Gets the last modified time of the job. | [optional] [readonly] 
**lastStatusModifiedTime** | **Date** | Gets the last status modified time of the job. | [optional] [readonly] 
**parameters** | **{String: String}** | Gets or sets the parameters of the job. | [optional] 
**provisioningState** | [**JobProvisioningStateProperty**](JobProvisioningStateProperty.md) |  | [optional] 
**runOn** | **String** | Gets or sets the runOn which specifies the group name where the job is to be executed. | [optional] 
**startTime** | **Date** | Gets the start time of the job. | [optional] [readonly] 
**startedBy** | **String** | Gets the compilation job started by. | [optional] [readonly] 
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




