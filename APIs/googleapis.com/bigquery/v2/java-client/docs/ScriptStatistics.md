

# ScriptStatistics

Job statistics specific to the child job of a script.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**evaluationKind** | [**EvaluationKindEnum**](#EvaluationKindEnum) | Whether this child job was a statement or expression. |  [optional] |
|**stackFrames** | [**List&lt;ScriptStackFrame&gt;**](ScriptStackFrame.md) | Stack trace showing the line/column/procedure name of each frame on the stack at the point where the current evaluation happened. The leaf frame is first, the primary script is last. Never empty. |  [optional] |



## Enum: EvaluationKindEnum

| Name | Value |
|---- | -----|
| EVALUATION_KIND_UNSPECIFIED | &quot;EVALUATION_KIND_UNSPECIFIED&quot; |
| STATEMENT | &quot;STATEMENT&quot; |
| EXPRESSION | &quot;EXPRESSION&quot; |



