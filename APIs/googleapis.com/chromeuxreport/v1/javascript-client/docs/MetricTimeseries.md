# ChromeUxReportApi.MetricTimeseries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fractionTimeseries** | [**{String: FractionTimeseries}**](FractionTimeseries.md) | Mapping from labels to timeseries of fractions attributed to this label. | [optional] 
**histogramTimeseries** | [**[TimeseriesBin]**](TimeseriesBin.md) | The histogram of user experiences for a metric. The histogram will have at least one bin and the densities of all bins will add up to ~1, for each timeseries entry. | [optional] 
**percentilesTimeseries** | [**TimeseriesPercentiles**](TimeseriesPercentiles.md) |  | [optional] 


