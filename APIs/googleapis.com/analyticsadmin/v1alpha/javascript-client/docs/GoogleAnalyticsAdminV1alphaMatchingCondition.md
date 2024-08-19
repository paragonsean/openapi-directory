# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaMatchingCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparisonType** | **String** | Required. The type of comparison to be applied to the value. | [optional] 
**field** | **String** | Required. The name of the field that is compared against for the condition. If &#39;event_name&#39; is specified this condition will apply to the name of the event. Otherwise the condition will apply to a parameter with the specified name. This value cannot contain spaces. | [optional] 
**negated** | **Boolean** | Whether or not the result of the comparison should be negated. For example, if &#x60;negated&#x60; is true, then &#39;equals&#39; comparisons would function as &#39;not equals&#39;. | [optional] 
**value** | **String** | Required. The value being compared against for this condition. The runtime implementation may perform type coercion of this value to evaluate this condition based on the type of the parameter value. | [optional] 



## Enum: ComparisonTypeEnum


* `COMPARISON_TYPE_UNSPECIFIED` (value: `"COMPARISON_TYPE_UNSPECIFIED"`)

* `EQUALS` (value: `"EQUALS"`)

* `EQUALS_CASE_INSENSITIVE` (value: `"EQUALS_CASE_INSENSITIVE"`)

* `CONTAINS` (value: `"CONTAINS"`)

* `CONTAINS_CASE_INSENSITIVE` (value: `"CONTAINS_CASE_INSENSITIVE"`)

* `STARTS_WITH` (value: `"STARTS_WITH"`)

* `STARTS_WITH_CASE_INSENSITIVE` (value: `"STARTS_WITH_CASE_INSENSITIVE"`)

* `ENDS_WITH` (value: `"ENDS_WITH"`)

* `ENDS_WITH_CASE_INSENSITIVE` (value: `"ENDS_WITH_CASE_INSENSITIVE"`)

* `GREATER_THAN` (value: `"GREATER_THAN"`)

* `GREATER_THAN_OR_EQUAL` (value: `"GREATER_THAN_OR_EQUAL"`)

* `LESS_THAN` (value: `"LESS_THAN"`)

* `LESS_THAN_OR_EQUAL` (value: `"LESS_THAN_OR_EQUAL"`)

* `REGULAR_EXPRESSION` (value: `"REGULAR_EXPRESSION"`)

* `REGULAR_EXPRESSION_CASE_INSENSITIVE` (value: `"REGULAR_EXPRESSION_CASE_INSENSITIVE"`)




