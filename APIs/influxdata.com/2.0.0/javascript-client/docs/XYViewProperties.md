# InfluxOssApiService.XYViewProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**axes** | [**Axes**](Axes.md) |  | 
**colors** | [**[DashboardColor]**](DashboardColor.md) | Colors define color encoding of data into a visualization | 
**generateXAxisTicks** | **[String]** |  | [optional] 
**generateYAxisTicks** | **[String]** |  | [optional] 
**geom** | [**XYGeom**](XYGeom.md) |  | 
**hoverDimension** | **String** |  | [optional] 
**legendColorizeRows** | **Boolean** |  | [optional] 
**legendHide** | **Boolean** |  | [optional] 
**legendOpacity** | **Number** |  | [optional] 
**legendOrientationThreshold** | **Number** |  | [optional] 
**note** | **String** |  | 
**position** | **String** |  | 
**queries** | [**[DashboardQuery]**](DashboardQuery.md) |  | 
**shadeBelow** | **Boolean** |  | [optional] 
**shape** | **String** |  | 
**showNoteWhenEmpty** | **Boolean** | If true, will display note when empty | 
**staticLegend** | [**StaticLegend**](StaticLegend.md) |  | [optional] 
**timeFormat** | **String** |  | [optional] 
**type** | **String** |  | 
**xColumn** | **String** |  | [optional] 
**xTickStart** | **Number** |  | [optional] 
**xTickStep** | **Number** |  | [optional] 
**xTotalTicks** | **Number** |  | [optional] 
**yColumn** | **String** |  | [optional] 
**yTickStart** | **Number** |  | [optional] 
**yTickStep** | **Number** |  | [optional] 
**yTotalTicks** | **Number** |  | [optional] 



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


* `xy` (value: `"xy"`)




