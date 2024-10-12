# DFlightApi.UASOperatingAreasApi

All URIs are relative to *https://dflight-api.ljaero.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uoaByDistanceUsV1UoaDistanceQueryPost**](UASOperatingAreasApi.md#uoaByDistanceUsV1UoaDistanceQueryPost) | **POST** /us/v1/uoa/distance-query | Retrieve UAS Operating Areas (UOAs) found within given distance of location.
[**uoaByPolyUsV1UoaPolygonQueryPost**](UASOperatingAreasApi.md#uoaByPolyUsV1UoaPolygonQueryPost) | **POST** /us/v1/uoa/polygon-query | Retrieve UAS Operating Areas (UOAs) found within given area.
[**uoaByRouteUsV1UoaRouteQueryPost**](UASOperatingAreasApi.md#uoaByRouteUsV1UoaRouteQueryPost) | **POST** /us/v1/uoa/route-query | Retrieve UAS Operating Areas (UOAs) found along route.



## uoaByDistanceUsV1UoaDistanceQueryPost

> UOAsDistanceResponse uoaByDistanceUsV1UoaDistanceQueryPost(uOAsByDistance, opts)

Retrieve UAS Operating Areas (UOAs) found within given distance of location.

Retrieve UAS Operating Areas (UOAs) found within given distance of a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.UASOperatingAreasApi();
let uOAsByDistance = new DFlightApi.UOAsByDistance(); // UOAsByDistance | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.uoaByDistanceUsV1UoaDistanceQueryPost(uOAsByDistance, opts, (error, data, response) => {
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
 **uOAsByDistance** | [**UOAsByDistance**](UOAsByDistance.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**UOAsDistanceResponse**](UOAsDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## uoaByPolyUsV1UoaPolygonQueryPost

> UOAsPolyResponse uoaByPolyUsV1UoaPolygonQueryPost(uOAsByPolygon, opts)

Retrieve UAS Operating Areas (UOAs) found within given area.

Retrieve UAS Operating Areas (UOAs) found within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.UASOperatingAreasApi();
let uOAsByPolygon = new DFlightApi.UOAsByPolygon(); // UOAsByPolygon | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.uoaByPolyUsV1UoaPolygonQueryPost(uOAsByPolygon, opts, (error, data, response) => {
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
 **uOAsByPolygon** | [**UOAsByPolygon**](UOAsByPolygon.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**UOAsPolyResponse**](UOAsPolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## uoaByRouteUsV1UoaRouteQueryPost

> UOAsRouteResponse uoaByRouteUsV1UoaRouteQueryPost(uOAsByRoute, opts)

Retrieve UAS Operating Areas (UOAs) found along route.

Retrieve UAS Operating Areas (UOAs) found along your route. Request body parameters are: * route:  [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.UASOperatingAreasApi();
let uOAsByRoute = new DFlightApi.UOAsByRoute(); // UOAsByRoute | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.uoaByRouteUsV1UoaRouteQueryPost(uOAsByRoute, opts, (error, data, response) => {
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
 **uOAsByRoute** | [**UOAsByRoute**](UOAsByRoute.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**UOAsRouteResponse**](UOAsRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

