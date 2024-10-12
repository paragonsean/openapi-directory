# CloudDeployApi.RetryAttempt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **String** | Output only. The index of this retry attempt. | [optional] [readonly] 
**state** | **String** | Output only. Valid state of this retry action. | [optional] [readonly] 
**stateDesc** | **String** | Output only. Description of the state of the Retry. | [optional] [readonly] 
**wait** | **String** | Output only. How long the operation will be paused. | [optional] [readonly] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"REPAIR_STATE_UNSPECIFIED"`)

* `SUCCEEDED` (value: `"REPAIR_STATE_SUCCEEDED"`)

* `CANCELLED` (value: `"REPAIR_STATE_CANCELLED"`)

* `FAILED` (value: `"REPAIR_STATE_FAILED"`)

* `IN_PROGRESS` (value: `"REPAIR_STATE_IN_PROGRESS"`)

* `PENDING` (value: `"REPAIR_STATE_PENDING"`)

* `SKIPPED` (value: `"REPAIR_STATE_SKIPPED"`)

* `ABORTED` (value: `"REPAIR_STATE_ABORTED"`)




