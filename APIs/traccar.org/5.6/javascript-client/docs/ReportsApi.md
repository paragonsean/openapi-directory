# Traccar.ReportsApi

All URIs are relative to *https://demo.traccar.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportsEventsGet**](ReportsApi.md#reportsEventsGet) | **GET** /reports/events | Fetch a list of Events within the time period for the Devices or Groups
[**reportsRouteGet**](ReportsApi.md#reportsRouteGet) | **GET** /reports/route | Fetch a list of Positions within the time period for the Devices or Groups
[**reportsStopsGet**](ReportsApi.md#reportsStopsGet) | **GET** /reports/stops | Fetch a list of ReportStops within the time period for the Devices or Groups
[**reportsSummaryGet**](ReportsApi.md#reportsSummaryGet) | **GET** /reports/summary | Fetch a list of ReportSummary within the time period for the Devices or Groups
[**reportsTripsGet**](ReportsApi.md#reportsTripsGet) | **GET** /reports/trips | Fetch a list of ReportTrips within the time period for the Devices or Groups



## reportsEventsGet

> [Event] reportsEventsGet(from, to, opts)

Fetch a list of Events within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.ReportsApi();
let from = new Date("2013-10-20T19:20:30+01:00"); // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
let to = new Date("2013-10-20T19:20:30+01:00"); // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
let opts = {
  'deviceId': [null], // [Number] | 
  'groupId': [null], // [Number] | 
  'type': ["null"] // [String] | % can be used to return events of all types
};
apiInstance.reportsEventsGet(from, to, opts, (error, data, response) => {
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
 **from** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **to** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **deviceId** | [**[Number]**](Number.md)|  | [optional] 
 **groupId** | [**[Number]**](Number.md)|  | [optional] 
 **type** | [**[String]**](String.md)| % can be used to return events of all types | [optional] 

### Return type

[**[Event]**](Event.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet


## reportsRouteGet

> [Position] reportsRouteGet(from, to, opts)

Fetch a list of Positions within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.ReportsApi();
let from = new Date("2013-10-20T19:20:30+01:00"); // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
let to = new Date("2013-10-20T19:20:30+01:00"); // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
let opts = {
  'deviceId': [null], // [Number] | 
  'groupId': [null] // [Number] | 
};
apiInstance.reportsRouteGet(from, to, opts, (error, data, response) => {
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
 **from** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **to** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **deviceId** | [**[Number]**](Number.md)|  | [optional] 
 **groupId** | [**[Number]**](Number.md)|  | [optional] 

### Return type

[**[Position]**](Position.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet


## reportsStopsGet

> [ReportStops] reportsStopsGet(from, to, opts)

Fetch a list of ReportStops within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.ReportsApi();
let from = new Date("2013-10-20T19:20:30+01:00"); // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
let to = new Date("2013-10-20T19:20:30+01:00"); // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
let opts = {
  'deviceId': [null], // [Number] | 
  'groupId': [null] // [Number] | 
};
apiInstance.reportsStopsGet(from, to, opts, (error, data, response) => {
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
 **from** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **to** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **deviceId** | [**[Number]**](Number.md)|  | [optional] 
 **groupId** | [**[Number]**](Number.md)|  | [optional] 

### Return type

[**[ReportStops]**](ReportStops.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet


## reportsSummaryGet

> [ReportSummary] reportsSummaryGet(from, to, opts)

Fetch a list of ReportSummary within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.ReportsApi();
let from = new Date("2013-10-20T19:20:30+01:00"); // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
let to = new Date("2013-10-20T19:20:30+01:00"); // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
let opts = {
  'deviceId': [null], // [Number] | 
  'groupId': [null] // [Number] | 
};
apiInstance.reportsSummaryGet(from, to, opts, (error, data, response) => {
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
 **from** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **to** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **deviceId** | [**[Number]**](Number.md)|  | [optional] 
 **groupId** | [**[Number]**](Number.md)|  | [optional] 

### Return type

[**[ReportSummary]**](ReportSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet


## reportsTripsGet

> [ReportTrips] reportsTripsGet(from, to, opts)

Fetch a list of ReportTrips within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.ReportsApi();
let from = new Date("2013-10-20T19:20:30+01:00"); // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
let to = new Date("2013-10-20T19:20:30+01:00"); // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
let opts = {
  'deviceId': [null], // [Number] | 
  'groupId': [null] // [Number] | 
};
apiInstance.reportsTripsGet(from, to, opts, (error, data, response) => {
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
 **from** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **to** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **deviceId** | [**[Number]**](Number.md)|  | [optional] 
 **groupId** | [**[Number]**](Number.md)|  | [optional] 

### Return type

[**[ReportTrips]**](ReportTrips.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

