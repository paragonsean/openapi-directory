

# BooleanCondition

A condition that can evaluate to true or false. BooleanConditions are used by conditional formatting, data validation, and the criteria in filters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | The type of condition. |  [optional] |
|**values** | [**List&lt;ConditionValue&gt;**](ConditionValue.md) | The values of the condition. The number of supported values depends on the condition type. Some support zero values, others one or two values, and ConditionType.ONE_OF_LIST supports an arbitrary number of values. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CONDITION_TYPE_UNSPECIFIED | &quot;CONDITION_TYPE_UNSPECIFIED&quot; |
| NUMBER_GREATER | &quot;NUMBER_GREATER&quot; |
| NUMBER_GREATER_THAN_EQ | &quot;NUMBER_GREATER_THAN_EQ&quot; |
| NUMBER_LESS | &quot;NUMBER_LESS&quot; |
| NUMBER_LESS_THAN_EQ | &quot;NUMBER_LESS_THAN_EQ&quot; |
| NUMBER_EQ | &quot;NUMBER_EQ&quot; |
| NUMBER_NOT_EQ | &quot;NUMBER_NOT_EQ&quot; |
| NUMBER_BETWEEN | &quot;NUMBER_BETWEEN&quot; |
| NUMBER_NOT_BETWEEN | &quot;NUMBER_NOT_BETWEEN&quot; |
| TEXT_CONTAINS | &quot;TEXT_CONTAINS&quot; |
| TEXT_NOT_CONTAINS | &quot;TEXT_NOT_CONTAINS&quot; |
| TEXT_STARTS_WITH | &quot;TEXT_STARTS_WITH&quot; |
| TEXT_ENDS_WITH | &quot;TEXT_ENDS_WITH&quot; |
| TEXT_EQ | &quot;TEXT_EQ&quot; |
| TEXT_IS_EMAIL | &quot;TEXT_IS_EMAIL&quot; |
| TEXT_IS_URL | &quot;TEXT_IS_URL&quot; |
| DATE_EQ | &quot;DATE_EQ&quot; |
| DATE_BEFORE | &quot;DATE_BEFORE&quot; |
| DATE_AFTER | &quot;DATE_AFTER&quot; |
| DATE_ON_OR_BEFORE | &quot;DATE_ON_OR_BEFORE&quot; |
| DATE_ON_OR_AFTER | &quot;DATE_ON_OR_AFTER&quot; |
| DATE_BETWEEN | &quot;DATE_BETWEEN&quot; |
| DATE_NOT_BETWEEN | &quot;DATE_NOT_BETWEEN&quot; |
| DATE_IS_VALID | &quot;DATE_IS_VALID&quot; |
| ONE_OF_RANGE | &quot;ONE_OF_RANGE&quot; |
| ONE_OF_LIST | &quot;ONE_OF_LIST&quot; |
| BLANK | &quot;BLANK&quot; |
| NOT_BLANK | &quot;NOT_BLANK&quot; |
| CUSTOM_FORMULA | &quot;CUSTOM_FORMULA&quot; |
| BOOLEAN | &quot;BOOLEAN&quot; |
| TEXT_NOT_EQ | &quot;TEXT_NOT_EQ&quot; |
| DATE_NOT_EQ | &quot;DATE_NOT_EQ&quot; |
| FILTER_EXPRESSION | &quot;FILTER_EXPRESSION&quot; |



