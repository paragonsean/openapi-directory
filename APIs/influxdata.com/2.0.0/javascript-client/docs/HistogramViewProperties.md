# InfluxOssApiService.HistogramViewProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binCount** | **Number** |  | 
**colors** | [**[DashboardColor]**](DashboardColor.md) | Colors define color encoding of data into a visualization | 
**fillColumns** | **[String]** |  | 
**legendColorizeRows** | **Boolean** |  | [optional] 
**legendHide** | **Boolean** |  | [optional] 
**legendOpacity** | **Number** |  | [optional] 
**legendOrientationThreshold** | **Number** |  | [optional] 
**note** | **String** |  | 
**position** | **String** |  | 
**queries** | [**[DashboardQuery]**](DashboardQuery.md) |  | 
**shape** | **String** |  | 
**showNoteWhenEmpty** | **Boolean** | If true, will display note when empty | 
**type** | **String** |  | 
**xAxisLabel** | **String** |  | 
**xColumn** | **String** |  | 
**xDomain** | **[Number]** |  | 



## Enum: PositionEnum


* `overlaid` (value: `"overlaid"`)

* `stacked` (value: `"stacked"`)





## Enum: ShapeEnum


* `chronograf-v2` (value: `"chronograf-v2"`)





## Enum: TypeEnum


* `histogram` (value: `"histogram"`)




