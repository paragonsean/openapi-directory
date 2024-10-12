

# UpdateTaskInstance


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dryRun** | **Boolean** | If set, don&#39;t actually run this operation. The response will contain the task instance planned to be affected, but won&#39;t be modified in any way.  |  [optional] |
|**newState** | [**NewStateEnum**](#NewStateEnum) | Expected new state. |  [optional] |



## Enum: NewStateEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| FAILED | &quot;failed&quot; |



