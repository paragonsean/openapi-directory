# Maps.CopyrightsApi

All URIs are relative to *https://api.tomtom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapVersionNumberCopyrightsCaptionFormatGet**](CopyrightsApi.md#mapVersionNumberCopyrightsCaptionFormatGet) | **GET** /map/{versionNumber}/copyrights/caption.{format} | Captions
[**mapVersionNumberCopyrightsFormatGet**](CopyrightsApi.md#mapVersionNumberCopyrightsFormatGet) | **GET** /map/{versionNumber}/copyrights.{format} | Copyrights whole world
[**mapVersionNumberCopyrightsMinLonMinLatMaxLonMaxLatFormatGet**](CopyrightsApi.md#mapVersionNumberCopyrightsMinLonMinLatMaxLonMaxLatFormatGet) | **GET** /map/{versionNumber}/copyrights/{minLon}/{minLat}/{maxLon}/{maxLat}.{format} | Copyrights bounding box
[**mapVersionNumberCopyrightsZoomXYFormatGet**](CopyrightsApi.md#mapVersionNumberCopyrightsZoomXYFormatGet) | **GET** /map/{versionNumber}/copyrights/{zoom}/{X}/{Y}.{format} | Copyrights tile



## mapVersionNumberCopyrightsCaptionFormatGet

> mapVersionNumberCopyrightsCaptionFormatGet(versionNumber, format, opts)

Captions

This API returns copyright captions for the map service.

### Example

```javascript
import Maps from 'maps';
let defaultClient = Maps.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Maps.CopyrightsApi();
let versionNumber = 56; // Number | Version of the service to call. The current version is 1.
let format = "'xml'"; // String | Format of the response
let opts = {
  'callback': "callback_example" // String | Specifies the jsonp callback method. Only used when format is jsonp
};
apiInstance.mapVersionNumberCopyrightsCaptionFormatGet(versionNumber, format, opts, (error, data, response) => {
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
 **versionNumber** | **Number**| Version of the service to call. The current version is 1. | 
 **format** | **String**| Format of the response | [default to &#39;xml&#39;]
 **callback** | **String**| Specifies the jsonp callback method. Only used when format is jsonp | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## mapVersionNumberCopyrightsFormatGet

> mapVersionNumberCopyrightsFormatGet(versionNumber, format, opts)

Copyrights whole world

The Copyrights API returns copyright information for the Maps API Raster Tile Service in JSON, JSONP, or XML format. This call returns copyright information for the whole world.

### Example

```javascript
import Maps from 'maps';
let defaultClient = Maps.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Maps.CopyrightsApi();
let versionNumber = 56; // Number | Version of the service to call. The current version is 1
let format = "'xml'"; // String | Format of the response
let opts = {
  'callback': "callback_example" // String | Specifies the jsonp callback method. Only used when format is jsonp
};
apiInstance.mapVersionNumberCopyrightsFormatGet(versionNumber, format, opts, (error, data, response) => {
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
 **versionNumber** | **Number**| Version of the service to call. The current version is 1 | 
 **format** | **String**| Format of the response | [default to &#39;xml&#39;]
 **callback** | **String**| Specifies the jsonp callback method. Only used when format is jsonp | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## mapVersionNumberCopyrightsMinLonMinLatMaxLonMaxLatFormatGet

> mapVersionNumberCopyrightsMinLonMinLatMaxLonMaxLatFormatGet(versionNumber, format, minLon, minLat, maxLon, maxLat, opts)

Copyrights bounding box

The Copyrights API returns copyright information for the Maps API Raster Tile Service in JSON, JSONP, or XML format. This call returns copyright information for a specific bounding box.

### Example

```javascript
import Maps from 'maps';
let defaultClient = Maps.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Maps.CopyrightsApi();
let versionNumber = 56; // Number | Version of the service to call. The current version is 1
let format = "'xml'"; // String | Format of the response
let minLon = -179.1506; // Number | Minimum longitude coordinate of bounding box defined in terms of latitude/longitude.
let minLat = 18.9117; // Number | Minimum latitude coordinate of bounding box defined in terms of latitude/longitude.
let maxLon = -66.9406; // Number | Maximum longitude coordinate of bounding box defined in terms of latitude/longitude.
let maxLat = 71.441; // Number | Maximum latitude coordinate of bounding box defined in terms of latitude/longitude.
let opts = {
  'callback': "callback_example" // String | Specifies the jsonp callback method. Only used when format is jsonp.
};
apiInstance.mapVersionNumberCopyrightsMinLonMinLatMaxLonMaxLatFormatGet(versionNumber, format, minLon, minLat, maxLon, maxLat, opts, (error, data, response) => {
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
 **versionNumber** | **Number**| Version of the service to call. The current version is 1 | 
 **format** | **String**| Format of the response | [default to &#39;xml&#39;]
 **minLon** | **Number**| Minimum longitude coordinate of bounding box defined in terms of latitude/longitude. | 
 **minLat** | **Number**| Minimum latitude coordinate of bounding box defined in terms of latitude/longitude. | 
 **maxLon** | **Number**| Maximum longitude coordinate of bounding box defined in terms of latitude/longitude. | 
 **maxLat** | **Number**| Maximum latitude coordinate of bounding box defined in terms of latitude/longitude. | 
 **callback** | **String**| Specifies the jsonp callback method. Only used when format is jsonp. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## mapVersionNumberCopyrightsZoomXYFormatGet

> mapVersionNumberCopyrightsZoomXYFormatGet(versionNumber, format, zoom, X, Y, opts)

Copyrights tile

The Copyrights API returns copyright information for the Maps API Raster Tile Service in JSON, JSONP, or XML format. This call returns copyright information for the a specific map tile.

### Example

```javascript
import Maps from 'maps';
let defaultClient = Maps.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Maps.CopyrightsApi();
let versionNumber = 56; // Number | Version of the service to call. The current version is 1
let format = "'xml'"; // String | Format of the response
let zoom = 0; // Number | Zoom level of tile to be rendered. Only used for tile-level copyright calls.
let X = 0; // Number | X coordinate of the tile on zoom grid. Only used for tile-level copyright calls.
let Y = 0; // Number | Y coordinate of the tile on zoom grid. Only used for tile-level copyright calls.
let opts = {
  'callback': "callback_example" // String | Specifies the jsonp callback method. Only used when format is jsonp.
};
apiInstance.mapVersionNumberCopyrightsZoomXYFormatGet(versionNumber, format, zoom, X, Y, opts, (error, data, response) => {
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
 **versionNumber** | **Number**| Version of the service to call. The current version is 1 | 
 **format** | **String**| Format of the response | [default to &#39;xml&#39;]
 **zoom** | **Number**| Zoom level of tile to be rendered. Only used for tile-level copyright calls. | 
 **X** | **Number**| X coordinate of the tile on zoom grid. Only used for tile-level copyright calls. | 
 **Y** | **Number**| Y coordinate of the tile on zoom grid. Only used for tile-level copyright calls. | 
 **callback** | **String**| Specifies the jsonp callback method. Only used when format is jsonp. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

