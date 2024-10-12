# InfluxOssApiService.MosaicViewProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colors** | **[String]** | Colors define color encoding of data into a visualization | 
**fillColumns** | **[String]** |  | 
**generateXAxisTicks** | **[String]** |  | [optional] 
**hoverDimension** | **String** |  | [optional] 
**legendColorizeRows** | **Boolean** |  | [optional] 
**legendHide** | **Boolean** |  | [optional] 
**legendOpacity** | **Number** |  | [optional] 
**legendOrientationThreshold** | **Number** |  | [optional] 
**note** | **String** |  | 
**queries** | [**[DashboardQuery]**](DashboardQuery.md) |  | 
**shape** | **String** |  | 
**showNoteWhenEmpty** | **Boolean** | If true, will display note when empty | 
**timeFormat** | **String** |  | [optional] 
**type** | **String** |  | 
**xAxisLabel** | **String** |  | 
**xColumn** | **String** |  | 
**xDomain** | **[Number]** |  | 
**xPrefix** | **String** |  | 
**xSuffix** | **String** |  | 
**xTickStart** | **Number** |  | [optional] 
**xTickStep** | **Number** |  | [optional] 
**xTotalTicks** | **Number** |  | [optional] 
**yAxisLabel** | **String** |  | 
**yDomain** | **[Number]** |  | 
**yLabelColumnSeparator** | **String** |  | [optional] 
**yLabelColumns** | **[String]** |  | [optional] 
**yPrefix** | **String** |  | 
**ySeriesColumns** | **[String]** |  | 
**ySuffix** | **String** |  | 



## Enum: HoverDimensionEnum


* `auto` (value: `"auto"`)

* `x` (value: `"x"`)

* `y` (value: `"y"`)

* `xy` (value: `"xy"`)





## Enum: ShapeEnum


* `chronograf-v2` (value: `"chronograf-v2"`)





## Enum: TypeEnum


* `mosaic` (value: `"mosaic"`)




