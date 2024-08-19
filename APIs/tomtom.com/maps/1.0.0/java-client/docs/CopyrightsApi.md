# CopyrightsApi

All URIs are relative to *https://api.tomtom.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mapVersionNumberCopyrightsCaptionFormatGet**](CopyrightsApi.md#mapVersionNumberCopyrightsCaptionFormatGet) | **GET** /map/{versionNumber}/copyrights/caption.{format} | Captions |
| [**mapVersionNumberCopyrightsFormatGet**](CopyrightsApi.md#mapVersionNumberCopyrightsFormatGet) | **GET** /map/{versionNumber}/copyrights.{format} | Copyrights whole world |
| [**mapVersionNumberCopyrightsMinLonMinLatMaxLonMaxLatFormatGet**](CopyrightsApi.md#mapVersionNumberCopyrightsMinLonMinLatMaxLonMaxLatFormatGet) | **GET** /map/{versionNumber}/copyrights/{minLon}/{minLat}/{maxLon}/{maxLat}.{format} | Copyrights bounding box |
| [**mapVersionNumberCopyrightsZoomXYFormatGet**](CopyrightsApi.md#mapVersionNumberCopyrightsZoomXYFormatGet) | **GET** /map/{versionNumber}/copyrights/{zoom}/{X}/{Y}.{format} | Copyrights tile |


<a id="mapVersionNumberCopyrightsCaptionFormatGet"></a>
# **mapVersionNumberCopyrightsCaptionFormatGet**
> mapVersionNumberCopyrightsCaptionFormatGet(versionNumber, format, paramCallback)

Captions

This API returns copyright captions for the map service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CopyrightsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CopyrightsApi apiInstance = new CopyrightsApi(defaultClient);
    Integer versionNumber = 1; // Integer | Version of the service to call. The current version is 1.
    String format = "json"; // String | Format of the response
    String paramCallback = "paramCallback_example"; // String | Specifies the jsonp callback method. Only used when format is jsonp
    try {
      apiInstance.mapVersionNumberCopyrightsCaptionFormatGet(versionNumber, format, paramCallback);
    } catch (ApiException e) {
      System.err.println("Exception when calling CopyrightsApi#mapVersionNumberCopyrightsCaptionFormatGet");
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
| **format** | **String**| Format of the response | [default to xml] [enum: json, jsonp, xml] |
| **paramCallback** | **String**| Specifies the jsonp callback method. Only used when format is jsonp | [optional] |

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
| **304** | &lt;b&gt;Not Modified&lt;/b&gt; |  -  |
| **400** | &lt;b&gt;Malformed request&lt;/b&gt;: malformed syntax. Possible causes include:   - requested syntax is not available |  -  |
| **403** | &lt;b&gt;Forbidden&lt;/b&gt;: Supplied API key is not valid for this request |  -  |
| **410** | &lt;b&gt;Gone&lt;/b&gt;: Request for unsupported format |  -  |
| **500** | &lt;b&gt;Internal Server Error&lt;/b&gt;: There is a problem with the TomTom Copyrights API service |  -  |

<a id="mapVersionNumberCopyrightsFormatGet"></a>
# **mapVersionNumberCopyrightsFormatGet**
> mapVersionNumberCopyrightsFormatGet(versionNumber, format, paramCallback)

Copyrights whole world

The Copyrights API returns copyright information for the Maps API Raster Tile Service in JSON, JSONP, or XML format. This call returns copyright information for the whole world.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CopyrightsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CopyrightsApi apiInstance = new CopyrightsApi(defaultClient);
    Integer versionNumber = 1; // Integer | Version of the service to call. The current version is 1
    String format = "json"; // String | Format of the response
    String paramCallback = "paramCallback_example"; // String | Specifies the jsonp callback method. Only used when format is jsonp
    try {
      apiInstance.mapVersionNumberCopyrightsFormatGet(versionNumber, format, paramCallback);
    } catch (ApiException e) {
      System.err.println("Exception when calling CopyrightsApi#mapVersionNumberCopyrightsFormatGet");
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
| **format** | **String**| Format of the response | [default to xml] [enum: json, jsonp, xml] |
| **paramCallback** | **String**| Specifies the jsonp callback method. Only used when format is jsonp | [optional] |

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
| **304** | &lt;b&gt;Not Modified&lt;/b&gt; |  -  |
| **400** | &lt;b&gt;Malformed request&lt;/b&gt;: malformed syntax. Possible causes include:   - requested syntax is not available |  -  |
| **403** | &lt;b&gt;Forbidden&lt;/b&gt;: Supplied API key is not valid for this request |  -  |
| **410** | &lt;b&gt;Gone&lt;/b&gt;: Request for unsupported format |  -  |
| **500** | &lt;b&gt;Internal Server Error&lt;/b&gt;: There is a problem with the TomTom Copyrights API service |  -  |

<a id="mapVersionNumberCopyrightsMinLonMinLatMaxLonMaxLatFormatGet"></a>
# **mapVersionNumberCopyrightsMinLonMinLatMaxLonMaxLatFormatGet**
> mapVersionNumberCopyrightsMinLonMinLatMaxLonMaxLatFormatGet(versionNumber, format, minLon, minLat, maxLon, maxLat, paramCallback)

Copyrights bounding box

The Copyrights API returns copyright information for the Maps API Raster Tile Service in JSON, JSONP, or XML format. This call returns copyright information for a specific bounding box.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CopyrightsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CopyrightsApi apiInstance = new CopyrightsApi(defaultClient);
    Integer versionNumber = 1; // Integer | Version of the service to call. The current version is 1
    String format = "json"; // String | Format of the response
    BigDecimal minLon = new BigDecimal("-179.1506"); // BigDecimal | Minimum longitude coordinate of bounding box defined in terms of latitude/longitude.
    BigDecimal minLat = new BigDecimal("18.9117"); // BigDecimal | Minimum latitude coordinate of bounding box defined in terms of latitude/longitude.
    BigDecimal maxLon = new BigDecimal("-66.9406"); // BigDecimal | Maximum longitude coordinate of bounding box defined in terms of latitude/longitude.
    BigDecimal maxLat = new BigDecimal("71.441"); // BigDecimal | Maximum latitude coordinate of bounding box defined in terms of latitude/longitude.
    String paramCallback = "paramCallback_example"; // String | Specifies the jsonp callback method. Only used when format is jsonp.
    try {
      apiInstance.mapVersionNumberCopyrightsMinLonMinLatMaxLonMaxLatFormatGet(versionNumber, format, minLon, minLat, maxLon, maxLat, paramCallback);
    } catch (ApiException e) {
      System.err.println("Exception when calling CopyrightsApi#mapVersionNumberCopyrightsMinLonMinLatMaxLonMaxLatFormatGet");
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
| **format** | **String**| Format of the response | [default to xml] [enum: json, jsonp, xml] |
| **minLon** | **BigDecimal**| Minimum longitude coordinate of bounding box defined in terms of latitude/longitude. | |
| **minLat** | **BigDecimal**| Minimum latitude coordinate of bounding box defined in terms of latitude/longitude. | |
| **maxLon** | **BigDecimal**| Maximum longitude coordinate of bounding box defined in terms of latitude/longitude. | |
| **maxLat** | **BigDecimal**| Maximum latitude coordinate of bounding box defined in terms of latitude/longitude. | |
| **paramCallback** | **String**| Specifies the jsonp callback method. Only used when format is jsonp. | [optional] |

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
| **304** | &lt;b&gt;Not Modified&lt;/b&gt; |  -  |
| **400** | &lt;b&gt;Malformed request&lt;/b&gt;: malformed syntax. Possible causes include:   - requested syntax is not available |  -  |
| **401** | &lt;b&gt;Bad request&lt;/b&gt;: Parameters out of range. Possible causes include:   - minLon n is out of range [-180,180]: the requested minimum longitude coordinate is out of possible range   - minLat n is out of range [-90,90]: the requested minimum latitude coordinate is out of possible range   - maxLon n is out of range [-180,180]: the requested maximum longitude coordinate is out of possible range   - maxLat n is out of range [-90,90]: the requested minimum latitude coordinate is out of possible range |  -  |
| **403** | &lt;b&gt;Forbidden&lt;/b&gt;: Supplied API key is not valid for this request |  -  |
| **410** | &lt;b&gt;Gone&lt;/b&gt;: Request for unsupported format |  -  |
| **500** | &lt;b&gt;Internal Server Error&lt;/b&gt;: There is a problem with the TomTom Copyrights API service |  -  |

<a id="mapVersionNumberCopyrightsZoomXYFormatGet"></a>
# **mapVersionNumberCopyrightsZoomXYFormatGet**
> mapVersionNumberCopyrightsZoomXYFormatGet(versionNumber, format, zoom, X, Y, paramCallback)

Copyrights tile

The Copyrights API returns copyright information for the Maps API Raster Tile Service in JSON, JSONP, or XML format. This call returns copyright information for the a specific map tile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CopyrightsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CopyrightsApi apiInstance = new CopyrightsApi(defaultClient);
    Integer versionNumber = 1; // Integer | Version of the service to call. The current version is 1
    String format = "json"; // String | Format of the response
    Integer zoom = 0; // Integer | Zoom level of tile to be rendered. Only used for tile-level copyright calls.
    Integer X = 0; // Integer | X coordinate of the tile on zoom grid. Only used for tile-level copyright calls.
    Integer Y = 0; // Integer | Y coordinate of the tile on zoom grid. Only used for tile-level copyright calls.
    String paramCallback = "paramCallback_example"; // String | Specifies the jsonp callback method. Only used when format is jsonp.
    try {
      apiInstance.mapVersionNumberCopyrightsZoomXYFormatGet(versionNumber, format, zoom, X, Y, paramCallback);
    } catch (ApiException e) {
      System.err.println("Exception when calling CopyrightsApi#mapVersionNumberCopyrightsZoomXYFormatGet");
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
| **format** | **String**| Format of the response | [default to xml] [enum: json, jsonp, xml] |
| **zoom** | **Integer**| Zoom level of tile to be rendered. Only used for tile-level copyright calls. | [enum: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] |
| **X** | **Integer**| X coordinate of the tile on zoom grid. Only used for tile-level copyright calls. | |
| **Y** | **Integer**| Y coordinate of the tile on zoom grid. Only used for tile-level copyright calls. | |
| **paramCallback** | **String**| Specifies the jsonp callback method. Only used when format is jsonp. | [optional] |

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
| **304** | &lt;b&gt;Not Modified&lt;/b&gt; |  -  |
| **400** | &lt;b&gt;Malformed request&lt;/b&gt;: malformed syntax. Possible causes include:   - requested syntax is not available |  -  |
| **401** | &lt;b&gt;Bad request&lt;/b&gt;: Parameters out of range. Possible causes include:   - zoom n is out of range 0 &lt;&#x3D; zoom &lt; 19: the requested zoom level is out of the possible range   - x n is out of range [0,m]: the requested x coordinate is out of the possible range (the value of m will vary depending on zoom level)   - y n is out of range [0,m]: the requested y coordinate is out of the possible range (the value of m will vary depending on zoom level) |  -  |
| **403** | &lt;b&gt;Forbidden&lt;/b&gt;: Supplied API key is not valid for this request |  -  |
| **410** | &lt;b&gt;Gone&lt;/b&gt;: Request for unsupported format |  -  |
| **500** | &lt;b&gt;Internal Server Error&lt;/b&gt;: There is a problem with the TomTom Copyrights API service |  -  |

