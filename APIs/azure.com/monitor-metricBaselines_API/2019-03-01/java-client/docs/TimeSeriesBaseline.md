

# TimeSeriesBaseline

The baseline values for a single time series.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregation** | **String** | The aggregation type of the metric. |  |
|**data** | [**List&lt;SingleBaseline&gt;**](SingleBaseline.md) | The baseline values for each sensitivity. |  |
|**dimensions** | [**List&lt;MetricSingleDimension&gt;**](MetricSingleDimension.md) | The dimensions of this time series. |  [optional] |
|**metadata** | [**List&lt;BaselineMetadata&gt;**](BaselineMetadata.md) | The baseline metadata values. |  [optional] |
|**timestamps** | **List&lt;OffsetDateTime&gt;** | The list of timestamps of the baselines. |  |



