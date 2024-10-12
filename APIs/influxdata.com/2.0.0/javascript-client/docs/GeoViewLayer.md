# InfluxOssApiService.GeoViewLayer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **String** |  | 
**colorDimension** | [**Axis**](Axis.md) |  | 
**colorField** | **String** | Marker color field | 
**colors** | [**[DashboardColor]**](DashboardColor.md) | Colors define color encoding of data into a visualization | 
**interpolateColors** | **Boolean** | Interpolate circle color based on displayed value | [optional] 
**radius** | **Number** | Radius size in pixels | 
**radiusDimension** | [**Axis**](Axis.md) |  | 
**radiusField** | **String** | Radius field | 
**blur** | **Number** | Blur for heatmap points | 
**intensityDimension** | [**Axis**](Axis.md) |  | 
**intensityField** | **String** | Intensity field | 
**isClustered** | **Boolean** | Cluster close markers together | [optional] 
**randomColors** | **Boolean** | Assign different colors to different tracks | 
**speed** | **Number** | Speed of the track animation | 
**trackWidth** | **Number** | Width of the track | 



## Enum: TypeEnum


* `heatmap` (value: `"heatmap"`)

* `circleMap` (value: `"circleMap"`)

* `pointMap` (value: `"pointMap"`)

* `trackMap` (value: `"trackMap"`)




