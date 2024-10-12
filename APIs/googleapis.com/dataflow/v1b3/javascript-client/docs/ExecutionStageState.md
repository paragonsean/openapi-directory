# DataflowApi.ExecutionStageState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentStateTime** | **String** | The time at which the stage transitioned to this state. | [optional] 
**executionStageName** | **String** | The name of the execution stage. | [optional] 
**executionStageState** | **String** | Executions stage states allow the same set of values as JobState. | [optional] 



## Enum: ExecutionStageStateEnum


* `UNKNOWN` (value: `"JOB_STATE_UNKNOWN"`)

* `STOPPED` (value: `"JOB_STATE_STOPPED"`)

* `RUNNING` (value: `"JOB_STATE_RUNNING"`)

* `DONE` (value: `"JOB_STATE_DONE"`)

* `FAILED` (value: `"JOB_STATE_FAILED"`)

* `CANCELLED` (value: `"JOB_STATE_CANCELLED"`)

* `UPDATED` (value: `"JOB_STATE_UPDATED"`)

* `DRAINING` (value: `"JOB_STATE_DRAINING"`)

* `DRAINED` (value: `"JOB_STATE_DRAINED"`)

* `PENDING` (value: `"JOB_STATE_PENDING"`)

* `CANCELLING` (value: `"JOB_STATE_CANCELLING"`)

* `QUEUED` (value: `"JOB_STATE_QUEUED"`)

* `RESOURCE_CLEANING_UP` (value: `"JOB_STATE_RESOURCE_CLEANING_UP"`)




