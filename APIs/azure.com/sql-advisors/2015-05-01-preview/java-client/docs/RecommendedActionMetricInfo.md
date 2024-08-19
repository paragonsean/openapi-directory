

# RecommendedActionMetricInfo

Contains time series of various impacted metrics for an Azure SQL Database, Server or Elastic Pool Recommended Action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricName** | **String** | Gets the name of the metric. e.g., CPU, Number of Queries. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | Gets the start time of time interval given by this MetricInfo. |  [optional] [readonly] |
|**timeGrain** | **String** | Gets the duration of time interval for the value given by this MetricInfo. e.g., PT1H (1 hour) |  [optional] [readonly] |
|**unit** | **String** | Gets the unit in which metric is measured. e.g., DTU, Frequency |  [optional] [readonly] |
|**value** | **Double** | Gets the value of the metric in the time interval given by this MetricInfo. |  [optional] [readonly] |



