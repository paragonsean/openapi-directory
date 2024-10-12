

# SegmentDimensionFilter

Dimension filter specifies the filtering options on a dimension.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caseSensitive** | **Boolean** | Should the match be case sensitive, ignored for &#x60;IN_LIST&#x60; operator. |  [optional] |
|**dimensionName** | **String** | Name of the dimension for which the filter is being applied. |  [optional] |
|**expressions** | **List&lt;String&gt;** | The list of expressions, only the first element is used for all operators |  [optional] |
|**maxComparisonValue** | **String** | Maximum comparison values for &#x60;BETWEEN&#x60; match type. |  [optional] |
|**minComparisonValue** | **String** | Minimum comparison values for &#x60;BETWEEN&#x60; match type. |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | The operator to use to match the dimension with the expressions. |  [optional] |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| OPERATOR_UNSPECIFIED | &quot;OPERATOR_UNSPECIFIED&quot; |
| REGEXP | &quot;REGEXP&quot; |
| BEGINS_WITH | &quot;BEGINS_WITH&quot; |
| ENDS_WITH | &quot;ENDS_WITH&quot; |
| PARTIAL | &quot;PARTIAL&quot; |
| EXACT | &quot;EXACT&quot; |
| IN_LIST | &quot;IN_LIST&quot; |
| NUMERIC_LESS_THAN | &quot;NUMERIC_LESS_THAN&quot; |
| NUMERIC_GREATER_THAN | &quot;NUMERIC_GREATER_THAN&quot; |
| NUMERIC_BETWEEN | &quot;NUMERIC_BETWEEN&quot; |



