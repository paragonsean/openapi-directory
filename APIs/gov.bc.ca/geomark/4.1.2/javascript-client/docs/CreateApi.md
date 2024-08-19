# GeoMarkWebServiceRestApi.CreateApi

All URIs are relative to *https://apps.gov.bc.ca/pub/geomark*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geomarksCopyPost**](CreateApi.md#geomarksCopyPost) | **POST** /geomarks/copy | Create a new geomark by copying the geometries from one or more existing geomarks from the current server.
[**geomarksNewPost**](CreateApi.md#geomarksNewPost) | **POST** /geomarks/new | Create a new geomark



## geomarksCopyPost

> geomarksCopyPost(geomarkUrl, opts)

Create a new geomark by copying the geometries from one or more existing geomarks from the current server.

The source geomarks can be specified by with the geomarkUrl parameter.  Repeat the parameter if sourcing from multiple geomarks

### Example

```javascript
import GeoMarkWebServiceRestApi from 'geo_mark_web_service_rest_api';

let apiInstance = new GeoMarkWebServiceRestApi.CreateApi();
let geomarkUrl = "https://apps.gov.bc.ca/pub/geomark/geomarks/gm-abcdefghijklmnopqrstuv0bcislands"; // String | One or more geomark URLs or identifiers to create the new geomark from.
let opts = {
  'resultFormat': "json", // String | The file format the geomark info resource should be returned using.
  'allowOverlap': false, // Boolean | Select this option to allow overlapping geometries
  'callback': "callback_example", // String | The callback function a JSON result format would be wrapped in to support Ajax requests.
  'redirectUrl': "redirectUrl_example", // String | The optional external URL to redirect the user to when the geomark is created rather than showing the geomark info page. The geomarkId and geomarkUrl query string parameters will be added to the redirectUrl so that the target application gets a reference to the geomark.
  'failureRedirectUrl': "failureRedirectUrl_example", // String | The url to redirect if the geomark could not be created. The URL will include a <fieldName>_Error parameter with the error message for the field that caused the error.
  'bufferMetres': 56, // Number | The amount to buffer the geometry in metres, must only contain numerical digits (e.g 10). Leave blank and no buffer will be added to input geometries. If blank then any Point, LineString, MultiPoint and MultiLineString geometries will be ignored.
  'bufferJoin': "'ROUND'", // String | If bufferMetres is specified, The style of buffer to use for joins between the line segments for lines and polygons.
  'bufferCap': "'ROUND'", // String | If bufferMetres is specified, The style of buffer to use at the ends of a buffered line.
  'bufferMitreLimit': 5, // Number | If bufferMetres is specified, the maximum ratio of distance from the original geometry to a mitre buffer point and the buffer amount. If the ratio is greater than this a bevel will be used instead. This prevents infinite distances when the angle between the two lines at a join is small. Must be > 0.
  'bufferSegments': 8 // Number | If bufferMetres is specified, the number of line segments used in each quadrant to approximate the curve for round end-cap and join styles. Must be > 0.
};
apiInstance.geomarksCopyPost(geomarkUrl, opts, (error, data, response) => {
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
 **geomarkUrl** | **String**| One or more geomark URLs or identifiers to create the new geomark from. | 
 **resultFormat** | **String**| The file format the geomark info resource should be returned using. | [optional] 
 **allowOverlap** | **Boolean**| Select this option to allow overlapping geometries | [optional] [default to false]
 **callback** | **String**| The callback function a JSON result format would be wrapped in to support Ajax requests. | [optional] 
 **redirectUrl** | **String**| The optional external URL to redirect the user to when the geomark is created rather than showing the geomark info page. The geomarkId and geomarkUrl query string parameters will be added to the redirectUrl so that the target application gets a reference to the geomark. | [optional] 
 **failureRedirectUrl** | **String**| The url to redirect if the geomark could not be created. The URL will include a &lt;fieldName&gt;_Error parameter with the error message for the field that caused the error. | [optional] 
 **bufferMetres** | **Number**| The amount to buffer the geometry in metres, must only contain numerical digits (e.g 10). Leave blank and no buffer will be added to input geometries. If blank then any Point, LineString, MultiPoint and MultiLineString geometries will be ignored. | [optional] 
 **bufferJoin** | **String**| If bufferMetres is specified, The style of buffer to use for joins between the line segments for lines and polygons. | [optional] [default to &#39;ROUND&#39;]
 **bufferCap** | **String**| If bufferMetres is specified, The style of buffer to use at the ends of a buffered line. | [optional] [default to &#39;ROUND&#39;]
 **bufferMitreLimit** | **Number**| If bufferMetres is specified, the maximum ratio of distance from the original geometry to a mitre buffer point and the buffer amount. If the ratio is greater than this a bevel will be used instead. This prevents infinite distances when the angle between the two lines at a join is small. Must be &gt; 0. | [optional] [default to 5]
 **bufferSegments** | **Number**| If bufferMetres is specified, the number of line segments used in each quadrant to approximate the curve for round end-cap and join styles. Must be &gt; 0. | [optional] [default to 8]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## geomarksNewPost

> geomarksNewPost(opts)

Create a new geomark

Create a new geomark from the geometries read from the &#39;body&#39; parameter or file.

### Example

```javascript
import GeoMarkWebServiceRestApi from 'geo_mark_web_service_rest_api';

let apiInstance = new GeoMarkWebServiceRestApi.CreateApi();
let opts = {
  'allowOverlap': false, // Boolean | When multiple=true select this option to allow overlapping geometries
  'body': "body_example", // String | The binary or character content representing the geometry or geometries
  'bufferCap': "'ROUND'", // String | If bufferMetres is specified, The style of buffer to use at the ends of a buffered line.
  'bufferJoin': "'ROUND'", // String | If bufferMetres is specified, The style of buffer to use for joins between the line segments for lines and polygons.
  'bufferMetres': 56, // Number | The amount to buffer the geometry in metres, must only contain numerical digits (e.g 10). Leave blank and no buffer will be added to input geometries. If blank then any Point, LineString, MultiPoint and MultiLineString geometries will be ignored.
  'bufferMitreLimit': 5, // Number | If bufferMetres is specified, the maximum ratio of distance from the original geometry to a mitre buffer point and the buffer amount. If the ratio is greater than this a bevel will be used instead. This prevents infinite distances when the angle between the two lines at a join is small. Must be > 0.
  'bufferSegments': 8, // Number | If bufferMetres is specified, the number of line segments used in each quadrant to approximate the curve for round end-cap and join styles. Must be > 0.
  'callback': "callback_example", // String | The callback function a JSON result format would be wrapped in to support Ajax requests.
  'failureRedirectUrl': "failureRedirectUrl_example", // String | The url to redirect if the geomark could not be created. The URL will include a <fieldName>_Error parameter with the error message for the field that caused the error.
  'format': "format_example", // String | The file format name extension of the input geometry.
  'multiple': false, // Boolean | Boolean flag indicating if multiple geometries are to be used for the geomark (true) or only a single geometry from the first geometry (false).
  'redirectUrl': "redirectUrl_example", // String | The optional external URL to redirect the user to when the geomark is created rather than showing the geomark info page. The geomarkId and geomarkUrl query string parameters will be added to the redirectUrl so that the target application gets a reference to the geomark.
  'resultFormat': "resultFormat_example", // String | The file format the geomark info resource should be returned using.
  'srid': 4326 // Number | The srid of the coordinate system the input geometries are in. If the file includes a coordinate system definition that will be used.
};
apiInstance.geomarksNewPost(opts, (error, data, response) => {
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
 **allowOverlap** | **Boolean**| When multiple&#x3D;true select this option to allow overlapping geometries | [optional] [default to false]
 **body** | **String**| The binary or character content representing the geometry or geometries | [optional] 
 **bufferCap** | **String**| If bufferMetres is specified, The style of buffer to use at the ends of a buffered line. | [optional] [default to &#39;ROUND&#39;]
 **bufferJoin** | **String**| If bufferMetres is specified, The style of buffer to use for joins between the line segments for lines and polygons. | [optional] [default to &#39;ROUND&#39;]
 **bufferMetres** | **Number**| The amount to buffer the geometry in metres, must only contain numerical digits (e.g 10). Leave blank and no buffer will be added to input geometries. If blank then any Point, LineString, MultiPoint and MultiLineString geometries will be ignored. | [optional] 
 **bufferMitreLimit** | **Number**| If bufferMetres is specified, the maximum ratio of distance from the original geometry to a mitre buffer point and the buffer amount. If the ratio is greater than this a bevel will be used instead. This prevents infinite distances when the angle between the two lines at a join is small. Must be &gt; 0. | [optional] [default to 5]
 **bufferSegments** | **Number**| If bufferMetres is specified, the number of line segments used in each quadrant to approximate the curve for round end-cap and join styles. Must be &gt; 0. | [optional] [default to 8]
 **callback** | **String**| The callback function a JSON result format would be wrapped in to support Ajax requests. | [optional] 
 **failureRedirectUrl** | **String**| The url to redirect if the geomark could not be created. The URL will include a &lt;fieldName&gt;_Error parameter with the error message for the field that caused the error. | [optional] 
 **format** | **String**| The file format name extension of the input geometry. | [optional] 
 **multiple** | **Boolean**| Boolean flag indicating if multiple geometries are to be used for the geomark (true) or only a single geometry from the first geometry (false). | [optional] [default to false]
 **redirectUrl** | **String**| The optional external URL to redirect the user to when the geomark is created rather than showing the geomark info page. The geomarkId and geomarkUrl query string parameters will be added to the redirectUrl so that the target application gets a reference to the geomark. | [optional] 
 **resultFormat** | **String**| The file format the geomark info resource should be returned using. | [optional] 
 **srid** | **Number**| The srid of the coordinate system the input geometries are in. If the file includes a coordinate system definition that will be used. | [optional] [default to 4326]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

