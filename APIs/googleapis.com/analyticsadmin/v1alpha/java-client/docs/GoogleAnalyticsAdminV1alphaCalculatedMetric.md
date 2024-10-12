

# GoogleAnalyticsAdminV1alphaCalculatedMetric

A definition for a calculated metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calculatedMetricId** | **String** | Output only. The ID to use for the calculated metric. In the UI, this is referred to as the \&quot;API name.\&quot; The calculated_metric_id is used when referencing this calculated metric from external APIs. For example, \&quot;calcMetric:{calculated_metric_id}\&quot;. |  [optional] [readonly] |
|**description** | **String** | Optional. Description for this calculated metric. Max length of 4096 characters. |  [optional] |
|**displayName** | **String** | Required. Display name for this calculated metric as shown in the Google Analytics UI. Max length 82 characters. |  [optional] |
|**formula** | **String** | Required. The calculated metric&#39;s definition. Maximum number of unique referenced custom metrics is 5. Formulas supports the following operations: + (addition), - (subtraction), - (negative), * (multiplication), / (division), () (parenthesis). Any valid real numbers are acceptable that fit in a Long (64bit integer) or a Double (64 bit floating point number). Example formula: \&quot;( customEvent:parameter_name + cartPurchaseQuantity ) / 2.0\&quot; |  [optional] |
|**invalidMetricReference** | **Boolean** | Output only. If true, this calculated metric has a invalid metric reference. Anything using a calculated metric with invalid_metric_reference set to true may fail, produce warnings, or produce unexpected results. |  [optional] [readonly] |
|**metricUnit** | [**MetricUnitEnum**](#MetricUnitEnum) | Required. The type for the calculated metric&#39;s value. |  [optional] |
|**name** | **String** | Output only. Resource name for this CalculatedMetric. Format: &#39;properties/{property_id}/calculatedMetrics/{calculated_metric_id}&#39; |  [optional] [readonly] |
|**restrictedMetricType** | [**List&lt;RestrictedMetricTypeEnum&gt;**](#List&lt;RestrictedMetricTypeEnum&gt;) | Output only. Types of restricted data that this metric contains. |  [optional] [readonly] |



## Enum: MetricUnitEnum

| Name | Value |
|---- | -----|
| METRIC_UNIT_UNSPECIFIED | &quot;METRIC_UNIT_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| CURRENCY | &quot;CURRENCY&quot; |
| FEET | &quot;FEET&quot; |
| MILES | &quot;MILES&quot; |
| METERS | &quot;METERS&quot; |
| KILOMETERS | &quot;KILOMETERS&quot; |
| MILLISECONDS | &quot;MILLISECONDS&quot; |
| SECONDS | &quot;SECONDS&quot; |
| MINUTES | &quot;MINUTES&quot; |
| HOURS | &quot;HOURS&quot; |



## Enum: List&lt;RestrictedMetricTypeEnum&gt;

| Name | Value |
|---- | -----|
| RESTRICTED_METRIC_TYPE_UNSPECIFIED | &quot;RESTRICTED_METRIC_TYPE_UNSPECIFIED&quot; |
| COST_DATA | &quot;COST_DATA&quot; |
| REVENUE_DATA | &quot;REVENUE_DATA&quot; |



