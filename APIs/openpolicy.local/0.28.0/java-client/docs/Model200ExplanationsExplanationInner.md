

# Model200ExplanationsExplanationInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**locals** | [**List&lt;Model200ExplanationsExplanationInnerLocalsInner&gt;**](Model200ExplanationsExplanationInnerLocalsInner.md) | The query&#39;s term bindings at the point when the trace event was emitted. |  [optional] |
|**node** | [**Model200ExplanationsExplanationInnerNode**](Model200ExplanationsExplanationInnerNode.md) |  |  [optional] |
|**op** | [**OpEnum**](#OpEnum) | The kind of *trace event*  Each trace event represents a step in the query evaluation process. Trace events are emitted at the following points: - enter - before a body or rule is evaluated - exit - after a body or rule has evaluated successfully - eval - before an expression is evaluated - fail - after an expression has evaluated to false. - redo - before evaluation restarts from a body, rule, or expression.  By default, OPA searches for all sets of term bindings that make all expressions in the query evaluate to true. Because there may be multiple answers, the search can restart when OPA determines the query is true or false. When the search restarts, a *redo trace event* is emitted. |  [optional] |
|**parentId** | **BigDecimal** | The parent query. Use this field to identify trace events from related queries.  For example, if query A references rule R, trace events emitted when evaluating rule R will have the *parent_id* field set to query A’s *query_id*. |  [optional] |
|**queryId** | **BigDecimal** | The query that the trace event was emitted for. Use this field to distinguish trace events emitted by from different queries. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the **node** field |  [optional] |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| ENTER | &quot;enter&quot; |
| EXIT | &quot;exit&quot; |
| EVAL | &quot;eval&quot; |
| FAIL | &quot;fail&quot; |
| REDO | &quot;redo&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EXPR | &quot;expr&quot; |
| RULE | &quot;rule&quot; |
| BODY | &quot;body&quot; |



