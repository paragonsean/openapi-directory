# Maps.VectorApi

All URIs are relative to *https://api.tomtom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapVersionNumberTileLayerStyleZoomXYPbfGet**](VectorApi.md#mapVersionNumberTileLayerStyleZoomXYPbfGet) | **GET** /map/{versionNumber}/tile/{layer}/{style}/{zoom}/{X}/{Y}.pbf | Tile



## mapVersionNumberTileLayerStyleZoomXYPbfGet

> mapVersionNumberTileLayerStyleZoomXYPbfGet(versionNumber, layer, style, zoom, X, Y, opts)

Tile

The Maps API Vector Service delivers vector tiles, which are representations of square sections of map data.

### Example

```javascript
import Maps from 'maps';
let defaultClient = Maps.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Maps.VectorApi();
let versionNumber = 56; // Number | Version of the service to call. The current version is 1
let layer = "basic"; // String | Layer of tile to be rendered
let style = "main"; // String | Style of tile to be rendered
let zoom = 0; // Number | Zoom level of tile to be rendered
let X = 0; // Number | x coordinate of tile on zoom grid
let Y = 0; // Number | y coordinate of tile on zoom grid
let opts = {
  'view': "Unified", // String | Geopolitical view. Determines rendering of disputed areas. See the <a href=\"/maps-api/maps-api-documentation-vector/tile\">documentation</a> for an explanation of how this works in live services.
  'language': "'NGT'" // String | Language to be used for labels in the response. The default is NGT: Neutral Ground Truth, which uses each place's local official language and script (where available). See the <a href=\"/maps-api/maps-api-documentation-vector/tile\">documentation</a> for a full list of options.
};
apiInstance.mapVersionNumberTileLayerStyleZoomXYPbfGet(versionNumber, layer, style, zoom, X, Y, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionNumber** | **Number**| Version of the service to call. The current version is 1 | 
 **layer** | **String**| Layer of tile to be rendered | 
 **style** | **String**| Style of tile to be rendered | 
 **zoom** | **Number**| Zoom level of tile to be rendered | 
 **X** | **Number**| x coordinate of tile on zoom grid | 
 **Y** | **Number**| y coordinate of tile on zoom grid | 
 **view** | **String**| Geopolitical view. Determines rendering of disputed areas. See the &lt;a href&#x3D;\&quot;/maps-api/maps-api-documentation-vector/tile\&quot;&gt;documentation&lt;/a&gt; for an explanation of how this works in live services. | [optional] 
 **language** | **String**| Language to be used for labels in the response. The default is NGT: Neutral Ground Truth, which uses each place&#39;s local official language and script (where available). See the &lt;a href&#x3D;\&quot;/maps-api/maps-api-documentation-vector/tile\&quot;&gt;documentation&lt;/a&gt; for a full list of options. | [optional] [default to &#39;NGT&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

