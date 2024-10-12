

# ConditionValue

The value of the condition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**relativeDate** | [**RelativeDateEnum**](#RelativeDateEnum) | A relative date (based on the current date). Valid only if the type is DATE_BEFORE, DATE_AFTER, DATE_ON_OR_BEFORE or DATE_ON_OR_AFTER. Relative dates are not supported in data validation. They are supported only in conditional formatting and conditional filters. |  [optional] |
|**userEnteredValue** | **String** | A value the condition is based on. The value is parsed as if the user typed into a cell. Formulas are supported (and must begin with an &#x60;&#x3D;&#x60; or a &#39;+&#39;). |  [optional] |



## Enum: RelativeDateEnum

| Name | Value |
|---- | -----|
| RELATIVE_DATE_UNSPECIFIED | &quot;RELATIVE_DATE_UNSPECIFIED&quot; |
| PAST_YEAR | &quot;PAST_YEAR&quot; |
| PAST_MONTH | &quot;PAST_MONTH&quot; |
| PAST_WEEK | &quot;PAST_WEEK&quot; |
| YESTERDAY | &quot;YESTERDAY&quot; |
| TODAY | &quot;TODAY&quot; |
| TOMORROW | &quot;TOMORROW&quot; |



