# WmsWmtsApi

All URIs are relative to *https://api.tomtom.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCapabilities**](WmsWmtsApi.md#getCapabilities) | **GET** /map/{versionNumber}/wms// | GetCapabilities |
| [**getMap**](WmsWmtsApi.md#getMap) | **GET** /map/{versionNumber}/wms/ | GetMap |
| [**mapVersionNumberWmtsKeyWmtsVersionWMTSCapabilitiesXmlGet**](WmsWmtsApi.md#mapVersionNumberWmtsKeyWmtsVersionWMTSCapabilitiesXmlGet) | **GET** /map/{versionNumber}/wmts/{key}/{wmtsVersion}/WMTSCapabilities.xml | WMTS |


<a id="getCapabilities"></a>
# **getCapabilities**
> getCapabilities(versionNumber, service, request, version)

GetCapabilities

The GetCapabilities call is part of TomTom&#39;s implementation of version 1.1.1 the Web Map Service (WMS). It provides descriptions of the other calls that are available in the implementation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WmsWmtsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    WmsWmtsApi apiInstance = new WmsWmtsApi(defaultClient);
    Integer versionNumber = 1; // Integer | 
    String service = "WMS"; // String | 
    String request = "GetCapabilities"; // String | 
    String version = "1.1.1"; // String | WMS service version
    try {
      apiInstance.getCapabilities(versionNumber, service, request, version);
    } catch (ApiException e) {
      System.err.println("Exception when calling WmsWmtsApi#getCapabilities");
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
| **versionNumber** | **Integer**|  | [enum: 1] |
| **service** | **String**|  | [enum: WMS] |
| **request** | **String**|  | [enum: GetCapabilities] |
| **version** | **String**| WMS service version | [optional] [enum: 1.1.1] |

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
| **202** | &lt;b&gt;Accepted&lt;/b&gt;: Received by the interface, but there is a WMS exception in processing it. Possible causes include:   - one or more required parameters is missing   - unsupported or unrecognized parameter value   - malformed bounding box requested   - invalid map dimensions requested                                   This code is returned if the parameters of the request were malformed. The response includes a detailed explanation in the Service Exception Report. |  -  |
| **401** | &lt;b&gt;Unauthorized&lt;/b&gt;: Supplied API key is not valid for the request |  -  |
| **500** | &lt;b&gt;Internal Server Error&lt;/b&gt;: There is a problem with the TomTom WMS service |  -  |

<a id="getMap"></a>
# **getMap**
> getMap(versionNumber, request, srs, bbox, width, height, format, layers, version, styles, service)

GetMap

The GetMap call implements the Web Map Service 1.1.1 standard to access TomTom raster map tiles. This service is described in the response to the GetCapabilities API call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WmsWmtsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    WmsWmtsApi apiInstance = new WmsWmtsApi(defaultClient);
    Integer versionNumber = 1; // Integer | Version of the service to call. The current version is 1
    String request = "GetMap"; // String | Request type
    String srs = "EPSG:3857"; // String | Projection used in describing the <b>bbox</b> EPSG:3857 is recommended, particularly at higher zoom levels. (Note that EPSG:3857 is functionally equivalent to EPSG:900913/EPSG:3785)
    String bbox = "-0.489,51.28,0.236,51.686"; // String | Bounding box in the projection stated in <b>srs</b> (minLon,minLat,maxLon,maxLat)
    Integer width = 512; // Integer | Width of the resulting image, in pixels Maximum value is 2048
    Integer height = 512; // Integer | Height of the resulting image, in pixels Maximum value is 2048
    String format = "image/jpeg"; // String | Image format to be returned
    String layers = "basic"; // String | Map layers requested Currently only the basic layer is available
    String version = "1.1.1"; // String | WMS service version
    String styles = ""; // String | Map styles to be returned. Currently, no styles are available. This parameter is present for forward compatibility; it must be used and left blank.
    String service = "WMS"; // String | Service type
    try {
      apiInstance.getMap(versionNumber, request, srs, bbox, width, height, format, layers, version, styles, service);
    } catch (ApiException e) {
      System.err.println("Exception when calling WmsWmtsApi#getMap");
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
| **request** | **String**| Request type | [enum: GetMap] |
| **srs** | **String**| Projection used in describing the &lt;b&gt;bbox&lt;/b&gt; EPSG:3857 is recommended, particularly at higher zoom levels. (Note that EPSG:3857 is functionally equivalent to EPSG:900913/EPSG:3785) | [enum: EPSG:3857, EPSG:4326] |
| **bbox** | **String**| Bounding box in the projection stated in &lt;b&gt;srs&lt;/b&gt; (minLon,minLat,maxLon,maxLat) | |
| **width** | **Integer**| Width of the resulting image, in pixels Maximum value is 2048 | |
| **height** | **Integer**| Height of the resulting image, in pixels Maximum value is 2048 | |
| **format** | **String**| Image format to be returned | [enum: image/jpeg, image/png] |
| **layers** | **String**| Map layers requested Currently only the basic layer is available | [enum: basic] |
| **version** | **String**| WMS service version | [enum: 1.1.1] |
| **styles** | **String**| Map styles to be returned. Currently, no styles are available. This parameter is present for forward compatibility; it must be used and left blank. | [optional] [enum: ] |
| **service** | **String**| Service type | [optional] [enum: WMS] |

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
| **202** | &lt;b&gt;Accepted&lt;/b&gt;: Received by the interface, but there is a WMS exception in processing it. Possible causes include:   - one or more required parameters is missing   - unsupported or unrecognized parameter value   - malformed bounding box requested   - invalid map dimensions requested                                   This code is returned if the parameters of the request were malformed. The response includes a detailed explanation in the Service Exception Report. |  -  |
| **401** | &lt;b&gt;Unauthorized&lt;/b&gt;: Supplied API key is not valid for the request |  -  |
| **500** | &lt;b&gt;Internal Server Error&lt;/b&gt;: There is a problem with the TomTom WMS service |  -  |

<a id="mapVersionNumberWmtsKeyWmtsVersionWMTSCapabilitiesXmlGet"></a>
# **mapVersionNumberWmtsKeyWmtsVersionWMTSCapabilitiesXmlGet**
> mapVersionNumberWmtsKeyWmtsVersionWMTSCapabilitiesXmlGet(versionNumber, key, wmtsVersion)

WMTS

The WMTS GetCapabilities call implements version 1.0.0 of the &lt;a href&#x3D;\&quot;http://www.opengeospatial.org/standards/wmts\&quot;&gt;Web Map Tile Service&lt;/a&gt; (WMTS) standard. It returns metadata that allows compatible calling systems to construct calls to TomTom&#39;s raster map tile service. See the &lt;a href&#x3D;\&quot;/maps-api/maps-api-documentation-raster/wmts\&quot;&gt;documentation&lt;/a&gt; for more information on WMTS.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WmsWmtsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");

    WmsWmtsApi apiInstance = new WmsWmtsApi(defaultClient);
    Integer versionNumber = 1; // Integer | Version of the service to call. The current version is 1
    String key = "key_example"; // String | Your API key for calling this service.
    String wmtsVersion = "1.0.0"; // String | 
    try {
      apiInstance.mapVersionNumberWmtsKeyWmtsVersionWMTSCapabilitiesXmlGet(versionNumber, key, wmtsVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling WmsWmtsApi#mapVersionNumberWmtsKeyWmtsVersionWMTSCapabilitiesXmlGet");
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
| **key** | **String**| Your API key for calling this service. | |
| **wmtsVersion** | **String**|  | [enum: 1.0.0] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &lt;b&gt;OK&lt;/b&gt; |  -  |
| **400** | &lt;b&gt;Bad request&lt;/b&gt;: Probably malformed syntax |  -  |
| **401** | &lt;b&gt;Unauthorized&lt;/b&gt;: Supplied API key is not valid for this request |  -  |
| **500** | &lt;b&gt;Internal Server Error&lt;/b&gt;: There is a problem with the TomTom WMTS service |  -  |

