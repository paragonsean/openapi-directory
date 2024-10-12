# CloudDeployApi.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanceChildRolloutJob** | **Object** | An advanceChildRollout Job. | [optional] 
**createChildRolloutJob** | **Object** | A createChildRollout Job. | [optional] 
**deployJob** | **Object** | A deploy Job. | [optional] 
**id** | **String** | Output only. The ID of the Job. | [optional] [readonly] 
**jobRun** | **String** | Output only. The name of the &#x60;JobRun&#x60; responsible for the most recent invocation of this Job. | [optional] [readonly] 
**postdeployJob** | [**PostdeployJob**](PostdeployJob.md) |  | [optional] 
**predeployJob** | [**PredeployJob**](PredeployJob.md) |  | [optional] 
**skipMessage** | **String** | Output only. Additional information on why the Job was skipped, if available. | [optional] [readonly] 
**state** | **String** | Output only. The current state of the Job. | [optional] [readonly] 
**verifyJob** | **Object** | A verify Job. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `DISABLED` (value: `"DISABLED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `ABORTED` (value: `"ABORTED"`)

* `SKIPPED` (value: `"SKIPPED"`)

* `IGNORED` (value: `"IGNORED"`)




