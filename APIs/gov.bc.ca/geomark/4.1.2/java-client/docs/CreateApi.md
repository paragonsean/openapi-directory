# CreateApi

All URIs are relative to *https://apps.gov.bc.ca/pub/geomark*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**geomarksCopyPost**](CreateApi.md#geomarksCopyPost) | **POST** /geomarks/copy | Create a new geomark by copying the geometries from one or more existing geomarks from the current server. |
| [**geomarksNewPost**](CreateApi.md#geomarksNewPost) | **POST** /geomarks/new | Create a new geomark |


<a id="geomarksCopyPost"></a>
# **geomarksCopyPost**
> geomarksCopyPost(geomarkUrl, resultFormat, allowOverlap, paramCallback, redirectUrl, failureRedirectUrl, bufferMetres, bufferJoin, bufferCap, bufferMitreLimit, bufferSegments)

Create a new geomark by copying the geometries from one or more existing geomarks from the current server.

The source geomarks can be specified by with the geomarkUrl parameter.  Repeat the parameter if sourcing from multiple geomarks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/geomark");

    CreateApi apiInstance = new CreateApi(defaultClient);
    String geomarkUrl = "https://apps.gov.bc.ca/pub/geomark/geomarks/gm-abcdefghijklmnopqrstuv0bcislands"; // String | One or more geomark URLs or identifiers to create the new geomark from.
    String resultFormat = "json"; // String | The file format the geomark info resource should be returned using.
    Boolean allowOverlap = false; // Boolean | Select this option to allow overlapping geometries
    String paramCallback = "paramCallback_example"; // String | The callback function a JSON result format would be wrapped in to support Ajax requests.
    String redirectUrl = "redirectUrl_example"; // String | The optional external URL to redirect the user to when the geomark is created rather than showing the geomark info page. The geomarkId and geomarkUrl query string parameters will be added to the redirectUrl so that the target application gets a reference to the geomark.
    String failureRedirectUrl = "failureRedirectUrl_example"; // String | The url to redirect if the geomark could not be created. The URL will include a <fieldName>_Error parameter with the error message for the field that caused the error.
    Integer bufferMetres = 56; // Integer | The amount to buffer the geometry in metres, must only contain numerical digits (e.g 10). Leave blank and no buffer will be added to input geometries. If blank then any Point, LineString, MultiPoint and MultiLineString geometries will be ignored.
    String bufferJoin = "ROUND"; // String | If bufferMetres is specified, The style of buffer to use for joins between the line segments for lines and polygons.
    String bufferCap = "ROUND"; // String | If bufferMetres is specified, The style of buffer to use at the ends of a buffered line.
    Integer bufferMitreLimit = 5; // Integer | If bufferMetres is specified, the maximum ratio of distance from the original geometry to a mitre buffer point and the buffer amount. If the ratio is greater than this a bevel will be used instead. This prevents infinite distances when the angle between the two lines at a join is small. Must be > 0.
    Integer bufferSegments = 8; // Integer | If bufferMetres is specified, the number of line segments used in each quadrant to approximate the curve for round end-cap and join styles. Must be > 0.
    try {
      apiInstance.geomarksCopyPost(geomarkUrl, resultFormat, allowOverlap, paramCallback, redirectUrl, failureRedirectUrl, bufferMetres, bufferJoin, bufferCap, bufferMitreLimit, bufferSegments);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreateApi#geomarksCopyPost");
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
| **geomarkUrl** | **String**| One or more geomark URLs or identifiers to create the new geomark from. | |
| **resultFormat** | **String**| The file format the geomark info resource should be returned using. | [optional] [enum: json, xml, kml, kmz, shp, shpz, geojson, gml, gpkg, wkt] |
| **allowOverlap** | **Boolean**| Select this option to allow overlapping geometries | [optional] [default to false] |
| **paramCallback** | **String**| The callback function a JSON result format would be wrapped in to support Ajax requests. | [optional] |
| **redirectUrl** | **String**| The optional external URL to redirect the user to when the geomark is created rather than showing the geomark info page. The geomarkId and geomarkUrl query string parameters will be added to the redirectUrl so that the target application gets a reference to the geomark. | [optional] |
| **failureRedirectUrl** | **String**| The url to redirect if the geomark could not be created. The URL will include a &lt;fieldName&gt;_Error parameter with the error message for the field that caused the error. | [optional] |
| **bufferMetres** | **Integer**| The amount to buffer the geometry in metres, must only contain numerical digits (e.g 10). Leave blank and no buffer will be added to input geometries. If blank then any Point, LineString, MultiPoint and MultiLineString geometries will be ignored. | [optional] |
| **bufferJoin** | **String**| If bufferMetres is specified, The style of buffer to use for joins between the line segments for lines and polygons. | [optional] [default to ROUND] [enum: ROUND, MITRE, BEVEL] |
| **bufferCap** | **String**| If bufferMetres is specified, The style of buffer to use at the ends of a buffered line. | [optional] [default to ROUND] [enum: ROUND, SQUARE, FLAT] |
| **bufferMitreLimit** | **Integer**| If bufferMetres is specified, the maximum ratio of distance from the original geometry to a mitre buffer point and the buffer amount. If the ratio is greater than this a bevel will be used instead. This prevents infinite distances when the angle between the two lines at a join is small. Must be &gt; 0. | [optional] [default to 5] |
| **bufferSegments** | **Integer**| If bufferMetres is specified, the number of line segments used in each quadrant to approximate the curve for round end-cap and join styles. Must be &gt; 0. | [optional] [default to 8] |

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
| **200** | If the geomark was created via a web service call. |  -  |
| **302** | If the geomark was created and a redirectUrl was specified then the response will redirect to the redirectUrl with the query string parameters geomarkId and geomarkUrl of the created geomark.  Additional reasons for this status code can be found in the [Geomark Web Service Developer Guide](https://apps.gov.bc.ca/pub/geomark/docs/rest-api/) |  -  |
| **400** | **Couldn&#39;t create Geomark.**  Possible reasons:  * No Polygon, Multi-Polygon, or folder(set) of Polygons provided. * A point or line was provided without a buffer width.  Additional reasons for this status code can be found in the [Geomark Web Service Developer Guide](https://apps.gov.bc.ca/pub/geomark/docs/rest-api/) |  -  |
| **500** | **Internal Server Error** |  -  |

<a id="geomarksNewPost"></a>
# **geomarksNewPost**
> geomarksNewPost(allowOverlap, body, bufferCap, bufferJoin, bufferMetres, bufferMitreLimit, bufferSegments, paramCallback, failureRedirectUrl, format, multiple, redirectUrl, resultFormat, srid)

Create a new geomark

Create a new geomark from the geometries read from the &#39;body&#39; parameter or file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/geomark");

    CreateApi apiInstance = new CreateApi(defaultClient);
    Boolean allowOverlap = false; // Boolean | When multiple=true select this option to allow overlapping geometries
    String body = "body_example"; // String | The binary or character content representing the geometry or geometries
    String bufferCap = "ROUND"; // String | If bufferMetres is specified, The style of buffer to use at the ends of a buffered line.
    String bufferJoin = "ROUND"; // String | If bufferMetres is specified, The style of buffer to use for joins between the line segments for lines and polygons.
    Integer bufferMetres = 56; // Integer | The amount to buffer the geometry in metres, must only contain numerical digits (e.g 10). Leave blank and no buffer will be added to input geometries. If blank then any Point, LineString, MultiPoint and MultiLineString geometries will be ignored.
    Integer bufferMitreLimit = 5; // Integer | If bufferMetres is specified, the maximum ratio of distance from the original geometry to a mitre buffer point and the buffer amount. If the ratio is greater than this a bevel will be used instead. This prevents infinite distances when the angle between the two lines at a join is small. Must be > 0.
    Integer bufferSegments = 8; // Integer | If bufferMetres is specified, the number of line segments used in each quadrant to approximate the curve for round end-cap and join styles. Must be > 0.
    String paramCallback = "paramCallback_example"; // String | The callback function a JSON result format would be wrapped in to support Ajax requests.
    String failureRedirectUrl = "failureRedirectUrl_example"; // String | The url to redirect if the geomark could not be created. The URL will include a <fieldName>_Error parameter with the error message for the field that caused the error.
    String format = "json"; // String | The file format name extension of the input geometry.
    Boolean multiple = false; // Boolean | Boolean flag indicating if multiple geometries are to be used for the geomark (true) or only a single geometry from the first geometry (false).
    String redirectUrl = "redirectUrl_example"; // String | The optional external URL to redirect the user to when the geomark is created rather than showing the geomark info page. The geomarkId and geomarkUrl query string parameters will be added to the redirectUrl so that the target application gets a reference to the geomark.
    String resultFormat = "json"; // String | The file format the geomark info resource should be returned using.
    Integer srid = 4326; // Integer | The srid of the coordinate system the input geometries are in. If the file includes a coordinate system definition that will be used.
    try {
      apiInstance.geomarksNewPost(allowOverlap, body, bufferCap, bufferJoin, bufferMetres, bufferMitreLimit, bufferSegments, paramCallback, failureRedirectUrl, format, multiple, redirectUrl, resultFormat, srid);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreateApi#geomarksNewPost");
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
| **allowOverlap** | **Boolean**| When multiple&#x3D;true select this option to allow overlapping geometries | [optional] [default to false] |
| **body** | **String**| The binary or character content representing the geometry or geometries | [optional] |
| **bufferCap** | **String**| If bufferMetres is specified, The style of buffer to use at the ends of a buffered line. | [optional] [default to ROUND] [enum: ROUND, SQUARE, FLAT] |
| **bufferJoin** | **String**| If bufferMetres is specified, The style of buffer to use for joins between the line segments for lines and polygons. | [optional] [default to ROUND] [enum: ROUND, MITRE, BEVEL] |
| **bufferMetres** | **Integer**| The amount to buffer the geometry in metres, must only contain numerical digits (e.g 10). Leave blank and no buffer will be added to input geometries. If blank then any Point, LineString, MultiPoint and MultiLineString geometries will be ignored. | [optional] |
| **bufferMitreLimit** | **Integer**| If bufferMetres is specified, the maximum ratio of distance from the original geometry to a mitre buffer point and the buffer amount. If the ratio is greater than this a bevel will be used instead. This prevents infinite distances when the angle between the two lines at a join is small. Must be &gt; 0. | [optional] [default to 5] |
| **bufferSegments** | **Integer**| If bufferMetres is specified, the number of line segments used in each quadrant to approximate the curve for round end-cap and join styles. Must be &gt; 0. | [optional] [default to 8] |
| **paramCallback** | **String**| The callback function a JSON result format would be wrapped in to support Ajax requests. | [optional] |
| **failureRedirectUrl** | **String**| The url to redirect if the geomark could not be created. The URL will include a &lt;fieldName&gt;_Error parameter with the error message for the field that caused the error. | [optional] |
| **format** | **String**| The file format name extension of the input geometry. | [optional] [enum: json, xml, kml, kmz, shp, shpz, geojson, gml, gpkg, wkt] |
| **multiple** | **Boolean**| Boolean flag indicating if multiple geometries are to be used for the geomark (true) or only a single geometry from the first geometry (false). | [optional] [default to false] |
| **redirectUrl** | **String**| The optional external URL to redirect the user to when the geomark is created rather than showing the geomark info page. The geomarkId and geomarkUrl query string parameters will be added to the redirectUrl so that the target application gets a reference to the geomark. | [optional] |
| **resultFormat** | **String**| The file format the geomark info resource should be returned using. | [optional] [enum: json, xml, kml, kmz, shp, shpz, geojson, gml, gpkg, wkt] |
| **srid** | **Integer**| The srid of the coordinate system the input geometries are in. If the file includes a coordinate system definition that will be used. | [optional] [default to 4326] [enum: 4326, 3005, 3857, 26907, 26908, 26909, 26910, 26911] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If the geomark was created via a web service call. |  -  |
| **302** | If the geomark was created and a redirectUrl was specified then the response will redirect to the redirectUrl with the query string parameters geomarkId and geomarkUrl of the created geomark.  Additional reasons for this status code can be found in the [Geomark Web Service Developer Guide](https://apps.gov.bc.ca/pub/geomark/docs/rest-api/) |  -  |
| **400** | **Couldn&#39;t create Geomark.**  Possible reasons:  * No Polygon, Multi-Polygon, or folder(set) of Polygons provided. * A point or line was provided without a buffer width.  Additional reasons for this status code can be found in the [Geomark Web Service Developer Guide](https://apps.gov.bc.ca/pub/geomark/docs/rest-api/) |  -  |
| **500** | **Internal Server Error** |  -  |

