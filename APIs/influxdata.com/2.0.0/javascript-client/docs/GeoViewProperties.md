# InfluxOssApiService.GeoViewProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowPanAndZoom** | **Boolean** | If true, map zoom and pan controls are enabled on the dashboard view | [default to true]
**center** | [**GeoViewPropertiesCenter**](GeoViewPropertiesCenter.md) |  | 
**colors** | [**[DashboardColor]**](DashboardColor.md) | Colors define color encoding of data into a visualization | [optional] 
**detectCoordinateFields** | **Boolean** | If true, search results get automatically regroupped so that lon,lat and value are treated as columns | [default to true]
**layers** | [**[GeoViewLayer]**](GeoViewLayer.md) | List of individual layers shown in the map | 
**mapStyle** | **String** | Define map type - regular, satellite etc. | [optional] 
**note** | **String** |  | 
**queries** | [**[DashboardQuery]**](DashboardQuery.md) |  | 
**shape** | **String** |  | 
**showNoteWhenEmpty** | **Boolean** | If true, will display note when empty | 
**type** | **String** |  | 
**zoom** | **Number** | Zoom level used for initial display of the map | 



## Enum: ShapeEnum


* `chronograf-v2` (value: `"chronograf-v2"`)





## Enum: TypeEnum


* `geo` (value: `"geo"`)




