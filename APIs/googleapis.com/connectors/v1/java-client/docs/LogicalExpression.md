

# LogicalExpression

Struct for representing boolean expressions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fieldComparisons** | [**List&lt;FieldComparison&gt;**](FieldComparison.md) | A list of fields to be compared. |  [optional] |
|**logicalExpressions** | [**List&lt;LogicalExpression&gt;**](LogicalExpression.md) | A list of nested conditions to be compared. |  [optional] |
|**logicalOperator** | [**LogicalOperatorEnum**](#LogicalOperatorEnum) | The logical operator to use between the fields and conditions. |  [optional] |



## Enum: LogicalOperatorEnum

| Name | Value |
|---- | -----|
| OPERATOR_UNSPECIFIED | &quot;OPERATOR_UNSPECIFIED&quot; |
| AND | &quot;AND&quot; |
| OR | &quot;OR&quot; |



