# GoogleSheetsApi.BasicChartSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**axis** | [**[BasicChartAxis]**](BasicChartAxis.md) | The axis on the chart. | [optional] 
**chartType** | **String** | The type of the chart. | [optional] 
**compareMode** | **String** | The behavior of tooltips and data highlighting when hovering on data and chart area. | [optional] 
**domains** | [**[BasicChartDomain]**](BasicChartDomain.md) | The domain of data this is charting. Only a single domain is supported. | [optional] 
**headerCount** | **Number** | The number of rows or columns in the data that are \&quot;headers\&quot;. If not set, Google Sheets will guess how many rows are headers based on the data. (Note that BasicChartAxis.title may override the axis title inferred from the header values.) | [optional] 
**interpolateNulls** | **Boolean** | If some values in a series are missing, gaps may appear in the chart (e.g, segments of lines in a line chart will be missing). To eliminate these gaps set this to true. Applies to Line, Area, and Combo charts. | [optional] 
**legendPosition** | **String** | The position of the chart legend. | [optional] 
**lineSmoothing** | **Boolean** | Gets whether all lines should be rendered smooth or straight by default. Applies to Line charts. | [optional] 
**series** | [**[BasicChartSeries]**](BasicChartSeries.md) | The data this chart is visualizing. | [optional] 
**stackedType** | **String** | The stacked type for charts that support vertical stacking. Applies to Area, Bar, Column, Combo, and Stepped Area charts. | [optional] 
**threeDimensional** | **Boolean** | True to make the chart 3D. Applies to Bar and Column charts. | [optional] 
**totalDataLabel** | [**DataLabel**](DataLabel.md) |  | [optional] 



## Enum: ChartTypeEnum


* `BASIC_CHART_TYPE_UNSPECIFIED` (value: `"BASIC_CHART_TYPE_UNSPECIFIED"`)

* `BAR` (value: `"BAR"`)

* `LINE` (value: `"LINE"`)

* `AREA` (value: `"AREA"`)

* `COLUMN` (value: `"COLUMN"`)

* `SCATTER` (value: `"SCATTER"`)

* `COMBO` (value: `"COMBO"`)

* `STEPPED_AREA` (value: `"STEPPED_AREA"`)





## Enum: CompareModeEnum


* `BASIC_CHART_COMPARE_MODE_UNSPECIFIED` (value: `"BASIC_CHART_COMPARE_MODE_UNSPECIFIED"`)

* `DATUM` (value: `"DATUM"`)

* `CATEGORY` (value: `"CATEGORY"`)





## Enum: LegendPositionEnum


* `BASIC_CHART_LEGEND_POSITION_UNSPECIFIED` (value: `"BASIC_CHART_LEGEND_POSITION_UNSPECIFIED"`)

* `BOTTOM_LEGEND` (value: `"BOTTOM_LEGEND"`)

* `LEFT_LEGEND` (value: `"LEFT_LEGEND"`)

* `RIGHT_LEGEND` (value: `"RIGHT_LEGEND"`)

* `TOP_LEGEND` (value: `"TOP_LEGEND"`)

* `NO_LEGEND` (value: `"NO_LEGEND"`)





## Enum: StackedTypeEnum


* `BASIC_CHART_STACKED_TYPE_UNSPECIFIED` (value: `"BASIC_CHART_STACKED_TYPE_UNSPECIFIED"`)

* `NOT_STACKED` (value: `"NOT_STACKED"`)

* `STACKED` (value: `"STACKED"`)

* `PERCENT_STACKED` (value: `"PERCENT_STACKED"`)




