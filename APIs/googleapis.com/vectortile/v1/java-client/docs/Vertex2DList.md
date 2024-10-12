

# Vertex2DList

2D vertex list used for lines and areas. Each entry represents an offset from the previous one in local tile coordinates. The first entry is offset from (0, 0). For example, the list of vertices [(1,1), (2, 2), (1, 2)] would be encoded in vertex offsets as [(1, 1), (1, 1), (-1, 0)].

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**xOffsets** | **List&lt;Integer&gt;** | List of x-offsets in local tile coordinates. |  [optional] |
|**yOffsets** | **List&lt;Integer&gt;** | List of y-offsets in local tile coordinates. |  [optional] |



