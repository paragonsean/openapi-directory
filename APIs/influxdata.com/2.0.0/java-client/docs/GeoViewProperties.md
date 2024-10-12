

# GeoViewProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowPanAndZoom** | **Boolean** | If true, map zoom and pan controls are enabled on the dashboard view |  |
|**center** | [**GeoViewPropertiesCenter**](GeoViewPropertiesCenter.md) |  |  |
|**colors** | [**List&lt;DashboardColor&gt;**](DashboardColor.md) | Colors define color encoding of data into a visualization |  [optional] |
|**detectCoordinateFields** | **Boolean** | If true, search results get automatically regroupped so that lon,lat and value are treated as columns |  |
|**layers** | [**List&lt;GeoViewLayer&gt;**](GeoViewLayer.md) | List of individual layers shown in the map |  |
|**mapStyle** | **String** | Define map type - regular, satellite etc. |  [optional] |
|**note** | **String** |  |  |
|**queries** | [**List&lt;DashboardQuery&gt;**](DashboardQuery.md) |  |  |
|**shape** | [**ShapeEnum**](#ShapeEnum) |  |  |
|**showNoteWhenEmpty** | **Boolean** | If true, will display note when empty |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**zoom** | **Double** | Zoom level used for initial display of the map |  |



## Enum: ShapeEnum

| Name | Value |
|---- | -----|
| CHRONOGRAF_V2 | &quot;chronograf-v2&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GEO | &quot;geo&quot; |



