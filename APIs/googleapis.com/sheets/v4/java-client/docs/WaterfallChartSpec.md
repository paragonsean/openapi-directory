

# WaterfallChartSpec

A waterfall chart.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectorLineStyle** | [**LineStyle**](LineStyle.md) |  |  [optional] |
|**domain** | [**WaterfallChartDomain**](WaterfallChartDomain.md) |  |  [optional] |
|**firstValueIsTotal** | **Boolean** | True to interpret the first value as a total. |  [optional] |
|**hideConnectorLines** | **Boolean** | True to hide connector lines between columns. |  [optional] |
|**series** | [**List&lt;WaterfallChartSeries&gt;**](WaterfallChartSeries.md) | The data this waterfall chart is visualizing. |  [optional] |
|**stackedType** | [**StackedTypeEnum**](#StackedTypeEnum) | The stacked type. |  [optional] |
|**totalDataLabel** | [**DataLabel**](DataLabel.md) |  |  [optional] |



## Enum: StackedTypeEnum

| Name | Value |
|---- | -----|
| WATERFALL_STACKED_TYPE_UNSPECIFIED | &quot;WATERFALL_STACKED_TYPE_UNSPECIFIED&quot; |
| STACKED | &quot;STACKED&quot; |
| SEQUENTIAL | &quot;SEQUENTIAL&quot; |



