

# MosaicViewProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**colors** | **List&lt;String&gt;** | Colors define color encoding of data into a visualization |  |
|**fillColumns** | **List&lt;String&gt;** |  |  |
|**generateXAxisTicks** | **List&lt;String&gt;** |  |  [optional] |
|**hoverDimension** | [**HoverDimensionEnum**](#HoverDimensionEnum) |  |  [optional] |
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
|**yDomain** | **List&lt;BigDecimal&gt;** |  |  |
|**yLabelColumnSeparator** | **String** |  |  [optional] |
|**yLabelColumns** | **List&lt;String&gt;** |  |  [optional] |
|**yPrefix** | **String** |  |  |
|**ySeriesColumns** | **List&lt;String&gt;** |  |  |
|**ySuffix** | **String** |  |  |



## Enum: HoverDimensionEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| X | &quot;x&quot; |
| Y | &quot;y&quot; |
| XY | &quot;xy&quot; |



## Enum: ShapeEnum

| Name | Value |
|---- | -----|
| CHRONOGRAF_V2 | &quot;chronograf-v2&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MOSAIC | &quot;mosaic&quot; |



