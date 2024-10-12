

# WorkflowInvocation

Represents a single invocation of a compilation result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compilationResult** | **String** | Immutable. The name of the compilation result to use for this invocation. Must be in the format &#x60;projects/_*_/locations/_*_/repositories/_*_/compilationResults/_*&#x60;. |  [optional] |
|**invocationConfig** | [**InvocationConfig**](InvocationConfig.md) |  |  [optional] |
|**invocationTiming** | [**Interval**](Interval.md) |  |  [optional] |
|**name** | **String** | Output only. The workflow invocation&#39;s name. |  [optional] [readonly] |
|**resolvedCompilationResult** | **String** | Output only. The resolved compilation result that was used to create this invocation. Will be in the format &#x60;projects/_*_/locations/_*_/repositories/_*_/compilationResults/_*&#x60;. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. This workflow invocation&#39;s current state. |  [optional] [readonly] |
|**workflowConfig** | **String** | Immutable. The name of the workflow config to invoke. Must be in the format &#x60;projects/_*_/locations/_*_/repositories/_*_/workflowConfigs/_*&#x60;. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELING | &quot;CANCELING&quot; |



