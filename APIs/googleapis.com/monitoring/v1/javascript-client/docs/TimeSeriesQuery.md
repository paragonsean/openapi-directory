# CloudMonitoringApi.TimeSeriesQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opsAnalyticsQuery** | [**OpsAnalyticsQuery**](OpsAnalyticsQuery.md) |  | [optional] 
**outputFullDuration** | **Boolean** | Optional. If set, Cloud Monitoring will treat the full query duration as the alignment period so that there will be only 1 output value.*Note: This could override the configured alignment period except for the cases where a series of data points are expected, like - XyChart - Scorecard&#39;s spark chart | [optional] 
**prometheusQuery** | **String** | A query used to fetch time series with PromQL. | [optional] 
**timeSeriesFilter** | [**TimeSeriesFilter**](TimeSeriesFilter.md) |  | [optional] 
**timeSeriesFilterRatio** | [**TimeSeriesFilterRatio**](TimeSeriesFilterRatio.md) |  | [optional] 
**timeSeriesQueryLanguage** | **String** | A query used to fetch time series with MQL. | [optional] 
**unitOverride** | **String** | The unit of data contained in fetched time series. If non-empty, this unit will override any unit that accompanies fetched data. The format is the same as the unit (https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors) field in MetricDescriptor. | [optional] 


