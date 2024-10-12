

# JobAddParameter


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonEnvironmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) |  |  [optional] |
|**constraints** | [**JobConstraints**](JobConstraints.md) |  |  [optional] |
|**displayName** | **String** | The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024. |  [optional] |
|**id** | **String** | The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. It is common to use a GUID for the id. |  |
|**jobManagerTask** | [**JobManagerTask**](JobManagerTask.md) |  |  [optional] |
|**jobPreparationTask** | [**JobPreparationTask**](JobPreparationTask.md) |  |  [optional] |
|**jobReleaseTask** | [**JobReleaseTask**](JobReleaseTask.md) |  |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | The Batch service does not assign any meaning to metadata; it is solely for the use of user code. |  [optional] |
|**onAllTasksComplete** | [**OnAllTasksCompleteEnum**](#OnAllTasksCompleteEnum) | Note that if a job contains no tasks, then all tasks are considered complete. This option is therefore most commonly used with a job manager task; if you want to use automatic job termination without a job manager, you should initially set onAllTasksComplete to noAction and update the job properties to set onAllTasksComplete to terminateJob once you have finished adding tasks. Permitted values are: noAction – do nothing. The job remains active unless terminated or disabled by some other means. terminateJob – terminate the job. The job’s terminateReason is set to &#39;AllTasksComplete&#39;. The default is noAction. |  [optional] |
|**onTaskFailure** | [**OnTaskFailureEnum**](#OnTaskFailureEnum) | Permitted values are: noAction – do nothing. performExitOptionsJobAction – take the action associated with the task exit condition in the task&#39;s exitConditions collection. (This may still result in no action being taken, if that is what the task specifies.) The default is noAction. |  [optional] |
|**poolInfo** | [**PoolInformation**](PoolInformation.md) |  |  |
|**priority** | **Integer** |  Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. |  [optional] |
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



