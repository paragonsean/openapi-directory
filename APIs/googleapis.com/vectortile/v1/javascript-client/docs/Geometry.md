# SemanticTileApi.Geometry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**areas** | [**[Area]**](Area.md) | The areas present in this geometry. | [optional] 
**extrudedAreas** | [**[ExtrudedArea]**](ExtrudedArea.md) | The extruded areas present in this geometry. Not populated if modeled_volumes are included in this geometry unless always_include_building_footprints is set in GetFeatureTileRequest, in which case the client should decide which (extruded areas or modeled volumes) should be used (they should not be rendered together). | [optional] 
**lines** | [**[Line]**](Line.md) | The lines present in this geometry. | [optional] 
**modeledVolumes** | [**[ModeledVolume]**](ModeledVolume.md) | The modeled volumes present in this geometry. Not populated unless enable_modeled_volumes has been set in GetFeatureTileRequest. | [optional] 


