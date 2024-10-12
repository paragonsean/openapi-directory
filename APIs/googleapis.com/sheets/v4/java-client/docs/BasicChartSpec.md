

# BasicChartSpec

The specification for a basic chart. See BasicChartType for the list of charts this supports.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**axis** | [**List&lt;BasicChartAxis&gt;**](BasicChartAxis.md) | The axis on the chart. |  [optional] |
|**chartType** | [**ChartTypeEnum**](#ChartTypeEnum) | The type of the chart. |  [optional] |
|**compareMode** | [**CompareModeEnum**](#CompareModeEnum) | The behavior of tooltips and data highlighting when hovering on data and chart area. |  [optional] |
|**domains** | [**List&lt;BasicChartDomain&gt;**](BasicChartDomain.md) | The domain of data this is charting. Only a single domain is supported. |  [optional] |
|**headerCount** | **Integer** | The number of rows or columns in the data that are \&quot;headers\&quot;. If not set, Google Sheets will guess how many rows are headers based on the data. (Note that BasicChartAxis.title may override the axis title inferred from the header values.) |  [optional] |
|**interpolateNulls** | **Boolean** | If some values in a series are missing, gaps may appear in the chart (e.g, segments of lines in a line chart will be missing). To eliminate these gaps set this to true. Applies to Line, Area, and Combo charts. |  [optional] |
|**legendPosition** | [**LegendPositionEnum**](#LegendPositionEnum) | The position of the chart legend. |  [optional] |
|**lineSmoothing** | **Boolean** | Gets whether all lines should be rendered smooth or straight by default. Applies to Line charts. |  [optional] |
|**series** | [**List&lt;BasicChartSeries&gt;**](BasicChartSeries.md) | The data this chart is visualizing. |  [optional] |
|**stackedType** | [**StackedTypeEnum**](#StackedTypeEnum) | The stacked type for charts that support vertical stacking. Applies to Area, Bar, Column, Combo, and Stepped Area charts. |  [optional] |
|**threeDimensional** | **Boolean** | True to make the chart 3D. Applies to Bar and Column charts. |  [optional] |
|**totalDataLabel** | [**DataLabel**](DataLabel.md) |  |  [optional] |



## Enum: ChartTypeEnum

| Name | Value |
|---- | -----|
| BASIC_CHART_TYPE_UNSPECIFIED | &quot;BASIC_CHART_TYPE_UNSPECIFIED&quot; |
| BAR | &quot;BAR&quot; |
| LINE | &quot;LINE&quot; |
| AREA | &quot;AREA&quot; |
| COLUMN | &quot;COLUMN&quot; |
| SCATTER | &quot;SCATTER&quot; |
| COMBO | &quot;COMBO&quot; |
| STEPPED_AREA | &quot;STEPPED_AREA&quot; |



## Enum: CompareModeEnum

| Name | Value |
|---- | -----|
| BASIC_CHART_COMPARE_MODE_UNSPECIFIED | &quot;BASIC_CHART_COMPARE_MODE_UNSPECIFIED&quot; |
| DATUM | &quot;DATUM&quot; |
| CATEGORY | &quot;CATEGORY&quot; |



## Enum: LegendPositionEnum

| Name | Value |
|---- | -----|
| BASIC_CHART_LEGEND_POSITION_UNSPECIFIED | &quot;BASIC_CHART_LEGEND_POSITION_UNSPECIFIED&quot; |
| BOTTOM_LEGEND | &quot;BOTTOM_LEGEND&quot; |
| LEFT_LEGEND | &quot;LEFT_LEGEND&quot; |
| RIGHT_LEGEND | &quot;RIGHT_LEGEND&quot; |
| TOP_LEGEND | &quot;TOP_LEGEND&quot; |
| NO_LEGEND | &quot;NO_LEGEND&quot; |



## Enum: StackedTypeEnum

| Name | Value |
|---- | -----|
| BASIC_CHART_STACKED_TYPE_UNSPECIFIED | &quot;BASIC_CHART_STACKED_TYPE_UNSPECIFIED&quot; |
| NOT_STACKED | &quot;NOT_STACKED&quot; |
| STACKED | &quot;STACKED&quot; |
| PERCENT_STACKED | &quot;PERCENT_STACKED&quot; |



