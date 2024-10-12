# DFlightApi.RestrictedPublicVenuesApi

All URIs are relative to *https://dflight-api.ljaero.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**venByDistanceUsV1VenuesDistanceQueryPost**](RestrictedPublicVenuesApi.md#venByDistanceUsV1VenuesDistanceQueryPost) | **POST** /us/v1/venues/distance-query | Retrieve all restricted public venues located within given distance of location.
[**venByPolyUsV1VenuesPolygonQueryPost**](RestrictedPublicVenuesApi.md#venByPolyUsV1VenuesPolygonQueryPost) | **POST** /us/v1/venues/polygon-query | Retrieve all restricted public venues located within given GeoJSON Polygon.
[**venByRouteUsV1VenuesRouteQueryPost**](RestrictedPublicVenuesApi.md#venByRouteUsV1VenuesRouteQueryPost) | **POST** /us/v1/venues/route-query | Retrieve all restricted public venues traversed by route.



## venByDistanceUsV1VenuesDistanceQueryPost

> VenueDistanceResponse venByDistanceUsV1VenuesDistanceQueryPost(venuesByDistance, opts)

Retrieve all restricted public venues located within given distance of location.

Retrieve venues existing within given distance from a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.RestrictedPublicVenuesApi();
let venuesByDistance = new DFlightApi.VenuesByDistance(); // VenuesByDistance | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.venByDistanceUsV1VenuesDistanceQueryPost(venuesByDistance, opts, (error, data, response) => {
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
 **venuesByDistance** | [**VenuesByDistance**](VenuesByDistance.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**VenueDistanceResponse**](VenueDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## venByPolyUsV1VenuesPolygonQueryPost

> VenuePolyResponse venByPolyUsV1VenuesPolygonQueryPost(venuesByPolygon, opts)

Retrieve all restricted public venues located within given GeoJSON Polygon.

Retrieve all restricted public venues located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.RestrictedPublicVenuesApi();
let venuesByPolygon = new DFlightApi.VenuesByPolygon(); // VenuesByPolygon | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.venByPolyUsV1VenuesPolygonQueryPost(venuesByPolygon, opts, (error, data, response) => {
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
 **venuesByPolygon** | [**VenuesByPolygon**](VenuesByPolygon.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**VenuePolyResponse**](VenuePolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## venByRouteUsV1VenuesRouteQueryPost

> VenueRouteResponse venByRouteUsV1VenuesRouteQueryPost(venuesByRoute, opts)

Retrieve all restricted public venues traversed by route.

Retrieve all restricted public venues intersected by route. Request body parameters are: * route: [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.RestrictedPublicVenuesApi();
let venuesByRoute = new DFlightApi.VenuesByRoute(); // VenuesByRoute | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.venByRouteUsV1VenuesRouteQueryPost(venuesByRoute, opts, (error, data, response) => {
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
 **venuesByRoute** | [**VenuesByRoute**](VenuesByRoute.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**VenueRouteResponse**](VenueRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

