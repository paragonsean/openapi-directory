# DataformApi.WorkflowInvocationAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigqueryAction** | [**BigQueryAction**](BigQueryAction.md) |  | [optional] 
**canonicalTarget** | [**Target**](Target.md) |  | [optional] 
**failureReason** | **String** | Output only. If and only if action&#39;s state is FAILED a failure reason is set. | [optional] [readonly] 
**invocationTiming** | [**Interval**](Interval.md) |  | [optional] 
**state** | **String** | Output only. This action&#39;s current state. | [optional] [readonly] 
**target** | [**Target**](Target.md) |  | [optional] 



## Enum: StateEnum


* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `SKIPPED` (value: `"SKIPPED"`)

* `DISABLED` (value: `"DISABLED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `FAILED` (value: `"FAILED"`)




