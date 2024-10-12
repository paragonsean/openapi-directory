

# AutomationTriggeringRule

A rule which is evaluated upon event interception. The rule is configured by comparing a specific value from the event model to an expected value. This comparison is done by using one of the supported operators set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expectedValue** | **String** | The expected value. |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | A valid comparer operator to use. A case-insensitive comparison will be applied for String PropertyType. |  [optional] |
|**propertyJPath** | **String** | The JPath of the entity model property that should be checked. |  [optional] |
|**propertyType** | [**PropertyTypeEnum**](#PropertyTypeEnum) | The data type of the compared operands (string, integer, floating point number or a boolean [true/false]] |  [optional] |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| EQUALS | &quot;Equals&quot; |
| GREATER_THAN | &quot;GreaterThan&quot; |
| GREATER_THAN_OR_EQUAL_TO | &quot;GreaterThanOrEqualTo&quot; |
| LESSER_THAN | &quot;LesserThan&quot; |
| LESSER_THAN_OR_EQUAL_TO | &quot;LesserThanOrEqualTo&quot; |
| NOT_EQUALS | &quot;NotEquals&quot; |
| CONTAINS | &quot;Contains&quot; |
| STARTS_WITH | &quot;StartsWith&quot; |
| ENDS_WITH | &quot;EndsWith&quot; |



## Enum: PropertyTypeEnum

| Name | Value |
|---- | -----|
| STRING | &quot;String&quot; |
| INTEGER | &quot;Integer&quot; |
| NUMBER | &quot;Number&quot; |
| BOOLEAN | &quot;Boolean&quot; |



