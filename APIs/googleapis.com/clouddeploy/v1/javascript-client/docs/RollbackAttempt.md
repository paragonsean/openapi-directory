# CloudDeployApi.RollbackAttempt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinationPhase** | **String** | Output only. The phase to which the rollout will be rolled back to. | [optional] [readonly] 
**rolloutId** | **String** | Output only. ID of the rollback &#x60;Rollout&#x60; to create. | [optional] [readonly] 
**state** | **String** | Output only. Valid state of this rollback action. | [optional] [readonly] 
**stateDesc** | **String** | Output only. Description of the state of the Rollback. | [optional] [readonly] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"REPAIR_STATE_UNSPECIFIED"`)

* `SUCCEEDED` (value: `"REPAIR_STATE_SUCCEEDED"`)

* `CANCELLED` (value: `"REPAIR_STATE_CANCELLED"`)

* `FAILED` (value: `"REPAIR_STATE_FAILED"`)

* `IN_PROGRESS` (value: `"REPAIR_STATE_IN_PROGRESS"`)

* `PENDING` (value: `"REPAIR_STATE_PENDING"`)

* `SKIPPED` (value: `"REPAIR_STATE_SKIPPED"`)

* `ABORTED` (value: `"REPAIR_STATE_ABORTED"`)




