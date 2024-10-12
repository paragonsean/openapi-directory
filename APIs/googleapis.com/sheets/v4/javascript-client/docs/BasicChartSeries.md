# GoogleSheetsApi.BasicChartSeries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**Color**](Color.md) |  | [optional] 
**colorStyle** | [**ColorStyle**](ColorStyle.md) |  | [optional] 
**dataLabel** | [**DataLabel**](DataLabel.md) |  | [optional] 
**lineStyle** | [**LineStyle**](LineStyle.md) |  | [optional] 
**pointStyle** | [**PointStyle**](PointStyle.md) |  | [optional] 
**series** | [**ChartData**](ChartData.md) |  | [optional] 
**styleOverrides** | [**[BasicSeriesDataPointStyleOverride]**](BasicSeriesDataPointStyleOverride.md) | Style override settings for series data points. | [optional] 
**targetAxis** | **String** | The minor axis that will specify the range of values for this series. For example, if charting stocks over time, the \&quot;Volume\&quot; series may want to be pinned to the right with the prices pinned to the left, because the scale of trading volume is different than the scale of prices. It is an error to specify an axis that isn&#39;t a valid minor axis for the chart&#39;s type. | [optional] 
**type** | **String** | The type of this series. Valid only if the chartType is COMBO. Different types will change the way the series is visualized. Only LINE, AREA, and COLUMN are supported. | [optional] 



## Enum: TargetAxisEnum


* `BASIC_CHART_AXIS_POSITION_UNSPECIFIED` (value: `"BASIC_CHART_AXIS_POSITION_UNSPECIFIED"`)

* `BOTTOM_AXIS` (value: `"BOTTOM_AXIS"`)

* `LEFT_AXIS` (value: `"LEFT_AXIS"`)

* `RIGHT_AXIS` (value: `"RIGHT_AXIS"`)





## Enum: TypeEnum


* `BASIC_CHART_TYPE_UNSPECIFIED` (value: `"BASIC_CHART_TYPE_UNSPECIFIED"`)

* `BAR` (value: `"BAR"`)

* `LINE` (value: `"LINE"`)

* `AREA` (value: `"AREA"`)

* `COLUMN` (value: `"COLUMN"`)

* `SCATTER` (value: `"SCATTER"`)

* `COMBO` (value: `"COMBO"`)

* `STEPPED_AREA` (value: `"STEPPED_AREA"`)




