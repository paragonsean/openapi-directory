

# GoogleCloudDataplexV1Task

A task represents a user-visible job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time when the task was created. |  [optional] [readonly] |
|**description** | **String** | Optional. Description of the task. |  [optional] |
|**displayName** | **String** | Optional. User friendly display name. |  [optional] |
|**executionSpec** | [**GoogleCloudDataplexV1TaskExecutionSpec**](GoogleCloudDataplexV1TaskExecutionSpec.md) |  |  [optional] |
|**executionStatus** | [**GoogleCloudDataplexV1TaskExecutionStatus**](GoogleCloudDataplexV1TaskExecutionStatus.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. User-defined labels for the task. |  [optional] |
|**name** | **String** | Output only. The relative resource name of the task, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/ tasks/{task_id}. |  [optional] [readonly] |
|**notebook** | [**GoogleCloudDataplexV1TaskNotebookTaskConfig**](GoogleCloudDataplexV1TaskNotebookTaskConfig.md) |  |  [optional] |
|**spark** | [**GoogleCloudDataplexV1TaskSparkTaskConfig**](GoogleCloudDataplexV1TaskSparkTaskConfig.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Current state of the task. |  [optional] [readonly] |
|**triggerSpec** | [**GoogleCloudDataplexV1TaskTriggerSpec**](GoogleCloudDataplexV1TaskTriggerSpec.md) |  |  [optional] |
|**uid** | **String** | Output only. System generated globally unique ID for the task. This ID will be different if the task is deleted and re-created with the same name. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time when the task was last updated. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CREATING | &quot;CREATING&quot; |
| DELETING | &quot;DELETING&quot; |
| ACTION_REQUIRED | &quot;ACTION_REQUIRED&quot; |



