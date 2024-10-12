# BatchService.CloudJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commonEnvironmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) | Individual tasks can override an environment setting specified here by specifying the same setting name with a different value. | [optional] 
**constraints** | [**JobConstraints**](JobConstraints.md) |  | [optional] 
**creationTime** | **Date** |  | [optional] 
**displayName** | **String** |  | [optional] 
**eTag** | **String** | This is an opaque string. You can use it to detect whether the job has changed between requests. In particular, you can be pass the ETag when updating a job to specify that your changes should take effect only if nobody else has modified the job in the meantime. | [optional] 
**executionInfo** | [**JobExecutionInformation**](JobExecutionInformation.md) |  | [optional] 
**id** | **String** | The ID is case-preserving and case-insensitive (that is, you may not have two IDs within an account that differ only by case). | [optional] 
**jobManagerTask** | [**JobManagerTask**](JobManagerTask.md) |  | [optional] 
**jobPreparationTask** | [**JobPreparationTask**](JobPreparationTask.md) |  | [optional] 
**jobReleaseTask** | [**JobReleaseTask**](JobReleaseTask.md) |  | [optional] 
**lastModified** | **Date** | This is the last time at which the job level data, such as the job state or priority, changed. It does not factor in task-level changes such as adding new tasks or tasks changing state. | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | The Batch service does not assign any meaning to metadata; it is solely for the use of user code. | [optional] 
**networkConfiguration** | [**JobNetworkConfiguration**](JobNetworkConfiguration.md) |  | [optional] 
**onAllTasksComplete** | [**OnAllTasksComplete**](OnAllTasksComplete.md) |  | [optional] 
**onTaskFailure** | [**OnTaskFailure**](OnTaskFailure.md) |  | [optional] 
**poolInfo** | [**PoolInformation**](PoolInformation.md) |  | [optional] 
**previousState** | [**JobState**](JobState.md) |  | [optional] 
**previousStateTransitionTime** | **Date** | This property is not set if the job is in its initial Active state. | [optional] 
**priority** | **Number** | Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. | [optional] 
**state** | [**JobState**](JobState.md) |  | [optional] 
**stateTransitionTime** | **Date** |  | [optional] 
**stats** | [**JobStatistics**](JobStatistics.md) |  | [optional] 
**url** | **String** |  | [optional] 
**usesTaskDependencies** | **Boolean** |  | [optional] 


