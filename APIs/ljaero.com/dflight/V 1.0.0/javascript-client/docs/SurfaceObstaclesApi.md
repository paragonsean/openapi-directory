# DFlightApi.SurfaceObstaclesApi

All URIs are relative to *https://dflight-api.ljaero.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**obstaclesByDistanceUsV1ObstaclesDistanceQueryPost**](SurfaceObstaclesApi.md#obstaclesByDistanceUsV1ObstaclesDistanceQueryPost) | **POST** /us/v1/obstacles/distance-query | Retrieve obstacles within given distance of location.
[**obstaclesByPolyUsV1ObstaclesPolygonQueryPost**](SurfaceObstaclesApi.md#obstaclesByPolyUsV1ObstaclesPolygonQueryPost) | **POST** /us/v1/obstacles/polygon-query | Retrieve obstacles located within given area.
[**obstaclesByRouteUsV1ObstaclesRouteQueryPost**](SurfaceObstaclesApi.md#obstaclesByRouteUsV1ObstaclesRouteQueryPost) | **POST** /us/v1/obstacles/route-query | Retrieve obstacles found along a route.



## obstaclesByDistanceUsV1ObstaclesDistanceQueryPost

> ObstacleDistanceResponse obstaclesByDistanceUsV1ObstaclesDistanceQueryPost(obstaclesByDistance, opts)

Retrieve obstacles within given distance of location.

Retrieve obstacles within given distance of a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.SurfaceObstaclesApi();
let obstaclesByDistance = new DFlightApi.ObstaclesByDistance(); // ObstaclesByDistance | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.obstaclesByDistanceUsV1ObstaclesDistanceQueryPost(obstaclesByDistance, opts, (error, data, response) => {
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
 **obstaclesByDistance** | [**ObstaclesByDistance**](ObstaclesByDistance.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**ObstacleDistanceResponse**](ObstacleDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## obstaclesByPolyUsV1ObstaclesPolygonQueryPost

> ObstaclePolyResponse obstaclesByPolyUsV1ObstaclesPolygonQueryPost(obstaclesByPolygon, opts)

Retrieve obstacles located within given area.

Retrieve obstacles located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.SurfaceObstaclesApi();
let obstaclesByPolygon = new DFlightApi.ObstaclesByPolygon(); // ObstaclesByPolygon | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.obstaclesByPolyUsV1ObstaclesPolygonQueryPost(obstaclesByPolygon, opts, (error, data, response) => {
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
 **obstaclesByPolygon** | [**ObstaclesByPolygon**](ObstaclesByPolygon.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**ObstaclePolyResponse**](ObstaclePolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## obstaclesByRouteUsV1ObstaclesRouteQueryPost

> ObstacleRouteResponse obstaclesByRouteUsV1ObstaclesRouteQueryPost(obstaclesByRoute, opts)

Retrieve obstacles found along a route.

Retrieve obstacles found along a route. Request body parameters are: * route: [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.SurfaceObstaclesApi();
let obstaclesByRoute = new DFlightApi.ObstaclesByRoute(); // ObstaclesByRoute | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.obstaclesByRouteUsV1ObstaclesRouteQueryPost(obstaclesByRoute, opts, (error, data, response) => {
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
 **obstaclesByRoute** | [**ObstaclesByRoute**](ObstaclesByRoute.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**ObstacleRouteResponse**](ObstacleRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

