

# CloudJob

An Azure Batch job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonEnvironmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) | The list of common environment variable settings. These environment variables are set for all tasks in the job (including the Job Manager, Job Preparation and Job Release tasks). |  [optional] |
|**constraints** | [**JobConstraints**](JobConstraints.md) |  |  [optional] |
|**creationTime** | **OffsetDateTime** | The creation time of the job. |  [optional] |
|**displayName** | **String** | The display name for the job. |  [optional] |
|**eTag** | **String** | The ETag of the job. |  [optional] |
|**executionInfo** | [**JobExecutionInformation**](JobExecutionInformation.md) |  |  [optional] |
|**id** | **String** | A string that uniquely identifies the job within the account. The id can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. It is common to use a GUID for the id. |  [optional] |
|**jobManagerTask** | [**JobManagerTask**](JobManagerTask.md) |  |  [optional] |
|**jobPreparationTask** | [**JobPreparationTask**](JobPreparationTask.md) |  |  [optional] |
|**jobReleaseTask** | [**JobReleaseTask**](JobReleaseTask.md) |  |  [optional] |
|**lastModified** | **OffsetDateTime** | The last modified time of the job. |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | A list of name-value pairs associated with the job as metadata. |  [optional] |
|**poolInfo** | [**PoolInformation**](PoolInformation.md) |  |  [optional] |
|**previousState** | [**PreviousStateEnum**](#PreviousStateEnum) | The previous state of the job. This property is not set if the job is in its initial Active state. |  [optional] |
|**previousStateTransitionTime** | **OffsetDateTime** | The time at which the job entered its previous state. This property is not set if the job is in its initial Active state. |  [optional] |
|**priority** | **Integer** | The priority of the job. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the job. |  [optional] |
|**stateTransitionTime** | **OffsetDateTime** | The time at which the job entered its current state. |  [optional] |
|**stats** | [**JobStatistics**](JobStatistics.md) |  |  [optional] |
|**url** | **String** | The URL of the job. |  [optional] |
|**usesTaskDependencies** | **Boolean** | The flag that determines if this job will use tasks with dependencies. |  [optional] |



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



