# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1betaCustomMetric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Optional. Description for this custom dimension. Max length of 150 characters. | [optional] 
**displayName** | **String** | Required. Display name for this custom metric as shown in the Analytics UI. Max length of 82 characters, alphanumeric plus space and underscore starting with a letter. Legacy system-generated display names may contain square brackets, but updates to this field will never permit square brackets. | [optional] 
**measurementUnit** | **String** | Required. The type for the custom metric&#39;s value. | [optional] 
**name** | **String** | Output only. Resource name for this CustomMetric resource. Format: properties/{property}/customMetrics/{customMetric} | [optional] [readonly] 
**parameterName** | **String** | Required. Immutable. Tagging name for this custom metric. If this is an event-scoped metric, then this is the event parameter name. May only contain alphanumeric and underscore charactes, starting with a letter. Max length of 40 characters for event-scoped metrics. | [optional] 
**restrictedMetricType** | **[String]** | Optional. Types of restricted data that this metric may contain. Required for metrics with CURRENCY measurement unit. Must be empty for metrics with a non-CURRENCY measurement unit. | [optional] 
**scope** | **String** | Required. Immutable. The scope of this custom metric. | [optional] 



## Enum: MeasurementUnitEnum


* `MEASUREMENT_UNIT_UNSPECIFIED` (value: `"MEASUREMENT_UNIT_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `CURRENCY` (value: `"CURRENCY"`)

* `FEET` (value: `"FEET"`)

* `METERS` (value: `"METERS"`)

* `KILOMETERS` (value: `"KILOMETERS"`)

* `MILES` (value: `"MILES"`)

* `MILLISECONDS` (value: `"MILLISECONDS"`)

* `SECONDS` (value: `"SECONDS"`)

* `MINUTES` (value: `"MINUTES"`)

* `HOURS` (value: `"HOURS"`)





## Enum: [RestrictedMetricTypeEnum]


* `RESTRICTED_METRIC_TYPE_UNSPECIFIED` (value: `"RESTRICTED_METRIC_TYPE_UNSPECIFIED"`)

* `COST_DATA` (value: `"COST_DATA"`)

* `REVENUE_DATA` (value: `"REVENUE_DATA"`)





## Enum: ScopeEnum


* `METRIC_SCOPE_UNSPECIFIED` (value: `"METRIC_SCOPE_UNSPECIFIED"`)

* `EVENT` (value: `"EVENT"`)




