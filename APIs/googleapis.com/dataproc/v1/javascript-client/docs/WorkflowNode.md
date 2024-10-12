# CloudDataprocApi.WorkflowNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **String** | Output only. The error detail. | [optional] [readonly] 
**jobId** | **String** | Output only. The job id; populated after the node enters RUNNING state. | [optional] [readonly] 
**prerequisiteStepIds** | **[String]** | Output only. Node&#39;s prerequisite nodes. | [optional] [readonly] 
**state** | **String** | Output only. The node state. | [optional] [readonly] 
**stepId** | **String** | Output only. The name of the node. | [optional] [readonly] 



## Enum: StateEnum


* `NODE_STATE_UNSPECIFIED` (value: `"NODE_STATE_UNSPECIFIED"`)

* `BLOCKED` (value: `"BLOCKED"`)

* `RUNNABLE` (value: `"RUNNABLE"`)

* `RUNNING` (value: `"RUNNING"`)

* `COMPLETED` (value: `"COMPLETED"`)

* `FAILED` (value: `"FAILED"`)




