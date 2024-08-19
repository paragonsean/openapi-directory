# GeoMarkWebServiceRestApi.PointApi

All URIs are relative to *https://apps.gov.bc.ca/pub/geomark*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geomarksGeomarkIdPointFileFormatExtensionGet**](PointApi.md#geomarksGeomarkIdPointFileFormatExtensionGet) | **GET** /geomarks/{geomarkId}/point.{fileFormatExtension} | Gets a single spatial point representative of the geomark.



## geomarksGeomarkIdPointFileFormatExtensionGet

> geomarksGeomarkIdPointFileFormatExtensionGet(geomarkId, fileFormatExtension, opts)

Gets a single spatial point representative of the geomark.

The geomark point resource returns a single spatial feature with a single Point and the geomark attribution.  The point geometry will be created from the first geometry part of the Geomark. Point geomarks will return the first Point part in the geomark.  LineString geomarks will return the first coordinate of the first LineString part in the geomark. Polygon geomarks will return the centroid or another point inside the first Polygon part in the geomark. The geometry and attribution can be downloaded as a spatial download file format in a supported coordinate system. The download files can then be used in a desktop GIS application (e.g. ArcMap), Google Earth or a web mapping application.

### Example

```javascript
import GeoMarkWebServiceRestApi from 'geo_mark_web_service_rest_api';

let apiInstance = new GeoMarkWebServiceRestApi.PointApi();
let geomarkId = "gm-abcdefghijklmnopqrstuv0bcislands"; // String | The unique identifier for the geomark.
let fileFormatExtension = "json"; // String | The file format name extension used to represent the geomark download.
let opts = {
  'srid': 4326 // Number | The srid of the coordinate system the geometry should be converted to.
};
apiInstance.geomarksGeomarkIdPointFileFormatExtensionGet(geomarkId, fileFormatExtension, opts, (error, data, response) => {
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
 **geomarkId** | **String**| The unique identifier for the geomark. | 
 **fileFormatExtension** | **String**| The file format name extension used to represent the geomark download. | 
 **srid** | **Number**| The srid of the coordinate system the geometry should be converted to. | [optional] [default to 4326]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

