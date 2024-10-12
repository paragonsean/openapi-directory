# BigQueryApi.ScriptStatistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluationKind** | **String** | Whether this child job was a statement or expression. | [optional] 
**stackFrames** | [**[ScriptStackFrame]**](ScriptStackFrame.md) | Stack trace showing the line/column/procedure name of each frame on the stack at the point where the current evaluation happened. The leaf frame is first, the primary script is last. Never empty. | [optional] 



## Enum: EvaluationKindEnum


* `EVALUATION_KIND_UNSPECIFIED` (value: `"EVALUATION_KIND_UNSPECIFIED"`)

* `STATEMENT` (value: `"STATEMENT"`)

* `EXPRESSION` (value: `"EXPRESSION"`)




