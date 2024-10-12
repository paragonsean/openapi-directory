# PtvTimetableApiVersion3.RunsApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**runsForRoute**](RunsApi.md#runsForRoute) | **GET** /v3/runs/route/{route_id} | View all trip/service runs for a specific route ID
[**runsForRouteAndRouteType**](RunsApi.md#runsForRouteAndRouteType) | **GET** /v3/runs/route/{route_id}/route_type/{route_type} | View all trip/service runs for a specific route ID and route type
[**runsForRun**](RunsApi.md#runsForRun) | **GET** /v3/runs/{run_ref} | View all trip/service runs for a specific run_ref
[**runsForRunAndRouteType**](RunsApi.md#runsForRunAndRouteType) | **GET** /v3/runs/{run_ref}/route_type/{route_type} | View the trip/service run for a specific run_ref and route type



## runsForRoute

> V3RunsResponse runsForRoute(routeId, opts)

View all trip/service runs for a specific route ID

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.RunsApi();
let routeId = 56; // Number | Identifier of route; values returned by Routes API - v3/routes.
let opts = {
  'expand': ["null"], // [String] | List of objects to be returned in full (i.e. expanded) - options include: All, VehiclePosition, VehicleDescriptor, or None. Default is None.
  'dateUtc': new Date("2013-10-20T19:20:30+01:00"), // Date | Date of the request. (optional - defaults to now)
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.runsForRoute(routeId, opts, (error, data, response) => {
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
 **routeId** | **Number**| Identifier of route; values returned by Routes API - v3/routes. | 
 **expand** | [**[String]**](String.md)| List of objects to be returned in full (i.e. expanded) - options include: All, VehiclePosition, VehicleDescriptor, or None. Default is None. | [optional] 
 **dateUtc** | **Date**| Date of the request. (optional - defaults to now) | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3RunsResponse**](V3RunsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json


## runsForRouteAndRouteType

> V3RunsResponse runsForRouteAndRouteType(routeId, routeType, expand, opts)

View all trip/service runs for a specific route ID and route type

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.RunsApi();
let routeId = 56; // Number | Identifier of route; values returned by Routes API - v3/routes.
let routeType = 56; // Number | Number identifying transport mode; values returned via RouteTypes API
let expand = ["null"]; // [String] | List of objects to be returned in full (i.e. expanded) - options include: All, VehiclePosition, VehicleDescriptor, or None. Default is All.
let opts = {
  'dateUtc': new Date("2013-10-20T19:20:30+01:00"), // Date | Date of the request. (optional - defaults to now)
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.runsForRouteAndRouteType(routeId, routeType, expand, opts, (error, data, response) => {
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
 **routeId** | **Number**| Identifier of route; values returned by Routes API - v3/routes. | 
 **routeType** | **Number**| Number identifying transport mode; values returned via RouteTypes API | 
 **expand** | [**[String]**](String.md)| List of objects to be returned in full (i.e. expanded) - options include: All, VehiclePosition, VehicleDescriptor, or None. Default is All. | 
 **dateUtc** | **Date**| Date of the request. (optional - defaults to now) | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3RunsResponse**](V3RunsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json


## runsForRun

> V3RunsResponse runsForRun(runRef, expand, opts)

View all trip/service runs for a specific run_ref

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.RunsApi();
let runRef = "runRef_example"; // String | The run_ref is the identifier of a run as returned by the departures/_* and runs/_* endpoints. WARNING, run_id is deprecated. Use run_ref instead.
let expand = ["null"]; // [String] | List of objects to be returned in full (i.e. expanded) - options include: All, VehiclePosition, VehicleDescriptor, or None. Default is None.
let opts = {
  'dateUtc': new Date("2013-10-20T19:20:30+01:00"), // Date | Date of the request. (optional - defaults to now)
  'includeGeopath': true, // Boolean | Indicates if geopath data will be returned (default = false)
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.runsForRun(runRef, expand, opts, (error, data, response) => {
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
 **expand** | [**[String]**](String.md)| List of objects to be returned in full (i.e. expanded) - options include: All, VehiclePosition, VehicleDescriptor, or None. Default is None. | 
 **dateUtc** | **Date**| Date of the request. (optional - defaults to now) | [optional] 
 **includeGeopath** | **Boolean**| Indicates if geopath data will be returned (default &#x3D; false) | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3RunsResponse**](V3RunsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json


## runsForRunAndRouteType

> V3RunResponse runsForRunAndRouteType(runRef, routeType, expand, opts)

View the trip/service run for a specific run_ref and route type

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.RunsApi();
let runRef = "runRef_example"; // String | The run_ref is the identifier of a run as returned by the departures/_* and runs/_* endpoints. WARNING, run_id is deprecated. Use run_ref instead.
let routeType = 56; // Number | Number identifying transport mode; values returned via RouteTypes API
let expand = ["null"]; // [String] | List of objects to be returned in full (i.e. expanded) - options include: All, VehiclePosition, VehicleDescriptor, or None. Default is None.
let opts = {
  'dateUtc': new Date("2013-10-20T19:20:30+01:00"), // Date | Date of the request. (optional - defaults to now)
  'includeGeopath': true, // Boolean | Indicates if geopath data will be returned (default = false)
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.runsForRunAndRouteType(runRef, routeType, expand, opts, (error, data, response) => {
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
 **expand** | [**[String]**](String.md)| List of objects to be returned in full (i.e. expanded) - options include: All, VehiclePosition, VehicleDescriptor, or None. Default is None. | 
 **dateUtc** | **Date**| Date of the request. (optional - defaults to now) | [optional] 
 **includeGeopath** | **Boolean**| Indicates if geopath data will be returned (default &#x3D; false) | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3RunResponse**](V3RunResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json

