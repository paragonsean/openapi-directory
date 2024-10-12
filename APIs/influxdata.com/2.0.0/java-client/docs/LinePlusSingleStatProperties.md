

# LinePlusSingleStatProperties


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
|**timeFormat** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**xColumn** | **String** |  |  [optional] |
|**xTickStart** | **Float** |  |  [optional] |
|**xTickStep** | **Float** |  |  [optional] |
|**xTotalTicks** | **Integer** |  |  [optional] |
|**yColumn** | **String** |  |  [optional] |
|**yTickStart** | **Float** |  |  [optional] |
|**yTickStep** | **Float** |  |  [optional] |
|**yTotalTicks** | **Integer** |  |  [optional] |



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



