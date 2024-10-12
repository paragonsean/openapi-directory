# SemanticTileApi.Line

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basemapZOrder** | [**BasemapZOrder**](BasemapZOrder.md) |  | [optional] 
**vertexOffsets** | [**Vertex2DList**](Vertex2DList.md) |  | [optional] 
**zOrder** | **Number** | The z-order of the line. Lines with a lower z-order should be rendered beneath lines with a higher z-order. This z-ordering does not imply anything about the altitude of the area relative to the ground, but it can be used to prevent z-fighting during rendering on the client. In general, larger and more important road features will have a higher z-order line associated with them. This z-ordering can only be used to compare lines, and cannot be compared with the z_order field in the Area message. The z-order may be negative or zero. Prefer Line.basemap_z_order. | [optional] 


