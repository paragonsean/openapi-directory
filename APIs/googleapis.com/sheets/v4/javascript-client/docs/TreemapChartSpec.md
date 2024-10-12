# GoogleSheetsApi.TreemapChartSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colorData** | [**ChartData**](ChartData.md) |  | [optional] 
**colorScale** | [**TreemapChartColorScale**](TreemapChartColorScale.md) |  | [optional] 
**headerColor** | [**Color**](Color.md) |  | [optional] 
**headerColorStyle** | [**ColorStyle**](ColorStyle.md) |  | [optional] 
**hideTooltips** | **Boolean** | True to hide tooltips. | [optional] 
**hintedLevels** | **Number** | The number of additional data levels beyond the labeled levels to be shown on the treemap chart. These levels are not interactive and are shown without their labels. Defaults to 0 if not specified. | [optional] 
**labels** | [**ChartData**](ChartData.md) |  | [optional] 
**levels** | **Number** | The number of data levels to show on the treemap chart. These levels are interactive and are shown with their labels. Defaults to 2 if not specified. | [optional] 
**maxValue** | **Number** | The maximum possible data value. Cells with values greater than this will have the same color as cells with this value. If not specified, defaults to the actual maximum value from color_data, or the maximum value from size_data if color_data is not specified. | [optional] 
**minValue** | **Number** | The minimum possible data value. Cells with values less than this will have the same color as cells with this value. If not specified, defaults to the actual minimum value from color_data, or the minimum value from size_data if color_data is not specified. | [optional] 
**parentLabels** | [**ChartData**](ChartData.md) |  | [optional] 
**sizeData** | [**ChartData**](ChartData.md) |  | [optional] 
**textFormat** | [**TextFormat**](TextFormat.md) |  | [optional] 


