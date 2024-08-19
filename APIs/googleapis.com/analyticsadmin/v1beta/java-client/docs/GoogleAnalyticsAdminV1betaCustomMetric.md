

# GoogleAnalyticsAdminV1betaCustomMetric

A definition for a custom metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Optional. Description for this custom dimension. Max length of 150 characters. |  [optional] |
|**displayName** | **String** | Required. Display name for this custom metric as shown in the Analytics UI. Max length of 82 characters, alphanumeric plus space and underscore starting with a letter. Legacy system-generated display names may contain square brackets, but updates to this field will never permit square brackets. |  [optional] |
|**measurementUnit** | [**MeasurementUnitEnum**](#MeasurementUnitEnum) | Required. The type for the custom metric&#39;s value. |  [optional] |
|**name** | **String** | Output only. Resource name for this CustomMetric resource. Format: properties/{property}/customMetrics/{customMetric} |  [optional] [readonly] |
|**parameterName** | **String** | Required. Immutable. Tagging name for this custom metric. If this is an event-scoped metric, then this is the event parameter name. May only contain alphanumeric and underscore charactes, starting with a letter. Max length of 40 characters for event-scoped metrics. |  [optional] |
|**restrictedMetricType** | [**List&lt;RestrictedMetricTypeEnum&gt;**](#List&lt;RestrictedMetricTypeEnum&gt;) | Optional. Types of restricted data that this metric may contain. Required for metrics with CURRENCY measurement unit. Must be empty for metrics with a non-CURRENCY measurement unit. |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | Required. Immutable. The scope of this custom metric. |  [optional] |



## Enum: MeasurementUnitEnum

| Name | Value |
|---- | -----|
| MEASUREMENT_UNIT_UNSPECIFIED | &quot;MEASUREMENT_UNIT_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| CURRENCY | &quot;CURRENCY&quot; |
| FEET | &quot;FEET&quot; |
| METERS | &quot;METERS&quot; |
| KILOMETERS | &quot;KILOMETERS&quot; |
| MILES | &quot;MILES&quot; |
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



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| METRIC_SCOPE_UNSPECIFIED | &quot;METRIC_SCOPE_UNSPECIFIED&quot; |
| EVENT | &quot;EVENT&quot; |



