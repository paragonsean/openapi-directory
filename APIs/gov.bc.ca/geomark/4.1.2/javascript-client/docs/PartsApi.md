# GeoMarkWebServiceRestApi.PartsApi

All URIs are relative to *https://apps.gov.bc.ca/pub/geomark*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geomarksGeomarkIdPartsFileFormatExtensionGet**](PartsApi.md#geomarksGeomarkIdPartsFileFormatExtensionGet) | **GET** /geomarks/{geomarkId}/parts.{fileFormatExtension} | Get the individual geometries within a multi-part geometry



## geomarksGeomarkIdPartsFileFormatExtensionGet

> geomarksGeomarkIdPartsFileFormatExtensionGet(geomarkId, fileFormatExtension, opts)

Get the individual geometries within a multi-part geometry

The geomark parts resource returns a one or more spatial features. One for each part of the Geomark&#39;s geomerty. Each part contains a single (Point, LineString, Polygon) geometry and the geomark attribution.

### Example

```javascript
import GeoMarkWebServiceRestApi from 'geo_mark_web_service_rest_api';

let apiInstance = new GeoMarkWebServiceRestApi.PartsApi();
let geomarkId = "gm-abcdefghijklmnopqrstuv0bcislands"; // String | The unique identifier for the geomark
let fileFormatExtension = "json"; // String | The file format name extension used to represent the geomark download.
let opts = {
  'srid': 4326 // Number | The srid of the coordinate system the geometry should be converted to.
};
apiInstance.geomarksGeomarkIdPartsFileFormatExtensionGet(geomarkId, fileFormatExtension, opts, (error, data, response) => {
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
 **geomarkId** | **String**| The unique identifier for the geomark | 
 **fileFormatExtension** | **String**| The file format name extension used to represent the geomark download. | 
 **srid** | **Number**| The srid of the coordinate system the geometry should be converted to. | [optional] [default to 4326]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

