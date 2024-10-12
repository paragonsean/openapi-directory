# BatchService.JobAddParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commonEnvironmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) | Individual tasks can override an environment setting specified here by specifying the same setting name with a different value. | [optional] 
**constraints** | [**JobConstraints**](JobConstraints.md) |  | [optional] 
**displayName** | **String** | The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024. | [optional] 
**id** | **String** | The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two IDs within an account that differ only by case). | 
**jobManagerTask** | [**JobManagerTask**](JobManagerTask.md) |  | [optional] 
**jobPreparationTask** | [**JobPreparationTask**](JobPreparationTask.md) |  | [optional] 
**jobReleaseTask** | [**JobReleaseTask**](JobReleaseTask.md) |  | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | The Batch service does not assign any meaning to metadata; it is solely for the use of user code. | [optional] 
**onAllTasksComplete** | [**OnAllTasksComplete**](OnAllTasksComplete.md) |  | [optional] 
**onTaskFailure** | [**OnTaskFailure**](OnTaskFailure.md) |  | [optional] 
**poolInfo** | [**PoolInformation**](PoolInformation.md) |  | 
**priority** | **Number** | Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. | [optional] 
**usesTaskDependencies** | **Boolean** |  | [optional] 


