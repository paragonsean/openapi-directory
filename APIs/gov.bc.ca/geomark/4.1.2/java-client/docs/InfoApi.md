# InfoApi

All URIs are relative to *https://apps.gov.bc.ca/pub/geomark*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**geomarksGeomarkIdFileFormatExtensionGet**](InfoApi.md#geomarksGeomarkIdFileFormatExtensionGet) | **GET** /geomarks/{geomarkId}.{fileFormatExtension} | Get information about a particular geomark |


<a id="geomarksGeomarkIdFileFormatExtensionGet"></a>
# **geomarksGeomarkIdFileFormatExtensionGet**
> geomarksGeomarkIdFileFormatExtensionGet(geomarkId, fileFormatExtension, srid)

Get information about a particular geomark

The attribution can be downloaded as a info file format. The download files can then be processed by a client application to access the geomark info fields and to get the URLs to the geometry download resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/geomark");

    InfoApi apiInstance = new InfoApi(defaultClient);
    String geomarkId = "gm-abcdefghijklmnopqrstuv0bcislands"; // String | The unique identifier for the geomark.
    String fileFormatExtension = "json"; // String | The file format name extension used to represent the geomark download.
    Integer srid = 4326; // Integer | The srid of the coordinate system the geometry should be converted to.
    try {
      apiInstance.geomarksGeomarkIdFileFormatExtensionGet(geomarkId, fileFormatExtension, srid);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#geomarksGeomarkIdFileFormatExtensionGet");
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
| **geomarkId** | **String**| The unique identifier for the geomark. | |
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
| **404** | **The geomark &lt;geomarkId&gt; could not be found.**  Check for extra characters on the end of the URL. The geomark may have expired and been deleted. |  -  |
| **500** | **Internal Server Error** |  -  |

