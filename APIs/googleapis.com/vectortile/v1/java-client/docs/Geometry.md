

# Geometry

Represents the geometry of a feature, that is, the shape that it has on the map. The local tile coordinate system has the origin at the north-west (upper-left) corner of the tile, and is scaled to 4096 units across each edge. The height (Z) axis has the same scale factor: an extruded area with a max_z value of 4096 has the same height as the width of the tile that it is on. There is no clipping boundary, so it is possible that some coordinates will lie outside the tile boundaries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**areas** | [**List&lt;Area&gt;**](Area.md) | The areas present in this geometry. |  [optional] |
|**extrudedAreas** | [**List&lt;ExtrudedArea&gt;**](ExtrudedArea.md) | The extruded areas present in this geometry. Not populated if modeled_volumes are included in this geometry unless always_include_building_footprints is set in GetFeatureTileRequest, in which case the client should decide which (extruded areas or modeled volumes) should be used (they should not be rendered together). |  [optional] |
|**lines** | [**List&lt;Line&gt;**](Line.md) | The lines present in this geometry. |  [optional] |
|**modeledVolumes** | [**List&lt;ModeledVolume&gt;**](ModeledVolume.md) | The modeled volumes present in this geometry. Not populated unless enable_modeled_volumes has been set in GetFeatureTileRequest. |  [optional] |



