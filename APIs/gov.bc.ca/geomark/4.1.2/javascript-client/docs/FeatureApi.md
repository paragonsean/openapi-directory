# GeoMarkWebServiceRestApi.FeatureApi

All URIs are relative to *https://apps.gov.bc.ca/pub/geomark*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geomarksGeomarkIdFeatureFileFormatExtensionGet**](FeatureApi.md#geomarksGeomarkIdFeatureFileFormatExtensionGet) | **GET** /geomarks/{geomarkId}/feature.{fileFormatExtension} | Get the feature and attribution of the geomark



## geomarksGeomarkIdFeatureFileFormatExtensionGet

> geomarksGeomarkIdFeatureFileFormatExtensionGet(geomarkId, fileFormatExtension, opts)

Get the feature and attribution of the geomark

The geomark feature resource returns a single spatial feature with either a single (Point, LineString, Polygon) or multi-part geometry (MultiPoint, MultiLineString, MultiPolygon) and the geomark attribution.  The geometry and attribution can be downloaded as a spatial download file format in a supported coordinate system. The download files can then be used in a desktop GIS application (e.g. ArcMap), Google Earth or a web mapping application.

### Example

```javascript
import GeoMarkWebServiceRestApi from 'geo_mark_web_service_rest_api';

let apiInstance = new GeoMarkWebServiceRestApi.FeatureApi();
let geomarkId = "gm-abcdefghijklmnopqrstuv0bcislands"; // String | The unique identifier for the geomark
let fileFormatExtension = "json"; // String | The file format name extension used to represent the geomark download.
let opts = {
  'srid': 4326 // Number | The srid of the coordinate system the geometry should be converted to.
};
apiInstance.geomarksGeomarkIdFeatureFileFormatExtensionGet(geomarkId, fileFormatExtension, opts, (error, data, response) => {
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

