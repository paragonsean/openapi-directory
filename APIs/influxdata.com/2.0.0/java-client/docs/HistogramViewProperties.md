

# HistogramViewProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**binCount** | **Integer** |  |  |
|**colors** | [**List&lt;DashboardColor&gt;**](DashboardColor.md) | Colors define color encoding of data into a visualization |  |
|**fillColumns** | **List&lt;String&gt;** |  |  |
|**legendColorizeRows** | **Boolean** |  |  [optional] |
|**legendHide** | **Boolean** |  |  [optional] |
|**legendOpacity** | **Float** |  |  [optional] |
|**legendOrientationThreshold** | **Integer** |  |  [optional] |
|**note** | **String** |  |  |
|**position** | [**PositionEnum**](#PositionEnum) |  |  |
|**queries** | [**List&lt;DashboardQuery&gt;**](DashboardQuery.md) |  |  |
|**shape** | [**ShapeEnum**](#ShapeEnum) |  |  |
|**showNoteWhenEmpty** | **Boolean** | If true, will display note when empty |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**xAxisLabel** | **String** |  |  |
|**xColumn** | **String** |  |  |
|**xDomain** | **List&lt;Float&gt;** |  |  |



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
| HISTOGRAM | &quot;histogram&quot; |



