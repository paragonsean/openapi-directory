

# TasksList200ResponseValueInnerProperties

Base class for all types of DMS task properties. If task is not supported by current client, this object is returned.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;OperationsListDefaultResponseError&gt;**](OperationsListDefaultResponseError.md) | Array of errors. This is ignored if submitted. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The state of the task. This is ignored if submitted. |  [optional] [readonly] |
|**taskType** | **String** | Task type. |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| QUEUED | &quot;Queued&quot; |
| RUNNING | &quot;Running&quot; |
| CANCELED | &quot;Canceled&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| FAILED_INPUT_VALIDATION | &quot;FailedInputValidation&quot; |
| FAULTED | &quot;Faulted&quot; |



