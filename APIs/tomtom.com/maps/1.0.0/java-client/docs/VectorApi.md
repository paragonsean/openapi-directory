# VectorApi

All URIs are relative to *https://api.tomtom.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mapVersionNumberTileLayerStyleZoomXYPbfGet**](VectorApi.md#mapVersionNumberTileLayerStyleZoomXYPbfGet) | **GET** /map/{versionNumber}/tile/{layer}/{style}/{zoom}/{X}/{Y}.pbf | Tile |


<a id="mapVersionNumberTileLayerStyleZoomXYPbfGet"></a>
# **mapVersionNumberTileLayerStyleZoomXYPbfGet**
> mapVersionNumberTileLayerStyleZoomXYPbfGet(versionNumber, layer, style, zoom, X, Y, view, language)

Tile

The Maps API Vector Service delivers vector tiles, which are representations of square sections of map data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VectorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    VectorApi apiInstance = new VectorApi(defaultClient);
    Integer versionNumber = 1; // Integer | Version of the service to call. The current version is 1
    String layer = "basic"; // String | Layer of tile to be rendered
    String style = "main"; // String | Style of tile to be rendered
    Integer zoom = 0; // Integer | Zoom level of tile to be rendered
    Integer X = 0; // Integer | x coordinate of tile on zoom grid
    Integer Y = 0; // Integer | y coordinate of tile on zoom grid
    String view = "Unified"; // String | Geopolitical view. Determines rendering of disputed areas. See the <a href=\"/maps-api/maps-api-documentation-vector/tile\">documentation</a> for an explanation of how this works in live services.
    String language = "NGT"; // String | Language to be used for labels in the response. The default is NGT: Neutral Ground Truth, which uses each place's local official language and script (where available). See the <a href=\"/maps-api/maps-api-documentation-vector/tile\">documentation</a> for a full list of options.
    try {
      apiInstance.mapVersionNumberTileLayerStyleZoomXYPbfGet(versionNumber, layer, style, zoom, X, Y, view, language);
    } catch (ApiException e) {
      System.err.println("Exception when calling VectorApi#mapVersionNumberTileLayerStyleZoomXYPbfGet");
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
| **versionNumber** | **Integer**| Version of the service to call. The current version is 1 | [enum: 1] |
| **layer** | **String**| Layer of tile to be rendered | [enum: basic, hybrid, labels] |
| **style** | **String**| Style of tile to be rendered | [enum: main] |
| **zoom** | **Integer**| Zoom level of tile to be rendered | [enum: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] |
| **X** | **Integer**| x coordinate of tile on zoom grid | |
| **Y** | **Integer**| y coordinate of tile on zoom grid | |
| **view** | **String**| Geopolitical view. Determines rendering of disputed areas. See the &lt;a href&#x3D;\&quot;/maps-api/maps-api-documentation-vector/tile\&quot;&gt;documentation&lt;/a&gt; for an explanation of how this works in live services. | [optional] [enum: Unified, IL, IN] |
| **language** | **String**| Language to be used for labels in the response. The default is NGT: Neutral Ground Truth, which uses each place&#39;s local official language and script (where available). See the &lt;a href&#x3D;\&quot;/maps-api/maps-api-documentation-vector/tile\&quot;&gt;documentation&lt;/a&gt; for a full list of options. | [optional] [default to NGT] |

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
| **400** | &lt;b&gt;Bad request&lt;/b&gt;: Usually the result of malformed syntax:   - the given combination of layer, style, and query parameters is not supported   - zoom n is out of range 0 &lt;&#x3D; zoom &lt;&#x3D; 22: the requested zoom level is out of the possible range   - x n is out of range [0,m]: the requested x coordinate is out of the possible range (the value of m will vary depending on zoom level)   - y n is out of range [0,m]: the requested y coordinate is out of the possible range (the value of m will vary depending on zoom level)   - the requested view is not supported |  -  |
| **403** | &lt;b&gt;Forbidden&lt;/b&gt;:    - the supplied API key is not valid for this request   - the requested view is not available in your country |  -  |
| **500** | &lt;b&gt;Internal Server Error&lt;/b&gt;: There is a problem with the TomTom Maps API Vector Tile service |  -  |
| **503** | &lt;b&gt;Service currently unavailable&lt;/b&gt;. |  -  |

