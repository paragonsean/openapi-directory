

# DateTimeRule

Allows you to organize the date-time values in a source data column into buckets based on selected parts of their date or time values. For example, consider a pivot table showing sales transactions by date: +----------+--------------+ | Date | SUM of Sales | +----------+--------------+ | 1/1/2017 | $621.14 | | 2/3/2017 | $708.84 | | 5/8/2017 | $326.84 | ... +----------+--------------+ Applying a date-time group rule with a DateTimeRuleType of YEAR_MONTH results in the following pivot table. +--------------+--------------+ | Grouped Date | SUM of Sales | +--------------+--------------+ | 2017-Jan | $53,731.78 | | 2017-Feb | $83,475.32 | | 2017-Mar | $94,385.05 | ... +--------------+--------------+

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | The type of date-time grouping to apply. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DATE_TIME_RULE_TYPE_UNSPECIFIED | &quot;DATE_TIME_RULE_TYPE_UNSPECIFIED&quot; |
| SECOND | &quot;SECOND&quot; |
| MINUTE | &quot;MINUTE&quot; |
| HOUR | &quot;HOUR&quot; |
| HOUR_MINUTE | &quot;HOUR_MINUTE&quot; |
| HOUR_MINUTE_AMPM | &quot;HOUR_MINUTE_AMPM&quot; |
| DAY_OF_WEEK | &quot;DAY_OF_WEEK&quot; |
| DAY_OF_YEAR | &quot;DAY_OF_YEAR&quot; |
| DAY_OF_MONTH | &quot;DAY_OF_MONTH&quot; |
| DAY_MONTH | &quot;DAY_MONTH&quot; |
| MONTH | &quot;MONTH&quot; |
| QUARTER | &quot;QUARTER&quot; |
| YEAR | &quot;YEAR&quot; |
| YEAR_MONTH | &quot;YEAR_MONTH&quot; |
| YEAR_QUARTER | &quot;YEAR_QUARTER&quot; |
| YEAR_MONTH_DAY | &quot;YEAR_MONTH_DAY&quot; |



