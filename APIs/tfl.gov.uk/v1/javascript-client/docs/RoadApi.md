# TransportForLondonUnifiedApi.RoadApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roadDisruptedStreets**](RoadApi.md#roadDisruptedStreets) | **GET** /Road/all/Street/Disruption | Gets a list of disrupted streets. If no date filters are provided, current disruptions are returned.
[**roadDisruption**](RoadApi.md#roadDisruption) | **GET** /Road/{ids}/Disruption | Get active disruptions, filtered by road ids
[**roadDisruptionById**](RoadApi.md#roadDisruptionById) | **GET** /Road/all/Disruption/{disruptionIds} | Gets a list of active disruptions filtered by disruption Ids.
[**roadGet**](RoadApi.md#roadGet) | **GET** /Road | Gets all roads managed by TfL
[**roadIdsGet**](RoadApi.md#roadIdsGet) | **GET** /Road/{ids} | Gets the road with the specified id (e.g. A1)
[**roadMetaCategories**](RoadApi.md#roadMetaCategories) | **GET** /Road/Meta/Categories | Gets a list of valid RoadDisruption categories
[**roadMetaSeverities**](RoadApi.md#roadMetaSeverities) | **GET** /Road/Meta/Severities | Gets a list of valid RoadDisruption severity codes
[**roadStatus**](RoadApi.md#roadStatus) | **GET** /Road/{ids}/Status | Gets the specified roads with the status aggregated over the date range specified, or now until the end of today if no dates are passed.



## roadDisruptedStreets

> Object roadDisruptedStreets(startDate, endDate)

Gets a list of disrupted streets. If no date filters are provided, current disruptions are returned.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.RoadApi();
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Optional, the start time to filter on.
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Optional, The end time to filter on.
apiInstance.roadDisruptedStreets(startDate, endDate, (error, data, response) => {
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
 **startDate** | **Date**| Optional, the start time to filter on. | 
 **endDate** | **Date**| Optional, The end time to filter on. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## roadDisruption

> [TflApiPresentationEntitiesRoadDisruption] roadDisruption(ids, opts)

Get active disruptions, filtered by road ids

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.RoadApi();
let ids = ["null"]; // [String] | Comma-separated list of road identifiers e.g. \"A406, A2\" use all for all to ignore id filter (a full list of supported road identifiers can be found at the /Road/ endpoint)
let opts = {
  'stripContent': true, // Boolean | Optional, defaults to false. When true, removes every property/node except for id, point, severity, severityDescription, startDate, endDate, corridor details, location, comments and streets
  'severities': ["null"], // [String] | an optional list of Severity names to filter on (a valid list of severities can be obtained from the /Road/Meta/severities endpoint)
  'categories': ["null"], // [String] | an optional list of category names to filter on (a valid list of categories can be obtained from the /Road/Meta/categories endpoint)
  'closures': true // Boolean | Optional, defaults to true. When true, always includes disruptions that have road closures, regardless of the severity filter. When false, the severity filter works as normal.
};
apiInstance.roadDisruption(ids, opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| Comma-separated list of road identifiers e.g. \&quot;A406, A2\&quot; use all for all to ignore id filter (a full list of supported road identifiers can be found at the /Road/ endpoint) | 
 **stripContent** | **Boolean**| Optional, defaults to false. When true, removes every property/node except for id, point, severity, severityDescription, startDate, endDate, corridor details, location, comments and streets | [optional] 
 **severities** | [**[String]**](String.md)| an optional list of Severity names to filter on (a valid list of severities can be obtained from the /Road/Meta/severities endpoint) | [optional] 
 **categories** | [**[String]**](String.md)| an optional list of category names to filter on (a valid list of categories can be obtained from the /Road/Meta/categories endpoint) | [optional] 
 **closures** | **Boolean**| Optional, defaults to true. When true, always includes disruptions that have road closures, regardless of the severity filter. When false, the severity filter works as normal. | [optional] 

### Return type

[**[TflApiPresentationEntitiesRoadDisruption]**](TflApiPresentationEntitiesRoadDisruption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/geo+json, application/json, application/xml, text/json, text/xml


## roadDisruptionById

> TflApiPresentationEntitiesRoadDisruption roadDisruptionById(disruptionIds, opts)

Gets a list of active disruptions filtered by disruption Ids.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.RoadApi();
let disruptionIds = ["null"]; // [String] | Comma-separated list of disruption identifiers to filter by.
let opts = {
  'stripContent': true // Boolean | Optional, defaults to false. When true, removes every property/node except for id, point, severity, severityDescription, startDate, endDate, corridor details, location and comments.
};
apiInstance.roadDisruptionById(disruptionIds, opts, (error, data, response) => {
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
 **disruptionIds** | [**[String]**](String.md)| Comma-separated list of disruption identifiers to filter by. | 
 **stripContent** | **Boolean**| Optional, defaults to false. When true, removes every property/node except for id, point, severity, severityDescription, startDate, endDate, corridor details, location and comments. | [optional] 

### Return type

[**TflApiPresentationEntitiesRoadDisruption**](TflApiPresentationEntitiesRoadDisruption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/geo+json, application/json, application/xml, text/json, text/xml


## roadGet

> [TflApiPresentationEntitiesRoadCorridor] roadGet()

Gets all roads managed by TfL

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.RoadApi();
apiInstance.roadGet((error, data, response) => {
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

[**[TflApiPresentationEntitiesRoadCorridor]**](TflApiPresentationEntitiesRoadCorridor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## roadIdsGet

> [TflApiPresentationEntitiesRoadCorridor] roadIdsGet(ids)

Gets the road with the specified id (e.g. A1)

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.RoadApi();
let ids = ["null"]; // [String] | Comma-separated list of road identifiers e.g. \"A406, A2\" (a full list of supported road identifiers can be found at the /Road/ endpoint)
apiInstance.roadIdsGet(ids, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| Comma-separated list of road identifiers e.g. \&quot;A406, A2\&quot; (a full list of supported road identifiers can be found at the /Road/ endpoint) | 

### Return type

[**[TflApiPresentationEntitiesRoadCorridor]**](TflApiPresentationEntitiesRoadCorridor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## roadMetaCategories

> [String] roadMetaCategories()

Gets a list of valid RoadDisruption categories

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.RoadApi();
apiInstance.roadMetaCategories((error, data, response) => {
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


## roadMetaSeverities

> [TflApiPresentationEntitiesStatusSeverity] roadMetaSeverities()

Gets a list of valid RoadDisruption severity codes

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.RoadApi();
apiInstance.roadMetaSeverities((error, data, response) => {
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


## roadStatus

> [TflApiPresentationEntitiesRoadCorridor] roadStatus(ids, opts)

Gets the specified roads with the status aggregated over the date range specified, or now until the end of today if no dates are passed.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.RoadApi();
let ids = ["null"]; // [String] | Comma-separated list of road identifiers e.g. \"A406, A2\" or use \"all\" to ignore id filter (a full list of supported road identifiers can be found at the /Road/ endpoint)
let opts = {
  'dateRangeNullableStartDate': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'dateRangeNullableEndDate': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.roadStatus(ids, opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| Comma-separated list of road identifiers e.g. \&quot;A406, A2\&quot; or use \&quot;all\&quot; to ignore id filter (a full list of supported road identifiers can be found at the /Road/ endpoint) | 
 **dateRangeNullableStartDate** | **Date**|  | [optional] 
 **dateRangeNullableEndDate** | **Date**|  | [optional] 

### Return type

[**[TflApiPresentationEntitiesRoadCorridor]**](TflApiPresentationEntitiesRoadCorridor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

