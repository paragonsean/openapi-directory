

# WaterfallChartSeries

A single series of data for a waterfall chart.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customSubtotals** | [**List&lt;WaterfallChartCustomSubtotal&gt;**](WaterfallChartCustomSubtotal.md) | Custom subtotal columns appearing in this series. The order in which subtotals are defined is not significant. Only one subtotal may be defined for each data point. |  [optional] |
|**data** | [**ChartData**](ChartData.md) |  |  [optional] |
|**dataLabel** | [**DataLabel**](DataLabel.md) |  |  [optional] |
|**hideTrailingSubtotal** | **Boolean** | True to hide the subtotal column from the end of the series. By default, a subtotal column will appear at the end of each series. Setting this field to true will hide that subtotal column for this series. |  [optional] |
|**negativeColumnsStyle** | [**WaterfallChartColumnStyle**](WaterfallChartColumnStyle.md) |  |  [optional] |
|**positiveColumnsStyle** | [**WaterfallChartColumnStyle**](WaterfallChartColumnStyle.md) |  |  [optional] |
|**subtotalColumnsStyle** | [**WaterfallChartColumnStyle**](WaterfallChartColumnStyle.md) |  |  [optional] |



