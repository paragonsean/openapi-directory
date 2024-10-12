# DFlightApi.SpecialSecurityAreasApi

All URIs are relative to *https://dflight-api.ljaero.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ssaByDistanceUsV1SsaDistanceQueryPost**](SpecialSecurityAreasApi.md#ssaByDistanceUsV1SsaDistanceQueryPost) | **POST** /us/v1/ssa/distance-query | Retrieve all special security areas located within given distance of location.
[**ssaByPolyUsV1SsaPolygonQueryPost**](SpecialSecurityAreasApi.md#ssaByPolyUsV1SsaPolygonQueryPost) | **POST** /us/v1/ssa/polygon-query | Retrieve all special security areas located within given GeoJSON Polygon.
[**ssaByRouteUsV1SsaRouteQueryPost**](SpecialSecurityAreasApi.md#ssaByRouteUsV1SsaRouteQueryPost) | **POST** /us/v1/ssa/route-query | Retrieve all special security areas traversed by route.



## ssaByDistanceUsV1SsaDistanceQueryPost

> SSADistanceResponse ssaByDistanceUsV1SsaDistanceQueryPost(sSAByDistance, opts)

Retrieve all special security areas located within given distance of location.

Retrieve special security areas existing within given distance from a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.SpecialSecurityAreasApi();
let sSAByDistance = new DFlightApi.SSAByDistance(); // SSAByDistance | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.ssaByDistanceUsV1SsaDistanceQueryPost(sSAByDistance, opts, (error, data, response) => {
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
 **sSAByDistance** | [**SSAByDistance**](SSAByDistance.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**SSADistanceResponse**](SSADistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ssaByPolyUsV1SsaPolygonQueryPost

> SSAPolyResponse ssaByPolyUsV1SsaPolygonQueryPost(sSAByPolygon, opts)

Retrieve all special security areas located within given GeoJSON Polygon.

Retrieve all special security areas located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.SpecialSecurityAreasApi();
let sSAByPolygon = new DFlightApi.SSAByPolygon(); // SSAByPolygon | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.ssaByPolyUsV1SsaPolygonQueryPost(sSAByPolygon, opts, (error, data, response) => {
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
 **sSAByPolygon** | [**SSAByPolygon**](SSAByPolygon.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**SSAPolyResponse**](SSAPolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ssaByRouteUsV1SsaRouteQueryPost

> SSARouteResponse ssaByRouteUsV1SsaRouteQueryPost(sSAByRoute, opts)

Retrieve all special security areas traversed by route.

Retrieve all special security areas intersected by route. Request body parameters are: * route: [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.SpecialSecurityAreasApi();
let sSAByRoute = new DFlightApi.SSAByRoute(); // SSAByRoute | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.ssaByRouteUsV1SsaRouteQueryPost(sSAByRoute, opts, (error, data, response) => {
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
 **sSAByRoute** | [**SSAByRoute**](SSAByRoute.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**SSARouteResponse**](SSARouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

