# Maps.WMSWMTSApi

All URIs are relative to *https://api.tomtom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCapabilities**](WMSWMTSApi.md#getCapabilities) | **GET** /map/{versionNumber}/wms// | GetCapabilities
[**getMap**](WMSWMTSApi.md#getMap) | **GET** /map/{versionNumber}/wms/ | GetMap
[**mapVersionNumberWmtsKeyWmtsVersionWMTSCapabilitiesXmlGet**](WMSWMTSApi.md#mapVersionNumberWmtsKeyWmtsVersionWMTSCapabilitiesXmlGet) | **GET** /map/{versionNumber}/wmts/{key}/{wmtsVersion}/WMTSCapabilities.xml | WMTS



## getCapabilities

> getCapabilities(versionNumber, service, request, opts)

GetCapabilities

The GetCapabilities call is part of TomTom&#39;s implementation of version 1.1.1 the Web Map Service (WMS). It provides descriptions of the other calls that are available in the implementation.

### Example

```javascript
import Maps from 'maps';
let defaultClient = Maps.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Maps.WMSWMTSApi();
let versionNumber = 56; // Number | 
let service = "service_example"; // String | 
let request = "request_example"; // String | 
let opts = {
  'version': "version_example" // String | WMS service version
};
apiInstance.getCapabilities(versionNumber, service, request, opts, (error, data, response) => {
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
 **versionNumber** | **Number**|  | 
 **service** | **String**|  | 
 **request** | **String**|  | 
 **version** | **String**| WMS service version | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMap

> getMap(versionNumber, request, srs, bbox, width, height, format, layers, version, opts)

GetMap

The GetMap call implements the Web Map Service 1.1.1 standard to access TomTom raster map tiles. This service is described in the response to the GetCapabilities API call.

### Example

```javascript
import Maps from 'maps';
let defaultClient = Maps.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Maps.WMSWMTSApi();
let versionNumber = 56; // Number | Version of the service to call. The current version is 1
let request = "request_example"; // String | Request type
let srs = "EPSG:4326"; // String | Projection used in describing the <b>bbox</b> EPSG:3857 is recommended, particularly at higher zoom levels. (Note that EPSG:3857 is functionally equivalent to EPSG:900913/EPSG:3785)
let bbox = "-0.489,51.28,0.236,51.686"; // String | Bounding box in the projection stated in <b>srs</b> (minLon,minLat,maxLon,maxLat)
let width = 512; // Number | Width of the resulting image, in pixels Maximum value is 2048
let height = 512; // Number | Height of the resulting image, in pixels Maximum value is 2048
let format = "image/png"; // String | Image format to be returned
let layers = "layers_example"; // String | Map layers requested Currently only the basic layer is available
let version = "version_example"; // String | WMS service version
let opts = {
  'styles': "styles_example", // String | Map styles to be returned. Currently, no styles are available. This parameter is present for forward compatibility; it must be used and left blank.
  'service': "service_example" // String | Service type
};
apiInstance.getMap(versionNumber, request, srs, bbox, width, height, format, layers, version, opts, (error, data, response) => {
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
 **request** | **String**| Request type | 
 **srs** | **String**| Projection used in describing the &lt;b&gt;bbox&lt;/b&gt; EPSG:3857 is recommended, particularly at higher zoom levels. (Note that EPSG:3857 is functionally equivalent to EPSG:900913/EPSG:3785) | 
 **bbox** | **String**| Bounding box in the projection stated in &lt;b&gt;srs&lt;/b&gt; (minLon,minLat,maxLon,maxLat) | 
 **width** | **Number**| Width of the resulting image, in pixels Maximum value is 2048 | 
 **height** | **Number**| Height of the resulting image, in pixels Maximum value is 2048 | 
 **format** | **String**| Image format to be returned | 
 **layers** | **String**| Map layers requested Currently only the basic layer is available | 
 **version** | **String**| WMS service version | 
 **styles** | **String**| Map styles to be returned. Currently, no styles are available. This parameter is present for forward compatibility; it must be used and left blank. | [optional] 
 **service** | **String**| Service type | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## mapVersionNumberWmtsKeyWmtsVersionWMTSCapabilitiesXmlGet

> mapVersionNumberWmtsKeyWmtsVersionWMTSCapabilitiesXmlGet(versionNumber, key, wmtsVersion)

WMTS

The WMTS GetCapabilities call implements version 1.0.0 of the &lt;a href&#x3D;\&quot;http://www.opengeospatial.org/standards/wmts\&quot;&gt;Web Map Tile Service&lt;/a&gt; (WMTS) standard. It returns metadata that allows compatible calling systems to construct calls to TomTom&#39;s raster map tile service. See the &lt;a href&#x3D;\&quot;/maps-api/maps-api-documentation-raster/wmts\&quot;&gt;documentation&lt;/a&gt; for more information on WMTS.

### Example

```javascript
import Maps from 'maps';

let apiInstance = new Maps.WMSWMTSApi();
let versionNumber = 56; // Number | Version of the service to call. The current version is 1
let key = "key_example"; // String | Your API key for calling this service.
let wmtsVersion = "wmtsVersion_example"; // String | 
apiInstance.mapVersionNumberWmtsKeyWmtsVersionWMTSCapabilitiesXmlGet(versionNumber, key, wmtsVersion, (error, data, response) => {
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
 **key** | **String**| Your API key for calling this service. | 
 **wmtsVersion** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

