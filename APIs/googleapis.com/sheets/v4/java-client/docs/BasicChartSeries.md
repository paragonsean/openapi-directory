

# BasicChartSeries

A single series of data in a chart. For example, if charting stock prices over time, multiple series may exist, one for the \"Open Price\", \"High Price\", \"Low Price\" and \"Close Price\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**color** | [**Color**](Color.md) |  |  [optional] |
|**colorStyle** | [**ColorStyle**](ColorStyle.md) |  |  [optional] |
|**dataLabel** | [**DataLabel**](DataLabel.md) |  |  [optional] |
|**lineStyle** | [**LineStyle**](LineStyle.md) |  |  [optional] |
|**pointStyle** | [**PointStyle**](PointStyle.md) |  |  [optional] |
|**series** | [**ChartData**](ChartData.md) |  |  [optional] |
|**styleOverrides** | [**List&lt;BasicSeriesDataPointStyleOverride&gt;**](BasicSeriesDataPointStyleOverride.md) | Style override settings for series data points. |  [optional] |
|**targetAxis** | [**TargetAxisEnum**](#TargetAxisEnum) | The minor axis that will specify the range of values for this series. For example, if charting stocks over time, the \&quot;Volume\&quot; series may want to be pinned to the right with the prices pinned to the left, because the scale of trading volume is different than the scale of prices. It is an error to specify an axis that isn&#39;t a valid minor axis for the chart&#39;s type. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this series. Valid only if the chartType is COMBO. Different types will change the way the series is visualized. Only LINE, AREA, and COLUMN are supported. |  [optional] |



## Enum: TargetAxisEnum

| Name | Value |
|---- | -----|
| BASIC_CHART_AXIS_POSITION_UNSPECIFIED | &quot;BASIC_CHART_AXIS_POSITION_UNSPECIFIED&quot; |
| BOTTOM_AXIS | &quot;BOTTOM_AXIS&quot; |
| LEFT_AXIS | &quot;LEFT_AXIS&quot; |
| RIGHT_AXIS | &quot;RIGHT_AXIS&quot; |



## Enum: TypeEnum

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



