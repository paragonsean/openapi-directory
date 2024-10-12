# CloudMonitoringApi.StatisticalTimeSeriesFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numTimeSeries** | **Number** | How many time series to output. | [optional] 
**rankingMethod** | **String** | rankingMethod is applied to a set of time series, and then the produced value for each individual time series is used to compare a given time series to others. These are methods that cannot be applied stream-by-stream, but rather require the full context of a request to evaluate time series. | [optional] 



## Enum: RankingMethodEnum


* `UNSPECIFIED` (value: `"METHOD_UNSPECIFIED"`)

* `CLUSTER_OUTLIER` (value: `"METHOD_CLUSTER_OUTLIER"`)




