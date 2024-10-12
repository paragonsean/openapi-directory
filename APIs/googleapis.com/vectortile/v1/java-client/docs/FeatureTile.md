

# FeatureTile

A tile containing information about the map features located in the region it covers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**coordinates** | [**TileCoordinates**](TileCoordinates.md) |  |  [optional] |
|**features** | [**List&lt;Feature&gt;**](Feature.md) | Features present on this map tile. |  [optional] |
|**name** | **String** | Resource name of the tile. The tile resource name is prefixed by its collection ID &#x60;tiles/&#x60; followed by the resource ID, which encodes the tile&#39;s global x and y coordinates and zoom level as &#x60;@,,z&#x60;. For example, &#x60;tiles/@1,2,3z&#x60;. |  [optional] |
|**providers** | [**List&lt;ProviderInfo&gt;**](ProviderInfo.md) | Data providers for the data contained in this tile. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Tile response status code to support tile caching. |  [optional] |
|**versionId** | **String** | An opaque value, usually less than 30 characters, that contains version info about this tile and the data that was used to generate it. The client should store this value in its tile cache and pass it back to the API in the client_tile_version_id field of subsequent tile requests in order to enable the API to detect when the new tile would be the same as the one the client already has in its cache. Also see STATUS_OK_DATA_UNCHANGED. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;STATUS_OK&quot; |
| OK_DATA_UNCHANGED | &quot;STATUS_OK_DATA_UNCHANGED&quot; |



