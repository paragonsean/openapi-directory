

# TimeSeriesFilter

A filter that defines a subset of time series data that is displayed in a widget. Time series data is fetched using the ListTimeSeries (https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregation** | [**Aggregation**](Aggregation.md) |  |  [optional] |
|**filter** | **String** | Required. The monitoring filter (https://cloud.google.com/monitoring/api/v3/filters) that identifies the metric types, resources, and projects to query. |  [optional] |
|**pickTimeSeriesFilter** | [**PickTimeSeriesFilter**](PickTimeSeriesFilter.md) |  |  [optional] |
|**secondaryAggregation** | [**Aggregation**](Aggregation.md) |  |  [optional] |
|**statisticalTimeSeriesFilter** | [**StatisticalTimeSeriesFilter**](StatisticalTimeSeriesFilter.md) |  |  [optional] |



