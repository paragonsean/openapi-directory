# PtvTimetableApiVersion3.RoutesApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**routesOneOrMoreRoutes**](RoutesApi.md#routesOneOrMoreRoutes) | **GET** /v3/routes | View route names and numbers for all routes
[**routesRouteFromId**](RoutesApi.md#routesRouteFromId) | **GET** /v3/routes/{route_id} | View route name and number for specific route ID



## routesOneOrMoreRoutes

> V3RouteResponse routesOneOrMoreRoutes(opts)

View route names and numbers for all routes

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.RoutesApi();
let opts = {
  'routeTypes': [null], // [Number] | Filter by route_type; values returned via RouteTypes API
  'routeName': "routeName_example", // String | Filter by name  of route (accepts partial route name matches)
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.routesOneOrMoreRoutes(opts, (error, data, response) => {
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
 **routeTypes** | [**[Number]**](Number.md)| Filter by route_type; values returned via RouteTypes API | [optional] 
 **routeName** | **String**| Filter by name  of route (accepts partial route name matches) | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3RouteResponse**](V3RouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json


## routesRouteFromId

> V3RouteResponse routesRouteFromId(routeId, opts)

View route name and number for specific route ID

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.RoutesApi();
let routeId = 56; // Number | Identifier of route; values returned by Departures, Directions and Disruptions APIs
let opts = {
  'includeGeopath': true, // Boolean | Indicates kif geopath data will be returned (default = false)
  'geopathUtc': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter geopaths by date (ISO 8601 UTC format) (default = current date)
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.routesRouteFromId(routeId, opts, (error, data, response) => {
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
 **routeId** | **Number**| Identifier of route; values returned by Departures, Directions and Disruptions APIs | 
 **includeGeopath** | **Boolean**| Indicates kif geopath data will be returned (default &#x3D; false) | [optional] 
 **geopathUtc** | **Date**| Filter geopaths by date (ISO 8601 UTC format) (default &#x3D; current date) | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3RouteResponse**](V3RouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json

