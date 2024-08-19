# GeoMarkWebServiceRestApi.BoundingBoxApi

All URIs are relative to *https://apps.gov.bc.ca/pub/geomark*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geomarksGeomarkIdBoundingBoxFileFormatExtensionGet**](BoundingBoxApi.md#geomarksGeomarkIdBoundingBoxFileFormatExtensionGet) | **GET** /geomarks/{geomarkId}/boundingBox.{fileFormatExtension} | Gets the bounding box of the geomark



## geomarksGeomarkIdBoundingBoxFileFormatExtensionGet

> geomarksGeomarkIdBoundingBoxFileFormatExtensionGet(geomarkId, fileFormatExtension, opts)

Gets the bounding box of the geomark

The source geomarks can be specified by with the geomarkUrl parameter.  Repeat the parameter if sourcing from multiple geomarks

### Example

```javascript
import GeoMarkWebServiceRestApi from 'geo_mark_web_service_rest_api';

let apiInstance = new GeoMarkWebServiceRestApi.BoundingBoxApi();
let geomarkId = "gm-abcdefghijklmnopqrstuv0bcislands"; // String | The unique identifier for the geomark
let fileFormatExtension = "json"; // String | The file format name extension used to represent the geomark download.
let opts = {
  'srid': 4326 // Number | The srid of the coordinate system the geometry should be converted to.
};
apiInstance.geomarksGeomarkIdBoundingBoxFileFormatExtensionGet(geomarkId, fileFormatExtension, opts, (error, data, response) => {
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

