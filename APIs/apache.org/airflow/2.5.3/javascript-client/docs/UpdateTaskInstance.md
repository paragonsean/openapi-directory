# AirflowApiStable.UpdateTaskInstance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dryRun** | **Boolean** | If set, don&#39;t actually run this operation. The response will contain the task instance planned to be affected, but won&#39;t be modified in any way.  | [optional] [default to false]
**newState** | **String** | Expected new state. | [optional] 



## Enum: NewStateEnum


* `success` (value: `"success"`)

* `failed` (value: `"failed"`)




