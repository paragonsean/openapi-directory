

# TriangleStrip

Represents a strip of triangles. Each triangle uses the last edge of the previous one. The following diagram shows an example of a triangle strip, with each vertex labeled with its index in the vertex_index array. (1)-----(3) / \\ / \\ / \\ / \\ / \\ / \\ (0)-----(2)-----(4) Vertices may be in either clockwise or counter-clockwise order.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**vertexIndices** | **List&lt;Integer&gt;** | Index into the vertex_offset array representing the next vertex in the triangle strip. |  [optional] |



