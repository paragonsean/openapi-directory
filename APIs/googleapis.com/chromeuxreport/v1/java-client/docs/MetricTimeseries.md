

# MetricTimeseries

A `metric timeseries` is a set of user experience data for a single web performance metric, like \"first contentful paint\". It contains a summary histogram of real world Chrome usage as a series of `bins`, where each bin has density values for a particular time period.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fractionTimeseries** | [**Map&lt;String, FractionTimeseries&gt;**](FractionTimeseries.md) | Mapping from labels to timeseries of fractions attributed to this label. |  [optional] |
|**histogramTimeseries** | [**List&lt;TimeseriesBin&gt;**](TimeseriesBin.md) | The histogram of user experiences for a metric. The histogram will have at least one bin and the densities of all bins will add up to ~1, for each timeseries entry. |  [optional] |
|**percentilesTimeseries** | [**TimeseriesPercentiles**](TimeseriesPercentiles.md) |  |  [optional] |



