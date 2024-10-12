# MonitorManagementClient.MetricBaselinesProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baselines** | [**[TimeSeriesBaseline]**](TimeSeriesBaseline.md) | The baseline for each time series that was queried. | 
**interval** | **String** | The interval (window size) for which the metric data was returned in.  This may be adjusted in the future and returned back from what was originally requested.  This is not present if a metadata request was made. | 
**namespace** | **String** | The namespace of the metrics been queried. | [optional] 
**timespan** | **String** | The timespan for which the data was retrieved. Its value consists of two datetimes concatenated, separated by &#39;/&#39;.  This may be adjusted in the future and returned back from what was originally requested. | 


