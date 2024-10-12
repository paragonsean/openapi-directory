

# SparkChartView

A sparkChart is a small chart suitable for inclusion in a table-cell or inline in text. This message contains the configuration for a sparkChart to show up on a Scorecard, showing recent trends of the scorecard's timeseries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**minAlignmentPeriod** | **String** | The lower bound on data point frequency in the chart implemented by specifying the minimum alignment period to use in a time series query. For example, if the data is published once every 10 minutes it would not make sense to fetch and align data at one minute intervals. This field is optional and exists only as a hint. |  [optional] |
|**sparkChartType** | [**SparkChartTypeEnum**](#SparkChartTypeEnum) | Required. The type of sparkchart to show in this chartView. |  [optional] |



## Enum: SparkChartTypeEnum

| Name | Value |
|---- | -----|
| CHART_TYPE_UNSPECIFIED | &quot;SPARK_CHART_TYPE_UNSPECIFIED&quot; |
| LINE | &quot;SPARK_LINE&quot; |
| BAR | &quot;SPARK_BAR&quot; |



