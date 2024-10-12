# CloudDataprocApi.StateHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **String** | Output only. The state of the batch at this point in history. | [optional] [readonly] 
**stateMessage** | **String** | Output only. Details about the state at this point in history. | [optional] [readonly] 
**stateStartTime** | **String** | Output only. The time when the batch entered the historical state. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)




