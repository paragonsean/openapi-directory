

# GoogleAnalyticsAdminV1alphaMatchingCondition

Defines a condition for when an Event Edit or Event Creation rule applies to an event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comparisonType** | [**ComparisonTypeEnum**](#ComparisonTypeEnum) | Required. The type of comparison to be applied to the value. |  [optional] |
|**field** | **String** | Required. The name of the field that is compared against for the condition. If &#39;event_name&#39; is specified this condition will apply to the name of the event. Otherwise the condition will apply to a parameter with the specified name. This value cannot contain spaces. |  [optional] |
|**negated** | **Boolean** | Whether or not the result of the comparison should be negated. For example, if &#x60;negated&#x60; is true, then &#39;equals&#39; comparisons would function as &#39;not equals&#39;. |  [optional] |
|**value** | **String** | Required. The value being compared against for this condition. The runtime implementation may perform type coercion of this value to evaluate this condition based on the type of the parameter value. |  [optional] |



## Enum: ComparisonTypeEnum

| Name | Value |
|---- | -----|
| COMPARISON_TYPE_UNSPECIFIED | &quot;COMPARISON_TYPE_UNSPECIFIED&quot; |
| EQUALS | &quot;EQUALS&quot; |
| EQUALS_CASE_INSENSITIVE | &quot;EQUALS_CASE_INSENSITIVE&quot; |
| CONTAINS | &quot;CONTAINS&quot; |
| CONTAINS_CASE_INSENSITIVE | &quot;CONTAINS_CASE_INSENSITIVE&quot; |
| STARTS_WITH | &quot;STARTS_WITH&quot; |
| STARTS_WITH_CASE_INSENSITIVE | &quot;STARTS_WITH_CASE_INSENSITIVE&quot; |
| ENDS_WITH | &quot;ENDS_WITH&quot; |
| ENDS_WITH_CASE_INSENSITIVE | &quot;ENDS_WITH_CASE_INSENSITIVE&quot; |
| GREATER_THAN | &quot;GREATER_THAN&quot; |
| GREATER_THAN_OR_EQUAL | &quot;GREATER_THAN_OR_EQUAL&quot; |
| LESS_THAN | &quot;LESS_THAN&quot; |
| LESS_THAN_OR_EQUAL | &quot;LESS_THAN_OR_EQUAL&quot; |
| REGULAR_EXPRESSION | &quot;REGULAR_EXPRESSION&quot; |
| REGULAR_EXPRESSION_CASE_INSENSITIVE | &quot;REGULAR_EXPRESSION_CASE_INSENSITIVE&quot; |



