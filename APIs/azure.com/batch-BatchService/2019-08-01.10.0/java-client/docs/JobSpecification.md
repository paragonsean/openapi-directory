

# JobSpecification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonEnvironmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) | Individual Tasks can override an environment setting specified here by specifying the same setting name with a different value. |  [optional] |
|**constraints** | [**JobConstraints**](JobConstraints.md) |  |  [optional] |
|**displayName** | **String** | The name need not be unique and can contain any Unicode characters up to a maximum length of 1024. |  [optional] |
|**jobManagerTask** | [**JobManagerTask**](JobManagerTask.md) |  |  [optional] |
|**jobPreparationTask** | [**JobPreparationTask**](JobPreparationTask.md) |  |  [optional] |
|**jobReleaseTask** | [**JobReleaseTask**](JobReleaseTask.md) |  |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | The Batch service does not assign any meaning to metadata; it is solely for the use of user code. |  [optional] |
|**networkConfiguration** | [**JobNetworkConfiguration**](JobNetworkConfiguration.md) |  |  [optional] |
|**onAllTasksComplete** | **OnAllTasksComplete** |  |  [optional] |
|**onTaskFailure** | **OnTaskFailure** |  |  [optional] |
|**poolInfo** | [**PoolInformation**](PoolInformation.md) |  |  |
|**priority** | **Integer** | Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. This priority is used as the default for all Jobs under the Job Schedule. You can update a Job&#39;s priority after it has been created using by using the update Job API. |  [optional] |
|**usesTaskDependencies** | **Boolean** |  |  [optional] |



