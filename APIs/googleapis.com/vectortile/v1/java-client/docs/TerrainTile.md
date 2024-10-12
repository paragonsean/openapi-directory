

# TerrainTile

A tile containing information about the terrain located in the region it covers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**coordinates** | [**TileCoordinates**](TileCoordinates.md) |  |  [optional] |
|**firstDerivative** | [**FirstDerivativeElevationGrid**](FirstDerivativeElevationGrid.md) |  |  [optional] |
|**name** | **String** | Resource name of the tile. The tile resource name is prefixed by its collection ID &#x60;terrain/&#x60; followed by the resource ID, which encodes the tile&#39;s global x and y coordinates and zoom level as &#x60;@,,z&#x60;. For example, &#x60;terrain/@1,2,3z&#x60;. |  [optional] |
|**secondDerivative** | [**SecondDerivativeElevationGrid**](SecondDerivativeElevationGrid.md) |  |  [optional] |



