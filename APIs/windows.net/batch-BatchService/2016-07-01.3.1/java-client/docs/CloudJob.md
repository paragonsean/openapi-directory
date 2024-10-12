

# CloudJob


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonEnvironmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) |  |  [optional] |
|**constraints** | [**JobConstraints**](JobConstraints.md) |  |  [optional] |
|**creationTime** | **OffsetDateTime** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**eTag** | **String** | This is an opaque string. You can use it to detect whether the job has changed between requests. In particular, you can be pass the ETag when updating a job to specify that your changes should take effect only if nobody else has modified the job in the meantime. |  [optional] |
|**executionInfo** | [**JobExecutionInformation**](JobExecutionInformation.md) |  |  [optional] |
|**id** | **String** | The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. It is common to use a GUID for the id. |  [optional] |
|**jobManagerTask** | [**JobManagerTask**](JobManagerTask.md) |  |  [optional] |
|**jobPreparationTask** | [**JobPreparationTask**](JobPreparationTask.md) |  |  [optional] |
|**jobReleaseTask** | [**JobReleaseTask**](JobReleaseTask.md) |  |  [optional] |
|**lastModified** | **OffsetDateTime** | This is the last time at which the job level data, such as the job state or priority, changed. It does not factor in task-level changes such as adding new tasks or tasks changing state. |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | The Batch service does not assign any meaning to metadata; it is solely for the use of user code. |  [optional] |
|**onAllTasksComplete** | [**OnAllTasksCompleteEnum**](#OnAllTasksCompleteEnum) | Permitted values are: noAction – do nothing. The job remains active unless terminated or disabled by some other means. terminateJob – terminate the job. The job&#39;s terminateReason is set to &#39;AllTasksComplete&#39;. The default is noAction. |  [optional] |
|**onTaskFailure** | [**OnTaskFailureEnum**](#OnTaskFailureEnum) | Permitted values are: noAction – do nothing. performExitOptionsJobAction – take the action associated with the task exit condition in the task&#39;s exitConditions collection. (This may still result in no action being taken, if that is what the task specifies.) The default is noAction. |  [optional] |
|**poolInfo** | [**PoolInformation**](PoolInformation.md) |  |  [optional] |
|**previousState** | [**PreviousStateEnum**](#PreviousStateEnum) | This property is not set if the job is in its initial Active state. |  [optional] |
|**previousStateTransitionTime** | **OffsetDateTime** | This property is not set if the job is in its initial Active state. |  [optional] |
|**priority** | **Integer** | Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  [optional] |
|**stateTransitionTime** | **OffsetDateTime** |  |  [optional] |
|**stats** | [**JobStatistics**](JobStatistics.md) |  |  [optional] |
|**url** | **String** |  |  [optional] |
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



## Enum: PreviousStateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DISABLING | &quot;disabling&quot; |
| DISABLED | &quot;disabled&quot; |
| ENABLING | &quot;enabling&quot; |
| TERMINATING | &quot;terminating&quot; |
| COMPLETED | &quot;completed&quot; |
| DELETING | &quot;deleting&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DISABLING | &quot;disabling&quot; |
| DISABLED | &quot;disabled&quot; |
| ENABLING | &quot;enabling&quot; |
| TERMINATING | &quot;terminating&quot; |
| COMPLETED | &quot;completed&quot; |
| DELETING | &quot;deleting&quot; |



