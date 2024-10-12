

# JobSpecification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonEnvironmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) | Individual tasks can override an environment setting specified here by specifying the same setting name with a different value. |  [optional] |
|**constraints** | [**JobConstraints**](JobConstraints.md) |  |  [optional] |
|**displayName** | **String** | The name need not be unique and can contain any Unicode characters up to a maximum length of 1024. |  [optional] |
|**jobManagerTask** | [**JobManagerTask**](JobManagerTask.md) |  |  [optional] |
|**jobPreparationTask** | [**JobPreparationTask**](JobPreparationTask.md) |  |  [optional] |
|**jobReleaseTask** | [**JobReleaseTask**](JobReleaseTask.md) |  |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | The Batch service does not assign any meaning to metadata; it is solely for the use of user code. |  [optional] |
|**onAllTasksComplete** | [**OnAllTasksCompleteEnum**](#OnAllTasksCompleteEnum) | Note that if a job contains no tasks, then all tasks are considered complete. This option is therefore most commonly used with a job manager task; if you want to use automatic job termination without a job manager, you should initially set onAllTasksComplete to noAction and update the job properties to set onAllTasksComplete to terminateJob once you have finished adding tasks. The default is noAction. |  [optional] |
|**onTaskFailure** | [**OnTaskFailureEnum**](#OnTaskFailureEnum) | The default is noAction. |  [optional] |
|**poolInfo** | [**PoolInformation**](PoolInformation.md) |  |  |
|**priority** | **Integer** | Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. This priority is used as the default for all jobs under the job schedule. You can update a job&#39;s priority after it has been created using by using the update job API. |  [optional] |
|**usesTaskDependencies** | **Boolean** |  |  [optional] |



## Enum: OnAllTasksCompleteEnum

| Name | Value |
|---- | -----|
| NO_ACTION | &quot;noAction&quot; |
| TERMINATE_JOB | &quot;terminateJob&quot; |



## Enum: OnTaskFailureEnum

| Name | Value |
|---- | -----|
| NO_ACTION | &quot;noAction&quot; |
| PERFORM_EXIT_OPTIONS_JOB_ACTION | &quot;performExitOptionsJobAction&quot; |



