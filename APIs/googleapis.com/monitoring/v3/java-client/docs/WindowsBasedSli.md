

# WindowsBasedSli

A WindowsBasedSli defines good_service as the count of time windows for which the provided service was of good quality. Criteria for determining if service was good are embedded in the window_criterion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**goodBadMetricFilter** | **String** | A monitoring filter (https://cloud.google.com/monitoring/api/v3/filters) specifying a TimeSeries with ValueType &#x3D; BOOL. The window is good if any true values appear in the window. |  [optional] |
|**goodTotalRatioThreshold** | [**PerformanceThreshold**](PerformanceThreshold.md) |  |  [optional] |
|**metricMeanInRange** | [**MetricRange**](MetricRange.md) |  |  [optional] |
|**metricSumInRange** | [**MetricRange**](MetricRange.md) |  |  [optional] |
|**windowPeriod** | **String** | Duration over which window quality is evaluated. Must be an integer fraction of a day and at least 60s. |  [optional] |



