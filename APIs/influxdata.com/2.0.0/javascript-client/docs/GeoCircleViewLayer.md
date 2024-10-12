# InfluxOssApiService.GeoCircleViewLayer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **String** |  | 
**colorDimension** | [**Axis**](Axis.md) |  | 
**colorField** | **String** | Circle color field | 
**colors** | [**[DashboardColor]**](DashboardColor.md) | Colors define color encoding of data into a visualization | 
**interpolateColors** | **Boolean** | Interpolate circle color based on displayed value | [optional] 
**radius** | **Number** | Maximum radius size in pixels | [optional] 
**radiusDimension** | [**Axis**](Axis.md) |  | 
**radiusField** | **String** | Radius field | 



## Enum: TypeEnum


* `heatmap` (value: `"heatmap"`)

* `circleMap` (value: `"circleMap"`)

* `pointMap` (value: `"pointMap"`)

* `trackMap` (value: `"trackMap"`)




