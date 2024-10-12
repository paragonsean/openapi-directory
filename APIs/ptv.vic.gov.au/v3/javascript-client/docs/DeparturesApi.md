# PtvTimetableApiVersion3.DeparturesApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**departuresGetForStop**](DeparturesApi.md#departuresGetForStop) | **GET** /v3/departures/route_type/{route_type}/stop/{stop_id} | View departures for all routes from a stop
[**departuresGetForStopAndRoute**](DeparturesApi.md#departuresGetForStopAndRoute) | **GET** /v3/departures/route_type/{route_type}/stop/{stop_id}/route/{route_id} | View departures for a specific route from a stop



## departuresGetForStop

> V3DeparturesResponse departuresGetForStop(routeType, stopId, opts)

View departures for all routes from a stop

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.DeparturesApi();
let routeType = 56; // Number | Number identifying transport mode; values returned via RouteTypes API
let stopId = 56; // Number | Identifier of stop; values returned by Stops API
let opts = {
  'platformNumbers': [null], // [Number] | Filter by platform number at stop
  'directionId': 56, // Number | Filter by identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id}
  'gtfs': true, // Boolean | Indicates that stop_id parameter will accept \"GTFS stop_id\" data
  'dateUtc': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter by the date and time of the request (ISO 8601 UTC format) (default = current date and time)
  'maxResults': 56, // Number | Maximum number of results returned
  'includeCancelled': true, // Boolean | Indicates if cancelled services (if they exist) are returned (default = false) - metropolitan train only
  'lookBackwards': true, // Boolean | Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default = false). Requires max_results &gt; 0.
  'expand': ["null"], // [String] | List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.              Run must be expanded to receive VehiclePosition and VehicleDescriptor information.
  'includeGeopath': true, // Boolean | Indicates if the route geopath should be returned
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.departuresGetForStop(routeType, stopId, opts, (error, data, response) => {
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
 **routeType** | **Number**| Number identifying transport mode; values returned via RouteTypes API | 
 **stopId** | **Number**| Identifier of stop; values returned by Stops API | 
 **platformNumbers** | [**[Number]**](Number.md)| Filter by platform number at stop | [optional] 
 **directionId** | **Number**| Filter by identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id} | [optional] 
 **gtfs** | **Boolean**| Indicates that stop_id parameter will accept \&quot;GTFS stop_id\&quot; data | [optional] 
 **dateUtc** | **Date**| Filter by the date and time of the request (ISO 8601 UTC format) (default &#x3D; current date and time) | [optional] 
 **maxResults** | **Number**| Maximum number of results returned | [optional] 
 **includeCancelled** | **Boolean**| Indicates if cancelled services (if they exist) are returned (default &#x3D; false) - metropolitan train only | [optional] 
 **lookBackwards** | **Boolean**| Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default &#x3D; false). Requires max_results &amp;gt; 0. | [optional] 
 **expand** | [**[String]**](String.md)| List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.              Run must be expanded to receive VehiclePosition and VehicleDescriptor information. | [optional] 
 **includeGeopath** | **Boolean**| Indicates if the route geopath should be returned | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3DeparturesResponse**](V3DeparturesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json


## departuresGetForStopAndRoute

> V3DeparturesResponse departuresGetForStopAndRoute(routeType, stopId, routeId, opts)

View departures for a specific route from a stop

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.DeparturesApi();
let routeType = 56; // Number | Number identifying transport mode; values returned via RouteTypes API
let stopId = 56; // Number | Identifier of stop; values returned by Stops API
let routeId = "routeId_example"; // String | Identifier of route; values returned by Routes API - v3/routes
let opts = {
  'directionId': 56, // Number | Filter by identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id}
  'gtfs': true, // Boolean | Indicates that stop_id parameter will accept \"GTFS stop_id\" data
  'dateUtc': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter by the date and time of the request (ISO 8601 UTC format) (default = current date and time)
  'maxResults': 56, // Number | Maximum number of results returned
  'includeCancelled': true, // Boolean | Indicates if cancelled services (if they exist) are returned (default = false) - metropolitan train only
  'lookBackwards': true, // Boolean | Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default = false). Requires max_results &gt; 0.
  'expand': ["null"], // [String] | List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.              Run must be expanded to receive VehiclePosition and VehicleDescriptor information.
  'includeGeopath': true, // Boolean | Indicates if the route geopath should be returned
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.departuresGetForStopAndRoute(routeType, stopId, routeId, opts, (error, data, response) => {
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
 **routeType** | **Number**| Number identifying transport mode; values returned via RouteTypes API | 
 **stopId** | **Number**| Identifier of stop; values returned by Stops API | 
 **routeId** | **String**| Identifier of route; values returned by Routes API - v3/routes | 
 **directionId** | **Number**| Filter by identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id} | [optional] 
 **gtfs** | **Boolean**| Indicates that stop_id parameter will accept \&quot;GTFS stop_id\&quot; data | [optional] 
 **dateUtc** | **Date**| Filter by the date and time of the request (ISO 8601 UTC format) (default &#x3D; current date and time) | [optional] 
 **maxResults** | **Number**| Maximum number of results returned | [optional] 
 **includeCancelled** | **Boolean**| Indicates if cancelled services (if they exist) are returned (default &#x3D; false) - metropolitan train only | [optional] 
 **lookBackwards** | **Boolean**| Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default &#x3D; false). Requires max_results &amp;gt; 0. | [optional] 
 **expand** | [**[String]**](String.md)| List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.              Run must be expanded to receive VehiclePosition and VehicleDescriptor information. | [optional] 
 **includeGeopath** | **Boolean**| Indicates if the route geopath should be returned | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3DeparturesResponse**](V3DeparturesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json

