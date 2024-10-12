

# CloudJob


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonEnvironmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) | Individual Tasks can override an environment setting specified here by specifying the same setting name with a different value. |  [optional] |
|**constraints** | [**JobConstraints**](JobConstraints.md) |  |  [optional] |
|**creationTime** | **OffsetDateTime** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**eTag** | **String** | This is an opaque string. You can use it to detect whether the Job has changed between requests. In particular, you can be pass the ETag when updating a Job to specify that your changes should take effect only if nobody else has modified the Job in the meantime. |  [optional] |
|**executionInfo** | [**JobExecutionInformation**](JobExecutionInformation.md) |  |  [optional] |
|**id** | **String** | The ID is case-preserving and case-insensitive (that is, you may not have two IDs within an Account that differ only by case). |  [optional] |
|**jobManagerTask** | [**JobManagerTask**](JobManagerTask.md) |  |  [optional] |
|**jobPreparationTask** | [**JobPreparationTask**](JobPreparationTask.md) |  |  [optional] |
|**jobReleaseTask** | [**JobReleaseTask**](JobReleaseTask.md) |  |  [optional] |
|**lastModified** | **OffsetDateTime** | This is the last time at which the Job level data, such as the Job state or priority, changed. It does not factor in task-level changes such as adding new Tasks or Tasks changing state. |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | The Batch service does not assign any meaning to metadata; it is solely for the use of user code. |  [optional] |
|**networkConfiguration** | [**JobNetworkConfiguration**](JobNetworkConfiguration.md) |  |  [optional] |
|**onAllTasksComplete** | **OnAllTasksComplete** |  |  [optional] |
|**onTaskFailure** | **OnTaskFailure** |  |  [optional] |
|**poolInfo** | [**PoolInformation**](PoolInformation.md) |  |  [optional] |
|**previousState** | **JobState** |  |  [optional] |
|**previousStateTransitionTime** | **OffsetDateTime** | This property is not set if the Job is in its initial Active state. |  [optional] |
|**priority** | **Integer** | Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. |  [optional] |
|**state** | **JobState** |  |  [optional] |
|**stateTransitionTime** | **OffsetDateTime** |  |  [optional] |
|**stats** | [**JobStatistics**](JobStatistics.md) |  |  [optional] |
|**url** | **String** |  |  [optional] |
|**usesTaskDependencies** | **Boolean** |  |  [optional] |



