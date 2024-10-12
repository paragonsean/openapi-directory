

# JobSpecification

Specifies details of the jobs to be created on a schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonEnvironmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) | A list of common environment variable settings. These environment variables are set for all tasks in jobs created under this schedule (including the Job Manager, Job Preparation and Job Release tasks). |  [optional] |
|**constraints** | [**JobConstraints**](JobConstraints.md) |  |  [optional] |
|**displayName** | **String** | The display name for jobs created under this schedule. It need not be unique and can contain any Unicode characters up to a maximum length of 1024. |  [optional] |
|**jobManagerTask** | [**JobManagerTask**](JobManagerTask.md) |  |  [optional] |
|**jobPreparationTask** | [**JobPreparationTask**](JobPreparationTask.md) |  |  [optional] |
|**jobReleaseTask** | [**JobReleaseTask**](JobReleaseTask.md) |  |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | A list of name-value pairs associated with each job created under this schedule as metadata. |  [optional] |
|**poolInfo** | [**PoolInformation**](PoolInformation.md) |  |  [optional] |
|**priority** | **Integer** | The priority of jobs created under this schedule. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. |  [optional] |
|**usesTaskDependencies** | **Boolean** | The flag that determines if this job will use tasks with dependencies. |  [optional] |



