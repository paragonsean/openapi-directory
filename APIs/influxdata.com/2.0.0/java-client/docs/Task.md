

# Task


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationID** | **String** | The ID of the authorization used when this task communicates with the query engine. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**cron** | **String** | A task repetition schedule in the form &#39;* * * * * *&#39;; parsed from Flux. |  [optional] |
|**description** | **String** | An optional description of the task. |  [optional] |
|**every** | **String** | A simple task repetition schedule; parsed from Flux. |  [optional] |
|**flux** | **String** | The Flux script to run for this task. |  |
|**id** | **String** |  |  [readonly] |
|**labels** | [**List&lt;Label&gt;**](Label.md) |  |  [optional] |
|**lastRunError** | **String** |  |  [optional] [readonly] |
|**lastRunStatus** | [**LastRunStatusEnum**](#LastRunStatusEnum) |  |  [optional] [readonly] |
|**latestCompleted** | **OffsetDateTime** | Timestamp of latest scheduled, completed run, RFC3339. |  [optional] [readonly] |
|**links** | [**TaskLinks**](TaskLinks.md) |  |  [optional] |
|**name** | **String** | The name of the task. |  |
|**offset** | **String** | Duration to delay after the schedule, before executing the task; parsed from flux, if set to zero it will remove this option and use 0 as the default. |  [optional] |
|**org** | **String** | The name of the organization that owns this Task. |  [optional] |
|**orgID** | **String** | The ID of the organization that owns this Task. |  |
|**status** | **TaskStatusType** |  |  [optional] |
|**type** | **String** | The type of task, this can be used for filtering tasks on list actions. |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |



## Enum: LastRunStatusEnum

| Name | Value |
|---- | -----|
| FAILED | &quot;failed&quot; |
| SUCCESS | &quot;success&quot; |
| CANCELED | &quot;canceled&quot; |



