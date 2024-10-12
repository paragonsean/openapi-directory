# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaCalculatedMetric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculatedMetricId** | **String** | Output only. The ID to use for the calculated metric. In the UI, this is referred to as the \&quot;API name.\&quot; The calculated_metric_id is used when referencing this calculated metric from external APIs. For example, \&quot;calcMetric:{calculated_metric_id}\&quot;. | [optional] [readonly] 
**description** | **String** | Optional. Description for this calculated metric. Max length of 4096 characters. | [optional] 
**displayName** | **String** | Required. Display name for this calculated metric as shown in the Google Analytics UI. Max length 82 characters. | [optional] 
**formula** | **String** | Required. The calculated metric&#39;s definition. Maximum number of unique referenced custom metrics is 5. Formulas supports the following operations: + (addition), - (subtraction), - (negative), * (multiplication), / (division), () (parenthesis). Any valid real numbers are acceptable that fit in a Long (64bit integer) or a Double (64 bit floating point number). Example formula: \&quot;( customEvent:parameter_name + cartPurchaseQuantity ) / 2.0\&quot; | [optional] 
**invalidMetricReference** | **Boolean** | Output only. If true, this calculated metric has a invalid metric reference. Anything using a calculated metric with invalid_metric_reference set to true may fail, produce warnings, or produce unexpected results. | [optional] [readonly] 
**metricUnit** | **String** | Required. The type for the calculated metric&#39;s value. | [optional] 
**name** | **String** | Output only. Resource name for this CalculatedMetric. Format: &#39;properties/{property_id}/calculatedMetrics/{calculated_metric_id}&#39; | [optional] [readonly] 
**restrictedMetricType** | **[String]** | Output only. Types of restricted data that this metric contains. | [optional] [readonly] 



## Enum: MetricUnitEnum


* `METRIC_UNIT_UNSPECIFIED` (value: `"METRIC_UNIT_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `CURRENCY` (value: `"CURRENCY"`)

* `FEET` (value: `"FEET"`)

* `MILES` (value: `"MILES"`)

* `METERS` (value: `"METERS"`)

* `KILOMETERS` (value: `"KILOMETERS"`)

* `MILLISECONDS` (value: `"MILLISECONDS"`)

* `SECONDS` (value: `"SECONDS"`)

* `MINUTES` (value: `"MINUTES"`)

* `HOURS` (value: `"HOURS"`)





## Enum: [RestrictedMetricTypeEnum]


* `RESTRICTED_METRIC_TYPE_UNSPECIFIED` (value: `"RESTRICTED_METRIC_TYPE_UNSPECIFIED"`)

* `COST_DATA` (value: `"COST_DATA"`)

* `REVENUE_DATA` (value: `"REVENUE_DATA"`)




