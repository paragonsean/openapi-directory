# RasterApi

All URIs are relative to *https://api.tomtom.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mapVersionNumberStaticimageGet**](RasterApi.md#mapVersionNumberStaticimageGet) | **GET** /map/{versionNumber}/staticimage | Static Image |
| [**mapVersionNumberTileLayerStyleZoomXYFormatGet**](RasterApi.md#mapVersionNumberTileLayerStyleZoomXYFormatGet) | **GET** /map/{versionNumber}/tile/{layer}/{style}/{zoom}/{X}/{Y}.{format} | Tile |


<a id="mapVersionNumberStaticimageGet"></a>
# **mapVersionNumberStaticimageGet**
> mapVersionNumberStaticimageGet(versionNumber, layer, style, format, zoom, center, width, height, bbox, view)

Static Image

The Static Image service renders a rectangular raster image in the style, size, and zoom level specified. The image can be requested using either a center point plus width and height or a bounding box.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RasterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RasterApi apiInstance = new RasterApi(defaultClient);
    Integer versionNumber = 1; // Integer | Version of the service to call. The current version is 1.
    String layer = "basic"; // String | Layer of image to be rendered. <em>Hybrid</em> and <em>labels</em> are intended for layering with other data and are only available in <em>png</em> format.
    String style = "main"; // String | Map style to be returned
    String format = "png"; // String | Image format to be returned
    Integer zoom = 0; // Integer | Zoom level of map image to be returned.
    String center = "4.899886, 52.379031"; // String | Coordinates for the center point of the image. Must be used with the <strong>width</strong> and <strong>height</strong> parameters; cannot be used with <strong>bbox</strong>. Uses EPSG:3857 projection (functionally equivalent to EPSG:900910).
    Integer width = 512; // Integer | Width of the resulting image in pixels. Width must be a positive integer between 1 and 8192.
    Integer height = 512; // Integer | Height of the resulting image in pixels. Height must be a positive integer between 1 and 8192.
    String bbox = "bbox_example"; // String | Bounding box for the image, using EPSG:3857 projection (functionally equivalent to EPSG:900910). Values <strong>must</strong> be in the order of minLon, minLat, maxLon, maxLat. MaxLat must be greater than minLat. Longitude values can be on both sides of the 180th meridian. Cannot be used with <strong>center</strong>, <strong>width</strong>, or <strong>height</strong> parameters.
    String view = "Unified"; // String | Geopolitical view. Determines rendering of disputed areas. See the <a href=\"/maps-api/maps-api-documentation-raster/raster-tile\">documentation</a> for an explanation of how this works in live services.
    try {
      apiInstance.mapVersionNumberStaticimageGet(versionNumber, layer, style, format, zoom, center, width, height, bbox, view);
    } catch (ApiException e) {
      System.err.println("Exception when calling RasterApi#mapVersionNumberStaticimageGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **versionNumber** | **Integer**| Version of the service to call. The current version is 1. | [enum: 1] |
| **layer** | **String**| Layer of image to be rendered. &lt;em&gt;Hybrid&lt;/em&gt; and &lt;em&gt;labels&lt;/em&gt; are intended for layering with other data and are only available in &lt;em&gt;png&lt;/em&gt; format. | [optional] [default to basic] [enum: basic, hybrid, labels] |
| **style** | **String**| Map style to be returned | [optional] [default to main] [enum: main, night] |
| **format** | **String**| Image format to be returned | [optional] [default to png] [enum: png, jpg, jpeg] |
| **zoom** | **Integer**| Zoom level of map image to be returned. | [optional] [default to 12] [enum: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] |
| **center** | **String**| Coordinates for the center point of the image. Must be used with the &lt;strong&gt;width&lt;/strong&gt; and &lt;strong&gt;height&lt;/strong&gt; parameters; cannot be used with &lt;strong&gt;bbox&lt;/strong&gt;. Uses EPSG:3857 projection (functionally equivalent to EPSG:900910). | [optional] |
| **width** | **Integer**| Width of the resulting image in pixels. Width must be a positive integer between 1 and 8192. | [optional] [default to 512] |
| **height** | **Integer**| Height of the resulting image in pixels. Height must be a positive integer between 1 and 8192. | [optional] [default to 512] |
| **bbox** | **String**| Bounding box for the image, using EPSG:3857 projection (functionally equivalent to EPSG:900910). Values &lt;strong&gt;must&lt;/strong&gt; be in the order of minLon, minLat, maxLon, maxLat. MaxLat must be greater than minLat. Longitude values can be on both sides of the 180th meridian. Cannot be used with &lt;strong&gt;center&lt;/strong&gt;, &lt;strong&gt;width&lt;/strong&gt;, or &lt;strong&gt;height&lt;/strong&gt; parameters. | [optional] |
| **view** | **String**| Geopolitical view. Determines rendering of disputed areas. See the &lt;a href&#x3D;\&quot;/maps-api/maps-api-documentation-raster/raster-tile\&quot;&gt;documentation&lt;/a&gt; for an explanation of how this works in live services. | [optional] [enum: Unified, IN] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &lt;b&gt;OK&lt;/b&gt; |  -  |
| **400** | &lt;b&gt;Bad Request&lt;/b&gt;: Received by the interface, but there is an error in the request, such as:   - one or more of the required parameters is missing   - unsupported or unrecognized parameter value   - two or more mutually exclusive parameters are used in the same query (e.g. mixing center/width/height and bbox.)   - minimum latitude is greater than maximum latitude in a bbox call   - layer containing alpha channel is requested in format not supporting the alpha channel This code is returned if the required parameters of the request were malformed. A detailed exception explanation is returned in a response in form of Service Exception Report. |  -  |
| **403** | &lt;b&gt;Forbidden&lt;/b&gt;:   - supplied API key is not valid for the request   - the requested view is not available in the country where the request was sent from |  -  |
| **500** | &lt;b&gt;Internal Server Error&lt;/b&gt;: There is a problem with the Static Map Service. |  -  |
| **503** | &lt;b&gt;Service currently unavailable.&lt;/b&gt; |  -  |

<a id="mapVersionNumberTileLayerStyleZoomXYFormatGet"></a>
# **mapVersionNumberTileLayerStyleZoomXYFormatGet**
> mapVersionNumberTileLayerStyleZoomXYFormatGet(versionNumber, layer, style, zoom, X, Y, format, tileSize, view)

Tile

The Maps API Raster Service delivers raster tiles, which are representations of square sections of map data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RasterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RasterApi apiInstance = new RasterApi(defaultClient);
    Integer versionNumber = 1; // Integer | Version of the service to call. The current version is 1.
    String layer = "basic"; // String | Layer of tile to be rendered. <em>Hybrid</em> and <em>labels</em> are intended for layering with other data and are only available in <em>png</em> format.
    String style = "main"; // String | Style of tile to be rendered
    Integer zoom = 0; // Integer | Zoom level of tile to be rendered
    Integer X = 0; // Integer | x coordinate of tile on zoom grid
    Integer Y = 0; // Integer | y coordinate of tile on zoom grid
    String format = "jpg"; // String | Format of the response.
    Integer tileSize = 256; // Integer | Tile dimensions in pixels. <em>512</em> is only available for the <em>main</em> style and <em>basic</em> or <em>labels</em> layers.
    String view = "Unified"; // String | Geopolitical view. Determines rendering of disputed areas. See the <a href=\"/maps-sdk-web/functional-examples#geopolitical-views\">documentation</a> for an explanation of how this works in live services.
    try {
      apiInstance.mapVersionNumberTileLayerStyleZoomXYFormatGet(versionNumber, layer, style, zoom, X, Y, format, tileSize, view);
    } catch (ApiException e) {
      System.err.println("Exception when calling RasterApi#mapVersionNumberTileLayerStyleZoomXYFormatGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **versionNumber** | **Integer**| Version of the service to call. The current version is 1. | [enum: 1] |
| **layer** | **String**| Layer of tile to be rendered. &lt;em&gt;Hybrid&lt;/em&gt; and &lt;em&gt;labels&lt;/em&gt; are intended for layering with other data and are only available in &lt;em&gt;png&lt;/em&gt; format. | [enum: basic, hybrid, labels] |
| **style** | **String**| Style of tile to be rendered | [enum: main, night] |
| **zoom** | **Integer**| Zoom level of tile to be rendered | [enum: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] |
| **X** | **Integer**| x coordinate of tile on zoom grid | |
| **Y** | **Integer**| y coordinate of tile on zoom grid | |
| **format** | **String**| Format of the response. | [enum: jpg, png] |
| **tileSize** | **Integer**| Tile dimensions in pixels. &lt;em&gt;512&lt;/em&gt; is only available for the &lt;em&gt;main&lt;/em&gt; style and &lt;em&gt;basic&lt;/em&gt; or &lt;em&gt;labels&lt;/em&gt; layers. | [optional] [default to 256] [enum: 256, 512] |
| **view** | **String**| Geopolitical view. Determines rendering of disputed areas. See the &lt;a href&#x3D;\&quot;/maps-sdk-web/functional-examples#geopolitical-views\&quot;&gt;documentation&lt;/a&gt; for an explanation of how this works in live services. | [optional] [enum: Unified, IN] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &lt;b&gt;OK&lt;/b&gt; |  -  |
| **302** | &lt;b&gt;Found&lt;/b&gt;: URL redirection |  -  |
| **400** | &lt;b&gt;Bad request&lt;/b&gt;: Usually the result of malformed syntax:   - the given combination of layer, style, and query parameters is not supported   - zoom n is out of range 0 &lt;&#x3D; zoom &lt; 19: the requested zoom level is out of the possible range   - x n is out of range [0,m]: the requested x coordinate is out of the possible range (the value of m will vary depending on zoom level)   - y n is out of range [0,m]: the requested y coordinate is out of the possible range (the value of m will vary depending on zoom level)   - the requested view is not supported |  -  |
| **403** | &lt;b&gt;Forbidden&lt;/b&gt;:   - the supplied API key is not valid for this request   - the requested view is not available in the country where the request was sent from |  -  |
| **410** | &lt;b&gt;Gone&lt;/b&gt;: Request for unsupported format |  -  |
| **500** | &lt;b&gt;Internal Server Error&lt;/b&gt;: There is a problem with the TomTom Maps API Raster Tile service |  -  |

