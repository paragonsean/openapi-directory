

# HeatmapViewProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**binSize** | **BigDecimal** |  |  |
|**colors** | **List&lt;String&gt;** | Colors define color encoding of data into a visualization |  |
|**generateXAxisTicks** | **List&lt;String&gt;** |  |  [optional] |
|**generateYAxisTicks** | **List&lt;String&gt;** |  |  [optional] |
|**legendColorizeRows** | **Boolean** |  |  [optional] |
|**legendHide** | **Boolean** |  |  [optional] |
|**legendOpacity** | **Float** |  |  [optional] |
|**legendOrientationThreshold** | **Integer** |  |  [optional] |
|**note** | **String** |  |  |
|**queries** | [**List&lt;DashboardQuery&gt;**](DashboardQuery.md) |  |  |
|**shape** | [**ShapeEnum**](#ShapeEnum) |  |  |
|**showNoteWhenEmpty** | **Boolean** | If true, will display note when empty |  |
|**timeFormat** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**xAxisLabel** | **String** |  |  |
|**xColumn** | **String** |  |  |
|**xDomain** | **List&lt;BigDecimal&gt;** |  |  |
|**xPrefix** | **String** |  |  |
|**xSuffix** | **String** |  |  |
|**xTickStart** | **Float** |  |  [optional] |
|**xTickStep** | **Float** |  |  [optional] |
|**xTotalTicks** | **Integer** |  |  [optional] |
|**yAxisLabel** | **String** |  |  |
|**yColumn** | **String** |  |  |
|**yDomain** | **List&lt;BigDecimal&gt;** |  |  |
|**yPrefix** | **String** |  |  |
|**ySuffix** | **String** |  |  |
|**yTickStart** | **Float** |  |  [optional] |
|**yTickStep** | **Float** |  |  [optional] |
|**yTotalTicks** | **Integer** |  |  [optional] |



## Enum: ShapeEnum

| Name | Value |
|---- | -----|
| CHRONOGRAF_V2 | &quot;chronograf-v2&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HEATMAP | &quot;heatmap&quot; |



