

# PieChart

A widget that displays timeseries data as a pie or a donut.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chartType** | [**ChartTypeEnum**](#ChartTypeEnum) | Required. Indicates the visualization type for the PieChart. |  [optional] |
|**dataSets** | [**List&lt;PieChartDataSet&gt;**](PieChartDataSet.md) | Required. The queries for the chart&#39;s data. |  [optional] |
|**showLabels** | **Boolean** | Optional. Indicates whether or not the pie chart should show slices&#39; labels |  [optional] |



## Enum: ChartTypeEnum

| Name | Value |
|---- | -----|
| PIE_CHART_TYPE_UNSPECIFIED | &quot;PIE_CHART_TYPE_UNSPECIFIED&quot; |
| PIE | &quot;PIE&quot; |
| DONUT | &quot;DONUT&quot; |



