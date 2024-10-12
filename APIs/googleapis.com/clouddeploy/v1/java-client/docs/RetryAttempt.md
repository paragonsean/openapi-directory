

# RetryAttempt

RetryAttempt represents an action of retrying the failed Cloud Deploy job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attempt** | **String** | Output only. The index of this retry attempt. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Valid state of this retry action. |  [optional] [readonly] |
|**stateDesc** | **String** | Output only. Description of the state of the Retry. |  [optional] [readonly] |
|**wait** | **String** | Output only. How long the operation will be paused. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;REPAIR_STATE_UNSPECIFIED&quot; |
| SUCCEEDED | &quot;REPAIR_STATE_SUCCEEDED&quot; |
| CANCELLED | &quot;REPAIR_STATE_CANCELLED&quot; |
| FAILED | &quot;REPAIR_STATE_FAILED&quot; |
| IN_PROGRESS | &quot;REPAIR_STATE_IN_PROGRESS&quot; |
| PENDING | &quot;REPAIR_STATE_PENDING&quot; |
| SKIPPED | &quot;REPAIR_STATE_SKIPPED&quot; |
| ABORTED | &quot;REPAIR_STATE_ABORTED&quot; |



