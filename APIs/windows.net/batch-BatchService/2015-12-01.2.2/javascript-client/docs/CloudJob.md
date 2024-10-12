# BatchService.CloudJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commonEnvironmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) | Gets or sets the list of common environment variable settings.  These environment variables are set for all tasks in the job (including the Job Manager, Job Preparation and Job Release tasks). | [optional] 
**constraints** | [**JobConstraints**](JobConstraints.md) |  | [optional] 
**creationTime** | **Date** | Gets or sets the creation time of the job. | [optional] 
**displayName** | **String** | Gets or sets the display name for the job. | [optional] 
**eTag** | **String** | Gets or sets the ETag of the job. | [optional] 
**executionInfo** | [**JobExecutionInformation**](JobExecutionInformation.md) |  | [optional] 
**id** | **String** | Gets or sets a string that uniquely identifies the job within the account. The id can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. It is common to use a GUID for the id. | [optional] 
**jobManagerTask** | [**JobManagerTask**](JobManagerTask.md) |  | [optional] 
**jobPreparationTask** | [**JobPreparationTask**](JobPreparationTask.md) |  | [optional] 
**jobReleaseTask** | [**JobReleaseTask**](JobReleaseTask.md) |  | [optional] 
**lastModified** | **Date** | Gets or sets the last modified time of the job. | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | Gets or sets a list of name-value pairs associated with the job as metadata. | [optional] 
**poolInfo** | [**PoolInformation**](PoolInformation.md) |  | [optional] 
**previousState** | **String** | Gets or sets the previous state of the job. This property is not set if the job is in its initial Active state. | [optional] 
**previousStateTransitionTime** | **Date** | Gets or sets the time at which the job entered its previous state. This property is not set if the job is in its initial Active state. | [optional] 
**priority** | **Number** | Gets or sets the priority of the job. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. | [optional] 
**state** | **String** | Gets or sets the current state of the job. | [optional] 
**stateTransitionTime** | **Date** | Gets or sets the time at which the job entered its current state. | [optional] 
**stats** | [**JobStatistics**](JobStatistics.md) |  | [optional] 
**url** | **String** | Gets or sets the URL of the job. | [optional] 
**usesTaskDependencies** | **Boolean** | Gets or sets the flag that determines if this job will use tasks with dependencies. | [optional] 



## Enum: PreviousStateEnum


* `active` (value: `"active"`)

* `disabling` (value: `"disabling"`)

* `disabled` (value: `"disabled"`)

* `enabling` (value: `"enabling"`)

* `terminating` (value: `"terminating"`)

* `completed` (value: `"completed"`)

* `deleting` (value: `"deleting"`)





## Enum: StateEnum


* `active` (value: `"active"`)

* `disabling` (value: `"disabling"`)

* `disabled` (value: `"disabled"`)

* `enabling` (value: `"enabling"`)

* `terminating` (value: `"terminating"`)

* `completed` (value: `"completed"`)

* `deleting` (value: `"deleting"`)




