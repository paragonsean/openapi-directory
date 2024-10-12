

# AdvancedFilter

Represents an advanced filter that can be used to filter events based on various event envelope/data fields.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | The filter key. Represents an event property with up to two levels of nesting. |  [optional] |
|**operatorType** | [**OperatorTypeEnum**](#OperatorTypeEnum) | Represents the filter operator |  |



## Enum: OperatorTypeEnum

| Name | Value |
|---- | -----|
| NUMBER_IN | &quot;NumberIn&quot; |
| NUMBER_NOT_IN | &quot;NumberNotIn&quot; |
| NUMBER_LESS_THAN | &quot;NumberLessThan&quot; |
| NUMBER_GREATER_THAN | &quot;NumberGreaterThan&quot; |
| NUMBER_LESS_THAN_OR_EQUALS | &quot;NumberLessThanOrEquals&quot; |
| NUMBER_GREATER_THAN_OR_EQUALS | &quot;NumberGreaterThanOrEquals&quot; |
| BOOL_EQUALS | &quot;BoolEquals&quot; |
| STRING_IN | &quot;StringIn&quot; |
| STRING_NOT_IN | &quot;StringNotIn&quot; |
| STRING_BEGINS_WITH | &quot;StringBeginsWith&quot; |
| STRING_ENDS_WITH | &quot;StringEndsWith&quot; |
| STRING_CONTAINS | &quot;StringContains&quot; |



