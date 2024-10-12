

# ReportRow

A row of the returning report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensionValues** | [**Map&lt;String, ReportRowDimensionValue&gt;**](ReportRowDimensionValue.md) | Map of dimension values in a row, with keys as enum name of the dimensions. |  [optional] |
|**metricValues** | [**Map&lt;String, ReportRowMetricValue&gt;**](ReportRowMetricValue.md) | Map of metric values in a row, with keys as enum name of the metrics. If a metric being requested has no value returned, the map will not include it. |  [optional] |



