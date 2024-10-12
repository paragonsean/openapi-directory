

# ExtrudedArea

Represents a height-extruded area: a 3D prism with a constant X-Y plane cross section. Used to represent extruded buildings. A single building may consist of several extruded areas. The min_z and max_z fields are scaled to the size of the tile. An extruded area with a max_z value of 4096 has the same height as the width of the tile that it is on.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**area** | [**Area**](Area.md) |  |  [optional] |
|**maxZ** | **Integer** | The z-value in local tile coordinates where the extruded area ends. |  [optional] |
|**minZ** | **Integer** | The z-value in local tile coordinates where the extruded area begins. This is non-zero for extruded areas that begin off the ground. For example, a building with a skybridge may have an extruded area component with a non-zero min_z. |  [optional] |



