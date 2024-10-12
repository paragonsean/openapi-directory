# UebermapsApiEndpoints.EventsApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventsGet**](EventsApi.md#eventsGet) | **GET** /events | List your own events
[**eventsIdDelete**](EventsApi.md#eventsIdDelete) | **DELETE** /events/{id} | Delete event
[**eventsIdGet**](EventsApi.md#eventsIdGet) | **GET** /events/{id} | Get event
[**eventsIdPatch**](EventsApi.md#eventsIdPatch) | **PATCH** /events/{id} | Update event
[**spotsIdEventsGet**](EventsApi.md#spotsIdEventsGet) | **GET** /spots/{id}/events | List events for a given spot
[**spotsIdEventsPost**](EventsApi.md#spotsIdEventsPost) | **POST** /spots/{id}/events | Create event



## eventsGet

> [Event] eventsGet(opts)

List your own events

List your own events.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.EventsApi();
let opts = {
  'timeframeStart': "timeframeStart_example", // String | Begin of time range of event (ISO 8601 date format).
  'timeframeEnd': "timeframeEnd_example", // String | End of time range of event (ISO 8601 date format).
  'bounds': "bounds_example" // String | To refine your event index request to contain only events within                                                             a geographical box pass the followng bounds parameters.                                                             F. e. to get events within 'Hamburg, St. Pauli':                                                             bounds[sw_lat]=53.54831449741324                                                             bounds[sw_lon]=9.943227767944336                                                             bounds[ne_lat]=53.5571103674878                                                             bounds[ne_lon]=9.9776029586792
};
apiInstance.eventsGet(opts, (error, data, response) => {
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
 **timeframeStart** | **String**| Begin of time range of event (ISO 8601 date format). | [optional] 
 **timeframeEnd** | **String**| End of time range of event (ISO 8601 date format). | [optional] 
 **bounds** | **String**| To refine your event index request to contain only events within                                                             a geographical box pass the followng bounds parameters.                                                             F. e. to get events within &#39;Hamburg, St. Pauli&#39;:                                                             bounds[sw_lat]&#x3D;53.54831449741324                                                             bounds[sw_lon]&#x3D;9.943227767944336                                                             bounds[ne_lat]&#x3D;53.5571103674878                                                             bounds[ne_lon]&#x3D;9.9776029586792 | [optional] 

### Return type

[**[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventsIdDelete

> Event eventsIdDelete(id)

Delete event

Delete event.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.EventsApi();
let id = 56; // Number | Event id
apiInstance.eventsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| Event id | 

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventsIdGet

> Event eventsIdGet(id)

Get event

Get basic information about an event

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.EventsApi();
let id = 56; // Number | Id of event
apiInstance.eventsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of event | 

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventsIdPatch

> Map eventsIdPatch(id, opts)

Update event

Update event. Wrap event parameters in [event].

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.EventsApi();
let id = 56; // Number | Event id
let opts = {
  'event': new UebermapsApiEndpoints.EventEditable() // EventEditable | Event attributes
};
apiInstance.eventsIdPatch(id, opts, (error, data, response) => {
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
 **id** | **Number**| Event id | 
 **event** | [**EventEditable**](EventEditable.md)| Event attributes | [optional] 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## spotsIdEventsGet

> [Event] spotsIdEventsGet(id, opts)

List events for a given spot

List maps for a given spot.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.EventsApi();
let id = 56; // Number | Id of spot
let opts = {
  'timeframeStart': "timeframeStart_example", // String | Begin of time range of event (ISO 8601 date format).
  'timeframeEnd': "timeframeEnd_example", // String | End of time range of event (ISO 8601 date format).
  'bounds': "bounds_example" // String | To refine your event index request to contain only events within                                                             a geographical box pass the followng bounds parameters.                                                             F. e. to get events within 'Hamburg, St. Pauli':                                                             bounds[sw_lat]=53.54831449741324                                                             bounds[sw_lon]=9.943227767944336                                                             bounds[ne_lat]=53.5571103674878                                                             bounds[ne_lon]=9.9776029586792
};
apiInstance.spotsIdEventsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| Id of spot | 
 **timeframeStart** | **String**| Begin of time range of event (ISO 8601 date format). | [optional] 
 **timeframeEnd** | **String**| End of time range of event (ISO 8601 date format). | [optional] 
 **bounds** | **String**| To refine your event index request to contain only events within                                                             a geographical box pass the followng bounds parameters.                                                             F. e. to get events within &#39;Hamburg, St. Pauli&#39;:                                                             bounds[sw_lat]&#x3D;53.54831449741324                                                             bounds[sw_lon]&#x3D;9.943227767944336                                                             bounds[ne_lat]&#x3D;53.5571103674878                                                             bounds[ne_lon]&#x3D;9.9776029586792 | [optional] 

### Return type

[**[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spotsIdEventsPost

> Event spotsIdEventsPost(id, opts)

Create event

Create event. Wrap map parameters in [event].

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.EventsApi();
let id = 56; // Number | Spot id
let opts = {
  'event': new UebermapsApiEndpoints.EventEditable() // EventEditable | Event attributes
};
apiInstance.spotsIdEventsPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| Spot id | 
 **event** | [**EventEditable**](EventEditable.md)| Event attributes | [optional] 

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

