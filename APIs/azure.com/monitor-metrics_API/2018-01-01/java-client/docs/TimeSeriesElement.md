

# TimeSeriesElement

A time series result type. The discriminator value is always TimeSeries in this case.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**List&lt;MetricValue&gt;**](MetricValue.md) | An array of data points representing the metric values.  This is only returned if a result type of data is specified. |  [optional] |
|**metadatavalues** | [**List&lt;MetadataValue&gt;**](MetadataValue.md) | the metadata values returned if $filter was specified in the call. |  [optional] |



