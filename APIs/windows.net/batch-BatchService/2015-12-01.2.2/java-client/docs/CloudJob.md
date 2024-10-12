

# CloudJob

An Azure Batch job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonEnvironmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) | Gets or sets the list of common environment variable settings.  These environment variables are set for all tasks in the job (including the Job Manager, Job Preparation and Job Release tasks). |  [optional] |
|**constraints** | [**JobConstraints**](JobConstraints.md) |  |  [optional] |
|**creationTime** | **OffsetDateTime** | Gets or sets the creation time of the job. |  [optional] |
|**displayName** | **String** | Gets or sets the display name for the job. |  [optional] |
|**eTag** | **String** | Gets or sets the ETag of the job. |  [optional] |
|**executionInfo** | [**JobExecutionInformation**](JobExecutionInformation.md) |  |  [optional] |
|**id** | **String** | Gets or sets a string that uniquely identifies the job within the account. The id can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. It is common to use a GUID for the id. |  [optional] |
|**jobManagerTask** | [**JobManagerTask**](JobManagerTask.md) |  |  [optional] |
|**jobPreparationTask** | [**JobPreparationTask**](JobPreparationTask.md) |  |  [optional] |
|**jobReleaseTask** | [**JobReleaseTask**](JobReleaseTask.md) |  |  [optional] |
|**lastModified** | **OffsetDateTime** | Gets or sets the last modified time of the job. |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | Gets or sets a list of name-value pairs associated with the job as metadata. |  [optional] |
|**poolInfo** | [**PoolInformation**](PoolInformation.md) |  |  [optional] |
|**previousState** | [**PreviousStateEnum**](#PreviousStateEnum) | Gets or sets the previous state of the job. This property is not set if the job is in its initial Active state. |  [optional] |
|**previousStateTransitionTime** | **OffsetDateTime** | Gets or sets the time at which the job entered its previous state. This property is not set if the job is in its initial Active state. |  [optional] |
|**priority** | **Integer** | Gets or sets the priority of the job. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Gets or sets the current state of the job. |  [optional] |
|**stateTransitionTime** | **OffsetDateTime** | Gets or sets the time at which the job entered its current state. |  [optional] |
|**stats** | [**JobStatistics**](JobStatistics.md) |  |  [optional] |
|**url** | **String** | Gets or sets the URL of the job. |  [optional] |
|**usesTaskDependencies** | **Boolean** | Gets or sets the flag that determines if this job will use tasks with dependencies. |  [optional] |



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



