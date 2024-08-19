# TransportForLondonUnifiedApi.LineApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lineArrivals**](LineApi.md#lineArrivals) | **GET** /Line/{ids}/Arrivals/{stopPointId} | Get the list of arrival predictions for given line ids based at the given stop
[**lineDisruption**](LineApi.md#lineDisruption) | **GET** /Line/{ids}/Disruption | Get disruptions for the given line ids
[**lineDisruptionByMode**](LineApi.md#lineDisruptionByMode) | **GET** /Line/Mode/{modes}/Disruption | Get disruptions for all lines of the given modes.
[**lineGet**](LineApi.md#lineGet) | **GET** /Line/{ids} | Gets lines that match the specified line ids.
[**lineGetByMode**](LineApi.md#lineGetByMode) | **GET** /Line/Mode/{modes} | Gets lines that serve the given modes.
[**lineLineRoutesByIds**](LineApi.md#lineLineRoutesByIds) | **GET** /Line/{ids}/Route | Get all valid routes for given line ids, including the name and id of the originating and terminating stops for each route.
[**lineMetaDisruptionCategories**](LineApi.md#lineMetaDisruptionCategories) | **GET** /Line/Meta/DisruptionCategories | Gets a list of valid disruption categories
[**lineMetaModes**](LineApi.md#lineMetaModes) | **GET** /Line/Meta/Modes | Gets a list of valid modes
[**lineMetaServiceTypes**](LineApi.md#lineMetaServiceTypes) | **GET** /Line/Meta/ServiceTypes | Gets a list of valid ServiceTypes to filter on
[**lineMetaSeverity**](LineApi.md#lineMetaSeverity) | **GET** /Line/Meta/Severity | Gets a list of valid severity codes
[**lineRoute**](LineApi.md#lineRoute) | **GET** /Line/Route | Get all valid routes for all lines, including the name and id of the originating and terminating stops for each route.
[**lineRouteByMode**](LineApi.md#lineRouteByMode) | **GET** /Line/Mode/{modes}/Route | Gets all lines and their valid routes for given modes, including the name and id of the originating and terminating stops for each route
[**lineRouteSequence**](LineApi.md#lineRouteSequence) | **GET** /Line/{id}/Route/Sequence/{direction} | Gets all valid routes for given line id, including the sequence of stops on each route.
[**lineSearch**](LineApi.md#lineSearch) | **GET** /Line/Search/{query} | Search for lines or routes matching the query string
[**lineStatus**](LineApi.md#lineStatus) | **GET** /Line/{ids}/Status/{StartDate}/to/{EndDate} | Gets the line status for given line ids during the provided dates e.g Minor Delays
[**lineStatusByIds**](LineApi.md#lineStatusByIds) | **GET** /Line/{ids}/Status | Gets the line status of for given line ids e.g Minor Delays
[**lineStatusByMode**](LineApi.md#lineStatusByMode) | **GET** /Line/Mode/{modes}/Status | Gets the line status of for all lines for the given modes
[**lineStatusBySeverity**](LineApi.md#lineStatusBySeverity) | **GET** /Line/Status/{severity} | Gets the line status for all lines with a given severity              A list of valid severity codes can be obtained from a call to Line/Meta/Severity
[**lineStopPoints**](LineApi.md#lineStopPoints) | **GET** /Line/{id}/StopPoints | Gets a list of the stations that serve the given line id
[**lineTimetable**](LineApi.md#lineTimetable) | **GET** /Line/{id}/Timetable/{fromStopPointId} | Gets the timetable for a specified station on the give line
[**lineTimetableTo**](LineApi.md#lineTimetableTo) | **GET** /Line/{id}/Timetable/{fromStopPointId}/to/{toStopPointId} | Gets the timetable for a specified station on the give line with specified destination



## lineArrivals

> [TflApiPresentationEntitiesPrediction] lineArrivals(ids, stopPointId, opts)

Get the list of arrival predictions for given line ids based at the given stop

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let ids = ["null"]; // [String] | A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
let stopPointId = "stopPointId_example"; // String | Optional. Id of stop to get arrival predictions for (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
let opts = {
  'direction': "direction_example", // String | Optional. The direction of travel. Can be inbound or outbound or all. If left blank, and destinationStopId is set, will default to all
  'destinationStationId': "destinationStationId_example" // String | Optional. Id of destination stop
};
apiInstance.lineArrivals(ids, stopPointId, opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids. | 
 **stopPointId** | **String**| Optional. Id of stop to get arrival predictions for (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | 
 **direction** | **String**| Optional. The direction of travel. Can be inbound or outbound or all. If left blank, and destinationStopId is set, will default to all | [optional] 
 **destinationStationId** | **String**| Optional. Id of destination stop | [optional] 

### Return type

[**[TflApiPresentationEntitiesPrediction]**](TflApiPresentationEntitiesPrediction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineDisruption

> [TflApiPresentationEntitiesDisruption] lineDisruption(ids)

Get disruptions for the given line ids

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let ids = ["null"]; // [String] | A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
apiInstance.lineDisruption(ids, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids. | 

### Return type

[**[TflApiPresentationEntitiesDisruption]**](TflApiPresentationEntitiesDisruption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineDisruptionByMode

> [TflApiPresentationEntitiesDisruption] lineDisruptionByMode(modes)

Get disruptions for all lines of the given modes.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let modes = ["null"]; // [String] | A comma-separated list of modes e.g. tube,dlr
apiInstance.lineDisruptionByMode(modes, (error, data, response) => {
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
 **modes** | [**[String]**](String.md)| A comma-separated list of modes e.g. tube,dlr | 

### Return type

[**[TflApiPresentationEntitiesDisruption]**](TflApiPresentationEntitiesDisruption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineGet

> [TflApiPresentationEntitiesLine] lineGet(ids)

Gets lines that match the specified line ids.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let ids = ["null"]; // [String] | A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
apiInstance.lineGet(ids, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids. | 

### Return type

[**[TflApiPresentationEntitiesLine]**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineGetByMode

> [TflApiPresentationEntitiesLine] lineGetByMode(modes)

Gets lines that serve the given modes.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let modes = ["null"]; // [String] | A comma-separated list of modes e.g. tube,dlr
apiInstance.lineGetByMode(modes, (error, data, response) => {
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
 **modes** | [**[String]**](String.md)| A comma-separated list of modes e.g. tube,dlr | 

### Return type

[**[TflApiPresentationEntitiesLine]**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineLineRoutesByIds

> [TflApiPresentationEntitiesLine] lineLineRoutesByIds(ids, opts)

Get all valid routes for given line ids, including the name and id of the originating and terminating stops for each route.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let ids = ["null"]; // [String] | A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
let opts = {
  'serviceTypes': ["null"] // [String] | A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
};
apiInstance.lineLineRoutesByIds(ids, opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids. | 
 **serviceTypes** | [**[String]**](String.md)| A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] 

### Return type

[**[TflApiPresentationEntitiesLine]**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineMetaDisruptionCategories

> [String] lineMetaDisruptionCategories()

Gets a list of valid disruption categories

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
apiInstance.lineMetaDisruptionCategories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineMetaModes

> [TflApiPresentationEntitiesMode] lineMetaModes()

Gets a list of valid modes

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
apiInstance.lineMetaModes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[TflApiPresentationEntitiesMode]**](TflApiPresentationEntitiesMode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineMetaServiceTypes

> [String] lineMetaServiceTypes()

Gets a list of valid ServiceTypes to filter on

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
apiInstance.lineMetaServiceTypes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineMetaSeverity

> [TflApiPresentationEntitiesStatusSeverity] lineMetaSeverity()

Gets a list of valid severity codes

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
apiInstance.lineMetaSeverity((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[TflApiPresentationEntitiesStatusSeverity]**](TflApiPresentationEntitiesStatusSeverity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineRoute

> [TflApiPresentationEntitiesLine] lineRoute(opts)

Get all valid routes for all lines, including the name and id of the originating and terminating stops for each route.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let opts = {
  'serviceTypes': ["null"] // [String] | A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
};
apiInstance.lineRoute(opts, (error, data, response) => {
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
 **serviceTypes** | [**[String]**](String.md)| A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] 

### Return type

[**[TflApiPresentationEntitiesLine]**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineRouteByMode

> [TflApiPresentationEntitiesLine] lineRouteByMode(modes, opts)

Gets all lines and their valid routes for given modes, including the name and id of the originating and terminating stops for each route

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let modes = ["null"]; // [String] | A comma-separated list of modes e.g. tube,dlr
let opts = {
  'serviceTypes': ["null"] // [String] | A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
};
apiInstance.lineRouteByMode(modes, opts, (error, data, response) => {
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
 **modes** | [**[String]**](String.md)| A comma-separated list of modes e.g. tube,dlr | 
 **serviceTypes** | [**[String]**](String.md)| A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] 

### Return type

[**[TflApiPresentationEntitiesLine]**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineRouteSequence

> TflApiPresentationEntitiesRouteSequence lineRouteSequence(id, direction, opts)

Gets all valid routes for given line id, including the sequence of stops on each route.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let id = "id_example"; // String | A single line id e.g. victoria
let direction = "direction_example"; // String | The direction of travel. Can be inbound or outbound.
let opts = {
  'serviceTypes': ["null"], // [String] | A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
  'excludeCrowding': true // Boolean | That excludes crowding from line disruptions. Can be true or false.
};
apiInstance.lineRouteSequence(id, direction, opts, (error, data, response) => {
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
 **id** | **String**| A single line id e.g. victoria | 
 **direction** | **String**| The direction of travel. Can be inbound or outbound. | 
 **serviceTypes** | [**[String]**](String.md)| A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] 
 **excludeCrowding** | **Boolean**| That excludes crowding from line disruptions. Can be true or false. | [optional] 

### Return type

[**TflApiPresentationEntitiesRouteSequence**](TflApiPresentationEntitiesRouteSequence.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineSearch

> TflApiPresentationEntitiesRouteSearchResponse lineSearch(query, opts)

Search for lines or routes matching the query string

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let query = "query_example"; // String | Search term e.g victoria
let opts = {
  'modes': ["null"], // [String] | Optionally filter by the specified modes
  'serviceTypes': ["null"] // [String] | A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
};
apiInstance.lineSearch(query, opts, (error, data, response) => {
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
 **query** | **String**| Search term e.g victoria | 
 **modes** | [**[String]**](String.md)| Optionally filter by the specified modes | [optional] 
 **serviceTypes** | [**[String]**](String.md)| A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] 

### Return type

[**TflApiPresentationEntitiesRouteSearchResponse**](TflApiPresentationEntitiesRouteSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineStatus

> [TflApiPresentationEntitiesLine] lineStatus(ids, startDate, endDate, startDate2, endDate2, opts)

Gets the line status for given line ids during the provided dates e.g Minor Delays

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let ids = ["null"]; // [String] | A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
let startDate = "startDate_example"; // String | 
let endDate = "endDate_example"; // String | 
let startDate2 = "startDate_example"; // String | Automatically added
let endDate2 = "endDate_example"; // String | Automatically added
let opts = {
  'detail': true, // Boolean | Include details of the disruptions that are causing the line status including the affected stops and routes
  'dateRangeStartDate': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'dateRangeEndDate': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.lineStatus(ids, startDate, endDate, startDate2, endDate2, opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids. | 
 **startDate** | **String**|  | 
 **endDate** | **String**|  | 
 **startDate2** | **String**| Automatically added | 
 **endDate2** | **String**| Automatically added | 
 **detail** | **Boolean**| Include details of the disruptions that are causing the line status including the affected stops and routes | [optional] 
 **dateRangeStartDate** | **Date**|  | [optional] 
 **dateRangeEndDate** | **Date**|  | [optional] 

### Return type

[**[TflApiPresentationEntitiesLine]**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineStatusByIds

> [TflApiPresentationEntitiesLine] lineStatusByIds(ids, opts)

Gets the line status of for given line ids e.g Minor Delays

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let ids = ["null"]; // [String] | A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
let opts = {
  'detail': true // Boolean | Include details of the disruptions that are causing the line status including the affected stops and routes
};
apiInstance.lineStatusByIds(ids, opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids. | 
 **detail** | **Boolean**| Include details of the disruptions that are causing the line status including the affected stops and routes | [optional] 

### Return type

[**[TflApiPresentationEntitiesLine]**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineStatusByMode

> [TflApiPresentationEntitiesLine] lineStatusByMode(modes, opts)

Gets the line status of for all lines for the given modes

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let modes = ["null"]; // [String] | A comma-separated list of modes to filter by. e.g. tube,dlr
let opts = {
  'detail': true, // Boolean | Include details of the disruptions that are causing the line status including the affected stops and routes
  'severityLevel': "severityLevel_example" // String | If specified, ensures that only those line status(es) are returned within the lines that have disruptions with the matching severity level.
};
apiInstance.lineStatusByMode(modes, opts, (error, data, response) => {
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
 **modes** | [**[String]**](String.md)| A comma-separated list of modes to filter by. e.g. tube,dlr | 
 **detail** | **Boolean**| Include details of the disruptions that are causing the line status including the affected stops and routes | [optional] 
 **severityLevel** | **String**| If specified, ensures that only those line status(es) are returned within the lines that have disruptions with the matching severity level. | [optional] 

### Return type

[**[TflApiPresentationEntitiesLine]**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineStatusBySeverity

> [TflApiPresentationEntitiesLine] lineStatusBySeverity(severity)

Gets the line status for all lines with a given severity              A list of valid severity codes can be obtained from a call to Line/Meta/Severity

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let severity = 56; // Number | The level of severity (eg: a number from 0 to 14)
apiInstance.lineStatusBySeverity(severity, (error, data, response) => {
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
 **severity** | **Number**| The level of severity (eg: a number from 0 to 14) | 

### Return type

[**[TflApiPresentationEntitiesLine]**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineStopPoints

> [TflApiPresentationEntitiesStopPoint] lineStopPoints(id, opts)

Gets a list of the stations that serve the given line id

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let id = "id_example"; // String | A single line id e.g. victoria
let opts = {
  'tflOperatedNationalRailStationsOnly': true // Boolean | If the national-rail line is requested, this flag will filter the national rail stations so that only those operated by TfL are returned
};
apiInstance.lineStopPoints(id, opts, (error, data, response) => {
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
 **id** | **String**| A single line id e.g. victoria | 
 **tflOperatedNationalRailStationsOnly** | **Boolean**| If the national-rail line is requested, this flag will filter the national rail stations so that only those operated by TfL are returned | [optional] 

### Return type

[**[TflApiPresentationEntitiesStopPoint]**](TflApiPresentationEntitiesStopPoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineTimetable

> TflApiPresentationEntitiesTimetableResponse lineTimetable(fromStopPointId, id)

Gets the timetable for a specified station on the give line

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let fromStopPointId = "fromStopPointId_example"; // String | The originating station's stop point id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
let id = "id_example"; // String | A single line id e.g. victoria
apiInstance.lineTimetable(fromStopPointId, id, (error, data, response) => {
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
 **fromStopPointId** | **String**| The originating station&#39;s stop point id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | 
 **id** | **String**| A single line id e.g. victoria | 

### Return type

[**TflApiPresentationEntitiesTimetableResponse**](TflApiPresentationEntitiesTimetableResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## lineTimetableTo

> TflApiPresentationEntitiesTimetableResponse lineTimetableTo(fromStopPointId, id, toStopPointId)

Gets the timetable for a specified station on the give line with specified destination

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.LineApi();
let fromStopPointId = "fromStopPointId_example"; // String | The originating station's stop point id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
let id = "id_example"; // String | A single line id e.g. victoria
let toStopPointId = "toStopPointId_example"; // String | The destination stations's Naptan code
apiInstance.lineTimetableTo(fromStopPointId, id, toStopPointId, (error, data, response) => {
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
 **fromStopPointId** | **String**| The originating station&#39;s stop point id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | 
 **id** | **String**| A single line id e.g. victoria | 
 **toStopPointId** | **String**| The destination stations&#39;s Naptan code | 

### Return type

[**TflApiPresentationEntitiesTimetableResponse**](TflApiPresentationEntitiesTimetableResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

