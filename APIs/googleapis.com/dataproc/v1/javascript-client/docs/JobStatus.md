# CloudDataprocApi.JobStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **String** | Optional. Output only. Job state details, such as an error description if the state is ERROR. | [optional] [readonly] 
**state** | **String** | Output only. A state message specifying the overall job state. | [optional] [readonly] 
**stateStartTime** | **String** | Output only. The time when this state was entered. | [optional] [readonly] 
**substate** | **String** | Output only. Additional state information, which includes status reported by the agent. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `SETUP_DONE` (value: `"SETUP_DONE"`)

* `RUNNING` (value: `"RUNNING"`)

* `CANCEL_PENDING` (value: `"CANCEL_PENDING"`)

* `CANCEL_STARTED` (value: `"CANCEL_STARTED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `DONE` (value: `"DONE"`)

* `ERROR` (value: `"ERROR"`)

* `ATTEMPT_FAILURE` (value: `"ATTEMPT_FAILURE"`)





## Enum: SubstateEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `SUBMITTED` (value: `"SUBMITTED"`)

* `QUEUED` (value: `"QUEUED"`)

* `STALE_STATUS` (value: `"STALE_STATUS"`)




