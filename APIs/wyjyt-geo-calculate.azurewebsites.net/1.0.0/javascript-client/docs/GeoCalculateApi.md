# WyjytGeoCalculate.GeoCalculateApi

All URIs are relative to *https://wyjyt-geo-calculate.azurewebsites.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert**](GeoCalculateApi.md#convert) | **POST** /Convert | Convert the list of geo coordinates to a standard format - (latlon | utm | mgrs | ecef | epsg3857 | georef | cartesian)
[**distance**](GeoCalculateApi.md#distance) | **POST** /Distance | Calculate the distance between two geo coordinates.
[**fence**](GeoCalculateApi.md#fence) | **POST** /Fence | Check if a list of coordinates are inside of a fence of coordinates.
[**sky**](GeoCalculateApi.md#sky) | **POST** /Sky | Calculate sun, moon, eclipse and sky information for the date and location.



## convert

> GeoConvertResponse convert(geoConvertRequest)

Convert the list of geo coordinates to a standard format - (latlon | utm | mgrs | ecef | epsg3857 | georef | cartesian)

Convert the list of geo coordinates to a standard format - (latlon | utm | mgrs | ecef | epsg3857 | georef | cartesian)

### Example

```javascript
import WyjytGeoCalculate from 'wyjyt_geo_calculate';

let apiInstance = new WyjytGeoCalculate.GeoCalculateApi();
let geoConvertRequest = new WyjytGeoCalculate.GeoConvertRequest(); // GeoConvertRequest | 
apiInstance.convert(geoConvertRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geoConvertRequest** | [**GeoConvertRequest**](GeoConvertRequest.md)|  | 

### Return type

[**GeoConvertResponse**](GeoConvertResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## distance

> GeoDistanceResponse distance(geoDistanceRequest)

Calculate the distance between two geo coordinates.

Calculate the distance between two geo coordinates.

### Example

```javascript
import WyjytGeoCalculate from 'wyjyt_geo_calculate';

let apiInstance = new WyjytGeoCalculate.GeoCalculateApi();
let geoDistanceRequest = new WyjytGeoCalculate.GeoDistanceRequest(); // GeoDistanceRequest | 
apiInstance.distance(geoDistanceRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geoDistanceRequest** | [**GeoDistanceRequest**](GeoDistanceRequest.md)|  | 

### Return type

[**GeoDistanceResponse**](GeoDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## fence

> GeoFenceResponse fence(geoFenceRequest)

Check if a list of coordinates are inside of a fence of coordinates.

Check if a list of coordinates are inside of a fence of coordinates.

### Example

```javascript
import WyjytGeoCalculate from 'wyjyt_geo_calculate';

let apiInstance = new WyjytGeoCalculate.GeoCalculateApi();
let geoFenceRequest = new WyjytGeoCalculate.GeoFenceRequest(); // GeoFenceRequest | 
apiInstance.fence(geoFenceRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geoFenceRequest** | [**GeoFenceRequest**](GeoFenceRequest.md)|  | 

### Return type

[**GeoFenceResponse**](GeoFenceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sky

> GeoSkyResponse sky(geoSkyRequest)

Calculate sun, moon, eclipse and sky information for the date and location.

Calculate sun, moon, eclipse and sky information for the date and location.

### Example

```javascript
import WyjytGeoCalculate from 'wyjyt_geo_calculate';

let apiInstance = new WyjytGeoCalculate.GeoCalculateApi();
let geoSkyRequest = new WyjytGeoCalculate.GeoSkyRequest(); // GeoSkyRequest | 
apiInstance.sky(geoSkyRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geoSkyRequest** | [**GeoSkyRequest**](GeoSkyRequest.md)|  | 

### Return type

[**GeoSkyResponse**](GeoSkyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

