

# JobAddParameter

An Azure Batch job to add.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonEnvironmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) | Gets or sets the list of common environment variable settings.  These environment variables are set for all tasks in the job (including the Job Manager, Job Preparation and Job Release tasks). |  [optional] |
|**constraints** | [**JobConstraints**](JobConstraints.md) |  |  [optional] |
|**displayName** | **String** | Gets or sets the display name for the job. |  [optional] |
|**id** | **String** | Gets or sets a string that uniquely identifies the job within the account. The id can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. It is common to use a GUID for the id. |  |
|**jobManagerTask** | [**JobManagerTask**](JobManagerTask.md) |  |  [optional] |
|**jobPreparationTask** | [**JobPreparationTask**](JobPreparationTask.md) |  |  [optional] |
|**jobReleaseTask** | [**JobReleaseTask**](JobReleaseTask.md) |  |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | Gets or sets a list of name-value pairs associated with the job as metadata. |  [optional] |
|**poolInfo** | [**PoolInformation**](PoolInformation.md) |  |  |
|**priority** | **Integer** | Gets or sets the priority of the job. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. |  [optional] |
|**usesTaskDependencies** | **Boolean** | Gets or sets the flag that determines if this job will use tasks with dependencies. |  [optional] |



