# AnalyticsReportingApi.MetricFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparisonValue** | **String** | The value to compare against. | [optional] 
**metricName** | **String** | The metric that will be filtered on. A metricFilter must contain a metric name. A metric name can be an alias earlier defined as a metric or it can also be a metric expression. | [optional] 
**not** | **Boolean** | Logical &#x60;NOT&#x60; operator. If this boolean is set to true, then the matching metric values will be excluded in the report. The default is false. | [optional] 
**operator** | **String** | Is the metric &#x60;EQUAL&#x60;, &#x60;LESS_THAN&#x60; or &#x60;GREATER_THAN&#x60; the comparisonValue, the default is &#x60;EQUAL&#x60;. If the operator is &#x60;IS_MISSING&#x60;, checks if the metric is missing and would ignore the comparisonValue. | [optional] 



## Enum: OperatorEnum


* `OPERATOR_UNSPECIFIED` (value: `"OPERATOR_UNSPECIFIED"`)

* `EQUAL` (value: `"EQUAL"`)

* `LESS_THAN` (value: `"LESS_THAN"`)

* `GREATER_THAN` (value: `"GREATER_THAN"`)

* `IS_MISSING` (value: `"IS_MISSING"`)




