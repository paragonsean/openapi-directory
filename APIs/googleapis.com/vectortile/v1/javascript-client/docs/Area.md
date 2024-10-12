# SemanticTileApi.Area

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basemapZOrder** | [**BasemapZOrder**](BasemapZOrder.md) |  | [optional] 
**hasExternalEdges** | **Boolean** | True if the polygon is not entirely internal to the feature that it belongs to: that is, some of the edges are bordering another feature. | [optional] 
**internalEdges** | **[Number]** | When has_external_edges is true, the polygon has some edges that border another feature. This field indicates the internal edges that do not border another feature. Each value is an index into the vertices array, and denotes the start vertex of the internal edge (the next vertex in the boundary loop is the end of the edge). If the selected vertex is the last vertex in the boundary loop, then the edge between that vertex and the starting vertex of the loop is internal. This field may be used for styling. For example, building parapets could be placed only on the external edges of a building polygon, or water could be lighter colored near the external edges of a body of water. If has_external_edges is false, all edges are internal and this field will be empty. | [optional] 
**loopBreaks** | **[Number]** | Identifies the boundary loops of the polygon. Only set for INDEXED_TRIANGLE polygons. Each value is an index into the vertices array indicating the beginning of a loop. For instance, values of [2, 5] would indicate loop_data contained 3 loops with indices 0-1, 2-4, and 5-end. This may be used in conjunction with the internal_edges field for styling polygon boundaries. Note that an edge may be on a polygon boundary but still internal to the feature. For example, a feature split across multiple tiles will have an internal polygon boundary edge along the edge of the tile. | [optional] 
**triangleIndices** | **[Number]** | When the polygon encoding is of type INDEXED_TRIANGLES, this contains the indices of the triangle vertices in the vertex_offsets field. There are 3 vertex indices per triangle. | [optional] 
**type** | **String** | The polygon encoding type used for this area. | [optional] 
**vertexOffsets** | [**Vertex2DList**](Vertex2DList.md) |  | [optional] 
**zOrder** | **Number** | The z-ordering of this area. Areas with a lower z-order should be rendered beneath areas with a higher z-order. This z-ordering does not imply anything about the altitude of the line relative to the ground, but it can be used to prevent z-fighting during rendering on the client. This z-ordering can only be used to compare areas, and cannot be compared with the z_order field in the Line message. The z-order may be negative or zero. Prefer Area.basemap_z_order. | [optional] 



## Enum: TypeEnum


* `TRIANGLE_FAN` (value: `"TRIANGLE_FAN"`)

* `INDEXED_TRIANGLES` (value: `"INDEXED_TRIANGLES"`)

* `TRIANGLE_STRIP` (value: `"TRIANGLE_STRIP"`)




