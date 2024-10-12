

# TimeSeriesTable

A table that displays time series data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnSettings** | [**List&lt;ColumnSettings&gt;**](ColumnSettings.md) | Optional. The list of the persistent column settings for the table. |  [optional] |
|**dataSets** | [**List&lt;TableDataSet&gt;**](TableDataSet.md) | Required. The data displayed in this table. |  [optional] |
|**metricVisualization** | [**MetricVisualizationEnum**](#MetricVisualizationEnum) | Optional. Store rendering strategy |  [optional] |



## Enum: MetricVisualizationEnum

| Name | Value |
|---- | -----|
| METRIC_VISUALIZATION_UNSPECIFIED | &quot;METRIC_VISUALIZATION_UNSPECIFIED&quot; |
| NUMBER | &quot;NUMBER&quot; |
| BAR | &quot;BAR&quot; |



