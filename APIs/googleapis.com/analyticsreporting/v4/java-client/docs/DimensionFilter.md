

# DimensionFilter

Dimension filter specifies the filtering options on a dimension.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caseSensitive** | **Boolean** | Should the match be case sensitive? Default is false. |  [optional] |
|**dimensionName** | **String** | The dimension to filter on. A DimensionFilter must contain a dimension. |  [optional] |
|**expressions** | **List&lt;String&gt;** | Strings or regular expression to match against. Only the first value of the list is used for comparison unless the operator is &#x60;IN_LIST&#x60;. If &#x60;IN_LIST&#x60; operator, then the entire list is used to filter the dimensions as explained in the description of the &#x60;IN_LIST&#x60; operator. |  [optional] |
|**not** | **Boolean** | Logical &#x60;NOT&#x60; operator. If this boolean is set to true, then the matching dimension values will be excluded in the report. The default is false. |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | How to match the dimension to the expression. The default is REGEXP. |  [optional] |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| OPERATOR_UNSPECIFIED | &quot;OPERATOR_UNSPECIFIED&quot; |
| REGEXP | &quot;REGEXP&quot; |
| BEGINS_WITH | &quot;BEGINS_WITH&quot; |
| ENDS_WITH | &quot;ENDS_WITH&quot; |
| PARTIAL | &quot;PARTIAL&quot; |
| EXACT | &quot;EXACT&quot; |
| NUMERIC_EQUAL | &quot;NUMERIC_EQUAL&quot; |
| NUMERIC_GREATER_THAN | &quot;NUMERIC_GREATER_THAN&quot; |
| NUMERIC_LESS_THAN | &quot;NUMERIC_LESS_THAN&quot; |
| IN_LIST | &quot;IN_LIST&quot; |



