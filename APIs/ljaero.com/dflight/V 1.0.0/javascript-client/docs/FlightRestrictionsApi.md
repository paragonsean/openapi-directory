# DFlightApi.FlightRestrictionsApi

All URIs are relative to *https://dflight-api.ljaero.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tfrByDistanceUsV1RestrictionsDistanceQueryPost**](FlightRestrictionsApi.md#tfrByDistanceUsV1RestrictionsDistanceQueryPost) | **POST** /us/v1/restrictions/distance-query | Retrieve flight restrictions applicable within given distance of location.
[**tfrByPolyUsV1RestrictionsPolygonQueryPost**](FlightRestrictionsApi.md#tfrByPolyUsV1RestrictionsPolygonQueryPost) | **POST** /us/v1/restrictions/polygon-query | Retrieve flight restrictions applicable within given area.
[**tfrByRouteUsV1RestrictionsRouteQueryPost**](FlightRestrictionsApi.md#tfrByRouteUsV1RestrictionsRouteQueryPost) | **POST** /us/v1/restrictions/route-query | Retrieve flight restrictions applicable along route.



## tfrByDistanceUsV1RestrictionsDistanceQueryPost

> NOTAMsDistanceResponse tfrByDistanceUsV1RestrictionsDistanceQueryPost(nOTAMsByDistance, opts)

Retrieve flight restrictions applicable within given distance of location.

Retrieve Flight Restrictions applicable within given distance of a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.FlightRestrictionsApi();
let nOTAMsByDistance = new DFlightApi.NOTAMsByDistance(); // NOTAMsByDistance | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.tfrByDistanceUsV1RestrictionsDistanceQueryPost(nOTAMsByDistance, opts, (error, data, response) => {
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
 **nOTAMsByDistance** | [**NOTAMsByDistance**](NOTAMsByDistance.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**NOTAMsDistanceResponse**](NOTAMsDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tfrByPolyUsV1RestrictionsPolygonQueryPost

> NOTAMsPolyResponse tfrByPolyUsV1RestrictionsPolygonQueryPost(nOTAMsByPolygon, opts)

Retrieve flight restrictions applicable within given area.

Retrieve Flight Restrictions located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.FlightRestrictionsApi();
let nOTAMsByPolygon = new DFlightApi.NOTAMsByPolygon(); // NOTAMsByPolygon | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.tfrByPolyUsV1RestrictionsPolygonQueryPost(nOTAMsByPolygon, opts, (error, data, response) => {
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
 **nOTAMsByPolygon** | [**NOTAMsByPolygon**](NOTAMsByPolygon.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**NOTAMsPolyResponse**](NOTAMsPolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tfrByRouteUsV1RestrictionsRouteQueryPost

> NOTAMsRouteResponse tfrByRouteUsV1RestrictionsRouteQueryPost(nOTAMsByRoute, opts)

Retrieve flight restrictions applicable along route.

Retrieve Flight Restrictions applicable along your route. Request body parameters are: * route:  [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.FlightRestrictionsApi();
let nOTAMsByRoute = new DFlightApi.NOTAMsByRoute(); // NOTAMsByRoute | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.tfrByRouteUsV1RestrictionsRouteQueryPost(nOTAMsByRoute, opts, (error, data, response) => {
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
 **nOTAMsByRoute** | [**NOTAMsByRoute**](NOTAMsByRoute.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**NOTAMsRouteResponse**](NOTAMsRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

