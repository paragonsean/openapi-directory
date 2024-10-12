# GoogleSheetsApi.ChartSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**altText** | **String** | The alternative text that describes the chart. This is often used for accessibility. | [optional] 
**backgroundColor** | [**Color**](Color.md) |  | [optional] 
**backgroundColorStyle** | [**ColorStyle**](ColorStyle.md) |  | [optional] 
**basicChart** | [**BasicChartSpec**](BasicChartSpec.md) |  | [optional] 
**bubbleChart** | [**BubbleChartSpec**](BubbleChartSpec.md) |  | [optional] 
**candlestickChart** | [**CandlestickChartSpec**](CandlestickChartSpec.md) |  | [optional] 
**dataSourceChartProperties** | [**DataSourceChartProperties**](DataSourceChartProperties.md) |  | [optional] 
**filterSpecs** | [**[FilterSpec]**](FilterSpec.md) | The filters applied to the source data of the chart. Only supported for data source charts. | [optional] 
**fontName** | **String** | The name of the font to use by default for all chart text (e.g. title, axis labels, legend). If a font is specified for a specific part of the chart it will override this font name. | [optional] 
**hiddenDimensionStrategy** | **String** | Determines how the charts will use hidden rows or columns. | [optional] 
**histogramChart** | [**HistogramChartSpec**](HistogramChartSpec.md) |  | [optional] 
**maximized** | **Boolean** | True to make a chart fill the entire space in which it&#39;s rendered with minimum padding. False to use the default padding. (Not applicable to Geo and Org charts.) | [optional] 
**orgChart** | [**OrgChartSpec**](OrgChartSpec.md) |  | [optional] 
**pieChart** | [**PieChartSpec**](PieChartSpec.md) |  | [optional] 
**scorecardChart** | [**ScorecardChartSpec**](ScorecardChartSpec.md) |  | [optional] 
**sortSpecs** | [**[SortSpec]**](SortSpec.md) | The order to sort the chart data by. Only a single sort spec is supported. Only supported for data source charts. | [optional] 
**subtitle** | **String** | The subtitle of the chart. | [optional] 
**subtitleTextFormat** | [**TextFormat**](TextFormat.md) |  | [optional] 
**subtitleTextPosition** | [**TextPosition**](TextPosition.md) |  | [optional] 
**title** | **String** | The title of the chart. | [optional] 
**titleTextFormat** | [**TextFormat**](TextFormat.md) |  | [optional] 
**titleTextPosition** | [**TextPosition**](TextPosition.md) |  | [optional] 
**treemapChart** | [**TreemapChartSpec**](TreemapChartSpec.md) |  | [optional] 
**waterfallChart** | [**WaterfallChartSpec**](WaterfallChartSpec.md) |  | [optional] 



## Enum: HiddenDimensionStrategyEnum


* `CHART_HIDDEN_DIMENSION_STRATEGY_UNSPECIFIED` (value: `"CHART_HIDDEN_DIMENSION_STRATEGY_UNSPECIFIED"`)

* `SKIP_HIDDEN_ROWS_AND_COLUMNS` (value: `"SKIP_HIDDEN_ROWS_AND_COLUMNS"`)

* `SKIP_HIDDEN_ROWS` (value: `"SKIP_HIDDEN_ROWS"`)

* `SKIP_HIDDEN_COLUMNS` (value: `"SKIP_HIDDEN_COLUMNS"`)

* `SHOW_ALL` (value: `"SHOW_ALL"`)




