

# Metric

[Metrics](https://support.google.com/analytics/answer/1033861) are the quantitative measurements. For example, the metric `ga:users` indicates the total number of users for the requested time period.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alias** | **String** | An alias for the metric expression is an alternate name for the expression. The alias can be used for filtering and sorting. This field is optional and is useful if the expression is not a single metric but a complex expression which cannot be used in filtering and sorting. The alias is also used in the response column header. |  [optional] |
|**expression** | **String** | A metric expression in the request. An expression is constructed from one or more metrics and numbers. Accepted operators include: Plus (+), Minus (-), Negation (Unary -), Divided by (/), Multiplied by (*), Parenthesis, Positive cardinal numbers (0-9), can include decimals and is limited to 1024 characters. Example &#x60;ga:totalRefunds/ga:users&#x60;, in most cases the metric expression is just a single metric name like &#x60;ga:users&#x60;. Adding mixed &#x60;MetricType&#x60; (E.g., &#x60;CURRENCY&#x60; + &#x60;PERCENTAGE&#x60;) metrics will result in unexpected results. |  [optional] |
|**formattingType** | [**FormattingTypeEnum**](#FormattingTypeEnum) | Specifies how the metric expression should be formatted, for example &#x60;INTEGER&#x60;. |  [optional] |



## Enum: FormattingTypeEnum

| Name | Value |
|---- | -----|
| METRIC_TYPE_UNSPECIFIED | &quot;METRIC_TYPE_UNSPECIFIED&quot; |
| INTEGER | &quot;INTEGER&quot; |
| FLOAT | &quot;FLOAT&quot; |
| CURRENCY | &quot;CURRENCY&quot; |
| PERCENT | &quot;PERCENT&quot; |
| TIME | &quot;TIME&quot; |



