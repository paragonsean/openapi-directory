

# JobExecutionProperties

Properties for an Azure SQL Database Elastic job execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **OffsetDateTime** | The time that the job execution was created. |  [optional] [readonly] |
|**currentAttemptStartTime** | **OffsetDateTime** | Start time of the current attempt. |  [optional] [readonly] |
|**currentAttempts** | **Integer** | Number of times the job execution has been attempted. |  [optional] |
|**endTime** | **OffsetDateTime** | The time that the job execution completed. |  [optional] [readonly] |
|**jobExecutionId** | **UUID** | The unique identifier of the job execution. |  [optional] [readonly] |
|**jobVersion** | **Integer** | The job version number. |  [optional] [readonly] |
|**lastMessage** | **String** | The last status or error message. |  [optional] [readonly] |
|**lifecycle** | [**LifecycleEnum**](#LifecycleEnum) | The detailed state of the job execution. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The ARM provisioning state of the job execution. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | The time that the job execution started. |  [optional] [readonly] |
|**stepId** | **Integer** | The job step id. |  [optional] [readonly] |
|**stepName** | **String** | The job step name. |  [optional] [readonly] |
|**target** | [**JobExecutionTarget**](JobExecutionTarget.md) |  |  [optional] |



## Enum: LifecycleEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;Created&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| WAITING_FOR_CHILD_JOB_EXECUTIONS | &quot;WaitingForChildJobExecutions&quot; |
| WAITING_FOR_RETRY | &quot;WaitingForRetry&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| SUCCEEDED_WITH_SKIPPED | &quot;SucceededWithSkipped&quot; |
| FAILED | &quot;Failed&quot; |
| TIMED_OUT | &quot;TimedOut&quot; |
| CANCELED | &quot;Canceled&quot; |
| SKIPPED | &quot;Skipped&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;Created&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



