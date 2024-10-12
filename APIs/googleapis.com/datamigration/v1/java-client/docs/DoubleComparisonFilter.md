

# DoubleComparisonFilter

Filter based on relation between source value and compare value of type double in ConditionalColumnSetValue

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**value** | **Double** | Required. Double compare value to be used |  [optional] |
|**valueComparison** | [**ValueComparisonEnum**](#ValueComparisonEnum) | Required. Relation between source value and compare value |  [optional] |



## Enum: ValueComparisonEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;VALUE_COMPARISON_UNSPECIFIED&quot; |
| IF_VALUE_SMALLER_THAN | &quot;VALUE_COMPARISON_IF_VALUE_SMALLER_THAN&quot; |
| IF_VALUE_SMALLER_EQUAL_THAN | &quot;VALUE_COMPARISON_IF_VALUE_SMALLER_EQUAL_THAN&quot; |
| IF_VALUE_LARGER_THAN | &quot;VALUE_COMPARISON_IF_VALUE_LARGER_THAN&quot; |
| IF_VALUE_LARGER_EQUAL_THAN | &quot;VALUE_COMPARISON_IF_VALUE_LARGER_EQUAL_THAN&quot; |



