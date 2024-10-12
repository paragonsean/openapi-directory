# SqlManagementClient.JobExecutionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **Date** | The time that the job execution was created. | [optional] [readonly] 
**currentAttemptStartTime** | **Date** | Start time of the current attempt. | [optional] [readonly] 
**currentAttempts** | **Number** | Number of times the job execution has been attempted. | [optional] 
**endTime** | **Date** | The time that the job execution completed. | [optional] [readonly] 
**jobExecutionId** | **String** | The unique identifier of the job execution. | [optional] [readonly] 
**jobVersion** | **Number** | The job version number. | [optional] [readonly] 
**lastMessage** | **String** | The last status or error message. | [optional] [readonly] 
**lifecycle** | **String** | The detailed state of the job execution. | [optional] [readonly] 
**provisioningState** | **String** | The ARM provisioning state of the job execution. | [optional] [readonly] 
**startTime** | **Date** | The time that the job execution started. | [optional] [readonly] 
**stepId** | **Number** | The job step id. | [optional] [readonly] 
**stepName** | **String** | The job step name. | [optional] [readonly] 
**target** | [**JobExecutionTarget**](JobExecutionTarget.md) |  | [optional] 



## Enum: LifecycleEnum


* `Created` (value: `"Created"`)

* `InProgress` (value: `"InProgress"`)

* `WaitingForChildJobExecutions` (value: `"WaitingForChildJobExecutions"`)

* `WaitingForRetry` (value: `"WaitingForRetry"`)

* `Succeeded` (value: `"Succeeded"`)

* `SucceededWithSkipped` (value: `"SucceededWithSkipped"`)

* `Failed` (value: `"Failed"`)

* `TimedOut` (value: `"TimedOut"`)

* `Canceled` (value: `"Canceled"`)

* `Skipped` (value: `"Skipped"`)





## Enum: ProvisioningStateEnum


* `Created` (value: `"Created"`)

* `InProgress` (value: `"InProgress"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)




