# PartsApi

All URIs are relative to *https://apps.gov.bc.ca/pub/geomark*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**geomarksGeomarkIdPartsFileFormatExtensionGet**](PartsApi.md#geomarksGeomarkIdPartsFileFormatExtensionGet) | **GET** /geomarks/{geomarkId}/parts.{fileFormatExtension} | Get the individual geometries within a multi-part geometry |


<a id="geomarksGeomarkIdPartsFileFormatExtensionGet"></a>
# **geomarksGeomarkIdPartsFileFormatExtensionGet**
> geomarksGeomarkIdPartsFileFormatExtensionGet(geomarkId, fileFormatExtension, srid)

Get the individual geometries within a multi-part geometry

The geomark parts resource returns a one or more spatial features. One for each part of the Geomark&#39;s geomerty. Each part contains a single (Point, LineString, Polygon) geometry and the geomark attribution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/geomark");

    PartsApi apiInstance = new PartsApi(defaultClient);
    String geomarkId = "gm-abcdefghijklmnopqrstuv0bcislands"; // String | The unique identifier for the geomark
    String fileFormatExtension = "json"; // String | The file format name extension used to represent the geomark download.
    Integer srid = 4326; // Integer | The srid of the coordinate system the geometry should be converted to.
    try {
      apiInstance.geomarksGeomarkIdPartsFileFormatExtensionGet(geomarkId, fileFormatExtension, srid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartsApi#geomarksGeomarkIdPartsFileFormatExtensionGet");
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
| **geomarkId** | **String**| The unique identifier for the geomark | |
| **fileFormatExtension** | **String**| The file format name extension used to represent the geomark download. | [enum: json, xml, kml, kmz, shp, shpz, geojson, gml, gpkg, wkt] |
| **srid** | **Integer**| The srid of the coordinate system the geometry should be converted to. | [optional] [default to 4326] [enum: 4326, 3005, 3857, 26907, 26908, 26909, 26910, 26911] |

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
| **200** | The geomark will be returned in the body of the HTTP response encoded in the requested [file format](https://apps.gov.bc.ca/pub/geomark/docs/fileFormats.html). |  -  |
| **400** | **Coordinate system with srid &#x3D; &lt;srid&gt; is not supported.**  Check the list of supported [coordinate systems](https://apps.gov.bc.ca/pub/geomark/docs/coordinateSystems.html). |  -  |
| **404** | **The geomark &lt;geomarkId&gt; could not be found.**  Check for extra characters on the end of the URL. The geomark may have expired and been deleted. |  -  |
| **500** | **Internal Server Error** |  -  |

