# PtvTimetableApiVersion3.StopsApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stopsStopDetails**](StopsApi.md#stopsStopDetails) | **GET** /v3/stops/{stop_id}/route_type/{route_type} | View facilities at a specific stop (Metro and V/Line stations only)
[**stopsStopsByGeolocation**](StopsApi.md#stopsStopsByGeolocation) | **GET** /v3/stops/location/{latitude},{longitude} | View all stops near a specific location
[**stopsStopsForRoute**](StopsApi.md#stopsStopsForRoute) | **GET** /v3/stops/route/{route_id}/route_type/{route_type} | View all stops on a specific route



## stopsStopDetails

> V3StopResponse stopsStopDetails(stopId, routeType, opts)

View facilities at a specific stop (Metro and V/Line stations only)

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.StopsApi();
let stopId = 56; // Number | Identifier of stop; values returned by Stops API
let routeType = 56; // Number | Number identifying transport mode; values returned via RouteTypes API
let opts = {
  'stopLocation': true, // Boolean | Indicates if stop location information will be returned (default = false)
  'stopAmenities': true, // Boolean | Indicates if stop amenity information will be returned (default = false)
  'stopAccessibility': true, // Boolean | Indicates if stop accessibility information will be returned (default = false)
  'stopContact': true, // Boolean | Indicates if stop contact information will be returned (default = false)
  'stopTicket': true, // Boolean | Indicates if stop ticket information will be returned (default = false)
  'gtfs': true, // Boolean | Incdicates whether the stop_id is a GTFS ID or not
  'stopStaffing': true, // Boolean | Indicates if stop staffing information will be returned (default = false)
  'stopDisruptions': true, // Boolean | Indicates if stop disruption information will be returned (default = false)
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.stopsStopDetails(stopId, routeType, opts, (error, data, response) => {
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
 **stopId** | **Number**| Identifier of stop; values returned by Stops API | 
 **routeType** | **Number**| Number identifying transport mode; values returned via RouteTypes API | 
 **stopLocation** | **Boolean**| Indicates if stop location information will be returned (default &#x3D; false) | [optional] 
 **stopAmenities** | **Boolean**| Indicates if stop amenity information will be returned (default &#x3D; false) | [optional] 
 **stopAccessibility** | **Boolean**| Indicates if stop accessibility information will be returned (default &#x3D; false) | [optional] 
 **stopContact** | **Boolean**| Indicates if stop contact information will be returned (default &#x3D; false) | [optional] 
 **stopTicket** | **Boolean**| Indicates if stop ticket information will be returned (default &#x3D; false) | [optional] 
 **gtfs** | **Boolean**| Incdicates whether the stop_id is a GTFS ID or not | [optional] 
 **stopStaffing** | **Boolean**| Indicates if stop staffing information will be returned (default &#x3D; false) | [optional] 
 **stopDisruptions** | **Boolean**| Indicates if stop disruption information will be returned (default &#x3D; false) | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3StopResponse**](V3StopResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json


## stopsStopsByGeolocation

> V3StopsByDistanceResponse stopsStopsByGeolocation(latitude, longitude, opts)

View all stops near a specific location

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.StopsApi();
let latitude = 3.4; // Number | Geographic coordinate of latitude
let longitude = 3.4; // Number | Geographic coordinate of longitude
let opts = {
  'routeTypes': [null], // [Number] | Filter by route_type; values returned via RouteTypes API
  'maxResults': 56, // Number | Maximum number of results returned (default = 30)
  'maxDistance': 3.4, // Number | Filter by maximum distance (in metres) from location specified via latitude and longitude parameters (default = 300)
  'stopDisruptions': true, // Boolean | Indicates if stop disruption information will be returned (default = false)
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.stopsStopsByGeolocation(latitude, longitude, opts, (error, data, response) => {
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
 **latitude** | **Number**| Geographic coordinate of latitude | 
 **longitude** | **Number**| Geographic coordinate of longitude | 
 **routeTypes** | [**[Number]**](Number.md)| Filter by route_type; values returned via RouteTypes API | [optional] 
 **maxResults** | **Number**| Maximum number of results returned (default &#x3D; 30) | [optional] 
 **maxDistance** | **Number**| Filter by maximum distance (in metres) from location specified via latitude and longitude parameters (default &#x3D; 300) | [optional] 
 **stopDisruptions** | **Boolean**| Indicates if stop disruption information will be returned (default &#x3D; false) | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3StopsByDistanceResponse**](V3StopsByDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json


## stopsStopsForRoute

> V3StopsOnRouteResponse stopsStopsForRoute(routeId, routeType, opts)

View all stops on a specific route

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.StopsApi();
let routeId = 56; // Number | Identifier of route; values returned by Routes API - v3/routes
let routeType = 56; // Number | Number identifying transport mode; values returned via RouteTypes API
let opts = {
  'directionId': 56, // Number | An optional direction; values returned by Directions API. When this is set, stop sequence information is returned in the response.
  'stopDisruptions': true, // Boolean | Indicates if stop disruption information will be returned (default = false)
  'includeGeopath': true, // Boolean | Indicates if geopath data will be returned (default = false)
  'geopathUtc': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter geopaths by date (ISO 8601 UTC format) (default = current date)
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.stopsStopsForRoute(routeId, routeType, opts, (error, data, response) => {
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
 **routeId** | **Number**| Identifier of route; values returned by Routes API - v3/routes | 
 **routeType** | **Number**| Number identifying transport mode; values returned via RouteTypes API | 
 **directionId** | **Number**| An optional direction; values returned by Directions API. When this is set, stop sequence information is returned in the response. | [optional] 
 **stopDisruptions** | **Boolean**| Indicates if stop disruption information will be returned (default &#x3D; false) | [optional] 
 **includeGeopath** | **Boolean**| Indicates if geopath data will be returned (default &#x3D; false) | [optional] 
 **geopathUtc** | **Date**| Filter geopaths by date (ISO 8601 UTC format) (default &#x3D; current date) | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3StopsOnRouteResponse**](V3StopsOnRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json

