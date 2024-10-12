# CloudMonitoringApi.WindowsBasedSli

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goodBadMetricFilter** | **String** | A monitoring filter (https://cloud.google.com/monitoring/api/v3/filters) specifying a TimeSeries with ValueType &#x3D; BOOL. The window is good if any true values appear in the window. | [optional] 
**goodTotalRatioThreshold** | [**PerformanceThreshold**](PerformanceThreshold.md) |  | [optional] 
**metricMeanInRange** | [**MetricRange**](MetricRange.md) |  | [optional] 
**metricSumInRange** | [**MetricRange**](MetricRange.md) |  | [optional] 
**windowPeriod** | **String** | Duration over which window quality is evaluated. Must be an integer fraction of a day and at least 60s. | [optional] 


