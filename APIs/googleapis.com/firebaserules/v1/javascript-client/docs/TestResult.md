# FirebaseRulesApi.TestResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debugMessages** | **[String]** | Debug messages related to test execution issues encountered during evaluation. Debug messages may be related to too many or too few invocations of function mocks or to runtime errors that occur during evaluation. For example: &#x60;&#x60;&#x60;Unable to read variable [name: \&quot;resource\&quot;]&#x60;&#x60;&#x60; | [optional] 
**errorPosition** | [**SourcePosition**](SourcePosition.md) |  | [optional] 
**expressionReports** | [**[ExpressionReport]**](ExpressionReport.md) | The mapping from expression in the ruleset AST to the values they were evaluated to. Partially-nested to mirror AST structure. Note that this field is actually tracking expressions and not permission statements in contrast to the \&quot;visited_expressions\&quot; field above. Literal expressions are omitted. | [optional] 
**functionCalls** | [**[FunctionCall]**](FunctionCall.md) | The set of function calls made to service-defined methods. Function calls are included in the order in which they are encountered during evaluation, are provided for both mocked and unmocked functions, and included on the response regardless of the test &#x60;state&#x60;. | [optional] 
**state** | **String** | State of the test. | [optional] 
**visitedExpressions** | [**[VisitedExpression]**](VisitedExpression.md) | The set of visited permission expressions for a given test. This returns the positions and evaluation results of all visited permission expressions which were relevant to the test case, e.g. &#x60;&#x60;&#x60; match /path { allow read if: } &#x60;&#x60;&#x60; For a detailed report of the intermediate evaluation states, see the &#x60;expression_reports&#x60; field | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `SUCCESS` (value: `"SUCCESS"`)

* `FAILURE` (value: `"FAILURE"`)




