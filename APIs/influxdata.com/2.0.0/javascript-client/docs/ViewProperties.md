# InfluxOssApiService.ViewProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**axes** | [**Axes**](Axes.md) |  | 
**colors** | [**[DashboardColor]**](DashboardColor.md) | Colors define color encoding of data into a visualization | 
**decimalPlaces** | [**DecimalPlaces**](DecimalPlaces.md) |  | 
**generateXAxisTicks** | **[String]** |  | [optional] 
**generateYAxisTicks** | **[String]** |  | [optional] 
**hoverDimension** | **String** |  | [optional] 
**legendColorizeRows** | **Boolean** |  | [optional] 
**legendHide** | **Boolean** |  | [optional] 
**legendOpacity** | **Number** |  | [optional] 
**legendOrientationThreshold** | **Number** |  | [optional] 
**note** | **String** |  | 
**position** | **String** |  | 
**prefix** | **String** |  | 
**queries** | [**[DashboardQuery]**](DashboardQuery.md) |  | 
**shadeBelow** | **Boolean** |  | [optional] 
**shape** | **String** |  | 
**showNoteWhenEmpty** | **Boolean** | If true, will display note when empty | 
**staticLegend** | [**StaticLegend**](StaticLegend.md) |  | [optional] 
**suffix** | **String** |  | 
**timeFormat** | **String** |  | 
**type** | **String** |  | 
**xColumn** | **String** |  | 
**xTickStart** | **Number** |  | [optional] 
**xTickStep** | **Number** |  | [optional] 
**xTotalTicks** | **Number** |  | [optional] 
**yColumn** | **String** |  | 
**yTickStart** | **Number** |  | [optional] 
**yTickStep** | **Number** |  | [optional] 
**yTotalTicks** | **Number** |  | [optional] 
**geom** | [**XYGeom**](XYGeom.md) |  | 
**tickPrefix** | **String** |  | 
**tickSuffix** | **String** |  | 
**binCount** | **Number** |  | 
**fillColumns** | **[String]** |  | 
**xAxisLabel** | **String** |  | 
**xDomain** | **[Number]** |  | 
**fieldOptions** | [**[RenamableField]**](RenamableField.md) | fieldOptions represent the fields retrieved by the query with customization options | 
**tableOptions** | [**TableViewPropertiesTableOptions**](TableViewPropertiesTableOptions.md) |  | 
**check** | [**Check**](Check.md) |  | [optional] 
**checkID** | **String** |  | 
**symbolColumns** | **[String]** |  | 
**xPrefix** | **String** |  | 
**xSuffix** | **String** |  | 
**yAxisLabel** | **String** |  | 
**yDomain** | **[Number]** |  | 
**yPrefix** | **String** |  | 
**ySuffix** | **String** |  | 
**binSize** | **Number** |  | 
**yLabelColumnSeparator** | **String** |  | [optional] 
**yLabelColumns** | **[String]** |  | [optional] 
**ySeriesColumns** | **[String]** |  | 
**lowerColumn** | **String** |  | [optional] 
**mainColumn** | **String** |  | [optional] 
**upperColumn** | **String** |  | [optional] 
**allowPanAndZoom** | **Boolean** | If true, map zoom and pan controls are enabled on the dashboard view | [default to true]
**center** | [**GeoViewPropertiesCenter**](GeoViewPropertiesCenter.md) |  | 
**detectCoordinateFields** | **Boolean** | If true, search results get automatically regroupped so that lon,lat and value are treated as columns | [default to true]
**layers** | [**[GeoViewLayer]**](GeoViewLayer.md) | List of individual layers shown in the map | 
**mapStyle** | **String** | Define map type - regular, satellite etc. | [optional] 
**zoom** | **Number** | Zoom level used for initial display of the map | 



## Enum: HoverDimensionEnum


* `auto` (value: `"auto"`)

* `x` (value: `"x"`)

* `y` (value: `"y"`)

* `xy` (value: `"xy"`)





## Enum: PositionEnum


* `overlaid` (value: `"overlaid"`)

* `stacked` (value: `"stacked"`)





## Enum: ShapeEnum


* `chronograf-v2` (value: `"chronograf-v2"`)





## Enum: TypeEnum


* `line-plus-single-stat` (value: `"line-plus-single-stat"`)

* `xy` (value: `"xy"`)

* `single-stat` (value: `"single-stat"`)

* `histogram` (value: `"histogram"`)

* `gauge` (value: `"gauge"`)

* `table` (value: `"table"`)

* `markdown` (value: `"markdown"`)

* `check` (value: `"check"`)

* `scatter` (value: `"scatter"`)

* `heatmap` (value: `"heatmap"`)

* `mosaic` (value: `"mosaic"`)

* `band` (value: `"band"`)

* `geo` (value: `"geo"`)




