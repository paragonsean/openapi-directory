

# MapInfo

Geo information used for rendering a map that shows the user's work location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lat** | **Double** | Latitude in degrees |  [optional] |
|**locationUrl** | [**SafeUrlProto**](SafeUrlProto.md) |  |  [optional] |
|**_long** | **Double** | Longitude in degrees |  [optional] |
|**mapTile** | [**List&lt;MapTile&gt;**](MapTile.md) | MapTiles for the area around a user&#39;s work location |  [optional] |
|**zoom** | **Integer** | The zoom level of the map. A constant zoom value of 18 is used for now to match the zoom of the map shown on a Moma Teams Profile page |  [optional] |



