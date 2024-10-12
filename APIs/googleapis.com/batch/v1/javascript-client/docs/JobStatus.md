# BatchApi.JobStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runDuration** | **String** | The duration of time that the Job spent in status RUNNING. | [optional] 
**state** | **String** | Job state | [optional] 
**statusEvents** | [**[StatusEvent]**](StatusEvent.md) | Job status events | [optional] 
**taskGroups** | [**{String: TaskGroupStatus}**](TaskGroupStatus.md) | Aggregated task status for each TaskGroup in the Job. The map key is TaskGroup ID. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `QUEUED` (value: `"QUEUED"`)

* `SCHEDULED` (value: `"SCHEDULED"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `DELETION_IN_PROGRESS` (value: `"DELETION_IN_PROGRESS"`)




