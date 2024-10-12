# PtvTimetableApiVersion3.PatternsApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patternsGetPatternByRun**](PatternsApi.md#patternsGetPatternByRun) | **GET** /v3/pattern/run/{run_ref}/route_type/{route_type} | View the stopping pattern for a specific trip/service run



## patternsGetPatternByRun

> V3StoppingPattern patternsGetPatternByRun(runRef, routeType, expand, opts)

View the stopping pattern for a specific trip/service run

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.PatternsApi();
let runRef = "runRef_example"; // String | The run_ref is the identifier of a run as returned by the departures/_* and runs/_* endpoints. WARNING, run_id is deprecated. Use run_ref instead.
let routeType = 56; // Number | Number identifying transport mode; values returned via RouteTypes API
let expand = ["null"]; // [String] | List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor and None. Default is Disruption. Run must be expanded to receive VehiclePosition and VehicleDescriptor information.
let opts = {
  'stopId': 56, // Number | Filter by stop_id; values returned by Stops API
  'dateUtc': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter by the date and time of the request (ISO 8601 UTC format)
  'includeSkippedStops': true, // Boolean | Include any skipped stops in a stopping pattern. Defaults to false.
  'includeGeopath': true, // Boolean | Indicates if geopath data will be returned (default = false)
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.patternsGetPatternByRun(runRef, routeType, expand, opts, (error, data, response) => {
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
 **runRef** | **String**| The run_ref is the identifier of a run as returned by the departures/_* and runs/_* endpoints. WARNING, run_id is deprecated. Use run_ref instead. | 
 **routeType** | **Number**| Number identifying transport mode; values returned via RouteTypes API | 
 **expand** | [**[String]**](String.md)| List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor and None. Default is Disruption. Run must be expanded to receive VehiclePosition and VehicleDescriptor information. | 
 **stopId** | **Number**| Filter by stop_id; values returned by Stops API | [optional] 
 **dateUtc** | **Date**| Filter by the date and time of the request (ISO 8601 UTC format) | [optional] 
 **includeSkippedStops** | **Boolean**| Include any skipped stops in a stopping pattern. Defaults to false. | [optional] 
 **includeGeopath** | **Boolean**| Indicates if geopath data will be returned (default &#x3D; false) | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3StoppingPattern**](V3StoppingPattern.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json

