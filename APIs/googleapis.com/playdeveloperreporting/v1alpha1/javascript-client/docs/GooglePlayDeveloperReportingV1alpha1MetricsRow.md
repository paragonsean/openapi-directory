# GooglePlayDeveloperReportingApi.GooglePlayDeveloperReportingV1alpha1MetricsRow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregationPeriod** | **String** | Granularity of the aggregation period of the row. | [optional] 
**dimensions** | [**[GooglePlayDeveloperReportingV1alpha1DimensionValue]**](GooglePlayDeveloperReportingV1alpha1DimensionValue.md) | Dimension columns in the row. | [optional] 
**metrics** | [**[GooglePlayDeveloperReportingV1alpha1MetricValue]**](GooglePlayDeveloperReportingV1alpha1MetricValue.md) | Metric columns in the row. | [optional] 
**startTime** | [**GoogleTypeDateTime**](GoogleTypeDateTime.md) |  | [optional] 



## Enum: AggregationPeriodEnum


* `AGGREGATION_PERIOD_UNSPECIFIED` (value: `"AGGREGATION_PERIOD_UNSPECIFIED"`)

* `HOURLY` (value: `"HOURLY"`)

* `DAILY` (value: `"DAILY"`)

* `FULL_RANGE` (value: `"FULL_RANGE"`)




