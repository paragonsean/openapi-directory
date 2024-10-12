# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atAnyPointInTime** | **Boolean** | Optional. Indicates whether this filter needs dynamic evaluation or not. If set to true, users join the Audience if they ever met the condition (static evaluation). If unset or set to false, user evaluation for an Audience is dynamic; users are added to an Audience when they meet the conditions and then removed when they no longer meet them. This can only be set when Audience scope is ACROSS_ALL_SESSIONS. | [optional] 
**betweenFilter** | [**GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter**](GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter.md) |  | [optional] 
**fieldName** | **String** | Required. Immutable. The dimension name or metric name to filter. If the field name refers to a custom dimension or metric, a scope prefix will be added to the front of the custom dimensions or metric name. For more on scope prefixes or custom dimensions/metrics, reference the [Google Analytics Data API documentation] (https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#custom_dimensions). | [optional] 
**inAnyNDayPeriod** | **Number** | Optional. If set, specifies the time window for which to evaluate data in number of days. If not set, then audience data is evaluated against lifetime data (For example, infinite time window). For example, if set to 1 day, only the current day&#39;s data is evaluated. The reference point is the current day when at_any_point_in_time is unset or false. It can only be set when Audience scope is ACROSS_ALL_SESSIONS and cannot be greater than 60 days. | [optional] 
**inListFilter** | [**GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter**](GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter.md) |  | [optional] 
**numericFilter** | [**GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter**](GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter.md) |  | [optional] 
**stringFilter** | [**GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter**](GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter.md) |  | [optional] 


