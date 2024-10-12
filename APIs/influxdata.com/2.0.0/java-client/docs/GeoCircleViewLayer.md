

# GeoCircleViewLayer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**colorDimension** | [**Axis**](Axis.md) |  |  |
|**colorField** | **String** | Circle color field |  |
|**colors** | [**List&lt;DashboardColor&gt;**](DashboardColor.md) | Colors define color encoding of data into a visualization |  |
|**interpolateColors** | **Boolean** | Interpolate circle color based on displayed value |  [optional] |
|**radius** | **Integer** | Maximum radius size in pixels |  [optional] |
|**radiusDimension** | [**Axis**](Axis.md) |  |  |
|**radiusField** | **String** | Radius field |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HEATMAP | &quot;heatmap&quot; |
| CIRCLE_MAP | &quot;circleMap&quot; |
| POINT_MAP | &quot;pointMap&quot; |
| TRACK_MAP | &quot;trackMap&quot; |



