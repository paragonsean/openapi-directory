

# ScorecardChartSpec

A scorecard chart. Scorecard charts are used to highlight key performance indicators, known as KPIs, on the spreadsheet. A scorecard chart can represent things like total sales, average cost, or a top selling item. You can specify a single data value, or aggregate over a range of data. Percentage or absolute difference from a baseline value can be highlighted, like changes over time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregateType** | [**AggregateTypeEnum**](#AggregateTypeEnum) | The aggregation type for key and baseline chart data in scorecard chart. This field is not supported for data source charts. Use the ChartData.aggregateType field of the key_value_data or baseline_value_data instead for data source charts. This field is optional. |  [optional] |
|**baselineValueData** | [**ChartData**](ChartData.md) |  |  [optional] |
|**baselineValueFormat** | [**BaselineValueFormat**](BaselineValueFormat.md) |  |  [optional] |
|**customFormatOptions** | [**ChartCustomNumberFormatOptions**](ChartCustomNumberFormatOptions.md) |  |  [optional] |
|**keyValueData** | [**ChartData**](ChartData.md) |  |  [optional] |
|**keyValueFormat** | [**KeyValueFormat**](KeyValueFormat.md) |  |  [optional] |
|**numberFormatSource** | [**NumberFormatSourceEnum**](#NumberFormatSourceEnum) | The number format source used in the scorecard chart. This field is optional. |  [optional] |
|**scaleFactor** | **Double** | Value to scale scorecard key and baseline value. For example, a factor of 10 can be used to divide all values in the chart by 10. This field is optional. |  [optional] |



## Enum: AggregateTypeEnum

| Name | Value |
|---- | -----|
| CHART_AGGREGATE_TYPE_UNSPECIFIED | &quot;CHART_AGGREGATE_TYPE_UNSPECIFIED&quot; |
| AVERAGE | &quot;AVERAGE&quot; |
| COUNT | &quot;COUNT&quot; |
| MAX | &quot;MAX&quot; |
| MEDIAN | &quot;MEDIAN&quot; |
| MIN | &quot;MIN&quot; |
| SUM | &quot;SUM&quot; |



## Enum: NumberFormatSourceEnum

| Name | Value |
|---- | -----|
| CHART_NUMBER_FORMAT_SOURCE_UNDEFINED | &quot;CHART_NUMBER_FORMAT_SOURCE_UNDEFINED&quot; |
| FROM_DATA | &quot;FROM_DATA&quot; |
| CUSTOM | &quot;CUSTOM&quot; |



