

# Job

Job represents an operation for a `Rollout`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advanceChildRolloutJob** | **Object** | An advanceChildRollout Job. |  [optional] |
|**createChildRolloutJob** | **Object** | A createChildRollout Job. |  [optional] |
|**deployJob** | **Object** | A deploy Job. |  [optional] |
|**id** | **String** | Output only. The ID of the Job. |  [optional] [readonly] |
|**jobRun** | **String** | Output only. The name of the &#x60;JobRun&#x60; responsible for the most recent invocation of this Job. |  [optional] [readonly] |
|**postdeployJob** | [**PostdeployJob**](PostdeployJob.md) |  |  [optional] |
|**predeployJob** | [**PredeployJob**](PredeployJob.md) |  |  [optional] |
|**skipMessage** | **String** | Output only. Additional information on why the Job was skipped, if available. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the Job. |  [optional] [readonly] |
|**verifyJob** | **Object** | A verify Job. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| DISABLED | &quot;DISABLED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| ABORTED | &quot;ABORTED&quot; |
| SKIPPED | &quot;SKIPPED&quot; |
| IGNORED | &quot;IGNORED&quot; |



