# AnalyticsReportingApi.SegmentMetricFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparisonValue** | **String** | The value to compare against. If the operator is &#x60;BETWEEN&#x60;, this value is treated as minimum comparison value. | [optional] 
**maxComparisonValue** | **String** | Max comparison value is only used for &#x60;BETWEEN&#x60; operator. | [optional] 
**metricName** | **String** | The metric that will be filtered on. A &#x60;metricFilter&#x60; must contain a metric name. | [optional] 
**operator** | **String** | Specifies is the operation to perform to compare the metric. The default is &#x60;EQUAL&#x60;. | [optional] 
**scope** | **String** | Scope for a metric defines the level at which that metric is defined. The specified metric scope must be equal to or greater than its primary scope as defined in the data model. The primary scope is defined by if the segment is selecting users or sessions. | [optional] 



## Enum: OperatorEnum


* `UNSPECIFIED_OPERATOR` (value: `"UNSPECIFIED_OPERATOR"`)

* `LESS_THAN` (value: `"LESS_THAN"`)

* `GREATER_THAN` (value: `"GREATER_THAN"`)

* `EQUAL` (value: `"EQUAL"`)

* `BETWEEN` (value: `"BETWEEN"`)





## Enum: ScopeEnum


* `UNSPECIFIED_SCOPE` (value: `"UNSPECIFIED_SCOPE"`)

* `PRODUCT` (value: `"PRODUCT"`)

* `HIT` (value: `"HIT"`)

* `SESSION` (value: `"SESSION"`)

* `USER` (value: `"USER"`)




