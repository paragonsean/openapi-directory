# BatchApi.TaskStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **String** | Task state | [optional] 
**statusEvents** | [**[StatusEvent]**](StatusEvent.md) | Detailed info about why the state is reached. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `ASSIGNED` (value: `"ASSIGNED"`)

* `RUNNING` (value: `"RUNNING"`)

* `FAILED` (value: `"FAILED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `UNEXECUTED` (value: `"UNEXECUTED"`)




