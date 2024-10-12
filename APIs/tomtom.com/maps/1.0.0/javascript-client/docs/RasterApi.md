# Maps.RasterApi

All URIs are relative to *https://api.tomtom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapVersionNumberStaticimageGet**](RasterApi.md#mapVersionNumberStaticimageGet) | **GET** /map/{versionNumber}/staticimage | Static Image
[**mapVersionNumberTileLayerStyleZoomXYFormatGet**](RasterApi.md#mapVersionNumberTileLayerStyleZoomXYFormatGet) | **GET** /map/{versionNumber}/tile/{layer}/{style}/{zoom}/{X}/{Y}.{format} | Tile



## mapVersionNumberStaticimageGet

> mapVersionNumberStaticimageGet(versionNumber, opts)

Static Image

The Static Image service renders a rectangular raster image in the style, size, and zoom level specified. The image can be requested using either a center point plus width and height or a bounding box.

### Example

```javascript
import Maps from 'maps';
let defaultClient = Maps.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Maps.RasterApi();
let versionNumber = 56; // Number | Version of the service to call. The current version is 1.
let opts = {
  'layer': "basic", // String | Layer of image to be rendered. <em>Hybrid</em> and <em>labels</em> are intended for layering with other data and are only available in <em>png</em> format.
  'style': "main", // String | Map style to be returned
  'format': "png", // String | Image format to be returned
  'zoom': 12, // Number | Zoom level of map image to be returned.
  'center': "4.899886, 52.379031", // String | Coordinates for the center point of the image. Must be used with the <strong>width</strong> and <strong>height</strong> parameters; cannot be used with <strong>bbox</strong>. Uses EPSG:3857 projection (functionally equivalent to EPSG:900910).
  'width': 512, // Number | Width of the resulting image in pixels. Width must be a positive integer between 1 and 8192.
  'height': 512, // Number | Height of the resulting image in pixels. Height must be a positive integer between 1 and 8192.
  'bbox': "bbox_example", // String | Bounding box for the image, using EPSG:3857 projection (functionally equivalent to EPSG:900910). Values <strong>must</strong> be in the order of minLon, minLat, maxLon, maxLat. MaxLat must be greater than minLat. Longitude values can be on both sides of the 180th meridian. Cannot be used with <strong>center</strong>, <strong>width</strong>, or <strong>height</strong> parameters.
  'view': "Unified" // String | Geopolitical view. Determines rendering of disputed areas. See the <a href=\"/maps-api/maps-api-documentation-raster/raster-tile\">documentation</a> for an explanation of how this works in live services.
};
apiInstance.mapVersionNumberStaticimageGet(versionNumber, opts, (error, data, response) => {
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
 **versionNumber** | **Number**| Version of the service to call. The current version is 1. | 
 **layer** | **String**| Layer of image to be rendered. &lt;em&gt;Hybrid&lt;/em&gt; and &lt;em&gt;labels&lt;/em&gt; are intended for layering with other data and are only available in &lt;em&gt;png&lt;/em&gt; format. | [optional] [default to &#39;basic&#39;]
 **style** | **String**| Map style to be returned | [optional] [default to &#39;main&#39;]
 **format** | **String**| Image format to be returned | [optional] [default to &#39;png&#39;]
 **zoom** | **Number**| Zoom level of map image to be returned. | [optional] [default to 12]
 **center** | **String**| Coordinates for the center point of the image. Must be used with the &lt;strong&gt;width&lt;/strong&gt; and &lt;strong&gt;height&lt;/strong&gt; parameters; cannot be used with &lt;strong&gt;bbox&lt;/strong&gt;. Uses EPSG:3857 projection (functionally equivalent to EPSG:900910). | [optional] 
 **width** | **Number**| Width of the resulting image in pixels. Width must be a positive integer between 1 and 8192. | [optional] [default to 512]
 **height** | **Number**| Height of the resulting image in pixels. Height must be a positive integer between 1 and 8192. | [optional] [default to 512]
 **bbox** | **String**| Bounding box for the image, using EPSG:3857 projection (functionally equivalent to EPSG:900910). Values &lt;strong&gt;must&lt;/strong&gt; be in the order of minLon, minLat, maxLon, maxLat. MaxLat must be greater than minLat. Longitude values can be on both sides of the 180th meridian. Cannot be used with &lt;strong&gt;center&lt;/strong&gt;, &lt;strong&gt;width&lt;/strong&gt;, or &lt;strong&gt;height&lt;/strong&gt; parameters. | [optional] 
 **view** | **String**| Geopolitical view. Determines rendering of disputed areas. See the &lt;a href&#x3D;\&quot;/maps-api/maps-api-documentation-raster/raster-tile\&quot;&gt;documentation&lt;/a&gt; for an explanation of how this works in live services. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## mapVersionNumberTileLayerStyleZoomXYFormatGet

> mapVersionNumberTileLayerStyleZoomXYFormatGet(versionNumber, layer, style, zoom, X, Y, format, opts)

Tile

The Maps API Raster Service delivers raster tiles, which are representations of square sections of map data.

### Example

```javascript
import Maps from 'maps';
let defaultClient = Maps.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Maps.RasterApi();
let versionNumber = 56; // Number | Version of the service to call. The current version is 1.
let layer = "basic"; // String | Layer of tile to be rendered. <em>Hybrid</em> and <em>labels</em> are intended for layering with other data and are only available in <em>png</em> format.
let style = "main"; // String | Style of tile to be rendered
let zoom = 0; // Number | Zoom level of tile to be rendered
let X = 0; // Number | x coordinate of tile on zoom grid
let Y = 0; // Number | y coordinate of tile on zoom grid
let format = "png"; // String | Format of the response.
let opts = {
  'tileSize': 256, // Number | Tile dimensions in pixels. <em>512</em> is only available for the <em>main</em> style and <em>basic</em> or <em>labels</em> layers.
  'view': "Unified" // String | Geopolitical view. Determines rendering of disputed areas. See the <a href=\"/maps-sdk-web/functional-examples#geopolitical-views\">documentation</a> for an explanation of how this works in live services.
};
apiInstance.mapVersionNumberTileLayerStyleZoomXYFormatGet(versionNumber, layer, style, zoom, X, Y, format, opts, (error, data, response) => {
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
 **versionNumber** | **Number**| Version of the service to call. The current version is 1. | 
 **layer** | **String**| Layer of tile to be rendered. &lt;em&gt;Hybrid&lt;/em&gt; and &lt;em&gt;labels&lt;/em&gt; are intended for layering with other data and are only available in &lt;em&gt;png&lt;/em&gt; format. | 
 **style** | **String**| Style of tile to be rendered | 
 **zoom** | **Number**| Zoom level of tile to be rendered | 
 **X** | **Number**| x coordinate of tile on zoom grid | 
 **Y** | **Number**| y coordinate of tile on zoom grid | 
 **format** | **String**| Format of the response. | 
 **tileSize** | **Number**| Tile dimensions in pixels. &lt;em&gt;512&lt;/em&gt; is only available for the &lt;em&gt;main&lt;/em&gt; style and &lt;em&gt;basic&lt;/em&gt; or &lt;em&gt;labels&lt;/em&gt; layers. | [optional] [default to 256]
 **view** | **String**| Geopolitical view. Determines rendering of disputed areas. See the &lt;a href&#x3D;\&quot;/maps-sdk-web/functional-examples#geopolitical-views\&quot;&gt;documentation&lt;/a&gt; for an explanation of how this works in live services. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

