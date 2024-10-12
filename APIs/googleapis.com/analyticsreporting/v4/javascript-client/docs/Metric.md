# AnalyticsReportingApi.Metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **String** | An alias for the metric expression is an alternate name for the expression. The alias can be used for filtering and sorting. This field is optional and is useful if the expression is not a single metric but a complex expression which cannot be used in filtering and sorting. The alias is also used in the response column header. | [optional] 
**expression** | **String** | A metric expression in the request. An expression is constructed from one or more metrics and numbers. Accepted operators include: Plus (+), Minus (-), Negation (Unary -), Divided by (/), Multiplied by (*), Parenthesis, Positive cardinal numbers (0-9), can include decimals and is limited to 1024 characters. Example &#x60;ga:totalRefunds/ga:users&#x60;, in most cases the metric expression is just a single metric name like &#x60;ga:users&#x60;. Adding mixed &#x60;MetricType&#x60; (E.g., &#x60;CURRENCY&#x60; + &#x60;PERCENTAGE&#x60;) metrics will result in unexpected results. | [optional] 
**formattingType** | **String** | Specifies how the metric expression should be formatted, for example &#x60;INTEGER&#x60;. | [optional] 



## Enum: FormattingTypeEnum


* `METRIC_TYPE_UNSPECIFIED` (value: `"METRIC_TYPE_UNSPECIFIED"`)

* `INTEGER` (value: `"INTEGER"`)

* `FLOAT` (value: `"FLOAT"`)

* `CURRENCY` (value: `"CURRENCY"`)

* `PERCENT` (value: `"PERCENT"`)

* `TIME` (value: `"TIME"`)




