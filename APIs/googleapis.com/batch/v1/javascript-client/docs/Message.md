# BatchApi.Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**newJobState** | **String** | The new job state. | [optional] 
**newTaskState** | **String** | The new task state. | [optional] 
**type** | **String** | The message type. | [optional] 



## Enum: NewJobStateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `QUEUED` (value: `"QUEUED"`)

* `SCHEDULED` (value: `"SCHEDULED"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `DELETION_IN_PROGRESS` (value: `"DELETION_IN_PROGRESS"`)





## Enum: NewTaskStateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `ASSIGNED` (value: `"ASSIGNED"`)

* `RUNNING` (value: `"RUNNING"`)

* `FAILED` (value: `"FAILED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `UNEXECUTED` (value: `"UNEXECUTED"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `JOB_STATE_CHANGED` (value: `"JOB_STATE_CHANGED"`)

* `TASK_STATE_CHANGED` (value: `"TASK_STATE_CHANGED"`)




