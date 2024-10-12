

# WorkflowInvocationAction

Represents a single action in a workflow invocation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigqueryAction** | [**BigQueryAction**](BigQueryAction.md) |  |  [optional] |
|**canonicalTarget** | [**Target**](Target.md) |  |  [optional] |
|**failureReason** | **String** | Output only. If and only if action&#39;s state is FAILED a failure reason is set. |  [optional] [readonly] |
|**invocationTiming** | [**Interval**](Interval.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. This action&#39;s current state. |  [optional] [readonly] |
|**target** | [**Target**](Target.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SKIPPED | &quot;SKIPPED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| FAILED | &quot;FAILED&quot; |



