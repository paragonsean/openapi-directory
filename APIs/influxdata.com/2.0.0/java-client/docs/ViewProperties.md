

# ViewProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**axes** | [**Axes**](Axes.md) |  |  |
|**colors** | [**List&lt;DashboardColor&gt;**](DashboardColor.md) | Colors define color encoding of data into a visualization |  |
|**decimalPlaces** | [**DecimalPlaces**](DecimalPlaces.md) |  |  |
|**generateXAxisTicks** | **List&lt;String&gt;** |  |  [optional] |
|**generateYAxisTicks** | **List&lt;String&gt;** |  |  [optional] |
|**hoverDimension** | [**HoverDimensionEnum**](#HoverDimensionEnum) |  |  [optional] |
|**legendColorizeRows** | **Boolean** |  |  [optional] |
|**legendHide** | **Boolean** |  |  [optional] |
|**legendOpacity** | **Float** |  |  [optional] |
|**legendOrientationThreshold** | **Integer** |  |  [optional] |
|**note** | **String** |  |  |
|**position** | [**PositionEnum**](#PositionEnum) |  |  |
|**prefix** | **String** |  |  |
|**queries** | [**List&lt;DashboardQuery&gt;**](DashboardQuery.md) |  |  |
|**shadeBelow** | **Boolean** |  |  [optional] |
|**shape** | [**ShapeEnum**](#ShapeEnum) |  |  |
|**showNoteWhenEmpty** | **Boolean** | If true, will display note when empty |  |
|**staticLegend** | [**StaticLegend**](StaticLegend.md) |  |  [optional] |
|**suffix** | **String** |  |  |
|**timeFormat** | **String** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**xColumn** | **String** |  |  |
|**xTickStart** | **Float** |  |  [optional] |
|**xTickStep** | **Float** |  |  [optional] |
|**xTotalTicks** | **Integer** |  |  [optional] |
|**yColumn** | **String** |  |  |
|**yTickStart** | **Float** |  |  [optional] |
|**yTickStep** | **Float** |  |  [optional] |
|**yTotalTicks** | **Integer** |  |  [optional] |
|**geom** | **XYGeom** |  |  |
|**tickPrefix** | **String** |  |  |
|**tickSuffix** | **String** |  |  |
|**binCount** | **Integer** |  |  |
|**fillColumns** | **List&lt;String&gt;** |  |  |
|**xAxisLabel** | **String** |  |  |
|**xDomain** | **List&lt;BigDecimal&gt;** |  |  |
|**fieldOptions** | [**List&lt;RenamableField&gt;**](RenamableField.md) | fieldOptions represent the fields retrieved by the query with customization options |  |
|**tableOptions** | [**TableViewPropertiesTableOptions**](TableViewPropertiesTableOptions.md) |  |  |
|**check** | [**Check**](Check.md) |  |  [optional] |
|**checkID** | **String** |  |  |
|**symbolColumns** | **List&lt;String&gt;** |  |  |
|**xPrefix** | **String** |  |  |
|**xSuffix** | **String** |  |  |
|**yAxisLabel** | **String** |  |  |
|**yDomain** | **List&lt;BigDecimal&gt;** |  |  |
|**yPrefix** | **String** |  |  |
|**ySuffix** | **String** |  |  |
|**binSize** | **BigDecimal** |  |  |
|**yLabelColumnSeparator** | **String** |  |  [optional] |
|**yLabelColumns** | **List&lt;String&gt;** |  |  [optional] |
|**ySeriesColumns** | **List&lt;String&gt;** |  |  |
|**lowerColumn** | **String** |  |  [optional] |
|**mainColumn** | **String** |  |  [optional] |
|**upperColumn** | **String** |  |  [optional] |
|**allowPanAndZoom** | **Boolean** | If true, map zoom and pan controls are enabled on the dashboard view |  |
|**center** | [**GeoViewPropertiesCenter**](GeoViewPropertiesCenter.md) |  |  |
|**detectCoordinateFields** | **Boolean** | If true, search results get automatically regroupped so that lon,lat and value are treated as columns |  |
|**layers** | [**List&lt;GeoViewLayer&gt;**](GeoViewLayer.md) | List of individual layers shown in the map |  |
|**mapStyle** | **String** | Define map type - regular, satellite etc. |  [optional] |
|**zoom** | **Double** | Zoom level used for initial display of the map |  |



## Enum: HoverDimensionEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| X | &quot;x&quot; |
| Y | &quot;y&quot; |
| XY | &quot;xy&quot; |



## Enum: PositionEnum

| Name | Value |
|---- | -----|
| OVERLAID | &quot;overlaid&quot; |
| STACKED | &quot;stacked&quot; |



## Enum: ShapeEnum

| Name | Value |
|---- | -----|
| CHRONOGRAF_V2 | &quot;chronograf-v2&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LINE_PLUS_SINGLE_STAT | &quot;line-plus-single-stat&quot; |
| XY | &quot;xy&quot; |
| SINGLE_STAT | &quot;single-stat&quot; |
| HISTOGRAM | &quot;histogram&quot; |
| GAUGE | &quot;gauge&quot; |
| TABLE | &quot;table&quot; |
| MARKDOWN | &quot;markdown&quot; |
| CHECK | &quot;check&quot; |
| SCATTER | &quot;scatter&quot; |
| HEATMAP | &quot;heatmap&quot; |
| MOSAIC | &quot;mosaic&quot; |
| BAND | &quot;band&quot; |
| GEO | &quot;geo&quot; |



