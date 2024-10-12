

# RollbackAttempt

RollbackAttempt represents an action of rolling back a Cloud Deploy 'Target'.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationPhase** | **String** | Output only. The phase to which the rollout will be rolled back to. |  [optional] [readonly] |
|**rolloutId** | **String** | Output only. ID of the rollback &#x60;Rollout&#x60; to create. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Valid state of this rollback action. |  [optional] [readonly] |
|**stateDesc** | **String** | Output only. Description of the state of the Rollback. |  [optional] [readonly] |



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



