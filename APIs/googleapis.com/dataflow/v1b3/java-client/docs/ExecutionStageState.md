

# ExecutionStageState

A message describing the state of a particular execution stage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentStateTime** | **String** | The time at which the stage transitioned to this state. |  [optional] |
|**executionStageName** | **String** | The name of the execution stage. |  [optional] |
|**executionStageState** | [**ExecutionStageStateEnum**](#ExecutionStageStateEnum) | Executions stage states allow the same set of values as JobState. |  [optional] |



## Enum: ExecutionStageStateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;JOB_STATE_UNKNOWN&quot; |
| STOPPED | &quot;JOB_STATE_STOPPED&quot; |
| RUNNING | &quot;JOB_STATE_RUNNING&quot; |
| DONE | &quot;JOB_STATE_DONE&quot; |
| FAILED | &quot;JOB_STATE_FAILED&quot; |
| CANCELLED | &quot;JOB_STATE_CANCELLED&quot; |
| UPDATED | &quot;JOB_STATE_UPDATED&quot; |
| DRAINING | &quot;JOB_STATE_DRAINING&quot; |
| DRAINED | &quot;JOB_STATE_DRAINED&quot; |
| PENDING | &quot;JOB_STATE_PENDING&quot; |
| CANCELLING | &quot;JOB_STATE_CANCELLING&quot; |
| QUEUED | &quot;JOB_STATE_QUEUED&quot; |
| RESOURCE_CLEANING_UP | &quot;JOB_STATE_RESOURCE_CLEANING_UP&quot; |



