

# GeoViewLayer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**colorDimension** | [**Axis**](Axis.md) |  |  |
|**colorField** | **String** | Marker color field |  |
|**colors** | [**List&lt;DashboardColor&gt;**](DashboardColor.md) | Colors define color encoding of data into a visualization |  |
|**interpolateColors** | **Boolean** | Interpolate circle color based on displayed value |  [optional] |
|**radius** | **Integer** | Radius size in pixels |  |
|**radiusDimension** | [**Axis**](Axis.md) |  |  |
|**radiusField** | **String** | Radius field |  |
|**blur** | **Integer** | Blur for heatmap points |  |
|**intensityDimension** | [**Axis**](Axis.md) |  |  |
|**intensityField** | **String** | Intensity field |  |
|**isClustered** | **Boolean** | Cluster close markers together |  [optional] |
|**randomColors** | **Boolean** | Assign different colors to different tracks |  |
|**speed** | **Integer** | Speed of the track animation |  |
|**trackWidth** | **Integer** | Width of the track |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HEATMAP | &quot;heatmap&quot; |
| CIRCLE_MAP | &quot;circleMap&quot; |
| POINT_MAP | &quot;pointMap&quot; |
| TRACK_MAP | &quot;trackMap&quot; |



