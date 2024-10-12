

# ChartSpec

The specifications of a chart.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**altText** | **String** | The alternative text that describes the chart. This is often used for accessibility. |  [optional] |
|**backgroundColor** | [**Color**](Color.md) |  |  [optional] |
|**backgroundColorStyle** | [**ColorStyle**](ColorStyle.md) |  |  [optional] |
|**basicChart** | [**BasicChartSpec**](BasicChartSpec.md) |  |  [optional] |
|**bubbleChart** | [**BubbleChartSpec**](BubbleChartSpec.md) |  |  [optional] |
|**candlestickChart** | [**CandlestickChartSpec**](CandlestickChartSpec.md) |  |  [optional] |
|**dataSourceChartProperties** | [**DataSourceChartProperties**](DataSourceChartProperties.md) |  |  [optional] |
|**filterSpecs** | [**List&lt;FilterSpec&gt;**](FilterSpec.md) | The filters applied to the source data of the chart. Only supported for data source charts. |  [optional] |
|**fontName** | **String** | The name of the font to use by default for all chart text (e.g. title, axis labels, legend). If a font is specified for a specific part of the chart it will override this font name. |  [optional] |
|**hiddenDimensionStrategy** | [**HiddenDimensionStrategyEnum**](#HiddenDimensionStrategyEnum) | Determines how the charts will use hidden rows or columns. |  [optional] |
|**histogramChart** | [**HistogramChartSpec**](HistogramChartSpec.md) |  |  [optional] |
|**maximized** | **Boolean** | True to make a chart fill the entire space in which it&#39;s rendered with minimum padding. False to use the default padding. (Not applicable to Geo and Org charts.) |  [optional] |
|**orgChart** | [**OrgChartSpec**](OrgChartSpec.md) |  |  [optional] |
|**pieChart** | [**PieChartSpec**](PieChartSpec.md) |  |  [optional] |
|**scorecardChart** | [**ScorecardChartSpec**](ScorecardChartSpec.md) |  |  [optional] |
|**sortSpecs** | [**List&lt;SortSpec&gt;**](SortSpec.md) | The order to sort the chart data by. Only a single sort spec is supported. Only supported for data source charts. |  [optional] |
|**subtitle** | **String** | The subtitle of the chart. |  [optional] |
|**subtitleTextFormat** | [**TextFormat**](TextFormat.md) |  |  [optional] |
|**subtitleTextPosition** | [**TextPosition**](TextPosition.md) |  |  [optional] |
|**title** | **String** | The title of the chart. |  [optional] |
|**titleTextFormat** | [**TextFormat**](TextFormat.md) |  |  [optional] |
|**titleTextPosition** | [**TextPosition**](TextPosition.md) |  |  [optional] |
|**treemapChart** | [**TreemapChartSpec**](TreemapChartSpec.md) |  |  [optional] |
|**waterfallChart** | [**WaterfallChartSpec**](WaterfallChartSpec.md) |  |  [optional] |



## Enum: HiddenDimensionStrategyEnum

| Name | Value |
|---- | -----|
| CHART_HIDDEN_DIMENSION_STRATEGY_UNSPECIFIED | &quot;CHART_HIDDEN_DIMENSION_STRATEGY_UNSPECIFIED&quot; |
| SKIP_HIDDEN_ROWS_AND_COLUMNS | &quot;SKIP_HIDDEN_ROWS_AND_COLUMNS&quot; |
| SKIP_HIDDEN_ROWS | &quot;SKIP_HIDDEN_ROWS&quot; |
| SKIP_HIDDEN_COLUMNS | &quot;SKIP_HIDDEN_COLUMNS&quot; |
| SHOW_ALL | &quot;SHOW_ALL&quot; |



