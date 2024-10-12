

# GooglePlayDeveloperReportingV1alpha1MetricsRow

Represents a row of dimensions and metrics.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationPeriod** | [**AggregationPeriodEnum**](#AggregationPeriodEnum) | Granularity of the aggregation period of the row. |  [optional] |
|**dimensions** | [**List&lt;GooglePlayDeveloperReportingV1alpha1DimensionValue&gt;**](GooglePlayDeveloperReportingV1alpha1DimensionValue.md) | Dimension columns in the row. |  [optional] |
|**metrics** | [**List&lt;GooglePlayDeveloperReportingV1alpha1MetricValue&gt;**](GooglePlayDeveloperReportingV1alpha1MetricValue.md) | Metric columns in the row. |  [optional] |
|**startTime** | [**GoogleTypeDateTime**](GoogleTypeDateTime.md) |  |  [optional] |



## Enum: AggregationPeriodEnum

| Name | Value |
|---- | -----|
| AGGREGATION_PERIOD_UNSPECIFIED | &quot;AGGREGATION_PERIOD_UNSPECIFIED&quot; |
| HOURLY | &quot;HOURLY&quot; |
| DAILY | &quot;DAILY&quot; |
| FULL_RANGE | &quot;FULL_RANGE&quot; |



