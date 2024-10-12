

# QueryRequest

Request to execute a time series query over events. Exactly one of \"getEvents\", \"getSeries\" or \"aggregateSeries\" must be set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregateSeries** | [**AggregateSeries**](AggregateSeries.md) |  |  [optional] |
|**getEvents** | [**GetEvents**](GetEvents.md) |  |  [optional] |
|**getSeries** | [**GetSeries**](GetSeries.md) |  |  [optional] |



