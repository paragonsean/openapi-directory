# GeoMarkWebServiceRestApi.InfoApi

All URIs are relative to *https://apps.gov.bc.ca/pub/geomark*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geomarksGeomarkIdFileFormatExtensionGet**](InfoApi.md#geomarksGeomarkIdFileFormatExtensionGet) | **GET** /geomarks/{geomarkId}.{fileFormatExtension} | Get information about a particular geomark



## geomarksGeomarkIdFileFormatExtensionGet

> geomarksGeomarkIdFileFormatExtensionGet(geomarkId, fileFormatExtension, opts)

Get information about a particular geomark

The attribution can be downloaded as a info file format. The download files can then be processed by a client application to access the geomark info fields and to get the URLs to the geometry download resources.

### Example

```javascript
import GeoMarkWebServiceRestApi from 'geo_mark_web_service_rest_api';

let apiInstance = new GeoMarkWebServiceRestApi.InfoApi();
let geomarkId = "gm-abcdefghijklmnopqrstuv0bcislands"; // String | The unique identifier for the geomark.
let fileFormatExtension = "json"; // String | The file format name extension used to represent the geomark download.
let opts = {
  'srid': 4326 // Number | The srid of the coordinate system the geometry should be converted to.
};
apiInstance.geomarksGeomarkIdFileFormatExtensionGet(geomarkId, fileFormatExtension, opts, (error, data, response) => {
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

