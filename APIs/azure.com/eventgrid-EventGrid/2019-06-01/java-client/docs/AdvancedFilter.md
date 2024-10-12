

# AdvancedFilter

This is the base type that represents an advanced filter. To configure an advanced filter, do not directly instantiate an object of this class. Instead, instantiate an object of a derived class such as BoolEqualsAdvancedFilter, NumberInAdvancedFilter, StringEqualsAdvancedFilter etc. depending on the type of the key based on which you want to filter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | The field/property in the event based on which you want to filter. |  [optional] |
|**operatorType** | [**OperatorTypeEnum**](#OperatorTypeEnum) | The operator type used for filtering, e.g., NumberIn, StringContains, BoolEquals and others. |  |



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



