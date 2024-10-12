# BatchApi.StatusEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the event. | [optional] 
**eventTime** | **String** | The time this event occurred. | [optional] 
**taskExecution** | [**TaskExecution**](TaskExecution.md) |  | [optional] 
**taskState** | **String** | Task State | [optional] 
**type** | **String** | Type of the event. | [optional] 



## Enum: TaskStateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `ASSIGNED` (value: `"ASSIGNED"`)

* `RUNNING` (value: `"RUNNING"`)

* `FAILED` (value: `"FAILED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `UNEXECUTED` (value: `"UNEXECUTED"`)




