# DFlightApi.AerodromesApi

All URIs are relative to *https://dflight-api.ljaero.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aerodromesByDistanceUsV1AerodromesDistanceQueryPost**](AerodromesApi.md#aerodromesByDistanceUsV1AerodromesDistanceQueryPost) | **POST** /us/v1/aerodromes/distance-query | Retrieve aerodromes within given distance of location.
[**aerodromesByPolyUsV1AerodromesPolygonQueryPost**](AerodromesApi.md#aerodromesByPolyUsV1AerodromesPolygonQueryPost) | **POST** /us/v1/aerodromes/polygon-query | Retrieve aerodromes located within given area.
[**aerodromesByRouteUsV1AerodromesRouteQueryPost**](AerodromesApi.md#aerodromesByRouteUsV1AerodromesRouteQueryPost) | **POST** /us/v1/aerodromes/route-query | Retrieve aerodromes found along a route.



## aerodromesByDistanceUsV1AerodromesDistanceQueryPost

> AerodromeDistanceResponse aerodromesByDistanceUsV1AerodromesDistanceQueryPost(aerodromesByDistance, opts)

Retrieve aerodromes within given distance of location.

Retrieve aerodromes within given distance of a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)  Successful requests return a GeoJSON FeatureCollection, with a separate Feature for each Aerodrome found. All Features will include properties for the facility name, ident, type, and operational status.

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.AerodromesApi();
let aerodromesByDistance = new DFlightApi.AerodromesByDistance(); // AerodromesByDistance | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.aerodromesByDistanceUsV1AerodromesDistanceQueryPost(aerodromesByDistance, opts, (error, data, response) => {
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
 **aerodromesByDistance** | [**AerodromesByDistance**](AerodromesByDistance.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**AerodromeDistanceResponse**](AerodromeDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aerodromesByPolyUsV1AerodromesPolygonQueryPost

> AerodromePolyResponse aerodromesByPolyUsV1AerodromesPolygonQueryPost(aerodromesByPolygon, opts)

Retrieve aerodromes located within given area.

Retrieve aerodromes located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.  Successful requests return a GeoJSON FeatureCollection, with a separate Feature for each Aerodrome found. All Features will include properties for the facility name, ident, type, and operational status.

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.AerodromesApi();
let aerodromesByPolygon = new DFlightApi.AerodromesByPolygon(); // AerodromesByPolygon | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.aerodromesByPolyUsV1AerodromesPolygonQueryPost(aerodromesByPolygon, opts, (error, data, response) => {
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
 **aerodromesByPolygon** | [**AerodromesByPolygon**](AerodromesByPolygon.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**AerodromePolyResponse**](AerodromePolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## aerodromesByRouteUsV1AerodromesRouteQueryPost

> AerodromeRouteResponse aerodromesByRouteUsV1AerodromesRouteQueryPost(aerodromesByRoute, opts)

Retrieve aerodromes found along a route.

Retrieve aerodromes found along a route. Request body parameters are: * route: [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.  Successful requests return a GeoJSON FeatureCollection, with a separate Feature for each Aerodrome found. All Features will include properties for the facility name, ident, type, and operational status.

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.AerodromesApi();
let aerodromesByRoute = new DFlightApi.AerodromesByRoute(); // AerodromesByRoute | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.aerodromesByRouteUsV1AerodromesRouteQueryPost(aerodromesByRoute, opts, (error, data, response) => {
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
 **aerodromesByRoute** | [**AerodromesByRoute**](AerodromesByRoute.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**AerodromeRouteResponse**](AerodromeRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

